---
generated: 2026-10-09
made: mirrored
inputs:
  - CLAUDE.md
  - .claude/skills/setup/SKILL.md
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/new-artefact/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/critique/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/check/SKILL.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/spinoff/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Commands

This page lists every command of the forge, in the order of the
Commands table of `CLAUDE.md`: its signature and purpose, then what its
skill says of itself. It is for the user, the extender and the
evaluator who want the whole set at a glance.

"Guarded" is the skill's `disable-model-invocation`: yes means the
command is started only by the principal and never on Claude's own
judgement; no means the skill does not set it.

## The commands

| Command | Purpose |
|---|---|
| `/setup` | first run after cloning the engine: prepare the instance |
| `/new-project <slug>` | scaffold a project by kind: a thought project or a library |
| `/new-artefact <name>` | add a new kind of artefact to the forge |
| `/import-project <git-url>` | bring an existing project into `projects/` |
| `/forge [slug]` | the state map of a project |
| `/forge <state> [slug]` | iterate the target artefact through its definition |
| `/ingest [file] [slug]` | store, register and index external input in sources/; bare = sweep sources/ |
| `/render <recipe> [slug]` | regenerate a render from its recipe |
| `/publish <recipe> [slug]` | make the designed file from a render, through a model |
| `/recipe [genre] [slug]` | compose or iterate a render recipe by genre; bare = the genre roster |
| `/critique [lens] [artefact] [slug]` | run a critic lens on the quality of the documents; bare = the lens roster |
| `/challenge [persona] [artefact] [slug]` | run a challenger persona against the substance; bare = the persona roster |
| `/research <topic> [slug]` | best-practices research into research/, indexed |
| `/ledger [slug]` | state report from the ledger |
| `/check [check] [slug]` | run a check on a project or on the engine; bare = the check roster |
| `/save [slug] [-m "message"] [-Tag name]` | save one repository, or every one with changes |
| `/release [slug] [-m "message"] [-Tag name]` | release one repository from `main` |
| `/spinoff <project> <group> <slug>` | split a group into its own project |
| `/man [command \| method]` | the forge's manual, read from its own definitions |
| `/manual …` | alias of `/man` |

## What each skill says of itself

Each entry gives the skill's `description`, its `argument-hint` and
whether the command is guarded. `/forge` appears once, as one skill
behind two rows of the table.

| Command | Description | Argument hint | Guarded |
|---|---|---|---|
| `/setup` | First run after cloning the engine - create and fill CLAUDE.local.md by interview, set the session model (Fable), offer the git identity per host and the global guard in ~/.gitconfig; never overwrites, runs no git operation | none | yes |
| `/new-project` | Scaffold a new project from templates - a thought project (the chain) or a library (material only); files only, never git | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact to the forge - its position in the forge intent, its definition and template, its prefixes, its reviewers | `<name>` | yes |
| `/import-project` | Bring an existing project into projects/ - clone through scripts/forge-clone.ps1, which reports the commit identity git resolves | `<git-url>` | yes |
| `/forge` | Work the document chain - bare = state map, with a target = iterate that artefact | `[target-state] [project-slug]` | no |
| `/ingest` | Register external input (a file, or text pasted into the conversation) in sources/ - store, catalogue, ask what it is for, nothing more | `[file-or-path] [project-slug]` | yes |
| `/render` | Regenerate a render from its recipe in recipes/ | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed .pptx or .docx from the render of a recipe, through a model - started by the principal only | `<recipe> [project-slug]` | yes |
| `/recipe` | Compose a render recipe by genre - bare = genre roster, with a genre = guided composition | `[genre-or-recipe] [project-slug]` | no |
| `/critique` | Run a critic lens on the quality of a project's documents - bare = lens roster | `[lens] [artefact] [project-slug]` | no |
| `/challenge` | Run a challenger persona against the substance of any chain artefact - bare = persona roster | `[persona] [artefact] [project-slug]` | no |
| `/research` | Research current best practices on a topic; store durable notes | `<topic> [project-slug]` | no |
| `/ledger` | Report project state from the ledger | `[project-slug]` | no |
| `/check` | Run a check on the conformance of a project or the engine with the conventions - bare = check roster | `[check] [project-slug]` | no |
| `/save` | Save the forge to git - the light check, then commit and push; no renders | `[project-slug] [-m "message"] [-Tag name]` | yes |
| `/release` | Release one repository from main - its checks with walkthrough, README and release notes, then /save with the release message and the tag at an approved major | `[project-slug] [-m "message"] [-Tag name]` | yes |
| `/spinoff` | Spin a requirement group off into its own project (principal's explicit decision only) | `<source-project> <group-name> <new-slug>` | yes |
| `/man` | The forge's manual, read from its own definitions - bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill | `[command \| method]` | no |
| `/manual` | Alias of /man - the forge's manual, read from its own definitions | `[command \| method]` | no |

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
