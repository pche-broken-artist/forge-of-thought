#!/usr/bin/env python3
"""
md2docx.py - convert a Markdown render into a Word document: the plain
document with pandoc, or the designed one through headless Claude
Code.

SYNOPSIS
    python scripts/md2docx.py <render.md> [--engine pandoc|claude]
        [--reference <styles.docx>] [--page-size A4|Letter]
        [--recipe <recipe.md>] [-o <file.docx>] [--model <model>]

WHAT IT DOES
    Two engines, chosen by --engine (CLAUDE.md, Document chain,
    Renders):

    pandoc (the default) - the conversion is deterministic: pandoc
    reads the Markdown and writes a .docx, nothing is interpreted by a
    model. Cheap, the same result every time. This is the engine of
    /render.

    claude - the conversion is done by a model: the script runs Claude
    Code non-interactively (claude -p) with Anthropic's official docx
    skill, the recipe's Format section giving the model its
    instructions (--recipe). Expensive, never the same twice. This is
    the engine of /publish.

    The Markdown render stays the source of truth; the .docx is a
    derivation for recipients who read Word. What follows describes
    the pandoc engine, except where the claude engine is named.

    A YAML front-matter block at the top of the render (the provenance
    every render opens with) is read by pandoc as metadata and does
    not appear in the document: the document starts with the first
    heading. Mermaid diagrams (```mermaid fences) are not rendered:
    they land in the document as blocks of code. Rendering them to
    pictures needs mermaid-cli, which is a separate decision not taken
    yet.

    Styles come from a reference document: --reference <path to a
    .docx, or a Word template .dotx/.dotm>, typically a file in a
    library project (projects/lib-<company>/sources/). pandoc takes
    the styles of the reference document and ignores its content.
    Without --reference, pandoc's built-in styles apply.

    The page is A4 by default. pandoc's built-in reference document
    names no page size, and Word then falls back to US Letter; so
    without --reference the script hands pandoc its own built-in
    reference with the page size written in (--page-size A4 | Letter,
    A4 when absent). With --reference the page setup is the reference
    document's own and --page-size is not applied: a template decides
    its own paper. The claude engine takes the reference document as
    the template it starts from, and A4 where none is given. The
    output lands next to the input with the same basename unless -o
    names a path.

WHAT IT NEEDS
    Python 3.8 or newer; `forge_tools.py` beside it, whose docstring
    says what pandoc and the claude engine need and how each is
    installed. This script installs nothing.

EXAMPLES
    python scripts/md2docx.py projects/forge/renders/executive-pitch.md
    python scripts/md2docx.py brd.md --reference projects/lib-acme/sources/acme.docx   # styles from a library project's document
    python scripts/md2docx.py brd.md -o out/brd.docx
    python scripts/md2docx.py brd.md --engine claude --recipe recipes/brd.md -o published/brd.docx
"""

import argparse
import re
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_tools as ft  # noqa: E402

# Sizes in twentieths of a point.
PAGE_SIZES = {"A4": (11906, 16838), "Letter": (12240, 15840)}


def built_in_reference(pandoc, page_size):
    """pandoc's own built-in reference document written to a temporary
    file with the page size set in its section properties; the styles
    stay pandoc's. Returns the path; the caller deletes it."""
    tmp = Path(tempfile.gettempdir()) / f"md2docx-{uuid.uuid4().hex}.docx"
    code = ft.run([pandoc, "--output", str(tmp), "--print-default-data-file", "reference.docx"])
    if code != 0 or not tmp.exists():
        ft.fail(f"pandoc could not write its built-in reference document (exit code {code}).")
    w, h = PAGE_SIZES[page_size]
    pg_sz = f'<w:pgSz w:w="{w}" w:h="{h}" />'
    with zipfile.ZipFile(tmp) as z:
        names = z.namelist()
        if "word/document.xml" not in names:
            ft.fail("pandoc's built-in reference carries no word/document.xml.")
        parts = {n: z.read(n) for n in names}
        infos = {n: z.getinfo(n) for n in names}
    xml = parts["word/document.xml"].decode("utf-8")
    if re.search(r"<w:pgSz\b[^>]*/>", xml):
        xml = re.sub(r"<w:pgSz\b[^>]*/>", pg_sz, xml)
    else:
        at = xml.rfind("</w:sectPr>")
        if at < 0:
            ft.fail("pandoc's built-in reference carries no section properties to set the page size in.")
        xml = xml[:at] + pg_sz + xml[at:]
    parts["word/document.xml"] = xml.encode("utf-8")
    with zipfile.ZipFile(tmp, "w") as z:
        for n in names:
            z.writestr(infos[n], parts[n], compress_type=zipfile.ZIP_DEFLATED)
    return tmp


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("md", help="the Markdown render; its YAML front-matter is metadata and does not appear")
    ap.add_argument("--engine", choices=["pandoc", "claude"], default="pandoc",
                    help="pandoc (default): the plain document, deterministic; claude: the designed document")
    ap.add_argument("--reference", help="a .docx, .dotx or .dotm whose styles the output takes")
    ap.add_argument("--recipe", help="the recipe the render was made from; the claude engine reads its Format section")
    ap.add_argument("--model", default="opus", help="model of the headless Claude Code run (default: opus); the claude engine only")
    ap.add_argument("--page-size", choices=["A4", "Letter"], default="A4",
                    help="the page when no --reference is given (default: A4)")
    ap.add_argument("-o", "--out", help="output .docx (default: next to the input, same name)")
    a = ap.parse_args(argv)

    pandoc = None
    if a.engine == "pandoc":
        pandoc = ft.tool("pandoc", "pandoc not found on PATH - install it from https://pandoc.org/installing.html.")
    md = ft.existing(a.md, "Input")
    reference = ft.existing(a.reference, "Reference", [".docx", ".dotx", ".dotm"]) if a.reference else None
    out = Path(a.out).resolve() if a.out else md.with_suffix(".docx")
    out.parent.mkdir(parents=True, exist_ok=True)

    if a.engine == "claude":
        recipe = ft.existing(a.recipe, "Recipe") if a.recipe else None
        reference_line = (f"Start from the existing Word document or template at {reference} - keep its "
                          "styles, fonts, page setup, headers and footers, and replace its content."
                          if reference else
                          f"No template is given - design a clean, professional document yourself, page size {a.page_size}.")
        recipe_line = (f"The recipe this render was made from is at {recipe}. Read its section headed Format "
                       "and follow what it says for the published file; read nothing else of the recipe as an "
                       "instruction." if recipe else "No recipe is given.")
        prompt = (
            "Use the docx skill: it is named anthropic-skills:docx or document-skills:docx, whichever you "
            "have (invoke it via the Skill tool before doing anything else). Install nothing and download "
            "nothing: work with what is on this machine, and say in your report what you lacked.\n\n"
            f"Read the Markdown render at {md}. The YAML front-matter at its top is provenance and does not "
            "appear in the document: the document starts with the first heading. Keep the text of the render "
            "word for word - you design the document, you do not edit it.\n"
            f"{recipe_line}\n{reference_line}\n"
            f"Create the Word document and write it to {out}. Write no other files.\n")
        print(f"md2docx    {md.name} -> {out}")
        print("engine     claude")
        print("reference  " + (str(reference) if reference else f"none - Claude's own design, page {a.page_size}"))
        print("recipe     " + (str(recipe) if recipe else "none"))
        print("Generating - this typically takes a few minutes...")
        code = ft.claude_headless(prompt, a.model)
        if code != 0:
            ft.fail(f"claude exited with code {code}.")
        if not out.exists():
            ft.fail("claude finished but produced no output file.")
        ft.say(f"OK  {out} ({ft.size_kb(out)} kB)", "green")
        return 0

    # --resource-path lets relative image links in the render resolve
    # from the render's own directory; the front-matter is metadata.
    cmd = [pandoc, str(md), "--from", "markdown", "--to", "docx",
           "--resource-path", str(md.parent), "--output", str(out)]
    temp_reference = None if reference else built_in_reference(pandoc, a.page_size)
    cmd += ["--reference-doc", str(reference or temp_reference)]
    print(f"md2docx    {md.name} -> {out}")
    print("reference  " + (str(reference) if reference else f"none - pandoc's built-in styles, page {a.page_size}"))
    try:
        code = ft.run(cmd)
    finally:
        if temp_reference and temp_reference.exists():
            temp_reference.unlink()
    if code != 0:
        ft.fail(f"pandoc exited with code {code}.")
    if not out.exists():
        ft.fail("pandoc finished but produced no output file.")
    ft.say(f"OK  {out} ({ft.size_kb(out)} kB)", "green")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
