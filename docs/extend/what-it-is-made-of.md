---
generated: 2026-10-09
made: derived
inputs-hash: a04b0725e16bf0df
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# About what the forge is made of

This page is a tour of the operating layer for someone who wants to
extend the forge: which files and directories make it up, what each
kind of file is for, and where to read what a thing does before
changing it. It was put together from `CLAUDE.md` (its sections
Repository layout, Templates and Persistence) and from the forge's
own solution design (`projects/forge/40-solution-design.md`, the
section "How the parts work together" and the parts that describe
each kind of file).

## The four ideas that carry it

The forge is not a program. It is a set of instructions that Claude
Code reads, with deterministic work kept at its edge in scripts. Four
ideas hold the whole thing together, and every file below sits under
one of them.

1. **One always-on core, the rest on demand.** `CLAUDE.md` is loaded
   into every session and every subagent. A command, a definition, a
   contract or a template is a file read only when it is invoked.
   What must hold through a long conversation is repeated by a hook
   at every prompt.
2. **State in files.** State lives in Markdown files of the project,
   never in the conversation and never in the assistant's memory. A
   project is a directory: the artefacts of the chain, their history
   logs, the ledger, the records of the reviewers and the resources.
3. **Isolation by subagents.** A reviewer, a check and a render each
   run in a subagent that sees the files it is given and never the
   working conversation, all on the one session model.
4. **Deterministic work in scripts.** Git, the conversion of
   documents, the hook and the documentation's mechanics are
   scripts. The harness denies Claude raw `git`, so the scripts are
   the only door.

## The tour, file by file

Open the engine root and you see the following. Take them in this
order; each one is explained by the next.

### `CLAUDE.md`: the always-on core

The one file Claude Code loads into every session and for every
subagent. It carries what must hold everywhere: the roles, the prime
directives, the working methods in short, the document kinds, the
chain, the repository layout, persistence, versioning, the ID
scheme, the reviewers, the ledger and the list of commands. What it
deliberately does not carry is the rule of any one artefact: that
lives in the artefact's definition, read when `/forge` works that
artefact. The cost of this file is its size, which is why everything
that can wait for its situation lives elsewhere.

### `.claude/skills/<name>/SKILL.md`: the commands and the skills

Every command lives as one skill file, `.claude/skills/<name>/SKILL.md`.
"Command" stays the word for what the user invokes by slash;
"skill" names the file shape, whether or not the file is a command.
The body of a skill loads only when it is invoked, so adding one
costs the always-on context nothing but its description.

Two commands are dispatchers with supporting files beside them:

- `/forge` reads one definition file per target artefact from
  `.claude/skills/forge/states/<state>.md`. A definition says what
  the artefact is, how it is found and what rules it owns, and is
  paired with the artefact's template. Which artefacts the forge has
  is the listing of that directory: a new layer of the chain is one
  new file there, and the dispatcher stays untouched.
- `/recipe` reads one genre file per render genre from
  `.claude/skills/recipe/genres/<genre>.md`, the same shape, each
  genre with its skeleton under `templates/`.

Supporting files are read by path and registered as nothing: they
carry a description and no registration field, and need no guard of
their own.

Some skills are not commands at all:

- The three reviewer contracts, one per kind of reviewer
  (`critic-contract`, `challenger-contract`, `check-contract`), hold
  the shared behaviour of every lens, persona or check of that kind:
  conduct and isolation, the subject and its boundary, the way of
  working and the shape of the report. They are preloaded into the
  agent at launch, named in the agent file's front-matter, and never
  appear in the `/` menu.
- The walkthrough skill holds the shape of the walkthrough and of
  the elicitation interview, read whenever one runs. `CLAUDE.md`
  carries the rule in one sentence and a pointer; the hook repeats
  the one-item rule at every prompt.

### `.claude/agents/`: the reviewers and the documentation agents

One agent file per critic lens, challenger persona and check, named
`critic-<lens>`, `challenger-<persona>` and `check-<name>`. Each
carries its front-matter and its Lens section and nothing else: the
front-matter names the contract skill that is preloaded, and the
Lens section is a specialisation of that contract. It may narrow
what is read or make a shared rule stricter; it never renames, drops
or duplicates a shared rule or field, and the protocol changes in
the contract alone. Every agent declares `model: inherit`, so the
whole forge runs on the one session model.

Two further agents belong to the documentation: the planner, which
reads the target on disk and writes the documentation map, and the
writer, which makes one page from its entry of the map alone.

### `.claude/settings.json`: the deny rules and the hook

The engine's settings file does two things. Under `permissions.deny`
it denies Claude the `git` command in both shells, so that the
scripts are the only door to git, reading state included; it also
blocks sensitive paths outside the engine. And it carries the one
per-prompt hook, which runs the hook script at every prompt and
prints the one-item rule of the walkthrough and three lines of
conduct: a rule that must hold in a long conversation is not trusted
to `CLAUDE.md` alone. The hook is context, not enforcement.

The session model is not here: it lives in a gitignored local
settings file that the first-run command creates.

### `templates/`: the skeletons

The canonical skeletons for every new project and every new
document: the artefacts of the chain, the threads file, the ledger,
the history log, the resource indexes and the bundle catalogue, the
recipe and its genres. Where a shape had no owner it has a skeleton
here rather than a second description somewhere else; the state
vocabularies of findings and challenges, for instance, are comments
in the ledger's skeleton.

Among them is one `<type>-definition.md` per type the forge can be
extended by: an artefact, a critic lens, a challenger persona, a
check. Extending the forge by one member of such a type starts from
that skeleton.

### `scripts/`: the only platform-bound layer

Everything deterministic. The scripts are Python, run as
`python scripts/<name>.py`, with `python` on PATH as their one
prerequisite, and use nothing Windows-only: paths through `pathlib`,
processes through `subprocess` with argument lists and never a
shell, external tools (`git`, `markitdown`, `pandoc`, `claude`)
resolved from PATH. Each script carries its help in its module
docstring: synopsis, what it does, what it needs, examples.

The scripts fall into groups:

- the git scripts (`forge-save`, `forge-pull`, `forge-status`,
  `forge-clone`, `forge-branch`), the only door to git for the
  engine and every project repository;
- the conversions (`doc2md` from a document to Markdown, `md2pptx`
  and `md2docx` from a render to PowerPoint or Word, each by pandoc
  or by a model);
- the per-prompt hook (`hook-walkthrough`);
- the documentation scripts (`docs-state`, `docs-index`,
  `docs-check`: the state of the pages, the index, the check).

What several scripts share lives in one module beside them, imported
by path and never written twice: `forge_repos.py` for the git
scripts (the engine root, the git check, which repositories a run
visits, running git), `forge_tools.py` for the conversions (a tool
on PATH, resolving paths, the headless run) and `docs_map.py` for
the documentation scripts (the reader of the map).

### `projects/forge`: the forge's own project

Forge of Thought run through its own process. Here live its brief,
its intent (the design positions, the rejected directions) with its
open threads, its solution design, its decisions and its ledger, and
beside the ledger the documentation map. Its `recipes/` hold the
recipes of the engine's README, release notes and contributing file,
which are renders from those recipes into the engine root. Every
other project under `projects/` is a git repository of its own that
the engine does not know; `projects/forge` is the one exception,
re-included from the gitignore. A process change is complete only
once that intent is updated and the README re-rendered.

### `docs/`: the generated documentation

Pages of one topic each and their index, generated from the map
beside the forge project's ledger. Nothing in `docs/` is composed by
hand: a page is overwritten by the documentation run, the index is
derived by a script, and the map is never shown to the reader. What
the pages and the map are is told in About the documentation, linked
below.

## Where to read what a thing does

One mechanism lives in one place. Whatever the forge has a procedure
for, a command, a skill, a script or an agent, is described in full
by its own file and nowhere else: a command by its skill, an
artefact by its definition, a reviewer's shared conduct by its
contract and its particular hunt by its Lens, a script by its help
header, a skeleton by itself. `CLAUDE.md` says in short what exists
and points; where it needs another's mechanism it cites the file by
path. A procedure stated in two places is a defect, and a check
exists to find such doubles.

So before changing anything, open the file that owns it. If you
cannot find a second description of a thing, that is by design: the
one you found is the one to change.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [About how the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [About the documentation](../about/the-documentation.md): what `docs/` and the map are.
