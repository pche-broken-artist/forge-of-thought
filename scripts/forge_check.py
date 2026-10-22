"""
forge_check.py - what the mechanical checks of forge-check.py share:
a finding and its report in the shape of the check contract
(.claude/skills/check-contract/SKILL.md, Output), the front-matter
keys and the comment a template owns (templates/*.md), the comments
and the line numbers of a file, and the kinds of the versioned
documents. Not a command.

A check here raises on nothing: what a file does not give is a
finding or is left unread, named in the report (POS.1600).
"""

import re
from pathlib import Path

import forge_docs as fd
import forge_repos as fr

TEMPLATES = fr.ENGINE_ROOT / "templates"
SEVERITIES = ("high", "medium", "low")
COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
KEY_RE = re.compile(r"^\s*#?\s*([A-Za-z_][\w-]*):")
VERSION_RE = re.compile(r"^\d+\.\d+$")
STATUSES = ("draft", "approved", "superseded")


class Finding:
    """One finding: severity, headline, the places (file:line), the
    rule with its owner, the fix; immediate when pure bookkeeping."""

    def __init__(self, severity, headline, where, rule, fix, immediate=False):
        self.severity = severity
        self.headline = headline
        self.where = where if isinstance(where, list) else [where]
        self.rule = rule
        self.fix = fix
        self.immediate = immediate

    def markdown(self):
        fix = ("immediate fix: " if self.immediate else "") + self.fix
        return "\n".join([
            f"### {self.severity} — {self.headline}",
            f"- **Where:** {'; '.join(self.where)}",
            f"- **Rule:** {self.rule}",
            f"- **Fix:** {fix}",
        ])


def report(check, target, date, findings, left=(), facts=()):
    """The report in the contract's shape, the findings ranked by
    severity and otherwise in the order found; `left` names what the
    check leaves to reading, `facts` what it reports as a fact."""
    ranked = sorted(findings, key=lambda f: SEVERITIES.index(f.severity) if f.severity in SEVERITIES else 9)
    n = len(ranked)
    out = [f"# Check ({check}) — {target} — {date}", "",
           "conforms" if n == 0 else f"{n} finding" + ("" if n == 1 else "s"), "", "## Findings", ""]
    for f in ranked:
        out.append(f.markdown())
        out.append("")
    if facts:
        out += ["## Facts"] + [f"- {x}" for x in facts] + [""]
    if left:
        out += ["## Left to reading", "<!-- The clauses of the Lens this script does not verify; a",
                "model reads them, or nobody does: said here so that script and",
                "agent can be compared clause by clause. -->"] + [f"- {x}" for x in left] + [""]
    return "\n".join(out).rstrip("\n") + "\n"


# ------------------------------------------------------- templates

def template_text(name):
    p = TEMPLATES / f"{name}.md"
    return fd.read(p) if p.exists() else ""


def template_keys(name):
    """The front-matter keys a template owns, a commented-out key
    (`# output:`) among them as an optional one."""
    front, _ = fd.split_front(template_text(name))
    keys = []
    for line in front or []:
        m = KEY_RE.match(line)
        if m and m.group(1) not in keys:
            keys.append(m.group(1))
    return keys


def comments(text):
    """The HTML comments of a text, (line, normalised text) each."""
    out = []
    for m in COMMENT_RE.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        out.append((line, norm(m.group(1))))
    return out


def template_comment(name, nth=0):
    """The nth comment of a template, normalised; '' when absent."""
    cs = comments(template_text(name))
    return cs[nth][1] if len(cs) > nth else ""


def norm(text):
    return " ".join(text.split())


def front_keys(front):
    out = []
    for line in front or []:
        m = re.match(r"^([A-Za-z_][\w-]*):", line)
        if m:
            out.append(m.group(1))
    return out


def line_of(text, pattern, flags=0):
    """The 1-based line of the first match of `pattern`, 0 when none."""
    m = re.search(pattern, text, flags)
    return text.count("\n", 0, m.start()) + 1 if m else 0


def version_tuple(v):
    try:
        major, minor = v.split(".")
        return int(major), int(minor)
    except (ValueError, AttributeError):
        return None


def ids_in(text):
    return set(fd.ID_RE.findall(text))


def expand_ranges(text):
    """IDs of a text, a range `POS.0010 to POS.0030` or `POS.0010-POS.0030`
    expanded in tens."""
    found = ids_in(text)
    for m in re.finditer(r"\b([A-Z]{3})\.(\d{4,5})\s*(?:to|-|–|—)\s*(?:\1\.)?(\d{4,5})\b", text):
        prefix, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        for n in range(a, b + 1, 10):
            found.add(f"{prefix}.{n:04d}")
    return found


# -------------------------------------------- the versioned documents

def versioned_documents(proj):
    """(path, template name) of every versioned document of a project:
    the briefs, the artefacts of the chain, the recipes, the work
    specifications (CLAUDE.md, Versioning & status)."""
    proj = Path(proj)
    out = []
    for f in sorted(proj.glob("00-brief*.md")):
        if ".history." not in f.name:
            out.append((f, "brief"))
    for f in sorted(proj.glob("[0-9][0-9]-*.md")):
        if f.name.startswith("00-") or ".history." in f.name or ".threads." in f.name:
            continue
        state = re.sub(r"^\d\d-", "", f.stem)
        out.append((f, state if (TEMPLATES / f"{state}.md").exists() else "intent"))
    for f in sorted(proj.glob("recipes/*.md")):
        if ".history." not in f.name:
            out.append((f, "recipe"))
    for f in sorted(proj.glob("work/*.spec.md")):
        out.append((f, "work"))
    return out


def companion_of(path):
    return path.with_name(path.name[:-3] + ".history.md")


def rel(proj, path):
    try:
        return Path(path).resolve().relative_to(Path(proj).resolve()).as_posix()
    except ValueError:
        return Path(path).as_posix()
