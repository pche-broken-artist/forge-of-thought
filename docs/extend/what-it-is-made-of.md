---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: c43785f6dafe5169
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Persistence (git)
  - tmp/README.md
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/40-solution-design.md#The instruction layer
  - projects/forge/40-solution-design.md#The commands
  - projects/forge/40-solution-design.md#SOL.0300
  - projects/forge/40-solution-design.md#SOL.0330
  - projects/forge/40-solution-design.md#Across the parts
  - .claude/settings.json
---

# What the forge is made of

The forge is not a program but a set of instruction files that
Claude Code reads, with the deterministic work kept at the edge in
scripts. This page is for you, the extender: before you change any
of it, you need to know which files make up that operating layer,
what each one is, and at what moment the harness (Claude Code, the
program that runs Claude and reads these files) loads it. The table
below gives the files, one line gives the flow through them, and the
ideas that carry the layer follow. Every term of the forge is in one
line in the [Glossary](../reference/glossary.md).

## When to use it

Use this page when you are about to add or change something in the
forge and want to find the file that owns it, or when you want to
know why a change in one file is read by Claude at one moment and
not at another. The full directory listing, every project file
included, is the [Repository layout](../reference/repository-layout.md).
How a change is then recorded and released is
[Make a change to the forge](how-a-change-is-made.md).

## What you do

Find the kind of file you mean in the table. The third column says
when the harness reads it.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The always-on core: the roles, the prime directives, the working methods in short, the document kinds, the chain, the layout, persistence, versioning, the ID scheme, the reviewers, the ledger and the list of commands. A rule of one artefact is not here but in that artefact's definition. | Into every session and into every subagent. |
| `.claude/skills/<name>/SKILL.md` | One skill per command. The state files of `/forge` (`.claude/skills/forge/states/<state>.md`) and the genre files of `/recipe` (`.claude/skills/recipe/genres/<genre>.md`) are supporting files of their dispatcher: read by path, registered as nothing. Beside the commands stand the skills that are not commands: the three reviewer contracts (one per kind of reviewer), the documentation contract and the walkthrough skill. "Command" is the word for what you invoke by slash; "skill" names the file shape. | A command's body only when it is invoked. A supporting file when its dispatcher reads it. A contract injected whole into the agent that names it, at launch. The walkthrough skill whenever a walkthrough or an interview runs. |
| `.claude/agents/` | One file per critic lens, challenger persona and check, each carrying its front-matter and its Lens section and nothing else, the shared conduct being its contract's; and the documentation's planner and writer. Every agent declares `model: inherit`. | When a command launches the agent as an isolated subagent. |
| `.claude/settings.json` | The two hooks and the deny rules. The hooks: one at every prompt (`scripts/hook-walkthrough.py`) and one before every call of the shell tool `Bash` (`scripts/hook-git.py`), each started as `python` with the script path anchored at `${CLAUDE_PROJECT_DIR}`. The deny rules: reading two sensitive paths (`~/.ssh/**`, `~/.aws/**`) and running `git` in the other shell tool (`PowerShell(git *)`). | The per-prompt hook at every prompt. The git hook before every `Bash` call. The deny rules hold for the whole session. |
| `templates/` | The canonical skeletons for every new project and for every shape that has no other owner. A skeleton named `<type>-definition.md` is that of the definition of one member of a type the forge can be extended by: an artefact, a critic lens, a challenger persona, a check. The player page's skeleton, `templates/html-player.html`, is among them. The roster is [Templates](../reference/templates.md). | When a command makes a file from it. |
| `scripts/` | Python 3.8 or newer, run as `python scripts/<name>.py`, the only platform-bound layer, written to run unchanged on Linux and macOS. Each script carries its help in its module docstring. What several scripts share lives in one module beside them (`forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py`), never twice. The two hooks are scripts of this folder too. | When a command, a hook or you run one. They are never read as instructions. |
| `.gitattributes` | The engine's own ways of merging by path: its derived files at the root and under `projects/forge/`. | By git at a merge. |
| `tmp/` | The engine's working folder: the packets, envelopes and profiles of runs on another engine (`tmp/research/<run>/`), the tasks of a documentation run, a dry ledger, the manifest of a migration, a check's report before it is filed. The folder is in git with its own `README.md` and `.gitignore`; its contents never are. Nothing in it is a source of truth. A run is kept for inspection and deleted by hand, never by a script. | Written by the scripts and commands on the way to a result. Read by no check, no ledger and no history. |
| `projects/forge/` | The forge's own project, run through the forge's own process. It is the one project in the engine's repository: everything else under `projects/` is gitignored and a repository of its own. The documentation map, `docs-map.md`, lies beside its ledger. | When a command works on it, as on any project. |
| `docs/` | The generated documentation: pages of one topic each and their index, made by `/document` from the map. `docs/videos/` is the public folder of the projects' html-player files and the player page `index.html`, written by `md2video` from the player skeleton; it belongs to the videos, not to the documentation, and `/document` leaves it alone. `docs/.nojekyll` keeps GitHub Pages from touching the folder. What a page and the map are is [The documentation](../about/the-documentation.md). | Written by `/document`. Read by `/man` when a question in free words is routed by the index. |

Two files beside these hold what differs per instance (one
installation) and are gitignored: the instance facts in
`CLAUDE.local.md` at the root, created from its template, and the
session model in `.claude/settings.local.json`. Neither is part of
the layer you change.

The flow in one line: a session opens with `CLAUDE.md`; every prompt
gets the hook's lines; a command you type reads its skill, which
reads its supporting files and templates by path, launches an agent
with its contract where it needs isolation and calls a script where
the work is deterministic; what results is written into the files of
a project, never into the conversation, and reaches git through the
scripts.

## What happens

Five ideas carry the layer. They say why each file is loaded when
it is, and why a change lands where it does.

1. One always-on core, and everything else read when its situation
   arises. `CLAUDE.md` is loaded into every session and every
   subagent (an isolated run of Claude that sees the files it is
   given and never the working conversation). A command, a
   definition, a contract or a template is a file read when it is
   invoked. What must hold through a long conversation is repeated
   by a hook at every prompt. The per-prompt hook prints the
   one-item rule of the walkthrough (the method by which a list of
   decisions is worked one item per message) with its verdict line,
   a pointer to the walkthrough skill, and four lines of conduct.
   Why the core is small and the rest on demand is
   [How the rules are held](../about/how-the-rules-are-held.md).

2. State lives in Markdown files of the project, never in the
   conversation and never in Claude's memory. A project is a
   directory: the artefacts of the chain, their history logs, the
   ledger (the one source of truth for state, made at read time), the
   records of the reviewers and the resources.

3. Isolation is bought with subagents. A reviewer, a check and a
   render each run in a subagent, all on the one session model. A
   reviewer's agent file carries only its front-matter and its Lens
   section; the shared conduct arrives as a contract skill, injected
   at launch. The contract opens by citing `CLAUDE.md`, Isolated
   reviewers, for what the contract owns and what the lens file
   owns. Because the contract lands after the agent's own text, the
   agent must know which yields.

4. Git, the conversion of documents and the hooks are scripts. The
   scripts are the door to a write of git; reading git directly is
   open. The git hook holds the line between the two: it denies every
   write and names the script to use. The few commands that finish
   the step of a conflict are the exception; the hook puts them to
   the principal (whoever's thinking is being forged) and runs them
   on his yes.

5. Every file has a way of merging, and the forge tells git which in
   `.gitattributes`. Composed text and the record files merge as
   text; a conflict in a record file keeps both tails. Derived state
   is made at read time and never kept in git, or made only on `main`
   and taken as ours at a merge. Immutable files never conflict.
   Where git leaves a conflict standing, Claude lays both sides out
   and the principal decides; the forge merges nothing itself.

Two more rules shape the files you will touch. A skeleton named
`<type>-definition.md` in `templates/` is the skeleton of a
definition, so that a new artefact, lens, persona or check starts
from a shape and not from a copy of a neighbour. And `tmp/` is one
folder in the engine rather than the system's temporary directory,
so that a run is traceable on the machine and a profile's deny rules
have one path to name; the price is a folder you empty by hand.

## What you have afterwards

You know the file that owns the thing you want to change and the
moment Claude reads it: the core for what must hold always, a skill
for what one command does, a supporting file for one state or one
genre, an agent file for what one reviewer hunts, a template for a
shape, a script for deterministic work. The change itself, its
record and its release are
[Make a change to the forge](how-a-change-is-made.md).

## A worked example

One command traced through the layer: a check run on a project with
the placeholder slug `my-project`.

```
/check light my-project
```

1. The session already holds `CLAUDE.md`, loaded when it opened. The
   prompt that carries the command passes through
   `scripts/hook-walkthrough.py`, which adds the one-item rule and
   the four lines of conduct.
2. Claude reads `.claude/skills/check/SKILL.md`, the skill of the
   command. Until now that file was not in context.
3. The skill launches `.claude/agents/check-light.md` as an isolated
   subagent. Its front-matter names `check-contract`, so the harness
   injects `.claude/skills/check-contract/SKILL.md` whole at launch;
   the agent carries `CLAUDE.md` as every subagent does. The agent
   file itself holds only its front-matter and its Lens section.
4. The agent reads the documents of `projects/my-project/` from disk
   in its own run, stays read-only and returns its report with the
   findings unnumbered. It sees nothing of your conversation.
5. The command gives the findings their IDs and files the report in
   the project's `reviews/`; `scripts/forge-report.py` completes the
   file name in place. A report on its way to being filed may lie in
   `tmp/` meanwhile; nothing reads it there. A run that finds nothing
   files nothing.
6. The findings are settled by walkthrough, one item per message, in
   the shape of `.claude/skills/walkthrough/SKILL.md`, read now
   because a walkthrough runs.
7. The write at the round's end lands in the project's files, and a
   save reaches git through `scripts/forge-save.py`. Had Claude typed
   a `git` write itself, `scripts/hook-git.py` would have denied it
   and named the script.

The files touched, in order: the core, a hook script, a skill, an
agent file with its contract skill, the project's documents, a
script, a method skill, a git script. Nothing was read that the
moment did not call for.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
