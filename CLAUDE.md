# Project Rules — Aetherfall

## Art Pipeline

- **Art is NEVER deleted.** All generated art moves through: `generated/` -> `approved/` or `generated/` -> `archived/`. Rejected art goes to `archived/`, not the trash.
- Art lives in `art/{type}/{stage}/` — e.g., `art/logo/generated/`, `art/logo/approved/`
- File naming: `{description}_v{NN}_seed-{seed}.png`

## Rulebook Content

- Rulebook content must NEVER be changed without explicit user approval.
- Always persist design decisions in `docs/requirements/` BEFORE writing rulebook content.

## Voice & Style

- Voice callouts are in-world people sharing experiences. Never rules commentary.
- Spell Complexity is never exposed in the web rulebook.

## Natural Prose

- All prose (fiction, voice callouts, rulebook text, PR descriptions) follows `docs/writing/natural-prose.md`.
- After writing or revising fiction, run the `prose-check` skill (`python3 tools/prose_lint.py --summary <files>`) and bring every rate under its limit before committing. Above all: no ", and" chains, no ", and X had done Y" codas, no ", the way X does Y" similes, no "Not X. Y." contrasts.
