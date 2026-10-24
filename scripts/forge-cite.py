"""
forge-cite.py - verify the citations of a research note before it is
filed: every URL in the note is opened and its state reported, and an
arXiv abstract page is read for its title, which must match the words
the note gives the source. The one mitigation of fabricated citations
with a measured effect is to resolve the URL (research of 2026-10-24,
keeping the quality and currency of web sources, F5); this script does
that for the forge, so that nobody checks fourteen links by hand.

    python scripts/forge-cite.py <note.md | bundle-dir> [--timeout 20]
        [--out <report.md>]

WHAT IT DOES
    1. Reads the note, or every *.md of a bundle directory, and collects
       every http(s) URL with the line it stands on.
    2. Opens each URL once (GET, a browser-like User-Agent, redirects
       followed, the time limit per URL) and classifies it:
         ok            2xx
         dead          404, 410: the page is gone or never existed
         unverifiable  401, 403, 429, a timeout or a network error: the
                       page refused or did not answer; not wrong, said so
         mismatch      an arXiv abstract page whose title shares too few
                       words with the note's entry: the ID points to
                       another paper, the mark of a fabricated citation
    3. Prints one line per URL and a count, and writes the same as a
       Markdown report to --out when given (the run folder under tmp/
       is the place). Exit 0 when nothing is dead or mismatched, 1
       otherwise; 2 on a usage error.

WHAT IT DOES NOT DO
    It does not judge content, does not open paywalls, and does not
    check a quote against its page (the brief's later step). A 403 is
    the normal answer of a site that blocks bots and is never counted
    as a failure. Nothing is written into the note: the note is the
    agent's record; what the check finds goes into the synthesis
    (.claude/skills/research/SKILL.md, step 6).

EXAMPLES
    python scripts/forge-cite.py tmp/research/2026-10-24-trial/source-quality/antigravity.md
    python scripts/forge-cite.py projects/forge/research/2026-10-24-topic/ --out tmp/research/2026-10-24-topic/cite-report.md
"""

import argparse
import html
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from forge_tools import say, utf8_console  # noqa: E402

URL = re.compile(r"https?://[^\s<>\[\]\"'`]+")
TRAIL = ".,;:!?]}'\""
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 forge-cite")
STOP = {"the", "and", "for", "with", "from", "that", "this", "into", "over", "than",
        "when", "what", "how", "are", "its", "via", "not", "all", "our", "your", "their"}


ITEM = re.compile(r"^\s*(\d+\.|[-*])\s")


def urls_of(text):
    """[(url, entry)] in order of appearance, each URL once; the entry is
    the list item the URL stands in, joined over its wrapped lines (a
    source's title, author and date are on the lines above its URL), or
    the line alone outside a list."""
    seen, out = set(), []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for m in URL.finditer(line):
            u = m.group(0).rstrip(TRAIL)
            while u.endswith(")") and u.count(")") > u.count("("):
                u = u[:-1].rstrip(TRAIL)
            if u in seen:
                continue
            seen.add(u)
            start = i
            while start > 0 and not ITEM.match(lines[start]) and lines[start].strip() and not lines[start].startswith("#"):
                start -= 1
            end = i
            while end + 1 < len(lines) and lines[end + 1].strip() and not ITEM.match(lines[end + 1]) and not lines[end + 1].startswith("#"):
                end += 1
            out.append((u, " ".join(l.strip() for l in lines[start:end + 1])))
    return out


def fetch(url, timeout):
    """(status, body_or_None, error)"""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(200_000) if "arxiv.org/abs/" in url else None
            return r.status, body, None
    except urllib.error.HTTPError as e:
        return e.code, None, str(e.reason)
    except (urllib.error.URLError, socket.timeout, ValueError, OSError) as e:
        return None, None, str(getattr(e, "reason", e))


def arxiv_title(body):
    t = body.decode("utf-8", "replace")
    m = re.search(r'<meta\s+name="citation_title"\s+content="([^"]*)"', t)
    if not m:
        m = re.search(r"<title>\s*(?:\[[^\]]*\]\s*)?(.*?)\s*</title>", t, re.S)
    return html.unescape(m.group(1)).strip() if m else ""


def words(s):
    return {w for w in re.findall(r"[a-z0-9]{4,}", s.lower()) if w not in STOP}


def classify(url, line, timeout):
    status, body, err = fetch(url, timeout)
    if status is None:
        return "unverifiable", f"no answer: {err}"
    if status in (404, 410):
        return "dead", f"HTTP {status}"
    if status in (401, 403, 429):
        return "unverifiable", f"HTTP {status}"
    if status >= 400:
        return "dead", f"HTTP {status}"
    if body is not None:
        title = arxiv_title(body)
        tw, lw = words(title), words(line)
        if title and tw:
            share = len(tw & lw) / len(tw)
            if share < 0.4:
                return "mismatch", f'arXiv page is "{title[:90]}" ({int(share * 100)}% of its words in the note\'s line)'
            return "ok", f'arXiv title matches ({int(share * 100)}%)'
    return "ok", f"HTTP {status}"


def main():
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("target", help="a note, or a bundle directory")
    ap.add_argument("--timeout", type=int, default=20, help="seconds per URL; default 20")
    ap.add_argument("--out", help="write the report as Markdown here")
    a = ap.parse_args()

    t = Path(a.target)
    if t.is_dir():
        files = sorted(p for p in t.glob("*.md"))
    elif t.is_file():
        files = [t]
    else:
        say(f"ERROR: {t} not found.", "red")
        sys.exit(2)

    rows, counts = [], {"ok": 0, "dead": 0, "unverifiable": 0, "mismatch": 0}
    for f in files:
        for url, line in urls_of(f.read_text(encoding="utf-8", errors="replace")):
            state, detail = classify(url, line, a.timeout)
            counts[state] += 1
            rows.append((f.name, state, url, detail))
            colour = {"ok": "green", "dead": "red", "mismatch": "red", "unverifiable": "yellow"}[state]
            say(f"{state:12} {url}  ({detail})", colour)

    summary = ", ".join(f"{v} {k}" for k, v in counts.items())
    say(f"\n{len(rows)} URLs: {summary}", "cyan")
    if a.out:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# Citation check of {t}", "", f"{len(rows)} URLs: {summary}", "",
                 "| File | State | URL | Detail |", "|---|---|---|---|"]
        lines += [f"| {f} | {s} | {u} | {d.replace('|', '/')} |" for f, s, u, d in rows]
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        say(f"report written: {out}", "grey")
    sys.exit(1 if counts["dead"] or counts["mismatch"] else 0)


if __name__ == "__main__":
    main()
