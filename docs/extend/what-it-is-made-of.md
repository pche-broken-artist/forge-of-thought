---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 0b60c31121f4ff3c
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Persistence (git)
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/40-solution-design.md#The instruction layer
  - projects/forge/40-solution-design.md#The commands
  - projects/forge/40-solution-design.md#The reviewers
  - projects/forge/40-solution-design.md#Across the parts
---

# What the forge is made of

The forge is a set of instruction files that Claude Code reads, with
the deterministic work kept at its edge in scripts; it is not a
program. This page is for you, the extender: it says which files make
up that operating layer, what each kind of file is and when the
harness (Claude Code, the program that runs Claude and reads these
files) loads it, so that you know which file to open before you
change anything. How a change is then made, recorded and released is
the page [Make a change to the forge](how-a-change-is-made.md). The
full layout block, every directory of the engine and of a project, is
the page [Repository layout](../reference/repository-layout.md); the
terms of the forge in one line each are the
[Glossary](../reference/glossary.md).

## When to use it

Use this page when you are about to change the forge and need to
know where the thing you want to change lives, or when a command
behaves in a way you do not expect and you want to know which file
the harness read to produce it.

## What you do

Find the row of the kind of file you are after. The path in that row
is where it lives, the third column says when the harness reads it,
and therefore when a change to it takes effect.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | the universal core: the roles, the prime directives, the working methods in short, the document kinds, the chain, the layout, persistence, versioning, the ID scheme, the reviewers, the ledger and the list of commands; a rule of one artefact is not here but in that artefact's definition | into every session and every subagent, always on |
| `.claude/skills/<name>/SKILL.md` | one skill per command; the state files of `/forge` (`.claude/skills/forge/states/<state>.md`, the definitions of the artefacts) and the genre files of `/recipe` (`.claude/skills/recipe/genres/<genre>.md`) are supporting files of their dispatcher, read by path and registered as nothing | when you invoke the command; a supporting file when the dispatcher reaches for it |
| `.claude/skills/<kind>-contract/SKILL.md`, `.claude/skills/walkthrough/SKILL.md` | the skills that are not commands: the three reviewer contracts (`critic-contract`, `challenger-contract`, `check-contract`), the contract of the documentation agents, and the walkthrough skill, which holds the shape of the walkthrough and of the elicitation interview | a contract is injected whole into the agent that names it in its front-matter, at the agent's launch; the walkthrough skill whenever a walkthrough or an interview runs |
| `.claude/agents/` | one file per critic lens, challenger persona and check (`critic-<lens>.md`, `challenger-<persona>.md`, `check-<name>.md`), each carrying its front-matter and its Lens section and nothing else, and the documentation's planner and writer; every agent declares `model: inherit` | when its command launches it as a subagent; the agent sees the files it is given and never the working conversation |
| `.claude/settings.json` | the engine's settings: the per-prompt hook that starts `scripts/hook-walkthrough.py`, and the deny rules that keep Claude from raw `git` | read by the harness; the hook runs at every prompt |
| `templates/` | the templates (the skeletons every new document starts from); `<type>-definition.md` is the template of the definition of one member of a type the forge is extended by (an artefact, a critic lens, a challenger persona, a check); `recipe-<genre>.md` the template of a recipe of that genre; `html-player.html` the template of the player page of the videos | when a document is made from one |
| `scripts/` | Python, 3.8 or newer, run as `python scripts/<name>.py`, each with its help in its module docstring; what several scripts share lives in one module beside them (`forge_repos.py` for the git scripts, `forge_tools.py` for the conversions, `docs_map.py` for the documentation scripts), never twice; the scripts are the only door to git | when a command calls one or when you run one by hand; the hook at every prompt |
| `projects/forge/` | the forge's own project: the one directory under `projects/` that the engine's repository tracks, every other project being a repository of its own which the engine does not know; it holds the intent and the solution design of the forge | never on its own; when a command names it by its slug, `forge` |
| `docs/` | the generated documentation: pages of one topic each and their index, made by `/document` from the map `docs-map.md` beside the owning project's ledger; `docs/videos/` is the public folder of the projects' player files and of the player page `index.html`, written by `md2video` from `templates/html-player.html`, and is not part of the documentation; `docs/.nojekyll` keeps GitHub Pages from touching it | never; it is read by people and overwritten by its generators |

Beside these the engine root holds the README, the release notes and
the contributing note, each a render made from a recipe, the licence
and the avatar: outputs and ornaments, not the operating layer. What
every template is for is the page
[Templates](../reference/templates.md); what `docs/` and its map
are is the page [The documentation](../about/the-documentation.md).

## What happens

The flow of loading, in one line:

```
session start -> CLAUDE.md | every prompt -> the hook | a command -> its skill -> the definition, template, agent (with its contract) or script the skill reaches for
```

Before a file is read, what the session holds of it is its
description alone. A command guarded against being started unasked
carries `disable-model-invocation: true` in its front-matter, and
its description leaves the always-on context too. A contract is
`user-invocable: false`, out of the `/` menu, and its description
stays in the session's context, saying that it is preloaded.

Four ideas carry the layer.

- One always-on core and everything else read when its situation
  arises. `CLAUDE.md` is loaded into every session and every
  subagent. A command, a definition, a contract or a template is a
  file read when it is invoked. What must hold through a long
  conversation is repeated by the hook at every prompt, because text
  loaded once is not trusted to hold.
- State lives in Markdown files of the project, never in the
  conversation and never in the assistant's memory. A project is a
  directory: the artefacts of the chain, their history logs, the
  ledger (the one file that says the state of a project), the
  records of the reviewers and the resources.
- Isolation is bought with subagents (a separate run of Claude that
  is given files and a task and sees nothing of the working
  conversation). A reviewer, a check and a render each run in one,
  all on the one session model.
- Git, the conversion of documents and the hook are scripts. The
  harness denies Claude raw `git`, so the scripts are the only door,
  reading state included.

The reason the core is small and the rest is read on demand is the
page [How the rules are held](../about/how-the-rules-are-held.md).

## What you have afterwards

You know the one file that owns the thing you want to change, and
when the harness will read it again: the core at the start of the
next session and of every subagent launched after the change, a
skill at its next invocation, a contract at the next launch of an
agent that names it, a template when the next document is made from
it, a script at its next run, the hook at the next prompt. The change
itself, its record and its release are the page
[Make a change to the forge](how-a-change-is-made.md).

## If something goes wrong

- A command shows the first line of its body as its description.
  Its `argument-hint` is unquoted: a front-matter with CRLF line
  endings and an unquoted hint of two bracketed items fails to
  parse. Every `argument-hint` is quoted.
- An agent runs without the rules of its contract. The skill its
  front-matter names does not exist, and a missing skill is skipped
  silently. The check `engine` verifies that every skill an agent
  names exists.
- The hook does not run from a session started in a subdirectory.
  Its command in `.claude/settings.json` is anchored at the project
  root in exec form, `python` with
  `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
  argument; a relative path would be resolved against the session's
  working directory, not the engine root.
- A script does not start. `python` on PATH is the one prerequisite
  of the scripts; a system that has only `python3` gives it that
  name. The external tools the scripts call (`git`, `markitdown`,
  `pandoc`, `claude`) are resolved from PATH too.

## A worked example

One command traced through the layer: `/save my-project`, which saves
one project.

1. You type `/save my-project`. The harness reads
   `.claude/skills/save/SKILL.md`, which until now was in the
   session only by its description. The core, `CLAUDE.md`, was
   loaded at session start. You should now see the skill begin its
   check.
2. The skill runs the check `light`. It launches
   `.claude/agents/check-light.md` as a subagent; at launch the
   harness injects whole the contract the agent's front-matter
   names, `.claude/skills/check-contract/SKILL.md`; the agent runs
   on the session model (`model: inherit`), reads the project's
   files from disk, never the conversation, and returns its report.
   The agent is read-only: the `/check` procedure in the session
   files the report word for word and gives the IDs, and a run that
   finds nothing files nothing. Where it found something, the
   findings are settled by walkthrough (one item per message, the
   principal, the person whose thinking is forged, giving a verdict
   on each), and `.claude/skills/walkthrough/SKILL.md` is read at
   that moment. You should now see either no report or a filed
   report with its findings offered one by one.
3. The skill commits and pushes through
   `python scripts/forge-save.py`. The script imports
   `forge_repos.py` beside it for the engine root, the git check,
   the list of repositories the slug names and the running of git.
   Claude cannot call `git` itself: the deny rules of
   `.claude/settings.json` forbid it, so the script is the one door.
   The script carries no URL and no identity; the commit identity is
   git's own configuration. You should now see a commit on whatever
   branch is checked out, pushed, and no render made.

A template is the one kind of file this run does not touch: a
template is read when a document is made from it, as when a project
is scaffolded, not when one is saved.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
