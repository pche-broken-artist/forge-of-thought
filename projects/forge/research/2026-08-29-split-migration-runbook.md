---
project: forge
type: research
topic: step-by-step migration of this instance to the split engine (public engine, projects as repositories of their own)
date: 2026-08-29
derived_from: 00-brief-public-engine.md v1.0; 10-intent.md v2.21 (POS.0940–0980, REJ.0140–0150); research 2026-08-29-git-engine-projects-separation.md
status: immutable
---

# Migration runbook — from one monorepo to the split engine

## Question

How exactly is the engine/projects split (POS.0940) executed on this
instance — in what order, with which commands, and with which checks —
so that the public engine repository starts clean, the company
projects and the full history stay where they are, and every step
short of the public push can be rolled back?
The brief lists seven steps; this note turns them into a runbook with
the operating-layer work interleaved at the right moments. Nothing here
is a decision: every step realises a position of intent 2.21, and the
principal drives the execution at the terminal with Claude. Deviations
found while executing are recorded in the ledger (Waiting on
principal), never in this note.

Boundary: this note lives in the public forge project and therefore
names no company, host, address or template file. `<company>` stands
for the company; the real values live in the conversation, in
`CLAUDE.local.md` and in the git configuration — never in the engine.

## Answer in short

Four phases, in this order: **(A) move the projects out** — company
library first, then the two company projects, each into a repository
of its own on the company host, and drop them from the engine's index;
**(B) rebuild the operating layer** to intent 2.21 (gitignore,
instance files, scripts, templates, commands, recipes) while still on
the old history, saving normally, so every step is reversible and
`/check-forge` keeps watching; **(C) purge and publish** — rewrite the
forge project within the boundary, grep for traces, start the fresh
history, push to the new public remote, archive the company copy;
**(D) verify** by a fresh clone elsewhere, then approve intent 3.0 and
tag. The full record — the history with the company projects in it —
stays exactly where it is today, on the company host, archived
read-only. Operating layer
before fresh history is the one ordering rule that matters; the rest
is sequence for convenience.

Reversibility: phases A and B are ordinary commits on the existing
repository and are undone by git; the rollback point is a tag set
before the first step (Phase 0). Phase C is the one-way door for the
*public* repository only — the company copy is never rewritten, so
the old state is always there to return to. Rollback per phase is in
its own section at the end.

## Phase 0 — rollback point

Precondition: working tree clean (`scripts/forge-status.ps1`), the
last `/save` pushed.

```
git tag pre-split
git push origin pre-split
```

The tag names the last monorepo state on the company host. Every
rollback below returns to it.

## Phase A — move the projects out

Order: library first (the deck template must have a home before
`local/` disappears), then the two company projects. Every project
repository lands on the **company host** — the projects are company
content.

### A1 — the company library
1. `/new-project lib-<company>` — after B4 exists it scaffolds by
   kind; until then scaffold `library` by hand: `ledger.md` with
   `kind: library` in the header, `sources/00-INDEX.md`,
   `research/00-INDEX.md`, nothing else (POS.0970). Doing A1 after B4
   is simpler; the order here is only the brief's.
2. Move the `.potx` from `local/` into
   `projects/lib-<company>/sources/` (keep the file name).
3. `/ingest` (bare sweep) in the library — registers and indexes it.
4. Initialise its repository and push:
   ```
   git -C projects/lib-<company> init -b main
   git -C projects/lib-<company> add -A
   git -C projects/lib-<company> commit -m "lib-<company>: library project, deck template"
   git -C projects/lib-<company> remote add origin <company-host>/lib-<company>.git
   git -C projects/lib-<company> push -u origin main
   ```
   (Direct git here is legitimate: the scripts become the door only
   once they are rewritten in B3; until then this is the one-off act
   the brief names.)

### A2 — agentic-platform and flow-ba
For each `<slug>`:
1. Initialise the nested repository from the current content:
   ```
   git -C projects/<slug> init -b main
   git -C projects/<slug> add -A
   git -C projects/<slug> commit -m "<slug>: moved out of the forge monorepo (earlier history in the archived monorepo)"
   git -C projects/<slug> remote add origin <company-host>/<slug>.git
   git -C projects/<slug> push -u origin main
   ```
   The project's own history begins here; its earlier history stays
   in the monorepo on the company host (archived in C4) — accepted in
   DEC.0080.
2. Drop it from the engine's index, keeping the files on disk:
   ```
   git rm -r --cached projects/<slug>
   ```
   Do this **before** the gitignore change in B1 — an already-tracked
   path is not affected by `.gitignore`, and git would otherwise start
   reporting the nested repository as an embedded one.
3. Commit in the engine (one commit for both projects is fine).

Check: `git status` in the engine root shows neither project;
`git -C projects/<slug> status` is clean.

## Phase B — rebuild the operating layer to intent 2.21

Still on the old history, saved with `/save` as usual so
`/check-forge` reports what the intent and the core still disagree on.
Expect the pre-save check to flag the gap until B is complete; accept
the remaining findings knowingly per save.

### B1 — `.gitignore`
Replace the `local/` block with:
```
projects/*
!projects/forge
```
`projects/*`, never `projects/` — the re-include fails silently
otherwise (verified in the git research). Keep
`.claude/settings.local.json`, the Windows noise and Office lock
patterns. Confirm: `git check-ignore -v projects/agentic-platform` hits
the rule; `git check-ignore projects/forge` reports nothing.

### B2 — instance files
1. `templates/CLAUDE.local.md` (new): two placeholder lines —
   Principal, Conversation language — plus a comment saying the file
   is copied to the engine root and never committed.
2. Copy it to `CLAUDE.local.md` at the root and fill in the values.
3. `.claude/settings.json`: remove `"model"`; keep the deny rules.
   Create `.claude/settings.local.json` with the model (already
   gitignored). POS.0930/0950.
4. Delete `local/` entirely, `local/README.md` included (REJ.0140).

### B3 — scripts (POS.0550, POS.0940, POS.0830)
`forge-save.ps1`: remove the remote URL, `user.name`/`user.email`
and the first-run `git init`/`remote add`; add the repository loop —
bare = engine plus every `projects/*/.git` with changes, each its own
commit; slug = that repository, `forge` meaning the engine; no origin
→ commit and a note; never `git add -f`, never `git clean`.
`forge-pull.ps1`: bare = engine fast-forward (the upgrade) plus every
project with a remote; slug = one. `forge-status.ps1`: engine plus
every project — state, origin, or "not under git". `md2pptx.ps1`:
`-Template <path>`; drop the `local/` lookup and `default.potx`; help
text and examples updated. Test each on this instance before moving
on (status → pull → save on a trivial change).

### B4 — templates and commands
- `templates/ledger.md`: `kind: thought` in the header (POS.0960).
- `/new-project`: scaffold by kind (`library` = ledger,
  `sources/00-INDEX.md`, `research/` only); creates files only, no git.
- `/spinoff`: calls `/new-project`, no git.
- `/forge` map: a `library` is material, not "waiting for a brief";
  bare map says "not under git" per project.
- `/check`: `library` needs no chain; new finding "project is not a
  repository".
- `/ingest`: bare sweep reports changed files with a question, meaning
  by kind (POS.0180).
- `/recipe presentation` and `templates/recipe-presentation.md`: the
  template is named by path (POS.0740).
- `/save`: routes per repository through the rewritten script.

### B5 — CLAUDE.md
Principal and conversation language → "instance facts live in
`CLAUDE.local.md`"; "conversation in Czech" gone; the named host →
"a git remote"; layout: `local/` gone, `kind` added, the library as a
kind of project, projects as repositories of their own the engine does
not know; Persistence: scripts serve the engine and every
`projects/*/.git`; md2pptx template by path; the instance-facts
sentence under Portability removed.

### B6 — recipes and renders
- `recipes/readme.md`: remove the TEMPORARY relocation notice (the
  instruction and the blockquote in the Template) — it belongs to the
  last edition on the company host only, and the public README must
  carry no company URL; drop the agentic-platform inputs; the worked
  example is replaced by a placeholder sentence until THR.0200 is
  settled; Setup: clone, copy `templates/CLAUDE.local.md` to the root,
  launch Claude Code from the engine root, `forge-pull` = upgrade;
  naming: `forge` and `lib-`.
- `/save` re-renders README and the release-notes head as usual.

Exit check of phase B: `/check-forge` clean, or its findings
explicitly accepted; ledger Documents table current.

## Phase C — purge and publish

### C1 — rewrite the forge project within the boundary (POS.0980)
Walk every file of `projects/forge/` — the brief (already English),
both CTO challenges, the four research notes, the intent (positions
and Version History), decisions, ledger, recipes — and remove every
company-specific name: company name, host URLs, e-mail addresses,
template file names, content of the company projects. Immutability is
knowingly broken once for this; say so in the ledger note of the
migration, not in the files.

### C2 — grep for traces
Keep the list of forbidden strings **outside** the repository (the
conversation or a file in the archive repo), never as a file in the
engine. Run over the working tree:
```
git grep -n -i -e <term1> -e <term2> ... -- . ':!CLAUDE.local.md'
```
Also check file names (`git ls-files | grep -i ...`) and the two
tracked binaries (`logo.png` is fine; there must be no `.potx`).
Repeat after C1 until empty. The old history is not grepped — it is
not going public.

### C3 — fresh history
From a clean tree at the state after C2:
```
git checkout --orphan public
git add -A
git commit -m "Forge of Thought — public engine, intent 3.0 candidate"
git branch -M public main
```
Author identity for this commit and onward: set the private address
**locally** for this repository (`git config user.email <private>`,
`git config user.name ...`) — never in the scripts (POS.0950). Verify
`git log --oneline | wc -l` is 1 and `git log --format=%ae` shows the
private address.

### C4 — public remote, company copy archived
1. Create the public repository on GitHub (name per THR.0200; until
   decided, `forge`). Add `LICENSE` (THR.0200) — a commit on the new
   history.
2. `git remote set-url origin <github-url>` — the engine's origin is
   now GitHub. `git push -u origin main`.
3. Tag the approved major once 3.0 is approved (phase D), not now.
4. On the company host: **archive** the old project (Settings →
   General → Advanced → Archive project): read-only, a banner saying
   so, still cloneable, reversible. Before archiving, set its
   description to one sentence pointing to the new homes. This
   archived monorepo is the full record. The local clone keeps `pre-split` and the old `main` until
   the principal deletes them.
5. `.gitignore` is already right; confirm `git status` shows no project
   and that `git ls-files projects/` lists only `projects/forge/`.

## Phase D — verify, approve, tag

1. Fresh clone into a directory outside the current one:
   ```
   git clone <github-url> forge-verify
   ```
2. Copy `templates/CLAUDE.local.md` to the root, fill it in; create
   `.claude/settings.local.json` with the model. Launch Claude Code
   from the clone root.
3. `/forge` — the map reports the forge project and no others;
   `/new-project test` — scaffolds, "not under git"; `git -C
   projects/test init` and `/forge` again — under git, no origin;
   `scripts/forge-status.ps1` — engine plus `test`; `forge-pull` —
   fast-forward, projects skipped or pulled; `forge-save.ps1 test` —
   commit with the "no origin" note. `/check-forge` clean.
4. Delete `forge-verify`.
5. Back in the working copy: pull the company projects into
   `projects/` by cloning them from the company host if they are not
   already there (they are, from A); confirm `/forge agentic-platform`
   works unchanged — condition 4 of the brief (seamless work).
6. `/forge intent` → approve **3.0**; `/save`; `git tag v3.0` and
   `git push origin v3.0` (the scripts do not tag — a tag per approved
   major is a one-off act at approval, like `git init` for a project).
   Release notes: the Unreleased head becomes the 3.0 section.

## What can go wrong

- **Tracked files not ignored.** If B1 runs before A2's `git rm
  --cached`, the projects stay tracked and the fresh history (C3)
  publishes them. A2 before B1, and C2 catches the rest.
- **The re-include fails silently** with `projects/` instead of
  `projects/*` — `projects/forge` vanishes from the fresh history.
  Check with `git check-ignore` and `git ls-files projects/`.
- **Traces in immutables.** C2 is run over the whole tree, file names
  included, and repeated until empty; the forbidden-term list never
  enters the repository.
- **Author leaks.** The commit author of the orphan commit is whatever
  git config says at that moment; set the private identity locally
  before C3 and verify with `git log --format=%ae`.
- **Nested repository seen as embedded.** Symptom: git warns "adding
  embedded git repository". Cause: the path is still tracked or not
  ignored. Fix: `git rm -r --cached <path>`, then B1.
- **Scripts run against the wrong repository.** After C3 every script
  loops over `projects/*/.git`; test on this instance (B3) before C.
- **The library template unreachable.** `md2pptx.ps1 -Template` takes
  a path; a machine without the library repository has no template and
  Claude designs the visuals — by design (POS.0740).

## Rollback

Every rollback returns to `pre-split` on the company host. What is
undone depends on how far the migration got.

- **After Phase A (projects moved out).** In the engine:
  `git reset --hard pre-split` restores the tracked projects (files
  and index). Delete the nested repositories' metadata so the engine
  owns the files again: remove `projects/<slug>/.git` for each moved
  project (the files themselves are identical to what `pre-split`
  restored). Delete the new project repositories on the company host
  if they are not to be kept. Move the `.potx` back from the library
  to `local/`.
- **After Phase B (operating layer rebuilt).** Same reset —
  `git reset --hard pre-split` — undoes every operating-layer commit
  at once; if only one step is to be undone, `git revert <commit>`
  keeps the rest. Recreate `local/` from the tag; `CLAUDE.local.md`
  and `.claude/settings.local.json` are gitignored and may simply be
  deleted or kept (the tag's `settings.json` carries the model
  again). Push to the company host with `forge-save.ps1` from the
  tag's version of the script if the rewritten one no longer knows
  the remote (check out `scripts/` from the tag first:
  `git checkout pre-split -- scripts/`).
- **After Phase C, before the push to GitHub.** The orphan branch is
  local only: `git checkout main` (the old history is still there),
  `git branch -D public` (or whatever the orphan was renamed to — if
  it was already renamed to `main`, the old `main` is reachable as
  `pre-split` and `origin/main`: `git checkout -B main origin/main`).
  Then the Phase B rollback if wanted.
- **After Phase C, pushed to GitHub.** Delete the GitHub repository
  (or make it private) — nothing else holds the fresh history. Reset
  the local origin: `git remote set-url origin <company-host-url>`,
  then as above. Unarchive the company project if it was archived.
  The company host was never rewritten, so the full record is intact
  by construction.
- **After Phase D (3.0 approved, tagged).** Not a rollback case any
  more: a defect found now is fixed forward on the public engine
  (3.1, …). Should the public repository have to disappear, the
  company host still holds `pre-split` and the whole old `main`.

What is never rolled back automatically: repositories created on the
hosts (the library, the project repositories, the public engine) —
deleting a remote repository is the principal's explicit act each
time.

## Consult when

Executing the migration (this is the checklist), when a step fails
and the question is what depended on it, or when a second instance
(another principal) later asks how the split was done.
