---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 336f2bd62de0521b
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
---

# What the forge is made of

The operating layer of the forge is a set of files that Claude Code
reads, with the deterministic work kept in scripts at its edge. The
forge is not a program. This page is for the extender, that is,
someone who wants to change or add to the forge. It shows which file
holds what, when each file is loaded, and how one command passes
through them.

## When to use it

Use this page before you change anything in the forge. It tells you
which file holds the rule you want to change. It also tells you when
Claude reads that file, so you know when your change takes effect.
How a change is then made and recorded is described in
[Make a change to the forge](how-a-change-is-made.md).

## What you do

Find the part you want in the table below, then open its file. To
read what a command does, as its own definition says it, type:

```
/man critique
```

`/man` reads the forge's own definitions and prints them.

A few words the table needs:

- A **session** is one conversation with Claude Code.
- The **harness** is Claude Code itself: the program that runs
  Claude, loads its files and starts its hooks.
- A **subagent** is a separate run of Claude that sees only the
  files it is given, never the working conversation.
- The **principal** is the person whose thinking is being forged.
- A **hook** is a script the harness starts at a fixed moment, such
  as every prompt.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The universal core: what must hold in every session and for every subagent | Always, in every session and every subagent |
| `.claude/skills/<name>/SKILL.md` | One skill per command | When the command is invoked |
| `.claude/skills/forge/states/<state>.md` | The definitions of the artefacts, supporting files of `/forge` | Read by path when `/forge <state>` runs |
| `.claude/skills/recipe/genres/<genre>.md` | The genre files, supporting files of `/recipe` | Read by path when `/recipe <genre>` runs |
| `.claude/skills/critic-contract/`, `challenger-contract/`, `check-contract/` | The three reviewer contracts: skills that are not commands | Injected whole into every agent that names them, at its launch |
| `.claude/skills/docs-contract/SKILL.md` | The documentation contract: a skill that is not a command | Shared by the documentation's planner and writer |
| `.claude/skills/walkthrough/SKILL.md` | The shape of the walkthrough and of the elicitation interview: a skill that is not a command | Whenever a walkthrough or an interview runs |
| `.claude/agents/` | One file per critic lens, challenger persona and check, and the documentation's planner and writer | When a command launches the agent as a subagent |
| `.claude/settings.json` | The two hooks and the deny rule | Read by the harness; one hook runs at every prompt, the other before a tool is used |
| `templates/` | The canonical skeletons, the skeleton of the player page among them | When a command makes a file from one |
| `scripts/` | Python scripts with their shared modules beside them, the two hooks among them | When a command, a hook or you run one, as `python scripts/<name>.py` |
| `.gitattributes` | The engine's own ways of merging by path, for its derived files at the root and under `projects/forge/` | By git, at a merge |
| `tmp/` | The engine's working folder | Read by no check, no ledger and no history |
| `projects/forge/` | The forge's own project: the forge run through its own process | Like any project, when a command names it |
| `docs/` | The generated documentation and its index | Written by `/document`; pages are read by `/man` in its run |
| `docs/videos/` | The public folder of the videos: not the documentation's | Written by `md2video` |

What some rows hold in more detail:

- **The skills.** "Command" is the word for what you invoke by
  slash. "Skill" names the file shape, of commands and contracts
  alike. A command's body loads only when the command is invoked. The
  state files and the genre files are registered as nothing: they
  carry a description and no registration field, and their
  dispatcher reads them by path.
- **The reviewer contracts.** Each kind of reviewer (critic,
  challenger, check) owns one contract skill. Every lens, persona
  or check file of that kind names its contract in its front-matter
  (`skills:`). The agent file then carries only its front-matter and
  its Lens section. The contracts are kept out of the `/` menu.
- **The agents.** Every agent declares `model: inherit`, so all run
  on the one session model. That model is chosen in
  `.claude/settings.local.json`, which is not in git. A new check is
  one file, `check-<name>`, from `templates/check-definition.md`.
- **The hooks.** `scripts/hook-walkthrough.py` repeats the
  walkthrough's one-item rule and four lines of conduct at every
  prompt. `scripts/hook-git.py` holds the line between reading git
  and writing it: it denies a direct write of git and names the
  script to use instead.
- **The templates.** A skeleton named `<type>-definition.md` is the
  skeleton of the definition of one member of a type the forge can
  be extended by: an artefact, a critic lens, a challenger persona or
  a check. Every skeleton is listed in [Templates](../reference/templates.md).
- **The scripts.** What several scripts share lives in one module
  beside them, never twice: `forge_repos.py`, `forge_tools.py`,
  `forge_docs.py`, `docs_map.py` and `forge_check.py`. Each script
  carries its help in its module docstring. The scripts are the only
  platform-bound layer and are written to run unchanged on Windows,
  Linux and macOS.
- **The working folder.** `tmp/` holds what the scripts and
  commands make on the way to a result:
  - the packets, envelopes and profiles of runs on another engine
    (`tmp/research/<run>/`);
  - the tasks of a documentation run;
  - a check's report before it is filed;
  - a dry ledger;
  - the manifest of a migration.

  The folder is in git with its own `README.md` and `.gitignore`, so
  that it exists on every clone. Its contents never are. Nothing in
  it is a source of truth. A run is kept for inspection and deleted
  by hand, never by a script.
- **The documentation.** `docs/` is generated, never written by
  hand. What it is and how its map works is described in
  [The documentation](../about/the-documentation.md).
  `docs/videos/` holds the projects' html-player files and the player
  page `index.html`, written from `templates/html-player.html`.
  `docs/.nojekyll` keeps GitHub Pages from touching the folder.

The whole layout, file by file, is in
[Repository layout](../reference/repository-layout.md). Every term
of the forge is in the [Glossary](../reference/glossary.md).

## What happens

One line of flow runs through the layer whenever you type a command:

```
your prompt → hook → CLAUDE.md (always loaded) → the command's skill → definitions, templates, agents with their contracts → scripts → files of the project, and git through the scripts
```

Five ideas hold whatever a command does:

- **One always-on core, the rest on demand.** `CLAUDE.md` is loaded
  into every session and every subagent. A command, a definition, a
  contract or a template is a file read when its situation arises.
  What must hold through a long conversation is repeated by a hook at
  every prompt. Why the core is kept small is explained in
  [How the rules are held](../about/how-the-rules-are-held.md).
- **State lives in files.** State lives in the Markdown files of the
  project, never in the conversation and never in the assistant's
  memory. A project is a directory.
- **Isolation by subagents.** A reviewer, a check and a render each
  run in a subagent. It sees the files it is given and never the
  working conversation.
- **Deterministic work in scripts.** Git, the conversion of
  documents and the hooks are scripts. The scripts are the door to a
  write of git: the only way to write it. Reading git is open.
- **Every file has a way of merging.** Composed text and the record
  files merge as text. Derived state is made at read time and never
  kept in git, or made only on `main` and kept as the local side at a
  merge. Immutable files never conflict. Where git leaves a conflict,
  Claude lays both sides out and the principal decides.

The worked example below follows these steps for one command.

## If something goes wrong

- **An agent runs without its contract.** A skill an agent names in
  its front-matter that does not exist is skipped silently. The
  engine check verifies that every named skill exists:

  ```
  /check engine
  ```

- **A command shows the first line of its body as its
  description.** A front-matter with CRLF line endings and an
  unquoted `argument-hint` of two bracketed items fails to parse.
  Quote every `argument-hint`.
- **A command behaves as an older version.** A skill shadows a
  command file of the same name. Move a command to a skill whole,
  never in part.
- **A hook does not run in a session started elsewhere.** A relative
  path in `.claude/settings.json` is resolved against the session's
  working directory, not the engine root. The hooks are invoked with
  `${CLAUDE_PROJECT_DIR}/scripts/<hook>.py` as their one argument.
- **A reviewer run outside a session preloads nothing.** A headless
  `--agent` run does not preload the contract skill. Reviewers run
  as subagents only.

## A worked example

One run of `/critique clarity` on a project `my-project`, traced
through the layer:

1. You type the command. The harness starts
   `scripts/hook-walkthrough.py`, which adds the walkthrough rule
   and the lines of conduct to your prompt. `CLAUDE.md` is already
   loaded.
   You should now see Claude take up the command with the core's
   rules in force.
2. Claude reads the command's skill,
   `.claude/skills/critique/SKILL.md`. Nothing of it was loaded
   before.
   You should now see Claude follow the steps the skill gives.
3. The skill launches the agent `.claude/agents/critic-clarity.md`
   as a subagent, on the session model. At launch the harness
   injects `.claude/skills/critic-contract/SKILL.md`, which the
   agent names in its front-matter. The agent reads the project's
   files from disk and sees nothing of the conversation.
   You should now see the agent running apart from the conversation.
4. The agent returns its report with its findings unnumbered, and
   writes nothing. The command numbers the findings and files the
   report in `projects/my-project/reviews/`. The report's unique
   name is completed by `scripts/forge-report.py`.
   You should now see a new dated report in `reviews/`.
5. The findings are settled one at a time by walkthrough (the
   principal's verdict on each item, one per message). Claude reads
   `.claude/skills/walkthrough/SKILL.md` for its shape. The verdicts
   are written in one round at the end, and the ledger (the state of
   the project, made from its documents) is remade by
   `scripts/forge-ledger.py`.
   You should now see the settled findings in the project's files.
6. The work is saved through `scripts/forge-save.py`. Had Claude
   tried a direct write of git, `scripts/hook-git.py` would have
   denied it and named this script.
   You should now see a commit on the project's repository.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
