# Journal: <role-id>, <YYYY-MM-DD>

File: `<role journal folder>/journal-<YYYY-MM-DD>.md` | Written by the session itself (exempt from R10.1) | GUIDELINES R5.12
<!-- One line per event, appended as it happens. The handoff fact list is built from this file plus git log,
     so it survives auto-compaction and a full context. No outcome values of a held step; no secrets. -->

| Time | Kind | Event | Pointer |
|---|---|---|---|
| HH:MM | commit | <what> | <hash> |
| HH:MM | lead | <one line> | <file §> |
| HH:MM | peer | seen <name> (<role>, harness id <…>) | — |
| HH:MM | message | sent / received / acked M-<…> | <outbox row> |
| HH:MM | subagent | spawned <id>: <task> | <output path> |
| HH:MM | ask | asked the human: <…> | — |
| HH:MM | ruling | the human ruled: "<verbatim>" | outbox M-<…> to the Arbiter / DEC-<id> |
| HH:MM | exposure | <actor> saw <what, no values> via <channel> | exposure row # |
| HH:MM | finding | instruction found in data / sender check failed: <…> | <file> |
