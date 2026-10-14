# Codebook: <what is coded, e.g. the human's free-text reports> (version <n>)

File: `<docs>/methods/codebook-<topic>-v<n>.md` | Owner: Arbiter | GUIDELINES R7.40, R7.41
<!-- On whenever free-text reports are scored (R7.40, R7.41), whatever the other knobs. One file per codebook version;
     an old version stays (marked superseded). The codebook carries no outcome value of any held or scored step (R11.6). -->

## 1. Axes
One code per axis per clause (mutual exclusivity). Exhaustiveness comes from the out-of-scope bucket and the "unspecified" value.

| Axis | Codes | Definition and one boundary example | Primary or secondary |
|---|---|---|---|
| <axis> | <code>, <code>, … | <when it applies; the nearest code it is confused with> | primary / secondary |

## 2. Units and weights
- **Unit coded:** <clause / statement / report>; **unit counted in a rate:** <…>; weights: <equal / stated>.
- **Out-of-scope bucket:** <name>. Counts in coverage, never in the rate.
- **"Unspecified":** a value on every secondary axis (for example phase, place). A secondary field is scored only when the source states it.
- **Valence:** verdict and trust words are valence attached to a unit, not codes, until a measurable quantity predicts them. Valence field: <values>.

**Coder sheet.** Sections 1, 2 and 7 are the only part of this file staged to a second coder or the blind analyst. Priors (§3), agreement (§4) and uncodable shares (§5) stay in the full file: they anchor an independent coder toward the expected distribution.

## 3. Priors (R7.40)
Seeded from reports committed before `<commit>` (the intake commit of the earliest round this version will score; pointer to the sample: <…>), so a revision after a round's intake never absorbs that round's words. Default smoothing: Beta(1,1) per code, by subgroup with shrinkage toward the pool with pseudo-count <n>; a different method is a version change.

| Code | Subgroup | Smoothed prior p0 | Basis count | Shrunk toward pool? |
|---|---|---|---|---|

Display form: "k named of n, expected Σp0 = <x>". A tail probability is quoted as evidence only at ≤ <0.05>.

## 4. Agreement (R7.41)
Second coder: <fresh subagent id>, briefed with the coder sheet (§1, §2, §7) and the raw quotes only, in a private scratch folder (R6.8, R6.11); logged as exposed to the quotes it coded and never the blind analyst of a later round of the same subject (R7.41). Sample: <n> items drawn by `<script>` with seed `<s>`, excluding every item the rules were tuned on (tuning sample: <pointer>); the drawn ids are listed in `<path>` before the second coder starts.

| Slot (axis) | Fresh n | Agreement | Kappa | Too rare to estimate? |
|---|---|---|---|---|

A pilot on the tuning sample or on mixed codebook versions is labeled "pilot, not used". Until the first check, scores are labeled "provisional, codebook not yet checked": not quoted as evidence, not pooled into a hit rate. The first check runs as soon as <30> units outside the tuning sample exist (expected by round <3>); provisional rounds are then re-scored with the checked codebook. Repeat on a fresh sample after each revision and periodically.

## 5. Uncodable share
| Round | Units | Uncodable | Share |
|---|---|---|---|

Above about <10 %> the codebook goes back for redesign; the slot with the weakest agreement is read as a coder signal first.

## 6. Version history
| Version | Date | Change and cause | Agreement re-run? |
|---|---|---|---|

## 7. Coded output (one CSV per coder per sample; part of the coder sheet)
Columns: `unit_id,clause_id,axis,code,valence,quote_start,quote_end,coder,codebook_version`. One row per axis per clause; "unspecified" and the out-of-scope bucket are codes, not blanks. Blind cells (R8.18) use the same row form, plus `claim` and `basis` columns. Agreement (§4) is computed by `<script>` from two such files, so rounds and coders are comparable (R6.15).
