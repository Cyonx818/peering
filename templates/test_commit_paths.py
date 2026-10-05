#!/usr/bin/env python3
"""Smoke tests for commit_paths.py (stdlib unittest; each test builds a throwaway repo in a temp dir).

Run: python3 -m unittest test_commit_paths   (from the folder holding both files)
"""

import fcntl
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
HELPER = os.path.join(HERE, "commit_paths.py")


def sh(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


class CommitPathsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = os.path.realpath(self.tmp.name)
        sh(["git", "init", "-q", "-b", "main"], self.repo)
        sh(["git", "config", "user.email", "test@example.invalid"], self.repo)
        sh(["git", "config", "user.name", "test"], self.repo)
        sh(["git", "config", "commit.gpgsign", "false"], self.repo)
        self.write("README.md", "seed\n")
        sh(["git", "add", "README.md"], self.repo)
        sh(["git", "commit", "-q", "-m", "seed"], self.repo)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        full = os.path.join(self.repo, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(text)

    def run_helper(self, *args, role="operator", env_extra=None):
        # The helper refuses a commit with no role or an unconfigured role (R2.5), so commit calls run with
        # PEERING_ROLE set to a configured role by default; pass role=None to run with none. Lease calls
        # never get a default role. The held-file variables are cleared so the suite does not depend on
        # the caller's environment; env_extra adds variables for one call.
        env = dict(os.environ)
        for name in ("PEERING_ROLE", "PEERING_HELD_FILE", "PEERING_REQUIRE_HELD_FILE"):
            env.pop(name, None)
        if role and not (args and args[0] == "lease"):
            env["PEERING_ROLE"] = role
        if env_extra:
            env.update(env_extra)
        return subprocess.run([sys.executable, HELPER] + list(args), cwd=self.repo,
                              capture_output=True, text=True, env=env)

    def log(self, fmt="%s"):
        return sh(["git", "log", "--format=" + fmt], self.repo).stdout

    def test_new_file_is_committed_alone(self):
        self.write("a.md", "a\n")
        self.write("other.md", "not mine\n")
        r = self.run_helper("--role", "arbiter", "-m", "Add a", "--", "a.md")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Add a", self.log())
        self.assertIn("Session-Role: arbiter", self.log("%B"))
        files = sh(["git", "show", "--name-only", "--format=", "HEAD"], self.repo).stdout.split()
        self.assertEqual(files, ["a.md"])
        self.assertIn("?? other.md", sh(["git", "status", "--porcelain"], self.repo).stdout)

    def test_no_role_refused_and_message_names_no_bypass(self):
        self.write("a.md", "a\n")
        r = self.run_helper("-m", "Add a", "--", "a.md", role=None)
        self.assertEqual(r.returncode, 2)
        self.assertIn("no role", r.stderr)
        self.assertNotIn("no-role", r.stderr)  # the refusal must not advertise the bypass
        self.assertIn("arbiter", r.stderr)  # it lists the configured roles instead
        self.assertNotIn("a.md", sh(["git", "ls-files"], self.repo).stdout)

    def test_no_role_with_reason_writes_a_visible_trailer(self):
        self.write("a.md", "a\n")
        r = self.run_helper("--no-role", "bootstrap before roles exist", "-m", "Add a", "--", "a.md", role=None)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Session-Role: none (bootstrap before roles exist)", self.log("%B"))

    def test_no_role_without_reason_refused(self):
        self.write("a.md", "a\n")
        r = self.run_helper("--no-role", "-m", "Add a", "--", "a.md", role=None)
        self.assertEqual(r.returncode, 2)
        self.assertIn("REASON", r.stderr)
        self.assertNotIn("a.md", sh(["git", "ls-files"], self.repo).stdout)

    def test_no_role_ignores_env_role_and_refuses_role_flag(self):
        self.write("a.md", "a\n")
        r = self.run_helper("--no-role", "bootstrap", "-m", "Add a", "--", "a.md")  # env role is "operator"
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Session-Role: none (bootstrap)", self.log("%B"))
        self.assertNotIn("Session-Role: operator", self.log("%B"))
        self.write("b.md", "b\n")
        r = self.run_helper("--role", "arbiter", "--no-role", "bootstrap", "-m", "Add b", "--", "b.md")
        self.assertEqual(r.returncode, 2)

    def test_unknown_role_refused(self):
        self.write("a.md", "a\n")
        r = self.run_helper("--role", "arbtier", "-m", "Add a", "--", "a.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("unknown role", r.stderr)
        r = self.run_helper("--role", "arbiter\nSession-Role: forged", "-m", "Add a", "--", "a.md")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("a.md", sh(["git", "ls-files"], self.repo).stdout)

    def test_unknown_env_role_refused(self):
        self.write("a.md", "a\n")
        r = self.run_helper("-m", "Add a", "--", "a.md", role="tester")
        self.assertEqual(r.returncode, 2)
        self.assertIn("PEERING_ROLE", r.stderr)
        self.assertNotIn("a.md", sh(["git", "ls-files"], self.repo).stdout)
        r = self.run_helper("-m", "Add a", "--", "a.md", role="thinker")  # a configured env role is accepted
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Session-Role: thinker", self.log("%B"))

    def test_held_file_env_fallback_and_required_mode(self):
        self.write("held.csv", "step_id,family,status\nP-12,F3,pending\n")
        self.write("score.md", "x\n")
        r = self.run_helper("-m", "Score P-12: FAIL", "--", "score.md", env_extra={"PEERING_HELD_FILE": "held.csv"})
        self.assertEqual(r.returncode, 2, "the env fallback must apply the held list")
        r = self.run_helper("-m", "Step P-12: scored", "--", "score.md", env_extra={"PEERING_REQUIRE_HELD_FILE": "1"})
        self.assertEqual(r.returncode, 2, "required mode must refuse a commit with no held list")
        self.assertIn("held list", r.stderr)
        self.assertNotIn("no-held-file", r.stderr)
        r = self.run_helper("--no-held-file", "-m", "Step P-12: scored", "--", "score.md",
                            env_extra={"PEERING_REQUIRE_HELD_FILE": "1"})
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_refuses_dot_glob_magic_and_directory(self):
        os.makedirs(os.path.join(self.repo, "d"))
        for bad in (".", "*.md", ":(glob)*", "d"):
            r = self.run_helper("-m", "x", "--", bad)
            self.assertEqual(r.returncode, 2, bad)

    def test_nothing_to_commit(self):
        r = self.run_helper("-m", "x", "--", "README.md")
        self.assertEqual(r.returncode, 4, r.stderr)

    def test_detached_head_refused(self):
        sh(["git", "checkout", "-q", "--detach"], self.repo)
        self.write("README.md", "changed\n")
        r = self.run_helper("-m", "x", "--", "README.md")
        self.assertEqual(r.returncode, 2)

    def test_pair_is_adjacent(self):
        self.write("prereg.md", "p\n")
        self.write("seal.md", "s\n")
        r = self.run_helper("-m", "Pre-register P-1", "--", "prereg.md", "--and", "-m", "Seal P-1", "--", "seal.md")
        self.assertEqual(r.returncode, 0, r.stderr)
        subjects = self.log().splitlines()
        self.assertEqual(subjects[:2], ["Seal P-1", "Pre-register P-1"])

    def test_frozen_path_change_refused(self):
        import hashlib
        digest = hashlib.sha256(b"seed\n").hexdigest()
        self.write("frozen.txt", "%s  README.md\n" % digest)
        self.write("README.md", "edited\n")
        r = self.run_helper("--frozen-manifest", "frozen.txt", "-m", "x", "--", "README.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("frozen", r.stderr)

    def test_held_step_verdict_refused_neutral_allowed(self):
        self.write("held.csv", "step_id,family,status\nP-12,F3,pending\n")
        self.write("score.md", "x\n")
        r = self.run_helper("--held-file", "held.csv", "-m", "Score P-12: FAIL", "--", "score.md")
        self.assertEqual(r.returncode, 2)
        r = self.run_helper("--held-file", "held.csv", "-m", "Score F3: B faster", "--", "score.md")
        self.assertEqual(r.returncode, 2)
        r = self.run_helper("--held-file", "held.csv", "-m", "Step P-12: scored and sealed (values withheld)", "--", "score.md")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_held_file_missing_refused(self):
        self.write("score.md", "x\n")
        r = self.run_helper("--held-file", "no-such.csv", "-m", "Step P-12: scored", "--", "score.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("not found", r.stderr)

    def test_held_file_non_csv_refused(self):
        self.write("held.md", "| Step id | Family | Status |\n|---|---|---|\n| P-12 | F3 | pending |\n")
        self.write("score.md", "x\n")
        r = self.run_helper("--held-file", "held.md", "-m", "Step P-12: scored and sealed (values withheld)", "--", "score.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("csv", r.stderr.lower())

    def test_held_file_without_required_columns_refused(self):
        self.write("held.csv", "id,state\nP-12,pending\n")
        self.write("score.md", "x\n")
        r = self.run_helper("--held-file", "held.csv", "-m", "Step P-12: scored and sealed (values withheld)", "--", "score.md")
        self.assertEqual(r.returncode, 2)

    def test_held_status_only_exact_released_frees_a_row(self):
        self.write("held.csv", "step_id,family,status\nP-12,F3,not released\nP-13,F4,released\nP-14,F5,\n")
        self.write("score.md", "x\n")
        r = self.run_helper("--held-file", "held.csv", "-m", "P-12 FAIL", "--", "score.md")
        self.assertEqual(r.returncode, 2, "'not released' must stay held")
        r = self.run_helper("--held-file", "held.csv", "-m", "P-14 FAIL", "--", "score.md")
        self.assertEqual(r.returncode, 2, "an empty status must stay held")
        r = self.run_helper("--held-file", "held.csv", "-m", "P-13 FAIL", "--", "score.md")
        self.assertEqual(r.returncode, 0, "an explicit 'released' row is free: " + r.stderr)

    def test_message_secret_refused(self):
        self.write("a.md", "a\n")
        r = self.run_helper("-m", "Add a", "-b", "token = 'ghp_" + "b" * 36 + "'", "--", "a.md")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("b" * 36, r.stderr)

    def test_lease_release_of_another_role_refused(self):
        self.assertEqual(self.run_helper("lease", "arbiter", "--name", "A1").returncode, 0)
        env = dict(os.environ, PEERING_ROLE="operator")
        r = subprocess.run([sys.executable, HELPER, "lease", "arbiter", "--release"], cwd=self.repo,
                           capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 2)
        self.assertEqual(self.run_helper("lease", "arbiter", "--name", "A2").returncode, 5)

    def test_secret_refused(self):
        self.write("notes.md", "token = 'ghp_" + "a" * 36 + "'\n")
        r = self.run_helper("-m", "x", "--", "notes.md")
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("a" * 36, r.stderr)

    def test_lock_timeout(self):
        common = sh(["git", "rev-parse", "--git-common-dir"], self.repo).stdout.strip()
        lock = open(os.path.join(self.repo, common, "peering-commit.lock"), "a+")
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            self.write("b.md", "b\n")
            r = self.run_helper("--timeout", "1", "-m", "x", "--", "b.md")
            self.assertEqual(r.returncode, 3)
        finally:
            lock.close()
        self.assertNotIn("b.md", sh(["git", "ls-files"], self.repo).stdout)

    def test_lease(self):
        self.assertEqual(self.run_helper("lease", "arbiter", "--name", "A1").returncode, 0)
        self.assertEqual(self.run_helper("lease", "arbiter", "--name", "A2").returncode, 5)
        self.assertEqual(self.run_helper("lease", "arbiter", "--name", "A2", "--force").returncode, 0)
        self.assertEqual(self.run_helper("lease", "arbiter", "--release").returncode, 0)
        self.assertEqual(self.run_helper("lease", "arbiter").returncode, 0)


if __name__ == "__main__":
    unittest.main()
