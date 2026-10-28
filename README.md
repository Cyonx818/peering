# Peering: a framework for multi-session human–AI peer collaboration (v1.7)

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

**Do**
- Start each session with its start command and end it with the handoff command.
- Name each session when reminded (Claude Code: `/rename`).
- Push when you choose (sessions never push). With the Public mirror knob on, run the mirror publish script instead of pushing (R10.12).
- Relay "check your inbox" between sessions only if your harness has no cross-session messaging.
- Run the guarded delete script yourself when raw data must go (R10.9, knob: data intake).
- Run `/<project>-queue` when you want to clear everything waiting on you (R9.24).

**Say**
- Rulings when a session asks (each becomes a decision-log row with your words; you see the new row ids in every Arbiter handoff report).
- Facts you changed (silence means no change, R9.3). Names for things you save (R9.4).
- A side task for the Thinker in the Thinker's own chat (R4.12).
- Whether you want a scored test on your own work; the default is informal (R9.9).
- Your own report on a change before you see its numbers, and whether you report first or after the blind analysis is committed (R9.16).
- "Confirm or correct" on a ruling recorded from someone else's wording, and "confirm" on a hold a peer relayed (R7.31, R3.12).
- One raw sample of a format when a tool needs it (R7.34).
- (knob: blind report inference) Your own mark on each blind cell (named / partly / missed / can't say, or pass the round), from its claim line alone, before you see any number (R8.18). Once, in your own words, whether rounds run values-first (R8.18 (8)).
- (knob: Thinker) Answers to the Thinker's few one-choice questions when a brief allows them (R4.14).
- (knob: data intake) Once, a standing permission to rename and register files you deliver (R2.11).
- (v1.7, applied work) Only if you turn a preference zone on: at a milestone you choose, one word for each settings group (happy / ok / not there; R9.28). Your own choice for a setting that shows no footprint, which is then "set by your preference" (R9.19).
- (v1.7) The name of a run context the references cannot identify (R2.20), and a name for each initiative when more than one shares the repository (R2.21).
- (v1.7) A yes for each work queue and for each later addition (R9.24). The violations a time-switched rule accepted while it only warned are queued for you before it starts blocking (R2.19); the queue command lists them.

**Decide**
- Goals and scope. Which item to do next after each start report. Every ask on your time (each states what it buys). Method disputes.
- Whether an outside tool or non-default dependency is adopted, after reading its fit assessment (R2.16).
- Which design a large build uses, when a session sets it beside a cheaper priced alternative (R6.17).
- Lifting a seal (R8.11). Which session continues if two of one role are open (R1.8). A deputy if the Arbiter is lost (R1.7).
- When an iterative loop stops: you may end it at any time, and a session tells you when it sees nothing left worth trying (R9.19).
- When a held or `deferred` item may start: only your own words release a hold, even one a peer relayed (R3.12).
- (v1.7) Whether any budget-saving mode is on: what it defers, what it never defers and when it lapses. It counts only as a decision-log row in your words (R6.18).

Everything else is the sessions' job. If a session asks you for anything else, R9.5 and R12.1 say it should not (the lists above, including the knob lines, are the asks the framework defines; the v1.7 additions are marked). If you are a blinded subject: do not open files outside the human-readable set (R8.9) while a step is held.

## Harness requirements

| Capability | Used by | Claude Code mapping | If missing |
|---|---|---|---|
| Slash commands with arguments | start and handoff commands | `.claude/commands/<project>-<role>.md`; `$ARGUMENTS`; front matter `argument-hint`, `description`, `allowed-tools`, `disable-model-invocation: true` (only you can trigger them) | Paste the command file as the session's first message |
| Auto-loaded rules file | every session | `CLAUDE.md` at the repo root; `@` imports (about 5 hops in `CLAUDE.md`, one level in commands; large files dropped silently, R2.6) | Paste it at session start; keep it ≤ 120 lines |
| Subagents with short returns | orchestrator mode (R6.1–R6.5) | the Agent tool; resume by agent id only while the parent session lives. A type's tools come from its definition (`tools:` in `.claude/agents/<type>.md`) or are fixed for a built-in type; the Agent tool cannot narrow them per spawn, so a restricted read needs a restricted type or a permission rule | Direct-writer mode: the session does the work itself and writes detail to files |
| Cross-session messaging | live peer notifications (R3.6) | `ListAgents` / `SendMessage` (deferred tools; load with `ToolSearch` `select:ListAgents,SendMessage`); availability depends on version and configuration | Outbox files only; you are the courier ("check your inbox") |
| Persistent memory | behavior rules (§11) | the project memory folder and its `MEMORY.md` index (per machine, not in git; index truncated after about 200 lines) | The committed memory mirror (R11.9) read at start |
| Permission rules | R10.6 | `.claude/settings.json` `permissions.allow` / `ask` / `deny` (`templates/settings-permissions.json`) | Prose bans only; review commits |
| Session names | sender checks (R3.9) | `/rename` | A name line in each session's first report |
| Per-agent read isolation | staged inputs for independent agents (R6.11) | a fresh private directory per agent outside the working tree, listing checked before launch. Staging hides paths, but a subagent still auto-loads the rules file and the memory index, so those carry no outcome value of a held or scored step (a mandatory check for an R7.50 analysis, never a KNOB). For strict blindness run the blind agent as a separate session whose working directory is the staged folder (or another mechanism that prevents the auto-load); at the high-risk knob also a post-run transcript read audit | Staging plus the auto-load rule: the listing proves what was offered, not what was read or loaded; without transcripts write `Reads unverified` in the output header |

**Prerequisites.** git (any recent version; the helper writes the trailer itself) · Python 3.8+ on macOS or Linux (the helper uses `fcntl`) · if the sandbox is on, its write allowlist includes `<repo>/.git` (the helper writes objects, the index and its lock there) · if `.claude/` is a symlink to a shared repository, the command files are committed there, not here · the Thinker on a different model: start that session with `claude --model <id>` or `/model` (a command's `model:` front matter applies only to that command's turn).

**Helper environment.** `commit_paths.py` reads three optional environment variables. `PEERING_ROLE` is the fallback for `--role`; it is validated against the `ROLES` list in the helper's CONFIG block exactly like the flag (an unknown value is refused), and you should never export it in a shell profile that several sessions share, because every session's shell inherits it and every commit would then carry one role; pass `--role <role-id>` on every call. `PEERING_HELD_FILE` is the fallback for `--held-file` (the pending-blinded-steps CSV, R8.17); set it in the rules file for every role. `PEERING_BRANCH` restricts commits to one branch. A project with the blinding knob on also sets `REQUIRE_HELD_FILE` in its helper copy (the helper reads `PEERING_REQUIRE_HELD_FILE=1` for the same effect) so that a forgotten held list refuses the commit. A bootstrap commit made before roles exist uses `--no-role "<reason>"`, which writes `Session-Role: none (<reason>)` so the bypass shows in `git log`; the settings template puts that flag in the `ask` list.

## Quick start A: the minimum (two roles; about an hour for most setups, an estimate)

An **Arbiter** (owns records, standards and tools) and one **Operator** (your day-to-day interface for the applied work). Delete every line tagged `KNOB` in the templates unless its trigger in Quick start B has happened.

| # | Step | Time |
|---|---|---|
| 1 | Copy `templates/commit_paths.py` (and `test_commit_paths.py`) to `scripts/`; run `python3 -m unittest discover -s scripts -p 'test_commit_paths.py'` (23 tests, a few seconds); edit `ROLES` in the helper's CONFIG block to your role ids (see "Helper environment" above) | 5 min |
| 2 | Fill `templates/PROJECT-INSTRUCTIONS.md` as `CLAUDE.md`: what the project is, rules 2, 5, 7, 8, 10, 11, 12, the sessions table | 10 min |
| 3 | Two charters from `templates/ROLE-CHARTER.md` (arbiter: orchestrator mode; operator: direct writer). Put the "Minimum variant" table of `templates/WRITE-SCOPES.md` in `docs/STRUCTURE.md` with the placement test from `templates/STRUCTURE.md` | 10 min |
| 4 | Create `docs/decisions.csv` from `templates/DECISION-LOG.csv` (header only). First row: your adoption of the roles and scopes, in your words | 2 min |
| 5 | One handoff file per role from `templates/HANDOFF-FILE.md`, keeping Header (the Record line, the Session state table with its "Wired this session" row and the Open wire-in table; "none" is valid, R5.15), §0, §1, §2, §6 (one line: "Open holds: <ids or none>"), §7, §10. Create `docs/holds.csv` from `templates/HOLDS.csv` (header only; the holds table, R3.12) and `peers/outbox-arbiter.md` and `peers/outbox-operator.md` from `templates/OUTBOX.md` | 5 min |
| 6 | Install commands: `templates/START-COMMAND.md` twice as `.claude/commands/<project>-arbiter.md` (common steps + Arbiter block) and `<project>-operator.md` (common steps + Operator block); `templates/HANDOFF-COMMAND.md` once as `<project>-handoff.md` (Arbiter and Operator branches). Fill the `allowed-tools` placeholders. Optionally merge `templates/settings-permissions.json` into `.claude/settings.json` | 10 min |
| 7 | Smoke tests (next section) | 10 min |

The times are estimates, not measurements. The command templates are long (about 7,000 words together), so step 6 can take longer than its 10 minutes. Steps 2, 3, 5 and 6 can be handed to a bootstrap session (commit with `--no-role "bootstrap"`); your own time is then mostly step 1, your words in step 4 and reviewing the filled files.

Worked, filled versions of these files for a small invented project: `examples/minimal-setup.md`.

## Smoke tests

1. **Commit helper.** In a scratch clone: commit a new file with `--role` (expect exit 0 and only that file in the commit); commit with no role and no `PEERING_ROLE` (expect exit 2 and a message that lists the configured roles and does not name a bypass); commit with `--role` set to a name not in `ROLES` (expect exit 2); commit with `--no-role "bootstrap"` (expect exit 0 and the trailer `Session-Role: none (bootstrap)`); commit `.` (expect exit 2); hold the lock from a second shell (`python3 -c` with `fcntl.flock`) and commit (expect exit 3 after `--timeout`); with the blinding knob on, pass `--held-file` a missing path, the Markdown view and a CSV with a pending row (expect exit 2 for the first two, and a refused verdict word next to the pending id for the third). The bundled unit tests cover these and pairs, frozen paths, held subjects (CSV only, fail closed; only an exact `released` frees a row), secrets in files and messages, and leases.
2. **Messaging.** Session A lists agents and sends a one-line notification to B; B receives it; A closes; B sends to A and observes what happens. Write the observed semantics into the table in `PEER-MESSAGE-PROTOCOL.md`. Send one message per mode (free, relay, blinded, courier) and check the receiver's sender check against the roster in `docs/peer-comms-protocol.md`. No messaging tool → outbox files only.
3. **Start / handoff round trip.** Run the Arbiter start: expect a ≤ 15-line report that ends by waiting for you, with no permission prompts. Ask for one trivial change. Run the handoff: expect a commit through the helper, a header carrying the "Wired this session" row and the Open wire-in table ("none" is valid), rows edited in place with no new header block, and a final line `Next session: …`. Open a fresh session, run the start, and check it names the change. Then run the heading check from the handoff file's contract (`grep -n '^## ' <file>`) and check it passes (sections present in the template's order, the minimum §0 §1 §2 §6 §7 §10 present: the shipped example passes); delete a required heading in a scratch copy and check the start stops with "handoff structure broken". Run `cd templates && python3 -m unittest test_atom_diff` (the atom-diff tool's tests). Hold test: in the Operator session tell the Arbiter "hold X until I say so", have it relay that to the Operator, then reset the Operator and start it fresh: the report must list the hold as `held (relayed, unconfirmed)` first and ask you to confirm it. All pass → setup is done; do the token audit (R6.6) after the first real cycle.

## Quick start B: grow when the trigger happens

| Trigger | Add | Rules and templates |
|---|---|---|
| Insight work keeps displacing record work | a Thinker | R1.9; §4; `BRIEF.md`, `RESPONSE.md`, `THINKER-HANDOFF.md`, `KNOWLEDGE-INDEX.md`, Thinker blocks of the commands |
| Advice depends on a claim that could be wrong | evidence classes, pre-registration, per-datum ledger | §7; `PREREGISTRATION.md`, `DATA-STATUS-LEDGER.md`, `REVIEW-REPORT.md` |
| You are a test subject or rater | blinding | §8; `PENDING-BLINDED-STEPS.md`, `EXPOSURE-LOG.md`, the human-readable set in `STRUCTURE.md` |
| A session corrects its behavior after your feedback | memory entries, the same day | §11; `MEMORY-ENTRY.md` (Claude Code: the project memory folder) |
| Starts get slow or handoffs lose facts | status ledger and now-file, journal, token audit | R5.12, R5.16, R6.6; `STATUS.md`, `NOW.md`, `JOURNAL.md` |
| A status or handoff file grows by dated notes, or a start reads mostly history | consolidate it once into a current-state record, with a drop ledger, an atom diff and a blind reverse-read | R5.16, R5.17, R7.36, R2.14, R2.15; `CONSOLIDATION.md`, `atom_diff.py`, `STRUCTURE.md` §3c |
| Several work items in parallel | role instances | R1.11; §8 of the handoff file |
| An insight is flagged for explanation and a test on the human would cost more than <N, e.g. 2> hours, or a test chosen from the first explanation already failed (off by default; needs the evidence knob and a Thinker) | the investigation phase: isolated generators, averaged probability sheets, a red team, a kill plan, a scored ledger | R7.17–R7.22, R6.11, R6.12; `INVESTIGATION.md`, `LENS-CARDS.md`, `INVESTIGATION-LEDGER.csv` |
| Work gets built and then forgotten between sessions | the full surface inventory and grep at every handoff (the wire-in table and the "Wired this session" and "Open wire-in" header entries are already in the minimum, R5.15) | R5.15; `HANDOFF-COMMAND.md`, `HANDOFF-FILE.md` |
| A job is rerun by hand and you lose track of what is new | the automation table (the status file's table, or `AUTOMATION-RUNS.md` for many jobs) | R5.9; `STATUS.md`, `AUTOMATION-RUNS.md` |
| You deliver files (captures, exports) to the project | data intake: normalize on receipt, catalog | R2.11, R10.9 |
| A second tool duplicates an existing one, or you have more than a handful | the tool registry (until then the rules file's Key commands list is the registry) | R2.12; `STRUCTURE.md` §3b |
| Raw data must be freed or deleted | catalog first, guarded delete script the human runs | R10.9 |
| Tools read data that a held step covers | the machine-read held list: CSV record (with `held_subject` and `holds_from`, so later data of the subject are matched too), Markdown view, helper `--held-file` | R8.12, R8.16, R8.17; `PENDING-BLINDED-STEPS.csv`, `.md` |
| Scorers are built by agents | scorer built from the pre-registration text, pre-run rulings, one-run definition, pins that retire | R7.23–R7.27, R10.8; `PREREGISTRATION.md` |
| A protocol or framework needs maximum rigor | the five-seat review panel | R7.16; `PANEL-BRIEF.md`, `REVIEW-REPORT.md` |
| Two sessions collide on files often | one worktree per role | §15 |
| The human's subjective report is part of the measure and the session infers it from instrument data | blind report inference: words and prediction files sealed outside the working tree (only their sha256 committed), a redacted parent review, a content-token check, the human marks each blind cell; a codebook scored against base rates. On even when the blinding knob is off | R8.18, R7.39, R7.40, R7.41, R6.11; `BLIND-INFERENCE-ROUND.md`, `CODEBOOK.md` |
| You score free-text reports of any kind (tickets, comments, the human's notes) and the counts feed a decision, a hit rate or a claim | a codebook with priors and inter-coder agreement on a fresh sample (on whenever such reports are scored; reading reports one by one is not scoring) | R7.40, R7.41; `CODEBOOK.md` |
| The project holds raw media or publish-restricted data, or has a public remote | media out of version control, a strip list (`STRUCTURE.md` §3d), a deterministic mirror script (you run it; it refuses while any step is held), direct push disabled | R10.12, R7.15; knob "Public mirror" |
| A peer runs your shared tools while you change them | build in a private clone, tool-swap notice and ack (not a hold), drift check, swap, "done" (already on whenever two roles share a working copy) | R10.11, R2.8 |
| An outside tool or non-default dependency is proposed, or a tool prints a number below its own floor | a fit assessment before adoption; void out-of-rule output | R2.16, R2.17; `STRUCTURE.md` §3b |
| Packages of advice go to the human | a pre-relay check script and exact identity keys, once a standing ruling has been caught by hand | R9.25, R7.48 |
| A repeating workflow (a search, a screening, an intake campaign) | a workflow log of lessons and every candidate's data | R14.3 |
| (already on with applied work; listed so you know what to expect) A first package for a new configuration, or a "no data" basis | every setting designed with a label and a resolvable source; "no data" only after the listed sources were searched | R9.27, R9.13 |
| (already on with applied work; listed so you know what to expect) The same mistake caught a second time | one root-cause pass, then only the minimum effective remediation | R9.26 |
| An analysis designed after the data were recorded | design commit before decoding; never VALIDATED, at most STRONG; the analyst's harness-loaded context checked | R7.50; `REVIEW-REPORT.md` |
| A detector's parameter is tuned, or a per-case offset is calibrated from items assumed neutral | the detector tested against matched non-events first; calibration items justified | R7.51, R7.52; `REVIEW-REPORT.md` |
| A rule that changes with time | visible switch, countdown, queue rows (a malformed stamp blocks a blinding, publish, frozen-record or secret guard) | R2.19 |
| You want to save budget by deferring work | a budget mode: a decision-log row in your words that states what it defers, what it never defers and its lapse | R6.18 |
| A summary figure or rating the system computes drives settings | read it as an output, never a target | R9.23 |
| A build costs more than <K, e.g. 150 thousand> tokens or touches a pinned tool | a build plan with a cheaper alternative, decisions with fallbacks, the vetting table and per-phase rulings | R6.17, R4.16; `BUILD-PLAN.md` |
| Asks on the human pile up across sessions | one command that walks the human through everything waiting, from declared state files | R9.24; `HUMAN-QUEUE-COMMAND.md` |
| Applied work over several rounds (packages) | already on (§15 applied-work row): the stop rule, chosen measurement contexts, package guards with margin and valence, a use rule for review output; add the loop-state block | R9.19, R9.20, R9.21, R6.16; `OPERATOR-FOLDER-HANDOFF.md` |

## Upgrading from v1.6

v1.7 adds 11 rules and amends 30; nothing is renumbered and nothing is breaking. `atom_diff.py` is unchanged; `commit_paths.py` has one fail-closed fix (a status of `Released` or `RELEASED` no longer frees a held row; only an exact `released` does) and its 23 tests still apply (one test gained a row). No template is new. Adopt first the cheap clauses that prevent incidents: a checker that says what it skipped and never counts a skip as a pass (R2.15, appendix #101), and "no data" only after the listed sources were searched (R9.27, R9.13, appendix #95). In order:

1. **Re-copy the changed templates, by knob**, and carry over your filled placeholders; for a one-sentence change, paste the sentence instead.
   - **Everyone:** `SUBAGENT-BRIEF.md` (needs-shell line; number-parsing pitfalls; cache and fallback rules; tools-needed line; decision-inputs block), `STRUCTURE.md` (placement rows: initiative register, multi-run records, planned files, work queue, trigger bundles, setting-to-source map, caught-miss log), `HANDOFF-COMMAND.md` and `START-COMMAND.md` (two wire-in rows; a standing-rules row; budget-mode and caught-miss take-stock items; the handoff size-gate step; deferred tools in `allowed-tools`), `HANDOFF-FILE.md` (header rows "Budget mode" and "Start-read size"), `PEER-COMMS-PROTOCOL.md` (hold-registered notice, a `blinded` message), `settings-permissions.json` (`git rm` in `deny`).
   - **Thinker knob:** `RESPONSE.md` (header row "Misses since last response"), `STATUS.md` (Thinker-log column "Premise failed").
   - **Evidence knob:** `PREREGISTRATION.md` (three §B rows, a §G row, the after-capture design field), `REVIEW-REPORT.md` (tool checklist extended; two new checklists).
   - **Blinding knob / machine-read held list:** `PENDING-BLINDED-STEPS.csv` and `.md` (columns `held_subject`, `holds_from` as an ISO 8601 timestamp, `peers_notified`; append the three columns to an existing held list, the helper reads only `step_id`, `family` and `status`; the data-reading tools you own must match `held_subject` and `holds_from`, R8.17).
   - **Applied-work discipline:** `OPERATOR-FOLDER-HANDOFF.md` (four loop-state rows), `HUMAN-QUEUE-COMMAND.md` (proposed / ready states, new declared sources, resume across sessions from the declared path only).
2. **Project-side changes. Hand this step to the Arbiter as one brief; you do nothing here.** The Arbiter applies each item the next time its trigger happens, not all at once. (a) Give every checker a per-run "checked / skipped" report and a coverage rule for each positive duty (R2.15; a checker prints what it did not check); (b) from now on the first package for a configuration, and the first after a structural change, designs every setting with a label and a resolvable source (R9.27), and search the listed sources before writing "no data" (R9.13); (c) after a second catch of one mechanism, run one root-cause pass and apply only the minimum remediation (R9.26); (d) a blind analysis of already-recorded data is filed as STRONG at most, never VALIDATED, with a design commit that precedes decoding (R7.50; an analysis designed after the data were recorded cannot be filed as validated); (e) record any budget-saving mode with its scope and lapse, as a decision-log row in the human's words (R6.18); (f) time-switched gates print their countdown and queue what they accept (R2.19; a rule that starts blocking on a date prints how long is left); (g) cite planned files as non-path text until they exist (R5.20).
3. **Your part (the human).** Nothing is required at upgrade. From now on you may be asked for: a short endorsement word per settings group at natural milestones, only if you turn a preference zone on (R9.28); a yes for each work queue and addition, shown as "proposed, needs yes" until you approve (R9.24); the name of a run context the references cannot identify (R2.20) and of each initiative (R2.21); your choice for a setting with no footprint (R9.19); and a decision-log row for any budget-saving mode (R6.18). These are now in § "Your job as the human". You will also see a "checking" reply instead of a quick guess (R9.17) and a first package that lists every setting with its basis (R9.27).

**What you will notice.** The v1.7 rules close the gap between "the checker passed" and "the work was done": a skipped check is shown, a first package is complete, and a repeated miss gets one analysis instead of one patch each.

## Upgrading from v1.5

v1.6 adds 19 rules and amends 33; nothing is renumbered and nothing is breaking. `commit_paths.py` and `atom_diff.py` are unchanged (their tests still apply). Adopt first the cheap clauses that prevent incidents: gating a commit on the check's own exit status, never a pipe (R10.4, appendix #70), and building commit path lists from the files the session wrote plus its subagents' OUT lines within their briefs, never the whole tree's status (R10.2, appendix #71). In order:

1. **Copy two new templates** (only if their trigger has happened): `templates/BUILD-PLAN.md` (a build that costs more than <K> tokens or touches a pinned tool; R4.16, R6.17) and `templates/HUMAN-QUEUE-COMMAND.md` (one command that walks the human through what waits on them; R9.24).
2. **Re-copy the changed templates, by knob**, and carry over your filled placeholders; for a one-sentence change, paste the sentence instead.
   - **Everyone:** `PROJECT-INSTRUCTIONS.md` (rule 10: fit assessment, private clone, mirror; rule 12: deliverable first), `STRUCTURE.md` (§3b registry columns and statuses, new §3d strip list and §3e result-free path classes, two placement rows), `WRITE-SCOPES.md` (two rows), `SUBAGENT-BRIEF.md` (commit paths = OUT lines within the brief; shell pitfalls; tool-building rules), `ROLE-CHARTER.md` (rules 14 and 15), `HANDOFF-COMMAND.md` (the wire-in rows, an open tool swap in flight, the queue line), `HANDOFF-FILE.md` (owner `human`), `START-COMMAND.md` (the missing wire-in rows, standing rules for the new action-time rules, the queue line in the report) and `PEER-COMMS-PROTOCOL.md` (the instance-id check; the tool-swap notice), `settings-permissions.json` (`ask`: `git remote set-url` / `add` / `remove` / `rename`, `git clone`; `deny`: `git add` on raw-media paths, filter tools, the publish script; fill or delete the placeholders; the `git add` row only stops a stray direct add, and the binding media control is a repository check plus `.gitignore`, R10.12).
   - **Thinker knob:** `BRIEF.md` (decisions with fallbacks; `answered-by:` line), `RESPONSE.md` (fallback column; failure-mode table).
   - **Evidence knob:** `PREREGISTRATION.md` (four §B rows), `REVIEW-REPORT.md` (checklist for tools, builds and validity rules).
   - **Applied-work discipline:** `OPERATOR-FOLDER-HANDOFF.md` (workflow log, pre-relay checker, round order). **Blind report inference:** `BLIND-INFERENCE-ROUND.md` (the order that ran may be `values first`).
3. **Project-side changes.** (a) If two roles share a working copy, change shared tools a peer runs only from a private clone (R10.11); records and documents keep the in-place rule (R2.8). (b) If you hold raw media or publish-restricted data, or have a public remote, turn on the new knob "Public mirror": media out of version control, a strip list, a deterministic mirror script, direct push disabled (R10.12). (c) Register peer-built tools as `side, not reviewed` at once (R2.13); add a fit assessment and the human's yes before any outside tool or non-default dependency (R2.16). (d) Whenever you write or review a tool, build, acceptance test or validity rule (whatever the evidence knob says), give every acceptance test the question "could this fail on a wrong build?" (R7.45) and every validity rule two ends (R7.44). (e) Put your standing rulings about advice into one tested pre-relay script once a ruling has been caught by hand (R9.25).
4. **Wire in:** phase rulings and adopted vetting items go into the method doc in the commit of their phase (R4.16); derived records are rebuilt only after their source is final (R5.19).
5. **Your part (the human).** Nothing is required at upgrade. From now on you also approve outside tools and non-default dependencies (R2.16), choose between a build and its cheaper priced alternative when the trade is yours (R6.17), run the mirror publish script yourself under the Public mirror knob (R10.12), and may run the new command that lists everything waiting on you (R9.24). One optional decision: the order of a blind round. The default is unchanged (your marks come before the next values). If you would rather have the values first, say so once, in your own words; it is recorded as a ruling, marking becomes optional per round, and nothing then gates your values (R8.18 (8), R9.22).

**What you will notice.** No stage you did not ask for runs before your answer (R9.22); if you choose values-first, the next values arrive with the open prompt. Values are never carried over from another subject without a basis; the message is "no data", followed by the sources that were searched (R9.13, R9.27). A tool that prints a number below its own floor is fixed, and the number is withdrawn (R2.17).

## Upgrading from v1.4

v1.5 adds 16 rules (R3.13: the peer-comms protocol and message modes) and amends 27; nothing is renumbered and nothing is breaking. `commit_paths.py` and `atom_diff.py` are unchanged. In order:

1. **Copy two new templates** (only if their trigger has happened): `templates/CODEBOOK.md` (any scoring of free-text reports, R7.40, R7.41) and `templates/BLIND-INFERENCE-ROUND.md` (the new knob "Blind report inference", R8.18, GUIDELINES §15).
2. **Re-copy the changed templates, by knob**, and carry over your filled placeholders. For a one-sentence change, paste the sentence instead of re-copying the file.
   - **Everyone:** copy `PEER-COMMS-PROTOCOL.md` to `docs/peer-comms-protocol.md`, fill the roster, and tag messages and outbox rows with `mode:` (R3.13); re-copy `PEER-MESSAGE-PROTOCOL.md` (Authority section moved into it) and `OUTBOX.md` (Mode column). `START-COMMAND.md` (new standing-rules rows, R5.15; reads the protocol), `ROLE-CHARTER.md` (reset line; rules 11–12), `HANDOFF-COMMAND.md` (read each peer's open wire-in table directly; closed-design wire-in row; message requests paired), `PROJECT-INSTRUCTIONS.md` (rule 7 gains scripts, search-the-record and guard sentences; rule 12 the "not needed" line), `STRUCTURE.md` (§3b promotion-runs column; two placement rows), `WRITE-SCOPES.md` (round-file rows, footnote 21), `SUBAGENT-BRIEF.md` (scripts and blind-analyst constraints).
   - **Thinker knob:** `BRIEF.md`, `RESPONSE.md` (audit table gains "Rule or practice it replaces" and a "Deliberately left out" list; message requests), `THINKER-HANDOFF.md` (closed designs).
   - **Evidence knob:** `PREREGISTRATION.md` (count-only pass with the proxy branch, selection-rule check, actor operating point, fit-set commits), `REVIEW-REPORT.md` (disposition footer; unit, codebook and model-version checklists), `DATA-STATUS-LEDGER.md`.
   - **Applied-work discipline:** `OPERATOR-FOLDER-HANDOFF.md` (loop state, "not needed" line).
3. **Project-side checks.** Any pre-registration not yet sealed gets the count-only pass (R7.37) and the selection-rule check (R7.38). Applied-work reviews run the whole-subject sweep unprompted (R6.13 is now scoped to project-claim reviews). Mechanical jobs move from judging agents to tested scripts (R6.15). A blind round's words and prediction files move outside the working tree with only their sha256 committed, and the analyst's inputs are checked by content (R8.18, R6.11).
4. **Wire in:** list each closed design (R5.18) as an open wire-in item until its ledger row says so; a tool's promotion row gets both run hashes (R2.13).
5. **Your part (the human).** Nothing, unless you turn on blind report inference; then you mark at most <5> cells per round, on a four-value scale (named / partly / missed / can't say) from claim lines alone. You also see: a "not needed" line at the end of every ask (R9.1); Thinker questions that state the decision they unlock and fit in about a minute (R4.14); a stop call when a loop has nothing left worth trying (R9.19).

**What you will notice.** Asks state their floor, cap and counted unit (R9.1). Review output shrinks every few rounds (R6.16). A written disposition for every Critical or High finding (R7.7). Roles reset on a context fraction, not a brief count (R6.9, provisional). A new model version is vetted before it drives blind predictions (R7.42).

## Upgrading from v1.3

1. **Breaking, handoff and status files.** v1.4 replaces the history-marker contract with "write the state, log the event" (R5.2, R5.3, R5.16). A handoff or status file is now a current-state record: rows edited in place, no `**[history]` blocks, no dated sections, a "Record" line naming the commit that holds the old version. **Choose a path.**
   - **(A) Not now.** Keep the `**[history]` markers as the legacy reading aid (R5.3). The v1.4 start reads both forms (it detects a legacy file with `grep -c '^\*\*\[history\]' <file>` and reports "legacy file: <path>"), so you can switch the commands at any time; list each legacy file as an open wire-in item for consolidation.
   - **(B) Consolidate, one role at a time.** Quiesce the live peers first: record a hold in the holds table ("no start or handoff by <role> until its switch commit"), confirmed by you, and release it in the switch commit. For each role: **(1)** create the now-file from `templates/NOW.md` and the status ledger from `templates/STATUS.md` (the v1.4 start reads both and stops on an empty read, so they come first); **(2)** in one commit switch that role's start command and the new handoff-file and status templates (R2.14): re-copy `START-COMMAND.md` and `HANDOFF-COMMAND.md` whole (the handoff command is one universal file: switch it with the first role) and carry over your filled placeholders; the v1.4 start still reads a legacy file; **(3)** consolidate that role's handoff, then the status file, in its owner's session with a drop ledger, an atom diff and a reverse-read (R5.17, R7.36; `templates/CONSOLIDATION.md`); a role's file stays legacy until its consolidation commit; **(4)** run a start and a handoff to prove it (R2.14).
   - **Cost and your part.** The Arbiter session runs it, with subagents for the question writer, rewriter, readers and scorer: about one Arbiter session per role file. Handoffs are start reads and the status file is human-readable, so both take the full form (R7.36). Your part: read the rules section of each rewritten status file and confirm it (about 10 minutes per file); rule on a stale key if asked. Apply the §15 "Record consolidation" row at the size of the file. Before you start: copy `templates/atom_diff.py` and `test_atom_diff.py` to `scripts/` and run its tests (the atom diff needs a tool), and make an off-machine backup of the repository (dropped history survives only in `.git`).
2. Add the new `STRUCTURE.md` §3c (record kinds, the never-consolidated list including the held list, holds table and exposure logs, checker exemptions with a reason each) and the rows for the now-file and consolidation records (main file and the key file in its own sealed folder) in the placement test and the write-scope matrix (footnote 20: each role writes its own now-file row).
3. Re-copy `PREREGISTRATION.md` (decisiveness table; verdict rows by interval relations) and apply the new R7.2 gate to every pre-registration, whatever the investigation knob. Re-copy `SUBAGENT-BRIEF.md`, `REVIEW-REPORT.md`, `PANEL-BRIEF.md`, `BRIEF.md`, `RESPONSE.md`, `ROLE-CHARTER.md` role-specific rules 8–10, `PROJECT-INSTRUCTIONS.md` (rule 12 and the read-first row), `EXPOSURE-LOG.md`, `PENDING-BLINDED-STEPS.md` and `settings-permissions.json` (new `ask` and `deny` entries; verify them against your harness and fill or delete every `<placeholder>` row).
4. `commit_paths.py` is unchanged in v1.4 (its docstring still says v1.3); its 23 tests still apply. Gating a commit on the check's own exit status (R10.4) is a project-side change to your commit flow.

## Upgrading from v1.2

1. **Breaking:** the helper now refuses a commit with no role or an unconfigured role. Re-copy `commit_paths.py` and its tests, set `ROLES`, and add `--role <role-id>` to every script, hook and alias that calls it (or use `--no-role "<reason>"` for a deliberate bootstrap commit).
2. Append `,scope,quote_fidelity,question,options` to the decision log's header and set `quote_fidelity` to `legacy` on every existing row; old rows keep their status. Add one decision-log row recording the adoption and the cut-off id (R7.31).
3. Create `holds.csv` from `templates/HOLDS.csv`, add §6 (one line) to each handoff file, and re-copy the start command's step 7 and A5 (i)–(k), the handoff command's wire-in "ruling" row, Holds row and step 11, the rules file's rules 2 and 12, and the charter's role-specific rules.
4. Run the helper tests (23).

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
| Applied work (§9: package, lever, range, readout) | a settings set, each setting's adjustable range, the displayed summary figure | a config change set, allowed values or schema, a dashboard KPI | an edit set, style-guide bounds, a readability score | a change window's parameters, policy limits, an SLO panel |
| Configuration (R9.27, R9.28, R7.51: configuration, structural change, settings group, detector) | a setup and its adjustable settings, a replaced component, a settings page, an event flag | a deployment's config, a dependency or schema upgrade, a config module, an alert rule | a style sheet, a change of form or audience, a section of the style sheet, a lint rule | a service's parameter set, a platform migration, a policy group, an alert |
| Endorsement (R9.28) | a word per settings page at a campaign's end | a word per config area at a release | a word per section at a draft's end | a word per policy group after a change window |

## File map

| File | Purpose | Required at | Read when |
|---|---|---|---|
| `README.md` | this file | minimum | first |
| `GUIDELINES.md` | numbered rules with Why / Fails as; knobs (§15) | minimum | the core-rules box at setup; a section when its knob turns on |
| `appendix-worked-example.md` | the source project and the incidents behind the rules | — | when a rule seems like red tape |
| `examples/minimal-setup.md` | filled minimum files for an invented project (current for v1.7; last changed in v1.6) | — | during Quick start A |
| `CHANGELOG.md` | what changed between versions and why | — | when upgrading |
| `LICENSE` | MIT terms for the docs, templates and helper | — | before reusing or redistributing |
| `templates/commit_paths.py`, `test_commit_paths.py` | the commit helper (lock, new files, pairs, frozen paths, held subjects from the CSV list, role list and `--no-role REASON`, secrets in files and messages, leases) and its tests | minimum | setup |
| `templates/settings-permissions.json` | Claude Code allow / ask / deny rules for R10.6 (deny rules match command text, not effects; `<raw-data path>` and `<sealed path>` are placeholders to fill in or delete; verify the rule grammar in your harness version) | default | setup |
| `templates/PROJECT-INSTRUCTIONS.md` | the auto-loaded rules file | minimum | setup |
| `templates/ROLE-CHARTER.md` | one role: purpose, authority, mode, scope, model, lifecycle | minimum | adding a role |
| `templates/WRITE-SCOPES.md` | ownership matrix (S / W / A / P / R / N, human-readable set), minimum variant | minimum | before writing outside your folder |
| `templates/STRUCTURE.md` | layout, placement test, path map, human-readable set, frozen manifest | minimum | before creating a file |
| `templates/START-COMMAND.md` | session start: common steps plus a block per role | minimum | setup |
| `templates/HANDOFF-COMMAND.md` | universal handoff with a branch per role | minimum | setup |
| `templates/HANDOFF-FILE.md` | a role's memory file, a current-state record with a heading-order contract | minimum | setup |
| `templates/OUTBOX.md` | a role's outgoing messages (the file is the message) | minimum | setup |
| `templates/PEER-COMMS-PROTOCOL.md` | installed as `docs/peer-comms-protocol.md`: team roster, sender verification, the four message modes (free, relay, blinded, courier; R3.13) | minimum | setup; every start, every role |
| `templates/PEER-MESSAGE-PROTOCOL.md` | outbox mechanics: when to message, format, content rules, delivery, observed harness semantics | minimum | before the first message |
| `templates/DECISION-LOG.csv` | the human's rulings (header only) | minimum | setup |
| `templates/HOLDS.csv` | the holds table: restrictions the human imposed, relayed or direct, with state and release condition (header only; append-only; R3.12) | minimum | setup; every start |
| `templates/SUBAGENT-BRIEF.md` | a subagent's task, scope, tools and return format | default | before spawning |
| `templates/JOURNAL.md` | per-session event log for the handoff | default | every session |
| `templates/STATUS.md` | the status ledger (one row per subject, trajectory, queue, unknowns, rulings), automation runs, Thinker log with dispositions | default | Arbiter start |
| `templates/NOW.md` | the now-file (size guide e.g. 40 lines): current cycle, session start and end, next action per role (the one copy), last full check | default (status knob) | every session start |
| `templates/CONSOLIDATION.md` | one consolidation in two files: the key file (question set and answer key, in its own sealed folder) and the main file (score, key-literal and adjusted; drop ledger; atom map) | knob: record consolidation | before and after rewriting a drifted record (R5.17, R7.36) |
| `templates/atom_diff.py`, `test_atom_diff.py` | reference atom-diff tool (numbers, ids, dates and class words present in the old file and absent from the new file and the ledger; stdlib, tests) | knob: record consolidation | consolidation; handoff record gate (R5.7, R5.17) |
| `templates/OPERATOR-FOLDER-HANDOFF.md` | per-work-folder handoff and next-session prompt | default | Operator handoff |
| `templates/MEMORY-ENTRY.md` | a persistent behavior rule | default | after a correction from the human |
| `templates/BRIEF.md`, `templates/RESPONSE.md` | the Thinker exchange (three core response shapes, plus merge and plan for the investigation knob) | knob: Thinker | writing or answering a brief |
| `templates/THINKER-HANDOFF.md`, `templates/KNOWLEDGE-INDEX.md` | the Thinker's handoff and entry point | knob: Thinker | Thinker setup |
| `templates/PREREGISTRATION.md`, `templates/DATA-STATUS-LEDGER.md` | predictions before data; spent-data status | knob: evidence | before a confirmatory test |
| `templates/CODEBOOK.md` | a codebook for free-text reports: axes, units and weights, out-of-scope bucket, "unspecified" values, valence, prior table with smoothing, agreement table, uncodable share | knob: blind report inference (also on whenever free-text reports are scored, R7.40, R7.41) | before scoring reports |
| `templates/BLIND-INFERENCE-ROUND.md` | per-round file set for a blind report inference: sealed words and prediction files, blind cells file (claim and basis lines), the scoring card, score file; who may read which; commit order; audit lines | knob: blind report inference | each round (R8.18) |
| `templates/BUILD-PLAN.md` | a design memo for a multi-phase build: summary with the priced cheaper alternative, decisions with fallbacks, phases, vetting table, per-phase rulings, failure modes, generality check, superseded line | default (builds above the token threshold) | before a large build (R4.16, R6.17) |
| `templates/HUMAN-QUEUE-COMMAND.md` | one command that walks the human through every item waiting on them, from declared state files only, with options, a recommendation and what each unlocks | default | setup; whenever asks pile up (R9.24) |
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
| Current-state record; event record | a record with one row per subject, edited in place (status ledger, handoff, now-file, knowledge records); a record that is the event itself (test record, log, journal, frozen record) and is never consolidated (R5.16) |
| Trajectory | a table of dated flips (from → to, cause, pointer) kept inside a current-state record (R5.16) |
| Drop ledger; atom map; atom diff | the three records of a consolidation: where each dropped item went, where each class word and proof pointer went, and the mechanical list of old dates, numbers, class words and ids found nowhere (R5.17) |
| Reverse-read | a blind test of a rewritten record: questions and key written from the old file and sealed first, fresh readers of old and new, a separate scorer (R7.36) |
| Lazy-read markers (legacy) | `**[history]` lead-ins of v1.3 that let a start read only current blocks; a legacy form kept until the file is consolidated (R5.3) |
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
| Blind report inference; codebook; count-only pass | an analyst infers what the human experienced from instrument data while the human's words are physically absent (sealed outside the working tree), and the human marks the cells from claim lines (R8.18); the set of coding axes, priors and agreement table that scores free-text reports (R7.40, R7.41); a count-only run on the data a pre-registration will score, before it is sealed (R7.37) |
| Package guard | a non-inferiority check on an outcome a package must not worsen, with a margin and an unwanted side (R9.21); not a tool guard that refuses a datum (R8.16) |
| Values-first round | a blind round whose next values are sent first, as a bare list, with the open prompt, by the human's explicit ruling; marking is optional and never gates the values (R8.18 (8), R9.22) |
| Open prompt | the fixed, committed question that asks the human for their words in a blind round, naming no lever or expected effect (R8.18 (1)) |
| Private clone; tool-swap notice; swap | a copy of the repository outside the shared tree where a shared tool is changed and tested, then copied in after a notice to every role that runs it, their acks and a drift check; the notice is not a hold (R10.11) |
| `side, not reviewed` | registry status of a peer-built tool whose outputs stay leads until promotion (R2.13) |
| Build plan; vetting table | the design memo of a large build and the per-decision verdicts from its review (R4.16, R6.17) |
| Pre-relay check; standing ruling | one tested script that checks every package against the human's standing rulings before the human sees it; a standing ruling is a rule about how advice is shaped that the human gave once (R9.25) |
| Workflow log | per-step lessons of a workflow the human will run again (R14.3) |
| Design commit (after capture); blind analysis after capture | the commit of a design and metric list made after the data were recorded; such an analysis is never VALIDATED and earns at most STRONG (R7.50) |
| Negative-only checker | a checker that flags forbidden content only; it cannot certify a positive duty (R2.15) |
| Preference zone | a per-subject range built by script from outcomes the human endorsed, used as a starting prior and never as a fence (R9.28) |
| Queue command | the one command that walks the human through everything waiting on them, from declared state files only (R9.24) |
| Public mirror; strip list | a deterministic filtered copy of the history published to a public remote while the local history stays intact for hash citations; the list of paths and extensions it removes (R10.12) |
| Fit assessment | the written check, before adopting an outside tool or dependency, of every intended use against barred parties and existing tools, with a ground-truth benchmark where it reads data (R2.16) |
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
| Positive duty | something a deliverable must contain (every setting designed, every source cited), as opposed to something it must not contain (R2.15) |
| Budget mode | a recorded, time-limited decision, in the human's words, to defer named work to save budget (R6.18) |
| Time-switched rule | a check that warns until a set date and blocks after it, printing the time left (R2.19) |
| Verdict-diff sweep | re-running a changed checker over every record and listing the verdicts that changed, with causes (R10.11) |
| Basis label; setting-to-source map | the kind of reason behind a value (calculation, data, precedent, judgment); the list of where to look for each setting before writing "no data" (R9.27) |
| Structural change; `held (parent)` | a change that alters which settings exist or what they act on (R9.27, R2.18); a setting a later package leaves at its parent package's value (R9.27) |
| Endorsement word | the one-word verdict per settings group that feeds a preference zone (R9.28) |
| Initiative register | one row per line of work that shares the repository (R2.21) |
| Run scope | one metadata block per run in a multi-run file, "run k of N" (R2.20) |
| Provisional | a rule based on one project's incidents, revisited when a second project reports (GUIDELINES §15) |
| Caught-miss log | one row per correction the human makes to a session's work, keyed by mechanism (R9.26) |

## License

MIT. See `LICENSE`.
