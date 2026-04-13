# Continuation Prompt

## Last Session (23) — Economy & Resource System Design
- Designed complete narrative-first economy: Station (0–5), Ledger (Flush/Level/Lean/Dire), Backing (1–5), Cost Tiers, the Drift
- Full design doc with 10-system research survey: `docs/requirements/ECONOMY.md`
- Built "Coin & Commerce" web chapter (Chapter 12) with all tables, voice callouts, GM guidance
- Added Cost Tier column to all weapon/armor tables in equipment chapter
- Centralized chapter numbers and prev/next nav in PAGES registry — single-table update for chapter changes
- Confirmed: no enchanted firearms (violates Aetheric/Galvanic split), starting gear = pick within Station

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Website live:** 19-chapter rulebook (incl. Economy + Quickstart) + Character Sheet page with builder, blank sheet, and sample
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary. Use "the tavern test" (WRITING_STYLE.md). GM notes handle rules perspective.
- **CRITICAL INTERNAL:** Spell Complexity is essential in design docs but NEVER exposed in the web rulebook.
- **Navigation:** Chapter numbers, header text, and prev/next links are driven by PAGES array in `web/rules/js/main.js`. Update one table to reorder/insert chapters.
- **Chapter flow:** Welcome → State of the World → Adventuring Societies → Creating → Character Sheet → Rolling → Getting Hurt → Skills → Magic → Grimoire → World Between → Combat → **Coin & Commerce** → Arms & Equipment → Artifacts & Enchantments → Running the Game → Quick Reference → Table Index → GM Tools → The Ashwick Job (QS)
- **Not yet designed:** Zone formation mechanics, Push Timing, archetypes, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
Discuss whether the web rulebook warrants a framework/build system (user-initiated). Then: review economy chapter in browser, add Station/Backing/Ledger to character sheets.

## Key References
- `docs/requirements/ECONOMY.md` — Full economy design doc with research and system
- `web/rules/economy.html` — "Coin & Commerce" web chapter
- `web/rules/js/main.js` — PAGES registry (single source of truth for chapter order/numbers)
- `docs/requirements/MAGIC_SYSTEM.md` §3.4 — Backlash, Wild Effect table, residue escalation
- `docs/requirements/WRITING_STYLE.md` — Voice conventions, voice vs GM note distinction
- `docs/sessions/session-23-notes.md` — Full record of session 23
