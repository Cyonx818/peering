# Response: <topic>

File: `response-<YYYY-MM-DD>-<topic>.md` (same date and topic as the brief)
<!-- Keep ONE body shape (hypotheses, audit, specification, merge or plan, as the brief names) and delete the others.
     Lines tagged KNOB are optional; see GUIDELINES §15. -->

## Header
| Field | Value |
|---|---|
| Brief | `brief-<YYYY-MM-DD>-<topic>.md` @ `<commit hash>` (committed and clean when read) |
| Shape | hypotheses / audit / specification / merge / plan |
| Files read | `<path>` §<…>; `<path>` §<…> |
| Reads beyond the brief | none / <query or file>, purpose (R4.6) |
| Pre-scan | every file read was grepped for held identifiers first: <clean / hit at … → stopped, ruling …> |
| Exposure | none / <files, data, families seen that carry outcome values; channel>; rows in `exposure/thinker.md` |
| Class of everything below | lead (lowest class) |
| Cost <!-- KNOB: cost --> | <bytes or tokens read; agent runs requested> |

---

## Body (value-free: no outcome values; a predictor may read this part after the Arbiter certifies it, R4.7)

### Shape A: hypotheses
| # | Hypothesis | Mechanism | Variables / signals involved | Separating test | Expected gap (rough) | Cost tier |
|---|---|---|---|---|---|---|
| 1 | | | | | | offline / cheap ask / human session |

**Rivals and what kills each:** <for the top hypotheses: the rival, the observation that separates them, and by how much.>

### Shape B: audit
| # | Defect | Why it matters | Cheapest check | Expected effect if fixed | Severity |
|---|---|---|---|---|---|
| 1 | | | | | C / H / M / L |

### Shape C: specification
| # | Decision (not an option) | Acceptance test (numeric) | Dose and noise model | Why | Kill test (the check that would show it wrong; R4.9) |
|---|---|---|---|---|---|
| 1 | | | | | |

For a design or method answer in any shape, add one line: **Kill test:** <the check that would show the design wrong>. A recommendation without one is a hypothesis to test, not a design to adopt (R4.9).

### Shape D: merge <!-- KNOB: investigation (R7.19) -->
Clusters (5–8 hypotheses, each one sentence a ranker can put a probability on) · is / is-not test per hypothesis · mandatory slots (can't-miss, measurement artifact, subject adaptation, reference artifact, catch-all; `slot-fill` / `unfilled`) · evidence matrix (consistent / inconsistent / neutral; credibility; shared-source marks) · key evidence item · most diagnostic untested comparison · causal diagram per comparison · clusters only the merger produced (dependence signal). The ranker part carries no author names, cluster sizes or counts.

### Shape E: plan <!-- KNOB: investigation (R7.21) -->
| Hypothesis | Observable | Interval and plausible range | Rival interval | Gap in se (sd: file, n; block as unit) | Failure rule | Test, order, dose | Pursuit value | Advice line |
|---|---|---|---|---|---|---|---|---|

One branch per UNKNOWN in the fact sheet; an advice line for the catch-all.

### For the human
<Ideas in plain words for the human, each marked as a lead.>

### What the Arbiter must re-derive before pre-registering
- <number or assumption>

### Comparisons
<If several comparisons are proposed: their number, the correction, the expected false marks; "marked" vs "resolved" (R7.13).>

### Questions back
1. <one precise question>

---

## Strippable header (only if a record must carry fit-set or panel values, R4.7)
<!-- ARBITER STRIPS THIS SECTION BEFORE STAGING: the predictor receives the body only. -->
<values, if any>

## Exposed appendix (only if needed; every number tagged `exposed-derived`; never handed to a predictor)
| Item | Value | Derived from (file, family) |
|---|---|---|

## Human Q&A (not part of the body; never staged for a predictor, R4.7) <!-- KNOB: Thinker; only when the brief granted questions to the human (R4.14) -->
Screened by the Arbiter before the human saw them: <date / not needed (no held step open)>. Where the harness had no structured question tool: the question and lettered options were sent as one message, logged here verbatim.

| # | Question | Options offered (verbatim) | Pick and free text (verbatim) | If unanswered: how settled |
|---|---|---|---|---|
| 1 | | | | |

An answer that carries an outcome value or direction of a held or scored step is an exposure: declared in the Header and in `exposure/thinker.md` (R4.6). Rulings among the answers are proposed to the Arbiter through the outbox, citing this table's row, and are not applied (R7.11, R7.31).

<!-- The Arbiter commits this response before anything cites it (R4.3), then writes a disposition line in the
     status file's Thinker log (R4.10). Pairs are append-only; corrections and follow-ups are new pairs. -->
