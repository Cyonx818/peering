# Investigation <date>-<topic>: flag and step plan

Opened by: <role-id> | Date: <YYYY-MM-DD> | GUIDELINES R7.17–R7.22, R6.11
<!-- KNOB: investigation. Copy to `<evidence>/investigations/<date>-<topic>/00-flag.md` when an insight is flagged for explanation.
     `<topic>` names the question, never a direction or result (R8.4).
     Step files are append-only and carry no mutable front matter (R7.17): the state of the investigation is its highest committed step file.
     Seal hashes, resolution and scores live only in `<evidence>/investigations/ledger.csv` (`INVESTIGATION-LEDGER.csv`) and in later step files.
     Everything this phase produces is a lead (R7.1), never evidence.
     Requires the evidence knob and a Thinker or an unexposed merger subagent. Report the expected wall-clock time to the human before step 1. -->

## 00 Flag

| Field | Value |
|---|---|
| Observation | <what was seen, with `path@commit`> |
| Scope | <subject, conditions, data the observation covers> |
| Is / is-not boundary | <where the pattern is present; where it is absent> |
| Question | <one question to explain> |
| Blinding | <`clear` with the checks stated (R8.10) / `waits-on-step:<id>`; a flag that touches a held step waits for release> |
| Hunch | recorded in `00b-hunch.md`; do not open before the merge ends |
| Harness-loaded context | <the rules file and memory index carry no case content: grep for this investigation's identifiers printed a count of 0, on <date> (R6.11)> |

## 00b Hunch (flagger): its own file
<!-- Written to `00b-hunch.md`, a separate file committed at flag time and never in the same file as the observation (R7.18 a), or sealed outside the tree with its sha256 committed (R8.14).
     Never staged for anyone, never copied into a fact sheet, card or staged directory, and listed in the Forbidden (N) list of every brief until the merge ends (step 3).
     Opened into the merge record only after the merge part is committed. -->
<the flagger's own explanation, if any, in `00b-hunch.md`>

## Steps

| # | Step | Output file | Gate before the next step | Rule |
|---|---|---|---|---|
| 0 | Flag; hunch in its own file | `00-flag.md`, `00b-hunch.md` | committed; blinding field filled; "Who sees what" below filled and agrees with the write-scope matrix | R7.17, R7.18 a |
| 1 | Fact sheet (clerk, no generator) | `01-fact-sheet.md` | interpretive-word grep prints nothing; one reviewer pass; exclusions listed | R7.18 a |
| 1b | Scoring key (separate run, case values stripped) | `01b-key.md` | staged only for the merger | R7.18 a |
| 2 | Thinker's list, then generators plus a control | `02-thinker.md`, `02-gen-<n>.md` | brief dry-run kept in `dryrun/`, not a generator list (R6.12); each output's staged listing copied in; quota met | R7.18 b–e |
| 3 | Merge (hypotheses, mandatory rivals, matrix) | `03-merge.md` | <e.g. 5–8, or the plan's stated range> hypotheses; every slot filled, `slot-fill` or `unfilled`; no author names or counts in the ranker part | R7.19 |
| 4 | Rank, seal 1 | `04-seal1.md` | floor and catch-all checked; ranker agent ids in the header; seal hash (sha256 of the file) and its commit written in the header of `05-redteam.md` | R7.20 |
| 5 | Red team and merger reply | `05-redteam.md`, `05-reply.md` | red team saw top-3 names only | R7.20 |
| 6 | Rank, seal 2 (same rankers resumed; if the parent session ended, fresh rankers each given their own seal-1 sheet only plus the round-2 inputs, recorded as `rankers respawned` in the ledger row) | `06-seal2.md` | what moved is stated; seal hash and commit written in the header of `07-plan.md` and in the ledger `seal` row. Start steps 4–6 only with handoff headroom for all three (R5.13) | R7.20, R7.22 |
| 7 | Kill plan | `07-plan.md` | every kept hypothesis passes the R7.21 gate, items 1–6; advice line per outcome; branch per UNKNOWN | R7.21 |
| 8 | Pre-registration | `<PREREGISTRATION.md>` | R7.2; scorer built per R7.23 | R7.2, R7.23 |
| 9 | Apply (offline checks, then instruments, then the human) | per the plan | dose stated (R9.1); informal-by-default respected (R9.9) | R7.21 |
| 10 | Self-score | ledger `resolution` row appended | resolution or `unresolved-timeout` | R7.22 |

Commit subjects of every step name the step and the verdict class only (R8.15).

## Allowed inputs per role (R6.11)

| Role in the phase | Staged directory holds | Never staged |
|---|---|---|
| Clerk | raw tables, definitions, the human's dated statements | the hunch, any prior explanation |
| Key clerk | the reference list sources | case values |
| Generator | fact sheet, its own lens card | the hunch, other generators' lists, the key, cluster counts |
| Merger | all generator lists, fact sheet, key | the hunch until the merge ends; probabilities |
| Ranker | fact sheet, the ranker part of the merge; for seal 2 also the red-team output, the merger reply and its own seal-1 sheet | author names, cluster sizes, generator counts, the key, other rankers' sheets |
| Red team | fact sheet, matrix, top-3 names | probabilities, authors |
| Scorer builder | the committed pre-registration text and the frozen non-outcome inputs it names (schemas, configurations, fixtures) | any datum to be scored, outcome data, the plan |

Check each staged listing against this table before launch and copy it into the output header (order: R6.3). Staging does not stop the harness from auto-loading the rules file and memory index: the "Harness-loaded context" row of the flag records the check, and when strict blindness is required the agent runs as a separate session whose working directory is the staged folder (R6.11).

## Who sees what

Filled at step 0; it must agree with the write-scope matrix (`WRITE-SCOPES.md`). When the human will be a subject of the plan's tests, the Operator and the human are N on probabilities and kill-plan numbers until the test is scored, and the Operator receives only the advice line of the outcome that occurred.

| Artifact | Thinker | Operator | Generators | Rankers | Predictor | The human |
|---|---|---|---|---|---|---|
| Fact sheet | <R / N> | <R / N> | R | R | <R / N> | <R / N> |
| Hunch | <R / N> | <R / N> | N | N | N | <R / N> |
| Probabilities (seals) | <R / N> | <R / N> | N | own | N | <R / N> |
| Kill plan numbers | <R / N> | <R / N> | N | N | after the Arbiter re-derives them (R4.7) | <R / N> |
