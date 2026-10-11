---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: c3c940281de11d5a
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
program. This page is for you who want to change it. It says which
files make up the operating layer, what each kind of file is, when
the harness (Claude Code, the program that runs Claude and loads
these files) loads it, and where to read what a thing does.

## When to use it

Before you change anything of the forge, to find the file that owns
what you want to change. After something behaved unexpectedly, to
know which files were in play at that moment.

## What you do

Find the kind of file in the table, open the file, and read it. What
a thing does is said in its own file and nowhere else. The whole
layout, directory by directory, is on
[Repository layout](../reference/repository-layout.md); the
skeletons, one by one, are on [Templates](../reference/templates.md).

Several rows speak of a subagent: an isolated run of Claude that
sees the files it is given and never the working conversation, on
the one session model.

| Path | What it is | Loaded when |
|---|---|---|
| `CLAUDE.md` | The universal core: the roles, the prime directives, the working methods in short, the document kinds, the chain, the layout, persistence, versioning, the ID scheme, the reviewers, the ledger and the list of commands. A rule of one artefact is not here but in that artefact's definition. | Always on: in every session and in every subagent. |
| `.claude/skills/<name>/SKILL.md` | One skill per command. "Command" is the word for what you invoke by slash; "skill" names the file shape. A command that writes carries `disable-model-invocation: true` in its front-matter and starts only on your word. | Read when the command is invoked. |
| `.claude/skills/forge/states/<state>.md`, `.claude/skills/recipe/genres/<genre>.md` | Supporting files of their dispatcher: one definition per artefact of the chain, one per genre of recipe. Each carries a description and no registration field. | Read by path by the dispatcher, when it is invoked with that state or genre. |
| `.claude/skills/<kind>-contract/SKILL.md` | The contracts of the reviewers (`critic-contract`, `challenger-contract`, `check-contract`) and the contract of the documentation agents: what every member of a kind shares. Not user-invocable. | Preloaded into the agent at launch, named in the agent's front-matter under `skills:`. |
| `.claude/skills/walkthrough/SKILL.md` | The shape of the walkthrough (the method by which a list of items needing the principal's decision is worked one item per message, each closed with a verdict line) and of the elicitation interview. Not a command. | Read whenever a walkthrough or an interview runs. |
| `.claude/agents/` | One file per critic lens, challenger persona and check: front-matter and Lens section only, `model: inherit` declared. Beside them the planner and the writer of the documentation. | Loaded when launched as a subagent, its contract injected with it. |
| `.claude/settings.json` | The deny rules that keep Claude from raw `git`, and the per-prompt hook that starts `scripts/hook-walkthrough.py`. | Read by the harness when the session starts; the hook it names runs at every prompt. |
| `templates/` | The canonical skeletons: of every document of a new project, of a recipe by genre (`recipe-<genre>.md`), and one `<type>-definition.md` per type the forge is extended by (an artefact, a critic lens, a challenger persona, a check). Where a shape has no other owner, its skeleton is here. | Read when a file is born from it. |
| `scripts/` | Python, run as `python scripts/<name>.py`: the git scripts, the conversions of documents, the history of one item, the hook and the three scripts of the documentation. What several share lives in a module beside them (`forge_repos.py`, `forge_tools.py`, `docs_map.py`), never twice. Each script carries its help in its module docstring. | Run on demand, by a command or by you from the shell; the hook at every prompt. |
| `projects/forge/` | The forge's own project, a thought project like any other: its brief, intent and solution design, its documentation map, and the recipes from which the engine's README, release notes and CONTRIBUTING are rendered. | Read when a command works it, as any project is. |
| `docs/` | The generated documentation: pages of one topic each and their index, made from the map beside the ledger of `projects/forge/`. | Written by `/document`. Not an instruction file: nothing loads it. |

The principal is the person whose thinking the forge works; you,
the extender, may be the same person in another role. The root also
carries the renders `README.md`, `RELEASE-NOTES.md` and
`CONTRIBUTING.md`, the avatar `logo.png` and the `LICENSE`. They are
outputs and a licence, not instructions: nothing loads them, and a
render is regenerated from its recipe, never edited by hand.

## What happens

One prompt travels the layer like this.

1. You type a prompt. The hook named in `.claude/settings.json`
   runs `scripts/hook-walkthrough.py`, which adds its lines to the
   context: the one-item rule of the walkthrough with the verdict
   line that closes a proposition, a pointer to
   `.claude/skills/walkthrough/SKILL.md`, and three lines of
   conduct. You should now see the rule kept in Claude's answers: a
   list is worked one item per message.
2. Claude reads the skill of the command you invoked,
   `.claude/skills/<name>/SKILL.md`, and follows it. You should now
   see Claude doing what that file says and nothing beside it.
3. The skill reads what it needs by path: the definition of the
   target artefact or of the genre, and the skeleton from
   `templates/` where a file is born. You should now see the
   questions of that definition where the command runs by
   elicitation.
4. Where the command needs isolation, it launches an agent of
   `.claude/agents/` as a subagent, its contract preloaded and
   `CLAUDE.md` inside it. Where the work is deterministic, it runs a
   script with `python scripts/<name>.py`. You should now see the
   agent's report returned to the session, or the script's output.
5. The command writes files of the project: the artefact with a
   record appended to its history, the ledger (the project's single
   source of truth for state) brought current, a reviewer's report
   filed under `reviews/` or `challenges/`, a render under
   `renders/`. You should now see the files changed on disk, each
   where the layout puts it.

Four ideas carry this flow.

- One always-on core, and everything else read when its situation
  arises. `CLAUDE.md` is in every session and every subagent. A
  command, a definition, a contract or a template is a file read
  when it is invoked. What must hold through a long conversation is
  repeated by the hook at every prompt. The reason the core is kept
  small is on [How the rules are held](../about/how-the-rules-are-held.md).
- State lives in Markdown files of the project, never in the
  conversation and never in the assistant's memory. A project is a
  directory: the artefacts of the chain, their history logs, the
  ledger, the records of the reviewers and the resources.
- Isolation is bought with subagents. A reviewer, a check and a
  render each run in one that sees the files it is given and never
  the working conversation, all on the one session model.
- Deterministic work is scripts. Git, the conversion of documents
  and the hook are scripts. The harness denies Claude raw `git`, so
  the scripts are the only door, reading state included.

## What you have afterwards

You have the file that owns the thing. What it does is read there:

- a command: its skill, which carries its steps;
- an artefact: its definition under `.claude/skills/forge/states/`,
  which owns its rules and says in its Aim when the artefact is
  complete; its template says what comes out;
- a reviewer: the Lens section of its agent file for what it reads
  and goes after; its contract for the conduct, the isolation and
  the shape of the report;
- a script: the help in its module docstring (synopsis, what it
  does, what it needs, examples);
- a skeleton: the file itself under `templates/`; some carry a
  comment that says how an older form of the shape is read;
- the documentation and the map it is made from:
  [The documentation](../about/the-documentation.md).

How any of it is changed, recorded and released is on
[Make a change to the forge](how-a-change-is-made.md). The words
used here are each given one line on the
[Glossary](../reference/glossary.md).

## If something goes wrong

- An agent runs without its contract. The harness skips a named
  skill that does not exist, silently. `/check engine` verifies
  that every skill an agent names exists.
- A command's description shows as the first line of its body. The
  front-matter did not parse: with CRLF line endings an unquoted
  `argument-hint` of two bracketed items fails. Every
  `argument-hint` is quoted.
- A skill and a command file of the same name both exist. The skill
  shadows the command, so a migration is whole, never partial.
- The hook does not run when the session started in a subdirectory.
  A relative path in the hook's command is resolved against the
  session's working directory, not the engine root. The command is
  anchored at the root in exec form: `python` with
  `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
  argument.
- Claude is refused `git`. That is the deny rules at work: the
  scripts in `scripts/` are the only door, reading state included.
- A script does not start because `python` is not found. `python`
  on PATH is the one prerequisite of the scripts; a system that has
  only `python3` gives it that name.
- A commit fails for want of an identity. The forge sets none: the
  identity is git's, resolved per host by `includeIf` stanzas in
  `~/.gitconfig`, and with `user.useConfigOnly = true` a repository
  on a host with no stanza fails aloud instead of taking a default.
  `/setup` offers the stanzas and the guard.

## A worked example

One command traced through the layer: `/save my-project`.

1. You type `/save my-project`. The hook of `.claude/settings.json`
   runs `scripts/hook-walkthrough.py` and its lines enter the
   context. You should now see nothing new on your side yet; the
   lines are for Claude.
2. Claude reads `.claude/skills/save/SKILL.md`. The skill runs the
   check `light` through `/check`, whose procedure is
   `.claude/skills/check/SKILL.md`. A save makes no render. You
   should now see Claude announce the check.
3. `/check` launches the agent `.claude/agents/check-light.md` as a
   subagent, with the target path and nothing else. The harness
   injects `.claude/skills/check-contract/SKILL.md`, named in the
   agent's front-matter, and `CLAUDE.md` is in the subagent as in
   every one. The agent reads the files of `projects/my-project/`
   and verifies the front-matter against the history companion, the
   ledger against the files, the dependencies, the indexes and the
   one form of a source. It stays read-only and returns its report.
   You should now see the report back in the session.
4. Where the check found something, `/check` files the report word
   for word as `projects/my-project/reviews/YYYY-MM-DD-check-light.md`
   and gives its findings their IDs; findings are settled by
   walkthrough. You should now see the path of the filed report.
5. Claude runs `python scripts/forge-save.py` for the project. The
   script imports `forge_repos.py` beside it, which finds the engine
   root, checks for git, lists the repositories a bare or a slug
   form visits and runs git. It recognises the project by
   `projects/my-project/.git`, commits and pushes on whatever branch
   is checked out, under git's own identity: the script carries no
   URL and no identity. Claude could not have run `git` itself; the
   deny rules of `.claude/settings.json` forbid it. You should now
   see the script's report of the commit and the push.

Files of the layer this run never touched: no definition, because no
artefact was worked; no template, because no file was born; no
recipe, because a save renders nothing.

## See also

- [Repository layout](../reference/repository-layout.md): the layout block.
- [Templates](../reference/templates.md): every skeleton, what it is the skeleton of and which procedure creates from it.
- [How the rules are held](../about/how-the-rules-are-held.md): why the core is small and the rest on demand.
- [Make a change to the forge](how-a-change-is-made.md): changing any of it.
- [The documentation](../about/the-documentation.md): what `docs/` and the map are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
