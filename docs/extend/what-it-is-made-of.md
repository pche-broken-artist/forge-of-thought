---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 2e550370b26b637b
inputs:
  - .claude/reference/repository-layout.md
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Portability
  - CLAUDE.md#The system's own project
  - tmp/README.md
  - projects/README.md
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/10-intent.md#POS.1920
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/40-solution-design.md#The instruction layer
  - projects/forge/40-solution-design.md#The commands
  - projects/forge/40-solution-design.md#SOL.0300
  - projects/forge/40-solution-design.md#SOL.0330
  - projects/forge/40-solution-design.md#SOL.0460
  - projects/forge/40-solution-design.md#SOL.0500
  - projects/forge/40-solution-design.md#SOL.0900
  - projects/forge/40-solution-design.md#Across the parts
  - .claude/settings.json
---

# What the forge is made of

The operating layer of the forge is the set of files that Claude Code
reads and runs: one core that is always loaded, files that are read
when their situation arises, and scripts that do the deterministic
work. This page is for the extender, who changes the forge or adds to
it. It names each part of the [engine](../reference/glossary.md) (the
repository a user clones, with no project in it), says what the part
is and when it is loaded, and traces one command through the parts.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The core. It carries what must hold in every session and for every subagent. A rule of one artefact is not here: it stands in the [definition](../reference/glossary.md) of that artefact. | Always. Claude Code loads it into every session (one run of Claude Code) and into every subagent (a separate run of Claude that sees the files it is given and never the conversation). |
| `.claude/reference/` | What the core names and leaves to be read on demand: the table of commands, the table of ID prefixes and the layout of the engine's root. | On demand. The layout is read when a file of the engine is looked for. |
| `.claude/skills/<name>/SKILL.md` | A [skill](../reference/glossary.md), one per command. "Command" is the word for what is invoked by slash. "Skill" names the shape of the file. | When the command is invoked. Only the description of each command stays in the always-on context. |
| `.claude/skills/forge/states/<state>.md` and `.claude/skills/recipe/genres/<genre>.md` | Supporting files of the two dispatchers (`/forge` and `/recipe`, each a thin skill with one file per target). A state file is the definition of one artefact. A [genre](../reference/glossary.md) file is the definition of one genre of [recipe](../reference/glossary.md). Neither is registered as anything. | Read by path when its dispatcher is invoked for that state or genre. |
| `.claude/skills/<kind>-contract/SKILL.md`, `.claude/skills/docs-contract/SKILL.md` and `.claude/skills/walkthrough/SKILL.md` | Skills that are not commands. A [contract](../reference/glossary.md) carries what the agents of one kind share: there are three for the reviewers (`critic-contract`, `challenger-contract`, `check-contract`) and one for the two agents of the documentation. The walkthrough skill carries the shape of the walkthrough (the method in which a list of items is worked one item at a time) and of the [elicitation interview](../reference/glossary.md). | A contract is injected whole by Claude Code at the launch of every agent whose front-matter names it under `skills:`. The walkthrough skill is read whenever a walkthrough or an interview runs. |
| `.claude/agents/` | One file per critic [lens](../reference/glossary.md), per challenger [persona](../reference/glossary.md) and per check, and the documentation's planner and writer. A reviewer's file carries its front-matter and its Lens section and nothing else. | When a command launches the agent in a subagent. |
| `.claude/settings.json` | Two [hooks](../reference/glossary.md), three deny rules and the attribution switched off. The per-prompt hook runs `scripts/hook-walkthrough.py`, which repeats the one-item rule of the walkthrough and lines of conduct. The git hook runs `scripts/hook-git.py`, which holds the line between reading git and writing it. The deny rules forbid reading `~/.ssh`, reading `~/.aws` and git in the PowerShell tool (the other shell tool, which the git hook does not watch). | The per-prompt hook runs at every prompt. The git hook runs before every call of the Bash tool. |
| `templates/` | The templates ([Templates](../reference/templates.md)): the canonical skeletons, the player page's template (`templates/html-player.html`) among them. A template named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by: an artefact, a critic lens, a challenger persona, a check. A file made from a template keeps of its comments only the one line that names it (`<!-- Shape: templates/<name>.md -->`), where the template has it. | Read when a command makes a file from it. Read by a check that compares a file with the template it names. |
| `scripts/` | Programs in Python 3.8 or newer that do the deterministic work, such as git, the conversion of documents and the making of the [ledger](../reference/glossary.md) (the file of a project's state, made at read time and never kept in git). The two hooks are among them. The modules several scripts share lie beside them: `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py` and `forge_check.py`. It is the only platform-bound layer. | Run, not read. A command or a hook starts a script as `python scripts/<name>.py`. |
| `tests/`, `pytest.ini` and `.github/workflows/tests.yml` | The engine's tests ([The tests](../about/the-tests.md)). `tests/conftest.py` holds what the tests share. `tests/fixture` is the synthetic project that every test copies. `pytest.ini` says how pytest runs them: `tests/` as the path, `scripts/` on the import path. The workflow is the CI. | Run by `/test`. Run in CI at every push and pull request, on Linux and Windows. Run by a release of the engine, never by a save. |
| `.gitattributes` | The engine's own ways of merging by path, for its derived files at the root. | Read by git at a merge. |
| `.mailmap` | Git's own mapping of the author's names in the history to one handle. The history itself is untouched. | Read by git. |
| `tmp/` | The engine's working folder. It holds what the scripts and commands make on the way to a result, such as the tasks of a documentation run or a check's report before it is filed. The folder is in git with its own `README.md` and `.gitignore`. Its contents never are. Nothing in it is a source of truth. | Written by the script or command that needs it. No check, no ledger and no [history](../reference/glossary.md) reads from it. A run is kept for inspection and deleted by hand, never by a script. |
| `projects/` | Where every project lives, each a git repository of its own that the engine does not track ([Projects and the engine](../about/projects-and-the-engine.md)). The directory is gitignored but for its own `README.md`. The forge's own project (`projects/forge`) is one of them. Whoever develops the engine clones it beside the engine. No user needs it. | The files of a project are read when a command works on that project. Nothing a user runs reads `projects/forge`. |
| `docs/` | The generated documentation ([The documentation](../about/the-documentation.md)): pages of one topic each and their index, made by `/document` from the documentation map `docs-map.md`, which lies beside the ledger of the owning project. `docs/videos/` does not belong to the documentation. It is the public folder of the videos: the player files of the projects and the player page. | Read by people. `/man` routes a question in free words through the index `docs/README.md` and reads the pages it chooses. |
| `SECURITY.md` and `CODE_OF_CONDUCT.md` | The two fixed files of the root ([The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md)). They stand beside the [renders](../reference/glossary.md) of the root (outputs generated from a recipe, such as `README.md`) and are no render: they derive from nothing in the chain of documents. The security policy is the own text of the principal (the person whose thinking is forged). The code of conduct is the Contributor Covenant 3.0 word for word. | Read by people. Neither has a companion, a row or a check. Each changes only on the principal's word. |

The table gathers the root by kind of file. The layout block of the
root, file by file, is on
[Repository layout](../reference/repository-layout.md). To change any
of it, follow [Make a change to the forge](how-a-change-is-made.md).

## What happens

The forge is not a program. It is a set of instructions that Claude
Code reads, with the deterministic work kept at its edge in scripts.
From a typed command to a changed file the flow is one line:

```
CLAUDE.md (always) -> skill (when the command is invoked) -> definition, template, reference file (read by path) -> agent and contract (in a subagent) -> script (run) -> files of the project (state)
```

A command takes the stations it needs. A round of work on an artefact
launches no agent. A review launches one.

Five ideas carry the flow:

1. **One core is always on, and everything else is read when its
   situation arises.** `CLAUDE.md` is loaded into every session and
   every subagent. A command, a definition, a contract or a template
   is a file read when it is invoked. What must hold through a long
   conversation is repeated by a hook at every prompt. Why the core
   is small and the rest is read on demand is on
   [How the rules are held](../about/how-the-rules-are-held.md).
2. **State lives in files.** It lives in Markdown files of the
   project, never in the conversation and never in Claude's memory. A
   project is a directory. It holds the artefacts of the chain, their
   history logs, the ledger, the records of the reviewers and the
   resources.
3. **Isolation is bought with subagents.** A reviewer, a check and a
   render each run in a subagent. The subagent sees the files it is
   given and never the working conversation. All three run on the one
   session model (the model the session runs on).
4. **Git, the conversion of documents and the hooks are scripts.** A
   write of git goes through a script: the scripts are its door.
   Reading git is open. The git hook holds the line between the two.
   It puts the few git commands that finish the settling of a
   conflict to the principal.
5. **Every file has a way of merging, and the forge tells git
   which.**
   - Composed text and the record files merge as text. A conflict in
     a record file keeps both tails.
   - Derived state is made at read time and never kept in git, or it
     is made only on `main` and taken as ours at a merge.
   - Immutable files never conflict.

   Where git leaves a conflict, Claude lays both sides out and the
   principal decides. The forge merges nothing itself.

## A worked example

One check of one project, traced through the layer. The slug
`my-project` is a placeholder. You type one line:

```
/check project my-project
```

1. **The core and the hook.** `CLAUDE.md` is in the session already,
   with the description of every command. When you send the line, the
   per-prompt hook of `.claude/settings.json` runs
   `scripts/hook-walkthrough.py`, which adds its lines on the
   walkthrough and on conduct.
2. **The skill.** `/check` is a command. Its skill
   (`.claude/skills/check/SKILL.md`) is loaded now, at the
   invocation.
3. **The agent and its contract.** The skill launches one agent
   (`.claude/agents/check-project.md`) in a subagent. The file holds
   its front-matter and its Lens section and nothing else. The
   front-matter names `check-contract` under `skills:`, and Claude
   Code injects `.claude/skills/check-contract/SKILL.md` whole at the
   launch. The subagent is given the target path and nothing else.
   `CLAUDE.md` is loaded into it as into every subagent.
4. **The templates.** The agent reads the files of
   `projects/my-project`. A file made from a template names it in one
   line (`<!-- Shape: templates/<name>.md -->`). The agent reads the
   whole file against that template in `templates/`: the header, the
   fixed parts and fields in their order, the words the template
   gives. The agent writes nothing. It returns its report with the
   findings unnumbered.
5. **The filing.** The `/check` procedure files the report word for
   word and gives the findings their IDs. Before it is filed, the
   report lies in `tmp/`. `scripts/forge-report.py` gives it its
   unique name. The report of a check that found something is filed
   as
   `projects/my-project/reviews/YYYY-MM-DD-check-project-HHMM-<hash>.md`
   and is immutable from then on.
6. **The walkthrough.** The findings are settled by walkthrough.
   `.claude/skills/walkthrough/SKILL.md` is read now, and the
   per-prompt hook repeats the one-item rule at every prompt. What
   `accept` writes is defined in the skill of `/check`. What
   `reject`, `park` and `obsolete` write is defined in the
   walkthrough skill.
7. **The write.** What was settled is written in one round. A
   settled finding leaves a `closed` record in the history of the
   artefact, and `scripts/forge-record.py` appends a record at the
   end of its file. `scripts/forge-ledger.py` makes the ledger at
   read time, and the ledger reads the filed report.

The trace passed the core, the settings, one skill of a command, one
agent with its contract, the templates, the working folder, the
walkthrough skill, the scripts and the project. It wrote nothing to
git. A save is another command, and it commits and pushes through a
script.

## See also

- [Repository layout](../reference/repository-layout.md): the layout
  block.
- [Templates](../reference/templates.md): every template.
- [How the rules are held](../about/how-the-rules-are-held.md): why
  the core is small and the rest on demand.
- [The tests](../about/the-tests.md): what the tests cover and what
  the fixture is.
- [The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md):
  the two fixed files of the root.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  every project, the forge's own among them, is a repository of its
  own.
- [Make a change to the forge](how-a-change-is-made.md): changing any
  of it.
- [The documentation](../about/the-documentation.md): what `docs/`
  and the documentation map are.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
