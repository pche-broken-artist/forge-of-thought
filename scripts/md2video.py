#!/usr/bin/env python3
"""
md2video.py - make the format file of a screenplay render: a video, or
the timed events its player plays in the browser.

SYNOPSIS
    python scripts/md2video.py <render.md> --format video|html-player
        [--pace 4,8,16] [--date "28. 9. 2026"] [--section <name>]
        [--name <name>] [-o <file>] [--frame <seconds> <file.png>]

WHAT IT DOES
    Reads a screenplay render of the genre `screenplay` (CLAUDE.md,
    Document chain, Renders; the shape: templates/recipe-screenplay.md):
    the YAML front-matter for the language, a title card, a card of what
    the viewer will see, scenes with the real time of day, each with a
    caption of two parts (Now, Why) and a fenced block of what the
    terminal shows, and an end card. Computes the timeline from the
    pace - typing, the stand before Enter, the reveal of an answer, the
    hold for reading, the breath at a scene's end - and writes one of
    two formats, chosen by --format:

    video - every frame painted with Pillow as a simulated terminal
    (1280x890, a monospace font for the terminal, a sans font for the
    caption band) and piped into ffmpeg (H.264, 30 fps). Deterministic:
    the same file from the same render every time.

    html-player - the timeline as JSON of events for the player page of
    the engine, docs/videos/index.html, wrapped as a script
    (`forgeVideo({...})` in <name>.html-player.js) so that the page can
    load it by a script tag from a file on disk as well as from GitHub
    Pages, which forbid a page on disk to read a data file. Where the
    output lands under the engine's docs/videos/, the page is written
    anew from templates/html-player.html with the folder's files
    listed and loaded, since GitHub Pages cannot list a folder.

    The pace is three reading rates in words a second: the principal's
    lines, Claude's answers, the lines that only report a file (a path,
    a version, a ledger row); the default is 4,8,16. The pace, the date
    shown in the tab bar and the look come from the recipe's Format
    section, as arguments; the render carries none of it.

    The course on the player page comes from the recipe's Format the
    same way: --section names the section of the course the video
    belongs to, --name the name the list shows in the render's
    language, in place of the title card's title. Both go into the
    html-player file's data; the page groups the videos by section,
    sections and videos alike in the order of the file names, so the
    numbers of the recipe's `output:` order the course. A file without
    them is listed under its title, after the sections.

    The output lands next to the input with the render's basename
    (<name>.mp4 or <name>.html-player.js) unless -o names a path.
    --frame paints one frame of the video at the given second to a PNG
    and stops: a check of the look without the whole render.

WHAT IT NEEDS
    Python 3.8 or newer; `forge_tools.py` beside it. For video: Pillow
    (`pip install pillow`) and ffmpeg on PATH (https://ffmpeg.org;
    Windows: winget install Gyan.FFmpeg; macOS: brew install ffmpeg;
    Linux: your package manager). Fonts are taken from the system
    where they exist (Cascadia Mono or Consolas, Segoe UI; Menlo and
    Helvetica; DejaVu) and Pillow's built-in font otherwise. This script
    installs nothing.

EXAMPLES
    python scripts/md2video.py projects/acme/renders/first-steps.cs.md --format video --date "28. 9. 2026"
    python scripts/md2video.py projects/acme/renders/first-steps.cs.md --format html-player -o docs/videos/01-first-steps.cs.html-player.js
    python scripts/md2video.py projects/acme/renders/first-steps.en.md --format video --pace 4,8,16 --frame 75 check.png
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_tools as ft  # noqa: E402

ENGINE = Path(__file__).resolve().parent.parent
PLAYER_TEMPLATE = ENGINE / "templates" / "html-player.html"
PUBLIC_FOLDER = ENGINE / "docs" / "videos"

FPS = 30
W, H = 1280, 890
TAB_H, TERM_H = 36, 624
LINE_H = 26
PAD_X, PAD_Y = 18, 14
BG, FG, DIM, BOX, GREEN, TABBG, CAPBG, ACC = (
    "#0c0c0c", "#cccccc", "#767676", "#5a5a5a", "#13a10e", "#1f1f1f", "#161616", "#e0a85c")
SPIN = "✻✢✳✶✻✢"
TYPE_S, LINE_S, ENTER_S, THINK_S, GAP_S = 0.05, 0.22, 0.35, 0.8, 0.2
COLS = 96  # wrap width of the terminal in characters

LABELS = {"cs": {"Now": "Teď", "Why": "Proč"}, "en": {"Now": "Now", "Why": "Why"}}
# a line that only reports a file is skimmed: a path, a version, a ledger row
AUTO_RE = re.compile(r"[.]md\b|[.]py\b|ledger|řádek|řádků|verze|Zapsáno|Vytvořeno|tabulka|"
                     r"\brow\b|version|Written:|Created:|table")


# ---------------------------------------------------------------- parse
def parse(md):
    """The render as a list of parts: dict(kind='card'|'scene', title,
    time, caption=[(label, text)], steps=[(kind, arg)], text=[...]).
    Returns (lang, parts)."""
    lang = "en"
    fm = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    if fm:
        lm = re.search(r"^language:\s*(\w+)", fm.group(1), re.M)
        if lm:
            lang = lm.group(1)
        md = md[fm.end():]
    parts = []
    cur = None
    in_block = False
    block = []
    para = []

    def flush_para():
        if para and cur is not None and not in_block:
            cur["text"].append(" ".join(para))
        para.clear()

    for raw in md.splitlines():
        line = raw.rstrip("\n")
        if in_block:
            if line.startswith("```"):
                in_block = False
                cur["steps"] += block_to_steps(block)
                block = []
            else:
                block.append(line)
            continue
        m = re.match(r"^## (.+?)(?: \((\d+) s\))?$", line)
        if m:
            flush_para()
            title = m.group(1)
            sm = re.match(r"^(?:Scéna|Scene) (\d+) — (\d\d:\d\d) — (.+)$", title)
            if sm:
                cur = dict(kind="scene", no=int(sm.group(1)), time=sm.group(2), title=sm.group(3),
                           caption=[], steps=[], text=[])
            else:
                cur = dict(kind="card", title=title, caption=[], steps=[], text=[])
            parts.append(cur)
            continue
        if line.startswith("```"):
            flush_para()
            in_block = True
            continue
        if cur is None:
            continue
        cm = re.match(r"^\*\*(Teď|Proč|Now|Why):\*\* (.*)$", line)
        if cm:
            flush_para()
            cur["caption"].append([cm.group(1), cm.group(2)])
            continue
        if cur["caption"] and line and not line.startswith((" ", "**")) and cur["kind"] == "scene" and not para:
            cur["caption"][-1][1] += " " + line.strip()  # continuation of the caption
            continue
        if line.strip():
            para.append(line.strip())
        else:
            flush_para()
    flush_para()
    labels = LABELS.get(lang, LABELS["en"])
    for s in parts:
        s["caption"] = [(labels.get(lb, lb), re.sub(r"[`*]", "", t)) for lb, t in s["caption"]]
        if s["kind"] == "card" and s["text"]:
            m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", s["text"][0])
            if m:
                s["title"] = m.group(1).rstrip(".")
                s["text"][0] = m.group(2)
            s["text"] = [re.sub(r"[`*]", "", p) for p in s["text"] if p.strip()]
    return lang, parts


def block_to_steps(lines):
    """A fenced terminal block as steps: type (the principal's line),
    think, say (Claude's answer, wrapped), tool, hold."""
    steps = []
    say = []
    i = 0

    def flush_say():
        if say:
            steps.append(("say", wrap_lines(say)))
            say.clear()

    while i < len(lines):
        line = lines[i]
        if line.startswith("> "):
            flush_say()
            text = line[2:]
            while i + 1 < len(lines) and lines[i + 1].startswith("  ") and not lines[i + 1].startswith("  ·"):
                i += 1
                text += " " + lines[i].strip()
            steps.append(("type", text))
            steps.append(("think", THINK_S))
        elif line.startswith("  · "):
            flush_say()
            steps.append(("tool", line[4:]))
        elif line.strip() == "":
            # a blank line inside Claude's answer stays in the answer;
            # before a user or tool line it ends it
            nxt = next((ln for ln in lines[i + 1:] if ln.strip()), "")
            if say and nxt and not nxt.startswith(("> ", "  · ")):
                say.append("")
            else:
                flush_say()
                steps.append(("hold", GAP_S))
        else:
            say.append(line)
        i += 1
    flush_say()
    return steps


def wrap_lines(lines):
    out = []
    for line in lines:
        indent = len(line) - len(line.lstrip(" "))
        cur = " " * indent
        for w in line.strip().split(" "):
            if len(cur) + len(w) + 1 > COLS and cur.strip():
                out.append(cur)
                cur = " " * (indent + 2) + w
            else:
                cur = (cur + " " + w) if cur.strip() else cur + w
        out.append(cur)
    return out


LIST_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)]|[a-z][.)])\s")


def paragraphs(lines):
    """Hard-wrapped terminal lines regrouped into paragraphs the browser
    reflows: a blank line ends one, a list item or a heading starts one,
    a table row stays a line of its own. Each carries the number of
    lines it was, for the reveal."""
    out = []
    cur = []

    def flush():
        if cur:
            out.append(dict(t=" ".join(x.strip() for x in cur), n=len(cur), pre=cur[0].lstrip().startswith("|")))
            cur.clear()

    for ln in lines:
        st = ln.strip()
        if not st:
            flush()
            continue
        if LIST_RE.match(ln) or st.startswith(("#", "|")) or (cur and cur[0].lstrip().startswith("|")):
            flush()
        cur.append(ln)
    flush()
    return out


# ------------------------------------------------------------- timeline
# The viewer owes reading time for every text that appears (a caption,
# the principal's line, Claude's answer); the animation pays part of it
# off, and a hold is put only where a debt remains and a pause is
# natural: before Enter, after an answer, at the end of a scene. Nothing
# waits where there is nothing to read.
class Pace:
    def __init__(self, user, claude, auto):
        self.user, self.claude, self.auto, self.cap = user, claude, auto, claude

    def say_time(self, lines):
        return sum(len(ln.split()) / (self.auto if AUTO_RE.search(ln) else self.claude) for ln in lines)


def nwords(text):
    return len(text.split())


def minutes(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def events(parts, pace):
    """The screenplay as timed events, the one timeline of both formats."""
    out = []
    debt = 0.0
    prev_clock = None
    for s in parts:
        if s["kind"] == "card":
            words = sum(nwords(p) for p in s["text"])
            out.append(dict(k="card", title=s["title"], text=s["text"], dur=max(4.0, 2 + words / pace.cap)))
            prev_clock = None
            debt = 0.0
            continue
        # a scene within a quarter of an hour of the previous one keeps the screen
        clear = prev_clock is None or minutes(s["time"]) - minutes(prev_clock) > 15
        prev_clock = s["time"]
        debt = max(debt, 0.0) + sum(nwords(x[1]) for x in s["caption"]) / pace.cap
        out.append(dict(k="scene", no=s["no"], time=s["time"], title=s["title"], caption=s["caption"],
                        clear=clear, dur=0.8))
        debt -= 0.8
        for kind, arg in s["steps"]:
            if kind == "hold":
                out.append(dict(k="hold", dur=arg))
                debt -= arg
            elif kind == "type":
                speed = min(TYPE_S, 3.5 / max(len(arg), 1))  # a long line in 3.5 s at most
                typing = speed * len(arg)
                debt += nwords(arg) / pace.user - typing
                hold = min(max(debt, ENTER_S), 8.0)  # the line stands before Enter for what reading still needs
                debt -= hold
                out.append(dict(k="type", text=arg, typing=typing, hold=hold))
            elif kind == "think":
                out.append(dict(k="think", dur=arg))
                debt -= arg
            elif kind == "say":
                debt = max(debt, 0.0) + pace.say_time(arg) - len(arg) * LINE_S
                hold = min(max(debt, 0.6), 16.0)  # the answer stands for what reading still needs
                debt -= hold
                out.append(dict(k="say", lines=arg, paras=paragraphs(arg), line=LINE_S, hold=hold))
            elif kind == "tool":
                out.append(dict(k="tool", text=arg, line=LINE_S))
                debt -= 2 * LINE_S
        out.append(dict(k="end", dur=min(max(debt, 0.0), 6.0) + 1.0))  # what is unread, then a breath
        debt = 0.0
    return out


def duration(ev):
    t = 0.0
    for e in ev:
        if e["k"] == "type":
            t += e["typing"] + e["hold"] + ENTER_S
        elif e["k"] == "say":
            t += len(e["lines"]) * e["line"] + e["hold"]
        elif e["k"] == "tool":
            t += 2 * e["line"]
        else:
            t += e["dur"]
    return t


def frames(ev):
    """The events as (t_start, frame_spec) for the painter: ('card',
    title, text, start, duration) or ('term', conv, input, spinner, caption, time)."""
    t = 0.0
    out = []
    conv = []
    cap = []
    clock = ""

    def push(spec, dur):
        nonlocal t
        out.append((t, spec))
        t += dur

    def term(inp="", spin=None):
        return ("term", list(conv), inp, spin, cap, clock)

    for e in ev:
        k = e["k"]
        if k == "card":
            push(("card", e["title"], e["text"], t, e["dur"]), e["dur"])
            conv = []
        elif k == "scene":
            if e["clear"]:
                conv = []
            cap, clock = e["caption"], e["time"]
            push(term(), e["dur"])
        elif k in ("hold", "end"):
            push(term(), e["dur"])
        elif k == "type":
            speed = e["typing"] / max(len(e["text"]), 1)
            for i in range(1, len(e["text"]) + 1):
                push(term(e["text"][:i]), speed)
            push(term(e["text"]), e["hold"])
            for wl in wrap_lines(["> " + e["text"]]):
                conv.append((wl, DIM))
            conv.append(("", FG))
            push(term(), ENTER_S)
        elif k == "think":
            for i in range(int(e["dur"] / 0.12)):
                push(term(spin=SPIN[i % len(SPIN)] + " Thinking…"), 0.12)
        elif k == "say":
            for i, line in enumerate(e["lines"]):
                conv.append((("⏺ " + line.lstrip(" ")) if i == 0 else ("  " + line), FG))
                push(term(), e["line"])
            conv.append(("", FG))
            push(term(), e["hold"])
        elif k == "tool":
            conv.append(("⏺ " + e["text"], FG))
            push(term(), e["line"])
            conv.append(("  ⎿  ok", DIM))
            push(term(), e["line"])
            conv.append(("", FG))
    return out, t


# ---------------------------------------------------------------- paint
FONT_CANDIDATES = {
    "mono": ["CascadiaMono.ttf", "consola.ttf", "/System/Library/Fonts/Menlo.ttc",
             "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", "DejaVuSansMono.ttf"],
    "sans": ["segoeui.ttf", "/System/Library/Fonts/Helvetica.ttc",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"],
    "sansb": ["segoeuib.ttf", "/System/Library/Fonts/Helvetica.ttc",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "DejaVuSans-Bold.ttf"],
}


def font(kind, size, ImageFont):
    """A system font of the kind, or Pillow's built-in one."""
    for name in FONT_CANDIDATES[kind]:
        for p in (Path(name), Path("C:/Windows/Fonts") / name):
            try:
                return ImageFont.truetype(str(p), size)
            except (OSError, ValueError):
                continue
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()


class Painter:
    def __init__(self, date):
        from PIL import Image, ImageDraw, ImageFont  # Pillow, for the video only
        self.Image, self.ImageDraw = Image, ImageDraw
        self.date = date
        self.MONO = font("mono", 19, ImageFont)
        self.CAP = font("sans", 22, ImageFont)
        self.CAPB = font("sansb", 22, ImageFont)
        self.CARD = font("sans", 30, ImageFont)
        self.CARDB = font("sansb", 44, ImageFont)

    @staticmethod
    def wrap(text, fnt, width, d):
        words = text.split()
        lines = []
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if d.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def paint(self, spec, t):
        img = self.Image.new("RGB", (W, H), BG)
        d = self.ImageDraw.Draw(img)
        if spec[0] == "card":
            _, title, text, t0, dur = spec
            y = 220
            for line in self.wrap(title, self.CARDB, W - 200, d):
                d.text(((W - d.textlength(line, font=self.CARDB)) / 2, y), line, font=self.CARDB, fill="#f0f0f0")
                y += 56
            y += 20
            for para in text:
                for line in self.wrap(para, self.CARD, W - 240, d):
                    d.text(((W - d.textlength(line, font=self.CARD)) / 2, y), line, font=self.CARD, fill="#bdbdbd")
                    y += 40
                y += 14
            # a card is still: a thin line runs along its bottom for as long as it stands
            d.rectangle([0, H - 3, W * min(1.0, (t - t0) / max(dur, 0.01)), H], fill=ACC)
            return img
        _, conv, inp, spin, cap, clock = spec
        MONO = self.MONO
        cw = int(d.textlength("M", font=MONO))
        d.rectangle([0, 0, W, TAB_H], fill=TABBG)
        d.rectangle([8, 4, 220, TAB_H], fill=BG)
        d.text((22, 8), "⌂  PowerShell", font=MONO, fill=FG)
        d.text((W - 110, 8), "—   ☐   ✕", font=MONO, fill=DIM)
        stamp = (self.date + "  " if self.date else "") + clock
        d.text((W - 130 - d.textlength(stamp, font=MONO), 8), stamp, font=MONO, fill=DIM)
        cols = (W - 2 * PAD_X) // cw
        inner = cols - 6
        inp_lines = [""]
        for w in inp.split(" "):  # the prompt wraps by words, as a terminal does
            cand = (inp_lines[-1] + " " + w) if inp_lines[-1] else w
            if len(cand) <= inner or not inp_lines[-1]:
                inp_lines[-1] = cand
            else:
                inp_lines.append(w)
        box_rows, status_rows = 2 + len(inp_lines), 1
        rows_avail = (TERM_H - 2 * PAD_Y) // LINE_H - box_rows - status_rows - 1
        visible = conv[-rows_avail:] if len(conv) > rows_avail else conv
        y = TAB_H + PAD_Y
        for text, col in visible:
            if text.startswith("⏺"):
                cx, cy0 = PAD_X + cw // 2, y + LINE_H // 2 - 1
                d.ellipse([cx - 5, cy0 - 5, cx + 5, cy0 + 5], fill=GREEN)
                d.text((PAD_X, y), "  " + text[2:], font=MONO, fill=col)
            elif text.startswith("  ⎿"):
                x0 = PAD_X + 2 * cw + cw // 2
                d.line([x0, y + 2, x0, y + LINE_H // 2 + 2], fill=col, width=2)
                d.line([x0, y + LINE_H // 2 + 2, x0 + cw, y + LINE_H // 2 + 2], fill=col, width=2)
                d.text((PAD_X, y), "   " + text[3:], font=MONO, fill=col)
            else:
                d.text((PAD_X, y), text, font=MONO, fill=col)
            y += LINE_H
        if spin:
            d.text((PAD_X, y), spin, font=MONO, fill=ACC)
        by = TAB_H + TERM_H - PAD_Y - (box_rows + status_rows) * LINE_H
        d.text((PAD_X, by), "╭" + "─" * (cols - 2) + "╮", font=MONO, fill=BOX)
        cursor = "▌" if int(t * 2) % 2 == 0 and not inp else ""
        for k, seg in enumerate(inp_lines):
            yy = by + (k + 1) * LINE_H
            d.text((PAD_X, yy), "│", font=MONO, fill=BOX)
            d.text((PAD_X + (cols - 1) * cw, yy), "│", font=MONO, fill=BOX)
            prefix = "> " if k == 0 else "  "
            tail = cursor if k == len(inp_lines) - 1 else ""
            d.text((PAD_X + 2 * cw, yy), prefix + seg + tail, font=MONO, fill=FG)
        d.text((PAD_X, by + (len(inp_lines) + 1) * LINE_H), "╰" + "─" * (cols - 2) + "╯", font=MONO, fill=BOX)
        d.text((PAD_X + 2 * cw, by + (len(inp_lines) + 2) * LINE_H), "? for shortcuts", font=MONO, fill=DIM)
        cy = TAB_H + TERM_H
        d.rectangle([0, cy, W, H], fill=CAPBG)
        d.line([0, cy, W, cy], fill="#2a2a2a", width=2)
        y = cy + 16
        for label, text in cap:
            lw = d.textlength(label + ":  ", font=self.CAPB)
            d.text((40, y), label + ":", font=self.CAPB, fill=ACC)
            for line in self.wrap(text, self.CAP, W - 80 - lw, d):
                d.text((40 + lw, y), line, font=self.CAP, fill="#e6e6e6")
                y += 31
            y += 2
        return img


# --------------------------------------------------------------- outputs
def write_video(ev, out, date):
    ffmpeg = ft.tool("ffmpeg", "ffmpeg not found on PATH - install it from https://ffmpeg.org.")
    try:
        painter = Painter(date)
    except ImportError:
        ft.fail("Pillow not found - install it with `pip install pillow`.")
    fr, total = frames(ev)
    n = int(total * FPS)
    ft.say(f"{n} frames, {total:.1f} s", "grey")
    ff = subprocess.Popen([ffmpeg, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    k = 0
    last = None
    cache = None
    for i in range(n):
        t = i / FPS
        while k + 1 < len(fr) and fr[k + 1][0] <= t:
            k += 1
        key = (k, int(t * 2) % 2)
        if key != last:
            cache = painter.paint(fr[k][1], t).tobytes()
            last = key
        ff.stdin.write(cache)
    ff.stdin.close()
    if ff.wait() != 0:
        ft.fail("ffmpeg failed.")


def write_frame(ev, at, png, date):
    try:
        painter = Painter(date)
    except ImportError:
        ft.fail("Pillow not found - install it with `pip install pillow`.")
    fr, total = frames(ev)
    k = max(j for j, (ts, _) in enumerate(fr) if ts <= at)
    painter.paint(fr[k][1], at).save(png)
    ft.say(f"frame at {at:.1f} s of {total:.1f} -> {png}")


def write_player_js(ev, out, lang, title, date, pace, section="", name=""):
    """The events as a script the player page loads by a script tag:
    one call of forgeVideo with the data, the file's own name inside;
    the section and the name of the course where the recipe gives them."""
    data = dict(file=out.name, lang=lang, title=title, section=section, name=name,
                date=date, pace=[pace.user, pace.claude, pace.auto],
                duration=round(duration(ev), 1),
                events=[{k: v for k, v in e.items() if k != "lines"} for e in ev])
    out.write_text("forgeVideo(" + json.dumps(data, ensure_ascii=False) + ");\n", encoding="utf-8")


def renew_player_page(folder):
    """docs/videos/index.html written anew from the template with the
    folder's html-player files listed in the order of their names."""
    if not PLAYER_TEMPLATE.exists():
        ft.fail(f"the player's template {PLAYER_TEMPLATE} is missing.")
    files = sorted(p.name for p in folder.glob("*.html-player.js"))
    tags = "\n".join(f'<script src="{f}"></script>' for f in files)
    page = (PLAYER_TEMPLATE.read_text(encoding="utf-8")
            .replace("/*FILES*/", json.dumps(files, ensure_ascii=False))
            .replace("<!--SCRIPTS-->", tags))
    (folder / "index.html").write_text(page, encoding="utf-8")
    ft.say(f"player page renewed with {len(files)} file(s): {folder / 'index.html'}", "grey")


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("md", help="the screenplay render")
    ap.add_argument("--format", choices=["video", "html-player"], required=True,
                    help="video: an MP4 of the simulated terminal; html-player: the timed events for docs/videos/index.html")
    ap.add_argument("--pace", default="4,8,16",
                    help="reading rates in words a second: the principal's lines, Claude's answers, file reports (default 4,8,16)")
    ap.add_argument("--date", default="", help="the date shown in the tab bar beside the scene's time, e.g. \"28. 9. 2026\"")
    ap.add_argument("--section", default="", help="html-player: the section of the course on the player page, e.g. \"Tutorial\"")
    ap.add_argument("--name", default="", help="html-player: the name the player page lists, in the render's language (default: the title card's title)")
    ap.add_argument("-o", "--out", help="output file (default: next to the input, the render's basename)")
    ap.add_argument("--frame", nargs=2, metavar=("SECONDS", "PNG"), help="paint one frame of the video and stop")
    a = ap.parse_args(argv)

    md = ft.existing(a.md, "Input")
    try:
        rates = [float(x) for x in a.pace.split(",")]
        assert len(rates) == 3
    except (ValueError, AssertionError):
        ft.fail("--pace takes three numbers, e.g. 4,8,16.")
    pace = Pace(*rates)
    text = md.read_text(encoding="utf-8")
    lang, parts = parse(text)
    if not parts:
        ft.fail(f"{md} has no cards or scenes of a screenplay.")
    title = next((ln[2:] for ln in text.splitlines() if ln.startswith("# ")), md.stem)
    title = re.sub(r" — (screenplay|scénář)$", "", title)
    ev = events(parts, pace)
    ft.say(f"{len(parts)} parts, {len(ev)} events, {duration(ev):.0f} s, language {lang}", "grey")

    if a.frame:
        write_frame(ev, float(a.frame[0]), a.frame[1], a.date)
        return 0
    base = re.sub(r"\.md$", "", md.name)
    if a.format == "video":
        out = Path(a.out).resolve() if a.out else md.with_name(base + ".mp4")
        out.parent.mkdir(parents=True, exist_ok=True)
        write_video(ev, out, a.date)
    else:
        out = Path(a.out).resolve() if a.out else md.with_name(base + ".html-player.js")
        out.parent.mkdir(parents=True, exist_ok=True)
        write_player_js(ev, out, lang, title, a.date, pace, a.section, a.name)
        if out.parent.resolve() == PUBLIC_FOLDER.resolve():
            renew_player_page(PUBLIC_FOLDER)
    ft.say(f"written {out} ({ft.size_kb(out)} kB)", "green")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
