---
generated: 2026-10-10
made: derived
inputs-hash: af467fd0a69148a6
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# About what the forge is made of

This page is a tour of the operating layer for someone who wants to
extend the forge: which files and directories it is made of, what
each kind is for, and where to read what a thing does before
touching it. It was put together from `CLAUDE.md` and the forge's
solution design (`projects/forge/40-solution-design.md`); the
reasoning joins the layout block and the Templates and Persistence
sections of the one with the "How the parts work together" section
and the items of the other.

## Four ideas before the files

The forge is not a program. It is a set of instructions that Claude
Code reads, with deterministic work kept at its edge in scripts.
Four ideas carry it, and every file below is one of them made
concrete.

- **One always-on core, the rest on demand.** `CLAUDE.md` is loaded
  into every session and every subagent. A command, a definition,
  a contract or a template is a file read when it is invoked. What
  must hold through a long conversation is repeated by a hook at
  every prompt rather than trusted to text loaded once.
- **State lives in files.** A project is a directory of Markdown
  files: the artefacts of the chain, their history logs, the ledger,
  the records of the reviewers and the resources. Nothing of state
  lives in the conversation or in the assistant's memory.
- **Isolation is bought with subagents.** A reviewer, a check and a
  render each run in a subagent that sees the files it is given and
  never the working conversation, all on the one session model.
- **Deterministic work is a script.** Git, the conversion of
  documents and the hook are scripts. The harness denies Claude raw
  `git`, so the scripts are the only door.

## The tour

Walk the engine root in this order. Each step says what you open and
what you find there.

### 1. Open `CLAUDE.md`: the always-on core

This is the one file Claude Code loads into every session and for
every subagent. It carries what must hold everywhere: the roles, the
prime directives, the working methods in short, the document kinds,
the chain, the repository layout, persistence, versioning, the ID
scheme, the reviewers, the ledger and the list of commands. A rule
of one artefact is not here but in that artefact's definition. The
file's cost is its size, which is why everything that can be read
on demand lives elsewhere.

### 2. Open `.claude/skills/`: one skill per command, and the skills that are not commands

Every command lives as `.claude/skills/<name>/SKILL.md`, and its body
loads only when the command is invoked. "Command" is the word for
what the user invokes by slash; "skill" names the file shape,
commands and contracts alike.

Two commands are thin dispatchers with supporting files beside them,
read by path and registered as nothing:

- `/forge` has one definition file per artefact of the chain under
  `.claude/skills/forge/states/<state>.md`. The definition says what
  the artefact is, how it is found and owns its rules; it is paired
  with the artefact's template. Which artefacts the forge has is the
  listing of that directory and nothing else, so a future layer is
  added by one file and the dispatcher stays untouched.
- `/recipe` has the same shape: one genre file per render genre
  under `.claude/skills/recipe/genres/<genre>.md`, each with its
  skeleton in `templates/recipe-<genre>.md`.

Some skills are not commands and never appear in the slash menu.
They are preloaded into an agent at launch, named in the agent's
front-matter:

- the three reviewer contracts, `critic-contract`,
  `challenger-contract` and `check-contract` (the suffix because
  `check/` is the command): each owns the conduct and isolation, the
  subject and its boundary, the way of working and the shape of the
  output for its kind of reviewer;
- the contract of the documentation agents, `docs-contract`, which
  the planner and the writer share in the same way;
- the walkthrough skill, `.claude/skills/walkthrough/SKILL.md`,
  which holds the shape of the walkthrough and of the elicitation
  interview and is read whenever one runs.

A guarded command carries `disable-model-invocation: true` in its
front-matter, so that Claude cannot start it unasked; the supporting
files need no guard.

### 3. Open `.claude/agents/`: one file per reviewer, and the two documentation agents

A reviewer is one agent file: `critic-<lens>`, `challenger-<persona>`
or `check-<name>`. Each carries its front-matter and its Lens section
and nothing else; the shared behaviour comes from the contract the
front-matter names, and Claude Code injects the whole contract at
launch. A Lens section is a specialisation of its contract, never a
replacement: it may narrow what is read or make a shared rule
stricter, never rename, drop or duplicate a shared rule or field.
Every agent declares `model: inherit`, so the whole forge runs on one
model. A new check, lens or persona is one file, and only by the
principal's decision.

Beside the reviewers stand the two agents of the documentation: the
planner, which reads the target on disk and writes the map, and the
writer, which makes one page from its map entry alone.

### 4. Open `.claude/settings.json`: the deny rules and the hook

This file is the wall. Under `permissions.deny` it blocks the `git`
command in both shells and sensitive paths, so the scripts stay the
only door to git. It also carries the one per-prompt hook: at every
prompt it runs `scripts/hook-walkthrough.py` through `python`, with
the path anchored at the project root, and the script prints the
one-item rule of the walkthrough and three lines of conduct. In the
same file the commit attribution is switched off, so no trailer is
added to a commit.

### 5. Open `templates/`: the skeletons

Every new project is scaffolded from these canonical skeletons, and
every shape the forge needs has exactly one owner here. Two kinds
matter most to an extender:

- `<type>-definition.md` is the skeleton of the definition of one
  member of a type the forge can be extended by: an artefact, a
  critic lens, a challenger persona, a check.
- `docs-map.md` is the skeleton of the documentation map.

Where a shape once had no owner it was given a skeleton rather than
a second description: the bundle catalogue, the library form of the
ledger, the state vocabularies of findings and challenges.

### 6. Open `scripts/`: the only platform-bound layer

Everything else in the forge is Markdown; the scripts are Python,
3.8 or newer, run as `python scripts/<name>.py`, with `python` on
PATH their one prerequisite. They use nothing Windows-only: paths
through `pathlib`, processes through argument lists and never a
shell, external tools (`git`, `markitdown`, `pandoc`, `claude`)
resolved from PATH. They fall into four groups:

- git: `forge-save.py` commits and pushes, `forge-pull.py`
  fast-forwards from the remotes, `forge-status.py` reports state
  without changing anything, `forge-clone.py` brings an existing
  project in, `forge-branch.py` switches or creates a branch;
- conversion of documents: `doc2md.py` turns a document into a
  Markdown extract, `md2pptx.py` and `md2docx.py` turn a render into
  a PowerPoint or Word file, each by pandoc or by a model;
- the hook: `hook-walkthrough.py`;
- the documentation: `docs-state.py` computes the state of the pages
  from the content hashes of their inputs, `docs-index.py` derives
  the index, `docs-check.py` checks the pages.

What several scripts share lives in one module beside them, never
twice: `forge_repos.py` for the git scripts (the engine root, the
git check, which repositories a run visits, running git),
`forge_tools.py` for the three conversions (a tool on PATH,
resolving paths, the headless Claude Code run), `docs_map.py` for
the three documentation scripts (the reader of the map). Each
script carries its help in its module docstring: synopsis, what it
does, what it needs, examples.

### 7. Open `projects/forge/`: the forge's own project

The forge is run through its own process. This directory is a
project like any other and holds the brief, the intent with its
positions and rejected directions, the threads, the decisions, the
ledger and the solution design. Three things an extender needs
live only here:

- the documentation map, `docs-map.md`, beside the ledger;
- the recipes of the engine's README and release notes, in
  `projects/forge/recipes/`, from which `/release` regenerates both;
- the solution design, which names for every part of the forge the
  file that realises it, under `Where`.

The engine's `.gitignore` excludes `projects/*` and re-includes
`projects/forge`, so this one project travels with the engine while
every other project is a repository of its own that the engine does
not know. A process change is complete only once the intent here is
updated and the README re-rendered.

### 8. Open `docs/`: the generated documentation

Pages of one topic each and their index, generated by `/document`
from the map beside the owning project's ledger, never composed by
hand and never a source of truth. The map itself never lies in
`docs/`. The rest of the engine root is renders (the README, the
release notes, the contributing file) and the licence; the layout
block lists them.

## Where to read what a thing does

Its own file, never a second description. One mechanism lives in one
place, and a procedure stated in two places is a defect. So:

- what a command does is its skill's, and `/man <command>` prints
  it;
- what a script does and needs is its help header's;
- the rules of an artefact are its definition's, under
  `.claude/skills/forge/states/`;
- the conduct of a reviewer is its contract's, and what one lens,
  persona or check goes after is its agent file's;
- the reason behind a rule is the intent's, in `projects/forge/`,
  and the file that realises a part is named in the solution design.

The solution design says it plainly: the forge cannot yet be built
from its artefacts alone; whoever rebuilds it needs the intent, the
design and the files of the engine together. When you extend the
forge, start from the file that owns the thing you change, and add
nothing that describes it a second time.

## See also

- [Repository layout](../reference/repository-layout.md): the layout
  block.
- [About how the rules are held](../about/how-the-rules-are-held.md):
  why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing
  any of it.
- [About the documentation](../about/the-documentation.md): what
  `docs/` and the map are.
