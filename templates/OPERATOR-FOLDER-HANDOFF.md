# Operator folder handoff: <item id> <topic>

<!-- One pair per work folder: 99-handoff.md (this file: the state, the authority) and
     99-next-session-prompt.md (below the line: only what to read, R5.1). Every line cites a commit or file.
     A current-state record as in HANDOFF-FILE.md (R5.16): rows edited in place, no [history] blocks; the old version
     stays in version control. Lines tagged KNOB are optional. -->

**Header.** <date>, session <n>. <One paragraph: what the human did, what we now know, the next step.>

## State
| Item | Confirmed by the human? | Source (commit / file) |
|---|---|---|
| <setting / version, named only as the human saved it (R9.4)> | yes / no stated change (R9.3) | <…> |

## Next step
<Options with sources; what each buys and why this many (R9.1); floor and cap, each with its basis; the counted unit and its overhead. **Not needed this round:** <what the human need not do> (R9.1). The human chooses.>

## Loop state <!-- KNOB: applied-work discipline (R6.16, R9.19–R9.21; iterative applied work) -->
| Row | Value |
|---|---|
| Unused metrics (R6.16) | <metric → rounds unused (count); updated each round so the drop rule survives a reset> |
| Loop log | <pointer to the loop log: per round what changed the decision, what was computed and changed nothing (R6.16)> |
| Stop-call state (R9.19) | <rounds so far; consecutive null rounds from different hypotheses; best remaining lever vs the human's noise at a practical dose; "continue" / "say stop"> |
| Workflow log (R14.3) | <pointer to the log of a repeating workflow (per step worked / failed / lesson; human time; predictions scored) and to the per-candidate data kept; the next run starts from its lessons> |
| Pre-relay checker (R9.25) | <result per package: pass / hit fixed / hit overridden with reason; path of the script's output> |
| First package complete designed set (R9.27) | <yes / ledger path; checker coverage result, including what it skipped (R2.15), or "script-listed, audited by hand" where no checker exists; the reviewer's hits; "no data" rows with the sources searched> |
| Settings set by the human's preference (R9.19) | <settings with no footprint at N tried values, frozen at the human's choice> |
| Verdicts re-applied to the decision rule by a tested script (R6.1, R6.15) | <corrections made before relay / none> |
| Confounds checked before crediting a primary (R9.14) | <everything else that changed in the phase, including what the human did differently / none found> |
| Round order (R8.18 (8), R9.22) | <report first / analysis first / values first (only by the human's ruling: DEC id); skipped rounds logged "unscored"> |
| Targets (R9.20) | <exemplars and what they share; not a single liked result as the target> |

## Protocol that worked
<steps; walkthrough set size and why>

## Tools
| Tool | One line |
|---|---|

## Rules to keep
Dose rule; the human states changes; naming follows the human's act; nothing of a held step in any visible channel. <!-- KNOB: blinding -->

## In flight
pre-registrations sent to the Arbiter and their status: <…> · sealed files <!-- KNOB -->: <…> · data not yet registered or scored: <…> · questions to the human: <…> · outbox items open: <M-ids> · open wire-in: <item → surface, owner, or "none"; R5.15>

## Intake register <!-- KNOB: data intake -->
| Old name | New name | sha256 |
|---|---|---|
<!-- R2.11: files the human delivered, renamed on receipt before any analysis. -->

## Corrections given to the human this session
<what was wrong, what the fix is, where the record was corrected (R9.12); or "none">

---

# 99-next-session-prompt.md

You are the Operator for `<item id>`. Read, in order: the rules file (auto-loaded); `<this folder>/99-handoff.md` current blocks; `<files the next step needs>`. Then follow the Operator role block of the start command. Do not read: <list>.
