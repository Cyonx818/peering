# Changelog

Rule ids are stable: v1.0 ids keep their number (their text may change, as listed here); new rules are appended within their section. Finding ids refer to each version's review-panel disposition table, kept with the maintainers' development records (not published).

## v1.3 (2026-10-05)

Produced from a second exchange with the source project's sessions: the gap analysis of what the source project learned after v1.2 (51 learnings, 12 missing, 25 partial), the "where the source project is ahead" list of the reverse analysis (items A1–A5), and the Operator and Thinker lessons files. Then run through the five-seat review panel (R7.16; see "Review panel (R7.16)" below). Keyed to appendix incidents #36–#46 (new in this version). No existing rule id was renumbered or moved.

### Upgrading from v1.2
1. **Breaking:** the helper refuses a commit with no role or a role not on its `ROLES` list; its refusal no longer names a bypass. Re-copy `commit_paths.py` and `test_commit_paths.py`, set `ROLES`, and add `--role <role-id>` to every script, hook and alias that calls it; a deliberate bootstrap commit uses `--no-role "<reason>"` (trailer `Session-Role: none (<reason>)`). Never export `PEERING_ROLE` in a shared shell profile.
2. Append `,scope,quote_fidelity,question,options` to the decision log's header, set `quote_fidelity` to `legacy` on every existing row (legacy rows keep their status and are confirmed with the human only when next relied on), and add a decision-log row naming the cut-off id (R7.31).
3. Create the holds table from `templates/HOLDS.csv` (R3.12); add §6 to each handoff file; re-copy START-COMMAND step 7, A2, A5 (i)–(k) and the standing rules, HANDOFF-COMMAND (wire-in "ruling" row, Holds row, step 11), the rules file's rules 2, 12 and the compaction line, and the charters' role-specific rules.
4. Run the helper tests (23).

### New rules (appended within their sections)
- R2.13 a peer may build a tool in its own scope, the Arbiter promotes it (incident #41).
- R3.12 a relayed hold only restricts, never permits (#37); rewritten by the panel (see below): holds table, state `held (relayed, unconfirmed)`, the human is always the releaser.
- R4.14 the Thinker asks the human only on a brief's grant that also clears the held steps (#38).
- R6.13 recompute only what the change can reach (#36).
- R7.31 ruling fidelity: verbatim, relayed or paraphrased, and what the session added (#38, #39); R7.32 between-session comparisons carry a drift allowance (#46); R7.33 exploratory fits report an honest out-of-sample score (#40); R7.34 golden fixtures come from raw samples (#41); R7.35 enumerate the whole option space before proposing paths (#44).
- R9.13 advice states its rung on the advice ladder; R9.14 applied work runs in packages; R9.15 name things the way the human knows them (#45); R9.16 the human's report before any number (#42); R9.17 a waiting human gets the answer first (#43).

### Amended rules (ids unchanged)
- R2.11 reply first when the human waits; R4.6 header lists reads beyond the brief; R5.15 a ruling's wire-in greps loaded standards for text it contradicts, and the Arbiter lists peer close commits at start (the pass itself runs after the human's choice); R6.5 a campaign analyst may be resumed across reviews (never across a change in what it may read); R7.2 quantized readouts get a predicted reading on the grid and a not-resolvable mark; R7.11 pointer to the new columns; R7.14 scoped to project claims; R7.28 split complaints, unverifiable levers, structural changes last; R9.1 deterministic readouts; R9.5 bulk reads in the human's medium; R9.7 predictions committed before the readout, also for informal sets.
- From the source project's own practice (reverse analysis, "ahead" list): R2.5 content-checked seal pass-through (A5) and an append-only prefix guard described as a project option (A2); R7.22 optional fill-once ledger variant (A2); R8.15 optional numeric and verdict-word tripwire (A1); R9.15 and R7.31 `scope` column and the all-roles wire-in of a naming ruling (A3, A4).

- Also changed in v1.3 and not listed above (panel PRF-L8): §13 gains six rows (R9.14, R3.12, R9.16, R7.34, R7.35, R7.33) and the panel adds a seventh (relayed hold as a release channel); the §15 rows Thinker, Pre-registration and Peer messaging are updated; R1.3 notes that the Thinker's questions to the human are not advice (W8).

### Fixes to rules that looked wrong (B §5)
- W1 R9.11 (3) now reads "one change or one package" with signatures and a backout order. W2 the §12 row on relayed rules is split: permissions stay leads, restrictions are honored (R3.3, R3.4 point to R3.12). W3 R9.1 no longer sends a deterministic readout to a pilot. W4 R7.14 is scoped to project claims. W5 the reference helper refuses a commit with no role unless `--no-role` is passed. W8 the §1 Thinker row and R1.3 allow questions on a brief's grant. W9 `THINKER-HANDOFF.md` counts non-blank lines.
- W6 (numeric tripwire) and W7 (append-only guard) are described in R8.15 and R2.5 as project options; the reference helper does not implement them (see "Not applied").

### Templates and helper
- `DECISION-LOG.csv` (and the example) gains `scope`, `quote_fidelity`, `question`, `options`; `BRIEF.md` a "Questions to the human" field; `RESPONSE.md` a "Reads beyond the brief" header row and a "Human Q&A (verbatim)" section; `HANDOFF-FILE.md` §6 (superseded by the panel: it is now a view of the holds table); `HANDOFF-COMMAND.md` and `START-COMMAND.md` the wire-in row "ruling → decision log and every standard it contradicts", the peer-close wire-in pass and the open holds in take-stock; `THINKER-HANDOFF.md` "≤ 40 non-blank lines"; `ROLE-CHARTER.md`, `SUBAGENT-BRIEF.md`, `STRUCTURE.md` (two placement rows), `WRITE-SCOPES.md` (peer-built tool row), `PEER-MESSAGE-PROTOCOL.md` (relayed restrictions).
- `commit_paths.py`: refuses a commit with no role (exchange step; the suite grew from 16 to 17 tests, which the panel ran and passed); docstring and version string updated; README smoke test 1 and the test counts in README updated. The panel then changed it again (see below): role list, `--no-role REASON`, env fallbacks.

### Appendix
- Incidents #36–#46, evidence cited generically.

### Review panel (R7.16)
v1.3 went through the five-seat panel after the exchange step: 79 findings (C 0, H 13, M 34, L 32), 51 applied, 26 applied with a change, 2 declined. The Arbiter ruled six cross-seat points:
- **R-1 relayed holds (R3.12):** a relayed hold only restricts, never permits. State `held (relayed, unconfirmed)`; the releaser is always the human, never the relayer or a role it names; the receiver confirms the hold with the human at the next contact; any release needs the human's own words, recorded verbatim. Holds live in a small holds table (`templates/HOLDS.csv`: id, scope, source, state, release condition; part of the minimum), read by the start command and listed in the take-stock and the start report; tools reading it fail closed. A decision-log row below `verbatim`, and a new `relayed-by-<role>` fidelity value, is a lead until the human confirms it and does not bind (R7.31). Handoff §6 became a view of the table and joined the minimum handoff.
- **R-2 the Thinker's questions (R4.14):** only when the brief grants them and states that no held step involves the human (or names the held steps and forbids touching them); value-free; screened by the Arbiter while any held step is open; Human Q&A moved out of the value-free body.
- **R-3 always-on rules:** R7.28, R7.32, R7.34 and R7.35 stay in §7 with an "on regardless of the evidence knob" clause (cleaner than renumbering into §9); every new rule a session must follow is cited in the start command's standing rules, the charter or the rules file; a §15 row "Applied-work discipline" gives the small form.
- **R-4 migration:** rows written before the columns existed get `quote_fidelity` `legacy`, are not demoted and are confirmed only when next relied on; the adoption is a decision-log row naming the cut-off.
- **R-5 answer first (R9.17, R9.7):** the prediction commit lands before any readout of the data it predicts; answer-first governs reply order only, never data access; the commit is the next tool call of the same turn; other owed bookkeeping goes to the journal as `owed:` lines that the take-stock lists.
- **R-6 helper:** the refusal no longer names the bypass; the role is validated against `ROLES`; `$PEERING_ROLE` stays as a validated fallback documented in the README; `--no-role REASON` writes a visible trailer, and the harness `ask` list covers it; `$PEERING_HELD_FILE` and a `REQUIRE_HELD_FILE` switch close the opt-in held-list gap. Suite: 17 tests passed in the panel's runs before these changes; the revised suite has 23 and was not run by the writer (no shell): run `python3 -m unittest test_commit_paths` in `templates/` before release.
- Also: R9.13's ladder is now the "advice ladder" (R7.1's class ladder keeps "evidence ladder"); R2.13 grows (fixtures, wire-in trigger, refusal tests); R6.13 gains sentinels and a map owner; R6.5 gains a resume checkpoint; R7.31 gains the CSV writing rules and the verbatim-pointer requirement; R7.35 enumerates from the source of truth; the `ready` state is renamed `deferred`; British spellings and the catalog / catalogue mix are fixed; templates gain the holds table, a REVIEW-REPORT checklist for R7.33, a PREREGISTRATION quantized-readout row and an "On hold" section in the Thinker handoff.

### Not applied
- Helper options `--append-only` (prefix guard, optional fill-once mode, W7) and `--value-free-paths` with `--allow-values` (numeric tripwire, W6): larger changes needing several new tests; documented as project options in R2.5 and R8.15, left out of the reference helper.
- Decision-log header comment (B §9): a comment line would break the CSV readers that fail closed; the column meanings live in R7.31.

## v1.2 (2026-10-04)

Produced from a two-way exchange with the source project's sessions: the gap analysis of what the source project learned after v1.1, plus lessons from its Operator and Thinker sessions. Then run through the five-seat review panel (R7.16): 87 findings, all addressed (see "Review panel (R7.16)" below). Keyed to appendix incidents #24–#35 (new in this version). No existing rule id was renumbered or moved; v1.1 R8.4 and R10.5 and the §15 "Pinned tools" and "Pre-registration" rows were corrected.

### Investigation phase (knob: investigation; incident #35, appendix lesson 9)
- New R7.17–R7.22: investigate before choosing what to test; fact sheet and divergent generation with lens cards; merge with mandatory rival slots; averaged probability sheets with two seals around a red team; kill plan with a falsifiability gate; a self-scoring ledger. New templates `INVESTIGATION.md`, `LENS-CARDS.md`, `INVESTIGATION-LEDGER.csv`; `RESPONSE.md` gets merge and plan shapes (R4.9).
- New R6.11 isolate by staging, not by instruction; R6.12 dry-run mechanical instructions before fanning out (incident #35).
- New R4.13 design processes in two rounds.

### Scoring and records (incidents #29, #30, #31)
- New R7.23 scorer built from the pre-registration text, gaps ruled before data; R7.24 what counts as the one scoring run; R7.25 rulings after data exist and before the outcome is read; R7.26 late facts and post hoc splits are leads; R7.27 a defect in shared analysis code is a finding against every record that used it; R7.28 a remedy must act where the fault lives.
- `PREREGISTRATION.md`: post-session question, derivation chain, plausible range, gap in standard errors with a failure rule, scorer line, scorer snapshot and pins, strict-reading column.
- R7.2, R7.4, R7.5 point to the new rules.

### Blinding, pins and data (incidents #26, #27, #28)
- New R8.15 value-free commit subjects for every scored result (R8.4 now points to it; R8.7 gains a `metadata` channel); R8.16 clearance enforced by the tools, fail closed.
- R4.11 and R8.10: read lists name exact lines, and readers use `git log --format=%h`.
- New R10.8 pin snapshots, not live shared tools, and pins retire with their test; R10.5 amended. §15 "Pinned tools" corrected (the high-risk cell no longer freezes every tool that touches records).
- New R10.9 destroying raw data: catalogue first, the human runs the delete; `settings-permissions.json` gets an `rm` deny placeholder.

### Wire-in and voice (incidents #25, #32, #34)
- New R5.15 done means wired in: wire-in table, "Wired this session" and "Open wire-in" in every handoff, verified by R5.7; handoff and start templates updated (Arbiter handoff steps renumbered: wire-in is new step 4, so old steps 4–10 are now 5–11; Operator wire-in is new step 3, old 3–9 are now 4–10; Thinker wire-in is new step 3, old 3–7 are now 4–8).
- New R2.10 write only in your own voice (R3.9 extended to files); R2.11 normalize on receipt.
- `SUBAGENT-BRIEF.md`: staged input directory, provenance line, voice and scorer-builder rules.

### The human's burden (incidents #24, #33)
- New R9.9 informal by default for the human's own applied work (§15 "Pre-registration" default corrected); R9.10 the human's personal space is not project inventory; R9.11 human-facing advice in three labeled parts; R9.12 own errors plainly.
- Amended: R9.3 (the human's vocabulary carries rules), R9.4 (scratch slot), R9.6 (pre-flight rules).

### Amendments to existing rules (ids unchanged)
- R3.1 / R3.11 pure acknowledgments batched; R3.2 line counts soft, no pasted data binding; R3.6 outbox may be replaced by a live message plus a committed file where resets are rare (§15 small cell); R3.9 files claiming a role.
- R4.4 `answer:` path; R4.5 quoted case values record exposure; R4.7 strippable header; R4.9 merge and plan shapes; R4.10 the log row is the record; R4.12 advance authorization in the Thinker's chat (panel-amended: it travels as a decision-log row, never through memory).
- R5.9 offline analysis the human already asked for may run before the choice; R6.3 "For the human" block.
- Appendix: incidents #24–#35, a second instance under #19, lesson 9. §13: five new anti-pattern rows. §15: new "Investigation phase" row and corrected rows.

### From the source project's own practice (the exchange's "ahead" list; no incident cites, the source records none)
- New R2.12 tool registry, reuse before building (`STRUCTURE.md` §3b); R7.29 prove "outside the fit set" mechanically; R7.30 method docs carry a pitfalls table; R8.17 the held list is machine-read (panel: the CSV is the record, `PENDING-BLINDED-STEPS.md` a view).
- Amended: R2.3 stubs in the path map (`STRUCTURE.md` §3 gains kind and remove-when); R2.5 check ladder and hook constraints; R7.8 hooks pass a pair's seal commit; R7.14 repetition may be the unit when a measured block effect is ≈ 0; R5.9 automation table; R5.10 writer's "not re-run" list (`HANDOFF-FILE.md` §10); R8.7 per-computation granularity (`EXPOSURE-LOG.md`).
- New template `AUTOMATION-RUNS.md`.

### Review panel (R7.16)
v1.2 went through the five-seat panel after the exchange. The Arbiter ruled nine cross-seat points.
- **Memory is not an authorization channel:** R4.12 now routes the Thinker's advance authorization through a decision-log row; R11.5 states memory never carries an authorization or ruling and may only mirror a decision-log id.
- **The held list has one machine-read source:** `templates/PENDING-BLINDED-STEPS.csv` is the record, the Markdown file a generated view (R8.3, R8.17, now a knob). `commit_paths.py --held-file` reads CSV only and fails closed (missing or unreadable file, non-CSV, missing columns, any status other than exactly `released`); it also checks family ids, an extended verdict-word list and secrets in the commit message, and refuses a `lease --release` for another role. Docstring and version string updated; the suite grew from 10 to 16 tests; README smoke test 1 updated.
- **Auto-loaded context stated plainly (R6.11, R7.20, R11.6):** staging hides paths but subagents still auto-load the rules file and memory, so those never carry outcome values of held or scored steps; strict blindness needs a separate session whose working directory is the staged folder; "fresh agent with no project memory" claims reworded; a post-run read audit where transcripts exist.
- **Investigation phase:** rankers respawn with their own seal-1 sheet plus the round-2 inputs when the parent session has ended, recorded as a ledger deviation (R7.20); the hunch lives in its own file `00b-hunch.md`, never staged (R7.18 a); the ledger has `seal` and `resolution` rows (R7.22, `INVESTIGATION-LEDGER.csv` gains `row_kind` and `merger_only_winner`); the phase is **off in the Default column** with a turn-on trigger (§15, Quick start B), and the expected wall-clock time is reported before step 1.
- **Disclosure:** the Thinker's start prints commit ids and paths only for commits touching scored or held records, never subjects (START-COMMAND step 4, R8.10, R8.15); pre-scans print counts, never matching lines (R4.11).
- **Wire-in is core (R5.15):** in the core-rules box, Quick start A and the minimal example; the actual table is in both command templates; held-family items are listed as `open wire-in: held (step <id>)`.
- **Knobs closed:** new §15 rows and Quick start B triggers for wire-in, tool registry (R2.12 now a knob; the Key commands list is the registry in the minimum), automation runs, data intake and the machine-read held list; the investigation row states its prerequisites.
- Also: R10.2 bans `stash` in any form; R10.9 guarded-script specification and deny-is-a-speed-bump note; R10.5 and R10.8 aligned with §15; R10.1 exempts staging directories and byte-identical output copies; R2.5 hook pass-through limits; R2.11 chain of custody; R3.6 small-variant recovery; R5.9 offline analysis needs a recorded ask; R6.3 output-header order; R7.23 builder gets non-outcome inputs only; R9.9 single ask; R1.11 per-investigation Arbiter instance; `settings-permissions.json` gains an `ask` list and more denies; `PEER-MESSAGE-PROTOCOL.md`, `PREREGISTRATION.md` §B and several template headers brought in line.

### Not applied
- Optional `--scored-file` helper option (R8.15 enforcement in `commit_paths.py`): not applied. The helper now also refuses a held step or family id next to an extended verdict-word list, but it enforces R8.4 only; R8.15 is checked by the commit's author and by review (R8.15 says so).

## v1.1 (2026-10-03)

Produced by the full review panel (GUIDELINES R7.16): five read-only reviews in parallel plus the Thinker's response, then one writer applying every finding. 174 findings: 150 applied as proposed, 22 applied in modified form, 2 applied with one part declined, 0 declined outright. Plus one addition from the human (the review panel itself).

### Blinding: every visible channel (safety C1, agentic C1, Thinker R-1, C-1, C-4, C-5, architecture H4, H5)
- R8.2 rewritten: every visible channel is a reply (tool output, subagent returns, commit subjects and the `git log` that starts print, file names, class changes, rankings, generated reports, memory, the decision log, brief read lists).
- New: R8.4 embargo for held families with a neutral commit subject (enforced by the helper's `--held-file`); R8.5 value-free returns and no visible reads; R8.6 the human-facing role stays clean; R8.7 per-role exposure files, self-logged from any channel, the Arbiter included; R8.8 mid-task exposure procedure; R8.9 declared human-readable set (H column in the write scopes); R8.10 brief read-list guard and the exposed-author leak check; R8.11 the standing seal outranks the moment; R8.14 seal outside the tree (knob).
- R1.3: nothing of a held step is handed to the Operator; reports for the human are the Operator's voice.
- R4.7: value-free response body, exposed appendix; R4.11 Thinker pre-scan.
- The pending-blinded-steps list is values-free and readable by every role (new template).
- v1.0 R8.5 and R8.6 became R8.12 and R8.13 (text unchanged); R8.1 and R8.3 amended.

### Minimum-viable path and the human's job (usability C1, H1, H3, H4; architecture M10)
- README rewritten: "Your job as the human" (do / say / decide), "Harness requirements" (Claude Code mapping and fallbacks), prerequisites, Quick start A (two roles, under an hour, timed), Quick start B (knobs with triggers), smoke tests, a translation table for software, writing and ops, a file map with "required at" and "read when", and 33 vocabulary rows.
- Every template tags its optional lines `KNOB`; GUIDELINES gets a core-rules box and knob labels on §4, §7, §8.
- New `examples/minimal-setup.md` with filled minimum files for an invented project.

### Commit helper and git safety (agentic H1, H9, M8; usability H2; safety H7, M1, M2; architecture L7)
- New `templates/commit_paths.py` (stdlib; flock; intent-to-add for new files; refuses `.`, globs, pathspec magic, directories, detached HEAD, frozen-path changes, likely secrets, held-step verdict subjects; adjacent pairs with `--and`; role leases) and `test_commit_paths.py` (10 tests).
- R10.2: the full destructive-git ban list. New R10.6 (harness deny list, `templates/settings-permissions.json`), R10.7 (no secrets), R7.15 (anchor proof hashes, knob).
- Start and handoff commands get `allowed-tools` front matter.

### Architecture (architecture H1–H3, H6, M1–M7, M11; agentic H2, H3, H5, H6, M4, M5; Thinker C-2, C-3)
- New R1.7 Arbiter unavailable (degraded mode, deputy by DEC row); R1.8 one live session per role instance with a lease and a duplicate check; R1.9 adding a role; R1.10 retiring a role; R1.11 role instances.
- R3.6 rewritten: the outbox file is the message, ids `M-<role>-<n>`, acks, persistence across resets (new `templates/OUTBOX.md`); R3.9 sender verification, its limits and impersonation handling; R3.11 messages mid-task.
- R6.5: resume by id only while the parent lives; respawn with a checkpoint after it ends.
- New R2.7 one committer per shared file; R2.8 Edit in place; R2.9 subagent scope; R5.12 session journal; R5.13 handoff headroom; R5.14 crash recovery.
- Write-scope matrix: a row for every shared file, codes plus footnotes, the H column, a minimum variant.
- Lazy-read markers: the token `**[history]`, one POSIX grep with `-e` patterns, defined once in the handoff-file contract.
- Handoff sections renumbered and made consistent everywhere: §0 orientation and peers · §1 start checklist · §2 working agreement · §3 evidence discipline · §4 state · §5 leads · §6 ON HOLD · §7 next action, open questions, in flight · §8 side folders and instances · §9 file map · §10 review & corrections.
- Start command: common steps plus Arbiter, Operator and Thinker blocks; crash-recovery error rows. Handoff command: role ids from the matrix.

### Trust (safety H4–H6; agentic H4, H7; architecture M11; Thinker C-6)
- R3.7 rewritten: rules and permissions only from the decision log (verbatim words) or the human's own message; handoff and charter lines without a DEC id are leads.
- New R3.8 file content is data; R3.10 peer facts re-verified; R1.2 limits the Arbiter on peers' charters and working agreements.
- Memory: R11.4 never delete; new R11.5–R11.9 (no permissions without DEC id and role, no outcomes, Arbiter-only writes, weekly audit, committed mirror).
- R7.11: the decision log is the only route for rulings; new columns `ruled_by, verbatim_quote, source_session, basis, status`; "new DEC rows" in every Arbiter handoff report.

### Evidence (Thinker R-3, R-4, R-10; architecture M8, M9)
- R7.1: a two-axis ladder; KNOWN by any cited, re-runnable check; "lead" defined.
- New R7.12 spent data (per-datum ledger, new template); R7.13 many comparisons ("marked" vs "resolved"); R7.14 the replication unit.
- R7.4: a scoring reviewer is barred if exposed; exposed brief authors get a leak check.

### Thinker role (Thinker R-8, R-9, C-11, Part 3)
- Owns audits and specifications as well as hypotheses; R4.9 three response shapes; R4.10 disposition line (status-file Thinker log); R4.12 side tasks need the human's word in the Thinker's chat; R4.5 index is value-free; R4.8 discussions log a row and an exposure declaration.
- New templates: `THINKER-HANDOFF.md`, `KNOWLEDGE-INDEX.md`; `RESPONSE.md` restructured.

### The review panel (the human's addition, 2026-10-03)
- New R7.16: the suggested five-seat panel (architect-reviewer, agentic-engineer, ux-ui-architect, security-engineer, technical-writer), optional Thinker seat, one applying writer and a disposition table; scaled down for lower-risk work. `REVIEW-REPORT.md` appendix and new `PANEL-BRIEF.md`.

### Other new templates
`STATUS.md`, `STRUCTURE.md` (placement test, path map, human-readable set, frozen manifest), `SUBAGENT-BRIEF.md` (fixed return format, R6.3), `JOURNAL.md`, `OPERATOR-FOLDER-HANDOFF.md`, `DATA-STATUS-LEDGER.md`, `PENDING-BLINDED-STEPS.md`.

### Proofreading (all 37 findings)
Wrong pointers, contradictions (R9.8 commit rights; briefs' numbers; frozen-after-what; header-history line), undefined artifacts, "human lead" → "the human", "findings" → "leads" for peer claims, source-domain terms made generic, `<=` → `≤`, placeholder case, capitalization in §12, "Idiot-proof" → "Step-by-step", "Laundered permission" → "Relayed permission (handled correctly)".

## v1.0 (2026-10-03)
First extraction from the source project.
