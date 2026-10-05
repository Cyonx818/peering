# <ROLE> handoff: <PROJECT>

<!--
LAZY-READ CONTRACT (GUIDELINES R5.2, R5.3). This comment is the ONE place the marker grep is defined;
start and handoff commands read lines 1-20 of this file and run the grep below. Keep it identical.
- Each section starts with its CURRENT block.
- Superseded blocks follow, each opened by a bold lead-in that STARTS with the token [history]:
    **[history] In flight, end of session 6.**
  The word "history" anywhere else (e.g. **Git history check**) is not a marker.
- The previous session's header becomes **[history] Session <n-1> header.** and moves below the new header.
- Marker grep (shell, POSIX):  grep -n -e '^## ' -e '^\*\*\[history\]' <this file>
  Claude Code Grep tool (ripgrep): pattern  ^## |^\*\*\[history\]
- Read each section with offset/limit down to its first **[history] line. Never delete history.
- Grep returns only "## " lines although history exists, or nothing: markers are broken. Read header
  and §7 by heading, never the whole file, and tell the human.
-->
<!-- Lines tagged KNOB are optional; see GUIDELINES §15. Minimum file: Header, §0, §1, §2, §6, §7, §10. -->

**Session <n> header.** End of session <n>, <YYYY-MM-DD>. <One paragraph: what changed, what we now know that we did not, the single next action.>

**Wired this session:** <item → surface (commit)>. **Open wire-in:** <item → surface, owner>. (Write "none" explicitly; R5.15.)

**[history] Session <n-1> header.** <…>

## §0 Orientation and peers

<What this role is (one line; link the charter). How it relates to the other roles. Role id or instance id (R1.11).>

**Peer state at the end of session <n> (<date>).**

| Name (set by the human) | Role / instance | Harness id at last contact | State | Handoff file / last commit |
|---|---|---|---|---|
| "<name>" | <role> | <id or "unknown"> | <online / closed> | <path> @ <hash> |

Messages: my outbox `peers/outbox-<role>.md`. Open items sent by me (not done): <M-ids or "none">. Items acked by me this session: <M-ids or "none">.

**[history] Peer state at the end of session <n-1>.** <…>

## §1 Start-of-session checklist

| # | Step | Detail |
|---|---|---|
| 1 | Integrity <!-- KNOB: source-of-truth integrity --> | `<hash command>` = `<expected>`; frozen manifest check |
| 2 | Read this file, current blocks only | lazy-read contract above |
| 3 | Status slice <!-- KNOB: status file --> | rows State / Commit / Next action |
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

| Claim | Class | Proof (commit / record) | Scope |
|---|---|---|---|

<!-- During a held step: no class change for a held family is written here until release (R8.4). -->

## §5 Leads

| Lead | Source | Class | Next test |
|---|---|---|---|

## §6 ON HOLD

Open rows of the holds table `<holds table>` (R3.12); the table is the record and wins on any difference.

| Hold id | Scope | State (`held (relayed, unconfirmed)` / `held` / `deferred`) | Release condition (the releaser is always the human) | Age (days) |
|---|---|---|---|---|

<!-- Minimum: this section is one line, "Open holds: <ids or none>". A hold relayed by a peer binds at once, only restricts, and is confirmed with the human at the next contact (R3.12). `deferred` = wanted, not now: listed at every take-stock, never started without the human's word. -->

## §7 Next action and ranking

**Next action:** <one action>; first concrete step: <…>

| Rank | Item | Value (what it unblocks) | Human effort (what it buys, why this many) | Cost |
|---|---|---|---|---|

**Open questions to the human:** <numbered, each a decision that is theirs>

**In flight:** pre-registered not run: <…> · awaiting scoring: <…> · sealed unopened: <…> · briefs without response: <…> · uncommitted: <…> · outbox items not done: <M-ids> · live subagents: <id, task, output path, checkpoint>

**[history] Ranking, end of session <n-1>.** <…>

## §8 Side folders and instances <!-- KNOB: several roles or instances -->

| Folder | Owner (role / instance) | State | Handoff file |
|---|---|---|---|

## §9 File map

| Need | Path |
|---|---|

## §10 Review & corrections

| Review | Finding | Applied |
|---|---|---|
| Handoff writer, end of session <n> (<date>) | handoff brought current from the journal and the fact list | <sections touched; HEAD recorded>. Not re-run by the writer (no shell): <items cited as given, or "none"> (R5.10) |
