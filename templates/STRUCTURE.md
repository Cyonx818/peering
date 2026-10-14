# Structure: <PROJECT>

File: `<structure path>` | Owner: Arbiter | GUIDELINES R2.1–R2.5, R2.12–R2.15, R3.12, R5.16, R6.13, R7.23, R7.30, R7.34, R8.9
<!-- Lines tagged KNOB are optional; see GUIDELINES §15. -->

## 1. Layout
| Folder | Holds |
|---|---|
| `<docs>/` | rules, charter, goals, structure, status, methods, decision log |
| `peers/` | `outbox-<role>.md` per role |
| `<docs>/peer-comms-protocol.md` | the team roster, the sender check and the four message modes (R3.13); every role reads it at start; in the minimum |
| `<docs>/holds.csv` | the holds table (R3.12): one append-only CSV, in the minimum |
| `exposure/` <!-- KNOB: blinding --> | `<role>.md` per role |
| `<role>/journal-<date>.md` | each role's session journal |
| `<work>/<item>/` | the Operator's work folders |
| `<thinker folder>/` <!-- KNOB --> | briefs, responses, `HANDOFF.md` |
| `scripts/` | `commit_paths.py`, checks, tests |

## 2. Placement test (the file is … → it goes in …)
| The file is | It goes in | Template |
|---|---|---|
| a ruling by the human | a row in `<decision log>` | `DECISION-LOG.csv` |
| a role's memory of state | its handoff file | `HANDOFF-FILE.md` |
| a hold or a release by the human (R3.12) | a row in `<docs>/holds.csv` (append only; the receiving role appends it) | `HOLDS.csv` |
| a message with a `need:` | the sender's outbox, with its `mode:` | `OUTBOX.md` |
| the team roster, sender-check steps or message modes (R3.13) | `<docs>/peer-comms-protocol.md` (owner: Arbiter; roster rows change on the human's word) | `PEER-COMMS-PROTOCOL.md` |
| a prediction before data <!-- KNOB --> | `<evidence>/prereg/` | `PREREGISTRATION.md` |
| a review | `reviews/` | `REVIEW-REPORT.md` |
| a method document for a measurement or analysis (R7.30) | `<docs>/methods/`, with a pitfalls table | |
| the current cycle, next action per role, last full check (R5.16) | the now-file (≤ <40> lines), overwritten at every handoff | `NOW.md` |
| verbatim text that exists nowhere else and is clearly important, dropped from a current-state record (R5.16) | `<docs>/history/`, marked superseded, with a path-map row | |
| a consolidation record: question set, key, score, drop ledger, atom map (R5.17, R7.36) | the exploration folder | `CONSOLIDATION.md` |
| an investigation step file <!-- KNOB: investigation --> | `<evidence>/investigations/<date>-<topic>/` (append-only); `<topic>` names the question, never a direction or result (R8.4) | `INVESTIGATION.md`, `LENS-CARDS.md` |
| investigation scores <!-- KNOB: investigation --> | `<evidence>/investigations/ledger.csv` | `INVESTIGATION-LEDGER.csv` |
| a raw-data catalog (R10.9) <!-- KNOB: data intake --> | `<data>/catalog.csv` | |
| a lever-to-topic map (R6.13) | the method doc's "Lever-to-topic map" table, with the sentinel set (owner: Arbiter) | |
| pre-run rulings (R7.23) <!-- KNOB: evidence --> | beside the pre-registration's scorer, committed with it | |
| a fixture from a raw sample the human supplied (R7.34) | `scripts/fixtures/` for a promoted tool; the peer's own folder, beside its tool, before promotion (R2.13); byte for byte, marked "fixtures, not records" | |
| a peer-built tool, not yet promoted (R2.13) | the peer's own folder until the Arbiter promotes it (then `scripts/`, with a path-map row and a registry row, or a Key commands entry where the registry knob is off) | |
| a codebook for free-text reports, with its priors and agreement table (R7.40, R7.41) | `<docs>/methods/`, one file per codebook version (owner: Arbiter) | `CODEBOOK.md` |
| the per-round files of a blind inference of the human's report <!-- KNOB: blind report inference --> (R8.18) | the work item's folder holds the blind cells file and the score file; the words file and the prediction file live in a sealed location outside the working tree with only their sha256 committed until the cells are committed (R8.18); never merged into one file | `BLIND-INFERENCE-ROUND.md` |
| <…> | <…> | <…> |
| **no row fits** | **ask the Arbiter; add a row first** | |

## 3. Path map (moved paths and stubs)
| Old path | New path | Kind (moved / stub) | Remove when | Date, commit |
|---|---|---|---|---|
<!-- R2.3: a stub stays at the old path while something outside the repository still names it (a shared command repository, memory); `Remove when` states the condition. The repo check lists live stubs and blocks on a dangling one. -->

## 3b. Tool registry (R2.12) <!-- KNOB: tool registry. In the minimum the rules file's Key commands list is the registry. -->
| Tool | Command | Status (live / retired) | Tests | Owner role | Pinned? (R10.8) | Promotion runs (hash 1, hash 2; R2.13) |
|---|---|---|---|---|---|---|

## 3c. Record kinds, never-consolidated list and checker exemptions (R5.16, R2.15)
**Current-state records** (one row per subject, edited in place; may be consolidated): <status ledger, now-file, role handoffs, knowledge records, the human's preference record, indexes>.
**Event records, never consolidated:** frozen records, pre-registrations and test records, score records, journals, logs, Thinker pairs, append-only ledgers, the held list (CSV and view), the holds table, exposure logs, the decision log, outboxes, the frozen manifest, the data catalog and data-status ledger, the investigation ledger, <…>. A row of the held list or the holds table is never deleted (R2.4).

| Path or pattern the record checker exempts | Reason | Tested on a renamed copy? (date) |
|---|---|---|
<!-- R2.15: exact paths or tightly scoped patterns only; a date-, name- or suffix-based exemption is reviewed as High-risk. -->

## 4. Human-readable set (R8.9)
The files the human may open. During a held step every write to them passes the R8.2 check; results of a held step live only outside them. Mirror of the H column in `WRITE-SCOPES.md`.
- `git log` (commit subjects and bodies)
- <status file>, <decision log>, <READMEs>, <method docs>, <digests / generated reports>, <memory index>, <handoff files>

## 5. Frozen records and the frozen manifest
| Record | Freezes at | Correction route |
|---|---|---|
| pre-registration §A–§H <!-- KNOB --> | its commit | §V deviation block |
| decision-log rows | their commit | a new row with `supersedes` |
| exposure rows <!-- KNOB --> | their commit | a new row pointing to the old |
| §10 Review & corrections rows | their commit | a new row |
| investigation step files <!-- KNOB: investigation --> | their commit | a later numbered step file |
| pre-run rulings <!-- KNOB: evidence --> | their commit | clarifications appended before data only (R7.23) |
| <…> | <…> | <…> |

Manifest file `<frozen-manifest path>`: one line per frozen file, `<sha256>  <path>` (`shasum -a 256 <path>`). Passed to the commit helper with `--frozen-manifest`; the repo check verifies it at every start and before every commit (R2.5).
