---
argument-hint: "[item id | all]  (optional; default = every item waiting on the human)"
description: "<PROJECT>: walk the human through every item waiting on them: context, options with pros and cons, a recommendation, what each unlocks. Reads only the declared state files, never conversation memory. Records answers as rulings."
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Agent, Edit(<journal dir>/queue-answers-*.md), Write(<journal dir>/queue-answers-*.md), Bash(git status:*), Bash(git rev-parse:*), Bash(python3 <scripts>/commit_paths.py:*)
---
<!--
Save as .claude/commands/<project>-queue.md. GUIDELINES R9.24. One command for the human; the human may run it any time.
Run it in the Arbiter's or the Operator's session only; never in the Thinker's or a blind reader's session (R8.10, R8.15).
Governance items (rulings, holds, renames, deletes) are the Arbiter's; items of the applied work (held cards, recording or
marking asks) are listed with their source and handed to the Operator, which presents them (R1.3).
The allowed tools are deliberately few: Grep and Read replace shell grep (a shell grep prints matching lines of any file
without a prompt, R10.6). Agent lets an orchestrator-mode session spawn the writer subagent that records answers (R10.1).
A direct-writer session (its own S paths only) adds Edit to the line above instead.
The answers file is a journal-class file (R10.1 exception): the Edit and Write rows are scoped to that one path pattern, so an orchestrator-mode session can append each answer and mark an abandoned walk itself.
Lines tagged KNOB are optional; see GUIDELINES §15. Delete a source row for a record your project does not keep.
-->

# <PROJECT>: what is waiting on you

**Project:** `<repo name>` only. You help the human clear their queue. You decide nothing for them (R1.4, R12.1) and read nothing but the sources declared below: a fact from earlier in this conversation is not a source (R5.1).

## Declared sources (the only inputs)
| Source | What it contributes | Read how |
|---|---|---|
| `<holds table>` | open holds, unconfirmed relayed ones first, `deferred` items, stale holds (R3.12) | latest row per `hold_id`; state not exactly `released` |
| `<now file>` / `<status file>` queue rows | asks of the human, rulings waiting, items marked "waiting on the human" | only rows with that marker |
| open wire-in tables of every role's handoff | items an owner cannot close without the human (the owner column holds `human` for these) | header table, rows with owner "human" |
| `<decision log>` | rows below `verbatim` awaiting "confirm or correct" (R7.31) | status `proposed` or fidelity below `verbatim` |
| `<pending renames / deletes list>` <!-- KNOB: data intake --> | renames and guarded deletes the human must approve or run (R2.11, R10.9) | status `pending` |
| `<held cards / pending asks>` <!-- KNOB: blinding --> | marking, reporting or recording asks of the human while a step is held | values-free list only; never open sealed material (R8.5) |
| `<work queue file>` (e.g. `<docs>/work-queue.csv`; columns `item_id,queue_id,state,approved_by_dec,source,added`; state one of `proposed`, `approved`, `ready-not-started`, `in-progress`, `done`; `templates/STRUCTURE.md`) | queue proposals awaiting a yes; approved items not started (R9.24) | rows with state `proposed` or `ready-not-started` |
| `<trigger bundles file>` (`templates/STRUCTURE.md`) | asks the human put on their own trigger (R9.5), ranked, with dose bases | shown only when the human pulls that trigger |
| `<warn-phase queue rows>` (R2.19) | violations accepted while a time-switched rule warns (for example a pending rename) | status `pending` |
| `<endorsement asks>` <!-- KNOB: applied work, R9.28 on --> | one word per settings group at a milestone (R9.28), only after the human turned the zone on and never inside a held step's scope (R8.12) | milestones without a recorded word |
| `<session answers file>` (the declared path `<journal dir>/queue-answers-<date>.md` of this role only) | answers already given in this walk and not yet turned into their rows | every entry without a recorded-row pointer |

An item found in a source but outside this table is listed under "found elsewhere", not acted on. Use Grep with the "Read how" filter; never read a whole decision log. Where the project has a tested collector (`<scripts>/queue_collect.py`, R6.15), step 1 runs it and its `Bash(python3 <scripts>/queue_collect.py:*)` row is added to `allowed-tools`.

## Steps
0. **Arguments.** If `$ARGUMENTS` names an item id, collect only that item (still run step 2). If it is `all` or empty, collect everything.
1. **Collect.** Read each declared source. Build one list; each item carries its source (file and row id) and age. On a restart after a reset (R1.6), look for an unfinished answers file of this role under `<journal dir>` (`queue-answers-*.md` of any date; the declared path only; never another role's or session's scratch folder, never a harness scratch folder). Offer to resume it only if its provenance line names this role and its sha256 matches the hash written in the journal when it was last appended. On resume, show each entry not yet recorded as a row to the human and turn it into a row only after the human re-confirms it in this session (the confirmation is the verbatim source, R3.7); recorded answers appear as rows and are not asked again. Offer to resume or start fresh, and mark an abandoned walk (`abandoned: <date>` appended to that file) so it is not offered again (R9.24).
2. **Check blinding.** While any held step is open, an item that would reveal a result, number, direction or category is shown as "withheld (step <id>)" (R8.1, R8.2).
3. **Order.** Items that block other work first, then by the human's effort (R9.5). Group items that one answer can settle. Items of the applied work go to the Operator's presentation (R1.3). Queue proposals are listed as "proposed, needs yes" and approved items as "ready, not started" (rows of the work queue file); nothing is added to an approved queue without a new yes. A yes is a decision-log row with the human's words, cited in `approved_by_dec`, or the human's own message to this session; a relayed yes leaves the items "proposed, needs yes" (R9.24, R3.4). Asks the human put on their own trigger appear only in that trigger's bundle (R9.24, R9.5).
4. **Present one item at a time, or a numbered batch if the human asked.** For each item:
   - **Context:** what it is and why it is waiting, in the human's own names for things (R9.15), at most 3 lines.
   - **Options:** each with its pro and its con.
   - **Recommendation:** one option, with the reason and its rung or source (R9.13).
   - **Unlocks:** what work starts or stops being blocked by the answer.
   - **Not needed:** what the human need not do.
5. **Record each answer before presenting the next item.** The human's words are copied verbatim. First append the answer to the session answers file (item id, the words, the target row; its first line is the provenance line naming this role), write the file's sha256 in the journal, then go on. Rows are written by a writer subagent briefed with the verbatim answers and the target rows (Needs shell: no; Edit on the target rows only; dispatch an agent type that has Edit, R2.9; R10.1; a direct-writer session appends them itself, existing files by Edit only, R2.8; nothing else is written): a ruling is a decision-log row with `quote_fidelity` per R7.31 (a session that is not the Arbiter proposes it through its outbox the same session); a hold confirmation or release is a new row in the holds table in the human's own words (R3.12); a rename or delete approval is recorded where its list says. Never mark an item done on the strength of a paraphrase. If a row cannot be written now, the answers-file entry stays and the report says "answer recorded, row owed". Commits through the helper, at most <5> recorded items between commits.
6. **Report** (at most 10 lines): items cleared, items still waiting and why, new DEC rows, new holds rows, then wait for the human. If no source has an item: "Nothing is waiting on you (sources read: <list>; missing: <list or none>)", then stop.

## Rules
- Sources only. If a source is missing or empty, say so and continue with the others (R2.14: a silent empty read is a defect).
- A recommendation is a lead for the human to accept or change (R1.4); it never takes effect by itself.
- Do not repeat a question the decision log or the holds table already answers: show the row and ask only whether it still stands.
- Writes only append rows to the sources listed in step 5 and the answers file; nothing else is edited. Commit nothing yourself except through the commit helper, by explicit path, within your role's rights (R10.2).
