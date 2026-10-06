"""Tests for atom_diff.py (peering v1.4). Run: cd templates && python3 -m unittest test_atom_diff"""

import io
import os
import tempfile
import unittest

import atom_diff


class AtomDiffTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)

    def write(self, name, text):
        path = os.path.join(self.dir.name, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def run_main(self, *argv):
        buf = io.StringIO()
        code = atom_diff.main(list(argv), out=buf)
        return code, buf.getvalue()

    def test_number_missing_from_new(self):
        old = self.write("old.md", "speed 42 units\nlimit 7.5\n")
        new = self.write("new.md", "speed 42 units\n")
        code, out = self.run_main(old, new)
        self.assertEqual(code, 1)
        self.assertIn("number\t7.5\t2", out)
        self.assertNotIn("\t42\t", out)

    def test_nothing_missing_exit_zero(self):
        old = self.write("old.md", "alpha 3\n")
        new = self.write("new.md", "beta 3 and more\n")
        code, out = self.run_main(old, new)
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_also_file_accounts_for_atom(self):
        old = self.write("old.md", "value 99\n")
        new = self.write("new.md", "nothing here\n")
        ledger = self.write("ledger.md", "dropped 99: superseded\n")
        code, _ = self.run_main(old, new)
        self.assertEqual(code, 1)
        code, out = self.run_main(old, new, "--also", ledger)
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_class_word_case_insensitive_whole_word(self):
        old = self.write("old.md", "status: STRONG\nunknowing person\n")
        new = self.write("new.md", "status: weak\n")
        code, out = self.run_main(old, new)
        self.assertEqual(code, 1)
        self.assertIn("word\tstrong\t1", out)
        self.assertNotIn("unknown", out)  # "unknowing" is not a class word

    def test_class_word_present_in_new_is_accounted(self):
        old = self.write("old.md", "Known fact\n")
        new = self.write("new.md", "this is known\n")
        code, _ = self.run_main(old, new)
        self.assertEqual(code, 0)

    def test_extra_words_and_no_default_words(self):
        old = self.write("old.md", "phase habit\nstatus weak\n")
        new = self.write("new.md", "empty\n")
        code, out = self.run_main(old, new, "--words", "habit", "--no-default-words")
        self.assertEqual(code, 1)
        self.assertIn("word\thabit\t1", out)
        self.assertNotIn("weak", out)

    def test_date_and_id_are_single_atoms(self):
        old = self.write("old.md", "on 2026-10-06 see DEC-0003\n")
        new = self.write("new.md", "see DEC-0003\n")
        code, out = self.run_main(old, new)
        self.assertEqual(code, 1)
        self.assertIn("date\t2026-10-06\t1", out)
        self.assertNotIn("2026\t", out)  # the digits of a date are not separate numbers
        self.assertNotIn("DEC-0003", out)  # present in new

    def test_kinds_only_never_prints_atom_text(self):
        old = self.write("old.md", "secret value 12345\n")
        new = self.write("new.md", "gone\n")
        code, out = self.run_main(old, new, "--kinds-only")
        self.assertEqual(code, 1)
        self.assertNotIn("12345", out)
        self.assertIn("number\t1", out)

    def test_old_line_numbers_collected(self):
        old = self.write("old.md", "a 5\nb\nc 5\n")
        new = self.write("new.md", "x\n")
        code, out = self.run_main(old, new)
        self.assertEqual(code, 1)
        self.assertIn("number\t5\t1,3", out)

    def test_missing_file_exit_two(self):
        new = self.write("new.md", "x\n")
        code, out = self.run_main(os.path.join(self.dir.name, "nope.md"), new)
        self.assertEqual(code, 2)
        self.assertEqual(out, "")

    def test_presence_not_count(self):
        old = self.write("old.md", "7 and 7 and 7\n")
        new = self.write("new.md", "one 7\n")
        code, _ = self.run_main(old, new)
        self.assertEqual(code, 0)

    def test_extract_atoms_empty_text(self):
        self.assertEqual(atom_diff.extract_atoms(""), {})


if __name__ == "__main__":
    unittest.main()
