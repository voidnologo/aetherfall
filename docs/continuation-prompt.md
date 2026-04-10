# Continuation Prompt

## Last Session (22) — Wild Effect Table, Landing Page, Starter Adventure
- Added full Wild Effect table (10 effects x 3 tiers) with residue escalation model to magic.html
- Backlash now triggers on every cast (success or misfire), cancellation is burn-only
- Landing page tagline: "When the Aether Fell, Everything Changed." Removed "1920s Steampunk" label.
- Built complete starter adventure "The Ashwick Job" — Shadowrun-style module with read-aloud blocks, decision branches, NPC stats, three-zone arc (neutral → Galvanic → Aetheric)
- 4 printable pre-gen character sheets (individual files): Kael, Sera, Aldric, Mira — full skill builds

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Website live:** 17-chapter rulebook + Quickstart adventure + Character Sheet page with builder, blank sheet, and sample
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary. Use "the tavern test" (WRITING_STYLE.md). GM notes handle rules perspective.
- **CRITICAL INTERNAL:** Spell Complexity is essential in design docs but NEVER exposed in the web rulebook. Players see EP costs and casting times only.
- **Complete (first pass):** Core mechanics, skills, progression/XP, magic system + spell learning, spell compendium (38 spells), weapons, armor/soak, Galvanic oddities, vehicles, GM chapter, world design & factions, Adventuring Societies, voice sidebars, Zone Tracker, Combat Tracker, Character Sheet (blank + sample + interactive builder), Quick Reference with flowcharts, README, artifacts & enchantments, mid-campaign spell learning, Wild Effect table with residue escalation, **starter adventure "The Ashwick Job" with 4 pre-gen characters**
- **Chapter flow:** Welcome → State of the World → Adventuring Societies → Creating → Character Sheet → Rolling → Getting Hurt → Skills → Magic → Grimoire → World Between → Combat → Equipment → Artifacts & Enchantments → Running the Game → Quick Reference → Table Index → GM Tools → **The Ashwick Job (QS)**
- **Not yet designed:** Zone formation mechanics, Push Timing, archetypes, currency, bestiary, NPC stat blocks, corruption/madness, enchanted firearms

## Immediate Next Task
Review starter adventure and character sheets after rendering/printing. Character sheet art/watermarks. Visual polish pass.

## Key References
- `docs/requirements/STARTER_ADVENTURE.md` — Full starter adventure design doc
- `web/rules/quickstart.html` — "The Ashwick Job" web page
- `web/rules/tools/quickstart-{kael,sera,aldric,mira}.html` — Printable pre-gen character sheets
- `docs/requirements/MAGIC_SYSTEM.md` §3.4 — Backlash, Wild Effect table, residue escalation
- `docs/requirements/WRITING_STYLE.md` — Voice conventions, voice vs GM note distinction
- `docs/sessions/session-22-notes.md` — Full record of session 22
