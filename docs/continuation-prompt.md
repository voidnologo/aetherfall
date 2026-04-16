# Continuation Prompt

## Last Session (30) — World-Building Clarifications + Story 02 First Draft

- Clarified world-building fundamentals: neutral territory as default, old-world tech is neutral, Veil produces ecosystems / Engine produces objects, gradient is physics not a place, Ashwick is connected to a broader world
- Updated fiction docs: 01-the-world, 02-the-local-scene, 04-the-characters, 06-series-bible
- Wrote complete 10-chapter first draft of Story 02 (~18k words, rotating POV, sequential)
- Story follows Ash & Veil from briefing to Wilds expedition to inaccessible artifact to combat to return

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action with `--pathprefix=/aetherfall/`
- **Website:** 18 chapters + quickstart (.njk) + character sheets (from JSON + sheet.njk) + interactive tools
- **Fiction:** 6 world reference docs in `fiction/world/`, Story 02 first draft (10 chapters) in `fiction/stories/story-02/`
- **Art pipeline:** `art/{type}/{generated|approved|archived}/` — art NEVER deleted, only moved
- **Art generation:** `python tools/comfyui_generate.py` — builds flux-dev workflows, queues via ComfyUI API
- **Founding event:** "The Tear" (was "the Eruption" — renamed session 27)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- Read and revise Story 02 — editing pass for voice, pacing, continuity
- Choose a working title for Story 02
- Update series bible with new NPCs, world state, seeds from the draft
- Review Wave 1 art and select golden reference set

## Key References
- Fiction world docs: `fiction/world/01-the-world.md` through `06-series-bible.md`
- Story 02 plan: `fiction/stories/story-02/PLAN.md`
- Story 02 chapters: `fiction/stories/story-02/ch01.md` through `ch10.md`
- Style guide: `fiction/world/05-style-guide.md`
- Character sheets (game data): `web/_data/characters/*.json`

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
