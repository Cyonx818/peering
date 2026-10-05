# Roles and write scopes

Decided by the human on <YYYY-MM-DD> (decision log `<DEC-id>`). GUIDELINES §2.
<!-- Lines tagged KNOB are optional; see GUIDELINES §15. Delete rows and columns for parts you do not use. -->

## Principles
1. The Arbiter can write anywhere; whether it should depends on the case. It is the final arbiter of conformance and may fix other roles' records; each fix is named in the commit message. Exceptions: frozen records, and other roles' charters and §2 working agreements (only a DEC-cited line may be added) (R1.2).
2. Other roles' scopes define primary stakeholding (who normally writes and is responsible), not walls for the Arbiter.
3. Only the Arbiter changes an evidence class. Peer leads enter the record through the Arbiter, by the class's own route (R7.1).
4. Frozen and sealed records are append-only for every role, the Arbiter included; they are listed in the frozen manifest.
5. **One committer per shared file** (R2.7): where several roles add rows, each writes its own file (one recorded exception: the holds table, footnote 19).
6. A subagent's scope is the subset of its spawner's scope named in its brief: one output path (W), named inputs (R), a forbidden list (N). It never commits, messages peers or addresses the human (R2.9).
7. Every commit goes through the helper with `--role`, which adds the `Session-Role: <role>` trailer (self-asserted). Out-of-scope paths warn (never block the Arbiter); frozen paths block everyone. The Arbiter owns the check script, the scope list and the hook.
8. **Human-readable set (H column):** files the human may open. During a held step every write to them passes the R8.2 check; results of a held step live only outside them (R8.9).

## Legend
**S** primary stakeholder (normally writes, responsible) · **W** write · **A** append-only · **P** propose (drafted by the role in its outbox or folder, applied by the stakeholder) · **R** read · **N** no-read (blinding) · **H** = yes: in the human-readable set. Numbers are footnotes below the table.

## Matrix (default: three roles)

| Path / file | Arbiter | Operator | Thinker | H |
|---|---|---|---|---|
| rules file (`CLAUDE.md`), structure doc, methods / playbook | S | P | P | yes |
| charter, goals | W¹ | R | R | yes |
| decision log | S² | P² | P² | yes |
| status file (incl. Thinker log, automation runs) <!-- KNOB --> | S | P | R | yes |
| pending-blinded-steps list: CSV record and Markdown view (values-free) <!-- KNOB: blinding --> | S | R | R | yes |
| holds table `holds.csv` (R3.12; in the minimum) | S; A¹⁹ | A¹⁹ | A¹⁹ | yes |
| exposure files `exposure/<role>.md` <!-- KNOB: blinding --> | S own; R all | S own | S own | no |
| per-datum ledger <!-- KNOB: evidence --> | S | P | N | no |
| source of truth (read-only primary data) | R | R | R | no |
| reference docs (data dictionary) | S | R | R | yes |
| knowledge (claims and classes) | S³ | R; P | R; P | yes⁴ |
| knowledge index (≤ 80 lines, value-free) <!-- KNOB: Thinker --> | S | R | R | yes |
| Operator quick-reference card <!-- KNOB --> | S | A⁵ | R | yes⁴ |
| applied work folders `<work>/<item>/` | W⁶ | S | R⁷ | yes⁴ |
| the human's preference / profile records | W⁶ | S | R | yes |
| intake catalog, raw-data ledgers <!-- KNOB: data intake --> | S | A⁸ | N | no |
| sealed material, hidden assignments, scores after seal <!-- KNOB: blinding --> | A⁹ | N¹⁰ | N | no |
| evidence (pre-registrations, readings, logs) <!-- KNOB: evidence --> | S¹¹ | P¹² | R¹³ | no |
| raw-data catalog and disposal records (R10.9) <!-- KNOB: data intake --> | S | P | N | no |
| investigation folder `<evidence>/investigations/<date>-<topic>/` <!-- KNOB: investigation --> | S | R¹⁶ | R¹⁷; P (via the Arbiter) | no |
| investigation ledger `<evidence>/investigations/ledger.csv` <!-- KNOB: investigation --> | S (rows appended, never edited; or "S (fill-once)" where the R7.22 variant is chosen and recorded in the decision log) | R | R | no |
| tools, tests; commit helper | S | P | R | no |
| a tool the Operator (or a role whose charter grants it) built in its own folder, with its fixtures, until promoted (R2.13) | R (promotes it) | S | N | no |
| tool registry <!-- KNOB: tool registry --> | S | P | R | no |
| check script, scope list, frozen manifest, hooks | S | P | P | no |
| session commands and prompts | S | P (own start fragments) | P (own start fragments) | no |
| Thinker briefs <!-- KNOB: Thinker --> | S | P (asks via the Arbiter) | R | no |
| Thinker responses <!-- KNOB: Thinker --> | A¹⁴ | R if asked | S¹⁴ ¹⁸ | no |
| each role's handoff file (incl. Thinker `HANDOFF.md`, Operator folder handoffs) | S own; W⁶ others | S own | S own | yes⁴ |
| outboxes `peers/outbox-<role>.md` | S own; R all | S own; R all | S own; R rows to it | no |
| journals `<role>/journal-<date>.md` | S own | S own | S own | no |
| memory entries and index; memory mirror <!-- KNOB: memory --> | S | P | P | yes |
| outside sources, research packets | S | R | R (packets only) | no |
| CHANGELOG, review reports, disposition tables | S | R | R | yes |
| `git log` (commit subjects and bodies) | — | — | — | yes¹⁵ |

**Footnotes**
1. On the human's instruction only, with a DEC row.
2. Arbiter is the only committer. Other roles propose rulings given in their chat through their outbox, the same session, with the human's verbatim words (R7.11).
3. Sole class writer. No class change for a held family until release (R8.4).
4. In the human-readable set: during a held step, no outcome, direction or ranking change of that step goes here.
5. Rows labeled LEAD / RULE / HUMAN only.
6. To bring a record to standard; fix named in the commit.
7. Only what a brief names.
8. Own registered items.
9. Append-only; no-read unless the step record names the Arbiter as reader.
10. N while the human is blinded on the step; R after release (R8.6).
11. Pre-registration §A–§H frozen at the pre-registration commit; §V and §R append-only.
12. Own pre-registration drafts, committed by the Arbiter before data.
13. Except paths listed for a held step in the pending list (R8.3).
14. Default: the Arbiter commits responses (R4.3); corrections are new records pointing to the old one. In degraded mode the Thinker commits its own (R1.7 a).
15. Commit messages are visible: neutral subjects for held steps (R8.4) and value-free subjects for every scored result (R8.15).
16. Nothing of a held step (R8.6); a flag that touches a held step waits for its release (R7.17).
17. The hunch (`00b-hunch.md`) and other generators' lists only after its own list is committed; as merger, what the INVESTIGATION allowed-inputs table names for the merger. The "Who sees what" table in the investigation's flag agrees with this matrix.
18. Including the one `answer:` path a committed brief names (R4.4): the brief is the grant, one file only.
19. The recorded exception to one committer per shared file (R2.7): the holds table is append-only; the role that receives a hold, or the human's confirmation or release, appends its row at once, one helper call per row, after the R2.8 dirty check. Rows are never edited; the latest row per hold id is current; only the human's own words move a hold to `released` (R3.12).

## Minimum variant (Quick start A: Arbiter + Operator)

| Path / file | Arbiter | Operator | H |
|---|---|---|---|
| rules file, structure doc | S | P | yes |
| decision log | S | P | yes |
| holds table `holds.csv` | S; A¹⁹ | A¹⁹ | yes |
| knowledge / records | S | R; P | yes |
| work folders | W⁶ | S | yes |
| tools, commit helper, checks | S | P | no |
| each role's handoff file | S own | S own | yes |
| outboxes, journals | S own | S own | no |

## Exceptions
| Path | Rule | Decided |
|---|---|---|
| <path> | <e.g. the Operator may run tool X; the tool's write to Y is allowed> | <date, DEC-id> |
