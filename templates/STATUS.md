# Status: <PROJECT>

File: `<status path>` | Only committer: Arbiter (others propose via outbox) | In the human-readable set (R8.9)
<!-- KNOB: status file. Each cell: the current text first; the previous text below a **[history]** lead-in.
     Starts read only rows State / Commit / Next action, cut at the first **[history]**.
     During a held step: no result, direction or ranking change of that step here (R8.4). -->

## Current

| Row | Value |
|---|---|
| State | <one paragraph: what we now know; held families shown as `held (step <id>)`> |
| Commit | <hash of the last handoff commit> |
| Next action | <per role: arbiter: …; operator: …; thinker: …> |

**[history] State, <date>.** <…>

## Automation runs <!-- KNOB: automation; or the standalone `AUTOMATION-RUNS.md` -->
| Job | Last run (date, commit) | Input since | Cost class |
|---|---|---|---|

## Thinker log <!-- KNOB: Thinker -->
One row per brief sent, per free-form discussion (≤ 5 lines, R4.8), and a disposition when the Arbiter acts on a response (R4.10).

| Date | Brief / discussion | Response | Exposure (pointer to row) | Disposition (adopted / overridden: reason / open; per item if mixed) |
|---|---|---|---|---|
