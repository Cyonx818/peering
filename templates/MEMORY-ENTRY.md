---
name: <short-kebab-name>
description: <one line, ≤ 150 characters; this is what the index shows>
type: user | feedback | reference
---
<!--
GUIDELINES §11. type: user = who the human is and how they work; feedback = a behavior rule; reference = a
pointer to the committed file that holds a fact (never the fact itself). No "project" type: project state
lives in handoff files and records.
Only the Arbiter writes memory; other roles propose entries through their outbox, quoting the human (R11.7).
Never: an outcome value, verdict or direction of any step (R11.6); a secret, credential or personal detail
beyond what the rule needs (R10.7).
-->

<The rule in one or two sentences. Quote the human's words with the date when the rule came from them.>

**Why:** <the incident or reasoning that produced it, with date and a pointer (commit, record). What went wrong or what it cost.>

**How to apply:** <concrete triggers and actions: "before every X, do Y"; "never Z"; what to record and where; when to ask the human instead.>

**Applies to role(s):** <all / role ids>

**Decision:** <DEC-id if this entry grants a permission, widens a scope or relaxes a rule (required, else the entry is void, R11.5); otherwise "none">

**Supersedes / updated:** <date and what changed, or "none">. If this entry no longer applies: `SUPERSEDED <date> → <entry>`; never delete (R11.4).

Related: [[<other-entry>]], [[<other-entry>]]

<!--
Index line for the memory index (one line per entry; keep the index well under ~200 lines):
- [<Title>](<file>.md) — <≤ 150-character summary>
-->
