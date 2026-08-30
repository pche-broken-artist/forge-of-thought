---
project: forge
type: research
topic: git patterns for a shared engine beside many independent project repositories
date: 2026-08-29
derived_from: 10-intent.md v2.17 (POS.0760, THR.0130)
status: immutable
---

# Git patterns for "shared engine + many project repositories"

## Question

Does git, or the tooling around it, have a feature for the forge's
target shape — a public engine repository whose clone is the working
directory, with each user project an independent private repository
inside it, the engine upgradable without touching a project? Patterns
surveyed: nested repositories in a gitignored directory, submodules,
subtree, template repositories with sync, scaffolding tools with an
update story (Copier, cruft, Yeoman), the bare-repo and worktree
tricks, parent-directory discovery precedents, and multi-repo helper
tools. Sources fetched 2026-08-29; the nested-repository behaviour was
reproduced locally on git 2.53.0 (Windows 11). Epistemic tags: [V]
verified on the page, [V-test] reproduced locally, [S] inferred.

## Answer in one paragraph

No. Git has no feature for this relation, because every feature it
offers — submodules, subtree, worktrees — models a *dependency*: one
repository containing another's content at a pinned version. The
engine and a project share no history and pin nothing, so the right
mechanism is the absence of one: the engine's `.gitignore` excludes
`projects/*` (the pattern must be `projects/*`, never `projects/`,
or a `!projects/forge` re-include silently fails), each project is an
ordinary repository inside, and git provably does not see it — `git
add -A` in the engine stages nothing and prints nothing, and the
engine's ignore rules have no effect inside the project. Engine upgrade
is `git pull` in the engine root. Everything else surveyed is either
rejected for this case (submodules, subtree, template sync, bare repo,
worktree) or applies only to a different question (Copier for a
per-project skeleton; `gita` or a plain `git -C` loop for
status/pull/save across repositories).

## Nested repositories in a gitignored directory [V-test]

| Test (git 2.53.0) | Result |
|---|---|
| `projects/*` ignored; `git init projects/alpha`; `git add -A` in the outer repo | no output, no warning, nothing staged; `git check-ignore -v` names the rule |
| same nested repo **not** ignored; `git add -A` | `warning: adding embedded git repository`; a `160000` gitlink is staged with no `.gitmodules` |
| outer `.gitignore` has `*.log`; inner repo has `app.log` | inner `git status` shows `?? app.log` — outer rules do not reach the inner repo |

The last row is gitignore's documented cascade: patterns are read from
the file's directory up to the top of *that* working tree; the inner
tree starts at `projects/<slug>/` [V].

**The one real pitfall — the exclusion pattern** [V-test]:

| Pattern | `!projects/forge/` re-include works? |
|---|---|
| `projects/*` | yes |
| `projects/` | **no — silently fails** |
| `projects/**` | **no — silently fails** |

gitignore(5), verbatim: "It is not possible to re-include a file if a
parent directory of that file is excluded. Git doesn't list excluded
directories for performance reasons, so any patterns on contained
files have no effect, no matter where they are defined." [V]

Other pitfalls: `git add -f projects/x` (or an accidental un-ignore)
stages a bare gitlink — clones of the engine get an empty directory;
`git clean -xdf` in the engine deletes every project working tree;
`.claude/settings.local.json` is written at the repository root and
must stay ignored; a project cloned standalone elsewhere carries no
engine [S]; `.git/info/exclude` is the local, uncommitted place for
per-machine ignores [V].

## Rejected patterns

- **Submodules** [V] — a `160000` gitlink pins an exact commit;
  `.gitmodules` is committed; every upgrade is a commit in the
  superproject. Documented pain (Pro Git ch. 7.11): detached HEAD by
  default, unpushed submodules break collaborators, clones without
  `--recurse-submodules` get empty directories, orphan directories on
  branch switch, submodule-pointer conflicts. Both shapes fail here:
  projects as submodules of the engine put **private URLs into the
  public `.gitmodules`**; the engine as a submodule of each project
  lands `CLAUDE.md` one level below where Claude Code looks [S].
- **Subtree** [V] — vendors the engine's content and history into
  every project (`git subtree pull --prefix`), N copies to upgrade,
  `--squash` discipline to keep; a contrib porcelain not packaged on
  every Linux distribution.
- **Template repositories** [V] — GitHub: "branches created from a
  template have unrelated histories"; no update mechanism at all. The
  workarounds — `git remote add template` + `merge
  --allow-unrelated-histories`, or `actions-template-sync` opening a
  PR per downstream repo with `-X theirs` — make an upgrade an N-repo
  merge event that clobbers local edits.
- **Bare-repo dotfiles trick** [V] — a work-tree without `.git` in it;
  hides new files (`status.showUntrackedFiles no`) and breaks every
  tool that walks up to find `.git`, Claude Code's repo-root-bounded
  discovery included [S].
- **`git worktree`** [V] — several working trees of *one* repository;
  cannot host content from different repositories. Inapplicable.

## Applicable to a different question

- **Scaffolding with an update story** [V] — Copier records answers in
  `.copier-answers.yml` and runs a genuine three-way `copier update`
  with inline conflict markers (needs git tags on the template and a
  clean worktree); cruft + cookiecutter falls back to `.rej` files and
  bumps `.cruft.json` even on partial failure (a 2025-07 comparison
  recommends Copier); Yeoman has no update. Relevant only if projects
  one day carry a per-project skeleton that must be kept current —
  never for the engine.
- **Multi-repo loops** [V] — no native git command; `git
  for-each-repo` (2.30) is documented experimental, plumbing for `git
  maintenance`. Dedicated tools: `gita` (0.16.8.2, 2025-11, pure
  Python, active) is the only one worth considering; `repo` (Android;
  Windows "best effort"), `mr`/myrepos (frozen 2018), `meta` (npm
  2021), `gws`/`wstool` (archived) are not. At 5–20 repositories a
  PowerShell 7 loop over `git -C <dir>` in the existing `forge-*.ps1`
  idiom beats all of them.
- **Parent-directory discovery precedents** [V] — EditorConfig walks
  up to the filesystem root or a `root = true` boundary; direnv walks
  up gated by `direnv allow`; ESLint flat config stops at the first
  config found; Node walks up for `node_modules`; git itself walks up
  for `.git`, bounded by `GIT_CEILING_DIRECTORIES`. Config found in a
  parent is an established idiom, with an explicit boundary marker as
  the usual safety.

## Comparison

| Pattern | Engine upgrade | Touches projects | Public/private | What breaks | Fit |
|---|---|---|---|---|---|
| Nested repos in gitignored `projects/*` | `git pull` in the engine root | never | perfect both ways | wrong ignore pattern; `git clean -xdf`; `git add -f` | **excellent** |
| Copier skeleton per project | `copier update` per project | yes | good | conflict markers per project | only for a project skeleton |
| Template + sync | merge per project | yes, N | ok | `-X theirs` clobbers edits | mediocre |
| Submodules | pin bump per consumer | yes | **leaks private URLs** | detached HEAD, empty clones, conflicts | poor |
| Subtree | pull per project | yes, vendored | ok | N copies, `--squash` discipline | poor |
| Bare repo | `git pull` via alias | never | good | breaks `.git` walk-up tooling | not recommended |
| Worktree | — | — | — | single repository only | inapplicable |

## Relevance to this project

- **The mechanism for THR.0130 on the git side is "no mechanism":**
  `.gitignore` with `projects/*` and `!projects/forge`, projects as
  ordinary repositories inside, engine upgrade by `git pull`. Verified
  to be invisible to the engine in both directions.
- **Concrete guards for the scripts:** never `git add -f` under
  `projects/`; refuse or never use `git clean -xd` in the engine root;
  keep `.claude/settings.local.json` and `local/` ignored; document
  that `projects/` is the pattern to never "simplify".
- **Scripts loop over `projects/*/.git`** with `git -C` for bare
  status / pull / save; a project without a remote is committed and
  reported, not pushed.
- **Copier** is the tool to remember if projects ever carry their own
  skeleton to be kept current; not now.

## Sources

git-scm.com/docs/gitignore, /docs/git-worktree, /docs/git-for-each-repo,
/docs/git (environment variables); Pro Git ch. 7.11 "Submodules";
git-subtree(1) (Git for Windows 2.53.0); GitHub docs "Creating a
template repository"; github.com/AndreasAugustin/actions-template-sync;
copier.readthedocs.io (updating, comparisons); cruft.github.io;
github.com/cruft/cruft/issues/206; blenddata.nl "Cruft vs copier"
(2025-07-11); gerrit.googlesource.com/git-repo (README, docs/windows.md);
myrepos.branchable.com; github.com/nosarthur/gita (PyPI 0.16.8.2,
2025-11-17); github.com/mateodelnorte/meta; github.com/fabioz/mu-repo;
editorconfig.org; direnv.net/man/direnv.1.html; eslint.org
configuration files; nodejs.org modules; blog.timhutt.co.uk "Reasons
to avoid Git submodules"; lobste.rs "Never use git submodules";
Atlassian dotfiles tutorial (commands confirmed via paritybit.ca and
martijnvos.dev). Local reproduction: git 2.53.0, Windows 11,
2026-08-29.
