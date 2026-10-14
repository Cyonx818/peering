# Blind report inference round: <work item> round <n>

File: `<work item folder>/<round>-README.md` | Owner: Operator | GUIDELINES R8.18, R7.39, R9.16
<!-- KNOB: blind report inference. Off in the minimum. One folder per round; the files below stay separate files:
     merging two of them is the leak R8.18 exists to prevent. Physical separation (sealed location outside the working
     tree, staging, R6.11) is the control, not a "do not read" line. This template is on with the knob even when the
     blinding knob is off (R8.18). -->

## 0. Round settings
- **Open prompt (fixed, committed here before the run):** "<one open question, e.g. 'Tell me, in your own words, what you noticed about this run.'>" No question or option names a lever, phase, place or predicted effect until the words are on file.
- **Scoring time per round:** <none | a stated time, only if a proven problem calls for it, with the incident cited (R9.1)>. Cells per round: at most <5>.
- **Order that ran:** <report first | analysis first> (R9.16).
- **Sealed location (outside the working tree):** `<$TMPDIR/<run-id>/sealed/ or the project's seal location, R8.14>`; on the analyst's read-deny list where the harness has one.

## 1. File set
| File | Holds | Written by | Where / committed | Who may read it |
|---|---|---|---|---|
| `<sealed>/<round>-words.md` | the human's words for this round, verbatim, elicited with the open prompt above | the Operator records; the human's own words | outside the tree; **only its sha256 committed** before the analyst launches (report first); the file committed after the blind cells file, hash checked | the Operator, the second stage; **never the blind analyst** |
| `<sealed>/<round>-predictions.md` | the mechanism prediction lines (what the human should perceive) and the package signatures | the Operator | outside the tree; its sha256 committed before the run (meets R9.7); the file committed after the blind cells file, hash checked | not the blind analyst; records the analyst may read only point to this file (never copy it) |
| `<round>-blind-cells.md` | at most <5> coded cells (CODEBOOK §7 row form), each with a value-free **claim line** and a **basis line** (what it leans on, with numbers) | the blind analyst (a fresh, staged subagent, R6.11) | in the tree, before the human scores | claim lines: the human and everyone after commit; **basis lines: withheld from the human until the score file is committed** |
| `<round>-score.md` | the human's own mark per cell and per prediction line (named / partly / missed / can't say), verbatim | the human marks; the Operator transcribes and does not code | after the human scores | everyone |
| shared coded-data file `<path>` | coded history of earlier rounds | the Operator | this round's words enter **only after** the score file is committed | the blind analyst, staged as of the commit before this round's intake (R6.11) |
| `<round>-coded.csv` | this round's coded words and cells (CODEBOOK §7 schema) | the coder / the analyst | with the second stage | the second stage |

## 1b. Scoring card (what the human sees)
Each cell is shown as **its claim line only**: no basis line, citation, number or ranking. All cells at once, numbered, in one message.
- **named**: I noticed this and would have said it in my own words.
- **partly**: I noticed something near it (the right thing or place, a different kind or size).
- **missed**: I did not notice this.
- **can't say**: I can't tell whether I experienced this. Excluded from the hit rate; logged in the score file with the count.

Dose: at most <5> cells, about <2> minutes (R9.1). Not needed this round: reading any number, ranking or basis line. The human's reply is copied verbatim into the score file. After the cell marks are committed, the human marks each prediction line the same way (R7.39).

## 2. Commit order
1. Predictions written to the sealed location; their sha256 committed (before any readout of the data they predict, R9.7).
2. Words elicited with the committed open prompt and written to the sealed location; their sha256 committed (before the human sees any number), **or** recorded as deferred by the human (R9.16; analysis first).
3. Staged analyst folder built by a script and listed in the output header (R6.11): the instrument data for this round **under neutral file names** (audio or chat tracks stripped or listed as excluded); the **redacted copy** of the parent review (every prediction line, signature and package expectation replaced by a pointer to `<round>-predictions.md`); the coder sheet of the codebook (CODEBOOK §1, §2, §7 only); the analyst brief from the committed value-free brief template (`templates/SUBAGENT-BRIEF.md`: at most <5> cells, one code per axis, a claim line and a basis line per cell). Not copied: the words file, the prediction file, this round's rows of the shared coded-data file. The analyst is spawned fresh, with no inherited context. **Leak check before launch:** a script greps the staged folder and the brief for every content token of the words and prediction files (each distinctive word, and every phrase of ≥ 2 words); hits = 0 (content, not file names; pointers to the file name are allowed).
4. Blind cells file committed.
5. Analysis-first order only: the words are elicited and their sha256 committed now, after step 4 and before step 6.
6. The human marks each cell from the claim lines (scoring card, §1b); the Operator records the marks verbatim; score file committed. Then the basis lines are shown.
7. Words and predictions files committed, hash checked against the earlier commits.
8. Second stage (with the words): the Operator, or a subagent it names, writes `<round>-review.md` (cells against words and numbers), after the score file is committed.
9. This round's words enter the shared coded-data file.

## 3. Audit lines (every review)
- Echo share: <k> of <n> blind cells echo the previous round's words; reverse echo: <k> of <n> coded units in this round's words echo the previous round's blind cells (R8.18 (7)).
- Elicitation: prompt used = the committed prompt (yes / deviation: <…>).
- Reads verified: only `<staged dir>`, or the deviation (R6.11).
- Hit rates, kept separate (R7.39): pre-action prediction <k of n; expected Σp0>; post-action inference <k of n; expected Σp0>; "partly" = 0.5 in k, reported with and without partly; "can't say" marks excluded: <count> (codebook: `CODEBOOK.md`).
- Leak check: content-token grep of the staged folder and the brief = 0 before launch (script and result path: <…>).
