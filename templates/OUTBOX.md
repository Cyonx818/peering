# Outbox: <role-id>

File: `peers/outbox-<role-id>.md` | Only committer: <role-id> (GUIDELINES R2.7, R3.6)

Every message that carries a `need:` is a row here **before** any live notification. Receivers read the rows addressed to them (`grep -n '| <their role-id> |' peers/outbox-*.md`, then status `open`). Rows are never deleted; only the Status cell of your own rows changes (`open` → `done <commit>` or `withdrawn <reason>`). Acks you give to other roles' messages are rows too (What = `ack M-…`, Need = `nothing pending`, Status = `done`). Mode is one of the four in `PEER-COMMS-PROTOCOL.md` §3 (R3.13); a courier row's commit is what the receiver verifies. No outcome values of a held step (R3.5); no secrets (R10.7).

| Id | Date | To | Mode | What | Pointer (commit / path) | Need | Status |
|---|---|---|---|---|---|---|---|
| M-<role-id>-1 | YYYY-MM-DD | <role-id> | free / relay / blinded / courier | <what this is> | <hash or path> | <one ask> / nothing pending | open |
