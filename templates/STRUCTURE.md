# Structure: <PROJECT>

File: `<structure path>` | Owner: Arbiter | GUIDELINES R2.1–R2.5, R2.12, R2.13, R3.12, R6.13, R7.23, R7.30, R7.34, R8.9
<!-- Lines tagged KNOB are optional; see GUIDELINES §15. -->

## 1. Layout
| Folder | Holds |
|---|---|
| `<docs>/` | rules, charter, goals, structure, status, methods, decision log |
| `peers/` | `outbox-<role>.md` per role |
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
| a message with a `need:` | the sender's outbox | `OUTBOX.md` |
| a prediction before data <!-- KNOB --> | `<evidence>/prereg/` | `PREREGISTRATION.md` |
| a review | `reviews/` | `REVIEW-REPORT.md` |
| a method document for a measurement or analysis (R7.30) | `<docs>/methods/`, with a pitfalls table | |
| an investigation step file <!-- KNOB: investigation --> | `<evidence>/investigations/<date>-<topic>/` (append-only); `<topic>` names the question, never a direction or result (R8.4) | `INVESTIGATION.md`, `LENS-CARDS.md` |
| investigation scores <!-- KNOB: investigation --> | `<evidence>/investigations/ledger.csv` | `INVESTIGATION-LEDGER.csv` |
| a raw-data catalog (R10.9) <!-- KNOB: data intake --> | `<data>/catalog.csv` | |
| a lever-to-topic map (R6.13) | the method doc's "Lever-to-topic map" table, with the sentinel set (owner: Arbiter) | |
| pre-run rulings (R7.23) <!-- KNOB: evidence --> | beside the pre-registration's scorer, committed with it | |
| a fixture from a raw sample the human supplied (R7.34) | `scripts/fixtures/` for a promoted tool; the peer's own folder, beside its tool, before promotion (R2.13); byte for byte, marked "fixtures, not records" | |
| a peer-built tool, not yet promoted (R2.13) | the peer's own folder until the Arbiter promotes it (then `scripts/`, with a path-map row and a registry row, or a Key commands entry where the registry knob is off) | |
| <…> | <…> | <…> |
| **no row fits** | **ask the Arbiter; add a row first** | |

## 3. Path map (moved paths and stubs)
| Old path | New path | Kind (moved / stub) | Remove when | Date, commit |
|---|---|---|---|---|
<!-- R2.3: a stub stays at the old path while something outside the repository still names it (a shared command repository, memory); `Remove when` states the condition. The repo check lists live stubs and blocks on a dangling one. -->

## 3b. Tool registry (R2.12) <!-- KNOB: tool registry. In the minimum the rules file's Key commands list is the registry. -->
| Tool | Command | Status (live / retired) | Tests | Owner role | Pinned? (R10.8) |
|---|---|---|---|---|---|

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
