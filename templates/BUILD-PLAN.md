# Build plan: <what is built>

File: `<docs>/plans/<YYYY-MM-DD>-<topic>.md` | Owner: Arbiter | GUIDELINES R4.16, R6.17, R7.44–R7.47
<!-- A design memo for a multi-phase method or tool build. Written by the Arbiter (or a role it names), vetted by the
     Thinker (brief/response pair) or, with the Thinker knob off, by one fresh read-only reviewer subagent briefed with
     REVIEW-REPORT.md (R4.16, R7.7), built in phases. Each phase's rulings are written here as one line each; every
     vetting item a phase adopts is wired into the method doc in that phase's commit. At the end the memo is
     consolidated into the method doc and marked superseded. Lines tagged KNOB are optional; see GUIDELINES §15. -->

## 0. Summary
- **Goal:** <what the build lets the human or a role do that it cannot do now; the decision it feeds>.
- **Cost of this design:** <tokens, sessions, human time; the estimate and its basis (R6.17: the R6.10 cost notes, or "estimate, no basis")> | **Cheaper alternative (R6.17):** <design, cost, what it gives up> | **Chosen:** <which, by whom; the human's word if the trade is theirs (R12.1)>.
- **Touches:** <pinned tools, frozen records, history, shared tools a peer runs live (R10.11): none | list>.
- **Status:** draft | vetted `<response path>` @ `<hash>` | phase <n> built | superseded by `<method doc>`.

## 1. Decisions, each with alternatives and a fallback
| # | Decision | Alternatives considered | Why this one | Fallback if the data fails it | Kill test (R4.9) |
|---|---|---|---|---|---|
| D1 | | | | | |

A rule proposed offline is expected to meet data it fails on: every decision names its fallback before the build. A fallback taken is recorded in section 4 and flagged in the artifact's header (R7.10).

## 2. Phases
| Phase | Deliverable | Acceptance test (could it fail on a wrong build? R7.45) | Reviews (code + adversarial, R7.7) | Phase commit (subject `Phase <n>: <topic>`; hash filled in the next phase's commit) |
|---|---|---|---|---|
| 1 | | | | |

Shared tools a peer runs are built and reviewed in a private clone and swapped in with a tool-swap notice (R10.11).

## 3. Vetting table (from the Thinker's response or the review report; filled when it is committed)
| Item | Vetting verdict (accept / accept with change / reject) | As built | Wired into the method doc (phase commit subject; hash filled next phase) |
|---|---|---|---|
| | | | |

## 4. Per-phase rulings (one line each)
| Phase | Ruling | Basis | Deviation from the vetting (and flag in the artifact header) |
|---|---|---|---|
| | | | |

## 5. Failure modes
| Failure mode | Handled by test | Open (owner) |
|---|---|---|
| | | |

Check each validity rule is two-ended (R7.44) and each tolerance or closure test compares against something the build did not fit (R7.45).

## 6. Generality check (R7.47)
A rule built on one case is run read-only on every other case on disk before it is called general.
| Rule part | Cases on disk | Held | Failed (stays fail closed; data that would settle it) |
|---|---|---|---|
| | | | |

## 7. Superseded
`Superseded by <method doc> on <date>`: the decision table (vetting verdict → as built) and the failure-mode table were consolidated there; this memo is kept as the event record.
