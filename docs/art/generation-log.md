# Art Generation Log

## Session 25 — Logo & Brand Art (2026-04-13)

### 1. Wordmark Logo (Direction A: Split Wordmark)

| Field | Value |
|-------|-------|
| Piece name | Aetherfall Wordmark v01 |
| Art type | Logo / Wordmark |
| Model | flux1-dev (UNETLoader, fp8_e4m3fn) |
| CLIP | clip_l + t5xxl_fp16 (DualCLIPLoader, flux) |
| VAE | ae.safetensors |
| LoRA stack | None |
| Seed | 2126680450 |
| CFG | 3.5 |
| Steps | 25 |
| Sampler | euler / normal |
| Resolution | 1024 x 512 |
| File path | art/logo/generated/wordmark_v01_seed-2126680450.png |
| Accepted? | Pending review |

**Prompt:**
```
Art Deco logotype design. Elegant typographic wordmark with 1920s industrial and arcane influences. Clean vector-quality rendering suitable for logo use. Dual-tone color scheme: cyan (#3dc8e0) and amber (#e8a825) on dark background (#080b14).

The word "AETHERFALL" rendered as an Art Deco wordmark. Strong geometric letterforms inspired by Playfair Display serif typography. Visual split between cool cyan left side and warm amber right side, the transition occurring mid-word where the two forces meet. The lettering conveys tension between organic flowing energy and angular industrial precision. Subtle Art Deco sunburst motifs as restrained accents.

Horizontal layout, dark background (#080b14). The word is the primary element. Any decorative elements are subordinate to readability. Must work at small scale. Clean, sharp, professional logotype. Not an illustration — a wordmark. Minimal ornamentation. The tension between the two visual languages IS the design.
```

---

### 2. Monogram Icon (Direction B)

| Field | Value |
|-------|-------|
| Piece name | Aetherfall Monogram "A" v01 |
| Art type | Logo / Icon |
| Model | flux1-dev (UNETLoader, fp8_e4m3fn) |
| CLIP | clip_l + t5xxl_fp16 (DualCLIPLoader, flux) |
| VAE | ae.safetensors |
| LoRA stack | None |
| Seed | 788033284 |
| CFG | 3.5 |
| Steps | 25 |
| Sampler | euler / normal |
| Resolution | 768 x 768 |
| File path | art/logo/generated/monogram_v01_seed-788033284.png |
| Accepted? | Pending review |

**Prompt:**
```
Art Deco logotype design. Elegant typographic wordmark with 1920s industrial and arcane influences. Clean vector-quality rendering suitable for logo use. Dual-tone color scheme: cyan (#3dc8e0) and amber (#e8a825) on dark background (#080b14).

A stylized letter "A" monogram for the game "Aetherfall." The letterform is split or blended between two visual languages: one side organic and flowing representing magical Aether rendered in cyan #3dc8e0, the other side geometric and angular representing industrial technology rendered in amber #e8a825.

Square composition, centered. Works as a favicon at 32px and an app icon at 512px. Simple enough to read at small scale, detailed enough to reward inspection at large scale. Dark background (#080b14). Minimal — this is an icon, not an illustration. Clean edges, strong contrast, geometric precision.
```

---

### 3. Hero / Cover Image

| Field | Value |
|-------|-------|
| Piece name | Aetherfall Hero Cover v01 |
| Art type | Hero illustration / Book cover |
| Model | flux1-dev (UNETLoader, fp8_e4m3fn) |
| CLIP | clip_l + t5xxl_fp16 (DualCLIPLoader, flux) |
| VAE | ae.safetensors |
| LoRA stack | None |
| Seed | 3282193863 |
| CFG | 3.5 |
| Steps | 30 |
| Sampler | euler / normal |
| Resolution | 832 x 1216 |
| File path | art/hero/generated/hero_cover_v01_seed-3282193863.png |
| Accepted? | Pending review |

**Prompt:**
```
Art Deco logotype design with detailed illustration. Elegant typographic wordmark "AETHERFALL" with 1920s industrial and arcane influences. Dual-tone color scheme: cyan (#3dc8e0) and amber (#e8a825) on dark background (#080b14).

The word "AETHERFALL" rendered as an Art Deco wordmark at the top, with strong geometric letterforms. Below the title, a dramatic scene: a 1920s city skyline with Art Deco towers, split between two worlds — one side bathed in cool cyan magical energy with flowing Art Nouveau organic forms, ethereal particles, and arcane geometry dissolving into the air; the other side warm amber industrial light with geometric precision, factory smokestacks, and galvanic arc energy. Where the two sides meet in the center, reality fractures — the Aether falling like luminous rain through cracks in the sky.

Detailed illustration quality. Rich atmospheric depth. Suitable for a book cover or landing page hero image. The composition is grand and evocative — awe-inspiring, mysterious, and beautiful. The city below is tiny against the cosmic scale of the falling Aether above. Dark background (#080b14). Professional, polished, cinematic composition.
```

---

### 4. Embossed / Foil Stamp "A"

| Field | Value |
|-------|-------|
| Piece name | Aetherfall Emboss "A" v01 |
| Art type | Emboss / Foil stamp illustration |
| Model | flux1-dev (UNETLoader, fp8_e4m3fn) |
| CLIP | clip_l + t5xxl_fp16 (DualCLIPLoader, flux) |
| VAE | ae.safetensors |
| LoRA stack | None |
| Seed | 3077436582 |
| CFG | 3.5 |
| Steps | 30 |
| Sampler | euler / normal |
| Resolution | 1024 x 1024 |
| File path | art/emboss/generated/emboss_A_v01_seed-3077436582.png |
| Accepted? | Pending review |

**Prompt:**
```
A beautifully illustrated capital letter "A" designed as a book cover emboss or foil stamp. Art Deco and Art Nouveau fusion. The letterform is ornate and detailed — one side flows with organic magical energy in sinuous Art Nouveau curves (representing Aether), the other side is precise geometric Art Deco industrial design (representing Galvanic technology). The two halves meet at the apex of the letter in perfect tension.

Intricate decorative detail within and around the letter: fine crosshatching, stippling, flowing vine-like energy trails on the Aether side, geometric sunburst patterns and mechanical precision on the Galvanic side. The overall shape is contained and stamp-like — suitable for blind embossing or gold foil application on a leather book cover.

Rendered in high contrast monochrome — pure black on white background. Detailed pen and ink illustration quality with the ornamental precision of Aubrey Beardsley. The letter fills most of the frame. Square composition, centered. Every detail rewards close inspection. Traditional illustration technique, hand-drawn quality with steel nib dip pen.
```

---

## Session 34 — Style Direction Prototypes, Round 1 (2026-09-26)

Runner: `tools/prototype_styles.py`. Full per-image parameters and prompts are in `docs/art/prototype-runs.jsonl`.
Model flux1-dev fp8, 30 steps, guidance 3.5, euler/normal. Shared seeds per subject across directions.

| Direction | LoRAs | Notes |
|---|---|---|
| A — Engraver's Folio | engraving 0.7 + crosshatch 0.5 | Clean line, strong frames; duality weak in scenes (no crystals, lamps read as gas) |
| B — Two Inks | engraving 0.45 | Best-looking frames; colour discipline ~50% (amber magic in one spot, red brick/yellow sky leaks) |
| D — Deco Lithograph | none | Strongest immediate read; printed "KAEL DUNN" title on one portrait |

Subjects: header (1664×448), frame (832×1216), spot (1024²), portrait (832×1216). Two seeds each, plus one B spot test (seed 424242). 25 images total, all in `art/*/generated/proto-*`.

**Cross-direction issues:** Kael came out white in all six portraits despite "brown skin" (Flux bias; round 2 needs a stronger prompt and reference conditioning). Revolver misfire ignored in spots. Fake signatures in A and B.

**Status:** all pending review. Comparison page: https://claude.ai/artifact/KLMQwvngArrLWZpTzRGHhL

## Session 34 — Round 2, Direction D locked (2026-09-26)

Direction D2 (Deco Lithograph, six-ink palette, cyan = Aether, amber = Engine). 18 images: 4 lead portraits, 4 chapter-theme frames (aether/galvanic/split/neutral), sheet watermark, 2 seeds each, all `*_v02_*`. Per-image parameters are in `docs/art/prototype-runs.jsonl`. Queued with `--queue-only` and collected with `--collect`; the local wait loop was reaped for low RAM (ComfyUI holds about 19 GB), but ComfyUI finished unaffected.

**Findings:** strong series consistency across all four leads. Neutral and galvanic frames are near book-ready. One aether frame broke the colour rule (amber ivy). Both watermark emblems are usable (the crystal-fan seed reads best small). Tiny signature marks appear in corners and need cropping.

**Status:** pending user review. Page: https://claude.ai/artifact/KLMQwvngArrLWZpTzRGHhL

**Kept for later (user, Session 34):** `art/decorative/approved/proto-B-twoinks_frame_v01_seed-3867070072.png`, a round 1 Two Inks frame. Approved to keep; no use assigned yet. Candidates: fiction reader openers, PDF front matter.

**Mira approved (Session 34):** `mira_v02_seed-2096254533` (arms crossed under the lamp) and `mira_v02_seed-4036712205` (alley with satchel). Seeds 2370993926 and 2712825416 archived. All four leads now have approved portraits.

**Mira reference (Session 35):** `mira_v02_seed-2096254533` is the reference image for Mira (web portrait, sheets, future conditioning). 4036712205 stays approved as an alternate.

**Portraits wired in (Session 35):** web copies at `web/assets/art/portraits/{kael,sera,aldric,mira}.webp` (full 832×1216, WebP q86). Used on the quickstart pregen cards and in the Notes box on page 2 of each pregen sheet.

**Crown alpha (Session 35):** the web chapter crowns had been trimmed with a rectangular crop inside the frames' faint bone margin, which cut the ivy, the aether apex, and the compass point flat. `tools/crown_alpha.py` now builds each `web/assets/art/frames/{theme}-crown.webp` from the top 430 rows of the approved frame, clearing the bone margin to alpha (edge flood, limited to a 48 px band), so anything drawn over the margin keeps its full shape. Galvanic's rays still meet the top edge (there's no margin there to clear).

**Outpaint attempt, archived (Session 35):** `crown-outpaint_aether_v01_seed-3241878809` tried extending the canvas with Flux inpainting; the model painted new scenery around the bordered frame instead of finishing it. Archived; the approach was dropped along with its script. The other seven queued seeds were cancelled.

**Deco Wave 1 picks (Session 35):**
- divider_aether: approved `deco-divider_aether_v01_seed-3242900390.png`
- divider_engine: approved `deco-divider_engine_v01_seed-1937266984.png`
- divider_neutral: approved `deco-divider_neutral_v01_seed-1446613470.png`
- dropcap_aether: approved `deco-dropcap_aether_v01_seed-410393452.png`
- dropcap_engine: approved `deco-dropcap_engine_v01_seed-3802097061.png`
- dropcap_neutral: approved `deco-dropcap_neutral_v01_seed-668249163.png`
- tailpiece: approved `deco-tailpiece_v01_seed-4223877310.png`
- spot_tear: `deco-spot_tear_v01_seed-393502412.png` kept in generated/ as the fallback while v02 rerolls
- spot_misfire: `deco-spot_misfire_v01_seed-3558449554.png` kept in generated/ as the fallback while v02 rerolls
- Everything else from v01 archived. divider-neutral web copy recoloured navy → bone (web only).
- Web copies: `web/assets/art/ornaments/{divider,dropcap}-{aether,galvanic,neutral}.webp` and `tailpiece.webp` (tailpiece cut with `--main-only` to drop faint corner marks). Wired in via `[data-theme]` CSS: section dividers, the chapter-opening drop cap, and the end-of-chapter tailpiece. Split-theme chapters use the neutral set. PDF wiring waits for the print upscale.
- Spot rerolls queued as v02 (4 seeds each) with revised prompts in `tools/deco_suite.py`.

**Deco Wave 1 spots (Session 35, round 2):**
- spot_tear: approved `deco-spot_tear_v02_seed-3148179434.png` (8a, in use) and `deco-spot_tear_v02_seed-4156132992.png` (8d, alternate). The user offered either; 8a was used for its bolder tear and near-pure Aether palette.
- spot_misfire: approved `deco-spot_misfire_v02_seed-4031614979.png` (9c).
- All other v01/v02 spot renders archived, including the v01 fallbacks.
- Web copies `web/assets/art/spots/{tear,misfire}.webp`, cut with `--hull` (keeps the round vignette whole; 8a's pale crack reached the top edge and would otherwise have been keyed out) and, for the Tear, `--light-to-cyan` (Flux painted the crack bone-white; the palette says Aether light is cyan).
- Placed with the new `{% spot %}` shortcode: the Tear beside "The Tear" (Ch 02), the misfire beside "The Malfunction System" (Ch 11). Floated right; centred and narrower on phones.

**Print upscale (Session 35):** `tools/upscale_print.py` ran every approved PNG (except the transparent wordmark) through ComfyUI's RealESRGAN_x4plus_anime_6B into `art/{type}/print/{stem}_x4.png` (gitignored). The model keeps the flat fields and edges crisp, but drops the faint paper grain and smooths skin slightly. Plates are now 3328×4864. `scripts/build-pdf.py` cuts the chapter-opener and front-matter frames from these at the web crop (recovered by matching: 782×1168 at x 24–26, y 24 on the master), about 370 DPI on letter.

**Deco Wave 2 picks (Session 35):**
- spot_table (b): approved `deco-spot_table_v01_seed-3721935359.png`
- spot_tram (c): approved `deco-spot_tram_v01_seed-3737571921.png`
- spot_charter (a): approved `deco-spot_charter_v01_seed-2242206275.png`
- spot_kit (c): approved `deco-spot_kit_v01_seed-414637642.png`
- spot_wounded (c): approved `deco-spot_wounded_v01_seed-720151363.png`
- spot_lockpicks (b): approved `deco-spot_lockpicks_v01_seed-2658636431.png`
- spot_magnifier (a): approved `deco-spot_magnifier_v01_seed-2366548109.png`
- spot_handshake (b): approved `deco-spot_handshake_v01_seed-3384063528.png`
- spot_scholarly (c): approved `deco-spot_scholarly_v01_seed-3503377162.png`
- spot_wild (a): approved `deco-spot_wild_v01_seed-1932770582.png`
- spot_wild (c): approved `deco-spot_wild_v01_seed-942427744.png`
- spot_street (a): approved `deco-spot_street_v01_seed-2393896153.png`
- spot_timing (a): approved `deco-spot_timing_v01_seed-2551328071.png`
- sigil_aetheric (a): approved `deco-sigil_aetheric_v01_seed-1260207907.png`
- sigil_vivimancy (c): approved `deco-sigil_vivimancy_v01_seed-303236413.png`
- sigil_warding (c): approved `deco-sigil_warding_v01_seed-3120030221.png`
- sigil_divination (c): approved `deco-sigil_divination_v01_seed-3921553124.png`
- sigil_transmutation (b): approved `deco-sigil_transmutation_v01_seed-3327963557.png`
- sigil_ley (a): approved `deco-sigil_ley_v01_seed-1587638764.png`
- spot_wild: both a and c approved (a in use, c alternate). spot_street a approved as a fallback; reroll queued. spot_dice: none approved; reroll queued. Everything else archived.
- Web copies: `web/assets/art/spots/{table,tram,charter,kit,wounded,lockpicks,magnifier,handshake,scholarly,wild,timing}.webp` (`--hull`) and `web/assets/art/sigils/*.webp` (`--main-only`). Spots are placed with `{% spot %}` beside their planned sections; the three Skills spots use the new `center` option, because a full-width table follows each heading. School emblems appear on the Grimoire school headings and the Ch 08 school list (CSS only).
- **Lamps (user feedback):** nearly every Wave 2 spot has a lamp. Causes: lamp-heavy subject prompts, plus the D2 prefix's "light drawn as hard-edged rays and pools" and "arc lamps ... warm lamplight". `SPOT_STYLE` now has its own lamp-free prefix, asks for varied light (daylight, moonlight, window light, firelight), and says no lamps unless the scene names one.

**Deco Wave 2, round 2 (Session 35):**
- spot_dice (5b): approved `deco-spot_dice_v02_seed-3379016794.png` (six-sided dice are fine, per the user). Other v02 dice archived.
- spot_street: the user liked none of v02 (all four archived). The v01 fallback `deco-spot_street_v01_seed-2393896153.png` (12z) goes in as a stand-in, but both sides read industrial (power lines, lamps, stacks). v03 (Aether half with no buildings) and an alternative subject, `spot_scales` (a balance scale: cog vs crystal), are queued.

**Deco Wave 2, round 3 (Session 35):**
- spot_street v03 (Aether half with no buildings): approved `deco-spot_street_v03_seed-2577066863.png` (12b, in use) and `deco-spot_street_v03_seed-249387253.png` (12a, alternate; the user rated both "really good"). 12c/12d archived. The v01 stand-in stays approved but is replaced on the page.
- spot_scales: approved `deco-spot_scales_v01_seed-3076497211.png` (13c); the other three archived. It is Ch 10's second spot, beside "What Moves the Balance".

**Deco Wave 3 picks (Session 35):**
- spot_operatives (c): approved `deco-spot_operatives_v01_seed-3769924337.png`
- spot_silhouettes (c): approved `deco-spot_silhouettes_v01_seed-2686505075.png`
- spot_backlash (b): approved `deco-spot_backlash_v01_seed-4208299250.png`
- spot_knife (a): approved `deco-spot_knife_v01_seed-1120207886.png`
- spot_market (a): approved `deco-spot_market_v01_seed-1318848101.png`
- spot_collector (c): approved `deco-spot_collector_v01_seed-3318331926.png`
- spot_airship (b): approved `deco-spot_airship_v01_seed-3090174293.png`
- spot_watch (c): approved `deco-spot_watch_v01_seed-4148309664.png`
- spot_ward (c): approved `deco-spot_ward_v01_seed-3435583711.png`
- spot_vial (b): approved `deco-spot_vial_v01_seed-3978543307.png`
- spot_rooftops (a): approved `deco-spot_rooftops_v01_seed-2140374313.png`
- spot_informant (a): approved `deco-spot_informant_v01_seed-1099218142.png`
- spot_notebook (c): approved `deco-spot_notebook_v01_seed-942639246.png`
- spot_drawers (b): approved `deco-spot_drawers_v01_seed-2390427825.png`
- spot_handler (b): approved `deco-spot_handler_v01_seed-4119848123.png`
- spot_foundry (c): approved `deco-spot_foundry_v01_seed-785793098.png`
- spot_tunnels (c): approved `deco-spot_tunnels_v01_seed-260121104.png`
- corner_nouveau (a): approved `deco-corner_nouveau_v01_seed-2123906564.png`
- corner_deco (a): approved `deco-corner_deco_v01_seed-2769526848.png`
- badge_galvanic (b): approved `deco-badge_galvanic_v01_seed-1593863693.png`
- badge_aetheric (b): approved `deco-badge_aetheric_v01_seed-3505952753.png`
- badge_neutral (b): approved `deco-badge_neutral_v01_seed-2197070450.png`
- spot_catalogue: none approved; v02 queued (galvanic pistol spelled out). spot_watch 9c trimmed to the circle on cut-out (fake text outside it). Everything else archived.
- Web copies: 17 spots in `web/assets/art/spots/` (`--hull`; the watch also `--main-only` to drop fake text outside the circle); corners cropped to their top-left 60% before cut-out (Deco 20a had faint full-frame lines), with flipped `-tr`/`-bl` copies; badges in `web/assets/art/badges/`.
- Corners: callouts and stat blocks get top-right and bottom-left corners via one `::after` with two background layers (`::before` is the edge bar). Aether chapters use Nouveau, all others Deco. Pregen cards keep only the top-right corner, so the portrait stays clear.
- Zone badges: on the quickstart's location labels.
- spot_catalogue v02 (7c): approved `deco-spot_catalogue_v02_seed-3104587837.png`; the other three archived. Placed beside "Melee Weapons" (Ch 13).

**PDF ornaments (Session 35):** `build-pdf.py` tags each chapter `<section>` with `data-theme`, and `print.css` gets the same ornament set as the web: themed section dividers, drop cap, tailpiece, corners (callouts and stat blocks), school emblems (headings and the Ch 08 list; PDF ids carry a chapter prefix, so the selectors match on id endings), and zone badges. Print uses `divider-neutral-print.webp` (original navy; the web copy is recoloured to bone). The web copies are sharp enough at print size (dividers ~275 DPI at 4 in, tiles higher). The print drop cap is a raised initial, because WeasyPrint doesn't wrap the first line around a floated `::first-letter`. Corners shrank to fit inside the box padding on web and print; the bottom-left corner had crowded callout text. Print upscale re-run for Wave 2–3: 70 masters in `art/*/print/`.
