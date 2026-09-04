---
project: forge
title: Public engine — the forge as a standalone public project, user projects in repositories of their own
date: 2026-08-29
author: PCHe
version: 1.0
status: approved
last_change: 1.0 (2026-08-29): locked by the principal after the CTO challenge of the same day; drafts 0.1–0.5 born in the forge.
---

## What I want

I need the forge to stand as a project of its own that I can put on
git without worry. Nothing sensitive in it. Anyone can use it, and
then everyone has some repository of their own projects. One
repository, one project. It would be good if it were still driven
through the forge scripts — pull, status, save — per project, since
we go repository per project.

The goal is publication. Merely separating the company projects from
the engine, for myself, would be a fallback only if publication were
long and complicated; if we can go straight to publication,
separation on its own makes no sense.

**Access rights** are another reason for the split: today anyone
who collaborated had to be on all projects, the forge included. With
one repository per project I can grant access per project.

**Who for, and why** — all of it together, in this order: the first
task is to roll the forge out in the company; at the same time I
want it as a public project — a community might form around it; and
as a showcase of my work.

**Is the engine mine to publish?** Yes — it was built outside any
work assignment. It lived on the company's git only because, at the
time, it carried work information that had not yet been separated
and that must never reach my private GitHub. When it moves to my
private GitHub, the commit author changes to my private address.

## Conditions

1. Separate the development and maintenance of the forge from the
   user projects.
2. Everyone manages their own projects in their own git and gives
   them whatever visibility they need.
3. The forge must be easy to upgrade, and the user must have a tool
   that checks their project's conformance with the new version.
   Inconsistencies everyone fixes themselves with AI, as we do now.
   This holds without any engine version recorded in the project:
   `/check` measures against the current conventions.
4. I want seamless work in the projects, as it is now.
5. The engine carries nothing sensitive and no instance facts.
6. Driven through the forge scripts, on every platform.

Not committing now to the project being usable without the engine.
Public exemplar: either the forge itself, or one created later.

## What we researched and why

Before deciding we ran three researches, because we are not the first
to face this and I did not want to reinvent the wheel: how comparable
projects from the earlier landscape research separate the engine from
user projects and upgrade it; what Claude Code recommends and permits
(plugins, skills, CLAUDE.md); and whether git has a feature for our
problem.

What follows from them: only the shapes that keep the engine *out* of
the project are clean — copying the engine into projects leads
everywhere to manifests, override layers and migrations. Claude Code
has plugins, but a plugin does not carry CLAUDE.md, i.e. the core of
the forge; and commands are discovered only up to the repository
root, so the engine as the working directory works exactly when
launched from its root. Git has no feature for this — submodules,
subtree and worktrees model a dependency, which this relation is not;
the mechanism is a plain gitignore and nested repositories, verified
by test.

Notes in `research/`:
- `2026-08-29-framework-distribution-in-the-field.md` — how eleven
  comparable projects do it
- `2026-08-29-claude-code-packaging.md` — what Claude Code permits
  and forbids: plugins, skills, CLAUDE.md, discovery
- `2026-08-29-git-engine-projects-separation.md` — whether git has a
  feature for our problem

## What looks promising

Not a decision — that belongs to the intent.

**One shape of the engine, now.** The engine as a clone and the
projects as nested repositories in a gitignored `projects/`: meets all
six conditions with no mechanism at all, verified, done in days.

**Plugin — a possible future distribution layer, no preparation
now.** A plugin would give the only real upgrade channel and
project = repository, but it forces changes nobody needs yet
(shortening the core to a bootstrap, rewriting the commands from
`projects/<slug>/` to the repository root, solving multi-project
operations). Superpowers shows how a plugin gets its core to the
user: the CLAUDE.md in its repository is for contributors only, the
user never sees it; the core is a short bootstrap skill that a
SessionStart hook (startup, clear, compact) injects into context,
everything else is skills on demand. We once considered including
the forge CLAUDE.md into the user's — that works (`@import` is
official) but carries only CLAUDE.md, not commands and agents; on its
own it does not replace a plugin. For now we skip plugin preparation
entirely and do only the git split; a CLAUDE.md split is not a cheap
step (435 lines; moving half the rules from always-on to on-demand
is a behaviour change, and "200 lines" is a recommendation, not a
limit).

**Reject:** submodules, subtree, template repository; copying the
engine into projects; the plugin as the only shape right now.

## Where the conversation of 2026-08-29 arrived

Still a proposal — none of it is an intent decision.

### Agreed

1. **Project and git.** We need not police git so hard. `/new-project`
   creates files only and does not touch git; `git init` and the
   remote are the user's one-off act. The scripts recognise a project
   by `projects/<slug>/.git`; without it, status reports "not under
   git" and save/pull skip it; with it, commit and push to origin, or
   commit with a note when there is no origin. No remote configuration
   anywhere — git carries all the information itself (`.git/config`).
   I will have two or three gits: the forge on my public GitHub,
   private projects probably there too, work projects on the company's
   GitLab, where everything is stored today.
2. **The forge project stays in `projects/forge`** (`!projects/forge`);
   moving it elsewhere would only add special cases to the commands.
3. **Library = a project with only `sources/`.** I want a library of
   documents I use across projects — not only company ones. Sources
   are handled as everywhere (`/ingest` by file or link, or upload to
   `sources/` and a sweep indexes it); it has a ledger and an index
   like every project; nothing is redefined. Immutability is not to
   be taken so seriously here: overwrite, or put a new version beside
   it, is the owner's choice (for the company's deck template the
   previous version is irrelevant; for a requirement-writing
   convention it may be useful to say "supports v1 and v2"). Another
   project cites by path. Visibility is governed by its own
   repository. Recommended prefix `lib-`. **The first library is the
   company's** (on the company's GitLab) — and today's `.potx`
   template from `local/` moves into it.
   The library is *not* a condition of publication — the intention
   yes, the implementation when the first library is created. Citing
   across repositories is a dependency, and I take it knowingly: only
   someone with both repositories can read it; the assignment is
   self-contained anyway; the version in the citation is a visible,
   unguarded pin; a check is added when it hurts. Two kinds of
   material: a project's sources are inputs as of a date and
   immutable; a library's documents are maintained by an owner who is
   also their author — overwrite or version beside is their choice;
   registration and index in both cases.
4. **Drop `local/`** — it existed only to keep things out of the
   public repository, which gitignore now handles. No library for my
   own instance yet: `CLAUDE.local.md` at the engine root carries two
   lines directly — principal, conversation language. It must be at
   the root (that is where Claude Code looks for it); on a new machine
   it is copied from the template. The deck template comes from the
   company library.
5. **Project kind `kind: thought | library`** in the YAML header of the
   ledger, default `thought` (today's projects unchanged); the rules of
   a kind live in the engine, the project carries only a data marker;
   a project's CLAUDE.md stays polish, not kind rules (that would copy
   the engine into the project). Not "chain" — I cannot picture
   anything under it.
6. **Output language** = THR.0180 in the intent; the first Czech
   project opens it.
7. Plugin = a later distribution layer, no preparation now.

### Boundary for the forge project going public

Nothing company-specific by name — not the company's name, not URLs,
not e-mail addresses, not the content of the projects. Before
publication the forge project is gone through and rewritten,
**including the immutable artefacts** (this brief, the challenges of
2026-08-17 and 2026-08-29, the research notes) — in this one case we
knowingly break immutability, once. This brief is rewritten into
English before its lock; in Czech it would be useless in public, so
the rule "a brief verbatim in the language it was written in" yields
here.

### History

The public repository starts with a fresh history — filtering by path
(`git filter-repo`) is not enough, the company is also in the text of
commits, intent, challenges and research. The complete record stays
where it is: the company's GitLab copy stays read-only while it
exists.

### Upgrade and versions

Condition 3 holds without an engine version in the project. The engine
gets a git tag at every approved major of the intent. That a new
project starts "not under git" is a property, not a defect.

### What this means for the forge

Directory:

```
forge/                              repo E — public GitHub, fresh history
├── CLAUDE.md                       no instance facts, no fixed language
├── CLAUDE.local.md                 gitignored, 2 lines: Principal, Conversation language
├── README.md  RELEASE-NOTES.md  LICENSE  logo.png
├── .gitignore                      projects/*  !projects/forge  .claude/settings.local.json
├── .claude/  scripts/  templates/
└── projects/
    ├── forge/                      in E
    ├── lib-<company>/              repo, company GitLab — sources/<company>.potx (+ tech stack etc. later)
    ├── agentic-platform/           repo, company GitLab
    └── flow-ba/                    repo, company GitLab
```

Gone: `local/` (including `local/README.md`). No instance library yet.

File by file:

| Where | Change |
|---|---|
| `.gitignore` | `projects/*`, `!projects/forge`, `.claude/settings.local.json`; drop `local/*`, `!local/README.md`. The pattern must be `projects/*`, not `projects/` — otherwise the re-include fails silently. |
| `CLAUDE.md` | principal and conversation language → "instance facts live in `CLAUDE.local.md`"; the named git host → "a git remote"; layout: drop `local/`, add `kind`, the library as a kind of project, projects are repositories of their own that the engine does not know; Persistence: the scripts serve the engine and every `projects/*/.git`; "conversation in Czech" gone; artefact language stays EN for now (THR.0180); md2pptx: template by path, not from `local/` |
| `templates/ledger.md` | `kind:` in the header (default `thought`) |
| `templates/CLAUDE.local.md` (new) | two lines with placeholders (Principal, Conversation language) |
| `scripts/forge-save.ps1` | drop the hard-coded remote URL, `user.name/email`, first-run init; slug = that repository (`forge` = engine); bare = engine + every project with changes, each its own commit; no origin → commit + note; never `git add -f` / `git clean` |
| `scripts/forge-pull.ps1` | bare = engine fast-forward (**the upgrade**) + projects with a remote; slug = one |
| `scripts/forge-status.ps1` | engine + every project: state, origin, "not under git" |
| `scripts/md2pptx.ps1` | `-Template` = path to a `.potx` (e.g. `projects/lib-<company>/sources/<company>.potx`); without it Claude designs the visuals itself; drop `local/default.potx` and the bare-name lookup |
| recipe presentation / `/recipe` | the template is named by its path in the library |
| `/new-project` | scaffold by `kind` (`library` = ledger, `sources/00-INDEX.md`, `research/` only); no git |
| `/forge` map | `library` → material, not "waiting for a brief"; bare: "not under git" on projects |
| `/check` | `library` requires no chain; new finding "project is not a repository" |
| `/spinoff` | calls `/new-project`, no git |
| readme recipe | inputs from agentic-platform gone → exemplar (open); Setup: clone, `CLAUDE.local.md` from the template, launch from the engine root, `forge-pull` = upgrade; naming: forge + lib- |
| forge intent | mining of this brief: POS mechanism (THR.0130 closed), POS instance facts (THR.0090 scripts closed), POS library/kind, THR plugin; candidate for 3.0 + release notes; git tag |

One-off migration (me + Claude at the terminal):

1. the company library: `/new-project lib-<company>` (library), move the `.potx` from `local/` into `sources/`, `/ingest` registers and indexes it; `git init`, remote on the company GitLab, push
2. `agentic-platform`, `flow-ba`: `git init`, commit, remote on the company GitLab, push; in E `git rm -r --cached` both + commit; delete `local/`
3. `CLAUDE.local.md` at the root from the template
4. rewrite the forge project within the boundary above (this brief in English, challenges, research, intent history where it names the company)
5. new public repository on GitHub, fresh history; `origin` of E → GitHub, commit author → private address; the company GitLab read-only archive; grep for company traces before the first push; `LICENSE`
6. verification by a fresh clone elsewhere: `CLAUDE.local.md`, `/new-project test`, `/forge`, scripts

### Open

- exemplar for the README; repository name; licence
- THR.0180 — solve at the first Czech project
- lock the brief → `/forge intent`
