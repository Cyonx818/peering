# Pre-registration <ID>: <short title>

Date: <YYYY-MM-DD> | Author (predictor): <fresh subagent id> | Scorer: <fresh subagent id, assigned at commit; never the predictor> | Owner: Arbiter | Status: Registered
<!-- KNOB: evidence / pre-registration. Commit BEFORE any data it is scored on is captured or opened (R7.2).
     After the commit §A–§H are frozen; only §V (deviations) and §R (result) are appended.
     A design committed after the data were recorded is not a pre-registration: use the field `design_commit (after capture)` in place of the pre-registration commit, state the documented state value for it, and never record it as VALIDATED (provenance class at most STRONG; a lead labeled "blind analysis after capture" where the evidence knob is off; R7.50). -->

## §A Question and claim
<The claim under test, its current class, and what it becomes on PASS / FAIL.>

## §B Scope
| Item | Value |
|---|---|
| Subject(s) | <…> |
| Conditions / configuration | <…> |
| Data to be scored | <which observations; how they will be selected (mechanically, not by outcome)> |
| Fit set | <every datum used to build the prediction; none of these may confirm it> |
| Data status | <every datum to be scored is "clean" for this family in the per-datum ledger (R7.12)> |
| Replication unit | <repetition / block / session; why (R7.14)> |
| Quantized readout (R7.2) <!-- KNOB: only if the readout is on a grid --> | <grid step; per rival: predicted reading on the grid and the rounding band; rivals within <3> steps marked "not resolvable on one read"> |
| Outside-fit-set check (R7.29) | <tool, run date, exit code; output path @ commit> |
| Post-session question to the human (if the human is the subject; R7.26) | <wording; answer classes; consequence of a missing answer> |
| Derivation chain | <instruments and auxiliary assumptions, each validated (cite) or routed to an offline check (R7.21)> |
| Count-only pass (R7.37) | <script or counts mode; per cell: samples, passes or subjects surviving every selection rule; histogram of each selection variable; result path @ commit. If the counts already fix the outcome category, do not mint. Data not yet recorded: counts on the closest existing data of the same kind, labeled "proxy counts" (named, outside the fit set where possible); if none exists, "no proxy" and a pre-written support-refusal outcome (what is reported if the real counts fix the category, e.g. "not resolvable"); re-run on the real data before scoring> |
| Selection-rule check (R7.38) | <per rule: kept count as the quantity of interest grows; confounded with the effect? how paired or modeled> |
| Actor operating point (R7.2) <!-- KNOB: only if an actor is part of the instrument --> | <where the actor runs relative to the limit; measurement cited (file, n)> |
| Minimum-effect floor of the sign test (R7.42) | <the smallest mean residual that triggers a refit, e.g. one display unit; below it the record reads "significant, below the floor"> |
| What this set can decide / cannot decide (R7.42) | <e.g. a one-subject set decides a measure but not a between-subject slope> |
| Held-out set never printed for selection (R7.12) | <yes: no score of this set was printed per candidate; else the set is spent and a fresh one is named here> |
| Does a pass move a class? What the record already settles (R7.2) | <what the record already fixes (for example the sign); the scored size or shape cell the rivals predict differently; "none: the primary cell is open"> |
| Predicted vs read quantity (R7.2) | <same kind, unit and window: yes / the difference and how it is handled> |
| Calibration items (R7.52) <!-- KNOB: only if a per-case offset or scale is calibrated from items assumed neutral --> | <per item: why it carries no effect under test; items moved to the decision set, with removal rows (verdict with and without)> |
| Configuration reconciled against a conserved total (R7.49) | <the independent total (weight, cost, count, checksum) and the item-by-item reconciliation path; "not applicable" if no configuration is read from partial observations> |

## §C Prediction
| Cell | Predicted value | Tolerance band | Plausible range | Basis (derivation, sources with query / commit) |
|---|---|---|---|---|

## §D Falsifier
<The rival, its interval, the gap between the intervals in units of se = sd / √n (sd: file, n; block as the unit); k used and its basis (default 2); if the gap is < k·se the test cannot separate them (R7.21).> Failure rule (one sentence): <…>

Decisiveness (R7.2; applies to every pre-registration, whatever the investigation knob):

| Cell | Each rival's predicted interval, computed in this design's own regime, window and gates | Gap in se (spread cited: file, n; block as unit) | Independent variable verified on every subject in scope (cite; else narrow the scope label) | Decisive? |
|---|---|---|---|---|

Rivals whose intervals converge in the design's regime make it non-separable: retire the design before any prediction. A cell declared non-decisive here: <none | cells; the human was offered the trade (wait for the test / advice now and the test spent / a fresh datum later) and chose <…> on <date>; no data held for it> (R8.12).

## §E Scoring rule (fixed now)
1. <exact computation, rounding, windows, anchors>
2. <edge cases named in advance; unregistered ones become protocol gaps>
3. Comparisons: <number>; correction: <method or "none">; expected false marks: <n> (R7.13).
4. PASS = <…>; FAIL = <…>; NC (not conclusive) = <…>. Define each verdict by interval relations only (observed interval vs the predicted interval and the rival's), mutually exclusive, with a stated precedence order when two rows could both apply (R7.2).
4b. One selection rule for every arm: warm-up drops, exclusions and phase edges are written once and applied to all arms alike (R7.2).
5. Scorer: built from this text alone (R7.23); gaps ruled in `<pre-run rulings file>`, committed before any datum is read; a refusal before data is not the run (R7.24).

## §F Dose (human effort)
| Count asked | What it buys | Spread (source) | Effect to resolve | n required | Asked |
|---|---|---|---|---|---|
<!-- No spread known → say so and ask for the smallest pilot. Count blocks, not repetitions, when the subject drifts.
     State the floor and the cap, each with its basis, and the counted unit and its overhead (R9.1); the ask ends with a "not needed" line. -->

## §G Blinding and exposure <!-- KNOB: blinding -->
- Count-only passes (R7.37): <script path @ content hash; what each printed; exposure ruling row: exposure-free / what it exposed>.
- Predictor's forbidden files: <list>. The predictor's brief carried no outcome values.
- Brief author's logged exposures: <rows or "none">; leak check by an unexposed reader: <reviewer id / n.a.> (R7.4, R8.10).
- Thinker material read by the predictor: <response body @ commit, certified value-free by the Arbiter on <date> / none> (R4.7).
- Scorer: the fresh subagent named in the header, once, as written; returns `written: <path> @ <sha256>; values withheld (step <ID>)` (R8.5).
- Reviewer of the scoring (if any): <id>; not exposed to the family.
- Exposures of anyone involved: <rows or "none">.
- Human blinded? <yes / no>; held items and pending-list row: <…>; release condition: <…>.

## §H Locking
Pre-registration commit: <hash> | Seal commit (if any, direct child, same helper call with `--and`): <hash> | Anchored outside the repo <!-- KNOB: high-risk -->: <where, date> (R7.15)
Scorer snapshot: `<commit>:<path>` sha256 `<…>` | Pins on shared tools: <none / list, each with its retirement condition> (R10.8)
Fit-set pre-registration <!-- KNOB: only for a fit-set registration (R7.23) -->: commit 1 (specification and scorer pinned, before the fit data are read): <hash> | commit 2 (fit outputs and predictions recorded): <hash>. Confirmation comes only from data recorded after commit 2 (an exception to R7.3's "old or new": in a fit-set registration the analyst has read the data pool, so age is the only mechanical proof of separation; the R7.29 check compares capture stamps with commit 2).

## §V Deviations (append only, after commit)
| Date | Deviation | Effect on result | Verdict under the strict reading (R7.25) |
|---|---|---|---|
<!-- Post hoc splits go in their own file as leads (R7.26). -->


## §R Result (written by the scorer, after the seal opens)
| Cell | Observed | Verdict |
|---|---|---|
Overall: PASS / FAIL / NC. Class change (Arbiter only, after release): <from → to>.
