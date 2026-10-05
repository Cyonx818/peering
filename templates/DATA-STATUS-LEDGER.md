# Per-datum status ledger

File: `<path>` | Only committer: Arbiter | GUIDELINES R7.3, R7.12
<!-- KNOB: pre-registration. Mandatory wherever pre-registration is on. Not in the human-readable set.
     It records which data has already printed a family's outcome (spent), never the outcome itself. -->

Status per datum × family: **clean** (no analysis has printed this family's outcome from it) · **adjacent** (an analysis of a neighboring family touched it; state which) · **exposed** (an analysis printed this family's outcome from it: spent for confirming this family) · **scored** (used by a pre-registration's scorer). A pre-registration may be confirmed only by data that is clean for its family (§B "Data status").

| Datum (file / capture, sha256 prefix) | Family | Status | Since (date, record @ commit) | By (actor) |
|---|---|---|---|---|
