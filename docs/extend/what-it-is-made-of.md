---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# About what the forge is made of

This page is for someone who wants to extend or change the forge and
first needs to know which files make it up, what each kind of file is
for and where to read what a given thing does. It was put together
from `CLAUDE.md` (its Repository layout and Templates sections) and
from the forge's solution design
(`projects/forge/40-solution-design.md`, its "How the parts work
together" and the parts that say what each kind of file is). It
covers kinds of file, not each command or agent one by one.

## The four ideas that carry it

The forge is not a program. It is a set of instructions that Claude
Code reads, with deterministic work kept at its edge in scripts. Four
ideas hold it together, and each kind of file below serves one of
them.

1. **One always-on core, the rest on demand.** `CLAUDE.md` is loaded
   into every session and every subagent. A command, a definition, a
   contract or a template is a file read only when it is invoked. What
   must hold through a long conversation is repeated by a hook at
   every prompt.
2. **State lives in files.** State lives in the Markdown files of a
   project, never in the conversation and never in the assistant's
   memory. A project is a directory: the artefacts of the chain, their
   history logs, the ledger, the reviewers' records and the
   resources.
3. **Isolation by subagents.** A reviewer, a check and a render each
   run in a subagent that sees the files it is given and never the
   working conversation, all on the one session model.
4. **Deterministic work in scripts.** Git, the conversion of
   documents and the hook are scripts. Claude is denied raw `git`, so
   the scripts are the only door to it.

## The files, kind by kind

### `CLAUDE.md`: the always-on core

`CLAUDE.md` in the engine root carries what must hold in every
session and for every subagent: the roles, the prime directives, the
working methods in short, the document kinds, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger and
the list of commands. A rule that belongs to one artefact is not
here; it stands in that artefact's definition. The cost of the core
is its size, since it is loaded every time.

### `.claude/skills/`: commands and the skills that are not commands

- **One skill per command.** Every command lives as
  `.claude/skills/<name>/SKILL.md`. "Command" is the word for what
  you invoke by slash; "skill" names the file shape. A command's body
  loads only when it is invoked.
- **Supporting files of the two dispatchers.** `/forge` is a thin
  dispatcher with one definition file per target state,
  `.claude/skills/forge/states/<state>.md`, each paired with the
  artefact's template in `templates/`. `/recipe` has the same shape,
  with one file per genre in `.claude/skills/recipe/genres/` and the
  genre's skeleton in `templates/recipe-<genre>.md`. These files are
  read by path and registered as nothing. A new layer of the chain is
  added by one definition file, and the dispatcher stays untouched.
- **The three reviewer contracts.** `critic-contract`,
  `challenger-contract` and `check-contract`, each
  `.claude/skills/<kind>-contract/SKILL.md`. They are skills but not
  commands: kept out of the `/` menu and preloaded into every reviewer
  agent of their kind. A contract owns the conduct and isolation, the
  subject and its boundary, the way of working and the shape of the
  output.
- **The walkthrough skill.** `.claude/skills/walkthrough/SKILL.md`
  holds the shape of the walkthrough and of the elicitation interview.
  It is not a command: it is read whenever a walkthrough or an
  interview runs, while `CLAUDE.md` carries only the rule in short and
  the pointer.

### `.claude/agents/`: one file per lens, persona and check

The critic has lenses, the challenger has personas, the check has
checks, and each is one agent file (`critic-<lens>`,
`challenger-<persona>`, `check-<name>`). An agent file carries its
front-matter and its Lens section and nothing else: the front-matter
names the contract skill of its kind, which is injected at launch, and
the Lens section specialises the contract. A Lens may narrow what is
read or make a shared rule stricter; it never renames, drops or
duplicates a shared rule. Every agent declares `model: inherit`. A new
check, lens or persona is one file.

### `.claude/settings.json`: the deny rules and the hook

This file carries the deny rules that keep Claude from raw `git` in
both shells and from sensitive paths, and the per-prompt hook,
`scripts/hook-walkthrough.ps1`, which repeats the one-item rule of the
walkthrough and three lines of conduct at every prompt. A rule that
must hold in a long conversation is not trusted to `CLAUDE.md` alone.

### `templates/`: the skeletons

`templates/` holds the canonical skeletons for every new project: one
per artefact, the ledger, the indexes, the history log, the recipe
and each recipe genre. Where a shape had no owner it was given a
skeleton, rather than a second description somewhere else. A skeleton
named `<type>-definition.md` is that of the definition of one member
of a type the forge can be extended by: an artefact, a critic lens, a
challenger persona, a check. To add such a member, you start from its
`<type>-definition.md`.

### `scripts/`: the only platform-bound layer

`scripts/` holds the git scripts (save, pull, status, clone, branch),
the document conversions and the hook. They are the only door to git,
reading state included. They are the only layer bound to a platform
and are written to run unchanged on Linux and macOS: cross-platform
PowerShell 7 with nothing Windows-only, external tools resolved from
PATH. New scripts are written in Python, and the PowerShell scripts
are to be rewritten to it in time.

### `projects/forge`: the forge's own project

`projects/forge/` is the forge itself run through its own process. It
is the one project the engine's repository keeps; every other project
under `projects/` is a git repository of its own. Here live the
forge's brief, its intent, its solution design, its decisions and
ledger, and in `projects/forge/recipes/` the recipes from which the
engine's README and release notes are rendered. A change to how the
forge works is complete only once that intent is updated and the
README re-rendered.

## Where to read what a thing does

Read a thing in its own file, never in a second description. A
procedure stated in two places is a defect, so each mechanism lives
in one place:

- what a command does in full: its `SKILL.md`, which `/man <command>`
  prints;
- what an artefact is and how it is found: its definition under
  `.claude/skills/forge/states/`; what comes out: its template;
- what a reviewer goes after: its agent file; how all reviewers of
  that kind behave and report: the contract;
- what a script does, needs installed and where its output lands: its
  own help header;
- why the forge is built as it is: the intent and the solution design
  in `projects/forge/`.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [About how the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
