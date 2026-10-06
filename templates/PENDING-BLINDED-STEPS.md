# Pending blinded steps (held steps): human-readable view

File: `<path>.md` | View of `<path>.csv`, the only machine-read record | Only committer: Arbiter | Readable by every role (values-free by construction) | GUIDELINES R8.3, R8.4, R8.12, R8.17
<!-- KNOB: blinding. The CSV (`templates/PENDING-BLINDED-STEPS.csv`) is the record. This Markdown file is a view of it:
     regenerate it after every CSV change and never edit the table by hand. Both are in the human-readable set: they
     name WHAT is held, never a result, number, direction or category.
     The commit helper's --held-file option reads the CSV only (columns step_id, family, status). It refuses (exit 2)
     a missing or unreadable file, a non-CSV file and a CSV without those columns. A row is released only when its
     status is exactly `released`; any other value (including "not released" or an empty cell) is held.
     Regenerate the view:
     python3 -c "import csv,sys; r=list(csv.reader(open(sys.argv[1]))); print('\n'.join('| '+' | '.join(x)+' |' for x in r[:1]+[['---']*len(r[0])]+r[1:]))" <path>.csv -->

Derivative files that quote an outcome of a held step (analysis notes, feel records, investigation sheets, summary rows) are held data too: list them under `held_paths` and include them in every read-list pre-scan (R8.1, R8.10).

Every start command reads the CSV. Every scorer checks it. For each row: no class change, quick-reference row, ranking change or outcome-bearing file name for the family until release; neutral commit subject `Step <id>: scored and sealed (values withheld)`; start reports show `held (step <id>)`. Brief authors and readers pre-scan listed files for the step ids before reading with a count or file-name check, never a plain grep that prints the matching line: `grep -c -F -f <held-ids file> <file>` (or `grep -l`); for a line range, `sed -n '<a>,<b>p' <file> | grep -c -F -f <held-ids file>` (R8.10, R4.11). The `<held-ids file>` is one id per line, derived from the CSV's `step_id` and `family` columns, and carries ids only. Tools (scorers, analysis tools, intake, the commit helper) read the CSV from HEAD and refuse on a pending step; a tool that cannot read it refuses rather than proceeds (R8.17).

Columns of the CSV and of this view:

| step_id | family | held_paths (do not read in a visible session) | who_blinded | release_condition | status |
|---|---|---|---|---|---|
| <P-12> | <family id> | <sealed/P-12/; scores/P-12.csv> | <the human; Thinker> | <after the human's block-3 ratings are committed> | pending |
