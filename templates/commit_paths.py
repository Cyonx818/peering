#!/usr/bin/env python3
"""commit_paths.py: commit only the named paths, under a lock (peering framework v1.3).

Reference helper for GUIDELINES R10.2, R2.5, R7.8, R8.4, R10.7 and R1.8.
It uses only the Python standard library (3.8+) and POSIX file locks (macOS and Linux).
Copy it to <repo>/scripts/ and adjust the CONFIG block if you need to.

USAGE
  commit_paths.py [OPTIONS] -m SUBJECT [-b BODY] -- PATH [PATH ...]
  commit_paths.py [OPTIONS] -m S1 -- P1 ... --and -m S2 -- P2 ...    (adjacent pair, R7.8)
  commit_paths.py lease ROLE [--name NAME] [--max-age-hours H] [--force | --release | --show]

OPTIONS (before the first -m)
  --role ROLE            add the trailer "Session-Role: ROLE". ROLE must be one of the configured roles
                         (ROLES in the CONFIG block below); any other value is refused (exit 2).
                         Fallback when --role is absent: $PEERING_ROLE, validated the same way. Never
                         export PEERING_ROLE in a shell profile shared by several sessions (each session's
                         shell inherits it and every commit would carry one role); pass --role on every call.
  --no-role REASON       for a bootstrap commit before roles exist: write the trailer
                         "Session-Role: none (REASON)" so the bypass is visible in git log. REASON is
                         required and must be one line. It cannot be combined with --role, and it ignores
                         $PEERING_ROLE. Without a role the commit is refused (exit 2), so attribution
                         (R2.5) never lapses without a visible trailer.
  --branch NAME          refuse unless HEAD is on this branch (default: $PEERING_BRANCH, else any branch)
  --frozen-manifest F    refuse a change to any path listed in F ("<sha256>  <path>" lines)
  --no-held-file         only meaningful where REQUIRE_HELD_FILE is on: commit with no held list
  --held-file F          (default: $PEERING_HELD_FILE) the held list, a CSV (columns step_id, family, status;
                         GUIDELINES R8.17).
                         Refuse a subject or body that names a held step id or family id together with a
                         verdict word. Fails closed: a missing or unreadable file, a non-CSV file, a CSV
                         without the step_id and status columns, or a row without a step id is refused
                         (exit 2). A row is released only when its status is exactly "released"; any other
                         status, including "not released" or an empty cell, is held.
  --timeout SEC         lock and index.lock wait (default 60)
  --dry-run              validate and show what would be committed; change nothing

WHAT IT DOES
  1. Takes an exclusive flock on <git-common-dir>/peering-commit.lock. The OS releases a flock
     when the process dies, so a crash cannot deadlock the peers (an O_EXCL lock file can).
  2. Refuses: no role or an unconfigured role (see --role); where REQUIRE_HELD_FILE is on, no held list; no paths; ".", "..", directories, globs, ":" pathspec magic; paths outside the
     repository or inside .git; a detached HEAD; the wrong branch; changed frozen paths; likely
     secrets in the named files or in the message; verdict words next to a held step or family id
     in the message; an unreadable held list (see --held-file).
  3. Untracked files: "git add -N" (intent to add) for the named paths only, undone on failure.
     Plain "git commit --only -- <new file>" fails with "pathspec did not match".
  4. git commit --only -- <paths>. Never --no-verify. Retries while .git/index.lock exists.
  5. For a pair (--and), both commits happen under one lock hold and must be adjacent.

EXIT CODES
  0 committed (or dry run clean) | 1 git or hook failure, pair not adjacent | 2 refused
  3 lock timeout | 4 nothing to commit | 5 lease held by another live session

LIMITS (say these out loud in your rules file)
  - The role trailer is self-asserted: the session passes --role. It proves nothing about who ran it. The
    role list stops typos, not impersonation.
  - The holds table (GUIDELINES R3.12) is not read here: this helper commits, it does not read data.
  - Not implemented here (project options, GUIDELINES R2.5, R8.15): an append-only prefix guard for logs and
    ledgers, and a numeric tripwire for the subjects of scored-result commits.
  - It cannot tell whose edit a working-tree change is. "One committer per shared file" (R2.7) does that job.
  - The secret scan is a pattern list, not a guarantee.
  - The message check enforces R8.4 only (a held id next to a listed verdict word). R8.15 (no estimate,
    interval or direction in the subject of any scored result) is checked by the commit's author and by review.
  - "lease ROLE --release" is refused when $PEERING_ROLE is set and names another role; a forced or
    foreign release still needs the human's word (R1.8), so deny those forms in the harness.
"""

import csv
import datetime
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import time

# ---------------------------------------------------------------- CONFIG
# Role ids accepted by --role and $PEERING_ROLE (R2.5). Edit this list in the project's copy; add instance
# ids such as "operator:item-42" here only if you want them accepted as roles.
ROLES = ("arbiter", "operator", "thinker")
# Set True in the project's copy when the blinding knob is on: a commit with neither --held-file (or
# $PEERING_HELD_FILE) nor --no-held-file is then refused (R8.17), so a forgotten flag cannot skip the check.
REQUIRE_HELD_FILE = os.environ.get("PEERING_REQUIRE_HELD_FILE", "") == "1"
LOCK_NAME = "peering-commit.lock"
LEASE_DIR = os.path.join("peering", "leases")
MAX_SCAN_BYTES = 2 * 1024 * 1024
SECRET_PATTERNS = [
    ("private key block", re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("AWS access key id", re.compile(rb"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("Slack token", re.compile(rb"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("API secret key", re.compile(rb"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("password assignment", re.compile(rb"(?i)\b(password|passwd|secret|api_key|apikey|token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]")),
]
VERDICT_WORDS = re.compile(
    r"\b(PASS|PASSED|FAIL|FAILED|NC)\b|"
    r"(?i:\b(passes|fails|better|worse|confirmed|refuted|withdrawn|promoted|demoted|validated|"
    r"significant|resolved|improved|regressed|faster|slower|higher|lower|ahead|behind|supported|rejected|"
    r"consistent|inconsistent|marked|killed|wins)\b)"
)
# ---------------------------------------------------------------- END CONFIG

EXIT_OK, EXIT_GIT, EXIT_REFUSED, EXIT_LOCK, EXIT_NOTHING, EXIT_LEASE = 0, 1, 2, 3, 4, 5


class Refused(Exception):
    pass


def git(args, env=None):
    return subprocess.run(["git"] + args, capture_output=True, text=True, env=env)


def die(code, msg):
    sys.stderr.write("commit_paths: " + msg.rstrip() + "\n")
    sys.exit(code)


def repo_root():
    r = git(["rev-parse", "--show-toplevel"])
    if r.returncode != 0:
        die(EXIT_REFUSED, "not inside a git work tree")
    return os.path.realpath(r.stdout.strip())


def common_dir(root):
    r = git(["rev-parse", "--git-common-dir"])
    if r.returncode != 0:
        die(EXIT_GIT, r.stderr)
    d = r.stdout.strip()
    if not os.path.isabs(d):
        d = os.path.join(os.getcwd(), d)
    return os.path.realpath(d)


def take_lock(path, timeout):
    fh = open(path, "a+")
    deadline = time.time() + timeout
    while True:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fh
        except OSError:
            if time.time() >= deadline:
                fh.close()
                die(EXIT_LOCK, "lock timeout after %ss (%s); another session is committing" % (timeout, path))
            time.sleep(0.2)


def git_retry(args, timeout, env=None):
    """Run git, retrying while another git process holds index.lock."""
    deadline = time.time() + timeout
    delay = 0.2
    while True:
        r = git(args, env=env)
        if r.returncode == 0 or "index.lock" not in (r.stderr or ""):
            return r
        if time.time() >= deadline:
            return r
        time.sleep(delay)
        delay = min(delay * 2, 3.0)


# ---------------------------------------------------------------- argument parsing
def parse(argv):
    opts = {
        "role": os.environ.get("PEERING_ROLE", ""),
        "role_flag": False,
        "no_role": False,
        "no_role_reason": "",
        "branch": os.environ.get("PEERING_BRANCH", ""),
        "frozen": "",
        "held": os.environ.get("PEERING_HELD_FILE", ""),
        "no_held": False,
        "timeout": 60.0,
        "dry": False,
    }
    groups = []
    i = 0
    n = len(argv)
    value_opts = {"--role": "role", "--branch": "branch", "--frozen-manifest": "frozen",
                  "--held-file": "held", "--timeout": "timeout"}
    while i < n and argv[i] != "-m":
        a = argv[i]
        if a in value_opts:
            if i + 1 >= n:
                raise Refused("%s needs a value" % a)
            key = value_opts[a]
            opts[key] = float(argv[i + 1]) if key == "timeout" else argv[i + 1]
            if key == "role":
                opts["role_flag"] = True
            i += 2
        elif a == "--dry-run":
            opts["dry"] = True
            i += 1
        elif a == "--no-held-file":
            opts["no_held"] = True
            i += 1
        elif a == "--no-role":
            if i + 1 >= n or argv[i + 1].startswith("-"):
                raise Refused("--no-role needs a one-line REASON")
            opts["no_role"] = True
            opts["no_role_reason"] = argv[i + 1]
            i += 2
        elif a in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
        else:
            raise Refused("unknown option before -m: %r" % a)
    while i < n:
        if argv[i] != "-m" or i + 1 >= n:
            raise Refused("expected -m SUBJECT")
        subject = argv[i + 1]
        i += 2
        body = ""
        if i < n and argv[i] == "-b":
            if i + 1 >= n:
                raise Refused("-b needs a value")
            body = argv[i + 1]
            i += 2
        if i >= n or argv[i] != "--":
            raise Refused("expected -- before the paths")
        i += 1
        paths = []
        while i < n and argv[i] != "--and":
            paths.append(argv[i])
            i += 1
        if i < n and argv[i] == "--and":
            i += 1
        groups.append({"subject": subject, "body": body, "paths": paths})
    if not groups:
        raise Refused("no -m SUBJECT -- PATHS given")
    if len(groups) > 2:
        raise Refused("at most one --and (a pair)")
    if opts["no_role"]:
        reason = opts["no_role_reason"].strip()
        if opts["role_flag"]:
            raise Refused("--role and --no-role cannot be combined (R2.5)")
        if not reason or "\n" in reason or "\r" in reason:
            raise Refused("--no-role needs a one-line REASON (R2.5)")
        opts["role"] = ""  # $PEERING_ROLE is ignored; the trailer says "none"
        opts["trailer"] = "Session-Role: none (%s)" % reason
    else:
        role = opts["role"].strip()
        if not role:
            raise Refused("no role. Pass --role <%s> (R2.5)" % "|".join(ROLES))
        if role not in ROLES:
            source = "--role" if opts["role_flag"] else "PEERING_ROLE"
            raise Refused("unknown role %r from %s; configured roles: %s (R2.5)" % (role, source, ", ".join(ROLES)))
        opts["trailer"] = "Session-Role: " + role
    if REQUIRE_HELD_FILE and not opts["held"] and not opts["no_held"]:
        raise Refused("no held list: pass --held-file F or set PEERING_HELD_FILE (R8.17)")
    return opts, groups


# ---------------------------------------------------------------- checks
def normalise(root, p):
    if not p or p in (".", "..") or p.startswith(":"):
        raise Refused("refused path %r (no '.', '..', empty or ':' pathspec magic)" % p)
    if any(c in p for c in "*?["):
        raise Refused("refused path %r (no globs; name each file)" % p)
    absolute = os.path.realpath(p if os.path.isabs(p) else os.path.join(os.getcwd(), p))
    if absolute != root and not absolute.startswith(root + os.sep):
        raise Refused("refused path %r (outside the repository)" % p)
    rel = os.path.relpath(absolute, root)
    if rel == "." or rel.split(os.sep)[0] == ".git":
        raise Refused("refused path %r (repository root or .git)" % p)
    if os.path.isdir(absolute):
        raise Refused("refused path %r (a directory; name the files)" % p)
    return rel


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_frozen(root, manifest, rels):
    if not manifest:
        return
    mpath = manifest if os.path.isabs(manifest) else os.path.join(root, manifest)
    if not os.path.isfile(mpath):
        raise Refused("frozen manifest not found: %s" % manifest)
    frozen = {}
    with open(mpath, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                frozen[os.path.normpath(parts[1].strip())] = parts[0].lower()
    for rel in rels:
        want = frozen.get(os.path.normpath(rel))
        if want is None:
            continue
        full = os.path.join(root, rel)
        if not os.path.exists(full):
            raise Refused("frozen path deleted: %s" % rel)
        if sha256_file(full) != want:
            raise Refused("frozen path changed: %s (frozen records are append-only; write a new record)" % rel)


def held_ids(root, held):
    if not held:
        return []
    hpath = held if os.path.isabs(held) else os.path.join(root, held)
    # Fail closed (R8.17): a list that cannot be read as a CSV is a refusal, never an empty list.
    if not os.path.isfile(hpath):
        raise Refused("held file not found: %s (R8.17: refuse when the held list cannot be read)" % held)
    if not hpath.lower().endswith(".csv"):
        raise Refused("held file %s is not a .csv; the held list is machine-read as CSV only (R8.17)" % held)
    ids = []
    try:
        with open(hpath, encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            names = [(n or "").strip().lower() for n in (reader.fieldnames or [])]
            if "step_id" not in names or "status" not in names:
                raise Refused("held file %s needs the columns step_id and status (R8.17)" % held)
            for row in reader:
                row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items() if k is not None}
                if not any(row.values()):
                    continue
                sid = row.get("step_id", "").strip("`*")
                if not sid:
                    raise Refused("held file %s has a row without a step_id (R8.17)" % held)
                if row.get("status", "").lower() == "released":
                    continue
                ids.append(sid)
                fam = row.get("family", "").strip("`*")
                if fam and fam not in ids:
                    ids.append(fam)
    except (OSError, UnicodeDecodeError, csv.Error) as e:
        raise Refused("held file %s is unreadable: %s (R8.17)" % (held, e))
    return ids


def check_message_secrets(groups):
    for g in groups:
        data = (g["subject"] + "\n" + g["body"]).encode("utf-8", "replace")
        for name, pat in SECRET_PATTERNS:
            if pat.search(data):
                raise Refused("possible secret (%s) in the commit message; refer to secrets by store or variable name (R10.7)" % name)


def check_message(groups, ids):
    for g in groups:
        text = g["subject"] + "\n" + g["body"]
        for sid in ids:
            if re.search(r"(?<![\w-])" + re.escape(sid) + r"(?![\w-])", text) and VERDICT_WORDS.search(text):
                raise Refused(
                    "message names held step %s together with a verdict word; use the neutral form "
                    "'Step %s: scored and sealed (values withheld)' (GUIDELINES R8.4)" % (sid, sid))


def check_secrets(root, rels):
    for rel in rels:
        full = os.path.join(root, rel)
        if not os.path.isfile(full) or os.path.getsize(full) > MAX_SCAN_BYTES:
            continue
        with open(full, "rb") as fh:
            data = fh.read()
        for name, pat in SECRET_PATTERNS:
            if pat.search(data):
                raise Refused("possible secret (%s) in %s; refer to secrets by store or variable name (R10.7)" % (name, rel))


def check_head(branch):
    r = git(["symbolic-ref", "-q", "--short", "HEAD"])
    if r.returncode != 0:
        raise Refused("detached HEAD; check out a branch first (never commit on a detached HEAD)")
    current = r.stdout.strip()
    if branch and current != branch:
        raise Refused("on branch %r, expected %r" % (current, branch))
    return current


def is_tracked(rel):
    return git(["ls-files", "--error-unmatch", "--", rel]).returncode == 0


# ---------------------------------------------------------------- commit
def commit_group(root, opts, g, env):
    rels = g["paths"]
    added_n = []
    for rel in rels:
        if not is_tracked(rel):
            if not os.path.exists(os.path.join(root, rel)):
                raise Refused("no such path and not tracked: %s" % rel)
            if not opts["dry"]:
                r = git_retry(["add", "-N", "--", rel], opts["timeout"])
                if r.returncode != 0:
                    undo(added_n)
                    die(EXIT_GIT, "git add -N failed for %s: %s" % (rel, r.stderr))
            added_n.append(rel)
    status = git(["status", "--porcelain", "--"] + rels).stdout.strip()
    if not status:
        undo(added_n)
        return None
    if opts["dry"]:
        print("dry run: would commit %r:" % g["subject"])
        print(status)
        return "dry-run"
    args = ["commit", "--only", "-m", g["subject"]]
    if g["body"]:
        args += ["-m", g["body"]]
    args += ["-m", opts["trailer"]]
    args += ["--"] + rels
    r = git_retry(args, opts["timeout"], env=env)
    if r.returncode != 0:
        undo(added_n)
        die(EXIT_GIT, "git commit failed (no --no-verify; fix the cause):\n" + (r.stdout or "") + (r.stderr or ""))
    return git(["rev-parse", "--short", "HEAD"]).stdout.strip()


def undo(added_n):
    for rel in added_n:
        git(["reset", "-q", "--", rel])


def run_commit(argv):
    try:
        opts, groups = parse(argv)
    except Refused as e:
        die(EXIT_REFUSED, str(e))
    root = repo_root()
    os.chdir(root)
    lock = take_lock(os.path.join(common_dir(root), LOCK_NAME), opts["timeout"])
    try:
        try:
            check_head(opts["branch"])
            for g in groups:
                if not g["paths"]:
                    raise Refused("no paths for %r" % g["subject"])
                if not g["subject"].strip():
                    raise Refused("empty subject")
                g["paths"] = [normalise(root, p) for p in g["paths"]]
                check_frozen(root, opts["frozen"], g["paths"])
                check_secrets(root, g["paths"])
            check_message_secrets(groups)
            check_message(groups, held_ids(root, opts["held"]))
        except Refused as e:
            die(EXIT_REFUSED, str(e))
        env = dict(os.environ)
        env["PEERING_ROLE"] = opts["role"] or "none"
        made = []
        for idx, g in enumerate(groups):
            before = git(["rev-parse", "HEAD"]).stdout.strip()
            if idx == 1 and made and made[0] != "dry-run":
                if git(["rev-parse", "--short", "HEAD"]).stdout.strip() != made[0]:
                    die(EXIT_GIT, "pair void: another commit landed after %s" % made[0])
            try:
                h = commit_group(root, opts, g, env)
            except Refused as e:
                die(EXIT_REFUSED, str(e))
            if h is None:
                if made:
                    die(EXIT_NOTHING, "first commit %s made; second group had nothing to commit (pair incomplete)" % made[0])
                die(EXIT_NOTHING, "nothing to commit for %r" % g["subject"])
            if idx == 1 and h != "dry-run":
                parent = git(["rev-parse", "HEAD~1"]).stdout.strip()
                if parent != before:
                    die(EXIT_GIT, "pair void: commits not adjacent")
            made.append(h)
        for h, g in zip(made, groups):
            print("committed %s %s (%d path(s))" % (h, g["subject"], len(g["paths"])))
        return EXIT_OK
    finally:
        lock.close()


# ---------------------------------------------------------------- lease (one live session per role instance, R1.8)
def run_lease(argv):
    if not argv or argv[0].startswith("-"):
        die(EXIT_REFUSED, "usage: commit_paths.py lease ROLE [--name NAME] [--max-age-hours H] [--force|--release|--show]")
    role = argv[0]
    name, max_age, mode = "", 12.0, "acquire"
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--name" and i + 1 < len(argv):
            name, i = argv[i + 1], i + 2
        elif a == "--max-age-hours" and i + 1 < len(argv):
            max_age, i = float(argv[i + 1]), i + 2
        elif a in ("--force", "--release", "--show"):
            mode, i = a[2:], i + 1
        else:
            die(EXIT_REFUSED, "unknown lease option %r" % a)
    root = repo_root()
    cdir = common_dir(root)
    ldir = os.path.join(cdir, LEASE_DIR)
    os.makedirs(ldir, exist_ok=True)
    path = os.path.join(ldir, re.sub(r"[^A-Za-z0-9_.-]", "_", role) + ".json")
    lock = take_lock(os.path.join(cdir, LOCK_NAME), 30)
    try:
        held = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                held = json.load(fh)
        now = datetime.datetime.now(datetime.timezone.utc)
        if mode == "show":
            print(json.dumps(held) if held else "no lease for %s" % role)
            return EXIT_OK
        if mode == "release":
            caller = os.environ.get("PEERING_ROLE", "")
            if caller and caller != role:
                die(EXIT_REFUSED, "refused: PEERING_ROLE is %r, cannot release the lease of %r (R1.8: the human decides)" % (caller, role))
            if held:
                os.remove(path)
            print("released lease for %s" % role)
            return EXIT_OK
        if held and mode != "force":
            started = datetime.datetime.fromisoformat(held["started"])
            age_h = (now - started).total_seconds() / 3600.0
            if age_h < max_age:
                print("lease held: role %s, session %r, started %s (%.1f h ago)" % (
                    role, held.get("name", ""), held["started"], age_h))
                print("Ask the human whether that session is still open. Continue only on their word, with --force.")
                return EXIT_LEASE
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"role": role, "name": name, "started": now.isoformat(timespec="seconds")}, fh)
        print("lease acquired for %s%s" % (role, (" (" + name + ")") if name else ""))
        return EXIT_OK
    finally:
        lock.close()


def main(argv):
    if argv and argv[0] == "lease":
        return run_lease(argv[1:])
    return run_commit(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
