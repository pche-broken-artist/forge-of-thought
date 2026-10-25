#!/usr/bin/env python3
"""
hook-walkthrough.py - UserPromptSubmit hook of the engine: repeats the
one-item walkthrough rule at every prompt (POS.1170).

WHAT IT DOES
    Claude Code runs this script on every user prompt (configured in
    .claude/settings.json) and adds its standard output to the context
    of that turn. It prints two lines on the walkthrough: the rule that
    must hold in a long conversation - the verdict line that closes
    every proposition included, since 2026-09-27 - and the pointer to
    the skill that holds the full shape. Since 2026-09-20 it also
    prints three lines of conduct: use the forge's scripts, explain
    and ask before running a command of one's own, and change nothing
    that was not agreed and approved, and since 2026-10-24 that every
    step needing consent is a proposition closed by the verdict line, a
    yes with a question in it being `q` (POS.0850; THR.0400 of the forge intent; the
    git half of the gate that enforces them is scripts/hook-git.py,
    the rest the thread's open matter).
    It reads nothing, writes nothing, takes no arguments, and is
    independent of the working directory: a hook runs in the
    session's current working directory, not the engine root, so
    .claude/settings.json invokes this script in exec form and hands
    it its own path through the ${CLAUDE_PROJECT_DIR} placeholder.

WHAT IT NEEDS
    Python 3.8 or newer on PATH as `python`. Nothing else.
"""

LINES = [
    "Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, "
    "close a proposition with '(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark', stop. "
    "A question from the principal keeps the item open: answer, then close it again.",
    "When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.",
    "Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. "
    "git: read directly, every write through scripts/forge-*.py (the hook denies the rest).",
    "Own commands: before running anything of your own that is not plain reading, say what it does "
    "and why, and wait for the principal's yes.",
    "Consent: write, run and change nothing that was not agreed and approved. "
    "A yes covers exactly what was asked, never its consequences.",
    "Decisions: every question that asks the principal to decide - a step that needs consent "
    "(a write, a run, a commit, a change of a setting), a choice between options, an either/or, "
    "whether to write - is one proposition with Claude's recommendation as what accept means, "
    "and ends with the verdict line; a yes that carries a question is q. Only a question for "
    "information Claude lacks ends with the question alone.",
]

if __name__ == "__main__":
    print("\n".join(LINES))
