---
project: forge
type: research
topic: how Claude Code and comparable frameworks let a user add things of his own (agents, skills, commands, checks, artefact definitions, templates) kept apart from a centrally maintained core, and how those additions survive an upgrade of the core
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (User modifications); 10-intent.md v4.50; 10-intent.threads.md (THR.0300, THR.0480, THR.0190, THR.0230); research/2026-08-29-claude-code-packaging.md; research/2026-08-29-framework-distribution-in-the-field.md; research/2026-09-30-adding-a-new-type-to-the-engine.md
status: immutable
---

# User extensions kept apart from the core

## Question

How do Claude Code itself and comparable frameworks let a user add
things of his own (agents, skills, commands, checks, artefact
definitions, templates) kept apart from the centrally maintained
core, and how do those additions survive an upgrade of the core?
For each: where the user's thing lives, how the core finds it, what
happens on a name collision, what the core promises to keep stable,
how breakage on upgrade is detected. Then options for the forge and
a recommendation. Findings and options, not a design.

## Method and epistemic status

All pages were fetched on 2026-10-03. The fetch tool passes a page
through a small model; for some pages it returned the page text
itself, for others a summary. The tags say which:

- **[V]** verified on the page text as returned whole by the fetch
  (Claude Code: plugin manifest reference, create a marketplace,
  plugin loading reference, plugin dependencies, host a marketplace,
  create a plugin, plugins for your organization; and, read by
  search in the returned text, plugin components, settings, memory,
  permissions).
- **[Vs]** taken from the fetch tool's summary of the page, quotes
  as the summary gave them (Claude Code: skills, subagents,
  changelog; every framework page). A summary can drop or bend a
  detail; anything load-bearing below that rests on [Vs] is named
  under "What stays uncertain".
- **[2]** secondary source (a search result's digest, a third-party
  page).
- **[S]** Claude's own synthesis.

The Claude Code documentation was reorganised since the note of
2026-08-29: the plugin pages now live under
`code.claude.com/docs/en/plugins/*`, and the old `plugins-reference`
and `plugin-marketplaces` addresses redirect to the manifest
reference and to "Create a marketplace". The newest version in the
changelog is 2.1.288, dated 2026-10-02 [Vs]; the earlier note
referenced 2.1.246.

## Key findings

### 1. Claude Code today: the levels and what each carries

| Level | Skills and commands | Agents | Memory and rules | Settings |
|---|---|---|---|---|
| Managed (organisation) | yes, highest | yes, highest | managed CLAUDE.md, loads first | highest, cannot be overridden |
| User (`~/.claude/`) | `skills/`, `commands/` | `agents/` | `CLAUDE.md`, `rules/` | `settings.json`, lowest |
| Project (`.claude/`) | walk up from the working directory to the repository root | the same walk | `CLAUDE.md` and `CLAUDE.local.md` from the working directory and every directory above it; `.claude/rules/` | `settings.json` |
| Local | none of its own | none of its own | `CLAUDE.local.md` | `settings.local.json` |
| Nested, below the working directory | `<subdir>/.claude/skills/` load on first file access there | not stated | subdirectory `CLAUDE.md` and rules on file access | none |
| Added directory (`--add-dir`, `/add-dir`) | yes | yes | only with an environment variable | two plugin keys only |
| Plugin | `skills/`, `commands/`, namespaced | `agents/`, namespaced | none | `agent` and `subagentStatusLine` only |

Sources: skills page [Vs], subagents page [Vs], memory page [V],
settings page [V], permissions page [V], manifest reference [V].

**Collision rules differ by component, and in opposite directions.**

- Skills: "Enterprise over personal, and personal over project.
  With `deploy` in both `~/.claude/skills/` and the project's
  `.claude/skills/`, `/deploy` runs the personal one." [Vs] A user's
  personal skill therefore replaces a project command of the same
  name.
- Agents: managed, then the `--agents` flag, then project
  `.claude/agents/`, then user `~/.claude/agents/`, then plugin
  agents; the higher location wins. [Vs] Here the project wins over
  the user. Inside one `.claude/agents/` tree (subfolders are
  scanned recursively and identity comes from the `name` field
  alone) two files with the same name are resolved "by filesystem
  read order rather than documented precedence". [Vs]
- Commands from an added directory: "When the added directory and
  your project both define a command with the same name, Claude
  Code runs your project's command." [V] The page states no rule
  for skills or agents colliding across the project and an added
  directory.
- Nested skills: when a nested skill has the name of a root skill
  both stay, the nested one under a path-qualified name; the page's
  example is `/deploy` for the root and `/apps/web:deploy` for the
  nested one. [Vs]
- Plugins: every component is namespaced under the plugin's name,
  `plugin:skill` and `plugin:agent` (with subfolders,
  `plugin:folder:agent`); the bare skill name also works "unless
  another command uses that name". [V, Vs] The docs on converting a
  `.claude/` setup say of a plugin's and the project's copies: "the
  two sets don't collide, because the plugin's skills and agents
  carry the `my-plugin:` prefix ... Claude sees `reviewer` and
  `my-plugin:reviewer` as two subagents." [V] Hooks have no prefix
  and run twice when present in both. [V]
- Agent names "can't contain `:`", which is reserved for
  plugin-scoped identifiers; such a file is skipped since v2.1.218.
  [Vs]

**One level using another level's things.** An agent's `skills:`
field preloads the full skill content at start. Project and user
skills are named by their bare name, plugin skills by the scoped
identifier, for example `my-plugin:security-patterns`. "If a listed
skill is missing or disabled ... Claude Code skips it and logs a
warning to the debug log." [Vs] So a renamed or removed contract
skill does not stop an agent that preloads it: the agent runs
without the contract, and nothing is shown in the session. Whether a
plugin's agent can preload a project skill by its bare name is
implied by the naming rule and not stated in so many words.

**Added directories.** `--add-dir` and `/add-dir` load the added
directory's `.claude/skills/` (with live reload), `.claude/commands/`
and `.claude/agents/` (both without live reload); from its settings
files only `enabledPlugins` and `extraKnownMarketplaces`; its
`CLAUDE.md`, rules and `CLAUDE.local.md` only with
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`. Directories listed
in `permissions.additionalDirectories` of a settings file "grant
file access only and don't load any of the configuration". Running
`/add-dir` on a subdirectory of the working directory loads that
subdirectory's skills, commands and subagents for the rest of the
session without a prompt (v2.1.257 or later). [V]

**Plugins without a marketplace.** Three doors [V]:

- `--plugin-dir <path>` for one session; since v2.1.265 the path may
  be a folder of plugins, each subfolder with a
  `.claude-plugin/plugin.json` loading as its own plugin; since
  v2.1.280 the environment variable `CLAUDE_CODE_PLUGIN_DIRS` does
  the same without a flag (project and local settings cannot set
  it).
- A skills-directory plugin: any folder under `~/.claude/skills/`
  or the project's `.claude/skills/` that carries a
  `.claude-plugin/plugin.json` loads as a plugin in every session,
  id `<name>@skills-dir`, in place, never copied, no install step.
  The project-scope form loads only from the `.claude/skills/` of
  the session's primary working directory (no walk up), only after
  the workspace trust dialog, and its background monitors do not
  load. `claude plugin init <name>` scaffolds the personal form.
- A marketplace added from a local directory: plugins with a
  relative-path source load in place from that directory, edits
  take effect at the next session start or `/reload-plugins`, no
  version bump.

When plugins of one manifest name load from several origins, the
order is: managed, then `--plugin-dir` and its kin, then an
installed marketplace plugin, then a skills-directory plugin (the
personal copy over the project's), then a plugin synced from the
account; the loser is reported in the `/plugin` Errors tab. [V]

**Marketplaces, versions, updates.** A marketplace is a git
repository (any host, private included), a hosted
`marketplace.json`, or a directory on a shared filesystem; access to
a private one rides on the git credentials already on the machine,
and the catalogue has no field for a token. [V] A plugin's version
is the manifest's `version`, else the marketplace entry's, else the
commit SHA; a set `version` holds every user on the cached copy
until the string changes. Auto-update is on only for the official
marketplace and off "for every other marketplace" until a user or
an administrator turns it on. [V] A rename is migrated by an
append-only `renames` map in the catalogue; "there is no
deprecation state". [V]

**Plugin dependencies.** `dependencies` in `plugin.json` names
plugins that must be enabled, optionally with a semantic-version
range that resolves against git tags `<plugin>--v<version>`;
conflicting ranges fail the install with a message, an unsatisfied
range leaves the dependent plugin disabled with a line in
`claude plugin list`; a dependency in another marketplace needs an
allowlist entry in the root marketplace. [V] This is the one place
in Claude Code where a break between two separately maintained
parts is detected and shown rather than passed over.

**User configuration of a plugin.** `userConfig` prompts for typed
values at enable time, stores them under `pluginConfigs` in the
user's settings, substitutes them as `${user_config.KEY}` into skill
and agent content; a fixed list of `options` since v2.1.271. [V]

**What a plugin still cannot carry.** "A `CLAUDE.md` at the plugin
root isn't loaded as context, and `claude plugin validate` warns
when it finds one." A plugin's `settings` take effect for `agent`
and `subagentStatusLine` only. Plugin agents ignore `hooks`,
`mcpServers`, `permissionMode` and `initialPrompt`. [V]

**Organisation controls** exist for all of this
(`strictKnownMarketplaces`, `blockedMarketplaces`, managed
`enabledPlugins`, `disableSideloadFlags`, and
`strictPluginOnlyCustomization`, which "blocks skills, agents,
hooks, and MCP servers that don't come from a plugin, managed
settings, or Claude Code's built-ins"). [V] On a machine under such
a policy, anything a user keeps outside a plugin does not load.

### 2. What changed against the notes of 2026-08-29

Against `2026-08-29-claude-code-packaging.md`; what is not listed
here was re-read and still holds, and is cited from that note.

- **Changed:** the note says of `--add-dir` that "agents are not
  loaded". Today subagents in the added directory's
  `.claude/agents/` are loaded, without live reload. [V]
- **Sharper:** the note says a user's `~/.claude/agents/critic.md`
  "silently shadows the plugin's". The priority table still puts
  plugin agents last [Vs], but the docs now say a plugin's agent is
  identified by its scoped name and stands beside a same-named
  project agent as a second subagent [V]. Shadowing applies to the
  unqualified name; an agent called by `plugin:name` is not
  shadowed. [S]
- **New since late August** (version numbers as the pages give
  them): on-demand loading of nested `.claude/skills/` with
  path-qualified names, and `/add-dir` on a subdirectory (2.1.257);
  a folder of plugins through `--plugin-dir` (2.1.265) and
  `CLAUDE_CODE_PLUGIN_DIRS` (2.1.280); `userConfig` options
  (2.1.271) and plugin options in `/config` (2.1.269); the agent
  field `omitClaudeMd`, which starts a subagent without the user,
  project and local `CLAUDE.md` files (2.1.271); plugins synced
  from the account (2.1.273); `AGENTS.md` read directly (2.1.277);
  MCP checks in `claude plugin validate` (2.1.281); "mods", plugins
  that change deeper behaviour (2.1.287). [V, Vs]
- **Not in the earlier note, age not established:** plugin
  dependencies with version ranges, the name-conflict order between
  plugin origins, `strictPluginOnlyCustomization`, workflows and
  output styles as plugin components.
- **Still holds, cited not repeated:** a plugin carries no
  always-on `CLAUDE.md`; skills precedence enterprise, personal,
  project; the asymmetry of discovery (memory to the filesystem
  root, skills and agents to the repository root); third-party
  marketplaces do not auto-update by default; `renames` is the only
  migration primitive; `${CLAUDE_PLUGIN_ROOT}` changes on update and
  `${CLAUDE_PLUGIN_DATA}` persists. That settings have no
  parent-directory fallback was not re-read today.

Against `2026-08-29-framework-distribution-in-the-field.md`: its
four architectures and three upgrade mechanisms still describe the
field. That note asked how the engine is kept apart from user
*content*; this one asks how user *extensions* are kept apart from
the engine, and adds per framework what follows. Framework version
numbers were not re-checked.

### 3. Comparable frameworks

**BMAD Method** (docs.bmad-method.org, no date on the pages) [Vs].
Three layers per skill: "Priority 1 (wins):
`_bmad/custom/<skill>.user.toml` (personal, gitignored); Priority 2:
`_bmad/custom/<skill>.toml` (team, committed); Priority 3 (base):
the skill's own `customize.toml`". A central configuration has four
layers, two installer-owned files "regenerated on every install"
and two human-authored ones in `_bmad/custom/` that "are never
touched by the installer". Merging goes by the shape of the value:
scalars override, tables merge deeply, arrays of tables merge by
`code` or `id`, other arrays append. "No removal. An override cannot
delete a base item." A resolver script performs the merge and
prints JSON. The warning in the maintainers' words: "A full copy
locks in today's defaults, so the next update ships new values that
your override silently shadows." A user's own agents are an entry in
the custom configuration; a user's own module is a separate
repository or local path installed into `_bmad/<module>/`, its
source recorded in `_bmad/_config/manifest.yaml` "so that updates
can locate the source again"; a quick update re-reads each module
from its source and skips one whose source is gone. What happens
when two modules bring the same skill name is not documented.

**GitHub Spec Kit** (repository README files and guides) [Vs]. Two
extension kinds. *Presets* override templates and commands: they
install to `.specify/presets/<id>/`, and a template is resolved at
every lookup through a stack, highest first: project overrides
(`.specify/templates/overrides/`), installed presets ordered by a
numeric priority ("lower number = higher precedence"), extension
templates, core. A preset may `replace`, `prepend`, `append` or
`wrap` what lies below it; `specify preset resolve <name>` says
which layer supplied a template. *Extensions* add new commands:
`.specify/extensions/<id>/` with a manifest `extension.yml` carrying
`schema_version`, an id, a version and `requires.speckit_version`
(a range such as ">=0.1.0,<2.0.0"), a registry file
`.specify/extensions/.registry`, a four-level configuration
(extension defaults, project file, gitignored local file,
environment variables), and an enforced namespace: a command "must
match `speckit.{ext-id}.{command}`". Updates are offered by version
only: "a content change shipped without a version bump is never
delivered automatically." Catalogues stack at project and user
level, and an organisation can point at its own.
What went wrong, from the issue tracker: commands, unlike templates,
"are applied at install time", and issue 3849 (opened 2026-07-29 on
version 0.14.2, closed with a linked fix) reports that
`specify integration upgrade --force` "regenerates ... SKILL.md from
the core command templates and removes the command content supplied
by installed extensions or presets"; the stated cause is that the
upgrade path "does not reconcile the active extension and preset
command layers". A layer composed at install time is lost by any
later step that regenerates the same files.

**OpenSpec** (openspec.dev, repository docs) [Vs]. A custom schema
is a directory `openspec/schemas/<name>/` with `schema.yaml` and its
templates, the pair of "what is produced" and "how", made by
`openspec schema init` or `fork`, checked by
`openspec schema validate`. A schema is looked up in the project,
then the user's data directory, then the package; "the same name
can exist in more than one place, and the more specific location
wins", and `openspec schema which <name>` prints the source and
what it shadows. On forks: "Your fork keeps working exactly as you
left it, which also means it stops receiving improvements when the
built-in schema evolves." No statement on what a CLI upgrade may
break in a custom schema was found.

**Agent OS** (buildermethods.com, v3.0.0) [Vs]. A profile is a
folder of standards in the base installation,
`~/agent-os/profiles/<name>/`; `inherits_from` in the base
`config.yml` chains profiles, "base first, later wins", the child's
file replacing the parent's of the same path, and the install output
names the origin of each file. An update of the base replaces
`commands/` and `scripts/` and keeps `profiles/`, by a backup and
restore the user performs; "if you've customized any commands or
scripts, back those up separately and merge your changes after
updating."

**Superpowers** (repository README and its bootstrap skill) [Vs].
No extension mechanism of its own: it is a plugin, its skills are
namespaced `superpowers:<skill>`, and a user's own skills live at
whatever level the host offers. The project "don't generally accept
contributions of new skills". Its stated order is "user instructions
(CLAUDE.md, AGENTS.md ...) take precedence over skills, which in
turn override default behavior". How a personal skill of the same
name as a Superpowers skill is treated was not found at source.

**Outside the field, for the contract question.** VS Code separates
a stable extension API ("We take Extension API compatibility
seriously") from proposed APIs that are "subject to change" and
barred from published extensions, and an extension declares the
host version it needs (`engines.vscode`). [Vs, page dated
2026-09-30] The layout "vendor files in one tree, administrator
files in another, drop-in fragments rather than copies" of systemd
is the classic form of the override layer; its manual could not be
fetched today (the server refused), so this is from general
knowledge, unverified here. [S]

### 4. Patterns, and how settled each is

- **Consensus.** The user's things live where an upgrade never
  writes: a separate directory, a separate layer file, a separate
  repository (BMAD `_bmad/custom/`, Spec Kit overrides and
  extensions, OpenSpec project schemas, Agent OS profiles, Claude
  Code's user level and plugins). An override is sparse: it states
  only what differs, because a full copy freezes the defaults (BMAD
  and OpenSpec both say so in their own words). A tool answers
  "which one is in force and what does it hide" (`openspec schema
  which`, `specify preset resolve`, Claude Code's `/plugin` Errors
  tab and `claude plugin list`). [S over the sources above]
- **Emerging.** A manifest per extension that names the core
  version it needs (Spec Kit `requires.speckit_version`, Claude
  Code plugin dependencies with ranges); a registry of what is
  installed and where it came from (Spec Kit `.registry`, BMAD
  manifest, Claude Code `installed_plugins.json`); a validator the
  author runs (`claude plugin validate`, `openspec schema
  validate`); an enforced namespace for additions (Spec Kit
  `speckit.{ext-id}.{command}`, Claude Code `plugin:name`). [S]
- **Contested.** Whether a user's thing may take the name of a core
  thing. OpenSpec, BMAD, Agent OS and Claude Code's personal skills
  allow shadowing and treat it as the way to customise; Spec Kit's
  extensions and Claude Code's plugins forbid it by namespace and
  offer adding only. Shadowing gives the user power over the core
  and makes every core upgrade a silent fork; a namespace keeps the
  core intact and leaves no way to change a core behaviour. Also
  contested: composing layers at lookup or at install (Spec Kit
  does both, and the install-time half produced issue 3849), and
  whether updates arrive on their own. [S]
- **Rare.** A stated promise of what stays stable and how a change
  is announced. None of the prompt frameworks surveyed publishes a
  deprecation policy for its extension surface on the pages
  fetched; Claude Code says of plugin catalogues that "there is no
  deprecation state"; the VS Code pair of stable and proposed API
  is the model. [S]
- **How breakage is detected**, in ascending strength: not at all
  (Agent OS merges by hand; a Claude Code agent whose preloaded
  skill is gone runs without it and logs to the debug log only); by
  a refusal to overwrite (Spec Kit's install manifest); by a
  version range checked at load, with the dependent thing disabled
  and named (Spec Kit extensions, Claude Code plugin dependencies).
  [S]

## Options for the forge, with trade-offs

Two facts of the forge frame every option [S, from the note of
2026-09-30 and the engine's files]. First, a reviewer or a check is
a Claude Code agent and must sit where Claude Code registers
agents; an artefact definition, a render genre and a template are
files the forge's own dispatchers read by path, for which Claude
Code offers nothing and the forge must name a second root itself.
Second, the rosters are scans of the engine's directories
(`.claude/agents/critic-*` and so on), so "one list of everything"
is a question of which roots the scan reads.

**A. A gitignored directory inside the engine, read beside the
engine's own.** For agents this can be a gitignored subfolder of
`.claude/agents/`, since subfolders are scanned; for skills a
gitignored naming pattern under `.claude/skills/`; for states,
genres and templates a second root the dispatchers read. Cheapest,
no new mechanism of Claude Code, the pattern of `CLAUDE.local.md`.
Costs: no namespace, so names must be kept apart by convention
alone; a collision of two agent names inside `.claude/agents/` is
resolved by filesystem read order, undocumented; the user's files
sit inside the engine's tree, so "his own git" means a repository
nested in `.claude/`; a later engine release that takes a name the
user already uses collides at the pull. One list: the existing
scans widened to the subfolder.

**B. The user's own repository added as a directory.** A repository
with its own `.claude/` passed with `--add-dir` at launch; its
skills, commands and agents load. Clean separation and a git of his
own, anywhere on disk. Costs: it must be a launch flag every time
(the settings key grants file access only), so it needs a launcher;
no live reload for agents; no namespace; the collision rule is
stated for commands only; states, genres and templates still need
the forge's second root, pointed at a path outside the engine. One
list: the scans must be told the added path.

**C. Claude Code's user level (`~/.claude/agents/`,
`~/.claude/skills/`).** Works today with no change to the engine,
which answers THR.0300's question "whether Claude Code's own
user-level agents already serve": they register and can preload the
engine's contract by name. Costs: the two collision rules run
opposite ways (a personal skill replaces an engine command of the
same name, a personal agent is replaced by an engine agent of the
same name, neither with a message); the things are seen by every
engine clone and every other project on the machine; they are in
the user's git only if he keeps `~/.claude` in one; the rosters do
not scan there; states, genres and templates have no place.

**D. A plugin per user or per team, through a marketplace.** A
private git repository as catalogue and plugin; components
namespaced by construction; versions, an update command, a rename
map; enabled for one user through the gitignored
`settings.local.json`, or for a team. Costs: the weight of a
marketplace for what may be three files; an installed plugin is a
cached copy that changes only on a version change (a local-directory
marketplace avoids this); plugin agents cannot carry their own
hooks or permission mode; the rosters cannot scan the cache by a
fixed path and would read the registered agents instead; states,
genres and templates travel as plain files of the plugin, found
through its root path.

**D'. The light form of D: a skills-directory plugin.** The user's
pack is a folder with a `.claude-plugin/plugin.json`, kept either
in a gitignored place under the engine's `.claude/skills/` or under
`~/.claude/skills/`, loaded in place with no install, no
marketplace and no version bump, and it is a git repository of the
user's own exactly as a project under `projects/` is. It has the
namespace of D (`<pack>:<agent>`, `<pack>:<skill>`) without its
weight, and a fixed path the forge's dispatchers can scan for
states, genres and templates. Costs: the project-scope form loads
only when Claude Code is started at the engine root and the folder
is trusted, which is the forge's rule anyway; the agent limits of
D; one unproven step, a pack's agent preloading the engine's
contract skill by its bare name.

**E. The engine itself as a plugin, user packs as further
plugins.** The only shape in which a pack can declare "I need the
engine at `^4`" and be disabled with a message when that fails, and
the only real upgrade channel. Costs: everything THR.0190 already
records (no always-on `CLAUDE.md`, the commands and the projects
layout rewritten), which is the question of the brief
`engine-split`, not of this one.

**What each means for the one list and for names.** In A, B and C
the list is one only if the forge scans every root itself, and
names are kept apart only by a convention the forge states and a
check enforces. In D, D' and E Claude Code supplies the namespace
and the forge's list is the engine's scan plus one scan per pack,
each entry carrying its pack's name; the colon is Claude Code's
reserved separator and may not appear in an agent's own name, so
the pack name is the only place a user's namespace can live.

## Relevance to this project and recommendation

What the findings say to the brief's section "User modifications"
and to THR.0300, as Claude's reading, offered once:

1. **"Never mixed, ideally in his own git" has a ready form:** the
   pack as a folder that is its own repository, ignored by the
   engine's git, as projects already are. D' gives that form a
   namespace for free; A gives the same form without one.
2. **The boundary mechanism versus instance (THR.0300) matches the
   field's namespace camp, not its shadowing camp.** "The user
   never changes the mechanism" is Spec Kit's extension rule and
   Claude Code's plugin rule: additions only, under a prefix, no
   taking of a core name. The shadowing camp (OpenSpec, BMAD) is
   the model for a different wish, changing how a core thing
   behaves, which the brief does not ask for and THR.0420 would
   own.
3. **The open question of THR.0300, what happens when the engine
   renames or reshapes a contract, has a documented answer today:
   nothing visible happens.** The agent runs without its contract
   and a line goes to the debug log. Any option short of E needs
   the forge's own detection; the check `engine` already verifies
   every `skills:` entry of an agent against an existing skill, and
   that verification extended over the user's root is the cheapest
   net. The lesson of the field is that the contracts and the shape
   of a state file are the forge's extension surface, and nobody
   surveyed promises such a surface without a version on it.
4. **The rule "a roster is scanned, never written" proposed in the
   note of 2026-09-30 is the precondition** of every option: a
   written roster in `CLAUDE.md` cannot name what the user adds.
5. **Spec Kit's issue 3849 is the warning for the forge's renders
   and README:** whatever lists the user's things must be composed
   when it is read, never baked into an engine file that a release
   regenerates.

**Recommendation.** Take D' as the candidate for THR.0300 and A as
the fallback, and decide between them by one trial before anything
is designed: a pack folder with a manifest, one check agent that
names the engine's `check-contract` in `skills:`, one state file
and one template; started at the engine root; observed for (1)
whether the contract is preloaded, (2) under what name the agent
appears and whether the engine's `/check` can run it, (3) whether a
gitignored nested repository in that place loads after trust on
each platform in use. If (1) fails, A with a stated prefix
convention and a check for collisions is what remains without the
engine split. C is to be named in the documentation as what already
works for a single agent, with its two opposite collision rules
said aloud. E stays with the brief `engine-split`; a pack built as
D' is already a plugin and would need only a `dependencies` line to
move there. This note proposes no convention and changes none; the
names, the place and the shape of a pack are the principal's to
decide in a round of `/forge intent` or in the brief.

## What stays uncertain

- Whether an agent that comes from a plugin can preload a project
  skill by its bare name: the naming rule implies it, no page says
  it, and the forge's reviewer mechanism rests on it.
- The collision rule for skills and agents between the project and
  an added directory, and whether nested `.claude/agents/` below
  the working directory load on file access as nested skills do.
- The skills and subagents pages were read through the fetch tool's
  summary; the precedence orders and the debug-log sentence are
  quoted from that summary, not from the page text.
- Whether a gitignored folder under `.claude/skills/` that is a git
  repository of its own behaves like any other skills-directory
  plugin; nothing suggests otherwise and nothing confirms it.
- How BMAD resolves two modules bringing the same skill name, and
  how Superpowers treats a personal skill of a Superpowers name:
  not found at source.
- Issue trackers were sampled, not swept: one Spec Kit issue was
  read at source; for BMAD, OpenSpec and Agent OS no issue on lost
  customisations was read, only what their own guides admit.

## Sources

All fetched 2026-10-03.

Claude Code documentation, code.claude.com/docs/en/: `skills`,
`sub-agents`, `memory`, `settings`, `permissions`, `changelog`
(newest entry 2.1.288, 2026-10-02), `plugins/manifest-reference`
(reached from `plugins-reference`), `plugins/create-marketplace`
(reached from `plugin-marketplaces`), `plugins/loading`,
`plugins/dependencies`, `plugins/host-marketplace`,
`plugins/components`, `plugins/create`, `plugins/org`. The pages
carry no date of their own; version numbers quoted are those the
pages name.

BMAD Method: docs.bmad-method.org/customize/customize-bmad/ and
/customize/add-modules/ (no date on the pages).

GitHub Spec Kit: github.com/github/spec-kit, `presets/README.md`,
`extensions/README.md`, `extensions/EXTENSION-DEVELOPMENT-GUIDE.md`,
`docs/upgrade.md` (no dates on the files as fetched);
github.com/github/spec-kit/issues/3849 (opened 2026-07-29).

OpenSpec: openspec.dev/docs/customize-schemas;
github.com/Fission-AI/OpenSpec `docs/customization.md` (no dates).

Agent OS: buildermethods.com/agent-os/profiles and
/agent-os/updating (v3.0.0, no date).

Superpowers: github.com/obra/superpowers, `README.md` and
`skills/using-superpowers/SKILL.md` (no dates).

VS Code: code.visualstudio.com/api/advanced-topics/using-proposed-api
(page dated 2026-09-30).

Secondary, used only where marked [2] or to locate primary pages:
web search digests for BMAD customisation, OpenSpec schema
resolution, Spec Kit upgrade issues and Claude Code skill-collision
issues. Not fetched: the systemd manual (refused by the server).
