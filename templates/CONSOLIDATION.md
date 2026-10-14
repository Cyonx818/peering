# Consolidation record: <record being rewritten>

Two files. **Key file** (Parts 1-2): `<key folder>/<date>-consolidate-<record>-key.md`, in its own sealed folder outside the working tree, never in a folder the rewriter reads or writes. **Main file** (Parts 3-4): `<exploration folder>/<date>-consolidate-<record>.md`, citing the key only by commit and sha256. Written by: <role / subagent ids, one line per part> | GUIDELINES R5.16, R5.17, R7.36, R7.4, R6.11, R2.10
<!-- A consolidation or restructure of a current-state record (R5.16) is a rewrite, not a compression.
     HOW TO RUN. Form: full for any handoff, the status file, the now-file and any human-readable record; light only for
     small session records outside those (R7.36). Actors: the Arbiter launches four subagents, each staged in a fresh
     private folder with only its inputs (R6.11): question writer (old file), rewriter (old file; never the key folder),
     readers (one file each), scorer (key + answers). The question writer returns `written: <path> @ <sha256>` only;
     the orchestrator does not open the key. The key is CONVENTION-ENFORCED, not mechanical: staging, a Forbidden list in
     the rewriter's and readers' briefs, and the hash check are the guard; a rewriter that shows signs of having read it
     voids the test. Only the key's sha256 is committed before the rewrite; the key is committed with Part 3 after scoring.
     Terms: sentinel = a question on a value that flipped; trap = the superseded answer; key-literal / adjusted = score
     against the sealed key as written / corrected for repository changes since sealing, each correction proved by a command;
     via pointer = the answer points to a committed file that holds the fact.
     The rewrite is written to `<exploration folder>/<record>.candidate.md` and replaces the live record only in the commit
     after success. Held-step values never appear in any part (R8.5). Thresholds are starting values (e.g. 5 or 12-15 questions). -->

Old file: `<path>` @ `<commit>` (sha256 `<…>`) | New file: `<path>` (candidate: `<path>`) | Form: <light / full> (R7.36) | Key sealed: <sha256, date; key committed with Part 3 at <commit>>
Pre-checks (before the rewrite): `git cat-file -e <commit>:<path>` exit <0> and `git merge-base --is-ancestor <commit> HEAD` exit <0> (R5.17); held-ids count in the old file `grep -c -F -f <held-ids file> <old file>` = <n> (above 0: held rows copied verbatim as `held (step <id>)` and left out of the rewrite, or wait for release); the same count on the key before sealing = <0 required>.
Stage: <key sealed / rewrite written / readers done / scored / restored / committed> | Agent ids per stage: <…> (a start that finds the Record line `consolidating` reads the live record, never the candidate, and resumes at this stage)

## Part 1: Question set (key file; sealed before the rewrite)

| # | Question | Kind (current value / scope / row id / full-answer elements / qualifier / negation / "replaced" framing / formula / verbatim ruling) | Trap (the superseded value a careless reader would give as current) | Sentinel? (a value that flipped or splits by scope) |
|---|---|---|---|---|
| 1 | | | | |
| <n> | <one "not stated" question: the record does not say> | not stated | | |

Include at least one sentinel and one "not stated" question; aim questions at qualifiers, negations, "replaced" framings, formulas and verbatim rulings.

## Part 2: Answer key (key file; sealed with Part 1)

| # | Answer (current value, scope, row id) | Elements a full answer needs | Superseded value (flag if given as current) | Where in the old file (line) |
|---|---|---|---|---|

## Part 3: Score (main file; after the readers; separate scorer)

Readers: <old-file reader(s): an old file too large for one reader is split into parts, each with its own reader; per question the old score is the best score any part's reader achieved; new-file reader(s)>, each staged with one file only (R6.11). Scoring: full = 1, partial = 0.5, wrong = 0; a superseded value given as current is wrong and flagged. **Via pointer** scores as the target's content would score (full or partial) when the pointer resolves to a committed file, the fact is at the cited row or section, and the target is not itself an unscored output of this rewrite; otherwise 0; the scorer opens the target and cites the line. Absence claims are checked against the file, not the reader's word.

| # | Old: part | Old file: score | Old: flag | New file: key-literal | New: adjusted (proof command) | New: via pointer (target line) | New: flag | Reader "not blind"? |
|---|---|---|---|---|---|---|---|---|

Totals: old <x/n>; new key-literal <x/n>; new adjusted <x/n>. Success (R7.36): score(new) ≥ score(old) and zero flags on the new side. Adjustments are proved by a command each; the Arbiter rules which column applies: <ruling, date>. Lost facts restored: <ids>, at most two restore rounds (a fact still lost after the second goes to the Arbiter as open wire-in); re-read by a fresh reader (label "not blind" if told what was lost; such a read confirms only that the restored text is present and unambiguous and never adds to score(new)): <result>. Size is reported only: old <n> lines, new <n> lines (never a pass criterion, R6.7).

## Part 4: Drop ledger and atom map (main file; R5.17)

**Drop ledger** (every item recoverable at `<commit>`)

| Old line range | Item | Disposition (merged into row X / dropped: reason / moved to the history folder: path) |
|---|---|---|

**Atom map** (every class word and proof pointer of the old file)

| Atom (class word or proof pointer) | Old location | New location |
|---|---|---|

**Atom diff** (`python3 templates/atom_diff.py <old> <new> --also <ledger> [--words <class words>] > <out file>`, output to a file; scan the file for held ids with `grep -c -F -f <held-ids file> <out file>` before anyone reads it; the numbers and class words present in the old file and absent from the new file and the ledger): <list; each restored or ledgered, each ledger match confirmed by the reviewer (R5.17)>. Limits: a mention anywhere in the ledger clears an atom; unit-attached numbers and reformatting give noise; quotes and qualifiers are for the reverse-read.

Closing lines: no class was raised (per id, class(new) ≤ class(old); status words counted as classes): <confirmed by, date>. Held-step check: no held family's value appears in any part: <confirmed by, date>. Rulings found without a decision-log row, proposed for the Arbiter (R7.31): <ids or "none">.
