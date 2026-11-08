---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 8bbf5f826d3852fc
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Templates
  - CLAUDE.md#Persistence (git)
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

The forge is not a program: it is a set of instruction files that
Claude Code reads, with the deterministic work kept at the edge in
scripts. This page is for you, the extender, who is about to change
one of those files and needs to know which file holds what, and at
which moment Claude Code loads it. It opens with the table of the
files, follows with the one line of how a session flows through
them, names the ideas that carry the layout, and ends with one
command traced through the layer. Every term of the forge is in the
[Glossary](../reference/glossary.md); the full layout block, file
by file, is on [Repository layout](../reference/repository-layout.md).

## When to use it

Read this page before you touch the forge. A change to the forge is
a change to one of these files, and the file to change is the one
that owns the mechanism: a rule lives in one place and is cited from
every other, so the first question of any change is which file that
place is. How a change is then made, recorded and released is on
[Make a change to the forge](how-a-change-is-made.md). Why the core
is kept small and the rest is read only when its situation arises is
on [How the rules are held](../about/how-the-rules-are-held.md).

## The files

The engine is what a user clones: the root files, `.claude/`,
`templates/`, `scripts/`, `docs/`, `tests/` and `tmp/`, and no
project. "Loaded when" says the moment Claude Code, the harness
(the program that runs Claude and hands it its files), reads the
file, or the moment git or a script does where Claude never reads
it.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The always-on core: the roles, the prime directives, the working methods in short, the document kinds, the chain, the layout, persistence, versioning, the ID scheme, the reviewers, the ledger and the list of commands. A rule of one artefact is not here but in that artefact's definition. | Into every session and into every subagent, always. |
| `.claude/skills/<name>/SKILL.md` | One skill per command. The definitions of `/forge` (`.claude/skills/forge/states/<state>.md`) and the genre files of `/recipe` (`.claude/skills/recipe/genres/<genre>.md`) are supporting files of their dispatcher, read by path and registered as nothing. Five skills are not commands: the three reviewer contracts (`critic-contract`, `challenger-contract`, `check-contract`), the documentation contract (`docs-contract`) and the walkthrough skill (`walkthrough`). | A command's body when the command is invoked; only its description is in the always-on context. A definition or a genre file when its dispatcher reaches it. A contract whole, at the launch of the agent that names it. The walkthrough skill whenever a walkthrough or an interview runs. |
| `.claude/agents/` | One file per critic lens, challenger persona and check (`critic-<lens>`, `challenger-<persona>`, `check-<name>`), each its front-matter and its Lens section and nothing else; and the documentation's planner and writer (`docs-planner`, `docs-writer`). Every agent declares `model: inherit`. | When a command launches the agent as a subagent (an isolated run that never sees the conversation). The agent reads every input from disk in that run. |
| `.claude/settings.json` | The two hooks: `UserPromptSubmit` runs `scripts/hook-walkthrough.py`, `PreToolUse` on the Bash tool runs `scripts/hook-git.py`, both as `python` with the script's path under `${CLAUDE_PROJECT_DIR}` as the one argument. The deny rules: `Read(~/.ssh/**)` and `Read(~/.aws/**)`, the user's two sensitive paths, and `PowerShell(git *)`, git in the other shell tool. The attribution switched off. | Read by the harness. The first hook runs at every prompt; the second before every call of the Bash tool; a deny rule holds throughout the session. |
| `templates/` | The canonical skeletons: of every document a new project gets, of the recipe of each genre (`recipe-<genre>.md`), of a project's `.gitattributes` and `.gitignore`, of the player page (`html-player.html`). A skeleton named `<type>-definition.md` is that of the definition of one member of a type the forge is extended by: an artefact, a critic lens, a challenger persona, a check. | When a file is made from the skeleton: a project is scaffolded, a recipe is composed, a new member of a type is defined, the player page is written by the video conversion. |
| `scripts/` | Python, 3.8 or newer, run as `python scripts/<name>.py`, written to run unchanged on Linux and macOS: the git scripts (save, pull, status, clone, branch, config), the ledger, the history of an item, the name of a report, the migration, the check as a program, the run on another engine and its citation check, the conversions (document to Markdown, render to PowerPoint, to Word, to video), the three documentation scripts (state, index, check), and the two hooks. What several share lives in a module beside them: `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py`. Each script carries its help in its module docstring. | When a command calls it, as the skill says. The two hooks run from `.claude/settings.json`, at every prompt and before every Bash call. The scripts are the door to a write of git; reading git directly is open. |
| `tests/`, `pytest.ini`, `.github/workflows/tests.yml` | The engine's tests: pytest over `tests/`, `conftest.py` with what they share, `tests/fixture` the synthetic project every test copies. `pytest.ini` says how they run: `tests/` as the path, `scripts/` on the import path, so the shared modules import by name. The workflow is CI: at every push and pull request, on Linux and Windows, Python 3.8 and the newest. | Never by Claude in a session. Run by `/test`, by a release of the engine as its first step, and by CI at every push. |
| `.gitattributes` | The engine's own ways of merging by path: its derived files at the root taken as ours. | Read by git at a merge, not by the forge. |
| `.mailmap` | The author's names in the history mapped to one handle. Git's own mechanism; the history itself is untouched. | Read by git when it shows the history, not by the forge. |
| `tmp/` | The engine's working folder: packets, envelopes and profiles of runs on another engine (`tmp/research/<run>/`), the tasks of a documentation run, a dry ledger, the manifest of a migration, a check's report before it is filed. In git with its own `README.md` and `.gitignore`, its contents never. Nothing in it is a source of truth. | Written by the scripts and commands on the way to a result. Read by no check, no ledger and no history. A run is kept for inspection and deleted by hand, never by a script. |
| `projects/` | Every project of the instance, `projects/<slug>/`, each a git repository of its own that the engine does not track: the engine's `.gitignore` ignores `projects/*` whole but for the directory's own `README.md`, so that a clone has the directory and a line on what belongs in it. The forge's own project, `projects/forge`, is one of them, cloned beside the engine by whoever develops it and needed by no user. | By the commands over documents, when they work a project. The engine's repository never reads it. The forge's own project is read by the commands that check, document and release the engine and by the renders of its root files. |
| `docs/` | The generated documentation: pages of one topic each and their index `docs/README.md`, made from the documentation map `docs-map.md`, which lies beside the owning project's ledger and never in `docs/`. `docs/videos/` is not the documentation's: it is the public folder of the projects' player files and the player page `index.html`, served by GitHub Pages; `docs/.nojekyll` keeps Pages from touching it. | Written by `/document`; left alone by it in `docs/videos/`. Read by `/man` when a question in free words is routed by the index. |
| the root files | Beside `CLAUDE.md`: `README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md`, renders of recipes; `SECURITY.md`, the security policy, and `CODE_OF_CONDUCT.md`, the code of conduct, the two fixed files that are no render and derive from nothing in the chain, kept by hand on the word of the principal (the one whose thinking is forged), no companion, no row, no check; `LICENSE`, CC BY 4.0; `logo.png`, the avatar. | Read by humans and by GitHub. The three renders are overwritten by a release; the two fixed files by nothing. |

Every skeleton, one by one, is on [Templates](../reference/templates.md).
What the tests cover and what the fixture is are on
[The tests](../about/the-tests.md). The two fixed files are on
[The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md).
Why every project, the forge's own among them, is a repository of
its own is on [Projects and the engine](../about/projects-and-the-engine.md).
What `docs/` and the documentation map are is on
[The documentation](../about/the-documentation.md).

## The flow

One line, from the prompt to the disk:

```
CLAUDE.md (always on) -> the prompt hook -> the command's skill
  -> its definition, genre file or template
  -> an agent with its contract preloaded, or a script with its module
  -> a file of the project, a page of docs/, a trace in tmp/
  -> git, which merges by .gitattributes
```

## The ideas that carry it

Five ideas hold the layout together; the reasons are the design's.

- One always-on core and everything else read when its situation
  arises. `CLAUDE.md` is loaded into every session and every
  subagent. A command, a definition, a contract or a template is a
  file read when it is invoked. What must hold through a long
  conversation is repeated by a hook at every prompt, because text
  loaded once is not trusted to hold; the cost is that a hook is
  context and not enforcement.
- State lives in Markdown files of the project, never in the
  conversation and never in Claude's memory. A project is a
  directory: the artefacts of the chain, their history logs, the
  ledger (the state of the project, made at read time from its
  documents), the records of the reviewers and the resources. The
  instance's own facts stay out of the engine's files.
- Isolation is bought with subagents. A reviewer, a check, a render
  and a documentation agent each run in a subagent that sees the
  files it is given and never the working conversation, all on the
  one session model. The shared conduct of each kind is one contract
  skill, preloaded at launch, against a copy of the text in every
  agent file.
- Git, the conversion of documents and the hooks are scripts. The
  scripts are the door to a write of git; reading git is open; the
  git hook holds the line between the two and puts the few commands
  that finish the step of a conflict to the principal. What is
  deterministic is a script's; what several scripts share is one
  module beside them, never twice.
- Every file has a way of merging, and the forge tells git which.
  Composed text and the record files merge as text, a conflict in a
  record file two tails kept both; derived state is made at read
  time and never kept in git, or made only on `main` and taken as
  ours at a merge; immutable files never conflict. Where git leaves a
  conflict, Claude lays both sides out as a walkthrough (one item per
  message, each closed with a verdict) and the principal decides.

Two consequences follow for the extender. A new member of a type is
one file: a new check is one agent file, a new layer of the chain is
one definition beside its template, and the dispatcher stays
untouched. A shape with no owner gets a skeleton in `templates/`,
not a second description, so that every shape is said in one place.

## A worked example

One command traced through the layer: `/save my-project`, with
`my-project` standing for the slug of a project.

1. Before Claude reads the prompt, `.claude/settings.json` has run
   `scripts/hook-walkthrough.py` through the `UserPromptSubmit` hook,
   and the one-item rule of the walkthrough and the lines of conduct
   stand in the context once more. `CLAUDE.md` is there already: it
   has been in the context since the session opened.
2. Claude invokes the skill `.claude/skills/save/SKILL.md` through
   the harness's Skill tool. Its body is loaded now, not before; until
   this moment only its description was in the context.
3. The skill runs the check `light`. It launches the agent
   `.claude/agents/check-light.md` as a subagent; at launch the
   harness injects `.claude/skills/check-contract/SKILL.md`, which the
   agent's front-matter names, so that the agent carries the shared
   conduct and only its own Lens section. The agent reads
   `projects/my-project/` from disk, sees nothing of the conversation,
   writes nothing and returns its report with its findings unnumbered.
4. Where the check found something, the command gives the findings
   their IDs and files the report into `projects/my-project/reviews/`,
   its name completed by `scripts/forge-report.py`; the findings are
   settled by walkthrough, its shape read from
   `.claude/skills/walkthrough/SKILL.md`.
5. The skill then commits and pushes through
   `python scripts/forge-save.py my-project`. The script asks git,
   through the shared module `scripts/forge_repos.py`, whether the
   project's directory is the top of a repository; a project that is
   not under git is skipped, since that is a property and not a
   defect. The commit identity is git's own, resolved by the user's
   configuration; the script carries none.
6. Had Claude typed a `git commit` into the Bash tool instead,
   `scripts/hook-git.py`, the `PreToolUse` hook of
   `.claude/settings.json`, would have denied it and named the script
   to use; in the other shell tool, `git` is denied outright by the
   rule `PowerShell(git *)`.
7. Where the push meets a remote that has moved, git merges the
   project's files by the ways `projects/my-project/.gitattributes`
   names (from `templates/gitattributes`); a conflict is left
   standing, not aborted, and settled in the step of a conflict, the
   finishing commands of git run on the hook's ask.

What the run never touched: `tests/`, since a save runs no test;
`docs/` and the root renders, since a save renders nothing; and
`tmp/`, from which no check reads.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [The tests](../about/the-tests.md): what the tests cover and what the fixture is.
- [The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md): the two fixed files of the root.
- [Projects and the engine](../about/projects-and-the-engine.md): why every project, the forge's own among them, is a repository of its own.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
