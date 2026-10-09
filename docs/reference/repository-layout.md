---
generated: 2026-10-09
made: mirrored
inputs:
  - CLAUDE.md
---

# Repository layout

This page lists every file and directory of the engine root, of a
thought project and of a library, with the fact the engine states
about each. It is for the user who looks for where something lives,
for the extender who adds to the engine, and for the evaluator who
wants to see what a project holds.

## The engine root

| Path | What it is |
|---|---|
| `CLAUDE.md` | The universal core of the engine. |
| `CLAUDE.local.md` | Instance facts: those of this machine and its principal, not of the system. |
| `README.md` | For humans. A render, made by `/render readme`. |
| `RELEASE-NOTES.md` | Release notes. A render, made by `/render release-notes`; its shape is `templates/recipe-release-notes.md`. |
| `CONTRIBUTING.md` | For a visitor who wants to say, ask or change something. A render, made by `/render contributing`. |
| `logo.png` | The project avatar. |
| `LICENSE` | CC BY 4.0. The engine is published under attribution. |
| `scripts/` | The scripts: `forge-save`, `forge-pull`, `forge-status`, `forge-clone` and `forge-branch` (git); `doc2md` (document to Markdown); `md2pptx` (deck render to PowerPoint); `md2docx` (render to Word), each of the two by pandoc or by a model; `hook-walkthrough` (the per-prompt hook of `.claude/settings.json`). |
| `.claude/` | The skills (the commands, the reviewers' contracts and the walkthrough method), the agents and the settings. `settings.local.json` holds the session model and is gitignored. |
| `templates/` | The canonical skeletons. |
| `projects/` | Gitignored (`projects/*`) except `projects/forge`. Every other project is a git repository of its own, which the engine does not know. |

## A thought project

`projects/<slug>/` is a project of kind thought: the chain.

| Path | What it is |
|---|---|
| `.git/` | The project's own repository. |
| `README.md`, `RELEASE-NOTES.md` | Renders. |
| `logo.png` | Optional project avatar. |
| `00-brief.md`, `10-intent.md` | The trunk of every project. |
| `NN-<layer>.md` | Layers below the intent, as the project needs them. |
| `threads.md` | The project's open threads. The intent's definition governs it. |
| `00-brief-<name>.md` | Later briefs, one per whole. |
| `<file>.history.md` | History companion of a versioned document. |
| `<file>.history.archive.md` | A history table from before the log. Immutable. |
| `decisions.md` | The decisions record. |
| `ledger.md` | The ledger. Its header carries the project's kind. |
| `sources/00-INDEX.md` | Resource index. Rewritten. |
| `sources/<name>.<ext>` | Immutable external inputs, one form each: `<slug>.md`, the extract of a binary, or the binary itself. |
| `sources/.gitignore` | Originals converted in place. |
| `sources/<slug>/` | A bundle of related files: one source, one ledger entry, catalogued by its own `00-INDEX.md`. |
| `research/00-INDEX.md` | Resource index. Rewritten. |
| `recipes/<recipe>.md` | Render recipes: inputs, audience, instructions, template. Iterated. |
| `recipes/<recipe>.history.md` | The recipe's history. |
| `renders/<recipe>.md` | Generated outputs, overwritten by `/render`, with provenance front-matter. |
| `renders/<recipe>.pptx`, `renders/<recipe>.docx` | The plain file of a render, made by `/render` through pandoc where the recipe names a format. |
| `published/<recipe>.pptx`, `published/<recipe>.docx` | The designed file, made by `/publish` through a model. |
| `reviews/YYYY-MM-DD-critique-<lens>.md` | Immutable critique runs. |
| `reviews/YYYY-MM-DD-check-<name>.md` | Immutable check reports, filed when a check finds something. |
| `challenges/YYYY-MM-DD-challenge-<persona>.md` | Immutable peer reviews. |
| `research/YYYY-MM-DD-<topic>.md` | Immutable research notes. |
| `CLAUDE.md` | Optional project-specific polish. Claude Code's `/export` writes into the working directory, so export outside the project or gitignore it. |

## A library

`projects/lib-<name>/` is a project of kind library: material shared
across projects, with no chain. It holds only the ledger, sources and
research. Its documents are maintained by their owner. Its README is
the catalogue, a render of its recipe.

| Path | What it is |
|---|---|
| `.git/` | The library's own repository. |
| `ledger.md` | The ledger. |
| `README.md` | The catalogue of what the library holds. |
| `logo.png` | Project avatar. |
| `recipes/readme.md` | The recipe of the README. |
| `recipes/readme.history.md` | The recipe's history. |
| `sources/00-INDEX.md` | Resource index. |
| `research/00-INDEX.md` | Resource index. |

## See also

- [About projects and the engine](../about/projects-and-the-engine.md) - why projects are repositories of their own.
