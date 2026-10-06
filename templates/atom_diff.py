#!/usr/bin/env python3
"""Atom diff for a record rewrite (peering framework v1.4; GUIDELINES R5.17, R5.7).

Lists the atoms (dates, ids, numbers, class words) that are present in the OLD
file and absent from the NEW file and from every --also file (for example the
drop ledger). Presence is by value, not by count: an atom that appears anywhere
in NEW or in an --also file counts as accounted for. It is the mechanical half of
a consolidation check; quotes, qualifiers and meaning belong to the reverse-read
(R7.36). Unit-attached numbers and reformatting give noise.

Usage:
    python3 atom_diff.py OLD NEW [--also FILE]... [--words WORD[,WORD...]]...
                         [--no-default-words] [--kinds-only]

Output (stdout), one line per missing atom, tab-separated:
    <kind>  <atom>  <old line numbers, comma-separated>
With --kinds-only the atom text is never printed (<kind>  <old line numbers>):
use it when the old file may carry a held value and the output is visible
(R5.17, R8.1). Normally redirect the output to a file and scan the file for held
ids (`grep -c -F -f <held-ids file> <out file>`, R8.10) before anyone reads it.

Atom kinds: date (YYYY-MM-DD), id (Letters-Digits, e.g. DEC-0003), number
(integer or decimal), word (a class word, case-insensitive, whole word).
Default class words: unknown, weak, strong, known, validated, lead, held,
deferred, released. Add your own with --words (project class and status words).

Exit codes: 0 no missing atoms; 1 at least one missing atom; 2 usage or read
error. Python 3.8+, standard library only.
"""

import argparse
import re
import sys

DEFAULT_WORDS = (
    "unknown", "weak", "strong", "known", "validated",
    "lead", "held", "deferred", "released",
)

# Order matters: a date or id is one atom and its digits are not counted again.
_ATOM_RE = re.compile(
    r"(?P<date>\b\d{4}-\d{2}-\d{2}\b)"
    r"|(?P<id>\b[A-Za-z]+-\d+\b)"
    r"|(?P<number>(?<![\w.])\d+(?:\.\d+)?)"
)


def extract_atoms(text, words=DEFAULT_WORDS):
    """Return {(kind, atom): [line numbers]} for the text (1-based lines)."""
    found = {}
    wordset = {w.lower() for w in words if w}
    word_re = None
    if wordset:
        word_re = re.compile(
            r"\b(" + "|".join(re.escape(w) for w in sorted(wordset)) + r")\b",
            re.IGNORECASE,
        )
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in _ATOM_RE.finditer(line):
            kind = m.lastgroup
            found.setdefault((kind, m.group(0)), []).append(lineno)
        if word_re is not None:
            for m in word_re.finditer(line):
                found.setdefault(("word", m.group(1).lower()), []).append(lineno)
    return found


def missing_atoms(old_text, new_texts, words=DEFAULT_WORDS):
    """Atoms of old_text found in none of new_texts; {(kind, atom): [lines]}."""
    old = extract_atoms(old_text, words)
    present = set()
    for t in new_texts:
        present.update(extract_atoms(t, words).keys())
    return {k: v for k, v in old.items() if k not in present}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def main(argv=None, out=None):
    out = out if out is not None else sys.stdout
    p = argparse.ArgumentParser(description="Atoms of OLD absent from NEW and --also files.")
    p.add_argument("old")
    p.add_argument("new")
    p.add_argument("--also", action="append", default=[], metavar="FILE",
                   help="another file that accounts for atoms (e.g. the drop ledger); repeatable")
    p.add_argument("--words", action="append", default=[], metavar="WORDS",
                   help="extra class words, comma-separated; repeatable")
    p.add_argument("--no-default-words", action="store_true",
                   help="use only the words given with --words")
    p.add_argument("--kinds-only", action="store_true",
                   help="never print the atom text, only kind and old line numbers")
    try:
        args = p.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code not in (0, None) else 0
    words = [] if args.no_default_words else list(DEFAULT_WORDS)
    for group in args.words:
        words.extend(w.strip() for w in group.split(",") if w.strip())
    try:
        old_text = _read(args.old)
        new_texts = [_read(args.new)] + [_read(f) for f in args.also]
    except (OSError, UnicodeDecodeError) as e:
        sys.stderr.write("atom_diff: cannot read input: %s\n" % e)
        return 2
    missing = missing_atoms(old_text, new_texts, words)
    for (kind, atom), lines in sorted(missing.items(), key=lambda kv: kv[1][0]):
        nums = ",".join(str(n) for n in sorted(set(lines)))
        if args.kinds_only:
            out.write("%s\t%s\n" % (kind, nums))
        else:
            out.write("%s\t%s\t%s\n" % (kind, atom, nums))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
