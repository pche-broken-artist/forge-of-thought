---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 62689c71fd5f5589
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Persistence (git)
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/40-solution-design.md#The instruction layer
  - projects/forge/40-solution-design.md#The commands
  - projects/forge/40-solution-design.md#SOL.0300
  - projects/forge/40-solution-design.md#SOL.0330
  - projects/forge/40-solution-design.md#Across the parts
---

# What the forge is made of

The forge is not a program. It is a set of instruction files that
Claude Code reads, with the deterministic work kept at its edge in
Python scripts. This page is for the extender: the person who wants
to change or add to the forge and first needs to know which file
holds what, and when Claude reads it.

## When to use it

Use this page before you change anything in the forge. It tells you
where a rule, a command or a shape lives, so that you change the one
file that owns it. How the change itself is made is described in
[Make a change to the forge](how-a-change-is-made.md).

## What you do

Find the kind of thing you want to change in the table, then open
the file at its path. Every path is relative to the root of the
engine (the one installed copy of the forge, which holds the
instructions and the projects).

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The universal core: the rules that must hold everywhere. | Always: in every session (one run of Claude Code) and in every subagent (an isolated helper run of Claude that sees only the files it is given). |
| `.claude/skills/<name>/SKILL.md` | One skill per command. | When the command is invoked. |
| `.claude/skills/forge/states/<state>.md` | The definitions of the artefacts, supporting files of `/forge`. | Read by path when `/forge <state>` runs. |
| `.claude/skills/recipe/genres/<genre>.md` | The genre interviews, supporting files of `/recipe`. | Read by path when `/recipe <genre>` runs. |
| `.claude/skills/<kind>-contract/SKILL.md` | Skills that are not commands: the three reviewer contracts (critic, challenger, check) and the documentation contract. | Preloaded into an agent when the agent is launched. |
| `.claude/skills/walkthrough/SKILL.md` | A skill that is not a command: the shape of a walkthrough and of the elicitation interview. | Whenever a walkthrough or an interview runs. |
| `.claude/agents/` | One file per critic lens, challenger persona and check, and the documentation's planner and writer. | When a command launches the agent. |
| `.claude/settings.json` | The two hooks and the deny rule of the other shell. | By Claude Code: the per-prompt hook at every prompt, the git hook before a tool is used. |
| `templates/` | The canonical skeletons, the skeleton of the video player page (`templates/html-player.html`) among them. | When a command makes a document from one. |
| `scripts/` | The Python scripts, the two hooks among them, with the modules they share beside them. | When a command or a hook runs one. |
| `.gitattributes` | The engine's own ways of merging by path, for its derived files at the root and under `projects/forge/`. | By git, at a merge. |
| `projects/forge/` | The forge's own project: the forge run through its own process. | When a command targets the project `forge`. |
| `docs/` | The generated documentation: pages of one topic each and their index. | Written by `/document`; read by people. |
| `docs/videos/` | The public folder of the projects' video player files and the player page; it does not belong to the documentation. | Written by `scripts/md2video.py`; left alone by `/document`. |

The full layout, with the files of a project, is in
[Repository layout](../reference/repository-layout.md). Every
skeleton is listed in [Templates](../reference/templates.md). A
skeleton named `<type>-definition.md` is the skeleton of the
definition of one member of a type the forge can be extended by:
an artefact, a critic lens, a challenger persona or a check.

## What happens

The layer works in one line of flow:

`CLAUDE.md` always loaded → a command typed → its skill read → the
skill reads the definitions and templates it needs, launches agents
that preload their contract, and runs scripts for git and the
conversions → the result written as Markdown files of the project.

Five ideas carry it. Keep them in mind when you decide where a
change goes.

1. One always-on core, and everything else read when its situation
   arises.
   `CLAUDE.md` is loaded into every session and every subagent.
   A command, a definition, a contract or a template is a file read
   when it is invoked.
   What must hold through a long conversation is repeated by a hook
   at every prompt.
   You should now see why a rule of one artefact goes into that
   artefact's definition and not into `CLAUDE.md`.
2. State lives in Markdown files of the project.
   It never lives in the conversation or in the assistant's memory.
   A project is a directory: the artefacts of the chain, their
   history logs, the ledger (the one source of truth for a project's
   state, made from the documents when it is read), the records of
   the reviewers and the resources.
   You should now see that a command that changes state writes a
   file.
3. Isolation is bought with subagents.
   A reviewer, a check and a render each run in a subagent that sees
   the files it is given and never the working conversation.
   All of them run on the one model of the session.
   You should now see why every agent file declares `model: inherit`.
4. Git, the conversion of documents and the hooks are scripts.
   The scripts are the door to a write of git; reading git is open.
   The git hook holds the line between the two: it denies every
   write and names the script to use.
   The few commands that finish settling a merge conflict are put to
   the principal (the person whose thinking is forged, with final
   authority on all content) and run on his yes.
   You should now see that a new git operation means a script, not
   an instruction to Claude.
5. Every file has a way of merging, and the forge tells git which.
   Composed text and the record files merge as text.
   Derived state is made when it is read and never kept in git, or
   made only on `main` and taken as ours at a merge.
   Immutable files never conflict.
   Where git leaves a conflict, Claude lays both sides out and the
   principal decides; the forge merges nothing itself.
   You should now see what `.gitattributes` is for.

A few rules of the files themselves follow from this.

- A command is a skill. "Command" is the word for what you invoke
  by slash; "skill" names the file shape, commands and contracts
  alike.
- A state file of `/forge` and a genre file of `/recipe` are
  supporting files: read by path, registered as nothing, carrying a
  description and no registration field.
- A contract skill is not user-invocable and stays out of the `/`
  menu. Each lens, persona or check file names its contract in its
  front-matter (`skills:`) and carries only its front-matter and its
  Lens section.
- A new check is one file in `.claude/agents/`, made from
  `templates/check-definition.md`.
- A command that should never start unasked carries
  `disable-model-invocation: true` in its front-matter.
- Every `argument-hint` in a skill's front-matter is quoted.
  Because a front-matter with CRLF line endings and an unquoted hint
  of two bracketed items fails to parse, Claude Code would then show
  the body's first line as the description.
- Each script carries its help in its module docstring. What several
  scripts share lives in one module beside them (`forge_repos.py`,
  `forge_tools.py`, `forge_docs.py`, `docs_map.py`), never twice.
- The scripts run on Python 3.8 or newer as
  `python scripts/<name>.py`, with nothing Windows-only.

Why the core is kept small and the rest read on demand is explained
in [How the rules are held](../about/how-the-rules-are-held.md).
Every term of the forge is given in one line in the
[Glossary](../reference/glossary.md).

## What you have afterwards

You know which file owns the thing you want to change and when
Claude reads it. What `docs/` and its documentation map are is
explained in [The documentation](../about/the-documentation.md).

## A worked example

One command traced through the layer: a run of the check `light` on
a project with the placeholder slug `my-project`.

```
/check light my-project
```

1. `CLAUDE.md` is already loaded, as in every session.
   The per-prompt hook in `.claude/settings.json` runs
   `scripts/hook-walkthrough.py` and adds its lines to the context.
   You should now see the walkthrough's one-item rule repeated in
   the context.
2. The command's skill `.claude/skills/check/SKILL.md` is read,
   because the command was invoked.
   You should now see the check procedure running.
3. The skill launches the agent `.claude/agents/check-light.md` as a
   subagent. The agent's front-matter names the contract
   `check-contract`, so Claude Code injects
   `.claude/skills/check-contract/SKILL.md` into it at launch.
   The agent also carries `CLAUDE.md`.
   You should now see an isolated run that reads the project's files
   and never the conversation.
4. The agent stays read-only and returns its report with its
   findings unnumbered.
   You should now see the report handed back to the command.
5. The command writes the report into `reviews/` of the project and
   gives the findings their IDs.
   `scripts/forge-report.py` completes the report's name with the
   time and a short content hash.
   A run that finds nothing files nothing.
   You should now see a file named
   `YYYY-MM-DD-check-light-HHMM-<hash>.md` in `reviews/`.
6. The findings are settled by walkthrough (one item per message,
   each closed with a verdict), with
   `.claude/skills/walkthrough/SKILL.md` read for its shape, and
   written in one round.
   You should now see the verdicts written once, at the end of the
   round.

## See also

- [Repository layout](../reference/repository-layout.md): the layout
  block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why
  the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing
  any of it.
- [The documentation](../about/the-documentation.md): what `docs/`
  and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
