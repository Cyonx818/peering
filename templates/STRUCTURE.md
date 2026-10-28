# Structure: <PROJECT>

File: `<structure path>` | Owner: Arbiter | GUIDELINES R2.1–R2.5, R2.12–R2.15, R3.12, R5.16, R6.13, R7.23, R7.30, R7.34, R8.9, R9.24, R9.26, R9.27
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
| a multi-phase build memo: decisions with fallbacks, vetting table, per-phase rulings (R4.16) | `<docs>/plans/`, marked superseded when consolidated into the method doc | `BUILD-PLAN.md` |
| the command that walks the human through what waits on them (R9.24) | `<project>-queue` command file; its sources are the files it declares | `HUMAN-QUEUE-COMMAND.md` |
| an initiative register, where more than one initiative shares the repository (R2.21) | `<docs>/initiatives.csv` (id, name, goal, owner, state, pointer; an id family of its own; backfilled rows keep their written date and source line) | |
| a record that holds several runs (R2.20) | one file; its metadata carries one block per run (`run k of N, context <id>`), so the block count equals the run count; tools split only on those scopes | |
| a reference to a file not yet built (R5.20) | non-path text in the committed record ("the planned <file>, path set when built") and an open wire-in row with its owner; it becomes a path in the commit that creates the file | |
| a work queue: proposals awaiting the human's yes, approved items, items in progress (R9.24) | `<docs>/work-queue.csv` (owner: Arbiter; columns `item_id,queue_id,state,approved_by_dec,source,added`; state one of `proposed`, `approved`, `ready-not-started`, `in-progress`, `done`; an approval is a decision-log row in the human's words, which `approved_by_dec` cites) | |
| asks the human put on their own trigger, with dose bases (R9.5, R9.24) | `<docs>/trigger-bundles.csv` (owner: Arbiter; columns `trigger,ask,rank,dose_basis,source`; shown only when the human pulls that trigger) | |
| the setting-to-source map for "no data" searches (R9.27) <!-- KNOB: applied work --> | `<docs>/setting-sources.csv` (setting or setting group, source kinds in search order, path or query; owner: Arbiter; the source kinds named in R9.27 are the floor of every row) | |
| a caught-miss log: each correction the human makes to a session's work (R9.26) <!-- KNOB: applied work --> | `<docs>/caught-misses.csv` (date, mechanism key, record, correction commit, remediation commit; append only) | |
| <…> | <…> | <…> |
| **no row fits** | **ask the Arbiter; add a row first** | |

## 3. Path map (moved paths and stubs)
| Old path | New path | Kind (moved / stub) | Remove when | Date, commit |
|---|---|---|---|---|
<!-- R2.3: a stub stays at the old path while something outside the repository still names it (a shared command repository, memory); `Remove when` states the condition. The repo check lists live stubs and blocks on a dangling one. -->

## 3b. Tool registry (R2.12) <!-- KNOB: tool registry. In the minimum the rules file's Key commands list is the registry. -->
| Tool | Command | Status (`side, not reviewed` / `unreviewed` / `reviewed` / retired; R2.13, R6.15) | Tests | Owner role | Pinned? (R10.8) | Promotion runs (hash 1, hash 2; R2.13) | Dependency: why + decision id (R2.16) |
|---|---|---|---|---|---|---|---|

## 3d. Publish strip list <!-- KNOB: public mirror (R10.12). Delete this subsection when the knob is off. -->
| Path or extension | Why it is not published | Earlier locations followed through the path map (chained moves) |
|---|---|---|
<!-- Raw media and bulk binaries: kept on disk, cited by path and sha256, never committed. Publish-restricted data (a source of truth under terms, its derived extracts): listed here by path and extension. The mirror script strips every listed path from every commit and verifies fail closed that none remains; the commit map is saved locally, committed (append-only) and kept with the anchors (R7.15). A change to this list is a deliberate re-baseline the human runs (R10.12). -->

## 3e. Result-free path classes (R4.11) <!-- KNOB: Thinker. Delete this subsection when the knob is off. -->
Folders whose files carry no result (for example briefs, plans, method documents). Only a file in one of these may use the R4.11 narrow exception, and only for hit lines its author declared in advance (`id mentions at <lines>`); a result-bearing record is never listed. Default: none declared, so the stop always stands.
- <path class> | <why it carries no result>

## 3c. Record kinds, never-consolidated list and checker exemptions (R5.16, R2.15)
**Current-state records** (one row per subject, edited in place; may be consolidated): <status ledger, now-file, role handoffs, knowledge records, the human's preference record, indexes>.
**Event records, never consolidated:** frozen records, pre-registrations and test records, score records, journals, logs, Thinker pairs, append-only ledgers, the held list (CSV and view), the holds table, exposure logs, the decision log, outboxes, the frozen manifest, the data catalog and data-status ledger, the investigation ledger, the caught-miss log, <…>. A row of the held list or the holds table is never deleted (R2.4).

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
