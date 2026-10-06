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
<Options with sources; what each buys and why this many (R9.1). The human chooses.>

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
