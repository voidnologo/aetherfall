# Deco Art Suite — Plan (Session 35)

*Status: **approved plan** (user, Session 35, 2026-09-26). Nothing generated yet; Wave 1 is next.*

**Decisions:** Wave 1 = ornament kit + two spots · chapter vignettes skipped for now · drop caps are a generated tile with the letter typeset on top · Tier 2 spot list approved as drafted.

The house style is Direction D, Deco Lithograph (`style-guide.md`). Already approved and wired in: four lead portraits, four theme frames (web crowns + PDF openers), the Two Inks front-matter frame, and the sheet watermark. This plan covers everything else the book needs, in the order it pays off.

---

## 1. What we learned this session (applies to every piece)

1. **Generate cut-outs on a flat bone field, with margin.** Flux fills the canvas edge to edge unless told otherwise, and a rectangular crop then flattens the points (the crown problem). Every ornament and spot prompt asks for *"a single isolated motif on a plain flat bone paper background, generous empty margin on all sides, nothing touching the edges."* Then a cut-out step (generalising `tools/crown_alpha.py`) keys the bone to alpha.
2. **Outpainting a finished piece doesn't work** with flux1-dev (it paints new scenery around the frame). Get the composition right at generation time instead.
3. **No lettering in art.** Flux can't spell. Drop caps are an ornamental tile with the letter set in type on top, not a generated letter.
4. **Palette discipline.** Cyan is only the Aether and amber is only the Engine. Ornaments come in three colourways: Aether (cyan + midnight), Engine (amber + soot), neutral (oxblood + midnight on bone).
5. **Two backgrounds.** Every cut-out must read on the midnight web page *and* on bone paper in the PDF. Check both before approval.

---

## 2. The suite

### Tier 1 — Ornament kit (small, modular, used on every page)

| # | Piece | Count | Where it goes | Gen size |
|---|---|---|---|---|
| O1 | **Section divider**: a horizontal Deco rule with a centre medallion | 3 (Aether / Engine / neutral) | Replaces the CSS `.divider` gem and `<hr class="section-divider">`; picks the chapter's theme | 1664×320 → trim |
| O2 | **Drop-cap tile**: a square Deco cartouche with an empty centre; the letter is set in Playfair on top | 3 (per theme) | First paragraph of each chapter (the `.flavor` paragraph) | 1024×1024 |
| O3 | **Corner ornament** (one corner, mirrored by CSS) | 2 (Nouveau / Deco) | Handler callouts (32 of them) and stat blocks | 1024×1024 |
| O4 | **Tailpiece**: a small end-of-chapter mark | 1 (split motif) | End of each chapter; PDF chapter ends | 1024×1024 |
| O5 | **School sigils**: six round medallions, one per school | 6 | Grimoire and Magic school headings, spell tables | 1024×1024 each |
| O6 | **Zone badges**: Galvanic / Aetheric / neutral | 3 | Location blocks and zone tables (quickstart, World Between) | 1024×1024 |

The six schools: Aetheric Manipulation, Vivimancy, Warding, Divination, Transmutation, Ley Weaving.

### Tier 2 — Spot illustrations (2–4 in wide, irregular edges, cut out)

One or two per chapter to start (~24), each a single clear idea. Recurring figures are the four leads, described in the prompt, never named.

| Ch | Chapter | Spot subject(s) | Ink |
|---|---|---|---|
| 01 | Welcome | Game table by lamplight: two ten-sided dice, a revolver, an open spell notebook | split |
| 02 | State of the World | **The Tear**: a cyan crack splitting the sky over a Deco skyline · an ivy-eaten tram in the Reclaimed Wild | Aether · split |
| 03 | Societies | A charter document with a wax seal, a key, and a stack of marks on a patron's desk | neutral |
| 04 | Creating | An adventurer's kit laid out: coat, holster, notebook, charm, boots | neutral |
| 05 | Rolling | Two percentile dice mid-tumble, casting hard shadows | neutral |
| 06 | Getting Hurt | A figure binding a wounded forearm under a single lamp | neutral |
| 07 | Skills | Lockpicks in a keyhole · a magnifier over a map · a handshake across a card table | neutral |
| 08 | Magic | Scholarly casting: chalk geometry on a floor, cyan light rising · Wild casting: ivy and cyan flare erupting from an open hand | Aether |
| 09 | Grimoire | (school sigils, O5) | Aether |
| 10 | World Between | One street running from arc-lit factory to crystal-grown ruin: the number line as a place | split |
| 11 | Combat | A revolver misfiring in an alley, amber sparks · a knife and a pocket watch on a crate (the timing track) | Engine |
| 12 | Coin & Commerce | Marks (coins and notes) on a pawnbroker's counter | neutral |
| 13 | Arms & Equipment | Equipment study sheet: revolver, hunting knife, galvanic arc-pistol · a motorcar and a small airship | Engine |
| 14 | Artifacts | A pocket watch leaking cyan light · a ward charm nailed above a doorframe · potion bottles | Aether |
| 15 | Running the Game | A rooftop chase silhouette against arc lamps | split |
| QS | The Ashwick Job | The decommissioned foundry at night · the smuggling tunnels | Engine · Aether |

### Tier 3 — Chapter vignettes (deferred)

A wide location scene per chapter (the "header band", 1664×448). **Skipped for now** (user, Session 35): the web crowns already head each chapter, so the effort goes into spots. Revisit as either a scene inside the PDF opener frames or a band under the web crown.

### Tier 4 — Plates (later)

Full-page narrative scenes (832×1216 → 300 DPI upscale). Candidates: the four leads together in the Wet Ember; the Tear, 50 years ago; a Wild Zone swallowing a rail yard. Hold until Tiers 1–2 prove the pipeline.

---

## 3. Pipeline changes needed

1. **`tools/deco_suite.py`**: a subject list like `prototype_styles.py` (D2 prefix/suffix), with the "isolated on bone, margin" clause built into every ornament and spot prompt. It supports `--queue-only` / `--collect` (the ComfyUI memory rule) and writes to `art/{decorative,spots}/generated/`.
2. **`tools/cutout.py`**: generalises `crown_alpha.py`: flood from all four edges through bone, then clean up, trim, and export a WEBP with alpha for the web plus a PNG master.
3. **Web wiring**: `.divider` and `.section-divider` use O1 by theme; `.flavor::first-letter` gets the O2 tile; handler and stat-block corners get O3; a `{% spot "file", "caption" %}` shortcode floats a spot left or right (full width on phones).
4. **PDF wiring**: the same classes in `print.css`; spots need 300 DPI masters, so **upscaling** (the pending RealESRGAN task) comes before PDF use.

---

## 4. Waves

| Wave | Contents | Why first |
|---|---|---|
| **1: Kit proof** | O1 ×3, O2 ×3, O4, plus two spots (The Tear; the misfire) | Proves the bone-field cut-out on both backgrounds; dividers and drop caps show on every page |
| **2: Core spots** | Remaining Tier 2 for chapters 01–11 + O5 school sigils | The chapters players read first |
| **3: Finish** | Chapters 12–QS spots, O3 corners, O6 badges, upscale everything for print | Completes the book |
| **4: Big pieces** | Plates (vignettes if revived) | Most expensive, least modular |

Each wave: generate 3 seeds per piece → comparison page → user approves → cut-out → wire in → PR.
