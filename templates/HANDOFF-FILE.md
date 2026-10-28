# <ROLE> handoff: <PROJECT>

<!--
CURRENT-STATE CONTRACT (GUIDELINES R5.2, R5.3, R5.16). This file holds CURRENT rows only.
- A handoff writer edits rows in place. It adds no new header block, no dated section and no [history] block.
- The previous version is recoverable: `git show <commit>:<path>`, the commit named in the Record line below.
- Section numbers §0-§10 are this template's; commands cite them.
- Heading-order check (shell, POSIX):  grep -n '^## ' <this file>
  Expected: §0 §1 §2 [§3] [§4] [§5] §6 §7 [§8] [§9] §10   ([ ] = optional; compare on the §<n> token only;
  a heading without a § token, such as a writer's progress block at the end, is ignored; fenced blocks hold no `## ` lines).
  The sections present appear in this order and the minimum set (§0 §1 §2 §6 §7 §10) exists. A required heading
  missing, or any heading out of order: the start stops and tells the human "handoff structure broken: <heading>"
  and reads header and §7 by heading only. A deleted optional section is not a failure.
- Read with offset/limit by heading: header, §0, §1, §2, §7 down to its "### Trajectory" heading. Never the whole file.
- LEGACY FORM (a v1.3 file not yet consolidated, R5.3; delete these three lines in a new file): a file may keep
  **[history]** lead-ins as a reading aid (grep -c '^\*\*\[history\]' <file> above 0 = legacy; the start reads each
  section down to its first **[history] line) and is listed for consolidation (R5.17).
-->
<!-- Lines tagged KNOB are optional; see GUIDELINES §15. Minimum file: Header, §0, §1, §2, §6, §7, §10. -->

**Record:** status <current / consolidating>; current as of <YYYY-MM-DD>; old version at `<commit>:<path>` (or "none: new file"); drop ledger `<path or "none">` (R5.17).

**Session state** (one row each, overwritten at every handoff; R5.16)

| Item | Current |
|---|---|
| Last session end | in `<now file>` <!-- KNOB: status file; the now-file is the one record. Without it: session <n>, <YYYY-MM-DD>; HEAD before the handoff commit (= §1 row 6) `<short hash>` --> |
| What changed, what we now know (next action: §7) | <one paragraph> |
| Checks at that end | <repo checks, tests, integrity: result> |
| Wired this session | <item → surface (commit)>, or "none" (R5.15) |
| Running work | <live subagents (id, task, output path, checkpoint), uncommitted files, or "none"> |
| Budget mode (R6.18) | <id; defers; never defers; lapse date; decision-log id with the human's words>, or "none" |
| Start-read size (R6.6) <!-- KNOB: token audit --> | <bytes per start-read region; table cells over the cell limit; commit>, overwritten by the size gate at every handoff |

**Open wire-in** (R5.15; "none" is valid, written as one line). Owner is a role id, or `human` when only the human can close the item (it then appears in the queue command, R9.24).

| Item | Target surface | Owner | State |
|---|---|---|---|

## §0 Orientation and peers

<What this role is (one line; link the charter). How it relates to the other roles. Role id or instance id (R1.11).>

**Peers (current as of <date>).**

| Name (from the roster, `docs/peer-comms-protocol.md`) | Role / instance | Harness id at last contact | State | Handoff file / last commit |
|---|---|---|---|---|
| "<name>" | <role> | <id or "unknown"> | <online / closed> | <path> @ <hash> |

Messages: my outbox `peers/outbox-<role>.md`. Open items sent by me (not done): <M-ids or "none">. Items acked by me this session: <M-ids or "none">.

## §1 Start-of-session checklist

| # | Step | Detail |
|---|---|---|
| 1 | Integrity <!-- KNOB: source-of-truth integrity --> | `<hash command>` = `<expected>`; frozen manifest check |
| 2 | Read this file by heading order | contract above; stop if the heading check fails |
| 3 | Now-file <!-- KNOB: status file --> | `<now file>` (size guide `<40>` lines): current cycle, next action per role, last session end |
| 4 | Lease and peers | `commit_paths.py lease <role> --name <name>`; agent list; open outbox items addressed to me |
| 5 | Pending blinded steps <!-- KNOB: blinding --> | `<pending-blinded-steps file>` (values-free) |
| 6 | HEAD before the handoff commit | `<short hash>` |
| 7 | Journal of the last session | `<journal path>` (if the last session died before handoff, R5.14) |
| 8 | Holds table | `<holds table>`: latest row per hold id; list every open hold, unconfirmed ones first (R3.12) |

**Do not re-read:** <files and sections a fresh session must not spend tokens on, unless a question names them>

## §2 Working agreement

<Numbered rules for working with the human in this role, each with its date and source. A line that grants a permission or changes a scope cites its DEC id; without one it is a lead (R3.7).>
1. <rule> (DEC-<id> or <source>, <date>)

## §3 Evidence discipline as practiced <!-- KNOB: evidence -->

| Lesson | Source (record, review finding) |
|---|---|

## §4 State of knowledge

A pointer map (R5.16): the class of each subject lives in the status ledger, not here.

| Subject | Pointer (ledger row / record) |
|---|---|

<!-- During a held step: no class change for a held family is written here until release (R8.4). -->

## §5 Leads

| Lead | Source | Ledger row (the class lives there, R5.16) | Next test |
|---|---|---|---|

## §6 ON HOLD

Open rows of the holds table `<holds table>` (R3.12); the table is the record and wins on any difference.

| Hold id | Scope | State (`held (relayed, unconfirmed)` / `held` / `deferred`) | Release condition (the releaser is always the human) | Age (days) |
|---|---|---|---|---|

<!-- Minimum: this section is one line, "Open holds: <ids or none>". A hold relayed by a peer binds at once, only restricts, and is confirmed with the human at the next contact (R3.12). `deferred` = wanted, not now: listed at every take-stock, never started without the human's word. -->

## §7 Next action and ranking

**Next action:** in `<now file>`, row <role-id> (the one copy, R5.16) <!-- KNOB: status file. Without a now-file, write it here: <one action>; first concrete step: <…> -->

| Rank | Item | Value (what it unblocks) | Human effort (what it buys, why this many) | Cost |
|---|---|---|---|---|

**Open questions to the human:** <numbered, each a decision that is theirs>

**In flight:** pre-registered not run: <…> · awaiting scoring: <…> · sealed unopened: <…> · briefs without response: <…> · uncommitted: <…> · outbox items not done: <M-ids> · live subagents: <id, task, output path, checkpoint>

### Trajectory

Role-internal flips only (ranking, approach, working agreement), each a move of value, class, scope, direction or decision (R5.16); a subject's value or class flip goes to the status ledger's trajectory and is pointed to, not copied. A row stays while it still bears on reading this file.

| Date | Subject | From → to | Cause | Verdict | Pointer |
|---|---|---|---|---|---|

## §8 Side folders and instances <!-- KNOB: several roles or instances -->

| Folder | Owner (role / instance) | State | Handoff file |
|---|---|---|---|

## §9 File map

| Need | Path |
|---|---|
| Last consolidation record and drop ledger (kept by later handoffs) | `<path>` @ `<commit>` |

## §10 Review & corrections

A row only for a correction or review finding that still bears on how this file is read; otherwise the handoff commit body is the record (R5.10).

| Review | Finding | Applied |
|---|---|---|
