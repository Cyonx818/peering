# Lens cards and prompt skeletons

GUIDELINES R7.18, R6.11, R6.12
<!-- KNOB: investigation. Cards and prompts for the divergent-generation step. Cards carry a viewpoint, never an example:
     NO example candidates, NO mechanism families, NO famous names, NO backstory (R7.18 c). Examples anchor every generator onto the same few ideas.
     Dry-run the whole generator prompt on one agent before the fan-out (R6.12): every quota and ordering line must be satisfiable as written. -->

## Card skeleton (one file per lens)

```
Lens: <short neutral name>
Viewpoint: <one or two sentences: from where this generator looks at the facts>
Forbidden move: <one thing this lens must not do>
Prompts:
1. <question this lens asks of the fact sheet>
2. <…>
3. <…>
Structured step: <see below>
Closing prompt: <see below>
Start here: <the fact-sheet section to read first>
```

## Control card (no lens)

```
Lens: control
Viewpoint: none. Read the fact sheet and explain the observation.
Forbidden move: none beyond the common rules.
Structured step and closing prompt: as for every card.
```

## Structured step (the same for every card)
<Enumerate the fixed category list first. Give every category at least one candidate. Write at least <N, e.g. 6> candidates. Put your last two candidates in the categories that are thinnest so far. An explanation that fits no category gets a new named category.>
<!-- Check that "the last two" and "every category at least one" can both be met when the category count and N are as stated (the contradiction in appendix #35). -->

Per candidate: mechanism · category · prediction in the existing data · prediction under one named change · kill observation · the fact-sheet row it rests on. No numbers.

## Closing prompt (the same for every card)
<Assume this list misses the answer. What kind of explanation would that be? Add the best candidate of that kind, tagged `dialectical`.>

## Prompt skeletons

Each prompt: a staged directory (R6.11), "read only `<dir>`; do not read or search the repository; write `<dir>/out.md`", and the return follows R6.3. Output header order (R6.3): line 1 `Written by: subagent <id> for <role>, brief <path>` (R2.10); the staged-directory listing; `## Progress`; then any "For the human" block. Staging does not prevent the harness from auto-loading the rules file and memory index; they must carry no case content, and strict blindness needs a separate session whose working directory is the staged folder (R6.11).

| Agent | Skeleton |
|---|---|
| Clerk | Build the fact sheet from `<dir>`: tables, definitions, data used, the human's dated statements verbatim. No explanation, no plausibility comparison, no candidate cause. List what you excluded. |
| Key clerk | Write a reference list of known mechanisms for `<kind of observation>`, one line each, with no values from this case. |
| Generator | Read your card and the fact sheet. Follow the structured step and the closing prompt. |
| Merger | Cluster the candidates into <e.g. 5–8> hypotheses, each a sentence that can take a probability; apply the is / is-not test; fill the mandatory slots (can't-miss, measurement artifact, subject adaptation, reference artifact, catch-all) from the key where empty and tag them; build the evidence matrix. Produce the ranker part without author names, cluster sizes or counts. |
| Ranker | Assign the probability that each hypothesis is the main cause: every row ≥ <floor>, catch-all ≥ <catch-all floor>, sum 1. Name the evidence item whose reversal would change your top choice. For seal 2 (a resumed ranker, or a fresh one given only its own seal-1 sheet): read the red team output and the merger reply, revise, say what moved. |
| Red team | For each of the top three names, write the best account under its strongest rivals, a refutation premortem, consider-the-opposite on the key evidence item, and missed confounds. Tag new candidates `redteam-added`. |
