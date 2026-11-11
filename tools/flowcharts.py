#!/usr/bin/env python3
"""Draw the rulebook's procedure diagrams as Deco plates.

Why this exists: the charts were Mermaid, and Mermaid gives boxes. A box with an
accent colour is not the house style, and these two diagrams are the only drawn
pages in the book that a reader meets without an illustrator's hand on them. The
rest of the suite is lithograph plates; these should read as plates too.

The split of labour:

* ``dot`` does layout only. Working out where fourteen nodes go without crossings
  is solved work, and hand-placing them breaks the moment a rule changes.
* Everything you see is drawn here. Node silhouettes, rules, rivets, arrowheads,
  the frame and the title block are all emitted as paths, so the diagrams obey
  the style guide rather than a theme file.
* No colour is written into the SVG. Every element carries a class and the book's
  stylesheets paint it, which is what lets one asset serve the midnight web page
  and the bone-paper print edition without a second render.

Two registers, chosen by subject, matching the ornament split in
``docs/art/style-guide.md`` §3:

* ``engine``  — Deco geometry for the Combat sequence. Chamfered plates, rivets,
  chevron heads, orthogonal runs. It should look like a machine schedule.
* ``veil``    — Nouveau curve for the Spellcasting procedure. Cartouches with
  drawn-in corners, a rayed circle at each decision, flowing connectors. It
  should look like a page out of a working grimoire.

Usage: ``python3 tools/flowcharts.py`` writes web/assets/diagrams/*.svg.
"""

from __future__ import annotations

import json
import math
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "web" / "assets" / "diagrams"

# Layout is computed at 72dpi (graphviz points) and drawn at the same scale, so
# one SVG unit is one point and the printed size is predictable.
BODY_SIZE = 13.0          # node label, px/pt
EDGE_SIZE = 9.0           # edge label
CHAR_W = 0.52             # mean advance width of Source Serif 4, in ems
NODE_PAD_X = 26.0
NODE_PAD_Y = 20.0
LINE_H = 16.0
MAX_LABEL_CH = 22         # wrap wider labels; a long box starves the layout


# ── Diagram definitions ──────────────────────────────────────────────────────
# The wording of every node is the rulebook's own and is not edited here.

@dataclass
class Node:
    id: str
    label: str
    shape: str = "process"      # process | decision | terminal
    accent: str = ""            # aether | galvanic | warn | bad | good


@dataclass
class Edge:
    src: str
    dst: str
    label: str = ""


@dataclass
class Chart:
    key: str
    title: str
    stage: str
    plate: str
    register: str               # engine | veil
    nodes: list[Node]
    edges: list[Edge]
    rankdir: str = "TB"
    notes: list[str] = field(default_factory=list)


CHARTS: list[Chart] = [
    Chart(
        key="spell-1-casting", title="Spellcasting", stage="Casting",
        plate="I", register="veil",
        notes=["Interruption is checked once, at the moment it happens."],
        nodes=[
            Node("A", "Declare spell, begin casting", "terminal", "aether"),
            Node("B", "Wait the casting time"),
            Node("C", "Interrupted?", "decision"),
            Node("D", "Concentration check"),
            Node("CANCEL", "Spell fizzles", "terminal", "warn"),
            Node("E", "Roll d100 vs casting target", "terminal", "aether"),
        ],
        edges=[
            Edge("A", "B"), Edge("B", "C"),
            Edge("C", "D", "Yes"), Edge("C", "E", "No"),
            Edge("D", "CANCEL", "Fail"), Edge("D", "E", "Pass"),
        ],
    ),
    Chart(
        key="spell-2-roll", title="Spellcasting", stage="The Roll",
        plate="II", register="veil",
        notes=["The margin under the target sets the tier; a push buys one step."],
        nodes=[
            Node("E", "Roll d100 vs casting target", "terminal", "aether"),
            Node("F", "Under target?", "decision"),
            Node("MISFIRE", "Misfire", "process", "bad"),
            Node("G", "Margin sets the tier"),
            Node("H", "Push one tier?", "decision"),
            Node("PUSH", "Pay the extra EP"),
            Node("I", "Pay EP, apply the effect"),
            Node("J", "Backlash check", "terminal", "aether"),
        ],
        edges=[
            Edge("E", "F"),
            Edge("F", "MISFIRE", "No"), Edge("F", "G", "Yes"),
            Edge("G", "H"),
            Edge("H", "PUSH", "Yes"), Edge("H", "I", "No"),
            Edge("PUSH", "I"), Edge("I", "J"), Edge("MISFIRE", "J"),
        ],
    ),
    Chart(
        key="spell-3-backlash", title="Spellcasting", stage="Backlash",
        plate="III", register="veil",
        notes=["Backlash is the Aether biting back; describe it as the spell."],
        nodes=[
            Node("J", "Backlash check", "terminal", "aether"),
            Node("K", "Resolved", "terminal", "good"),
            Node("L", "Backlash: 1d4 HP", "process", "warn"),
            Node("M", "Wild effect? 25%", "decision"),
            Node("N", "Roll on the wild effect table", "process", "warn"),
        ],
        edges=[
            Edge("J", "K", "Pass"), Edge("J", "L", "Fail"),
            Edge("L", "M"), Edge("M", "K", "No"), Edge("M", "N", "Yes"),
            Edge("N", "K"),
        ],
    ),
    Chart(
        key="combat-1-count", title="Combat", stage="The Count",
        plate="I", register="engine",
        notes=["The count advances until a token is standing on it."],
        nodes=[
            Node("START", "New count", "terminal", "galvanic"),
            Node("CHECK", "Tokens here?", "decision"),
            Node("ADV", "Advance count"),
            Node("RESOLVE", "Resolve actions"),
            Node("TYPE", "Attack type?", "terminal", "galvanic"),
        ],
        edges=[
            Edge("START", "CHECK"),
            Edge("CHECK", "ADV", "No"), Edge("ADV", "START"),
            Edge("CHECK", "RESOLVE", "Yes"), Edge("RESOLVE", "TYPE"),
        ],
    ),
    Chart(
        key="combat-2-attack", title="Combat", stage="The Attack",
        plate="II", register="engine", rankdir="TB",
        notes=["Reliability is rolled before the attack, every shot."],
        nodes=[
            Node("TYPE", "Attack type?", "terminal", "galvanic"),
            Node("MROLL", "Roll vs Melee/Brawl"),
            Node("RROLL", "Roll vs Ranged"),
            Node("REL", "Roll Reliability"),
            Node("SPELL", "See Spell Flowchart", "process", "aether"),
            Node("RELCHECK", "Pass?", "decision"),
            Node("MAL", "Malfunction", "process", "bad"),
            Node("FROLL", "Roll vs Firearms"),
            Node("HIT", "Hit?", "terminal", "galvanic"),
            Node("DECLARE", "Declare next action", "terminal", "galvanic"),
        ],
        edges=[
            Edge("TYPE", "MROLL", "Melee"), Edge("TYPE", "RROLL", "Ranged"),
            Edge("TYPE", "REL", "Firearm"), Edge("TYPE", "SPELL", "Spell"),
            Edge("REL", "RELCHECK"),
            Edge("RELCHECK", "MAL", "Fail"), Edge("RELCHECK", "FROLL", "Pass"),
            Edge("MROLL", "HIT"), Edge("RROLL", "HIT"), Edge("FROLL", "HIT"),
            Edge("MAL", "DECLARE"),
        ],
    ),
    Chart(
        key="combat-3-damage", title="Combat", stage="Damage",
        plate="III", register="engine",
        notes=["Armour degrades only when the damage beats the soak."],
        nodes=[
            Node("HIT", "Hit?", "terminal", "galvanic"),
            Node("DMG", "Roll damage"),
            Node("SOAK", "Subtract armor soak"),
            Node("APPLY", "Apply to wound track"),
            Node("DEGRADE", "Damage > soak?", "decision"),
            Node("DEG", "Armor may degrade"),
            Node("DECLARE", "Declare next action", "terminal", "galvanic"),
        ],
        edges=[
            Edge("HIT", "DMG", "Hit"), Edge("HIT", "DECLARE", "Miss"),
            Edge("DMG", "SOAK"), Edge("SOAK", "APPLY"), Edge("APPLY", "DEGRADE"),
            Edge("DEGRADE", "DEG", "Yes"), Edge("DEGRADE", "DECLARE", "No"),
            Edge("DEG", "DECLARE"),
        ],
    ),
]


# ── Label measuring and wrapping ─────────────────────────────────────────────

def wrap(label: str, limit: int = MAX_LABEL_CH) -> list[str]:
    words, lines, line = label.split(), [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if len(candidate) > limit and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def node_size(node: Node) -> tuple[float, float, list[str]]:
    """Box size in points. Decisions need room for the shape around the text."""
    lines = wrap(node.label)
    text_w = max(len(l) for l in lines) * BODY_SIZE * CHAR_W
    width = text_w + NODE_PAD_X * 2
    height = len(lines) * LINE_H + NODE_PAD_Y * 2
    if node.shape == "decision":
        # A rayed circle or a stepped hexagon carries its label inside the form.
        width = max(width * 1.35, height * 2.1)
        height = max(height * 1.55, 74.0)
    elif node.shape == "terminal":
        width += 18.0
    return width, height, lines


# ── Layout via graphviz ──────────────────────────────────────────────────────

def layout(chart: Chart) -> dict:
    sizes = {n.id: node_size(n) for n in chart.nodes}
    # The Engine register is a machine plate, so its runs are square; the Veil
    # register flows, so its connectors stay splines.
    routing = "ortho" if chart.register == "engine" else "spline"
    lines = [
        "digraph {",
        f"  rankdir={chart.rankdir};",
        f"  splines={routing}; overlap=false;",
        "  nodesep=0.62; ranksep=0.70;",
        "  node [shape=box fixedsize=true];",
    ]
    for node in chart.nodes:
        w, h, _ = sizes[node.id]
        lines.append(f'  {node.id} [width={w / 72:.4f} height={h / 72:.4f}];')
    for edge in chart.edges:
        lines.append(f"  {edge.src} -> {edge.dst};")
    lines.append("}")
    source = "\n".join(lines)

    if not shutil.which("dot"):
        sys.exit("graphviz 'dot' not found; install graphviz to build the diagrams")
    proc = subprocess.run(["dot", "-Tjson"], input=source, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"dot failed for {chart.key}: {proc.stderr[:400]}")
    data = json.loads(proc.stdout)

    bb = [float(v) for v in data["bb"].split(",")]
    height = bb[3]
    positions = {}
    for obj in data.get("objects", []):
        x, y = (float(v) for v in obj["pos"].split(","))
        positions[obj["name"]] = (x, height - y)      # SVG y grows downward
    splines = {}
    for e in data.get("edges", []):
        src = data["objects"][e["tail"]]["name"]
        dst = data["objects"][e["head"]]["name"]
        pts, end = [], None
        for chunk in e.get("pos", "").split():
            if chunk.startswith("e,"):
                ex, ey = (float(v) for v in chunk[2:].split(","))
                end = (ex, height - ey)
            elif chunk.startswith("s,"):
                continue
            else:
                px, py = (float(v) for v in chunk.split(","))
                pts.append((px, height - py))
        if end:
            pts.append(end)
        splines[(src, dst)] = pts
    return {"w": bb[2], "h": bb[3], "pos": positions, "splines": splines, "sizes": sizes}


# ── Drawing ──────────────────────────────────────────────────────────────────

def esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def chamfered(x: float, y: float, w: float, h: float, cut: float) -> str:
    """Deco plate: a rectangle with its corners cut away."""
    return (f"M{x + cut:.1f} {y:.1f} H{x + w - cut:.1f} L{x + w:.1f} {y + cut:.1f} "
            f"V{y + h - cut:.1f} L{x + w - cut:.1f} {y + h:.1f} H{x + cut:.1f} "
            f"L{x:.1f} {y + h - cut:.1f} V{y + cut:.1f} Z")


def cartouche(x: float, y: float, w: float, h: float, r: float) -> str:
    """Nouveau frame: corners drawn inward, the way a ruled grimoire panel is."""
    return (f"M{x + r:.1f} {y:.1f} H{x + w - r:.1f} Q{x + w - r * 0.3:.1f} {y + r * 0.3:.1f} "
            f"{x + w:.1f} {y + r:.1f} V{y + h - r:.1f} Q{x + w - r * 0.3:.1f} {y + h - r * 0.3:.1f} "
            f"{x + w - r:.1f} {y + h:.1f} H{x + r:.1f} Q{x + r * 0.3:.1f} {y + h - r * 0.3:.1f} "
            f"{x:.1f} {y + h - r:.1f} V{y + r:.1f} Q{x + r * 0.3:.1f} {y + r * 0.3:.1f} "
            f"{x + r:.1f} {y:.1f} Z")


def stepped_hex(cx: float, cy: float, w: float, h: float) -> str:
    """Decision, Deco register: a hexagon with stepped shoulders."""
    hw, hh = w / 2, h / 2
    s = hw * 0.30
    return (f"M{cx - hw:.1f} {cy:.1f} L{cx - hw + s:.1f} {cy - hh:.1f} "
            f"H{cx + hw - s:.1f} L{cx + hw:.1f} {cy:.1f} "
            f"L{cx + hw - s:.1f} {cy + hh:.1f} H{cx - hw + s:.1f} Z")


def draw_node(node: Node, pos: tuple[float, float], size: tuple[float, float, list[str]],
              register: str) -> str:
    cx, cy = pos
    w, h, lines = size
    x, y = cx - w / 2, cy - h / 2
    cls = f"fc-node fc-{node.shape}" + (f" fc-{node.accent}" if node.accent else "")
    out = [f'<g class="{cls}">']

    if node.shape == "decision":
        if register == "veil":
            # A rayed circle: the decision as an alchemical figure.
            r = min(w, h) / 2
            out.append(f'<circle class="fc-shape" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>')
            out.append(f'<circle class="fc-inner" cx="{cx:.1f}" cy="{cy:.1f}" r="{r - 4.5:.1f}"/>')
            for i in range(12):
                a = math.radians(i * 30)
                x1, y1 = cx + math.cos(a) * (r + 2.5), cy + math.sin(a) * (r + 2.5)
                x2, y2 = cx + math.cos(a) * (r + 7.5), cy + math.sin(a) * (r + 7.5)
                out.append(f'<line class="fc-ray" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
        else:
            out.append(f'<path class="fc-shape" d="{stepped_hex(cx, cy, w, h)}"/>')
            out.append(f'<path class="fc-inner" d="{stepped_hex(cx, cy, w - 9, h - 9)}"/>')
    elif node.shape == "terminal":
        if register == "veil":
            r = h / 2
            out.append(f'<rect class="fc-shape" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
                       f'height="{h:.1f}" rx="{r:.1f}"/>')
            out.append(f'<rect class="fc-inner" x="{x + 4:.1f}" y="{y + 4:.1f}" '
                       f'width="{w - 8:.1f}" height="{h - 8:.1f}" rx="{r - 4:.1f}"/>')
        else:
            # Stadium with chevron ends: a terminal block on a machine plate.
            out.append(f'<path class="fc-shape" d="{chamfered(x, y, w, h, h / 2.6)}"/>')
            out.append(f'<path class="fc-inner" d="{chamfered(x + 4, y + 4, w - 8, h - 8, h / 2.6 - 3)}"/>')
    else:
        if register == "veil":
            out.append(f'<path class="fc-shape" d="{cartouche(x, y, w, h, 11)}"/>')
            out.append(f'<path class="fc-inner" d="{cartouche(x + 4, y + 4, w - 8, h - 8, 8)}"/>')
        else:
            cut = 7.0
            out.append(f'<path class="fc-shape" d="{chamfered(x, y, w, h, cut)}"/>')
            out.append(f'<path class="fc-inner" d="{chamfered(x + 4, y + 4, w - 8, h - 8, cut - 2)}"/>')
            for rx, ry in ((x + cut + 2.5, y + cut - 1.5), (x + w - cut - 2.5, y + cut - 1.5),
                           (x + cut + 2.5, y + h - cut + 1.5), (x + w - cut - 2.5, y + h - cut + 1.5)):
                out.append(f'<circle class="fc-rivet" cx="{rx:.1f}" cy="{ry:.1f}" r="1.7"/>')

    first = cy - (len(lines) - 1) * LINE_H / 2 + BODY_SIZE * 0.35
    for i, line in enumerate(lines):
        out.append(f'<text class="fc-text" x="{cx:.1f}" y="{first + i * LINE_H:.1f}">{esc(line)}</text>')
    out.append("</g>")
    return "\n".join(out)


def draw_edge(points: list[tuple[float, float]], label: str, register: str, idx: int) -> str:
    if len(points) < 2:
        return ""
    out = []
    if register == "engine":
        # Machine plates run square: straight segments, no easing.
        d = f"M{points[0][0]:.1f} {points[0][1]:.1f}" + "".join(
            f" L{px:.1f} {py:.1f}" for px, py in points[1:])
    else:
        d = f"M{points[0][0]:.1f} {points[0][1]:.1f}"
        for i in range(1, len(points) - 2, 3):
            p1, p2, p3 = points[i], points[i + 1], points[i + 2]
            d += (f" C{p1[0]:.1f} {p1[1]:.1f} {p2[0]:.1f} {p2[1]:.1f} "
                  f"{p3[0]:.1f} {p3[1]:.1f}")
        if (len(points) - 1) % 3:
            d += "".join(f" L{px:.1f} {py:.1f}" for px, py in points[-((len(points) - 1) % 3):])
    out.append(f'<path class="fc-edge" d="{d}"/>')

    # Arrowhead, drawn to match the register: open chevron, or a drawn point.
    (x2, y2), (x1, y1) = points[-1], points[-2]
    angle = math.atan2(y2 - y1, x2 - x1)
    if register == "engine":
        for sign in (1, -1):
            a = angle + sign * math.radians(148)
            out.append(f'<line class="fc-head" x1="{x2:.1f}" y1="{y2:.1f}" '
                       f'x2="{x2 + math.cos(a) * 9:.1f}" y2="{y2 + math.sin(a) * 9:.1f}"/>')
    else:
        a1, a2 = angle + math.radians(152), angle - math.radians(152)
        out.append(f'<path class="fc-point" d="M{x2:.1f} {y2:.1f} '
                   f'L{x2 + math.cos(a1) * 10:.1f} {y2 + math.sin(a1) * 10:.1f} '
                   f'Q{x2 - math.cos(angle) * 3.5:.1f} {y2 - math.sin(angle) * 3.5:.1f} '
                   f'{x2 + math.cos(a2) * 10:.1f} {y2 + math.sin(a2) * 10:.1f} Z"/>')

    if label:
        mid = points[len(points) // 2]
        chip_w = len(label) * EDGE_SIZE * 0.62 + 12
        out.append(f'<rect class="fc-chip" x="{mid[0] - chip_w / 2:.1f}" y="{mid[1] - 8:.1f}" '
                   f'width="{chip_w:.1f}" height="16" rx="1"/>')
        out.append(f'<text class="fc-edge-text" x="{mid[0]:.1f}" y="{mid[1] + 3.5:.1f}">'
                   f'{esc(label.upper())}</text>')
    return "\n".join(out)


def draw_frame(chart: Chart, w: float, h: float) -> str:
    """The plate's own chrome: rule, corner marks and a title block."""
    m = 14.0
    out = [f'<rect class="fc-field" x="0" y="0" width="{w:.1f}" height="{h:.1f}"/>',
           f'<rect class="fc-rule" x="{m:.1f}" y="{m:.1f}" width="{w - m * 2:.1f}" '
           f'height="{h - m * 2:.1f}"/>',
           f'<rect class="fc-rule-inner" x="{m + 4:.1f}" y="{m + 4:.1f}" '
           f'width="{w - (m + 4) * 2:.1f}" height="{h - (m + 4) * 2:.1f}"/>']
    # Corner marks: stepped for the Engine, a drawn curl for the Veil.
    for sx, sy, cx0, cy0 in ((1, 1, m, m), (-1, 1, w - m, m), (1, -1, m, h - m), (-1, -1, w - m, h - m)):
        if chart.register == "engine":
            out.append(f'<path class="fc-corner" d="M{cx0 + sx * 3:.1f} {cy0 + sy * 17:.1f} '
                       f'V{cy0 + sy * 9:.1f} H{cx0 + sx * 9:.1f} V{cy0 + sy * 3:.1f} '
                       f'H{cx0 + sx * 17:.1f}"/>')
        else:
            out.append(f'<path class="fc-corner" d="M{cx0 + sx * 3:.1f} {cy0 + sy * 19:.1f} '
                       f'Q{cx0 + sx * 3:.1f} {cy0 + sy * 3:.1f} {cx0 + sx * 19:.1f} {cy0 + sy * 3:.1f}"/>')
    # Title block, bottom rule: plate numeral, subject, stage.
    base = h - m - 13
    out.append(f'<line class="fc-hairline" x1="{m + 14:.1f}" y1="{base - 15:.1f}" '
               f'x2="{w - m - 14:.1f}" y2="{base - 15:.1f}"/>')
    out.append(f'<text class="fc-plate" x="{m + 16:.1f}" y="{base:.1f}">'
               f'{esc(chart.title.upper())} &#183; PLATE {chart.plate}</text>')
    out.append(f'<text class="fc-stage" x="{w - m - 16:.1f}" y="{base:.1f}" text-anchor="end">'
               f'{esc(chart.stage.upper())}</text>')
    return "\n".join(out)


def render(chart: Chart) -> str:
    geo = layout(chart)
    pad_x, pad_top, pad_bottom = 34.0, 34.0, 56.0   # room for the title block
    w = geo["w"] + pad_x * 2
    h = geo["h"] + pad_top + pad_bottom
    shift_x, shift_y = pad_x, pad_top

    body = [draw_frame(chart, w, h), f'<g transform="translate({shift_x:.1f} {shift_y:.1f})">']
    for i, edge in enumerate(chart.edges):
        pts = geo["splines"].get((edge.src, edge.dst), [])
        body.append(draw_edge(pts, edge.label, chart.register, i))
    for node in chart.nodes:
        body.append(draw_node(node, geo["pos"][node.id], geo["sizes"][node.id], chart.register))
    body.append("</g>")

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
            f'class="flowplate flowplate--{chart.register}" role="img" '
            f'aria-label="{esc(chart.title)} flowchart, {esc(chart.stage)}">\n'
            + "\n".join(body) + "\n</svg>\n")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for chart in CHARTS:
        svg = render(chart)
        (OUT_DIR / f"{chart.key}.svg").write_text(svg)
        print(f"  {chart.key}.svg  ({len(svg)} bytes)")
    print(f"{len(CHARTS)} plates written to {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
