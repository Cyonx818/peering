# Automation runs: <PROJECT>

File: `<path>` | Only committer: Arbiter | GUIDELINES R5.9, R2.12
<!-- KNOB: automation. One row per rerunnable job (a tool in the registry that turns new input into records).
     The start command's take-stock reads this file and reports "new since last run" per job (R5.9).
     If the status file's "Automation runs" table is enough for you, keep that instead and skip this file. -->

| Job | Tool (registry id) | Input it reads | Last run (date, commit) | New since last run (count, how found) | Cost class (cheap win / deep work) | Output record |
|---|---|---|---|---|---|---|
| <job> | <tool> | <folder or catalog> | <YYYY-MM-DD, hash> | <n; e.g. `git log --since` on the input folder, or files not in the catalog> | <class> | <path> |

Rules: a job runs only after the human chooses it at the start (R5.9); a run appends a row to its output record and updates "Last run" in the same commit; a tool that is not in the registry has no row here.
