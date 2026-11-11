#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — selector page for a Deco wave (Session 37)

Builds one self-contained HTML page (images embedded as JPEG data URIs) that shows
every generated candidate for the pieces in a wave, grouped by section. Each piece
gets a number and each candidate a letter, so the user can reply with codes like
"3b". Tapping a candidate marks it as the pick; the bar at the foot collects the
picks for copying (kept in the viewer's own browser only).

    python tools/wave_page.py --wave 4 --out /path/to/wave4.html
"""

import argparse
import base64
import html
import re
import subprocess
from pathlib import Path

from deco_suite import ART_DIR, PIECES

# Section order, title, and where each piece is meant to go (shown under its heading).
SECTIONS = [
    ("Full-page plates", "Tall plates that face a chapter opener in the PDF and sit under the crown on the web.", "plate_"),
    ("Half-page scenes", "Landscape scenes for establishing places: full column width on the web, half a page in print.", "scene_"),
    ("Cover candidates", "For the PDF cover and a redrawn web hero. Open sky at the top is left for the title.", "cover_"),
    ("NPC portraits", "The recurring faces of the fiction and the GM chapters.", "npc_"),
    ("Story 04 spots", "Round spots for No Kinder Country: its fiction card and the Combat and Getting Hurt chapters.", "spot_"),
]

WHERE = {
    "plate_tear": "The State of the World: the Tear, fifty years ago.",
    "plate_wet_ember": "Quickstart or Creating a Character: the four leads planning.",
    "plate_railyard": "The World Between: a Wild Zone swallowing a rail yard.",
    "plate_factory": "Arms & Equipment: the galvanic factory floor.",
    "plate_patron": "Societies & Patrons: meeting the patron.",
    "plate_market_fight": "Combat: a fight frozen on the timing track.",
    "plate_study": "Magic: the scholarly caster's workshop.",
    "plate_foundry": "Quickstart: the foundry climax.",
    "plate_mill": "Artifacts: the remade mill.",
    "plate_deep_wild": "Running the Game: an expedition into the Deep Wild.",
    "plate_gradient": "Introduction: the gradient street, the book's thesis image.",
    "plate_ford": "Getting Hurt, and Story 04: the ambush at the ford.",
    "scene_ashwick": "The State of the World: Ashwick at dawn.",
    "scene_quarter": "Societies or The World Between: the Veilwright Quarter market.",
    "scene_sootborn": "The World Between: the Sootborn settlement.",
    "scene_village_cars": "The World Between or Arms & Equipment: where engines stop.",
    "scene_airship": "Economy: the airship mast.",
    "scene_checkpoint": "Societies: a Greycoat checkpoint in the rain.",
    "scene_convoy": "Arms & Equipment: the suppression convoy (Story 04).",
    "scene_rooftop": "Skills: a rooftop chase.",
    "scene_communion": "The State of the World: the Thornfield Communion's fields.",
    "scene_vault": "Artifacts: the transformed tunnel nave (Story 03).",
    "cover_between": "PDF cover / web hero: the lone figure between two cities.",
    "cover_society": "PDF cover / web hero: the four on a hilltop road.",
    "cover_tear": "PDF cover / web hero: the Tear over the skyline.",
    "npc_fixer": "Corrigan Fels, the Syndicate fixer.",
    "npc_broker": "Dace Rennick of the Margin.",
    "npc_barkeep": "Hesper Brack of the Wet Ember.",
    "npc_scholar": "Dr. Isavel Crane of the Gradient Scholars.",
    "npc_inspector": "Inspector Renna Laine of the Greycoat Authority.",
    "npc_director": "Gideon Marlow, Ashworth's operations director.",
    "npc_envoy": "Thessaly Vane of the Covenant of Embers.",
    "spot_ford": "Story 04 card: the ford ambush.",
    "spot_stretcher": "Getting Hurt: the stretcher carry.",
    "spot_dampener": "Arms & Equipment: the suppression engine.",
    "spot_barrier": "Magic or Combat: a ward under fire.",
}

# Claude's notes on a candidate set (shown in amber under the placement line).
NOTES = {
    "plate_railyard": "These read more as forest than Wild Zone: few crystals. Reroll if you want the crystals.",
    "plate_foundry": "One seed has a small signature in its bottom-left corner; it would be cropped.",
    "plate_market_fight": "None of these show the cyan shield the prompt asked for; they work as a plain street fight.",
    "plate_wet_ember": "One seed has a fake sign over the bar; it would be cropped or painted out.",
    "scene_sootborn": "These came out as ordinary cottages, not scavenged carriages. Reroll candidate.",
    "scene_convoy": "One seed has a fake number plate on the lorry; crop or pick another.",
    "scene_quarter": "Lovely market, but no crystals. Fine for a street scene.",
    "plate_market_fight": "Round 2 reroll: the cyan shield is now the centre of the picture.",
    "scene_communion": "The crops came out normal-sized, not giant. Pleasant, but the strangeness is missing.",
    "npc_barkeep": "All three have two arms; Hesper lost one. The empty sleeve would need painting in, or a reroll.",
    "npc_scholar": "These read younger than Crane's fifties.",
    "npc_inspector": "The police boxes carry fake lettering, and she reads younger than mid-forties. Crop or reroll.",
    "npc_director": "Two seeds put him in a naval-style uniform rather than a suit.",
    "npc_broker": "One seed has stray letters in the bottom-right corner; it would be cropped.",
    "spot_barrier": "None of these show the cyan ward; he kneels with a raised hand. Reroll candidate.",
}


NAMES = {
    "plate_tear": "The Tear", "plate_wet_ember": "The Wet Ember", "plate_railyard": "The swallowed rail yard",
    "plate_factory": "Shift change", "plate_patron": "The patron's office", "plate_market_fight": "Market square fight",
    "plate_study": "The scholar's workshop", "plate_foundry": "The foundry crack", "plate_mill": "Inside the mill",
    "plate_deep_wild": "Into the Deep Wild", "plate_gradient": "The gradient street", "plate_ford": "The ford ambush",
    "scene_ashwick": "Ashwick at dawn", "scene_quarter": "The Quarter market", "scene_sootborn": "The Sootborn settlement",
    "scene_village_cars": "Where engines stop", "scene_airship": "The airship mast", "scene_checkpoint": "Checkpoint in the rain",
    "scene_convoy": "The suppression convoy", "scene_rooftop": "Rooftop chase", "scene_communion": "The Communion's fields",
    "scene_vault": "The tunnel nave", "cover_between": "Between two cities", "cover_society": "Four on the hill road",
    "cover_tear": "The Tear over the skyline", "npc_fixer": "The fixer", "npc_broker": "The broker",
    "npc_barkeep": "The barkeep", "npc_scholar": "The field scientist", "npc_inspector": "The inspector",
    "npc_director": "The director", "npc_envoy": "The envoy", "spot_ford": "The ford", "spot_stretcher": "The stretcher",
    "spot_dampener": "The dampener", "spot_barrier": "The ward under fire",
}


def title_of(piece: str) -> str:
    return NAMES.get(piece) or piece.split("_", 1)[1].replace("_", " ").capitalize()


def thumb(path: Path, width: int) -> str:
    out = subprocess.run(["magick", str(path), "-resize", f"{width}x>", "-strip", "-quality", "78", "jpg:-"],
                         check=True, capture_output=True).stdout
    return "data:image/jpeg;base64," + base64.b64encode(out).decode()


def candidates(piece: str) -> list[Path]:
    p = PIECES[piece]
    folder = ART_DIR / p["art_type"] / "generated"
    rx = re.compile(rf"^deco-{re.escape(piece)}_v\d+_seed-(\d+)\.png$")
    return sorted(f for f in folder.glob(f"deco-{piece}_v*_seed-*.png") if rx.match(f.name))


CSS = """
:root { color-scheme: dark; --midnight:#0e1a2b; --night:#0b0e17; --bone:#efe6d2; --bone-dim:#b9b09c;
  --soot:#17140f; --cyan:#3dc8e0; --amber:#e8a825; --oxblood:#b8493a; --rule:#22324a; }
body { background:var(--midnight); color:var(--bone); font:500 1.12rem/1.5 'Cormorant Garamond', Georgia, serif; }
.wrap { max-width:1180px; margin:0 auto; padding-inline:20px; padding-block:40px 120px; }
h1, h2, h3 { font-family:'Playfair Display', Georgia, serif; text-wrap:balance; margin:0; }
h1 { font-size:clamp(2rem,5vw,3.2rem); font-weight:900; }
.round { font:700 .8rem 'JetBrains Mono', monospace; letter-spacing:.12em; text-transform:uppercase; color:var(--amber); margin:.6rem 0 0; }
.lede { max-width:64ch; color:var(--bone-dim); margin:.6rem 0 0; }
.how { margin-top:1.4rem; padding:1rem 1.2rem; border:1px solid var(--rule); border-left:3px solid var(--amber); max-width:70ch; }
.how code { font-family:'JetBrains Mono', monospace; font-size:.85em; color:var(--amber); }
nav.toc { display:flex; flex-wrap:wrap; gap:.4rem 1.2rem; margin-top:1.2rem; font:700 .75rem 'JetBrains Mono', monospace; letter-spacing:.1em; text-transform:uppercase; }
nav.toc a { color:var(--bone-dim); text-decoration:none; border-bottom:1px solid var(--rule); }
nav.toc a:hover, nav.toc a:focus-visible { color:var(--amber); }
.section { margin-top:4rem; }
.section > h2 { font-size:clamp(1.6rem,3.6vw,2.2rem); font-weight:900; color:var(--bone); border-bottom:1px solid var(--rule); padding-bottom:.4rem; }
.section > p { color:var(--bone-dim); margin:.5rem 0 0; max-width:70ch; }
.piece { margin-top:2.4rem; }
.piece h3 { font-size:1.35rem; font-weight:700; display:flex; align-items:baseline; gap:.7rem; }
.num { font:700 .8rem 'JetBrains Mono', monospace; color:var(--bone-dim); }
.where { color:var(--bone-dim); margin:.2rem 0 .9rem; max-width:70ch; }
.flag { margin:-.5rem 0 .9rem; max-width:70ch; color:var(--amber); font-style:italic; }
.cands { display:grid; gap:16px; grid-template-columns:repeat(auto-fill, minmax(210px,1fr)); }
.landscape .cands { grid-template-columns:repeat(auto-fill, minmax(320px,1fr)); }
.cand { margin:0; border:1px solid var(--rule); background:var(--night); cursor:pointer; position:relative; }
.cand:focus-visible { outline:2px solid var(--amber); outline-offset:2px; }
.cand img { display:block; width:100%; height:auto; }
.cand figcaption { display:flex; justify-content:space-between; align-items:baseline; padding:.45rem .7rem;
  font:.74rem 'JetBrains Mono', monospace; color:var(--bone-dim); font-variant-numeric:tabular-nums; }
.cand figcaption b { color:var(--bone); font-size:1rem; }
.cand.picked { border-color:var(--amber); box-shadow:0 0 0 2px var(--amber); }
.cand.picked figcaption b::after { content:" ✓ picked"; color:var(--amber); font-size:.75rem; }
.bar { position:fixed; left:0; right:0; bottom:0; padding:.7rem 20px calc(.7rem + env(safe-area-inset-bottom,0px));
  background:rgba(11,14,23,.96); border-top:1px solid var(--rule); display:flex; gap:.8rem; align-items:center; flex-wrap:wrap; }
.bar .label { font:700 .72rem 'JetBrains Mono', monospace; letter-spacing:.12em; text-transform:uppercase; color:var(--amber); }
.bar output { flex:1 1 14rem; font:.9rem 'JetBrains Mono', monospace; color:var(--bone); min-height:1.2em; overflow-wrap:anywhere; }
.bar button { font:700 .75rem 'JetBrains Mono', monospace; letter-spacing:.1em; text-transform:uppercase; padding:.5rem .9rem;
  background:var(--amber); color:var(--soot); border:0; cursor:pointer; }
.bar button.ghost { background:transparent; color:var(--bone-dim); border:1px solid var(--rule); }
.bar button:focus-visible { outline:2px solid var(--bone); outline-offset:2px; }
@media (prefers-reduced-motion:no-preference) { .cand { transition:box-shadow .15s, border-color .15s; } }
"""

JS = """
const KEY = 'aetherfall-' + document.body.dataset.wave + '-picks';
let picks = {};
try { picks = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
const out = document.getElementById('picks');
function render() {
  document.querySelectorAll('.cand').forEach(c => c.classList.toggle('picked', picks[c.dataset.piece] === c.dataset.code));
  const codes = Object.values(picks).sort((a, b) => parseInt(a) - parseInt(b) || a.localeCompare(b));
  out.textContent = codes.length ? codes.join(' ') : 'Tap a picture to pick it.';
  try { localStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) {}
}
function toggle(c) {
  const p = c.dataset.piece;
  if (picks[p] === c.dataset.code) delete picks[p]; else picks[p] = c.dataset.code;
  render();
}
document.querySelectorAll('.cand').forEach(c => {
  c.addEventListener('click', () => toggle(c));
  c.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(c); } });
});
document.getElementById('copy').addEventListener('click', () => {
  const text = out.textContent;
  navigator.clipboard.writeText(text).then(() => { document.getElementById('copy').textContent = 'Copied'; },
    () => { const r = document.createRange(); r.selectNodeContents(out); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
});
document.getElementById('clear').addEventListener('click', () => { picks = {}; render(); });
render();
"""


def build(wave: int, title: str, round_label: str, lede: str) -> str:
    parts, toc, n = [], [], 0
    for sec_title, sec_note, prefix in SECTIONS:
        pieces = [k for k, v in PIECES.items() if v["wave"] == wave and k.startswith(prefix)]
        if not pieces:
            continue
        anchor = prefix.rstrip("_") + "s"
        toc.append(f'<a href="#{anchor}">{html.escape(sec_title)}</a>')
        body = []
        for piece in pieces:
            files = candidates(piece)
            if not files:
                continue
            n += 1
            p = PIECES[piece]
            landscape = p["width"] > p["height"]
            width = 900 if landscape else 520
            figs = []
            for i, f in enumerate(files):
                code = f"{n}{chr(97 + i)}"
                seed = f.stem.rsplit("seed-", 1)[1]
                figs.append(
                    f'<figure class="cand" tabindex="0" role="button" data-piece="{piece}" data-code="{code}" '
                    f'aria-label="Pick {code}"><img src="{thumb(f, width)}" alt="{html.escape(title_of(piece))}, candidate {code}" '
                    f'loading="lazy"><figcaption><b>{code}</b><span>seed {seed}</span></figcaption></figure>')
            body.append(
                f'<article class="piece{" landscape" if landscape else ""}" id="{piece}"><h3><span class="num">{n}</span>'
                f'{html.escape(title_of(piece))}</h3><p class="where">{html.escape(WHERE.get(piece, ""))}</p>'
                + (f'<p class="flag">{html.escape(NOTES[piece])}</p>' if piece in NOTES else '') +
                f'<div class="cands">{"".join(figs)}</div></article>')
        parts.append(f'<section class="section" id="{anchor}"><h2>{html.escape(sec_title)}</h2>'
                     f'<p>{html.escape(sec_note)}</p>{"".join(body)}</section>')
    return f"""<title>{html.escape(title)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=JetBrains+Mono:wght@400;700&display=swap">
<style>{CSS}</style>
<div class="wrap" data-wave="{wave}">
  <h1>{html.escape(title)}</h1>
  <p class="round">{html.escape(round_label)}</p>
  <p class="lede">{html.escape(lede)}</p>
  <div class="how">Tap the candidate you like for each piece, then copy your picks from the bar at the bottom and send them, like <code>1b 4a 13c</code>. Skip any piece you don't want. Reply "reroll 5" for a piece where nothing works.</div>
  <nav class="toc">{"".join(toc)}</nav>
  {"".join(parts)}
</div>
<div class="bar"><span class="label">Your picks</span><output id="picks"></output>
<button type="button" id="copy">Copy</button><button type="button" class="ghost" id="clear">Clear</button></div>
<script>document.body.dataset.wave = "wave{wave}-{re.sub(r"[^a-z0-9]+", "-", round_label.lower())}";{JS}</script>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default=None)
    ap.add_argument("--round", default="Round 1")
    ap.add_argument("--lede", default="")
    args = ap.parse_args()
    page = build(args.wave, args.title or f"Deco Wave {args.wave}", args.round, args.lede)
    Path(args.out).write_text(page)
    print(f"wrote {args.out} ({len(page) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
