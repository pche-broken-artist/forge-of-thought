---
project: forge
type: research
topic: what Claude Code offers for packaging a CLAUDE.md-centric framework — plugins, skills, memory discovery
date: 2026-08-29
derived_from: 10-intent.md v2.17 (POS.0760, THR.0090, THR.0130)
status: immutable
---

# Packaging a CLAUDE.md-centric framework for Claude Code

## Question

What does the current official Claude Code documentation offer, and
forbid, for distributing the forge — a `CLAUDE.md` of always-on
conventions, ~15 commands, two subagents, templates and scripts — to
other users who keep their projects in repositories of their own? In
particular: can a plugin carry the always-on core; how are `CLAUDE.md`,
commands, agents and settings discovered across directories; what do
Anthropic's own recommendations say about frameworks. Docs fetched
live on 2026-08-29 from `code.claude.com/docs` (the canonical home;
the old `docs.claude.com` URLs redirect), referencing Claude Code up
to v2.1.246. Epistemic tags: [V] verified on the page, [S] inferred.

## Answer in one paragraph

A plugin can carry every executable part of the forge unchanged —
commands (now skills), agents, templates, scripts — with real
versioning and a background update channel, and can house instance
facts through `userConfig`. It cannot carry the one thing the forge is
built around: the docs say in a single sentence that "a `CLAUDE.md`
file at the plugin root is not loaded as project context", and there
is no `rules/` component either. Always-on conventions from a plugin
arrive only by a `SessionStart` hook, by a main-thread agent that
replaces Claude Code's system prompt, or by one `@import` line written
into each project's `CLAUDE.md`. Discovery is asymmetric: `CLAUDE.md`
is found in every ancestor directory to the filesystem root, commands
and agents only up to the nearest repository root, settings only in
the working directory — so a framework clone serving nested project
repositories works exactly when Claude Code is launched from the
framework root, which the docs name as one of three supported sharing
routes. Anthropic's stated rule of thumb: "a second repository needs
the same setup → package it as a plugin"; no official document
addresses distributing a `CLAUDE.md`-centric methodology.

## Discovery — three systems, three walk-ups [V]

| Configuration | Where it is found |
|---|---|
| `CLAUDE.md`, `CLAUDE.local.md` | the working directory and **every directory above it to the filesystem root**, concatenated root-down; subdirectory files load on demand |
| `.claude/skills/`, `.claude/commands/`, `.claude/agents/` | walk up from the working directory **only to the nearest repository root** |
| `.claude/settings.json` | the working directory's `.claude/` only, **no parent-directory fallback** |

The session's project root is the directory Claude Code was launched
in, not the enclosing git repository. `claudeMdExcludes` exists
precisely because ancestor `CLAUDE.md` files can be unwanted in
monorepos — evidence that the ancestor walk is real and unbounded.

Consequence for a framework clone with nested project repositories:
launched from the framework root, everything loads; launched inside a
project (its own repository), the framework `CLAUDE.md` loads but
**none** of its commands, agents or settings. Fallback: `claude
--add-dir <framework>` loads `.claude/skills/` and `.claude/commands/`
from the added directory automatically (agents are not loaded; no
live reload), and `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`
additionally loads its `CLAUDE.md` and rules. The docs name three
sharing routes: "launch from the config directory", user-level
`~/.claude/`, or a plugin.

## Memory files [V]

- Hierarchy: managed policy → `~/.claude/CLAUDE.md` → `./CLAUDE.md` or
  `./.claude/CLAUDE.md` → `./CLAUDE.local.md` (gitignored, current and
  not deprecated). Target under 200 lines; "bloated CLAUDE.md files
  cause Claude to ignore your actual instructions". A project-root
  `CLAUDE.md` is re-read from disk after `/compact`.
- `@path` imports: relative or absolute (`@~/.claude/x.md`), four hops
  deep, skipped inside code fences. An import resolving outside the
  working directory shows a one-time approval dialog per project;
  declining disables it permanently. User-scope imports need no
  dialog.
- `.claude/rules/*.md` (project) and `~/.claude/rules/*.md` (user) load
  at launch with `CLAUDE.md` priority; optional `paths:` frontmatter
  scopes a rule to files. Symlinks are supported explicitly:
  "maintain a shared set of rules and link them into multiple
  projects". On Windows, symlinks need Administrator or Developer Mode;
  the docs recommend `@` imports instead.
- CLAUDE.md is "delivered as a user message after the system prompt";
  it is context, not enforced configuration — a `PreToolUse` hook is
  the enforcement mechanism.

## Skills [V]

"Custom commands have been merged into skills": `.claude/commands/x.md`
and `.claude/skills/x/SKILL.md` both create `/x` and behave the same;
the old form keeps working. A skill directory adds supporting files
(loaded only when read), `scripts/` (executed, not loaded),
`${CLAUDE_SKILL_DIR}`, and frontmatter: `context: fork` + `agent:`
(runs the skill in an isolated subagent), `shell: powershell`,
`disable-model-invocation`, `allowed-tools`, `model`, `paths`,
`` !`command` `` for dynamic context. Precedence: enterprise > personal
> project; a skill beats a same-named `.claude/commands/` file. Only
the skill's description (≤ 1,536 characters with `when_to_use`) is in
context at session start; the body loads on invocation and then stays
for the session.

Stated guidance: "Put it in CLAUDE.md if Claude should always know
it … Put it in a skill if it's reference material Claude needs
sometimes." Build-over-time triggers: a convention Claude gets wrong
twice → CLAUDE.md; a repeated prompt → a skill; something that must
happen every time → a hook; **"a second repository needs the same
setup → package it as a plugin"**.

## Plugins [V]

- Layout: `.claude-plugin/plugin.json` (only `name` required; `version`
  pins updates) plus, at the plugin root, `skills/`, `commands/`,
  `agents/`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`,
  `monitors/`, `bin/` (added to PATH), `scripts/`, `settings.json`,
  `CHANGELOG.md`, `LICENSE`. Arbitrary bundled files are allowed.
- Path variables: `${CLAUDE_PLUGIN_ROOT}` (changes on update — never
  hard-code), `${CLAUDE_PLUGIN_DATA}` (persists across updates),
  `${CLAUDE_PROJECT_DIR}` (the user's project root), substituted in
  skill and agent content, hook and MCP commands, and `allowed-tools`
  rules — a bundled script can be pre-approved.
- `userConfig`: values prompted at enable time (string, number,
  boolean, directory, file; `sensitive` → keychain), substituted as
  `${user_config.KEY}` into skill and agent content — a home for
  instance facts such as principal identity and conversation language.
- Namespacing: plugin skills are `/plugin-name:skill-name` (the bare
  form also works unless taken); plugin agents `plugin-name:agent`.
  Plugin agents have the **lowest** precedence (managed > CLI >
  project > user > plugin): a user's own `~/.claude/agents/critic.md`
  silently shadows the plugin's. Plugin-shipped agents cannot carry
  `hooks`, `mcpServers` or `permissionMode`.
- Marketplace: any git repository (GitHub `owner/repo`, any git URL
  including GitLab and self-managed GitLab, a local path, or a hosted
  `marketplace.json`) with `.claude-plugin/marketplace.json`; sources
  can pin `ref` or `sha`; `renames` is the only migration primitive.
  Install `/plugin marketplace add …` then `/plugin install
  name@marketplace`, scope user / project / local / managed. Users pin
  a marketplace ref (`#v1.0.0`), not a plugin version. Updates reach
  users only when the `version` string is bumped; **third-party and
  local marketplaces have auto-update disabled by default**. A project
  `.claude/settings.json` can declare `extraKnownMarketplaces` and
  `enabledPlugins`, but an externally sourced plugin still needs each
  user to install it.
- Development: `claude --plugin-dir ./x` (takes precedence over an
  installed plugin of the same name), `/reload-plugins`, `claude plugin
  validate`. A folder under `~/.claude/skills/` (or project
  `.claude/skills/`) containing `.claude-plugin/plugin.json` auto-loads
  as a plugin with no marketplace and no install step.
- Official channels: `claude-plugins-official` (curated at Anthropic's
  discretion, no application), `anthropics/claude-plugins-community`
  (submission form, automated validation and safety screening, catalog
  pinned to a commit SHA), `anthropics/skills` (examples, the Agent
  Skills spec, a template).

## The decisive sentence, and the substitutes [V]

From the plugins reference, verbatim: **"A `CLAUDE.md` file at the
plugin root is not loaded as project context. Plugins contribute
context through skills, agents, and hooks rather than CLAUDE.md. To
ship instructions that load into Claude's context, put them in a
skill."** There is no `rules/` component in the manifest or the
directory table. Substitutes, in descending strength:

1. **Plugin `settings.json` `{"agent": "<name>"}`** — a plugin agent
   becomes the main thread; "the subagent's system prompt replaces the
   default Claude Code system prompt entirely" (CLAUDE.md files still
   load). Highest instruction-following weight; the session stops being
   a general coding session; users cannot easily layer their own main
   agent.
2. **A `SessionStart` hook** whose stdout, or
   `hookSpecificOutput.additionalContext`, "Claude Code adds as context
   that Claude can see and act on". Every constituent fact is
   documented; the idiom "plugin equivalent of CLAUDE.md" is not.
   Invisible to `/memory`; does not survive `/compact` the way a
   project-root `CLAUDE.md` does [S].
3. **A skill** — only its description is always present. The wrong
   shape for prime directives that must govern every turn.
4. **One line per project** — a project `CLAUDE.md` containing
   `@~/.claude/forge-core.md` (one-time approval dialog) or a symlink
   into `.claude/rules/`, written by a `/new-project`-equivalent skill.
   The core is then a real memory file with proper precedence and
   compaction survival, and the plugin update refreshes the single
   canonical copy.

No official document addresses distributing a `CLAUDE.md`-centric
methodology [V, by absence across plugins, plugins-reference,
marketplaces, features-overview, best-practices, the plugins and
steering blog posts, and anthropics/skills]. The plugins announcement
(2025-10-09) names "framework authors package related extensions for
specific use cases" as a use case; the steering post (2026-06-18) says
customisations "can be bundled as a plugin to share a coherent setup
across teammates or projects".

## Relevance to this project

- **Engine clone as working directory is a supported route** ("launch
  from the config directory"), and the only launch point where
  `CLAUDE.md`, commands, agents and settings all resolve. The README
  must say so; `--add-dir` is the documented fallback.
- **Instance facts** have a native home today — `CLAUDE.local.md` —
  and a native home in a plugin — `userConfig`.
- **Commands are already skills.** Migrating `.claude/commands/*.md` to
  `.claude/skills/<name>/SKILL.md` changes no behaviour and gains a
  directory per command and `context: fork` for the isolated `/render`
  and both reviewers. It is also exactly what `plugin.json` would
  package unchanged.
- **A plugin is a distribution layer, not a home for the core.** If
  the forge is ever a plugin, the core must arrive by route 4 (the
  recommendation — it preserves the core as a memory file), route 2,
  or route 1; and the forge's multi-project operations (bare `/check`,
  `/spinoff`, a README from several projects) need a workspace notion
  that a plugin does not provide.
- **Plugin caveats to plan for:** namespaced commands (`/forge:save`),
  user agents shadowing plugin agents, auto-update off by default for
  third-party marketplaces, no version pin on the user side.

## Sources

Fetched 2026-08-29: code.claude.com/docs/en/plugins,
/plugins-reference, /plugin-marketplaces, /discover-plugins, /memory,
/skills, /sub-agents, /hooks, /settings, /settings-reference,
/features-overview, /best-practices;
claude.com/blog/claude-code-plugins (2025-10-09);
claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
(2026-06-18); github.com/anthropics/skills;
github.com/anthropics/claude-plugins-community.
