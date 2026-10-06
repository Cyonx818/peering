# Status: <PROJECT>

File: `<status path>` | Only committer: Arbiter (others propose via outbox) | In the human-readable set (R8.9)
<!-- KNOB: status file. A LEDGER, not a log (R5.16): one row per subject, edited in place; a new fact edits the row
     and, if it moved a value, class, scope, direction or decision (flips labeled), appends one line to the Trajectory table.
     No dated sections, no "previous text" blocks, no [history] cells. The dated narrative lives in the record
     that is the event; the row points to it. State / Commit / Next action live in the now-file (`NOW.md`).
     During a held step: no result, direction or ranking change of that step here (R8.4). -->

## Ledger (one row per subject)

| Subject | Value (reader's units) | Scope | Status word (fixed list: <e.g. open / working / measured / retired>) | Class (R7.1) <!-- KNOB: evidence; without it delete the column --> | Pointer (record, commit) | Last changed |
|---|---|---|---|---|---|---|
| <subject> | <current value; qualifiers and negations stay inside the row> | <subject, conditions> | <word> | <class> | <path or commit> | <YYYY-MM-DD> |

Held families are shown as `held (step <id>)`, never with a value.

## Trajectory (flips only)

A row stays while its subject's row is live and the flip still bears on reading it; otherwise it is dropped at the next consolidation with a drop-ledger line (R5.16, R5.17). Verdict: the verdict word of the cited record, or `held (step <id>)` while that step is held (R8.4).

| Date | Subject | From → to | Cause | Verdict | Pointer |
|---|---|---|---|---|---|

## Open queue

| Rank | Item | Owner | Pointer |
|---|---|---|---|

## Unknowns

| Unknown | What would settle it | Pointer |
|---|---|---|

## Rules and rulings

The human's rulings are listed as decision-log ids (the log holds the verbatim words); verbatim copies here only in a project without a decision log, never paraphrased (R5.16, R7.31).

| Ruling | Source (decision-log id) |
|---|---|

## Automation runs <!-- KNOB: automation; or the standalone `AUTOMATION-RUNS.md` -->
| Job | Last run (date, commit) | Input since | Cost class |
|---|---|---|---|

## Thinker log <!-- KNOB: Thinker -->
One row per brief sent, per free-form discussion (≤ 5 lines, R4.8), and a disposition when the Arbiter acts on a response (R4.10); one disposition per response item (adopted / retired / open, with the surface it was wired to; R5.15).

| Date | Brief / discussion | Response | Exposure (pointer to row) | Disposition (adopted / overridden: reason / open; per item if mixed) |
|---|---|---|---|---|
