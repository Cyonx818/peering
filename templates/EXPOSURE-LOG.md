# Exposure file: <role-id>

File: `exposure/<role-id>.md` | Only committer: <role-id> (one file per role, R2.7) | GUIDELINES R8.7
<!-- KNOB: blinding. Delete the folder if no step is ever blinded. -->

Append-only. One row per actor × exposure: who has seen which outcome data, through which channel. Actor-level; a per-datum status ledger, if pre-registration is on, is a separate file (`DATA-STATUS-LEDGER.md`, R7.12). Never edit a row; correct by a new row that points to the old one.

## Who writes
- **Every role logs its own exposure the moment it occurs**, whatever the channel: response, message, index row, brief read list, tool output, chat, metadata (commit subjects, file names, `git log` output).
- A role also logs the subagents it spawned that read outcome data (scorers, readers, decoders).
- The Arbiter logs its own exposures like any role, plus leaks it finds, and reconciles all files at each start. A leak to the human gets a row with actor = the human, written by the role that caused or found it.

## Why this exists
A confirmatory test is only blind if its predictor, scorer and scoring reviewer have not seen the outcomes. These files let every pre-registration answer "who is exposed to what" before choosing its actors.

Derivative files count (R8.1): an analysis note, feel record, investigation sheet or summary row that quotes an outcome, number, direction or category of a held step is held data like the raw datum, and reading one is an exposure.

## Rules
1. An exposed actor is never the predictor, the blind scorer or the reviewer of the scoring for that family.
2. A pre-registration lists every logged exposure of the actors it uses, including the predictor brief's author.
3. A leak to the human gets a row with actor = the human, and a §V deviation in the affected step.
4. A mid-task exposure (R8.8) records the step owner's ruling in the Consequence cell.
5. <!-- KNOB: high-risk --> Where the harness keeps tool-call transcripts, the Arbiter cross-checks declared reads against them; an undeclared read gets a new row and a §V deviation.
6. <!-- KNOB: high-risk --> Finer granularity (R8.7): a role that analyzes data may keep a per-computation log beside this file (one row per computation on a data file: date, file, family, what was printed, no values), so spent data is known exactly (R7.12).

## Log

| # | Date | Actor (role / session / subagent id) | Channel (response / message / index / brief read list / tool output / chat / metadata: commit subject, file name or `git log` output, R8.15) | What was seen (files, data, families; no values) | Declared in (file @ commit) | Consequence (what this actor may no longer do; ruling if mid-task) |
|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | <actor> | <channel> | <…> | <response header / record> | <e.g. not predictor, scorer or scoring reviewer for family Q3> |
