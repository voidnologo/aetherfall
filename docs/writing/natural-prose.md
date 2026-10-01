# Natural Prose: Cutting the AI-isms

Everything written for Aetherfall goes through this guide: fiction, voice callouts, rulebook text, PR descriptions. The fiction style guide (`fiction/world/05-style-guide.md`) says what the prose should sound like. This one lists the habits that make it sound machine-made, and how to fix them.

The checker is `tools/prose_lint.py`. The workflow is the `prose-check` skill.

## Why these habits happen

Language models write toward the most probable next sentence, so they lean on devices that are always safe: the simile, the contrast, the list of three, the clause joined with "and". None of these is wrong, and good writers use all of them. The trouble is frequency. A model uses them in every paragraph, at the same length and in the same position, and the reader starts to hear the pattern instead of the story. Colin Gorrie puts it well: the machine has the technique but no taste, and taste is mostly knowing when *not* to use a device.

The research agrees on three points:

1. **The tells are shared across models.** Sam Paech's Antislop study compared 67 models against human text. "Flickered" turns up in 98.5% of their over-used word lists. Some phrases run a thousand times more often than in human fiction ("heart hammered ribs" 1,192×, "voice trembling slightly" 731×). Character names are part of it: "Elara" and "Kael" are among the most over-used names in model fiction.
2. **Structure gives the game away more than vocabulary does.** EQ-Bench's slop score weights contrast constructions ("not X but Y") and stock trigrams alongside words. Wikipedia's AI-cleanup editors list negative parallelisms, "-ing" tails and copula avoidance ("serves as" for "is") among the clearest signs.
3. **Rates matter, not single uses.** Freeburg measured em dashes at 9.1 per thousand words for Claude Opus 4.6 and 3.2 for a sample of published human essays. A single dash means nothing. Ten a page is a fingerprint.

So the fix is rarely a ban. It's a budget.

## Calibration

`prose_lint.py` counts per thousand words of narration. Story 01's first draft against its revision and the two earlier stories:

| Measure (per 1k words) | Story 01 draft | Story 01 revised | Story 02 | Story 03 | Limit |
|---|---|---|---|---|---|
| sentences chaining 3+ clauses with "and" | 4.2 | 0 | 0.6 | 0.6 | 1 |
| `, and` + new subject (", and he...") | 6.2 | 2.6 | 3.0 | 2.7 | 4 |
| `the way X does Y` | 1.8 | 0.4 | 1.2 | 1.9 | 1.5 |
| "Not X. Y." contrasts | 1.3 | 0.1 | 2.4 | 2.4 | 1 |
| stock beats ("for a long moment") | 3.9 | 0.6 | 1.0 | 1.6 | 2 |
| em dashes | 11.1 | 1.6 | 14.9 | 15.0 | 8 |

Stories 02 and 03 are the reference for rhythm: their sentences rarely chain. They have their own tics, though (dashes, "Not X. Y."), so don't copy them blindly.

## The tics

Grouped roughly by how much damage they do in fiction.

### 1. The "and" chain

This is the worst offender, and the one that makes a page tiring. A sentence keeps going by bolting on another clause with ", and", then another.

> He sat down on the edge of the bed with it, and turned pages, and for a minute the only sound in the room was the paper and the faint hum through the wall.

> The revolver bucked in his hand, clean and sure, the way it had on every range and every street for seven years, and the big man's shot went into the brickwork a foot from Aldric's head and threw red dust over him, and the big man spun half round, clutching his right arm above the elbow, and his gun clattered on the cobbles.

It imitates breathless storytelling, but it gives every clause the same weight. Each one is "and then", so nothing lands. **Fix:** break it into sentences. Decide which action matters and give it its own sentence. Subordinate the rest ("when", "after", "while", "as") or cut it.

> He sat on the edge of the bed and turned the pages. For a minute the only sounds were the paper and the faint hum through the wall.

Polysyndeton ("and... and... and") is a real device. Use it once a story, on purpose, when the moment should feel like a pile-up.

### 2. The pluperfect coda: ", and X had done Y"

A short main clause, then a tacked-on clause of backstory that carries the actual point.

> The charter was seven days old and the ink still smudged if you rubbed it, and Mira had rubbed it a good deal.

Once, it's charming. Repeated, it becomes a wink at the reader. **Fix:** give the backstory its own sentence. *The ink still smudged if you rubbed it. Mira had rubbed it a good deal.*

### 3. The summary sentence

The scene shows something, then a sentence explains what it showed. Humanizer calls these "one-line closers".

> Nobody bothered anybody. That was the Wet Ember's whole religion.
> It was the look of someone deciding how much a thing was worth and whether she'd get change.
> That was the part Kael would remember. Not the shot. The after.

**Fix:** trust the scene. Delete the explaining sentence and check whether anything was lost. If something was, put it into the action. Keep at most one a chapter, where it earns a laugh or a turn.

### 4. The "the way X does Y" simile

> ...her hand went in and touched it, the way your tongue goes to a new tooth.
> ...Laine looked at it the way a jeweller looks at paste.
> ...his eyes went, the way a scholar's eyes go, straight to the place he was most interested in.

Each is fine on its own. Story 01's draft had twenty-one. The construction always sits in the same place, after a comma at the end of the sentence, and it always generalises ("the way a man frowns at a watch"). **Fix:** keep the best one or two a chapter. Cut the rest, or make them specific to this character and this moment.

Don't just swap "the way" for "like" or "as if". That moves the tic rather than removing it; the linter counts all three. Never put two similes in one sentence.

### 5. Negative parallelism: "Not X. Y."

> Not grey like a colour. Grey like a uniform.
> Not the shot. The after.
> "You're Syndicate," she said. Not a question.

It sets up a straw idea in order to knock it down. Every source above names it. Humanizer files it with a cousin, "arguing with no one": rejecting an idea nobody raised. **Fix:** state the true thing. *It was a Greycoat's grey: long and belted, a brass badge at the collar.* "Not a question" after a line with no question mark is redundant, so cut it. Keep a contrast only when it corrects something a character actually believes.

### 6. Lists of three and fragment runs

> Late afternoon. The fire was lit, the lamps were gas...
> Long, belted, the brass badge pinned at the collar, the hem dark with wet.
> Pre-Tear. Solid, sensible, municipal.

Three adjectives, three fragments, three beats. The rhythm turns into a drum. **Fix:** vary the count (one, two, four). Let a fragment stand alone or not at all. Three fragments in a row is a flag.

### 7. Echo openings

> She looked round the room once... She sat down without being asked. She put a thin card folder on the table...
> He watched her go... He watched the big one's shoulders... He watched the small one laugh...

Anaphora used once is emphasis. Used by default it reads like a list. **Fix:** combine, reorder, or open with the object or the time. Be careful when you fix one tic: rewriting an and-chain as "She left out X. She left out Y. She left out Z." swaps one pattern for another.

### 8. Dialogue tags with adverbs, and stock beats

"Said quietly", "said gently", "said simply", "said mildly". Silence that "sits" or "stretches". "For a long moment." "Nobody said anything for a moment." "Something at the corner of her mouth moved." "Very still." "At last." "As if he had all the time in the world." The Antislop list adds the generic ones: "voice barely above a whisper", "took a deep breath", "couldn't help but", "the air was thick with", "a shiver ran down her spine", "eyes never leaving".

These are filler. They pad a beat the dialogue should carry. **Fix:** use "said" or no tag, and let the line carry the tone. If the pause matters, show what fills it (someone drinks, a cart goes by), or cut to the next line.

### 9. Smaller habits

- **Doublets.** "went very still, and very young." Fine once; after that it's a mannerism.
- **Trailing participles.** ", sending sparks across the floor", ", leaving him breathless". Make it a sentence or cut it.
- **Signposted foreshadowing.** "He'd remember, much later." "He didn't know that yet." Once a story at most.
- **Hedges.** "Somehow", "something like", "a kind of". They avoid saying the thing.
- **Even rhythm.** Detection tools measure "burstiness": human sentence lengths vary widely, model sentences cluster. Don't fix an and-chain habit by making every sentence eight words long. Mix lengths on purpose.
- **Vocabulary.** Mostly a non-fiction problem: delve, tapestry, testament, pivotal, intricate, underscore, foster, vibrant, nestled, realm, "serves as" for "is". In fiction, watch the Antislop words in clusters: flickered, shimmered, gaze, etched, unease, faint, glow.

### 10. Non-fiction (PR descriptions, docs, rulebook)

The humanizer skill's list covers this well. The main ones: announcing the point before making it ("Here's what you need to know"), inflated significance ("a pivotal addition"), bold labels on every bullet, headings repeated in the first sentence, writing about the document instead of its subject ("this section covers"), chat residue ("I hope this helps"), and stacked hedges ("could potentially").

## What to do instead

Suppressing tics isn't enough; give each sentence a job.

1. **One idea per sentence.** If two "and"s join clauses, it probably holds two ideas. Split it.
2. **Vary length on purpose.** A long sentence, then a short one. A run of short ones in action.
3. **Specific over general.** Not "the way men say the names of foremen they're afraid of", but what this man does when he says this name.
4. **Cut the explanation.** After every striking image, check whether the next sentence explains it. If it does, delete the explanation.
5. **Let dialogue work.** People interrupt, answer the wrong question, trail off. Tags are "said" or nothing.
6. **Read it aloud.** Every tic in this list can be heard. If you run out of breath, or hear the same tune twice in a paragraph, rewrite.

## Process

1. Draft.
2. Run `python3 tools/prose_lint.py --summary <files>`. Any `OVER` line needs a pass.
3. Run it without `--summary` and work through the hits. A hit is a prompt to look, not an order. Keep the ones that earn their place, but bring every rate under its limit.
4. Audit the rewrite. Run the linter again and re-read for tics that moved rather than vanished ("the way" turned into "like"; an and-chain turned into an echo run).
5. Re-read a whole chapter for rhythm. The script can't hear monotony across paragraphs.
6. Never change plot, facts, the meaning of dialogue, or continuity details while cleaning. This is a line edit.

## Sources

- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup): negative parallelisms, copula avoidance, AI vocabulary, em-dash overuse, trailing "-ing" analysis.
- Paech et al., [Antislop: a framework for identifying and eliminating repetitive patterns in language models](https://arxiv.org/abs/2510.15061) (ICLR 2026), and the [antislop-sampler](https://github.com/sam-paech/antislop-sampler) phrase and word lists (Apache-2.0, vendored in `tools/data/antislop.json`).
- E. M. Freeburg, [The Last Fingerprint: how markdown training shapes LLM prose](https://arxiv.org/abs/2603.27006) (2026): em-dash rates by model against a human baseline.
- [EQ-Bench](https://eqbench.com/about.html) slop score: word frequency, contrast constructions and slop trigrams.
- Colin Gorrie, [Why ChatGPT writes like that](https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai): parallelism, antithesis and tricolon used without taste.
- [blader/humanizer](https://github.com/blader/humanizer) (MIT), a Claude skill built on the Wikipedia list: 26 patterns and a mark → rewrite → audit → final workflow. Our skill borrows the audit step and the non-fiction patterns.
- NousResearch, [autonovel ANTI-SLOP.md](https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md): tiered word lists, structural red flags, burstiness.
- Entangled Text, [How to use negative prompts to purge AI prose tics](https://www.entangledtext.com/guides/negative-prompts-purge-ai-prose-tics): phantom sensations, atmospheric filler, echo openings; redirect rather than only ban.
