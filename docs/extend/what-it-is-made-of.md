---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: aaa48a04f7dfc147
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Persistence (git)
  - tmp/README.md
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/10-intent.md#POS.1920
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/40-solution-design.md#The instruction layer
  - projects/forge/40-solution-design.md#The commands
  - projects/forge/40-solution-design.md#SOL.0300
  - projects/forge/40-solution-design.md#SOL.0330
  - projects/forge/40-solution-design.md#SOL.0900
  - projects/forge/40-solution-design.md#Across the parts
  - .claude/settings.json
---

# What the forge is made of

The forge is a set of instructions that Claude Code reads, with the
deterministic work kept at its edge in scripts; it is not a program.
This page is for you as the extender: it names the files of the
operating layer, says what each one is and when Claude Code (the
harness, that is the program that runs Claude and loads these files)
takes it up, so that you know which file to open before you change
anything. The reasons behind the layer are given after the table.

## When to use it

Use this page when you are about to change the forge and need to
know where the thing you are changing lives, and whether that file
is in Claude's context always or only when its situation arises. How
a change is then made, recorded and released is on
[Make a change to the forge](how-a-change-is-made.md). The full
block of paths, the projects' directories included, is on
[Repository layout](../reference/repository-layout.md).

## What you do

Find the thing you want to change in the table and open the file in
the first column. "Command" is the word for what you invoke by a
slash; "skill" is the shape of the file, commands and contracts
alike. "Definition" is the word for a state file of `/forge`;
"template" is the word for a skeleton.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | the always-on core: the roles, the prime directives, the working methods in short, the document kinds, the chain, the layout, persistence, versioning, the ID scheme, the reviewers, the ledger and the list of commands; a rule of one artefact is not here but in that artefact's definition | into every session and into every subagent |
| `.claude/skills/<name>/SKILL.md` | one skill per command; the state files of `/forge` (`.claude/skills/forge/states/<state>.md`, the definitions of the artefacts) and the genre files of `/recipe` (`.claude/skills/recipe/genres/<genre>.md`) are supporting files of their dispatcher, read by path and registered as nothing; every `argument-hint` is quoted | the description of every skill stays in the always-on context; the body, and a supporting file, load when the command is invoked and never before |
| `.claude/skills/<name>/SKILL.md`, the skills that are not commands | the three reviewer contracts (`critic-contract`, `challenger-contract`, `check-contract`), the contract of the documentation agents (`docs-contract`) and the walkthrough skill (`walkthrough`); the contracts are `user-invocable: false`, out of the `/` menu | a contract whole, at the launch of the agent whose front-matter names it under `skills:`; the walkthrough skill whenever a walkthrough or an elicitation interview runs |
| `.claude/agents/` | one file per critic lens (`critic-<lens>.md`), per challenger persona (`challenger-<persona>.md`) and per check (`check-<name>.md`), each its front-matter and its Lens section and nothing else; and the documentation's planner and writer; every agent declares `model: inherit` | when a command launches it as a subagent, which sees the files it is given and never the working conversation |
| `.claude/settings.json` | the two hooks: `scripts/hook-walkthrough.py` on `UserPromptSubmit` and `scripts/hook-git.py` on `PreToolUse` for the Bash tool, each started as `python` with the script's path anchored at `${CLAUDE_PROJECT_DIR}`; the deny rules: reading `~/.ssh/**`, reading `~/.aws/**`, and `git` in the other shell tool (`PowerShell(git *)`) | by Claude Code for the session; the first hook runs at every prompt, the second before every call of the Bash tool |
| `templates/` | the canonical skeletons; `<type>-definition.md` is the skeleton of the definition of one member of a type the forge is extended by (an artefact, a critic lens, a challenger persona, a check); `html-player.html` is the skeleton of the player page in `docs/videos/` | when a file is made from one |
| `scripts/` | Python, 3.8 or newer, run as `python scripts/<name>.py`, the help of each in its module docstring: the git scripts, the ledger made at read time, the history of one item, the unique name of a report, the migration, the mechanical clauses of a check, the runs on another engine, the conversions, the documentation's state, index and check; the shared modules beside them (`forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py`), never twice; the two hooks among them | run by the command that needs one, never loaded as text; the hooks by `settings.json` |
| `tests/`, `pytest.ini`, `.github/workflows/tests.yml` | the engine's tests, one file per concern, run by pytest; `tests/conftest.py` holds what they share; `tests/fixture` is the synthetic fixture project copied by every test; `pytest.ini` says how they run (`testpaths = tests`, `pythonpath = scripts`, so the shared modules import by name); the workflow runs them in CI at every push and pull request, on Linux and on Windows, with Python 3.8 and the newest stable | by `/test`, by `/release` of the engine, and by CI at every push |
| `.gitattributes` | the engine's own ways of merging by path, its derived files at the root and under `projects/forge/` | by git at a merge |
| `.mailmap` | git's own mapping of the author's names in the history to one handle, the history itself untouched | by git when it shows the history |
| `tmp/` | the engine's one working folder: what the scripts and commands make on the way to a result; in git with its own README and `.gitignore`, its contents never | written by a run; read by no check, no ledger and no history; a run is kept for inspection and deleted by hand, never by a script |
| `projects/forge/` | the forge's own project, the one project inside the engine's repository; every other project under `projects/` is gitignored and a git repository of its own, which the engine does not know | when a command works it, as any project |
| `docs/` | the generated documentation: pages of one topic each and their index, made by `/document` from the map beside the owning project's ledger; `docs/videos/` is the public folder of the projects' player files and of the player page, not the documentation's; `docs/.nojekyll` keeps GitHub Pages from touching it | written by `/document`; read by `/man` when a question in free words is routed by the index |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | renders of recipes of the forge's own project, never edited by hand | by `/render`; the first two at every `/release` |
| `SECURITY.md`, `CODE_OF_CONDUCT.md` | the two fixed files of the root: the security policy, the principal's own text, and the code of conduct, the Contributor Covenant 3.0 word for word; no render, no companion, no row, no check | changed on the principal's word only |
| `LICENSE`, `logo.png` | CC BY 4.0, under which the engine is published, and the repository avatar | by nothing of the forge |

The "principal" is the person whose thinking the forge serves and who
decides. The "ledger" is a project's state file, made at read time by
a script and never kept in git. A "subagent" is an isolated run of
Claude that sees the files it is given and never the working
conversation. A "walkthrough" is the working method that puts a list
to the principal one item at a time. Every skeleton of `templates/`
is described on [Templates](../reference/templates.md); what the
tests cover and what the fixture is, on [The tests](../about/the-tests.md);
the two fixed files, on
[The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md);
what `docs/` and its map are, on
[The documentation](../about/the-documentation.md). Every other term
is in the [Glossary](../reference/glossary.md).

## What happens

The flow in one line: the core is in context from the first prompt,
and the per-prompt hook adds its lines at every prompt; a slash
command reads its skill; the skill reads a definition or a template,
launches an agent with its contract, or runs a script where the work
is deterministic; the scripts write the files of a project and the
writes of git; git merges those files the way `.gitattributes` tells
it.

Five ideas carry the layer.

- One always-on core, and everything else read when its situation
  arises. `CLAUDE.md` is loaded into every session (one run of
  Claude Code, from its start to its end) and into every subagent. A
  command, a definition, a contract or a template is a file read when
  it is invoked. The always-on text holds one sentence and a pointer;
  the detail is a file read when its situation arises, because what
  the core costs is its size. Why the core is small and the rest on
  demand is on [How the rules are held](../about/how-the-rules-are-held.md).
  What must hold through a long conversation is repeated by a hook
  at every prompt, because text loaded once is not trusted to hold;
  the cost is that a hook is context and not enforcement.
- State lives in the Markdown files of the project, never in the
  conversation and never in the assistant's memory. A project is a
  directory: the artefacts of the chain, their history logs, the
  ledger, the records of the reviewers and the resources.
- Isolation is bought with subagents. A reviewer, a check and a
  render each run in a subagent, all on the one session model; a
  contract is a preloaded skill rather than a copy of the shared text
  in every agent file.
- Git, the conversion of documents and the hook are scripts. The
  scripts are the door to a write of git; reading git is open; the
  hook holds the line between the two, denies every write and names
  the script to use. The few commands that finish the step of a
  conflict are the exception: the hook puts them to the principal and
  runs them on his yes.
- Every file has a way of merging, and the forge tells git which.
  Composed text and the record files merge as text; a conflict in a
  record file keeps both tails. Derived state is made at read time
  and never kept in git, or made only on `main` and taken as ours at
  a merge. Immutable files never conflict. Where git leaves a
  conflict standing, Claude lays both sides out and the principal
  decides; the forge merges nothing itself.

What this layer deliberately does not fix is the wording and the
steps of each command, definition, contract, template and script:
those belong to that file.

## If something goes wrong

- A skill whose `argument-hint` is unquoted, in a front-matter with
  CRLF line endings and a hint of two bracketed items, fails to parse;
  the harness then shows the first line of the body as the
  description. Quote every hint.
- A skill an agent names in its front-matter and that does not exist
  is skipped silently at launch. The check `engine` verifies that
  every skill an agent names exists.
- A hook named by a relative path is resolved against the directory
  the session was started in, not the engine root. The two hooks are
  therefore anchored at `${CLAUDE_PROJECT_DIR}`.

## A worked example

One save of a project, `/save my-project`, traced through the layer.

1. You type the command. `CLAUDE.md` is already in context from the
   start of the session; its list of commands names `/save` in one
   line, and the description of every skill is in context too. At
   this prompt, as at every one, `scripts/hook-walkthrough.py` has
   printed its lines on the walkthrough and the conduct, started by
   `python` from `.claude/settings.json`.
2. Claude Code reads `.claude/skills/save/SKILL.md`. Nothing of its
   body was in context before this moment.
3. The skill runs the check `light`, unless you gave `--quick`.
   Claude launches `.claude/agents/check-light.md` as a subagent. At
   its launch the contract `.claude/skills/check-contract/SKILL.md`,
   which the agent's front-matter names, is injected whole, and
   `CLAUDE.md` goes along. The agent reads the project from disk,
   stays read-only and returns its report with its findings
   unnumbered.
4. Where the check found something, the command files the report
   into the project's `reviews/` and gives the findings their IDs;
   `scripts/forge-report.py` completes the file name with the time
   and a hash. The states a finding can take are those of
   `templates/ledger.md`. The findings are settled by walkthrough,
   whose shape is read from `.claude/skills/walkthrough/SKILL.md` for
   the occasion. A run that finds nothing files nothing.
5. The skill runs `python scripts/forge-save.py`, which commits and
   pushes on whatever branch is checked out; `scripts/forge_repos.py`
   beside it supplies the engine root, the git check and the list of
   repositories a bare or a slug form visits. Had Claude reached for
   `git commit` in the Bash tool instead, `scripts/hook-git.py` would
   have denied it and named the script; `git` in the other shell tool
   is denied by `settings.json` outright.
6. A conflict the script meets is left standing, not aborted, and
   settled in the step of a conflict: Claude lays both sides out as a
   walkthrough, the principal decides, Claude writes the wording, and
   the finishing commands of git run on the hook's ask. Which files
   merge as text and which are taken as ours is what the
   `.gitattributes` of that repository tells git.

Untouched by the whole run: `tests/`, since a save never runs the
tests; `tmp/`; `docs/`; and every render, since a save makes none.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [The tests](../about/the-tests.md): what the tests cover and what the fixture is.
- [The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md): the two fixed files of the root.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
