# Peering: a framework for multi-session human–AI peer collaboration (v1.3)

## What this is

A reusable set of guidelines and fill-in-the-blank templates for running **several full agentic LLM sessions at once as peers** inside one project, led by one human. Each session has a role, a write scope, a start command and a handoff command. Sessions talk through short, file-backed messages that double as information-disclosure limits. Every role's next session resumes from files alone, so each role behaves like one continuous session even though real sessions end when their context fills.

The framework was extracted from a long-running research project (`appendix-worked-example.md`). It is project-agnostic and **written for Claude Code**; § "Harness requirements" maps every feature it uses and gives a fallback for other harnesses.

**Why the rules.** Every rule exists because something went wrong without it (appendix §2 lists the incidents). The rules save your time: sessions ask you less, never repeat questions, and resume without re-briefing. Start with the minimum below and add parts only when their trigger happens.

## When to use it

| Use it when | Do not use it when |
|---|---|
| The work spans many sessions (weeks, not hours) and context windows run out | One session can finish the job |
| Two or more kinds of work compete for one session's attention (e.g. building the record vs. serving you day to day vs. deep thinking) | There is one kind of work |
| Claims must be provable later (evidence classes, pre-registration, frozen records) | Output is throwaway |
| You are also a test subject, rater or blinded participant | No blinding is needed (leave the blinding knob off, GUIDELINES §15) |
| Your time is the scarcest resource | You want to drive every step personally |

## Your job as the human

| | What |
|---|---|
| **Do** | Start each session with its start command and end it with the handoff command. Name each session when reminded (Claude Code: `/rename`). Push when you choose (sessions never push). Relay "check your inbox" between sessions only if your harness has no cross-session messaging. Run the guarded delete script yourself when raw data must go (R10.9, knob: data intake). |
| **Say** | Rulings when a session asks (each becomes a decision-log row with your words; you see the new row ids in every Arbiter handoff report). Facts you changed (silence means no change, R9.3). Names for things you save (R9.4). A side task for the Thinker in the Thinker's own chat (R4.12). Whether you want a scored test on your own work; the default is informal (R9.9). Your own report on a change before you see its numbers (R9.16). "Confirm or correct" on a ruling recorded from someone else's wording, and "confirm" on a hold a peer relayed (R7.31, R3.12). Answers to the Thinker's few one-choice questions when a brief allows them (R4.14, knob). One raw sample of a format when a tool needs it (R7.34). Once, a standing permission to rename and register files you deliver (R2.11, knob: data intake). |
| **Decide** | Goals and scope. Which item to do next after each start report. Every ask on your time (each states what it buys). Method disputes. Lifting a seal (R8.11). Which session continues if two of one role are open (R1.8). A deputy if the Arbiter is lost (R1.7). When a held or `deferred` item may start: only your own words release a hold, even one a peer relayed (R3.12). |

Everything else is the sessions' job. If a session asks you for anything else, R9.5 and R12.1 say it should not. If you are a blinded subject: do not open files outside the human-readable set (R8.9) while a step is held.

## Harness requirements

| Capability | Used by | Claude Code mapping | If missing |
|---|---|---|---|
| Slash commands with arguments | start and handoff commands | `.claude/commands/<project>-<role>.md`; `$ARGUMENTS`; front matter `argument-hint`, `description`, `allowed-tools`, `disable-model-invocation: true` (only you can trigger them) | Paste the command file as the session's first message |
| Auto-loaded rules file | every session | `CLAUDE.md` at the repo root; `@` imports (about 5 hops in `CLAUDE.md`, one level in commands; large files dropped silently, R2.6) | Paste it at session start; keep it ≤ 120 lines |
| Subagents with short returns | orchestrator mode (R6.1–R6.5) | the Agent tool; resume by agent id only while the parent session lives | Direct-writer mode: the session does the work itself and writes detail to files |
| Cross-session messaging | live peer notifications (R3.6) | `ListAgents` / `SendMessage` (deferred tools; load with `ToolSearch` `select:ListAgents,SendMessage`); availability depends on version and configuration | Outbox files only; you are the courier ("check your inbox") |
| Persistent memory | behavior rules (§11) | the project memory folder and its `MEMORY.md` index (per machine, not in git; index truncated after about 200 lines) | The committed memory mirror (R11.9) read at start |
| Permission rules | R10.6 | `.claude/settings.json` `permissions.allow` / `deny` (`templates/settings-permissions.json`) | Prose bans only; review commits |
| Session names | sender checks (R3.9) | `/rename` | A name line in each session's first report |
| Per-agent read isolation | staged inputs for independent agents (R6.11) | a fresh private directory per agent outside the working tree, listing checked before launch. Staging hides paths, but a subagent still auto-loads the rules file and the memory index, so those carry no outcome value of a held or scored step. For strict blindness run the blind agent as a separate session whose working directory is the staged folder (or another mechanism that prevents the auto-load); at the high-risk knob also a post-run transcript read audit | Staging plus the auto-load rule: the listing proves what was offered, not what was read or loaded; without transcripts write `Reads unverified` in the output header |

**Prerequisites.** git (any recent version; the helper writes the trailer itself) · Python 3.8+ on macOS or Linux (the helper uses `fcntl`) · if the sandbox is on, its write allowlist includes `<repo>/.git` (the helper writes objects, the index and its lock there) · if `.claude/` is a symlink to a shared repository, the command files are committed there, not here · the Thinker on a different model: start that session with `claude --model <id>` or `/model` (a command's `model:` front matter applies only to that command's turn).

**Helper environment.** `commit_paths.py` reads three optional environment variables. `PEERING_ROLE` is the fallback for `--role`; it is validated against the `ROLES` list in the helper's CONFIG block exactly like the flag (an unknown value is refused), and you should never export it in a shell profile that several sessions share, because every session's shell inherits it and every commit would then carry one role; pass `--role <role-id>` on every call. `PEERING_HELD_FILE` is the fallback for `--held-file` (the pending-blinded-steps CSV, R8.17); set it in the rules file for every role. `PEERING_BRANCH` restricts commits to one branch. A project with the blinding knob on also sets `REQUIRE_HELD_FILE` in its helper copy (the helper reads `PEERING_REQUIRE_HELD_FILE=1` for the same effect) so that a forgotten held list refuses the commit. A bootstrap commit made before roles exist uses `--no-role "<reason>"`, which writes `Session-Role: none (<reason>)` so the bypass shows in `git log`; the settings template puts that flag in the `ask` list.

## Quick start A: the minimum (two roles, under an hour)

An **Arbiter** (owns records, standards and tools) and one **Operator** (your day-to-day interface for the applied work). Delete every line tagged `KNOB` in the templates unless its trigger in Quick start B has happened.

| # | Step | Time |
|---|---|---|
| 1 | Copy `templates/commit_paths.py` (and `test_commit_paths.py`) to `scripts/`; run `python3 -m unittest discover -s scripts -p 'test_commit_paths.py'` (23 tests, a few seconds); edit `ROLES` in the helper's CONFIG block to your role ids (see "Helper environment" below) | 5 min |
| 2 | Fill `templates/PROJECT-INSTRUCTIONS.md` as `CLAUDE.md`: what the project is, rules 2, 5, 7, 8, 11, 12, the sessions table | 10 min |
| 3 | Two charters from `templates/ROLE-CHARTER.md` (arbiter: orchestrator mode; operator: direct writer). Put the "Minimum variant" table of `templates/WRITE-SCOPES.md` in `docs/STRUCTURE.md` with the placement test from `templates/STRUCTURE.md` | 10 min |
| 4 | Create `docs/decisions.csv` from `templates/DECISION-LOG.csv` (header only). First row: your adoption of the roles and scopes, in your words | 2 min |
| 5 | One handoff file per role from `templates/HANDOFF-FILE.md`, keeping Header (with the two wire-in lines, "none" is valid, R5.15), §0, §1, §2, §6 (one line: "Open holds: <ids or none>"), §7, §10. Create `docs/holds.csv` from `templates/HOLDS.csv` (header only; the holds table, R3.12) and `peers/outbox-arbiter.md` and `peers/outbox-operator.md` from `templates/OUTBOX.md` | 5 min |
| 6 | Install commands: `templates/START-COMMAND.md` twice as `.claude/commands/<project>-arbiter.md` (common steps + Arbiter block) and `<project>-operator.md` (common steps + Operator block); `templates/HANDOFF-COMMAND.md` once as `<project>-handoff.md` (Arbiter and Operator branches). Fill the `allowed-tools` placeholders. Optionally merge `templates/settings-permissions.json` into `.claude/settings.json` | 10 min |
| 7 | Smoke tests (below) | 10 min |

Worked, filled versions of these files for a small invented project: `examples/minimal-setup.md`.

## Quick start B: grow when the trigger happens

| Trigger | Add | Rules and templates |
|---|---|---|
| Insight work keeps displacing record work | a Thinker | R1.9; §4; `BRIEF.md`, `RESPONSE.md`, `THINKER-HANDOFF.md`, `KNOWLEDGE-INDEX.md`, Thinker blocks of the commands |
| Advice depends on a claim that could be wrong | evidence classes, pre-registration, per-datum ledger | §7; `PREREGISTRATION.md`, `DATA-STATUS-LEDGER.md`, `REVIEW-REPORT.md` |
| You are a test subject or rater | blinding | §8; `PENDING-BLINDED-STEPS.md`, `EXPOSURE-LOG.md`, the human-readable set in `STRUCTURE.md` |
| A session corrects its behavior after your feedback | memory entries, the same day | §11; `MEMORY-ENTRY.md` (Claude Code: the project memory folder) |
| Starts get slow or handoffs lose facts | status file, journal, token audit | R5.12, R6.6; `STATUS.md`, `JOURNAL.md` |
| Several work items in parallel | role instances | R1.11; §8 of the handoff file |
| An insight is flagged for explanation and a test on the human would cost more than <N, e.g. 2> hours, or a test chosen from the first explanation already failed (off by default; needs the evidence knob and a Thinker) | the investigation phase: isolated generators, averaged probability sheets, a red team, a kill plan, a scored ledger | R7.17–R7.22, R6.11, R6.12; `INVESTIGATION.md`, `LENS-CARDS.md`, `INVESTIGATION-LEDGER.csv` |
| Work gets built and then forgotten between sessions | the full surface inventory and grep at every handoff (the wire-in table and the two header lines are already in the minimum, R5.15) | R5.15; `HANDOFF-COMMAND.md`, `HANDOFF-FILE.md` |
| A job is rerun by hand and you lose track of what is new | the automation table (the status file's table, or `AUTOMATION-RUNS.md` for many jobs) | R5.9; `STATUS.md`, `AUTOMATION-RUNS.md` |
| You deliver files (captures, exports) to the project | data intake: normalize on receipt, catalog | R2.11, R10.9 |
| A second tool duplicates an existing one, or you have more than a handful | the tool registry (until then the rules file's Key commands list is the registry) | R2.12; `STRUCTURE.md` §3b |
| Raw data must be freed or deleted | catalog first, guarded delete script the human runs | R10.9 |
| Tools read data that a held step covers | the machine-read held list: CSV record, Markdown view, helper `--held-file` | R8.16, R8.17; `PENDING-BLINDED-STEPS.csv`, `.md` |
| Scorers are built by agents | scorer built from the pre-registration text, pre-run rulings, one-run definition, pins that retire | R7.23–R7.27, R10.8; `PREREGISTRATION.md` |
| A protocol or framework needs maximum rigor | the five-seat review panel | R7.16; `PANEL-BRIEF.md`, `REVIEW-REPORT.md` |
| Two sessions collide on files often | one worktree per role | §15 |

## Upgrading from v1.2

1. **Breaking:** the helper now refuses a commit with no role or an unconfigured role. Re-copy `commit_paths.py` and its tests, set `ROLES`, and add `--role <role-id>` to every script, hook and alias that calls it (or use `--no-role "<reason>"` for a deliberate bootstrap commit).
2. Append `,scope,quote_fidelity,question,options` to the decision log's header and set `quote_fidelity` to `legacy` on every existing row; old rows keep their status. Add one decision-log row recording the adoption and the cut-off id (R7.31).
3. Create `holds.csv` from `templates/HOLDS.csv`, add §6 (one line) to each handoff file, and re-copy the start command's step 7 and A5 (i)–(k), the handoff command's wire-in "ruling" row, Holds row and step 11, the rules file's rules 2 and 12, and the charter's role-specific rules.
4. Run the helper tests (23).

## Smoke tests

1. **Commit helper.** In a scratch clone: commit a new file with `--role` (expect exit 0 and only that file in the commit); commit with no role and no `PEERING_ROLE` (expect exit 2 and a message that lists the configured roles and does not name a bypass); commit with `--role` set to a name not in `ROLES` (expect exit 2); commit with `--no-role "bootstrap"` (expect exit 0 and the trailer `Session-Role: none (bootstrap)`); commit `.` (expect exit 2); hold the lock from a second shell (`python3 -c` with `fcntl.flock`) and commit (expect exit 3 after `--timeout`); with the blinding knob on, pass `--held-file` a missing path, the Markdown view and a CSV with a pending row (expect exit 2 for the first two, and a refused verdict word next to the pending id for the third). The bundled unit tests cover these and pairs, frozen paths, held subjects (CSV only, fail closed), secrets in files and messages, and leases.
2. **Messaging.** Session A lists agents and sends a one-line notification to B; B receives it; A closes; B sends to A and observes what happens. Write the observed semantics into the table in `PEER-MESSAGE-PROTOCOL.md`. No messaging tool → outbox files only.
3. **Start / handoff round trip.** Run the Arbiter start: expect a ≤ 15-line report that ends by waiting for you, with no permission prompts. Ask for one trivial change. Run the handoff: expect a commit through the helper, a header carrying the two wire-in lines ("none" is valid) and a final line `Next session: …`. Open a fresh session, run the start, and check it names the change. Then run the marker grep from the handoff file's contract and check it lists every section. Hold test: in the Operator session tell the Arbiter "hold X until I say so", have it relay that to the Operator, then reset the Operator and start it fresh: the report must list the hold as `held (relayed, unconfirmed)` first and ask you to confirm it. All pass → setup is done; do the token audit (R6.6) after the first real cycle.

## Translation table (other kinds of project)

| Rule family | Research with a subject | Software | Writing | Ops |
|---|---|---|---|---|
| Roles | Arbiter = R&D lead; Operator = the human's day-to-day test interface; Thinker = insight | Arbiter = architect / maintainer; Operator = feature session | Arbiter = editor; Operator = drafting session | Arbiter = SRE lead; Operator = incident session |
| Claim and proof (§7) | a law, a cited query, a scored test | "this change does X"; a test, benchmark, reviewer finding | "this passage achieves Y"; a reader test | "this runbook fixes X"; a game-day result |
| Frozen record | sealed pre-registration, score file | tagged release, merged ADR | published draft | post-incident review |
| Pre-registration | prediction before data | acceptance criteria written before implementation | a reader-test rubric written before the draft | expected outcome before a change window |
| Blinding (§8) | the human rates without seeing results | reviewers who do not see the author's expected result | readers who do not see the intended effect | — (usually off) |
| Dose (§9) | repetitions, blocks | reviewer hours, QA passes | reader sessions | on-call interruptions |
| Integrity (§10) | hashed read-only data | protected branch, CI | — | read-only production access |

## File map

| File | Purpose | Required at | Read when |
|---|---|---|---|
| `README.md` | this file | minimum | first |
| `GUIDELINES.md` | numbered rules with Why / Fails as; knobs (§15) | minimum | the core-rules box at setup; a section when its knob turns on |
| `appendix-worked-example.md` | the source project and the incidents behind the rules | — | when a rule seems like red tape |
| `examples/minimal-setup.md` | filled minimum files for an invented project | — | during Quick start A |
| `CHANGELOG.md` | what changed between versions and why | — | when upgrading |
| `templates/commit_paths.py`, `test_commit_paths.py` | the commit helper (lock, new files, pairs, frozen paths, held subjects from the CSV list, role list and `--no-role REASON`, secrets in files and messages, leases) and its tests | minimum | setup |
| `templates/settings-permissions.json` | Claude Code allow / ask / deny rules for R10.6 (deny rules match command text, not effects; `<raw-data path>` and `<sealed path>` are placeholders to fill in or delete; verify the rule grammar in your harness version) | default | setup |
| `templates/PROJECT-INSTRUCTIONS.md` | the auto-loaded rules file | minimum | setup |
| `templates/ROLE-CHARTER.md` | one role: purpose, authority, mode, scope, model, lifecycle | minimum | adding a role |
| `templates/WRITE-SCOPES.md` | ownership matrix (S / W / A / P / R / N, human-readable set), minimum variant | minimum | before writing outside your folder |
| `templates/STRUCTURE.md` | layout, placement test, path map, human-readable set, frozen manifest | minimum | before creating a file |
| `templates/START-COMMAND.md` | session start: common steps plus a block per role | minimum | setup |
| `templates/HANDOFF-COMMAND.md` | universal handoff with a branch per role | minimum | setup |
| `templates/HANDOFF-FILE.md` | a role's memory file with the lazy-read contract | minimum | setup |
| `templates/OUTBOX.md` | a role's outgoing messages (the file is the message) | minimum | setup |
| `templates/PEER-MESSAGE-PROTOCOL.md` | when and how peers message; trust; delivery | minimum | before the first message |
| `templates/DECISION-LOG.csv` | the human's rulings (header only) | minimum | setup |
| `templates/HOLDS.csv` | the holds table: restrictions the human imposed, relayed or direct, with state and release condition (header only; append-only; R3.12) | minimum | setup; every start |
| `templates/SUBAGENT-BRIEF.md` | a subagent's task, scope, tools and return format | default | before spawning |
| `templates/JOURNAL.md` | per-session event log for the handoff | default | every session |
| `templates/STATUS.md` | status rows, automation runs, Thinker log with dispositions | default | Arbiter start |
| `templates/OPERATOR-FOLDER-HANDOFF.md` | per-work-folder handoff and next-session prompt | default | Operator handoff |
| `templates/MEMORY-ENTRY.md` | a persistent behavior rule | default | after a correction from the human |
| `templates/BRIEF.md`, `templates/RESPONSE.md` | the Thinker exchange (three core response shapes, plus merge and plan for the investigation knob) | knob: Thinker | writing or answering a brief |
| `templates/THINKER-HANDOFF.md`, `templates/KNOWLEDGE-INDEX.md` | the Thinker's handoff and entry point | knob: Thinker | Thinker setup |
| `templates/PREREGISTRATION.md`, `templates/DATA-STATUS-LEDGER.md` | predictions before data; spent-data status | knob: evidence | before a confirmatory test |
| `templates/PENDING-BLINDED-STEPS.csv`, `templates/PENDING-BLINDED-STEPS.md`, `templates/EXPOSURE-LOG.md` | held steps (values-free): the CSV is the one machine-read record, the Markdown file its human-readable view; per-role exposure files | knob: blinding (machine-read list: knob) | every start while blinding is on |
| `templates/REVIEW-REPORT.md`, `templates/PANEL-BRIEF.md` | CR / RO reviews; the five-seat panel | default / knob: maximum rigor | reviewing |
| `templates/AUTOMATION-RUNS.md` | per-job last run and "new since last run" (feeds take-stock); the status file's table is the lighter alternative | knob: automation | Arbiter start (R5.9) |
| `templates/INVESTIGATION.md` | flag skeleton, step table with gates, allowed inputs per role, who sees what | knob: investigation | an insight is flagged for explanation |
| `templates/LENS-CARDS.md` | lens-card skeleton, control card, structured step, closing prompt, prompt skeletons for clerk, generator, merger, ranker, red team | knob: investigation | writing the generation briefs |
| `templates/INVESTIGATION-LEDGER.csv` | header of the append-only investigation score ledger (`seal` and `resolution` rows) | knob: investigation | after seal 2 and at resolution |

## Vocabulary

| Term | Meaning |
|---|---|
| The human | the one person who owns the project, makes rulings, and may also be a test subject |
| Role / role id / instance | a standing function (Arbiter, Operator, Thinker, …) with an id (`arbiter`); an instance is `<role>:<item>` (R1.11). One live session per instance (R1.8) |
| Session | one bounded agent conversation running a role |
| Subagent | a worker spawned by a session for one task; returns `STATUS / OUT / OPEN`, writes detail to files (R6.3) |
| Orchestrator mode / direct writer | a session that edits nothing itself and dispatches subagents / one that edits its own files (R10.1) |
| Handoff file | a role's memory: everything a fresh session of that role needs (R5.1) |
| Lazy-read markers | `**[history]` lead-ins that let a start read only current blocks (R5.2) |
| Take stock | the start's gather-only survey of new input, cheap wins, ready items and leads (R5.9) |
| Write scope; S / W / A / P / R / N | who may write what: stakeholder, write, append-only, propose, read, no-read (R2.1) |
| Human-readable set | the files the human may open; nothing of a held step goes there (R8.9) |
| Commit helper / lock | `commit_paths.py`: commits only named paths under a file lock (R10.2) |
| Session-Role trailer | `Session-Role: <role>` at the end of each commit message, added by the helper (R2.5) |
| Outbox; M-id | a role's file of outgoing messages; each message's id `M-<role>-<n>` (R3.6) |
| Journal | a session's own event log, source of its handoff facts (R5.12) |
| Decision log; DEC id | the only record of the human's rulings, with verbatim words, their fidelity and scope (R7.11, R7.31) |
| Package | in the human's own applied work, a combined set of changes with pre-written signatures and a backout order, instead of one-lever tests (R9.14) |
| Hold; `held (relayed, unconfirmed)`; `deferred` | a restriction the human imposed, honored at once even when relayed, recorded in the holds table; a relayed one is `held (relayed, unconfirmed)` until the human confirms it; only the human releases it; `deferred` = wanted, not now. A hold is not a held step (R3.12) |
| Signature; backout order; lever | a signature is a pre-written observable showing a change worked or failed; a backout order is the sequence in which to undo a package; a lever is one adjustable item a change moves (R9.14, R9.11) |
| Advice ladder; rung | the default order of what advice rests on, from checked project knowledge down to judgment; a rung is one step of it (R9.13). Not the class ladder of R7.1 |
| Drift allowance | how much a learning subject changes between sessions on its own, measured from data on file (R7.32) |
| Quote fidelity | per decision-log row: `verbatim` / `relayed-by-<role>` / `elided-by-<role>` / `paraphrase-by-<role>` / `legacy`; below `verbatim` is a lead until the human confirms (R7.31) |
| Lead | a claim that has not earned a class beyond WEAK; may guide exploration, never cited as known (R7.1) |
| Evidence class | UNKNOWN / WEAK / STRONG / KNOWN on provenance; lead / VALIDATED on behavior (R7.1) |
| Pre-registration | a prediction, its falsifier and its scoring rule, committed before the data it is scored on (R7.2) |
| Fit set | the data used to build a prediction; it cannot confirm it (R7.3) |
| Spent datum | data that already printed a family's outcome; it cannot confirm that family (R7.12) |
| Marked / resolved | passes an uncorrected threshold / survives the stated correction for many comparisons (R7.13) |
| NC | not conclusive: the scoring rule could not decide (R7.5) |
| CR / RO | code or record review / robustness review (R7.7) |
| Frozen record; seal | a file never edited after a defined event; sealing = committing material that stays unread until release (R2.4, R7.8) |
| Held step; family | a step on the pending-blinded-steps list; a family is a group of questions one exposure contaminates (R8.3) |
| Exposure | an actor having seen outcome data that a later blinded or confirmatory step depends on (R8.7) |
| §V deviation | a block in the affected record disclosing a departure from protocol (R7.10) |
| ON HOLD | work parked with a release condition: the open rows of the holds table, quoted in handoff §6 |
| Dose | the amount of work asked of the human, with what it buys and why this many (R9.1) |
| Quick-reference card | an optional short card of rules and leads the Operator consults during the human's live work; curated by the Arbiter |
| Research packet | curated excerpts the Arbiter prepares from outside sources for the Thinker (R4.5) |
| Playbook | the project's method doc for sessions that ask the human to act (walkthrough format, dose) |
| Knob | an optional part, off in the minimum, turned up when its trigger happens (GUIDELINES §15) |
| Wire-in; open wire-in | work reachable from the project's discovery surfaces; an item a role could not wire itself, passed to its owner (R5.15) |
| Staged directory | a fresh private directory holding only one agent's allowed inputs, listed before launch (R6.11) |
| Investigation phase | flag → fact sheet → generators → merge → seal 1 → red team → seal 2 → kill plan → pre-registration → apply → self-score (R7.17) |
| Lens card; rival slot; catch-all; kill plan; red team | investigation-phase terms: see the `templates/LENS-CARDS.md` header and R7.18–R7.21 |
| Pre-run rulings | the Arbiter's rulings on a scorer builder's flagged gaps, committed before any datum is read (R7.23) |
| Value-free subject | a commit subject that names the step and verdict class only (R8.15) |
