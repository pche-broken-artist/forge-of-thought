---
project: forge
date: 2026-10-10
topic: a user-only distribution of the engine
status: immutable
derived_from: the principal's question of 2026-10-10 after the release of 5.0; 10-intent.md v5.0 (POS.0940, POS.0950, THR.0190, THR.0230); research/2026-08-29-framework-distribution-in-the-field.md; research/2026-08-29-claude-code-packaging.md; the engine's tree measured on disk; web sources below
---

# Research: a user-only distribution of the engine

## Question

Whoever wants to use Forge of Thought clones the whole repository,
and with it `projects/forge`: the forge's own briefs, forty research
notes, thirty-six reviews and challenges, the histories. The
principal's question of 2026-10-10: that material is for those who
want to develop the forge, not for those who want to use it; should
there be a version on GitHub for the user only, how is that done,
what are the standard mechanisms, does it help, and should the forge
do it?

## What a clone carries today

Measured on disk on 2026-10-10, after the release of 5.0 [V]:

| Part | Files | Size |
|---|---|---|
| the working tree without `projects/` | 682 | 5.8 MB |
| of which `projects/forge` | 128 | 3.0 MB |
| of which `projects/forge/research` | 40 | 1.2 MB |
| of which `projects/forge/reviews` | 26 | 0.3 MB |
| `docs/` | 84 | 0.7 MB |
| the operating layer (`.claude`, `scripts`, `templates`) | 82 | 0.45 MB |
| `.git` (the history) | | 20 MB |

So the author's workshop is about half the working tree in bytes
and one directory in the reader's eye; the git history is three
times the whole tree. A user-only tree would save a user 3 MB of
23 MB and one directory he never opens.

## What the engine needs of `projects/forge`

The engine is not separable from its own project without rework
[V]:

- the `engine` check reads the forge intent, its threads and its
  decisions to verify the core against them;
- `/document` without a slug makes `projects/forge` the owning
  project: the map lies beside its ledger, the index carries its
  intent's version;
- `/release forge` runs the `project` and `light` checks on
  `projects/forge` and renders README, release notes and
  CONTRIBUTING from its recipes;
- the README, the release notes and the documentation cite the
  intent and its history by path; the `light` and `project` checks
  verify the ledger's registrations against the directories, so a
  tree with `research/` or `reviews/` removed fails its own checks.

What a user never runs is `/release forge`, `/document` bare and
`/check engine`; what a user does run (`/forge`, `/save`, `/check
light <slug>`) does not touch `projects/forge`. A user-only tree
would therefore have to carry the intent, the solution design, the
ledger, the recipes, the threads and the decisions in any case, and
could drop only the research, the reviews, the challenges, the
sources, the briefs and the history companions, at the price of a
ledger that no longer matches its directories.

## The standard mechanisms, and whether they fit

The forge's own constraints: a user needs git (the save script
refuses an engine that is not a repository; `forge-pull` is the
upgrade channel, a fast-forward from the remote), and Claude Code
must be started from the engine root (the packaging research of
2026-08-29) [V].

1. **`export-ignore` in `.gitattributes`** [V, consensus]. Paths
   marked `export-ignore` are left out of every archive git makes,
   GitHub's "Download ZIP" and the source archives of a release
   among them; a clone is unaffected. The attribute must be
   committed. It fits projects distributed as archives (PHP packages,
   WordPress themes). For the forge it does not fit: a ZIP is not a
   repository, so the save script refuses it and `forge-pull` cannot
   upgrade it; and a tree with the registered directories missing
   fails the `light` check.
2. **A template repository** [V]. "Use this template" copies every
   file into a fresh repository with no history and no upstream;
   nothing is filtered, and the upgrade channel is lost. Made for
   starter kits, not for an engine that upgrades.
3. **Sparse checkout on the user's side** [V, partly from Git's
   own documentation]. A user could clone with `--filter=blob:none
   --sparse` and choose paths; but cone mode, the default, lists
   what to include and cannot exclude one directory, and non-cone
   mode with negation is deprecated. It also puts the burden on the
   user, which is the opposite of what is asked.
4. **A second repository fed from the main one** [V]. The pattern
   of the field: a `dist` repository that a GitHub Actions workflow
   fills on every push to `main` or every release, by `git subtree
   split` (only a subtree, with a synthetic history, reproducible
   commit IDs) or by copying a filtered tree and force-pushing. The
   user clones the second repository and `forge-pull` fast-forwards
   from it; the engine's authors keep working in the first. The
   cost: a workflow, a token with write access to the second
   repository, two addresses to explain, and the filtered tree must
   still pass the forge's own checks, which means a derived ledger
   or a ledger that tolerates absent registered directories.
5. **A release branch in the same repository** [S, my own
   synthesis]. The same as 4 inside one repository: a branch
   `release` (or `user`) that a workflow rebuilds from `main`
   with the workshop filtered out; the user clones with `--branch
   release --single-branch`. Cheaper than a second repository, the
   same filtering problem, and it breaks the forge's own rule that
   `main` is the released line (CLAUDE.md, Persistence).
6. **A Claude Code plugin from a marketplace** [V]. A plugin
   carries skills, agents, hooks and scripts and installs with
   `/plugin marketplace add owner/repo`; users of Spec Kit and BMAD
   get the framework by one command (`uv tool install` from a
   pinned tag, `npx bmad-method install`) and never see the
   contributors' repository. This is the field's answer to the
   question asked: one route for users, the repository for
   contributors. For the forge it is the open thread THR.0190,
   merged into the brief `engine-split` (THR.0230): a plugin
   carries no `CLAUDE.md`, the commands address `projects/<slug>/`,
   and the multi-project operations need a workspace the plugin
   does not provide. Not cheap, and already on the forge's path.

## Does it help

For the user: little in bytes, something in orientation. The
`projects/forge` directory is the one thing in a fresh clone the
README does not tell him to open, and a visitor who browses it on
GitHub sees forty research notes and the author's reviews before
he sees the engine. That is a reading problem, and the field solves
it by words before it solves it by mechanism: Spec Kit and BMAD
both keep their repository as it is and send users to one install
command and contributors to CONTRIBUTING.

Against a split today, three things weigh [V]: `projects/forge` is
the forge run through its own process and the exemplar the README
and the documentation derive from (THR.0200, the public face); the
research is public by design and cited by the intent; and every
mechanism that filters the tree has to be reconciled with the
checks that verify the ledger against the directories.

## Options

| Option | What the user gets | Cost | Fits the forge |
|---|---|---|---|
| A. Nothing changes; the README says in one sentence what `projects/forge` is and that a user never opens it | the same clone, oriented | one line in the readme recipe | yes |
| B. `export-ignore` for the workshop directories | a light "Download ZIP" | one `.gitattributes` line; a ZIP the forge cannot run | no |
| C. A second repository or a release branch filled by a workflow | a clone without the workshop, upgradable by `forge-pull` | a workflow, a token, a filtered tree the checks must accept, two addresses | later, if the question returns |
| D. A plugin from a marketplace | one install command, no repository at all | the engine-split work of THR.0230 | the forge's own path, not now |

## Relevance to this project

**Recommendation: A now, D when the brief `engine-split` is taken
up; not B, and C only if the question returns before D.** The
saving a split offers today is 3 MB of 23 MB and one directory; the
cost is a second distribution to keep true against the checks. What
the user lacks is a sentence, not a repository: the readme recipe
can say that `projects/forge` is the forge's own project, the
exemplar every render and page derives from, and that a user never
needs to open it. The question itself is a position for the brief
`engine-split` (THR.0230): a framework is a package of instances,
and the user's route is the plugin, with the repository for those
who develop the forge. That brief is where the user-only version
is decided, with the three-layer question it belongs to.

What this research does not settle: whether the plugin route is
feasible at all is the research THR.0190 asks for and has not got;
and whether the checks could tolerate a filtered tree is a design
question for option C, not answered here.

## Sources

- git-archive, `export-ignore`: https://git-scm.com/docs/git-archive
- GitAttributes for PHP Composer projects:
  https://php.watch/articles/composer-gitattributes
- GitHub release slimming with `export-ignore`:
  https://www.x-cmd.com/blog/261001/
- GitHub, repository templates:
  https://github.blog/developer-skills/github/generate-new-repositories-with-repository-templates/
- Git sparse checkout (2026-01-24):
  https://oneuptime.com/blog/post/2026-01-24-git-sparse-checkout/view
- git-subtree split: https://man.he.net/man1/git-subtree
- Detaching a subdirectory into its own repository:
  https://betterstack.com/community/questions/how-to-detach-subdir-into-separate-git-repo/
- Claude Code plugins and marketplaces (2026):
  https://www.morphllm.com/claude-code-marketplace
- How the Specify CLI downloads its templates from releases:
  https://instagit.com/github/spec-kit/how-specify-cli-handles-template-download-extraction
- How to install BMad: https://docs.bmad-method.org/start/install-bmad/
- Prior research of this project:
  `2026-08-29-framework-distribution-in-the-field.md`,
  `2026-08-29-claude-code-packaging.md`

Epistemic tags: [V] verified in the source or on disk; [S] my own
synthesis; consensus where the sources agree.
