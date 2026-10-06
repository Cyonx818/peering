# Now: <PROJECT>

File: `<now path>` | Committer: Arbiter; each role writes its own "next action" row at its own handoff (R2.7) | Read by every session at start | In the human-readable set (R8.9) | GUIDELINES R5.16, R5.9
<!-- KNOB: status file. Size guide: about <40> non-blank lines; it warns, never blocks (R6.7). Overwritten at every
     handoff; never gains a dated section. Pointers, not narrative. Held families as `held (step <id>)` only (R8.4);
     a next action that follows from a held step's result (re-run, extend, retire, change a lever) is written
     `held (step <id>)` too, and the action itself lives in the Arbiter's handoff outside the human-readable set (R8.1).
     This file is the ONE record of the next action and of the last session end (R5.16); the handoffs and examples
     point to it. A start parser that finds this file empty stops with "slice empty: record restructured?" (R2.14).
     The session-start commit (R5.7) is the HEAD recorded in "Last session end". -->

## Current cycle
- Last session end: <role>, session <n>, <YYYY-MM-DD>; HEAD before the handoff commit (= handoff §1 row 6) `<short hash>`.
- Session start (R5.7): <role>, session <n>, HEAD `<short hash>` = the session-start commit; the role's own session writes this line, one helper call, and journals the same hash as the first journal line.
- Cycle: <one line: what the project is doing now; pointer to the record>.
- Last full check: <repo checks and tests: result, date, commit>.

## Next action per role
| Role | Next action (the record; the handoff §7 points here) | As of | Pointer |
|---|---|---|---|
| Arbiter | <one action; first concrete step> | <YYYY-MM-DD> | <handoff §7> |
| Operator | <one action; first concrete step> | <YYYY-MM-DD> | <folder handoff> |
| Thinker <!-- KNOB: Thinker; the Thinker commits only HANDOFF.md, so the Arbiter refreshes this row from it --> | <one action or "wait for a brief"> | <YYYY-MM-DD> | <HANDOFF.md> |

## Open holds
<ids from the holds table, unconfirmed first, or "none"> (R3.12)

## Pointers
- Status ledger: `<status path>`; handoffs: `<paths>`; decision log: `<path>`; holds: `<path>`.
