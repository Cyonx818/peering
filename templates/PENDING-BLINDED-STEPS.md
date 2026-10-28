# Pending blinded steps (held steps): human-readable view

File: `<path>.md` | View of `<path>.csv`, the only machine-read record | Only committer: Arbiter | Readable by every role (values-free by construction) | GUIDELINES R8.3, R8.4, R8.12, R8.17
<!-- KNOB: blinding. The CSV (`templates/PENDING-BLINDED-STEPS.csv`) is the record. This Markdown file is a view of it:
     regenerate it after every CSV change and never edit the table by hand. Both are in the human-readable set: they
     name WHAT is held, never a result, number, direction or category.
     The commit helper's --held-file option reads the CSV only (columns step_id, family, status). It refuses (exit 2)
     a missing or unreadable file, a non-CSV file and a CSV without those columns. A row is released only when its
     status is exactly `released`; any other value (including "not released", "Released" or an empty cell) is held.
     The helper commits and does not read data, so it does not use held_subject / holds_from; the data-reading
     tools (scorers, analysis tools, caches, intake) must match them (R8.17).
     Regenerate the view:
     python3 -c "import csv,sys; r=list(csv.reader(open(sys.argv[1]))); print('\n'.join('| '+' | '.join(x)+' |' for x in r[:1]+[['---']*len(r[0])]+r[1:]))" <path>.csv -->

Derivative files that quote an outcome of a held step (analysis notes, feel records, investigation sheets, summary rows) are held data too: list them under `held_paths` and include them in every read-list pre-scan (R8.1, R8.10). So are cache entries and generated digests built from data in a hold's scope (R6.15).

Every start command reads the CSV. Every scorer checks it. For each row: no class change, quick-reference row, ranking change or outcome-bearing file name for the family until release; neutral commit subject `Step <id>: scored and sealed (values withheld)`; start reports show `held (step <id>)`. Brief authors and readers pre-scan listed files for the step ids before reading with a count or file-name check, never a plain grep that prints the matching line: `grep -c -F -f <held-ids file> <file>` (or `grep -l`); for a line range, `sed -n '<a>,<b>p' <file> | grep -c -F -f <held-ids file>` (R8.10, R4.11). The `<held-ids file>` is one id per line, derived from the CSV's `step_id` and `family` columns, and carries ids only. Tools (scorers, analysis tools, intake, the commit helper) read the CSV from HEAD and refuse on a pending step; a tool that cannot read it refuses rather than proceeds (R8.17).

Columns of the CSV and of this view:

| step_id | family | held_paths (do not read in a visible session) | who_blinded | release_condition | status | held_subject | holds_from | peers_notified |
|---|---|---|---|---|---|---|---|---|
| <P-12> | <family id> | <sealed/P-12/; scores/P-12.csv> | <the human; Thinker> | <after the human's block-3 ratings are committed> | pending | <the subject's exact catalog id (R7.48)> | <ISO 8601 timestamp, e.g. 2026-01-31T12:00:00Z> | <roles and message ids> |

`held_subject` is the subject's exact catalog id (R7.48) and `holds_from` an ISO 8601 timestamp: together they are the machine-read scope of the later-data hold until the scoring run. `peers_notified` lists the roles told at registration and the message ids (R8.12). All three are values-free.

A datum is under a pending step when its path is in `held_paths`, or when its catalog subject equals `held_subject` and its catalog timestamp is at or after `holds_from`. A datum with no parseable catalog subject or time is refused while any row with a `held_subject` is pending, and so is any datum while a row has a `held_subject` with a blank or unparseable `holds_from` (fail closed, R8.17). A row from before v1.7 with both cells blank holds by `held_paths` only. The later-data hold is part of the held step, recorded here and released by the scoring run; it is not a hold in the sense of R3.12 and writes no holds-table row.
