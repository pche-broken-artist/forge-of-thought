"""
The conversions without their tool (projects/forge/00-brief-tests.md):
what pandoc, markitdown or the model return is not tested, only that
the script fails intelligibly when the tool is not there, naming it
and how to install it, before anything is made. The tool is taken
away by an empty PATH; md2video is left out, since it reads a whole
screenplay before it looks for ffmpeg.
"""
import os
import sys


def without_tools(tmp_path):
    """An environment whose PATH holds nothing: no pandoc, no
    markitdown. The interpreter is run by its own absolute path."""
    empty = tmp_path / "empty-path"
    empty.mkdir(exist_ok=True)
    return {"PATH": str(empty)}


def test_md2pptx_with_pandoc_fails_naming_pandoc(tmp_path, run_script):
    md = tmp_path / "deck.md"
    md.write_text("# A deck\n\n## One slide\n\n- a point\n", encoding="utf-8")
    r = run_script("md2pptx", md, "--engine", "pandoc", env=without_tools(tmp_path))
    assert r.returncode != 0
    assert "pandoc not found" in r.stdout + r.stderr and "pandoc.org" in r.stdout + r.stderr
    assert not md.with_suffix(".pptx").exists()


def test_md2docx_with_pandoc_fails_naming_pandoc(tmp_path, run_script):
    md = tmp_path / "paper.md"
    md.write_text("# A paper\n\nA paragraph.\n", encoding="utf-8")
    r = run_script("md2docx", md, "--engine", "pandoc", env=without_tools(tmp_path))
    assert r.returncode != 0
    assert "pandoc not found" in r.stdout + r.stderr
    assert not md.with_suffix(".docx").exists()


def test_doc2md_fails_naming_markitdown_and_how_to_install_it(tmp_path, run_script):
    doc = tmp_path / "offer.docx"
    doc.write_bytes(b"PK\x03\x04 not really a document")
    r = run_script("doc2md", doc, env=without_tools(tmp_path))
    assert r.returncode != 0
    assert "markitdown not found" in r.stdout + r.stderr and "pip install" in r.stdout + r.stderr
    assert not doc.with_suffix(".md").exists()


def test_doc2md_list_tools_reports_the_tool_missing_without_failing(tmp_path, run_script):
    r = run_script("doc2md", "--list-tools", env=without_tools(tmp_path))
    assert r.returncode == 0
    assert "not found on PATH" in r.stdout
