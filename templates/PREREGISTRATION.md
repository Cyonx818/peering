# Pre-registration <ID>: <short title>

Date: <YYYY-MM-DD> | Author (predictor): <fresh subagent id> | Scorer: <fresh subagent id, assigned at commit; never the predictor> | Owner: Arbiter | Status: Registered
<!-- KNOB: evidence / pre-registration. Commit BEFORE any data it is scored on is captured or opened (R7.2).
     After the commit §A–§H are frozen; only §V (deviations) and §R (result) are appended. -->

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
<!-- No spread known → say so and ask for the smallest pilot. Count blocks, not repetitions, when the subject drifts. -->

## §G Blinding and exposure <!-- KNOB: blinding -->
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

## §V Deviations (append only, after commit)
| Date | Deviation | Effect on result | Verdict under the strict reading (R7.25) |
|---|---|---|---|
<!-- Post hoc splits go in their own file as leads (R7.26). -->


## §R Result (written by the scorer, after the seal opens)
| Cell | Observed | Verdict |
|---|---|---|
Overall: PASS / FAIL / NC. Class change (Arbiter only, after release): <from → to>.
