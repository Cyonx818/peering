# Changelog

Rule ids are stable: v1.0 ids keep their number (their text may change, as listed here); new rules are appended within their section. Finding ids refer to each version's review-panel disposition table, kept with the maintainers' development records (not published).

## v1.7 (2026-10-28)

Produced from a sixth exchange with the source project's sessions: the gap analysis of what the source project learned between 2026-10-20 and 2026-10-28 (66 learnings: 20 covered, 34 partial, 12 missing), five framework rules it found wrong or contradicted by practice (W1 to W5), the reverse analysis's "where the source project is ahead" list (six items) and the three role lessons files. Applied by one writer, then run through the five-seat review panel (R7.16; see "Review panel (R7.16; `reviews/v1.7/`)" below). Keyed to appendix incidents #95–#115 (new in this version). No existing rule id was renumbered or moved. Every conservative call and skipped item is listed in the maintainers' development records (not published).

### Upgrading from v1.6
Nothing is breaking. The full steps are in `README.md` § "Upgrading from v1.6"; in short: `atom_diff.py` is unchanged; `commit_paths.py` has one fail-closed fix (only an exact `released` frees a held row) and its 23 helper tests still apply (one test gained a row). No template is new. Adopt first: a checker that reports what it skipped (R2.15) and "no data" only after the listed sources were searched (R9.27, R9.13).
1. Re-copy the changed templates, by knob, carrying over your filled placeholders. Everyone: `SUBAGENT-BRIEF.md`, `STRUCTURE.md`, `HANDOFF-COMMAND.md`, `START-COMMAND.md`, `HANDOFF-FILE.md`, `PEER-COMMS-PROTOCOL.md`, `settings-permissions.json`. Thinker: `RESPONSE.md`, `STATUS.md`. Evidence: `PREREGISTRATION.md`, `REVIEW-REPORT.md`. Blinding / machine-read held list: `PENDING-BLINDED-STEPS.csv` and `.md` (three columns appended). Applied-work discipline: `OPERATOR-FOLDER-HANDOFF.md`, `HUMAN-QUEUE-COMMAND.md`.
2. Project-side changes (hand them to the Arbiter as one brief; each applies when its trigger happens): checker reports with a coverage rule for each positive duty (R2.15); a complete designed first package (R9.27); one root-cause pass after a repeated miss (R9.26); blind analyses of recorded data never VALIDATED, at most STRONG (R7.50); budget modes recorded with a lapse (R6.18); time-switched gates with a countdown and a queue (R2.19); planned files cited as text (R5.20).
3. **Your part (the human).** Nothing is required at upgrade. You may now be asked for the asks listed in `README.md` § "Your job as the human" (marked v1.7): a one-word endorsement per settings group at milestones if you turn a preference zone on (R9.28), a yes for each work queue (R9.24), the name of an unidentified run context or an initiative (R2.20, R2.21), your choice for a setting with no footprint (R9.19), and a decision-log row for a budget mode (R6.18). You will also see a "checking" reply in place of a quick guess (R9.17) and a first package that lists every setting with its basis (R9.27).

### New rules (appended within their sections; 11)
- R2.19 time-switched rules are visible, fail safe and leave a queue (#103); R2.20 a record that holds several runs is scoped per run, never split by guess (#102); R2.21 initiatives that share a repository have a register (provisional).
- R5.20 cite planned files as non-path text (#114).
- R6.18 budget modes are scoped, recorded and lapse (#113).
- R7.50 blind analysis after capture is never VALIDATED, at most STRONG (#106); R7.51 a detector proves it discriminates before its parameters are tuned (#107); R7.52 calibration items must be boring (#108).
- R9.26 a repeated miss gets one root-cause pass and the minimum effective remediation (#95, #96); R9.27 the first package for a configuration is a complete designed set, and "no data" needs a search (#95; also carries the source project's per-setting basis-kind check); R9.28 seed from a preference zone, a prior and never a fence (provisional).

### Amended rules (ids unchanged; 30)
- R2.9: a brief states whether the task needs a shell; a subagent without one returns blocked and never substitutes a weaker method (#109). R2.11: evidence shown only in conversation is a lead until saved and registered. R2.15: a checker reports what it skipped, negative-only checkers are labeled, a guard runs in every writing mode, one test per documented form (#101, #102). R2.17: a fallback fires only on its named refusal and its label travels (#100). R2.18: after a structural change the entry check re-reads every dependent setting.
- R4.10: "Misses since last response" in the Thinker's header.
- R6.1: the orchestrator re-applies the written decision rule before relaying a verdict (#111). R6.6: the handoff waits while start-read bytes or long cells exceed the previous handoff's figures without a stated reason (the next rung of the report, warn, block ladder). R6.15: the cache key covers the derivation code, hits are validated, partial data is refused, and a cache refuses held data like the shared reader (#98, #99). R6.16: never means a first-package setting stays undesigned.
- R7.2: the decisiveness gate asks whether a pass moves a class; predicted and read quantity match; a law's scope names its instrument's operating point (#105). R7.7: Lows included before a swap, the fix patch is reviewed, an unreviewed rule is labeled (#100). R7.13: t quantile and zero-spread labels for small-n marks. R7.26: a mid-run follow-up metric is committed before its conclusion. R7.31: a human-facing rendering of backfilled rows may omit marks while the provenance columns stay (W3). R7.33: rules committed before the confirm set, obvious instrument combinations tested before "unknown", transfer coordinate by leave-one-case-out. R7.37: count-only scripts named with their hash and an exposure ruling. R7.43: a superlative names its population. R7.48: test expectations keyed by the source-of-truth attribute.
- R8.12: the hold's subject and start time are recorded as machine-read columns (`held_subject`, `holds_from`) that the fail-closed tools match (R8.16, R8.17), and every peer is told in a `blinded` message; pooled analyses list refused data (#110).
- R9.5: asks on the human's own trigger are kept ready as a bundle. R9.13: porting is between subjects, the subject's other configurations and the human's kept moves are this-subject data, and "no data" names the sources searched (W2). R9.14: a spend of a scarce shared budget earns its keep; confounds are listed before a primary is credited (#112); the first package designs every setting (W4). R9.17: answer-first never licenses an unchecked answer; "checking" is a valid answer (#97). R9.19: a setting with no footprint is set by the human's preference (#112). R9.22: "leanest path" never leaves a first-package setting undesigned (W4). R9.24: proposed and ready-not-started queue states; resume across sessions. R9.25: cross-reference to R9.26.
- R10.11: a verdict-diff sweep is the proof of unchanged uses for a checker. R10.12: one media list shared by the ignore file, helper, check and publish script, and an untrack mode that never re-adds.

### Fixes to rules that looked wrong
- W2 (R9.13: "another subject or configuration" and the bare "no data; the measurements decide"): applied; porting is between subjects and "no data" names the sources searched; R9.27 defines the search.
- W3 (R7.31 backfilling against a register shown "as if it had always been there"): applied as a presentation allowance (R7.31, R2.21); provenance columns stay.
- W4 (R9.14 scope by findings read with the lean-path rules R6.16 and R9.22): applied through R9.27 and cross-references in R6.16, R9.14 and R9.22.
- W1 (R10.11: no reply and no live lease asks the human; the source project proceeds when the receiver is idle): **not changed**. The evidence shows swaps that broke nothing, not a harm from asking the human; the framework keeps its controls, and the project's idle-peer shortcut is recorded as incident #115.
- W5 (R7.3 / R7.23 contradiction): **not changed**; still the human's call. One more clean use of the project ruling is on file in the maintainers' development records.

### Templates
- Changed (15 files, 12 in the applied version and 3 added by the review panel): `SUBAGENT-BRIEF.md` (needs-shell line; number-parsing pitfalls; cache and fallback rules; tools-needed line; decision-inputs block), `REVIEW-REPORT.md` (tool checklist extended; checklists for a pre-registration and for a blind post-capture analysis or detector), `PREREGISTRATION.md` (three §B rows, a §G count-only row, the after-capture design field), `RESPONSE.md` (header row "Misses since last response", built from the status file), `OPERATOR-FOLDER-HANDOFF.md` (four loop-state rows), `HUMAN-QUEUE-COMMAND.md` (proposed / ready states; resume from the declared path only; new declared sources), `PEER-COMMS-PROTOCOL.md` (hold-registered notice, a `blinded` message), `PENDING-BLINDED-STEPS.csv` and `.md` (columns `held_subject`, `holds_from` as ISO 8601, `peers_notified`), `STRUCTURE.md` (placement rows), `HANDOFF-COMMAND.md` and `START-COMMAND.md` (two wire-in rows each; a standing-rules row in the start command; a size-gate step and budget-mode and caught-miss take-stock items), and, added by the panel, `HANDOFF-FILE.md` (header rows "Budget mode" and "Start-read size"), `STATUS.md` (Thinker-log column "Premise failed") and `settings-permissions.json` (`git rm` in `deny`).
- `commit_paths.py` and `test_commit_paths.py`: one fail-closed fix from the panel (only an exact `released` frees a held row; one test gained a `Released` row); `atom_diff.py` and its tests: unchanged.

### §13 and §15
- §13 gains seven rows (PASS on what was not checked, "no data" without a search, one patch per symptom, tuning a detector before testing it, a calibration item that may carry the effect, a blind analysis after capture filed as validated, a time switch without a countdown or a queue). §15 extends the applied-work rows to R9.27 (and R9.28 once the human turns it on), gives R9.26 to R9.28 a small form, and adds R7.50, R7.51 and R7.52 to "On whatever the knobs say".

### Appendix
- Incidents #95–#115; lessons 14 and 15 added.

### Review panel (R7.16; `reviews/v1.7/`)
Five seats (architect, agentic, usability, security, writing) reviewed the applied v1.7; 77 findings (C 0, H 13, M 41, L 23 by seat count); all dispositions in `reviews/v1.7/DISPOSITION.md`. The orchestrator ruled ten cross-seat questions; the changes:
- **Holds (R8.12, R8.16, R8.17):** the later-data scope is machine-read (`held_subject`, `holds_from`), the hold-registered notice is a `blinded` message with the pre-scan, and it writes no holds-table row.
- **Fail closed (R2.19, R2.20, R6.15):** a malformed switch stamp or clock blocks a blinding, publish, frozen-record or secret guard; run-context matching never decodes held data; cache entries are quarantined when a hold starts; the helper frees a row only on an exact `released`.
- **Process (R6.6, R6.18, R9.24):** the handoff has a size-gate step (own regions block, shared files warn); budget modes take effect only from a decision-log row and the never-defer list is complete; queue states have declared source files; an answers-file resume uses the declared path of the same role and each entry is re-confirmed.
- **Evidence and applied work (R7.50, R9.26–R9.28):** R7.50 is never VALIDATED and its harness-loaded-context guard is mandatory; the first-package audit is a reviewer subagent with a script-listed fallback; R9.28 is opt-in and waits on holds; §15 gives R9.26 to R9.28 a small form.
- **Human-facing text:** "Your job as the human" lists the seven v1.7 asks; the setup time is an estimate; the smoke tests follow Quick start A; the vocabulary and translation table cover the v1.7 terms.
Left for the human: whether a tool swap may proceed without an ack when the receiver holds no live lease (R10.11, incident #115); whether the always-on provisional rules stay in the table; the R7.3 / R7.23 conflict (W5).

### Decided after the panel (to apply in the next revision)
- R10.11: a shared-tool swap may proceed without an acknowledgment when the receiving role holds no live lease.
- Provisional rules (R2.21, R9.28 and any future one) are opt-in until proven, not always on.
- R7.3 / R7.23: any datum outside a pre-registration's declared fit set may confirm it, whether recorded before or after the commit.

## v1.6 (2026-10-20)

Produced from a fifth exchange with the source project's sessions: the gap analysis of what the source project learned between 2026-10-14 and 2026-10-20 (65 learnings: 15 covered, 30 partial, 20 missing), the reverse analysis's "where the source project is ahead" list (A1–A8) and the framework-side contradictions it found (three; one applied at R3.9, one left unchanged below, one needing no change), and the three role lessons files. Applied by one writer, then run through the five-seat review panel (R7.16; see "Review panel (R7.16; `reviews/v1.6/`)" below). Keyed to appendix incidents #70–#94 (new in this version). No existing rule id was renumbered or moved. Every conservative call and skipped item is listed in the maintainers' development records (not published).

### Upgrading from v1.5
Nothing is breaking. The full steps are in `README.md` § "Upgrading from v1.5"; in short: `commit_paths.py` and `atom_diff.py` are unchanged (their 23 helper tests and the atom-diff tests still apply). Adopt first the cheap clauses that prevent incidents: gate a commit on the check's own exit status, never a pipe (R10.4), and build commit path lists from the files the session wrote plus its subagents' OUT lines within their briefs (R10.2).
1. Copy the two new templates if their trigger has happened: `BUILD-PLAN.md` (large or pinned-tool builds) and `HUMAN-QUEUE-COMMAND.md` (asks pile up).
2. Re-copy the changed templates, by knob, carrying over your filled placeholders. Everyone: `PROJECT-INSTRUCTIONS.md`, `STRUCTURE.md`, `WRITE-SCOPES.md`, `SUBAGENT-BRIEF.md`, `ROLE-CHARTER.md`, `HANDOFF-COMMAND.md`, `HANDOFF-FILE.md`, `START-COMMAND.md`, `PEER-COMMS-PROTOCOL.md`, `settings-permissions.json`. Thinker: `BRIEF.md`, `RESPONSE.md`. Evidence: `PREREGISTRATION.md`, `REVIEW-REPORT.md`. Applied-work discipline: `OPERATOR-FOLDER-HANDOFF.md`. Blind report inference: `BLIND-INFERENCE-ROUND.md`.
3. Project-side changes: change shared tools a peer runs only from a private clone, with a tool-swap notice (R10.11); with raw media, publish-restricted data or a public remote, turn on the knob "Public mirror" (R10.12); register peer-built tools as `side, not reviewed` and give outside tools a fit assessment (R2.13, R2.16); with the evidence knob on or off, give acceptance tests the "could this fail on a wrong build?" question (R7.44, R7.45; they are on whenever a tool or validity rule is written or reviewed); put standing advice rulings into one pre-relay script once a ruling has been caught by hand (R9.25).
4. Wire in phase rulings and adopted vetting items in the commit of their phase (R4.16); rebuild derived records only from a final source (R5.19).
5. **Your part (the human).** Nothing is required at upgrade. From now on you also approve outside tools and non-default dependencies (R2.16), choose between a build and its cheaper priced alternative when the trade is yours (R6.17), run the mirror publish script yourself under the Public mirror knob (R10.12), and may run the queue command that lists everything waiting on you (R9.24). One optional choice: the order of a blind round. The default is unchanged (your marks come before the next values); if you want the values first, say so once in your own words (it becomes a decision-log row; R8.18 (8), R9.22).

### New rules (appended within their sections; 19)
- R2.16 outside tools and dependencies enter by a fit assessment and the human's yes (#93); R2.17 a tool's out-of-rule output is void (#75); R2.18 record what was applied from the committed plan, mechanically (also carries the entry-check and prediction-predates-data clauses).
- R4.16 phased builds from a vetted design (#82).
- R5.19 rebuild derived records after their source is final (#86).
- R6.17 price the design before building; write the cheaper alternative (#74).
- R7.44 validity rules are two-ended (#79); R7.45 no acceptance test that passes by construction (#80); R7.46 mixtures are not noise (#81); R7.47 generality census before a one-case rule is called general (#82); R7.48 exact identity keys (#76, #77); R7.49 reconcile what was seen against a conserved total (#78).
- R9.22 the human's deliverable comes first; no process stage gates it (#83); R9.23 derived readouts are outputs, not targets (#85); R9.24 one command walks the human through what waits on them; R9.25 check advice against the human's standing rulings before relay (#90).
- R10.11 change a shared tool that a peer runs live only from a private clone (#72); R10.12 raw media stays out of version control, publish a mirror, never rewrite proof history (#73).
- R14.3 repeating workflows keep a workflow log and their per-candidate data (#92).

### Amended rules (ids unchanged; 33)
- R2.8: scoped to records and documents; live code and the data files it reads go through R10.11 (the in-place edit scope). R2.13: `side, not reviewed` registration; "no other role's record relies on its numbers". R2.14: alias registry for renamed identifiers.
- R3.5: barred folders bind message content (#89). R3.9: a roster row may hold a name pattern where the helper accepts instance ids, with unique instance names and a stated weak second check (the identity contradiction).
- R4.4: `answered-by:` line; a folded addendum needs both sources in the brief log. R4.11: a narrow, provisional exception for author-declared id mentions in files of a declared result-free path class, decided by script and not by the reader (#88).
- R6.9: the freshness-cap pointer names the §1 Thinker row. R6.15: cached outputs and a generated standards digest (#91).
- R7.7: two parallel reviews per phase, one fix round. R7.12: a held-out set printed per candidate is spent (#87). R7.14: spread is the residual sd after trend and offset. R7.15: anchors for a rewritten mirror, verified by rebuilding it. R7.16: the disposition table has four values; panel runs v1.1 to v1.6. R7.28: a negative causal claim names every path checked. R7.33: decompose by family, query dependent records, test path independence. R7.34: matcher thresholds calibrated on labeled items. R7.35: named sources first, per-source picks, filters checked against the pool (#92). R7.39: second marking optional under values-first. R7.42: minimum-effect floor on a sign-test refit; what a gate set can and cannot decide.
- R8.2: the public remote and any published mirror are a channel. R8.14: a sealed file starts with a random nonce line. R8.15: the tripwire fails closed. R8.16: holds on unscored pre-registrations lift only by an append-only release row. R8.18: new item (8), the round order is a knob the human sets (sealed prediction first, a bare values list, sealed files committed in every order, the ruling recorded verbatim); (5) a round may be passed; (6) second stage before scoring allowed under values-first.
- R9.3: a stated technique is a recorded preference fact. R9.13: a ported value is not proposed (#84, #94). R9.16: a third order, values first. R9.18: the range check and no-porting rulings run as one tested script.
- R10.2: path lists are the session's own files plus subagent OUT lines within their briefs; history-rewriting tools are banned on the shared tree only (#71). R10.4: appendix cite only. R10.6: `git clone`, `git remote add`/`remove`/`rename` in `ask`, the publish script in `deny` for sessions. R10.10: a scoped admissibility ruling for lead-level reads, marked in the catalog.

### Fixes to rules that looked wrong
- Round order (R8.18 / R9.16 / R7.39 and `BLIND-INFERENCE-ROUND.md`; the human marks before the next values): kept as the default; the order is now a knob the human sets, with values-first allowed by explicit ruling, recorded and labeled in the hit-rate table. Sealed files, staging and the content grep stay on in every order.
- The in-place edit scope: R2.8 scoped to records and documents. The read-list exception: R4.11 narrowed (declared result-free files, author-declared lines, script-made copy; result-bearing records still stop). The ported value: R9.13 rung 6 replaced (a ported value is not proposed). The mirror path: R10.2 and R7.15 clarified; R10.12 never rewrites local history.
- Contradiction (R7.3 / R7.23: a fit-set pre-registration confirms only on data recorded after its second commit, against a project ruling that any capture outside the declared fit set may confirm): **not changed**; both positions are described in the maintainers' development records. Left to the human with the general-deviation question.

### Templates
- New: `BUILD-PLAN.md`, `HUMAN-QUEUE-COMMAND.md` (writes through a writer subagent, keeps a session answers file, few auto-allowed tools).
- Changed (16): `BLIND-INFERENCE-ROUND.md` (order that ran may be `values first`; step 1a, step 7 mandatory, a bare values list, "passed"); `PROJECT-INSTRUCTIONS.md`; `STRUCTURE.md` (§3b statuses and dependency column, §3d strip list, §3e result-free path classes, two placement rows); `settings-permissions.json` (clone, remote and filter-tool rows, the publish script denied for sessions); `SUBAGENT-BRIEF.md`; `ROLE-CHARTER.md` (rules 14 and 15); `BRIEF.md`; `RESPONSE.md`; `REVIEW-REPORT.md`; `PREREGISTRATION.md`; `HANDOFF-COMMAND.md` (duplicate wire-in rows removed; open tool swap in flight); `HANDOFF-FILE.md` (owner `human`); `OPERATOR-FOLDER-HANDOFF.md`; `WRITE-SCOPES.md`; `START-COMMAND.md` (the missing wire-in rows, standing rules for the v1.6 action-time rules, a queue line in the report); `PEER-COMMS-PROTOCOL.md` (tool-swap notice).
- `commit_paths.py`, `atom_diff.py` and their tests: unchanged. The value-free commit guard that the source project built into its own helper is described as a project option in R8.15 (not added to the reference helper).

### §13 and §15
- §13 gains eight rows (a stage before the answer, editing live code in place, rewriting proof history, out-of-rule output quoted, label or prefix as key, a test that cannot fail, tuning to a readout, an unpriced first design). §15 gains the knob "Public mirror", adds R7.44, R7.45, R7.46, R7.47 and R10.11 to "On whatever the knobs say", extends the applied-work row to R7.48, R7.49, R9.22–R9.25 and R14.3, marks single-project rules "Provisional", and the "Blind report inference" row names the round-order knob. The core-rules box adds R10.11 and R9.22.

### Appendix
- Incidents #70–#94; lessons 12 and 13 added. "Source project" throughout; commits cited by date and hash. Source-project session names, handoff ids and domain nouns removed from the appendix intro, §1 table and incidents #1, #4, #16, #63 and the lessons.

### Review panel (R7.16; `reviews/v1.6/`)
Five seats (architect-reviewer, agentic-engineer, ux-ui-architect, security-engineer, technical-writer) reviewed the working tree in parallel; the Arbiter ruled on the ten cross-seat Highs (`reviews/v1.6/ARBITER-RULINGS.md`); one writer applied the rest and recorded every finding in `reviews/v1.6/DISPOSITION.md`. 94 findings (0 Critical, 17 High, 44 Medium, 33 Low): 79 applied, 10 applied with change, 0 moot, 0 declined, 5 left to the human (a general deviation mechanism for project rulings; whether R10.11 and R9.23–R9.25 stay always-on and in the core box; the default tier of the two new templates; whether older "Upgrading from" sections leave the README), plus the two open parts of the mirror findings (who builds the mirror script; whether `git filter-repo` is an acceptable dependency). The main changes: R4.11's exception is decided by the file's author and a script, not by the reader; R10.11 gets a tool-swap notice (not a hold) with ack, drift check, open-swap record and delete handling; R8.18 (8) seals the prediction first and sends a bare values list; R10.12 refuses to publish while a step is held and never rewrites local history; R9.22 no longer reads as gating correctness checks; R3.9 requires unique instance names and calls its second check weak; the queue command records answers through a writer subagent and an answers file; the start command, role charter and subagent brief carry rows for the new action-time rules; the human's job section lists the new duties.

## v1.5 (2026-10-14)

Produced from a fourth exchange with the source project's sessions: the gap analysis of what the source project learned between 2026-10-06 and 2026-10-13 (58 learnings: 14 covered, 27 partial, 17 missing), the reverse analysis's "where the source project is ahead" list (items A1–A13, merged with the first list where they overlap), and the Operator and Thinker lessons files. Applied by one writer, then run through the five-seat review panel (R7.16; see "Review panel (R7.16)" below). Keyed to appendix incidents #59–#69 (new in this version). No existing rule id was renumbered or moved. Every conservative call and skipped item is listed in the maintainers' development records (not published).

### Upgrading from v1.4
Nothing is breaking. The full steps are in `README.md` § "Upgrading from v1.4"; in short:
0. Copy `PEER-COMMS-PROTOCOL.md` to `docs/peer-comms-protocol.md`, fill the roster, read it at every start, and add a `mode:` line to every message and outbox row (R3.13).
1. Copy the two new templates if their trigger has happened: `CODEBOOK.md` (scoring free-text reports) and `BLIND-INFERENCE-ROUND.md` (the new knob "Blind report inference").
2. Re-copy the changed templates, by knob, and carry over your filled placeholders. Everyone: `START-COMMAND.md` (standing-rules rows), `ROLE-CHARTER.md` (rules 11–12, reset line), `HANDOFF-COMMAND.md`, `PROJECT-INSTRUCTIONS.md`, `STRUCTURE.md`, `WRITE-SCOPES.md`, `SUBAGENT-BRIEF.md`. Thinker: `BRIEF.md`, `RESPONSE.md`, `THINKER-HANDOFF.md`. Evidence: `PREREGISTRATION.md`, `REVIEW-REPORT.md`, `DATA-STATUS-LEDGER.md`. Applied-work discipline: `OPERATOR-FOLDER-HANDOFF.md`.
3. Add the count-only pass and selection-rule check to every pre-registration not yet sealed (R7.37, R7.38); give applied-work reviews the whole-subject sweep (R6.13 scope); move mechanical jobs to tested scripts (R6.15); move a blind round's words and prediction files outside the working tree and check the analyst's staged inputs by content (R8.18).
4. Wire in closed designs (R5.18) and give a promotion row both run hashes (R2.13).
5. `commit_paths.py` and `atom_diff.py` are unchanged; their tests (the 23 helper tests and the atom-diff tests) still apply.
6. **Your part (the human).** Nothing unless you turn on blind report inference; then about two minutes per round to mark at most five cells. Asks now end with a "not needed" line; Thinker questions to you state the decision they unlock and fit in about a minute.

### New rules (appended within their sections; 16)
- R3.13 load the peer-comms protocol at start, tag every message with its mode (see "Peer-comms protocol" below).
- R4.15 rank the questions before the research (#67).
- R5.18 a failed premise closes its design in the record (#61).
- R6.15 scripts for mechanical jobs; R6.16 produce only what a decision uses (#65).
- R7.37 count before you register (#59); R7.38 check every selection rule against the effect (#60); R7.39 two predictions, two scores; R7.40 coding free-text reports (#63); R7.41 inter-coder agreement on a fresh sample (#63); R7.42 vet a model version before it drives blind predictions, and gate it twice (#64); R7.43 state the unit of every ranking and rate (#62).
- R8.18 blind inference of the human's report (#66).
- R9.19 stop rule for iterative applied work; R9.20 measure in chosen contexts, build for the use (#69); R9.21 package guards are margins with valence.

### Amended rules (ids unchanged; 27)
- R3.2: the `mode:` header line. R3.9: sender name checked against the roster.
- R2.13: objective promotion trigger (same hash on two work items and a passing test); the promotion commit adds the registry row.
- R3.10: search the record before a test on a peer's lead (#68); now with a Why line.
- R4.1 and R4.2: a review request may be a message naming a committed artifact at its hash; only the Arbiter sends it, and it carries no grants or folder override.
- R4.4: one response per committed input.
- R4.6: only a committed brief file may name single files in a folder the Thinker does not read by default, after a held-ids pre-scan of 0.
- R4.9: audit answer is a ranked table naming the rule or practice each change replaces (or "new"), with a "deliberately left out" list.
- R4.14: a human item carries the decision it unlocks and a one-minute bound; relayed answers committed verbatim; a grant is re-checked against the held list.
- R5.15: read each peer's open wire-in table directly; a closed design is a wire-in row.
- R6.1: mechanical jobs go to a script.
- R6.9: reset on context fraction; the brief count is a fallback and a Thinker freshness cap (provisional).
- R6.11: allowed inputs checked for current-round contamination; a parent review is staged only redacted; staging is run by a role with a shell.
- R6.13: scoped to project-claim reviews; in applied work every review sweeps the whole subject.
- R7.2: an actor's operating point is measured and cited.
- R7.3: a fit-set pre-registration confirms only on data recorded after its second commit.
- R7.7: a written disposition for every Critical or High (applied / applied with change / moot / declined).
- R7.12: a count-only pass is "adjacent", not spent; per-arm counts under a confounded rule are "exposed".
- R7.14: a deterministic actor's run-to-run change is state.
- R7.23: a fit-set pre-registration is a leakage control, never a confirmation.
- R7.32: unchanged-configuration repeats logged as pairs.
- R9.1: efficient design first; floor and cap with basis; counted unit with overhead; lighter keep standard for applied calls; a "not needed" line in every ask.
- R9.5: find the human's inputs yourself; file-name quirks.
- R9.14: a package fixes every problem found (problem defined), judged as a whole; a keep by report is progress; package guards listed.
- R9.16: either order of report and analysis allowed.
- R10.1: the outputs of a registered, tested script run by the orchestrator are excepted.

### Fixes to rules that looked wrong (B §5)
- W1 R6.13 scoped (evidence: the human's complaint, an adopted loop design, a review High); W2 R4.1 / R4.2 allow the message form (three of five requests, citation chain held); W3 R6.9 resets on context, not on a count (one session carried five exchanges small; marked provisional in the rule, with an optional Thinker freshness cap); W4 R6.1 sends mechanical jobs to scripts (the human's ruling). All four amended; none left open.

### Templates
- New: `CODEBOOK.md`, `BLIND-INFERENCE-ROUND.md`.
- Changed: `PREREGISTRATION.md` (count-only pass with the proxy branch, selection-rule check, actor operating point in §B; fit-set commits in §H); `REVIEW-REPORT.md` (disposition footer; unit checklist; codebook and model-version checklist; delete checklists that do not apply); `BRIEF.md` (message-form note; ranked research questions); `RESPONSE.md` (audit shape; message request in the header); `HANDOFF-COMMAND.md` (peer wire-in tables read directly; closed-design row; message requests paired); `THINKER-HANDOFF.md` (closed designs); `STRUCTURE.md` (§3b promotion-runs column; two placement rows); `WRITE-SCOPES.md` (round files split into sealed, in-tree and coded-data rows; footnote 21); `PROJECT-INSTRUCTIONS.md` (scripts, search-the-record and guard sentences; "not needed" line); `OPERATOR-FOLDER-HANDOFF.md` (loop state, unused-metric counter, "not needed" line); `START-COMMAND.md` (standing rules for the new action-time rules; message requests); `ROLE-CHARTER.md` (reset line; rules 11–12); `SUBAGENT-BRIEF.md` (scripts and blind-analyst constraints); `DATA-STATUS-LEDGER.md` (count-only passes); `CONSOLIDATION.md` and `PANEL-BRIEF.md` (small).
- `commit_paths.py`, `atom_diff.py` and their tests: unchanged.

### Peer-comms protocol (added 2026-10-14, before the v1.5 release; no version bump)
CHANGELOG convention: a change made while the version is unreleased is recorded in that version's section; v1.5 is not yet committed, so this is part of v1.5, not v1.5.1. From the human's requirement of 2026-10-14.
- New rule R3.13: every role loads the project's `docs/peer-comms-protocol.md` at start and tags every message and outbox row with a `mode:` (free, relay, blinded, courier). New template `PEER-COMMS-PROTOCOL.md` (roster, sender verification, the four modes).
- `PEER-MESSAGE-PROTOCOL.md` kept as the outbox-mechanics file; its "Authority and trust" section moved into the new template (no rule is stated twice). Amended: R3.2 (the `mode:` header line, not counted in the line limits), R3.9 (the name check is against the roster; handoff §0 keeps live state only). Core-rules box and the §15 peer-messaging row updated. Rule ids unchanged.
- Templates changed: `OUTBOX.md` (Mode column), `START-COMMAND.md` (step 5 reads the protocol; standing rule; report line 12), `HANDOFF-COMMAND.md`, `ROLE-CHARTER.md` (rule 13), `THINKER-HANDOFF.md`, `HANDOFF-FILE.md` (§0 name column), `STRUCTURE.md`, `PROJECT-INSTRUCTIONS.md`.

### §13 and §15
- §13 gains six rows (verdict fixed by the counts, filter against the effect, blind analyst with a readable answer, reliability on the tuning sample, unit artifact, the question sets the scope). §15 gains the knob "Blind report inference" and updates the "Pre-registration" and "Applied-work discipline" rows.

### Appendix
- Incidents #59–#69, each cited by date and commit; lesson 11 added. "Source project" throughout; no source-project outcomes in #60, #62, #64.

### Review panel (R7.16; `reviews/v1.5/`)
Five seats (architect, agentic, usability, security, writing) reviewed the applied v1.5; 90 findings (C 0, H 13, M 41, L 36 by seat count); all dispositions in `reviews/v1.5/DISPOSITION.md`. The Arbiter ruled ten cross-seat questions; the changes:
- **Blind report inference (R8.18, R7.39, `BLIND-INFERENCE-ROUND.md`, `CODEBOOK.md`):** the words and prediction files live outside the working tree with only their sha256 committed; the analyst gets a redacted parent review checked by a content-token grep; each cell has a value-free claim line shown and marked first and a basis line revealed after; a fixed committed open prompt; the human marks each cell (named / partly / missed / "can't say", defined; "can't say" excluded from the hit rate and logged); no default scoring time (the human ruled 2026-10-14: a project states one only if a proven problem calls for it; the general principle is at R9.1). The "can't say" value is confirmed by the human (2026-10-14). CODEBOOK gains a coder sheet, a coded-output CSV schema, a prior cut-off and a draw record; R7.41 scores are provisional until the first agreement check.
- **R7.37:** a proxy-count branch for prospective tests (count on the closest existing data; else "no proxy" with a pre-written support-refusal outcome).
- **R7.23 vs R7.3 / R7.29:** the stricter reading is an explicit exception in both rules and in the PREREGISTRATION template.
- **Knob precedence:** a rule-level knob tag wins over its section's knob for the named leak controls (exception paragraphs in §7 and §8; the §15 table "On whatever the knobs say"; the top of GUIDELINES).
- **Message-form requests (R4.1, R4.6):** only the Arbiter; no grants or folder overrides; an override needs a committed brief and a held-ids pre-scan of 0.
- **Standing rules:** the new action-time rules are cited in START-COMMAND, ROLE-CHARTER and SUBAGENT-BRIEF (R5.15).
- **W3:** R6.9 marked provisional with a Why line and an optional freshness cap.
- **README:** the human's job table lists the new duties; the upgrade section has a "Your part" paragraph and tiered re-copy steps.

## v1.4 (2026-10-06)

Produced from a third exchange with the source project's sessions: the gap analysis of what the source project learned in its tenth session (75 learnings: 18 covered, 36 partial, 21 missing), the "where the source project is ahead" list of the reverse analysis (items A1–A7), and the Operator and Thinker lessons files. Applied by one writer, then run through the five-seat review panel (R7.16; see "Review panel (R7.16)" below). Keyed to appendix incidents #47–#58 (new in this version). No existing rule id was renumbered or moved. Every conservative call and skipped item is listed in the maintainers' development records (not published).

### Upgrading from v1.3
The full steps are in `README.md` § "Upgrading from v1.3"; this is the same order in short.
1. **Breaking (W1–W3):** the history-marker contract is replaced by "write the state, log the event" (R5.2, R5.3, R5.16). Handoff and status files become current-state records: rows edited in place, no `**[history]` blocks, no dated sections. Choose (A) *not now*: keep the markers as the documented legacy form (R5.3; the v1.4 start reads both forms and lists the file for consolidation), or (B) *consolidate, one role at a time*, with the live peers quiesced by a hold: first create the now-file and the status ledger, then in one commit switch that role's start command, the handoff command (whole) and the handoff-file and status templates (R2.14), then consolidate that role's handoff and the status file in its owner's session (R5.17, R7.36, `templates/CONSOLIDATION.md`; full form for every handoff and the status file), then run a start and a handoff to prove it. Copy `templates/atom_diff.py` first (the atom diff needs a tool) and back up the repository off-machine.
2. Add `STRUCTURE.md` §3c (record kinds, never-consolidated list, checker exemptions with reasons) and the new placement and write-scope rows (footnote 20: each role writes its own now-file row).
3. Re-copy `PREREGISTRATION.md` and apply the R7.2 decisiveness gate to every pre-registration, whatever the investigation knob; re-copy the other changed templates listed in the README (they now include `PANEL-BRIEF.md`, `PROJECT-INSTRUCTIONS.md` and the new `deny` / `ask` entries in `settings-permissions.json`).
4. `commit_paths.py` and its tests are unchanged (23 tests; its docstring still says v1.3, because the code did not change); gating a commit on the check's own exit status (R10.4) is a project-side change.

### New rules (appended within their sections)
- R2.14 restructure a cited record without breaking its readers (#52); R2.15 a check says exactly what it checks and its exemptions are tested (#51).
- R5.16 write the state, log the event (#47); R5.17 consolidate with a drop ledger, an atom diff and no class creep (#48, #49).
- R6.14 stop a subagent once its report is in (#57).
- R7.36 reverse-read test for any rewrite of a record (#48, #50).
- R9.18 range-check every proposed value before the human sees it (#58).
- R10.10 integrity failures at intake: one standing exception, everything else to the Arbiter (#56).
- R12.2 contact with outside parties is the human's (codified practice, no incident).

### Amended rules (ids unchanged)
- **Rewritten (breaking):** R5.2 (a role handoff is a current-state record; was "Current first, history after") and R5.3 (start reads by heading order and fails loudly; the `[history]` marker contract survives only as a legacy form). R5.10 (a §10 row only for a correction that still bears on reading, W2).
- R1.5 (a method or process proposal is adopted by ruling, not classed as a lead, W4); R2.4 (lines of a current-state record are edited in place, W7); R2.5 (a frozen-manifest entry may freeze a header line); R2.10 (quotation marks only around words at a cited source); R4.9 (kill test on every design answer); R4.14 (default grant for preference and method briefs); R5.4 (§4 is a pointer map); R5.7 (record gate on added lines, shape check); R5.15 (wire-in rows: class change → ledger, Thinker response items → disposition); R6.4 (cap read widths); R6.7 (never trim to a size target without a reverse-read); R7.2 (the decisiveness gate applies to every pre-registration; W5); R7.11 and R7.31 (backfilling rulings found in prose; the `refines <id>` form); R7.23 (a bespoke scorer calls the pinned guards or tests its own); R7.28 (layer before lever; a "limit" claim states its signature); R7.30 (process methods log defects of the method); R8.1 (derivative files are held data); R8.9 (the human-readable column sets review depth for rewrites); R8.12 (offer the trade before a hold on the human's own data); R8.15 (the tripwire may key on a content marker); R8.16 (a guard identifies a datum by content, never by name: resolve the path, compare the file's sha256 with the catalog, check the identity field in the first record; #54); R9.3 (independent readout once per package); R9.13 (a habit band is a prior, an unknown readout is no rung); R9.14 (match the reference's measured behavior signature; a metric and falsifier per subjective statement; name confounded lever pairs); R10.4 (gate on the check's own result, never a pipe; link only committed targets; #55); R14.2 (the status update edits rows, never adds a dated section; W6); §1 Thinker row ("the reader who is not inside the pipeline").

### Fixes to rules that looked wrong (B §5)
- W1 R5.2 / R5.3 and the handoff-file, handoff-command and start-command lazy-read steps; W2 R5.10; W3 the status template's history cells; W4 R1.5; W5 R7.21 items (3), (4), (6) now apply to every pre-registration through R7.2; W6 R14.2; W7 R2.4.

### Templates and helper
- `HANDOFF-FILE.md` rewritten: heading-order contract, Record line, Session state and Open wire-in tables in the header, §4 a pointer map, §7 Trajectory, §10 only for corrections that still bear on reading. `HANDOFF-COMMAND.md` and `START-COMMAND.md`: rows edited in place, heading-order check, record gate on added lines, empty-slice stop, the now-file at A1, two new wire-in rows, exit-status gating, stop the writer after its return. `STATUS.md` rebuilt as a ledger. New `NOW.md` and `CONSOLIDATION.md`.
- `STRUCTURE.md` (placement rows, §3c record kinds and checker exemptions), `WRITE-SCOPES.md` (two rows), `PREREGISTRATION.md` (decisiveness table, verdict rows by interval relations, one selection rule), `REVIEW-REPORT.md` (rewrite checklist), `SUBAGENT-BRIEF.md`, `BRIEF.md`, `RESPONSE.md` (kill test), `ROLE-CHARTER.md` (rules 8–10), `EXPOSURE-LOG.md` and `PENDING-BLINDED-STEPS.md` (derivative files), `OPERATOR-FOLDER-HANDOFF.md`, `settings-permissions.json` (`ask` entries for outside-posting commands), `examples/minimal-setup.md` (handoff in the new form).
- `commit_paths.py` and `test_commit_paths.py`: **unchanged** (its version string stays v1.3: the code did not change). The optional helper features B proposed (run the check itself, refuse links to untracked paths) and the content-keyed guards of the reverse analysis (A5) are documented as project options in R10.4, R2.5 and R8.15; no helper code was written because the writer has no shell to run the tests. The review panel added one new tool, `atom_diff.py`, and its tests (see below).

### §13 and §15
- §13 gains ten rows (log-shaped record, trim to target, class creep, quote inflation, stale key, exempted target, silent parser, non-decisive design sealed, name-only guard, piped gate). §15 gains a "Record consolidation" row; the "Handoff file" and "Helper guards" rows are updated.

### Appendix
- Incidents #47–#58, evidence cited generically; lesson 3 updated and lesson 10 added; incident #14 notes its supersession.

### Not applied
- See the maintainers' development records (not published): the helper changes and the reverse analysis's `CURRENT-STATE-RECORD.md` template (covered by `STATUS.md` and `NOW.md`). The `ask` list was widened by the review panel.

### Review panel (R7.16; reviews/v1.4/)
Five seats (architecture, agentic, usability, safety, proofread); 0 Critical, 15 High-class findings counted across seats (overlapping ones merged under seven orchestrator rulings), plus Medium and Low items; dispositions in `reviews/v1.4/DISPOSITION.md` (kept with the maintainers' development records, not published). Changes:
- **Heading-order check** (R5.3; ruling R1): applies only to the sections present, compared on the `§<n>` token; the minimum handoff and the shipped example pass; the legacy form is detected mechanically (`grep -c`); the §7 read stops at a `### Trajectory` heading; a writer's progress block goes at the END of an output file that is itself a record, and is deleted when done (R6.3, R6.5).
- **Sealed key** (R7.36; R2): the key lives in its own sealed folder, separate from the rewriter's working files; the rewriter's and readers' forbidden lists name it; stated plainly as convention-enforced, not mechanical. The rewrite goes to a candidate path and the consolidation record carries a Stage line; `CONSOLIDATION.md` is two files with a "how to run" box. Scoring: best part per question, via-pointer scoring, at most two restore rounds.
- **One copy of the next action** (R5.16; R3): the now-file holds the next action (one row per role, each role writes its own row; R2.7 second exception) and the last session end; handoff and example point to it.
- **Upgrade order** (R4): now-file first, then switch the start command; per role; quiesce live peers with a hold; the start keeps its legacy `[history]` read; README and this entry agree.
- **Gate coverage** (R5.7, R5; R7): a modified-row class check and an atom diff of changed record files as gate options; "session-start commit" defined and recorded in the now-file; new `templates/atom_diff.py` and `test_atom_diff.py` (not yet run by the writer; run them before release).
- **Held values** (R6): the held list, holds table and exposure logs are never consolidated; the never-drop list covers hold and exposure lines; a held-ids pre-scan before any consolidation; atom-diff output goes to a file scanned for held ids; R8.16 strengthened (canonical path, case-folded name, content check of edited copies, files not in the catalog refused, only the Arbiter adds catalog rows).
- **Smaller:** R7.36 trigger defined (consolidation, restructure, trim); trajectory rows retire; R9.18 clamp before the prediction commit and cited in START-COMMAND, PROJECT-INSTRUCTIONS and §15; R10.6 deny-list gaps (`git reset` every form, `git config`, `--git-dir`, `rm` forms, `gh api`, visibility changes, MCP posting tools; sandbox note; placeholder rows are a setup failure); R10.10 and R12.2 tightened; panel output paths carry `<version>/`; changelog and appendix no longer point to unpublished files or a source-project verdict.

## v1.3 (2026-10-05)

Produced from a second exchange with the source project's sessions: the gap analysis of what the source project learned after v1.2 (51 learnings, 12 missing, 25 partial), the "where the source project is ahead" list of the reverse analysis (items A1–A5), and the Operator and Thinker lessons files. Then run through the five-seat review panel (R7.16; see "Review panel (R7.16)" below). Keyed to appendix incidents #36–#46 (new in this version). No existing rule id was renumbered or moved.

### Upgrading from v1.2
1. **Breaking:** the helper refuses a commit with no role or a role not on its `ROLES` list; its refusal no longer names a bypass. Re-copy `commit_paths.py` and `test_commit_paths.py`, set `ROLES`, and add `--role <role-id>` to every script, hook and alias that calls it; a deliberate bootstrap commit uses `--no-role "<reason>"` (trailer `Session-Role: none (<reason>)`). Never export `PEERING_ROLE` in a shared shell profile.
2. Append `,scope,quote_fidelity,question,options` to the decision log's header, set `quote_fidelity` to `legacy` on every existing row (legacy rows keep their status and are confirmed with the human only when next relied on), and add a decision-log row naming the cut-off id (R7.31).
3. Create the holds table from `templates/HOLDS.csv` (R3.12); add §6 to each handoff file; re-copy START-COMMAND step 7, A2, A5 (i)–(k) and the standing rules, HANDOFF-COMMAND (wire-in "ruling" row, Holds row, step 11), the rules file's rules 2, 12 and the compaction line, and the charters' role-specific rules.
4. Run the helper tests (23).

### New rules (appended within their sections)
- R2.13 a peer may build a tool in its own scope, the Arbiter promotes it (incident #41).
- R3.12 a relayed hold only restricts, never permits (#37); rewritten by the panel (see below): holds table, state `held (relayed, unconfirmed)`, the human is always the releaser.
- R4.14 the Thinker asks the human only on a brief's grant that also clears the held steps (#38).
- R6.13 recompute only what the change can reach (#36).
- R7.31 ruling fidelity: verbatim, relayed or paraphrased, and what the session added (#38, #39); R7.32 between-session comparisons carry a drift allowance (#46); R7.33 exploratory fits report an honest out-of-sample score (#40); R7.34 golden fixtures come from raw samples (#41); R7.35 enumerate the whole option space before proposing paths (#44).
- R9.13 advice states its rung on the advice ladder; R9.14 applied work runs in packages; R9.15 name things the way the human knows them (#45); R9.16 the human's report before any number (#42); R9.17 a waiting human gets the answer first (#43).

### Amended rules (ids unchanged)
- R2.11 reply first when the human waits; R4.6 header lists reads beyond the brief; R5.15 a ruling's wire-in greps loaded standards for text it contradicts, and the Arbiter lists peer close commits at start (the pass itself runs after the human's choice); R6.5 a campaign analyst may be resumed across reviews (never across a change in what it may read); R7.2 quantized readouts get a predicted reading on the grid and a not-resolvable mark; R7.11 pointer to the new columns; R7.14 scoped to project claims; R7.28 split complaints, unverifiable levers, structural changes last; R9.1 deterministic readouts; R9.5 bulk reads in the human's medium; R9.7 predictions committed before the readout, also for informal sets.
- From the source project's own practice (reverse analysis, "ahead" list): R2.5 content-checked seal pass-through (A5) and an append-only prefix guard described as a project option (A2); R7.22 optional fill-once ledger variant (A2); R8.15 optional numeric and verdict-word tripwire (A1); R9.15 and R7.31 `scope` column and the all-roles wire-in of a naming ruling (A3, A4).

- Also changed in v1.3 and not listed above (panel PRF-L8): §13 gains six rows (R9.14, R3.12, R9.16, R7.34, R7.35, R7.33) and the panel adds a seventh (relayed hold as a release channel); the §15 rows Thinker, Pre-registration and Peer messaging are updated; R1.3 notes that the Thinker's questions to the human are not advice (W8).

### Fixes to rules that looked wrong (B §5)
- W1 R9.11 (3) now reads "one change or one package" with signatures and a backout order. W2 the §12 row on relayed rules is split: permissions stay leads, restrictions are honored (R3.3, R3.4 point to R3.12). W3 R9.1 no longer sends a deterministic readout to a pilot. W4 R7.14 is scoped to project claims. W5 the reference helper refuses a commit with no role unless `--no-role` is passed. W8 the §1 Thinker row and R1.3 allow questions on a brief's grant. W9 `THINKER-HANDOFF.md` counts non-blank lines.
- W6 (numeric tripwire) and W7 (append-only guard) are described in R8.15 and R2.5 as project options; the reference helper does not implement them (see "Not applied").

### Templates and helper
- `DECISION-LOG.csv` (and the example) gains `scope`, `quote_fidelity`, `question`, `options`; `BRIEF.md` a "Questions to the human" field; `RESPONSE.md` a "Reads beyond the brief" header row and a "Human Q&A (verbatim)" section; `HANDOFF-FILE.md` §6 (superseded by the panel: it is now a view of the holds table); `HANDOFF-COMMAND.md` and `START-COMMAND.md` the wire-in row "ruling → decision log and every standard it contradicts", the peer-close wire-in pass and the open holds in take-stock; `THINKER-HANDOFF.md` "≤ 40 non-blank lines"; `ROLE-CHARTER.md`, `SUBAGENT-BRIEF.md`, `STRUCTURE.md` (two placement rows), `WRITE-SCOPES.md` (peer-built tool row), `PEER-MESSAGE-PROTOCOL.md` (relayed restrictions).
- `commit_paths.py`: refuses a commit with no role (exchange step; the suite grew from 16 to 17 tests, which the panel ran and passed); docstring and version string updated; README smoke test 1 and the test counts in README updated. The panel then changed it again (see below): role list, `--no-role REASON`, env fallbacks.

### Appendix
- Incidents #36–#46, evidence cited generically.

### Review panel (R7.16)
v1.3 went through the five-seat panel after the exchange step: 79 findings (C 0, H 13, M 34, L 32), 51 applied, 26 applied with a change, 2 declined. The Arbiter ruled six cross-seat points:
- **R-1 relayed holds (R3.12):** a relayed hold only restricts, never permits. State `held (relayed, unconfirmed)`; the releaser is always the human, never the relayer or a role it names; the receiver confirms the hold with the human at the next contact; any release needs the human's own words, recorded verbatim. Holds live in a small holds table (`templates/HOLDS.csv`: id, scope, source, state, release condition; part of the minimum), read by the start command and listed in the take-stock and the start report; tools reading it fail closed. A decision-log row below `verbatim`, and a new `relayed-by-<role>` fidelity value, is a lead until the human confirms it and does not bind (R7.31). Handoff §6 became a view of the table and joined the minimum handoff.
- **R-2 the Thinker's questions (R4.14):** only when the brief grants them and states that no held step involves the human (or names the held steps and forbids touching them); value-free; screened by the Arbiter while any held step is open; Human Q&A moved out of the value-free body.
- **R-3 always-on rules:** R7.28, R7.32, R7.34 and R7.35 stay in §7 with an "on regardless of the evidence knob" clause (cleaner than renumbering into §9); every new rule a session must follow is cited in the start command's standing rules, the charter or the rules file; a §15 row "Applied-work discipline" gives the small form.
- **R-4 migration:** rows written before the columns existed get `quote_fidelity` `legacy`, are not demoted and are confirmed only when next relied on; the adoption is a decision-log row naming the cut-off.
- **R-5 answer first (R9.17, R9.7):** the prediction commit lands before any readout of the data it predicts; answer-first governs reply order only, never data access; the commit is the next tool call of the same turn; other owed bookkeeping goes to the journal as `owed:` lines that the take-stock lists.
- **R-6 helper:** the refusal no longer names the bypass; the role is validated against `ROLES`; `$PEERING_ROLE` stays as a validated fallback documented in the README; `--no-role REASON` writes a visible trailer, and the harness `ask` list covers it; `$PEERING_HELD_FILE` and a `REQUIRE_HELD_FILE` switch close the opt-in held-list gap. Suite: 17 tests passed in the panel's runs before these changes; the revised suite has 23 and was not run by the writer (no shell): run `python3 -m unittest test_commit_paths` in `templates/` before release.
- Also: R9.13's ladder is now the "advice ladder" (R7.1's class ladder keeps "evidence ladder"); R2.13 grows (fixtures, wire-in trigger, refusal tests); R6.13 gains sentinels and a map owner; R6.5 gains a resume checkpoint; R7.31 gains the CSV writing rules and the verbatim-pointer requirement; R7.35 enumerates from the source of truth; the `ready` state is renamed `deferred`; British spellings and the catalog / catalogue mix are fixed; templates gain the holds table, a REVIEW-REPORT checklist for R7.33, a PREREGISTRATION quantized-readout row and an "On hold" section in the Thinker handoff.

### Not applied
- Helper options `--append-only` (prefix guard, optional fill-once mode, W7) and `--value-free-paths` with `--allow-values` (numeric tripwire, W6): larger changes needing several new tests; documented as project options in R2.5 and R8.15, left out of the reference helper.
- Decision-log header comment (B §9): a comment line would break the CSV readers that fail closed; the column meanings live in R7.31.

## v1.2 (2026-10-04)

Produced from a two-way exchange with the source project's sessions: the gap analysis of what the source project learned after v1.1, plus lessons from its Operator and Thinker sessions. Then run through the five-seat review panel (R7.16): 87 findings, all addressed (see "Review panel (R7.16)" below). Keyed to appendix incidents #24–#35 (new in this version). No existing rule id was renumbered or moved; v1.1 R8.4 and R10.5 and the §15 "Pinned tools" and "Pre-registration" rows were corrected.

### Investigation phase (knob: investigation; incident #35, appendix lesson 9)
- New R7.17–R7.22: investigate before choosing what to test; fact sheet and divergent generation with lens cards; merge with mandatory rival slots; averaged probability sheets with two seals around a red team; kill plan with a falsifiability gate; a self-scoring ledger. New templates `INVESTIGATION.md`, `LENS-CARDS.md`, `INVESTIGATION-LEDGER.csv`; `RESPONSE.md` gets merge and plan shapes (R4.9).
- New R6.11 isolate by staging, not by instruction; R6.12 dry-run mechanical instructions before fanning out (incident #35).
- New R4.13 design processes in two rounds.

### Scoring and records (incidents #29, #30, #31)
- New R7.23 scorer built from the pre-registration text, gaps ruled before data; R7.24 what counts as the one scoring run; R7.25 rulings after data exist and before the outcome is read; R7.26 late facts and post hoc splits are leads; R7.27 a defect in shared analysis code is a finding against every record that used it; R7.28 a remedy must act where the fault lives.
- `PREREGISTRATION.md`: post-session question, derivation chain, plausible range, gap in standard errors with a failure rule, scorer line, scorer snapshot and pins, strict-reading column.
- R7.2, R7.4, R7.5 point to the new rules.

### Blinding, pins and data (incidents #26, #27, #28)
- New R8.15 value-free commit subjects for every scored result (R8.4 now points to it; R8.7 gains a `metadata` channel); R8.16 clearance enforced by the tools, fail closed.
- R4.11 and R8.10: read lists name exact lines, and readers use `git log --format=%h`.
- New R10.8 pin snapshots, not live shared tools, and pins retire with their test; R10.5 amended. §15 "Pinned tools" corrected (the high-risk cell no longer freezes every tool that touches records).
- New R10.9 destroying raw data: catalog first, the human runs the delete; `settings-permissions.json` gets an `rm` deny placeholder.

### Wire-in and voice (incidents #25, #32, #34)
- New R5.15 done means wired in: wire-in table, "Wired this session" and "Open wire-in" in every handoff, verified by R5.7; handoff and start templates updated (Arbiter handoff steps renumbered: wire-in is new step 4, so old steps 4–10 are now 5–11; Operator wire-in is new step 3, old 3–9 are now 4–10; Thinker wire-in is new step 3, old 3–7 are now 4–8).
- New R2.10 write only in your own voice (R3.9 extended to files); R2.11 normalize on receipt.
- `SUBAGENT-BRIEF.md`: staged input directory, provenance line, voice and scorer-builder rules.

### The human's burden (incidents #24, #33)
- New R9.9 informal by default for the human's own applied work (§15 "Pre-registration" default corrected); R9.10 the human's personal space is not project inventory; R9.11 human-facing advice in three labeled parts; R9.12 own errors plainly.
- Amended: R9.3 (the human's vocabulary carries rules), R9.4 (scratch slot), R9.6 (pre-flight rules).

### Amendments to existing rules (ids unchanged)
- R3.1 / R3.11 pure acknowledgments batched; R3.2 line counts soft, no pasted data binding; R3.6 outbox may be replaced by a live message plus a committed file where resets are rare (§15 small cell); R3.9 files claiming a role.
- R4.4 `answer:` path; R4.5 quoted case values record exposure; R4.7 strippable header; R4.9 merge and plan shapes; R4.10 the log row is the record; R4.12 advance authorization in the Thinker's chat (panel-amended: it travels as a decision-log row, never through memory).
- R5.9 offline analysis the human already asked for may run before the choice; R6.3 "For the human" block.
- Appendix: incidents #24–#35, a second instance under #19, lesson 9. §13: five new anti-pattern rows. §15: new "Investigation phase" row and corrected rows.

### From the source project's own practice (the exchange's "ahead" list; no incident cites, the source records none)
- New R2.12 tool registry, reuse before building (`STRUCTURE.md` §3b); R7.29 prove "outside the fit set" mechanically; R7.30 method docs carry a pitfalls table; R8.17 the held list is machine-read (panel: the CSV is the record, `PENDING-BLINDED-STEPS.md` a view).
- Amended: R2.3 stubs in the path map (`STRUCTURE.md` §3 gains kind and remove-when); R2.5 check ladder and hook constraints; R7.8 hooks pass a pair's seal commit; R7.14 repetition may be the unit when a measured block effect is ≈ 0; R5.9 automation table; R5.10 writer's "not re-run" list (`HANDOFF-FILE.md` §10); R8.7 per-computation granularity (`EXPOSURE-LOG.md`).
- New template `AUTOMATION-RUNS.md`.

### Review panel (R7.16)
v1.2 went through the five-seat panel after the exchange. The Arbiter ruled nine cross-seat points.
- **Memory is not an authorization channel:** R4.12 now routes the Thinker's advance authorization through a decision-log row; R11.5 states memory never carries an authorization or ruling and may only mirror a decision-log id.
- **The held list has one machine-read source:** `templates/PENDING-BLINDED-STEPS.csv` is the record, the Markdown file a generated view (R8.3, R8.17, now a knob). `commit_paths.py --held-file` reads CSV only and fails closed (missing or unreadable file, non-CSV, missing columns, any status other than exactly `released`); it also checks family ids, an extended verdict-word list and secrets in the commit message, and refuses a `lease --release` for another role. Docstring and version string updated; the suite grew from 10 to 16 tests; README smoke test 1 updated.
- **Auto-loaded context stated plainly (R6.11, R7.20, R11.6):** staging hides paths but subagents still auto-load the rules file and memory, so those never carry outcome values of held or scored steps; strict blindness needs a separate session whose working directory is the staged folder; "fresh agent with no project memory" claims reworded; a post-run read audit where transcripts exist.
- **Investigation phase:** rankers respawn with their own seal-1 sheet plus the round-2 inputs when the parent session has ended, recorded as a ledger deviation (R7.20); the hunch lives in its own file `00b-hunch.md`, never staged (R7.18 a); the ledger has `seal` and `resolution` rows (R7.22, `INVESTIGATION-LEDGER.csv` gains `row_kind` and `merger_only_winner`); the phase is **off in the Default column** with a turn-on trigger (§15, Quick start B), and the expected wall-clock time is reported before step 1.
- **Disclosure:** the Thinker's start prints commit ids and paths only for commits touching scored or held records, never subjects (START-COMMAND step 4, R8.10, R8.15); pre-scans print counts, never matching lines (R4.11).
- **Wire-in is core (R5.15):** in the core-rules box, Quick start A and the minimal example; the actual table is in both command templates; held-family items are listed as `open wire-in: held (step <id>)`.
- **Knobs closed:** new §15 rows and Quick start B triggers for wire-in, tool registry (R2.12 now a knob; the Key commands list is the registry in the minimum), automation runs, data intake and the machine-read held list; the investigation row states its prerequisites.
- Also: R10.2 bans `stash` in any form; R10.9 guarded-script specification and deny-is-a-speed-bump note; R10.5 and R10.8 aligned with §15; R10.1 exempts staging directories and byte-identical output copies; R2.5 hook pass-through limits; R2.11 chain of custody; R3.6 small-variant recovery; R5.9 offline analysis needs a recorded ask; R6.3 output-header order; R7.23 builder gets non-outcome inputs only; R9.9 single ask; R1.11 per-investigation Arbiter instance; `settings-permissions.json` gains an `ask` list and more denies; `PEER-MESSAGE-PROTOCOL.md`, `PREREGISTRATION.md` §B and several template headers brought in line.

### Not applied
- Optional `--scored-file` helper option (R8.15 enforcement in `commit_paths.py`): not applied. The helper now also refuses a held step or family id next to an extended verdict-word list, but it enforces R8.4 only; R8.15 is checked by the commit's author and by review (R8.15 says so).

## v1.1 (2026-10-03)

Produced by the full review panel (GUIDELINES R7.16): five read-only reviews in parallel plus the Thinker's response, then one writer applying every finding. 174 findings: 150 applied as proposed, 22 applied in modified form, 2 applied with one part declined, 0 declined outright. Plus one addition from the human (the review panel itself).

### Blinding: every visible channel (safety C1, agentic C1, Thinker R-1, C-1, C-4, C-5, architecture H4, H5)
- R8.2 rewritten: every visible channel is a reply (tool output, subagent returns, commit subjects and the `git log` that starts print, file names, class changes, rankings, generated reports, memory, the decision log, brief read lists).
- New: R8.4 embargo for held families with a neutral commit subject (enforced by the helper's `--held-file`); R8.5 value-free returns and no visible reads; R8.6 the human-facing role stays clean; R8.7 per-role exposure files, self-logged from any channel, the Arbiter included; R8.8 mid-task exposure procedure; R8.9 declared human-readable set (H column in the write scopes); R8.10 brief read-list guard and the exposed-author leak check; R8.11 the standing seal outranks the moment; R8.14 seal outside the tree (knob).
- R1.3: nothing of a held step is handed to the Operator; reports for the human are the Operator's voice.
- R4.7: value-free response body, exposed appendix; R4.11 Thinker pre-scan.
- The pending-blinded-steps list is values-free and readable by every role (new template).
- v1.0 R8.5 and R8.6 became R8.12 and R8.13 (text unchanged); R8.1 and R8.3 amended.

### Minimum-viable path and the human's job (usability C1, H1, H3, H4; architecture M10)
- README rewritten: "Your job as the human" (do / say / decide), "Harness requirements" (Claude Code mapping and fallbacks), prerequisites, Quick start A (two roles, under an hour, timed), Quick start B (knobs with triggers), smoke tests, a translation table for software, writing and ops, a file map with "required at" and "read when", and 33 vocabulary rows.
- Every template tags its optional lines `KNOB`; GUIDELINES gets a core-rules box and knob labels on §4, §7, §8.
- New `examples/minimal-setup.md` with filled minimum files for an invented project.

### Commit helper and git safety (agentic H1, H9, M8; usability H2; safety H7, M1, M2; architecture L7)
- New `templates/commit_paths.py` (stdlib; flock; intent-to-add for new files; refuses `.`, globs, pathspec magic, directories, detached HEAD, frozen-path changes, likely secrets, held-step verdict subjects; adjacent pairs with `--and`; role leases) and `test_commit_paths.py` (10 tests).
- R10.2: the full destructive-git ban list. New R10.6 (harness deny list, `templates/settings-permissions.json`), R10.7 (no secrets), R7.15 (anchor proof hashes, knob).
- Start and handoff commands get `allowed-tools` front matter.

### Architecture (architecture H1–H3, H6, M1–M7, M11; agentic H2, H3, H5, H6, M4, M5; Thinker C-2, C-3)
- New R1.7 Arbiter unavailable (degraded mode, deputy by DEC row); R1.8 one live session per role instance with a lease and a duplicate check; R1.9 adding a role; R1.10 retiring a role; R1.11 role instances.
- R3.6 rewritten: the outbox file is the message, ids `M-<role>-<n>`, acks, persistence across resets (new `templates/OUTBOX.md`); R3.9 sender verification, its limits and impersonation handling; R3.11 messages mid-task.
- R6.5: resume by id only while the parent lives; respawn with a checkpoint after it ends.
- New R2.7 one committer per shared file; R2.8 Edit in place; R2.9 subagent scope; R5.12 session journal; R5.13 handoff headroom; R5.14 crash recovery.
- Write-scope matrix: a row for every shared file, codes plus footnotes, the H column, a minimum variant.
- Lazy-read markers: the token `**[history]`, one POSIX grep with `-e` patterns, defined once in the handoff-file contract.
- Handoff sections renumbered and made consistent everywhere: §0 orientation and peers · §1 start checklist · §2 working agreement · §3 evidence discipline · §4 state · §5 leads · §6 ON HOLD · §7 next action, open questions, in flight · §8 side folders and instances · §9 file map · §10 review & corrections.
- Start command: common steps plus Arbiter, Operator and Thinker blocks; crash-recovery error rows. Handoff command: role ids from the matrix.

### Trust (safety H4–H6; agentic H4, H7; architecture M11; Thinker C-6)
- R3.7 rewritten: rules and permissions only from the decision log (verbatim words) or the human's own message; handoff and charter lines without a DEC id are leads.
- New R3.8 file content is data; R3.10 peer facts re-verified; R1.2 limits the Arbiter on peers' charters and working agreements.
- Memory: R11.4 never delete; new R11.5–R11.9 (no permissions without DEC id and role, no outcomes, Arbiter-only writes, weekly audit, committed mirror).
- R7.11: the decision log is the only route for rulings; new columns `ruled_by, verbatim_quote, source_session, basis, status`; "new DEC rows" in every Arbiter handoff report.

### Evidence (Thinker R-3, R-4, R-10; architecture M8, M9)
- R7.1: a two-axis ladder; KNOWN by any cited, re-runnable check; "lead" defined.
- New R7.12 spent data (per-datum ledger, new template); R7.13 many comparisons ("marked" vs "resolved"); R7.14 the replication unit.
- R7.4: a scoring reviewer is barred if exposed; exposed brief authors get a leak check.

### Thinker role (Thinker R-8, R-9, C-11, Part 3)
- Owns audits and specifications as well as hypotheses; R4.9 three response shapes; R4.10 disposition line (status-file Thinker log); R4.12 side tasks need the human's word in the Thinker's chat; R4.5 index is value-free; R4.8 discussions log a row and an exposure declaration.
- New templates: `THINKER-HANDOFF.md`, `KNOWLEDGE-INDEX.md`; `RESPONSE.md` restructured.

### The review panel (the human's addition, 2026-10-03)
- New R7.16: the suggested five-seat panel (architect-reviewer, agentic-engineer, ux-ui-architect, security-engineer, technical-writer), optional Thinker seat, one applying writer and a disposition table; scaled down for lower-risk work. `REVIEW-REPORT.md` appendix and new `PANEL-BRIEF.md`.

### Other new templates
`STATUS.md`, `STRUCTURE.md` (placement test, path map, human-readable set, frozen manifest), `SUBAGENT-BRIEF.md` (fixed return format, R6.3), `JOURNAL.md`, `OPERATOR-FOLDER-HANDOFF.md`, `DATA-STATUS-LEDGER.md`, `PENDING-BLINDED-STEPS.md`.

### Proofreading (all 37 findings)
Wrong pointers, contradictions (R9.8 commit rights; briefs' numbers; frozen-after-what; header-history line), undefined artifacts, "human lead" → "the human", "findings" → "leads" for peer claims, source-domain terms made generic, `<=` → `≤`, placeholder case, capitalization in §12, "Idiot-proof" → "Step-by-step", "Laundered permission" → "Relayed permission (handled correctly)".

## v1.0 (2026-10-03)
First extraction from the source project.
