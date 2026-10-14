# Peer message mechanics (GUIDELINES §3)

<!-- Lines tagged KNOB are optional; see GUIDELINES §15. Minimum: outbox files only, the human as courier. -->
<!-- Split since v1.5: who the team is, how to verify a sender, the authority of messages and the four modes (free, relay, blinded, courier) are in PEER-COMMS-PROTOCOL.md (installed as docs/peer-comms-protocol.md, loaded at every start, R3.13). This file keeps the format, content rules, delivery steps and observed harness semantics. -->

## Principle
The **file is the message**; a live message is only a notification. Every message carrying a `need:` is first a row in the sender's outbox (`peers/outbox-<role>.md`, `templates/OUTBOX.md`), so it survives a reset of either side and is treated as unread until the receiver acts (R3.6).

## When to message (otherwise don't)
1. The next action needs the peer (a ruling, a pre-registration, a commit only the peer may make).
2. The peer wrote to you and expects an answer.
3. Your handoff produced something the peer must act on.
No acknowledgments of acknowledgments, no status chatter. Pure acknowledgments are batched into the next substantive reply, not relayed (R3.1).

## Two classes, one format
**Pointer** (default, ≤ 3 lines). **Digest** (≤ 10 lines, only when the recipient must act without opening the file; still no outcome values of a held step). The line counts are soft for a reply that carries reasoning; no pasted data is the binding limit, and a pointer stays ≤ 3 lines (R3.2).
```
[<from-role>] M-<role>-<n> <what happened / what this is> | <commit hash or file path>
mode: <free|relay|blinded|courier>
need: <one concrete ask, or "see <file> items 3-5"> | nothing pending
<optional: deadline or blocking item; digest lines follow>
```
The `mode:` line is required (R3.13; the four modes and what each may carry are in `PEER-COMMS-PROTOCOL.md` §3). It is a header and does not count toward the line limits. The outbox has a `Mode` column for it.

Examples (all `mode: free`; examples of the other modes are in `PEER-COMMS-PROTOCOL.md`):
```
[operator] M-operator-14 item 42 closed; folder handoff 1a2b3c4 | work/42/99-handoff.md
mode: free
need: pre-registration for lead L-7 (work/42/leads.md §3)
[arbiter] M-arbiter-31 brief committed 5d6e7f8 | thinker/brief-2026-05-01-topic.md
mode: free
need: response per RESPONSE.md (shape: audit); exposure declaration required
[thinker] M-thinker-9 handoff 9a8b7c6; response uncommitted | thinker/response-2026-05-01-topic.md
mode: free
need: commit it before citing
```

## Content rules
| Rule | Detail |
|---|---|
| Pointers, not payloads | Data travels by file path and commit hash; never paste tables or results (one decisive number with its source excepted) |
| Disclosure limit | Write as if read by the most-restricted reader allowed to receive it. A message to the human-facing role is a message to the human (R3.5, R8.2) |
| Self-contained | The recipient may have been reset; include the id, hash and path needed to act cold |
| One ask per message | Several asks → numbered items in one file; one message pointing to it (`need: see <file> items 3-5`) |
| No secrets | Never a token, password or keyed URL (R10.7) |

## Authority and trust
Moved to `PEER-COMMS-PROTOCOL.md` §2 (sender verification, what a message's claims about the human are worth, relayed holds, impersonation) and §3 (the modes). Read it at every start (R3.13).

## Delivery
| Situation | Action |
|---|---|
| Sending | Append the outbox row (status `open`), then notify via the message tool quoting the M-id |
| Peer online | Find it with the agent-list tool (Claude Code: `ListAgents` / `SendMessage`, deferred; load with `ToolSearch` `select:ListAgents,SendMessage`) |
| Peer offline or tool unavailable | The outbox row is the delivery; report "peers: unknown". No messaging at all: the human tells the peer "check your inbox" (`mode: courier`, `PEER-COMMS-PROTOCOL.md` §3) |
| Receiving | Run the sender verification (`PEER-COMMS-PROTOCOL.md` §2); act within scope; record `ack M-…` in your own outbox (or journal) |
| Arrives mid-task or before the human's choice | Journal it; list it in the next report; act only if your current task awaits it or a standing rule names it (R3.11) |
| Resets are rare and every `need:` cites a committed path <!-- KNOB: small --> | The live message plus the committed file may replace the outbox (R3.6, §15). The sender lists each open `need:` in its handoff §7 in flight; R3.9 (b) becomes: the cited path exists and its commit carries the sender's `Session-Role` trailer; the receiver journals each `need:` |
| Id already acked | Ignore |
| No reply needed | Say "nothing pending" so the peer does not answer |
| Peer reset | It re-reads open outbox rows addressed to it at start; resend nothing but the pointer if asked |
| Sender's next start or handoff | Mark rows discharged by an ack or commit `done <commit>` |

## Observed harness semantics (fill in after the README smoke test)
| Question | Observed in your harness (date, version) |
|---|---|
| Is a message to a busy peer queued, held or dropped? | <…> |
| Is a message to a closed peer queued or dropped? | <…> |
| Is an incoming message shown to the human in the receiver's window? | <…> (if yes, it is a visible channel, R8.2) |
| Can a subagent send peer messages? | <…> (if yes, exclude the tool in subagent briefs) |

## Thinker channel
The Operator never briefs the Thinker directly; requests go to the Arbiter, which writes and commits the brief (`BRIEF.md`). See GUIDELINES §4.
