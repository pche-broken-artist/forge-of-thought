---
project: forge
directory: research
updated: 2026-08-29
---

# Index — research of Forge of Thought

<!-- Material index: a light catalogue so that Claude and the principal
know what exists here and what it is for without re-reading the files.
Freely rewritten (like the ledger) while the files it catalogues stay
immutable. Tracks nothing — no processing state, no positions — and is
an automatic input of no command. Registration state lives in the
ledger. Written by /research; verified by /check. -->

### `2026-08-25-comparable-projects-landscape.md`
- **Question:** do projects like Forge of Thought exist — a governed chain from raw idea to a versioned, adversarially reviewed assignment — and if so, what can be borrowed, and how unique is the forge? Three families swept: AI spec-driven frameworks (Spec Kit, BMAD and kin), structured-thinking and adversarial-review tooling (ADR, RFC/PEP, multi-agent critique), requirements standards (29148, INCOSE, BABOK).
- **Answer in short:** many neighbours, no twin. The spec-driven family all runs to code — none stops at an assignment, keeps a verbatim brief or stable never-renumbered IDs; isolated adversarial review is emerging but applied to code, and the forge's blind critic/challenger split is ahead of the field. What the field has and the forge lacks is packaging: challenger rerun deltas and "what I could not assess" sections, a correlated-bias warning when reviewers agree, a review package for different-family reviewers (POS.0800), model tiering in front-matter (THR.0160). Recommendation: do not change the chain; take the four packaging ideas in. Entries carry epistemic tags [V]/[S]/[M].
- **Consult when:** deciding what to adopt from the ecosystem, sharpening the challenger (POS.0420), designing the different-family review package (POS.0800), revisiting model choice (POS.0930 — one model, speed from context), or when asked how unique the forge is.

### `2026-08-29-framework-distribution-in-the-field.md`
- **Question:** how do eleven comparable frameworks (Spec Kit, BMAD, OpenSpec, Superpowers, Agent OS, cc-sdd, Conductor, GSD Core, LeanSpec, wshobson/agents, claude-task-master) separate the framework from the user's content, and how does an upgrade reach an existing user project?
- **Answer in short:** four architectures; only two keep the engine out of the project — plugin-only (nothing lands in the user repo: Superpowers, Conductor, wshobson) and engine installed once globally with a thin state file in the repo (GSD, Agent OS). Copying the engine into user repos (Spec Kit, BMAD, OpenSpec, cc-sdd, task-master) has forced manifests, override layers and migration commands. One repo = one project everywhere except Spec Kit. Worth borrowing: OpenSpec marker blocks, Agent OS reverse promotion.
- **Consult when:** choosing the engine/projects shape (THR.0130), designing anything the engine writes into a user-owned file, or asking how a project's learning flows back into the engine.

### `2026-08-29-claude-code-packaging.md`
- **Question:** what does the current Claude Code documentation offer and forbid for distributing a CLAUDE.md-centric framework — plugins, skills, memory discovery, instance configuration — and what does Anthropic recommend?
- **Answer in short:** a plugin carries commands, agents, templates and scripts with versioned updates and `userConfig` for instance facts, but "a CLAUDE.md at the plugin root is not loaded" and there is no rules component; always-on conventions arrive only by a SessionStart hook, a main-thread agent replacing the system prompt, or one `@import` line per project. Discovery is asymmetric — CLAUDE.md up to the filesystem root, commands and agents only to the nearest repository root, settings not at all — so an engine clone with nested project repos works exactly when Claude Code is launched from the engine root, a documented sharing route. Commands are already skills; `CLAUDE.local.md` is the native home for instance facts.
- **Consult when:** moving instance facts out of the engine (THR.0090), packaging the forge as a plugin, migrating `.claude/commands` to `.claude/skills`, or explaining where Claude Code must be started.

### `2026-08-29-git-engine-projects-separation.md`
- **Question:** does git or its tooling have a feature for a public engine repo whose clone is the working directory with independent private project repos inside, upgradable without touching them?
- **Answer in short:** no — submodules, subtree and worktrees all model a pinned dependency, which this relation is not. The mechanism is the absence of one: `.gitignore` with `projects/*` (never `projects/`, or the `!projects/forge` re-include silently fails) and ordinary repos inside; verified by test that the engine stages nothing and its ignore rules do not reach a project. Guards: no `git add -f`, no `git clean -xd` in the engine root. Copier only if projects ever carry a skeleton; a `git -C` loop for status/pull/save.
- **Consult when:** writing the `.gitignore` and the multi-repo behaviour of `forge-status` / `forge-pull` / `forge-save`, or when someone proposes submodules or a template repo.

### `2026-08-29-split-migration-runbook.md`
- **Question:** how exactly is the engine/projects split (POS.0940) executed on this instance — order, commands, checks, rollback — so that the public engine starts clean and the company projects and the full history stay where they are?
- **Answer in short:** a rollback tag `pre-split` on the company host, then four phases: (A) move the projects out — company library first, then the two company projects, each `git init` + push to the company host, then `git rm -r --cached` in the engine; (B) rebuild the operating layer to intent 2.21 on the old history (`.gitignore` `projects/*` + `!projects/forge`, `CLAUDE.local.md`, model to `settings.local.json`, `local/` deleted, scripts looping over `projects/*/.git`, templates, commands, CLAUDE.md, readme recipe); (C) rewrite the forge project within the boundary, grep for traces with a list kept outside the repo, orphan branch as the fresh history with the private author set locally, public remote, company project archived read-only as the full record; (D) verify by a fresh clone, approve 3.0, tag. One ordering rule matters: operating layer before fresh history. A Rollback section returns to `pre-split` from every phase; remote repositories are deleted only by the principal's explicit act.
- **Consult when:** executing the migration (it is the checklist), when a step fails and the question is what to roll back, or when another instance asks how the split was done.
