"""
forge_tools.py - what the conversion scripts share (md2pptx, md2docx):
finding an external tool on PATH, resolving paths, running a tool, the
headless Claude Code run. Not a command.

WHAT THE CONVERSIONS NEED (the one owner of this text)
    Every tool is resolved from PATH and never installed by a script
    (CLAUDE.md, Persistence, Portability); the model of the claude
    engine is told to install and download nothing as well.

    pandoc, the engine of /render: install it yourself, one-off, from
    https://pandoc.org/installing.html (Windows: winget install
    JohnMacFarlane.Pandoc; macOS: brew install pandoc; Linux: your
    package manager).

    The claude engine, behind /publish: the `claude` CLI on PATH and
    the official document skill of the format, pptx or docx, under
    either of its names - anthropic-skills:<format> where Claude Code
    brings it, document-skills:<format> where the plugin does. Where
    neither is there, install the plugin yourself, one-off, from an
    interactive Claude Code session:
        /plugin marketplace add anthropics/skills
        /plugin install document-skills@anthropic-agent-skills
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def say(text, colour=None):
    colours = {"red": "31", "green": "32", "yellow": "33", "cyan": "36", "grey": "90"}
    if colour and sys.stdout.isatty() and os.environ.get("NO_COLOR") is None:
        print(f"\033[{colours[colour]}m{text}\033[0m")
    else:
        print(text)


def fail(text):
    say(f"ERROR: {text}", "red")
    sys.exit(1)


def tool(name, hint):
    """The path of an external tool on PATH, or fail with `hint`."""
    p = shutil.which(name)
    if not p:
        fail(hint)
    return p


def existing(path, what, suffixes=None):
    """Resolve `path`, which must exist and, when `suffixes` is given,
    carry one of them."""
    p = Path(path)
    if not p.exists():
        fail(f"{what} '{path}' not found.")
    if suffixes and p.suffix.lower() not in suffixes:
        fail(f"{what} '{path}' is not a {' or '.join(suffixes)} file.")
    return p.resolve()


def run(cmd, cwd=None):
    """Run a tool, streaming its output; returns the exit code."""
    return subprocess.run(cmd, cwd=cwd).returncode


def size_kb(path):
    return round(Path(path).stat().st_size / 1024)


def claude_headless(prompt, model):
    """Run Claude Code non-interactively with the prompt, on the model,
    with the tools a document skill needs. Returns the exit code."""
    exe = tool("claude", "claude CLI not found on PATH - the claude engine runs on headless Claude Code.")
    return run([exe, "-p", prompt, "--model", model,
                "--allowedTools", "Skill,Read,Write,Edit,Bash,Glob,Grep"])
