---
project: forge
type: research
topic: how comparable frameworks separate engine from user content and upgrade it
date: 2026-08-29
derived_from: 10-intent.md v2.17 (POS.0760, THR.0130); 2026-08-25-comparable-projects-landscape.md
status: immutable
---

# How comparable frameworks separate the engine from user content

## Question

Eleven frameworks from the 2026-08-25 landscape were fetched live on
2026-08-29 and asked one question: how is the framework separated from
the user's content, and how does an upgrade of the framework reach an
existing user project? The forge's own destination (POS.0760) is a
public engine with private user projects; THR.0130 leaves the
mechanism open. Epistemic tags: [V] verified on the fetched page,
[S] inferred.

## Answer in one paragraph

Four architectures appear, and only two of them solve "engine public,
projects private, upgrade without touching projects": the plugin-only
shape, in which nothing at all lands in the user's repository
(Superpowers, wshobson/agents, Conductor), and the "engine installed
once globally, thin state file in the repository" shape (GSD Core,
Agent OS). The third and most common shape — the engine copied into
every user repository (Spec Kit, BMAD, OpenSpec, cc-sdd,
claude-task-master) — has forced each of those projects to build an
apparatus for surviving upgrades: ask-or-flag prompts, sparse override
layers over never-edited engine files, and finally install manifests
with a file taxonomy and migration journals. The fourth (wshobson,
task-master) is an authoring discipline: one source tree, generated
artefacts. Granularity is one repository = one project everywhere
except Spec Kit. Six of eleven ship a Claude Code plugin manifest,
three of them plugin-first.

## The four architectures

| Architecture | Who | Upgrade collision surface |
|---|---|---|
| Plugin only, nothing in the user repo | Superpowers, wshobson/agents, Conductor (scaffolds documents only) | none by construction |
| Engine installed once globally, thin state file in the repo | GSD Core (`~/.claude/gsd-core/` + `.planning/`), Agent OS (`~/agent-os` + `agent-os/standards/`) | the global install only |
| Engine copied into every user repo | Spec Kit, BMAD, OpenSpec, cc-sdd, claude-task-master | every project, every upgrade |
| Engine repo as pure source, artefacts generated | wshobson (adapters → gitignored per-harness output), task-master (plugin built from `assets/claude/`) | — (authoring discipline) |

## Surviving upgrades — three mechanisms, ascending maturity

1. **Ask-or-flag.** Agent OS prompts y/N before overwriting standards
   and offers `--commands-only`; cc-sdd offers `--dry-run --backup`.
   Cheapest, weakest [V].
2. **Sparse override layer over never-edited engine files.** BMAD:
   `_bmad/custom/{skill}.toml` (team, committed) and `.user.toml`
   (personal, gitignored) over the skill's shipped `customize.toml`;
   merge by value shape, no removal mechanism. Spec Kit:
   `templates/overrides/` → presets → extensions → core. OpenSpec:
   `openspec/config.yaml`. Because the engine files are never edited,
   they can be replaced wholesale [V].
3. **Install manifest with a file taxonomy.** Spec Kit's
   `.specify/integration.json` records what it installed and refuses
   to overwrite a modified managed file without `--force`. GSD Core
   classifies every file as managed / user-owned / unknown, prints a
   Plan before mutating disk, writes a Journal with rollback data,
   backs up local edits to `gsd-local-patches/` and re-merges them
   with `/gsd-update --reapply`. GSD names the real danger: not the
   upgrade but the *retirement* of a file — "delete a user-created
   file because it happens to live inside a GSD-managed directory" [V].

Two cautionary tales stated by maintainers themselves [V]: BMAD —
"Copying the full `customize.toml` into an override is actively
harmful: the next update ships new defaults, but your override file
locks in the old values. You'll silently drift out of sync with every
release." BMAD's disruptive v4→v6 migration happened because v4
"modified files directly". OpenSpec killed its passive `project.md`
because "agents might read it, might not, might forget what they
read" and replaced it with context "actively injected into every
planning request".

## Per framework

- **GitHub Spec Kit** (v1.0.1, 2026-08-21) [V] — Python CLI installed
  outside the repo (`uv tool install specify-cli`). Lands in the repo:
  `.specify/{memory/constitution.md,templates/,scripts/,integration.json}`,
  `.claude/skills/`, `specs/`. Explicitly two-part upgrade
  (`docs/upgrade.md`: "The CLI tool is separate from your project
  files"): `specify self upgrade [--tag vX.Y.Z]` for the tool,
  `specify integration upgrade <key>` for project files, manifest-aware;
  `specs/` and the constitution are never touched. The only framework
  supporting **many projects per repository**: the project is
  "whichever directory contains `.specify/`", nearest-ancestor
  resolution, `SPECIFY_INIT_DIR` errors rather than falls back. No
  Claude Code plugin.
- **BMAD-METHOD** (v6.11.0, 2026-08-10) [V] — `npx bmad-method install`
  *and* a plugin marketplace (`.claude-plugin/marketplace.json`). Lands:
  `_bmad/{core,bmm,bmb,cis,_config,custom}`, `_bmad-output/`,
  `.claude/skills/`. Re-run the installer to upgrade; customisation
  only through the override stack above.
- **OpenSpec** (v1.11.0, 2026-08-26) [V] — global npm CLI; an
  `install.md` written as a prompt for the agent. Lands:
  `openspec/{specs,changes,config.yaml}` plus per-tool command files.
  Injects into the user's `CLAUDE.md`/`AGENTS.md` behind **marker
  blocks** so that only its own text is ever retracted; deletes its own
  legacy files automatically. "Stores (beta)": specs in a separate
  shared repository across several code repositories.
- **Superpowers** (v6.3.0, 2026-08-12) [V] — pure Claude Code plugin
  (official marketplace and its own), manifests for thirteen harnesses
  side by side; **nothing lands in the user repo**; dated
  `RELEASE-NOTES.md`, `bump-version.sh` across all manifests. Cleanest
  separation of the eleven.
- **Agent OS** (v3.0.0, 2026-01-20) [V] — base install (the repo
  cloned to `~/agent-os`) + `scripts/project-install.sh` run inside the
  project; lands `agent-os/standards/` and `.claude/commands/agent-os/`.
  Upgrade re-runs the script, `--commands-only` spares standards;
  customised commands are merged by hand. A reverse channel
  `sync-to-profile.sh` pushes a project's evolved standards *back up*
  into a base profile. No plugin.
- **cc-sdd** (v3.0.2, 2026-04-13) [V] — `npx cc-sdd@latest` in the
  repo; lands `.claude/skills/` and `.kiro/{settings,specs,steering}`;
  customise by editing installed files, upgrade by re-running — the
  collision the forge is trying to avoid; `--dry-run --backup` the only
  guard.
- **Conductor** (v0.4.1, 2026-03-11) [V] — Claude Code plugin (+
  Antigravity); plugin holds `skills/` and `rules/`, the repo holds only
  documents scaffolded by `/conductor:conductor-setup`
  (`conductor/product.md`, `tracks/<id>/{spec,plan}.md`). Structurally
  the closest to the forge's target. No upgrade documented.
- **GSD Core** (v1.11.0, 2026-08-19) [V] — installer mandatory ("do
  not copy files directly"), `--global` or `--local`; global install
  under `~/.claude/{gsd-core/,commands/gsd/,agents/gsd-*.md,hooks/}`,
  repo holds `.planning/config.json`. The most engineered migration
  layer (`docs/installer-migrations.md`).
- **LeanSpec** (v0.2.28, 2026-03-23) [V] — npm CLI, also installable
  as a skill; lands `.lean-spec/`, `specs/`, `AGENTS.md`, `CLAUDE.md`;
  `skills-lock.json` pins skills; differentiator is not owning storage
  (adapters for Markdown / GitHub Issues / ADO).
- **wshobson/agents** [V] — plugin marketplace of 93 plugins; nothing
  lands in the user repo. Invariants: single authored source tree,
  generated gitignored per-harness artefacts ("never hand-edit
  generated files"), `CLAUDE.md` a symlink to `AGENTS.md`, drift
  detection in CI (`make garden`). No versioning, no releases.
- **claude-task-master** (0.43.1, 2026-03-31) [V] — npm, npx, MCP
  server and a plugin built from `assets/claude/`; lands `.taskmaster/`
  and `.claude/commands/`; a shipped `task-master migrate` for its own
  `tasks/` → `.taskmaster/` relocation.

## Comparison

| Framework | Mechanism | In the user repo | Upgrade | Granularity |
|---|---|---|---|---|
| Spec Kit | CLI outside the repo | `.specify/`, skills, `specs/` | two-part, manifest-aware | many per repo (nearest `.specify/`) |
| BMAD | installer + plugin | `_bmad/`, `_bmad-output/`, skills | re-run installer; override stack | one per repo |
| OpenSpec | global CLI | `openspec/`, per-tool commands | `openspec update`; marker blocks | one per repo; shared Stores |
| Superpowers | plugin | nothing | plugin update | global |
| Agent OS | base install + script | `agent-os/standards/`, commands | re-run script; `--commands-only` | one per repo, many profiles |
| cc-sdd | npx in repo | skills, `.kiro/` | re-run; `--dry-run --backup` | one repo, many specs |
| Conductor | plugin | documents only | not documented | one per repo, many tracks |
| GSD Core | installer, global | `.planning/` | manifest + Plan + Journal | one per repo |
| LeanSpec | npm CLI / skill | `.lean-spec/`, `specs/` | `npm update` | one `specs/` tree |
| wshobson/agents | plugin marketplace | nothing | `/plugin update` | not project-scoped |
| task-master | npm / MCP / plugin | `.taskmaster/`, commands | `npm update`; `migrate` | one per repo, tags |

## Relevance to this project

- The forge's chosen granularity (one repository per project) is the
  field's norm; Spec Kit's nearest-`.specify/` rule is the design to
  copy only if several projects ever share one repository.
- The two clean shapes both keep the engine *outside* the project:
  either installed once (Agent OS base install, GSD global install —
  the forge's "engine clone as working directory" is the same idea) or
  as a plugin. Copying engine files into projects is the shape to
  avoid; it is what generates manifests, overrides and migrations.
- Two techniques worth borrowing regardless of mechanism: OpenSpec's
  marker blocks for anything the engine ever writes into a user-owned
  file, and Agent OS's reverse promotion — a scripted path from a
  project back into the engine, which the forge does conceptually
  (`projects/forge`) but not across repository boundaries.
- Conductor is the closest structural precedent for a plugin-shaped
  forge: engine in the plugin, only documents in the repository,
  scaffolded by a setup command.

## Sources

Fetched 2026-08-29: github.com/github/spec-kit (README,
docs/upgrade.md, docs/guides/monorepo.md,
docs/guides/evolving-specs.md); github.com/bmad-code-org/BMAD-METHOD
(docs/start/install-bmad.md, docs/how-to/upgrade-to-v6.md,
docs/how-to/customize-bmad.md, .claude-plugin/marketplace.json);
github.com/Fission-AI/OpenSpec (install.md, docs/customization.md,
docs/migration-guide.md); github.com/obra/superpowers
(.claude-plugin/plugin.json, RELEASE-NOTES.md);
github.com/buildermethods/agent-os (scripts/project-install.sh,
scripts/sync-to-profile.sh), buildermethods.com/agent-os/updating;
github.com/gotalab/cc-sdd (tools/cc-sdd/README.md,
docs/guides/migration-guide.md);
github.com/gemini-cli-extensions/conductor;
github.com/open-gsd/gsd-core (docs/manual-update.md,
docs/installer-migrations.md, docs/CONFIGURATION.md);
github.com/codervisor/leanspec (.lean-spec/config.json,
CHANGELOG.md); github.com/wshobson/agents (ARCHITECTURE.md);
github.com/eyaltoledano/claude-task-master (CLAUDE_CODE_PLUGIN.md).
