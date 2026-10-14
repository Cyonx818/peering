---
argument-hint: "<role-id>  (one of the roles or instances in <write-scopes path>; optional, the session detects its role when omitted)"
description: "<PROJECT>: end-of-session handoff for any role. Brings the role's handoff files current from the journal, verifies them, commits by explicit path through the helper, updates the outbox, releases the lease and prints the next start command."
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Edit, Write, Agent, Bash(git log:*), Bash(git status:*), Bash(git rev-parse:*), Bash(git diff:*), Bash(git cat-file:*), Bash(grep:*), Bash(cut -c1-240:*), Bash(<hash command>:*), Bash(python3 <scripts>/<check script>:*), Bash(python3 -m unittest:*), Bash(python3 <scripts>/atom_diff.py:*), Bash(python3 <scripts>/commit_paths.py:*)
---
<!--
Save as .claude/commands/<project>-handoff.md. One universal command; one branch per role.
Lines tagged KNOB are optional; see GUIDELINES §15. A branch for a role you do not run can be deleted.
Edit / Write are listed for direct-writer roles; an orchestrator role still edits nothing itself (R10.1).
-->

# <PROJECT> session handoff

**Purpose:** a fresh session of the same role must resume from files alone, as if it had just finished the last step. Everything it needs is in the role's handoff files when this command ends.

**Arguments:** `$ARGUMENTS`

## Standing rules (all roles)

| Rule | Detail |
|---|---|
| Integrity <!-- KNOB --> | `<hash command>` prints `<expected>`; no side-files; frozen manifest matches; at start and again before the commit. Else stop, report, commit nothing |
| Scope | A file outside the role's scope that needs a change becomes an outbox item for its owner |
| Blinding <!-- KNOB --> | Never decode, summarize or mention outcomes of a held step while closing out, in any visible channel: chat, tool output, subagent returns, commit subject or body, file names (R8.2). Neutral commit subject for a held step: `Step <id>: scored and sealed (values withheld)`. Subjects of every scored result are value-free whether or not a step is held (R8.15) |
| Facts | Every state line cites a commit hash or file; built from the journal and `git log`, not from conversation memory (R5.12); unverifiable = "unverified" |
| Commits | `python3 <scripts>/commit_paths.py --role <role-id> [--held-file <pending list>] [--frozen-manifest <manifest>] -m "<subject>" [-b "<body>"] -- <paths>`; never push or mention pushing |
| Peers | Messages per `templates/PEER-MESSAGE-PROTOCOL.md`: outbox row first, live notification second; tool missing → the outbox row is the delivery |
| Headroom | Run this with about a quarter of the context left (R5.13) |
| Holds | The holds table (`<holds table>`, R3.12) is the record of every hold; a hold you received this session is in it, an unconfirmed relayed one is listed first in your report and carried in your handoff §6 with its age; only the human releases a hold, in their own words, recorded verbatim. Open `owed:` journal lines (R9.17) go to "in flight" |
| Wire-in | Work is done only when reachable from its discovery surface (R5.15, core); each role wires what it may write; the rest is open wire-in with an owner; every handoff carries the "Wired this session" row and the "Open wire-in" table in its header ("none" is valid); items of a held family are listed only as `open wire-in: held (step <id>)` |

## Wire-in table (R5.15)

A row whose surface your project does not have: n/a.

| Item kind | Surface that must point to it | Owner |
|---|---|---|
| tool, script | command list in the rules file; the tool registry where that knob is on | Arbiter |
| rerunnable job | automation table (n/a where that knob is off) | Arbiter |
| general law or rule | quick-reference card or rules file | Arbiter |
| fact or lead | knowledge index; handoff §5 | Arbiter |
| method | methods folder | Arbiter |
| class change | the ledger row of that subject (a session note is not the record; R5.16) | Arbiter |
| Thinker response item | the Arbiter's handoff: one disposition per item (adopted / retired / open, with the surface it was wired to; R4.10) | Arbiter |
| closed design (failed premise; R5.18) | the ledger row of its subject: design, failed premise, evidence commit, what would reopen it | Arbiter |
| ruling | decision log, and every loaded standard, template or start fragment it contradicts (list them from the start command; grep each for the superseded rule's key terms; a writer subagent reads each against the ruling; record `contradiction check: <files>, <date>` in the Wired list) | Arbiter |
| new place or file kind | structure file and rules file | Arbiter |
| applied work item | the Operator's folder handoff | Operator |

## Step 1: determine the role

`$ARGUMENTS` names a role id → use it. Otherwise infer from the start command used, the lease (`commit_paths.py lease <role-id> --show`), the session name and the paths this session wrote, mapped through the columns of `<write-scopes path>`. Conflicting or no signals: ask "Which role is this session: <list of role ids>?" and wait; never guess. State the role in one line; run only its branch.

## Step 2 (Arbiter)

Orchestrator mode: gather facts, dispatch one writer, verify, check, commit.

1. Integrity check.
2. **Facts** (read-only): `git log --oneline <recorded HEAD>..HEAD`; `git status --porcelain`; the current §7 block; **the session journal** `<journal path>`. A numbered list, one commit or file per line: (a) commits and what each did; (b) state changes; (c) new leads; (d) re-ranked next actions and the single next action; (e) peers seen, names and harness ids; (f) open questions to the human; (g) in flight (pre-registered not run, awaiting scoring, sealed unopened, briefs without response, uncommitted work, outbox items not done, live subagents with output paths and checkpoints); (h) new DEC rows this session; (i) exposures logged this session.
3. **Data registration** <!-- KNOB: data intake -->: run the catalog checks; non-zero → dispatch a writer for the intake steps, or add "registration not current: <items>" to (g).
4. **Wire-in** (R5.15, table above): inventory the step-2 items plus the open wire-in items peers sent; read each peer handoff's open wire-in table directly, not only the peer's message, and list items older than one session first (R5.15); grep each item's discovery surface for its path or id; include a wire-in pass on each peer close or handoff commit since the last Arbiter handoff (one commit per peer close, the fixes named; R5.15), and for each new ruling with status `active` the contradiction check of the table above; unwired items inside the Arbiter's scope go to the writer as a wiring list; the others go to (g) with their owner. An item of a held family is listed only as `open wire-in: held (step <id>)`, never described, and is wired at release (R8.4).
5. **Handoff writer** (one, sequential; `templates/SUBAGENT-BRIEF.md`; pass paths, the fact list and the wiring list, not contents). Brief:
   - **edit rows in place** (R5.16): update the "Record" line (current as of, the commit holding the old version), the "Session state" table and the "Open wire-in" table ("Wired this session" and open wire-in, "none" stated explicitly); add **no** new header block, no dated section and no `[history]` block; delete superseded text (version control keeps it) but never a current value, scope, class word, pointer, qualifier, hold, exposure declaration or `held (step <id>)` marker, and never a held-list, holds-table or exposure-log row (R5.16); a Trajectory line in §7 only for a role-internal flip that still bears on reading the file (a value or class flip goes to the status ledger's trajectory); **copy every Class and status-word cell verbatim** unless the fact list names a class change with its proof commit; never raise one yourself; your Progress block (R6.3 exception) goes at the END of the file and is deleted before you return;
   - §1 row 6 "HEAD before the handoff commit" = current `git rev-parse --short HEAD`; §6 = the open rows of the holds table (id, state, release condition), or "none";
   - state rows with commits; leads in §5; ranking and next action; peers, names and harness ids in §0; open questions; in flight;
   - a §10 "Review & corrections" row only for a correction that still bears on how the file is read (R5.10);
   - **keep the heading order** of the template (the contract at the top of the file);
   - status ledger <!-- KNOB -->: edit the rows the session changed (value, scope, class, pointer, last changed) and append a trajectory line for a flip; the now-file (size guide `<40>` lines: current cycle, last session end, next action per role, last full check) is overwritten: it is the one record of the next action and the last session end, so the handoff's §7 and Session state point to it (R5.16); a Thinker-log row per brief sent and a disposition per response acted on (R4.10);
   - memory mirror <!-- KNOB: memory -->: copy the memory index and entries to `<docs>/memory-mirror/` (R11.9);
   - nothing else; re-run any data claim before writing it; return per R6.3.
6. **Verify** (changed regions only): `git diff --stat`; "Record" line date; §1 row 6 = `git rev-parse --short HEAD`; every (g) item present; every wire-in item grep-able on its surface or listed open with an owner; now-file matches; heading order intact (`grep -n '^## ' <handoff file>`, the contract's check: sections present in order, minimum set exists); **record gate** (R5.7): every current-state record the session edited keeps one row per subject and gained no dated section, judged on the lines the session added only (a diff against the **session-start commit**: the "Session start" line of the now-file, else the first journal line, else `git log -1 --format=%h -- <handoff file>`; pre-existing defects in a touched file go to open wire-in, never into this session's work). Gate options, run where the project adopts them (R5.7): (a) **class check**: diff the Class and status-word cells of every edited record against the session-start commit; any change not on the fact list is reverted, and any listed one goes to a reviewer (never for a held family, R8.4); (b) **atom diff**: `python3 <scripts>/atom_diff.py <old version> <new version> --also <ledger> > <out file>` for each edited current-state record (old = `git show <session-start commit>:<path>` saved to a file), output to a file and scanned for held ids (`grep -c -F -f <held-ids file> <out file>`) before anyone reads it; each removed number or class word is present in a replacing line or named in the commit body as `dropped: <item>: <reason>`, else restored. If this handoff consolidated, restructured or trimmed a record: the consolidation record is present, the key sealed, the success rule met (R7.36). Missing → one correction to the same writer, re-verify.
7. **Outbox:** mark items discharged by a peer's ack or commit `done <commit>`; add rows for anything a peer must act on.
8. **Checks:** `<repo checks>`; `<test suite>`. Gate on each check's own exit status or result line, never on a pipe such as `check | tail` (R10.4). Split failures into "in my paths" and "peer WIP: <path>". Failures go to in flight and the report; do not fix now unless asked. A record you edited links only targets that are committed or in this commit (R10.4).
9. Integrity check again; commit the handoff files, status, outbox and mirror through the helper. Subject `Handoff: end of Arbiter session <n> (<date>)`; body: what was verified, what remains open.
10. Release the lease: `commit_paths.py lease <role-id> --release`.
11. **Report** (≤ 10 lines): commit hash; next action; items waiting on the human; open wire-in count; **new DEC rows: <ids>** (so the human sees every row written in their name, R7.11); **rows below `verbatim`: "<id> recorded from <fidelity>: <decision, ≤ 1 line>; confirm or correct"** (R7.31); open holds, unconfirmed first; failed checks; then `Next session: <start command> [<focus>]`.

## Step 2 (Operator)

Direct writer, own scope only.

1. Integrity check.
2. Active work folder(s) this session touched; handle each.
3. **Wire-in** (R5.15): wire what the Operator may write; tools (each unpromoted tool the Operator built is an open wire-in item, R2.13), methods, rulings and laws are open wire-in items for the Arbiter.
4. **Now-file row** <!-- KNOB: status file -->: write the Operator's own "next action" row of `<now file>` (one helper call after the R2.8 dirty check, R2.7); the folder handoff points to it. **Folder handoff and next-session prompt** (`templates/OPERATOR-FOLDER-HANDOFF.md`): state (what the human confirmed vs. not; names only as the human saved them); next step with options and sources; the protocol that worked; tools, one line each; rules to keep (dose rule, the human states changes, naming); in flight (pre-registrations sent to the Arbiter and their status, sealed files, data not yet registered or scored, questions to the human; open wire-in items or "none"; corrections given to the human this session, R9.12). The next-session prompt only lists what to read. Every line cites a commit or file.
5. **Rulings and memory:** any ruling the human gave in this chat → an outbox item for the Arbiter with the human's verbatim words and the journal line they were copied from (R7.11, R7.31); any hold the human gave or confirmed → a row in the holds table (R3.12); any behavior correction → a memory proposal in the outbox (R11.7).
6. Records used: the folder's lessons notes (what worked, what did not), the human's preference record if preferences moved, the per-computation log (one line per data file looked at, so spent data is known, R7.12) <!-- KNOB: evidence -->.
7. Integrity check again; commit own files through the helper. Subject `<work item> <topic>: Operator close (<date>)`.
8. **Outbox and notification:** ≤ 3-line message to the Arbiter: item and commit; what changed; open wire-in items or "none"; what you need or "nothing pending".
9. Release the lease.
10. **Report** (≤ 8 lines): commit hash, the next step the human chose or must choose, then `Next session: <start command> <item id>`.

## Step 2 (Thinker) <!-- KNOB: Thinker -->

Read nothing new; write only in `<thinker folder>`.

1. Pair each `brief-<date>-<topic>.md` with its `response-<date>-<topic>.md`, and each open message request in the outbox (R3.6) that names an artifact @ hash (R4.1) with its response; a message request is the Arbiter's, carries no grants and no folder override, and any override needs a committed brief file with a held-ids pre-scan of 0 (R4.6).
2. **Exposure file** `exposure/thinker.md`: every exposure this session met, whatever the channel (response, message, index row, brief read list, tool output, chat, metadata: commit subjects, file names, `git log` output), has a row; append missing rows; never edit a row (R8.7).
3. **Wire-in** (R5.15): every insight or method in this session's responses is an open wire-in item for the Arbiter (response §, target surface); one that rests on a held family is listed only as `open wire-in: held (step <id>)`.
4. **`HANDOFF.md`** (`templates/THINKER-HANDOFF.md`, ≤ 40 non-blank lines, overwrite; its "On hold" section lists the open holds that bind this role, R3.12).
5. Commit only `HANDOFF.md`, the exposure file and your outbox through the helper. Responses are the Arbiter's to commit (R4.3) unless the Arbiter is unavailable (R1.7 a); name any uncommitted response in HANDOFF.md and the message.
6. **Outbox and notification** to the Arbiter, one line: commit hash plus any uncommitted response or pending question, and the open wire-in items.
7. Release the lease.
8. **Report** (≤ 5 lines), ending `Next session: <thinker start command>`.

## Error handling

| Condition | Action |
|---|---|
| Integrity failure | Stop; report; commit nothing |
| A file to update is missing | Create it from its template; say so |
| Helper exit 2 (refused) | Read the reason; fix the cause (path, held subject, frozen path, secret); never work around it |
| Helper exit 1 (hook or git failure) | Report the exact error; no `--no-verify`; leave the files for the human |
| Helper exit 3 (lock timeout) | Another session is committing; retry once after a minute, then report |
| Helper exit 4 (nothing to commit) | Check the path list against `git status`; report if the files are not what you expected |
| Peer offline | The outbox row is the delivery |
| Writer returned | Confirm it is idle and stop it if not; diff its write paths against the return (R6.14) |
| Writer stopped by quota | Resume it by id while this session lives; respawn with the partial file and its Progress block (at the end of a handoff file, R6.3 exception) only if resume fails (R6.5) |
| A check fails | Record in in flight and the report; do not fix silently |
| The harness blocks a destructive action (a delete) | Do not work around it; follow R10.9 (catalog, guarded script, the human runs it) |

Never finish without printing the next session's start command.
