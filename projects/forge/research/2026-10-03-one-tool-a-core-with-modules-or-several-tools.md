---
project: forge
type: research
topic: how comparable ecosystems divide the whole - one tool, a core with modules, or several tools handing artefacts
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (The shape of the whole); 10-intent.threads.md (THR.0230, THR.0420, THR.0300, THR.0140); 2026-08-25-comparable-projects-landscape.md; 2026-08-29-framework-distribution-in-the-field.md
status: immutable
---

# One tool, a core with modules, or several tools

## Question

How do comparable ecosystems divide the whole - as one general
tool, a core with modules or packs on it, or several separate tools
that hand outputs to each other - and what has each division been
seen to cost and to give?

Who the neighbours are is the note
`2026-08-25-comparable-projects-landscape.md`; how each is
installed and upgraded is
`2026-08-29-framework-distribution-in-the-field.md`; what a Claude
Code plugin can and cannot carry is
`2026-08-29-claude-code-packaging.md`; how files meet a tracker is
`2026-10-03-where-requirements-meet-outside-git.md`. None of that
is repeated here. This note asks only where the cut between core
and the rest runs, who may add what, and what the cut has cost.

How to read the claims. Tags: **[V]** verified on a page fetched
on 2026-10-03; **[S]** taken from a secondary source (a search
result's digest, a forum member's account, a third party's
article); **[M]** my own synthesis. The fetch tool returns a
summary made by a small model, not the page: every quotation
tagged [V] came through that summary and is to be checked at the
URL before it is quoted onward. The exception is the three Claude
Code documentation pages, which arrived as full text. Where a page
could not be fetched, it is said.

## Answer in one paragraph

Nobody in the surveyed field stays one closed tool, and nobody
runs several equal tools that hand artefacts to each other as a
designed system: every AI framework read has ended at a small core
with typed extension points, and the documented movements go in
both directions - parts moved out of the core when one maintainer
or one release train could not carry them (BMAD's modules,
Terraform's providers, Ansible's collections), and parts moved
back or deleted when the split or the ambition cost more than it
gave (Superpowers' skills repository, BMAD's remote registry,
Agent OS cut by about 70 %, Segment's 140 services). What is
consensus: the core is the mechanism and the shared format, the
module is content; modules declare the core version they need;
community modules are listed but not reviewed. What is contested:
whether third parties may add at all (Superpowers and Hugo say no,
or nearly), and how much of a framework survives the harness
growing under it. What the older literature adds is a warning
about order: boundaries drawn before two or three real cases exist
are usually drawn wrong, and a core extracted ahead of its
products is paid for before it pays back.

## Key findings

### 1. The AI spec-driven and agent frameworks today

**BMAD Method** - a core with modules, most of them in
repositories of their own.
- In v4 the unit of extension was the "expansion pack", each in a
  dot-folder of its own beside `.bmad-core`; v6 put everything
  under one `_bmad/` with `core/` as the universal layer and
  modules beside it (`bmm` the method itself, `bmb` the builder,
  `cis`), and the game-development packs were merged into one
  module while the infrastructure pack was discontinued [S: search
  digest of docs.bmad-method.org/how-to/upgrade-to-v6/; the page
  itself returned only a redirect on 2026-10-03].
- The method is itself a module on the core, not the core [S, same
  digest; consistent with the README's ecosystem table, V].
- v6.0.0-Beta.1 (January 2026): "bmad-builder, CIS (Creative
  Intelligence Suite), and Game Dev Studio moved to separate
  repositories for focused development" [V: CHANGELOG]. The README
  now lists five official modules, each a repository: Builder,
  Creative Intelligence Suite, Test Architect, Loop, Game Dev
  Studio [V: README].
- Who may add: anyone, through the Builder module, which creates
  agents, workflows and modules and packages them "through the
  BMad Marketplace or any compliant public marketplace" [V:
  bmad-builder README]. A custom module installs from any git URL
  or local path, pinned by a git ref, behind the warning
  "UNVERIFIED MODULE: This module has not been reviewed by the
  BMad team" [V: docs.bmad-method.org/customize/add-modules/].
- Dependence on the core's version: v6.4.0 (2026-04-24) gave
  "stable and bleeding-edge release channels, standardized across
  all modules", with per-module pinning; the changelog states no
  rule that ties a module version to a core version [V: CHANGELOG].
- Retreats, read from the changelog [V]: v6.7.0 (2026-05-17)
  "Remote marketplace registry fully retired", "Community modules
  picker removed from the interactive installer", the bundled
  `bmad-modules.yaml` now "the single source of truth" for official
  modules; v6.11.0 (2026-08-09) "Core drops from fourteen skills to
  eight", review, research and documentation skills merged. The
  changelog gives no reason for retiring the registry; that a
  curated remote catalogue was more than the maintainers wished to
  carry is my reading [M].
- Earlier note: the v4 to v6 migration was disruptive because v4
  customisation edited the shipped files
  (`2026-08-29-framework-distribution-in-the-field.md`).

**GitHub Spec Kit** - a core with five typed extension points.
- Extensions "add domain-specific processes, external integrations,
  or development phases beyond the core" (commands, templates,
  scripts, hooks); presets override templates and commands "without
  forking or modifying core files"; project-local overrides;
  workflows; and bundles, which provision "a complete role-based
  setup in one operation" [V: customization guide, presets README].
  The README's own sentence: "Extensions add capabilities, presets
  adapt existing behavior, workflows automate steps, and bundles
  package a role-based setup" [V].
- Stated motive: extensions let one "add new functionality without
  bloating the core framework" [V: extensions README].
- Resolution order: project overrides, presets by priority,
  extensions, core [V].
- Dependence on the core: the extension manifest must carry
  `requires: speckit_version` with a semantic-version range, and
  may name the core commands and outside tools it needs; commands
  are namespaced `speckit.{ext-id}.{command}`; an extension hooks
  into the core's lifecycle (`before_plan`, `after_tasks`) [V:
  extension development guide].
- Who may add: anyone; the upstream catalogue an organisation
  installs from is shipped empty for the organisation to curate,
  and the community catalogue is listed with the disclaimer that
  maintainers "do not review, audit, endorse, or support the
  extension code itself" [V: extensions README].
- No maintainer statement of cost was found; the multiplication of
  extension kinds (three in the note of 2026-08-29, five now) is
  itself the visible sign of pressure on the core [M].

**OpenSpec** - a fixed lifecycle with the workflow as data.
- The reason given for leaving the old fixed workflow:
  "Instructions are hardcoded - buried in TypeScript, you can't
  change them", "Fixed structure - same workflow for everyone, no
  customization", "One big command creates everything" [V:
  docs/opsx.md]. No cost of the change is acknowledged there.
- A schema defines the artefacts, their dependencies and order,
  templates and per-artefact instructions; the change lifecycle,
  the CLI, the configuration and archive mechanics stay core. One
  schema ships (`spec-driven`); a user forks it or starts one
  (`openspec schema fork`, `schema init`), in the project or
  user-global; the schema is chosen by flag, by the change's
  metadata, by project configuration, then the default [V:
  docs/customization.md].
- Community schemas live in their authors' repositories and are
  copied in by hand; one of those listed is a bridge to another
  framework (`superpowers-bridge`) [V]. Nothing is said about a
  schema's compatibility with the core's version [V: absent on the
  page].
- This is the closest outside model of "a new framework is written
  as content only" (THR.0230): the artefact chain is data, the
  mechanism is the tool [M].

**Superpowers** - one closed tool that tried a split and took it
back.
- v2.0.0 (2025-10-12): "Skills no longer live in the plugin.
  They've been moved to a separate repository", cloned to the
  user's configuration directory and fetched at every session
  start, so that users could fork and edit [V: RELEASE-NOTES].
- v3.0.1 (2025-10-16), four days later: "We now use Anthropic's
  first-party skills system!" and the skills returned to the
  plugin [V]. The separate repository was archived on 2025-10-27
  [V: its GitHub page]. No reason is written beyond the sentence
  quoted; that the harness gained a native mechanism which made
  the home-made one redundant is the plain reading [M].
- Today the README says "we don't generally accept contributions
  of new skills" and that any change must work across every
  supported coding agent; about seventeen skills ship [V: README].
  The core is closed on purpose; whoever wants more writes a plugin
  of his own.
- Later releases keep deleting what the harness now does: the
  per-harness tool tables went because they "restated guidance
  modern agents already follow" (v6.1.0), the legacy slash commands
  and a named agent were removed (v5.1.0) [V: RELEASE-NOTES].

**Agent OS** - the ambition cut back, with the reason stated.
- v3 (January 2026, the discussion titled "Leaner and more aligned
  for 2026"): the maintainer removed spec writing, task breakdown
  and implementation orchestration, because the coding tools now do
  them, and wrote that it "doesn't make sense to reinvent these
  core functions, which are much better handled by the core tools
  than 3rd-party frameworks" [V: discussion 310]. About 70 % of the
  framework went [S: search digest].
- What remained is the part the harness does not own: discovering,
  recording and injecting a team's standards [V].
- The cost seen in the replies: no guidance on what to do with the
  old files of v2, and a release reported unusable until pending
  pull requests were merged [V: replies of 2026-02-02 and
  2026-02-09].
- This is the clearest sign in the field of an ambition outgrowing
  what one maintainer could carry against a moving harness [M].

**Kiro** - one tool with a fixed chain; extension only at the
side.
- A spec is three files (requirements or bugfix, design, tasks) in
  two kinds, feature and bugfix, with a quick variant; the docs
  show no way for a user to define a spec type of his own [V:
  kiro.dev/docs/specs/; absence on the page, not a stated ban].
- "Powers" extend the agent's knowledge and tools, not the chain: a
  package of skills, MCP configuration and steering that follows
  the Agent Plugins format and is loaded only when the task matches
  its keywords; the stated reason is context cost ("Connect five
  MCP servers and your agent loads 100+ tool definitions"); anyone
  may publish one from a git URL [V: kiro.dev/docs/powers/].

Pattern across the six [M]: the chain of artefacts is either fixed
(Kiro, Superpowers), overridable piece by piece (Spec Kit, BMAD),
or data (OpenSpec). Nobody ships two chains as two separate tools.
Where a second chain exists (BMAD's game development, test
architecture, creative suite) it is a module on the same core.

### 2. How Anthropic's own packaging divides things

Read as full text from the Claude Code documentation, 2026-10-03.
- The unit is the plugin: "a directory of skills, agents, hooks,
  MCP servers, or other components that Claude Code installs and
  loads as one unit". A skill, an agent or a hook also works on its
  own; the advice is to "use a plugin when you want several skills,
  subagents, hooks, or MCP servers packaged as one unit" [V].
- There is no core plugin. The core is the harness and the formats;
  plugins are peers. A plugin's skill runs under the plugin's name
  (`/my-plugin:review`), which is the collision rule [V].
- Dependencies between plugins exist: a `dependencies` array in
  `plugin.json`, each entry optionally with a semantic-version
  range resolved against git tags `<plugin-name>--v<version>`;
  several plugins' ranges on one dependency are intersected, and a
  conflict fails the install; a plugin with nothing but a name and
  dependencies is a valid bundle ("a platform team can publish
  role-specific bundles"); a dependency in another marketplace is
  installed only if the root marketplace allows it [V:
  plugins/dependencies]. The page states the cost of no constraint
  in its own words: "If that release renames an MCP tool your
  plugin calls, your plugin breaks for everyone who updates."
- An enabled plugin costs context in every session whether used or
  not: the name and description of every skill and agent are
  loaded each turn [V: plugins overview]. Dividing into several
  plugins that can be enabled per need is therefore also a way to
  pay for less.
- Marketplaces are catalogues in three tiers (official, community,
  third-party); "Anthropic doesn't review third-party marketplaces"
  [V: plugins/anthropic-marketplaces].
- The knowledge-work collection divides by profession: eleven
  plugins (productivity, sales, customer support, product
  management, marketing, legal, finance, data, enterprise search,
  bio-research, and one for making and customising plugins), each
  with the same four parts (manifest, connectors, commands,
  skills), "generic starting points" to be customised by editing;
  no shared core among them and no dependency between them is
  described [V: github.com/anthropics/knowledge-work-plugins,
  through the summarising fetch]. The division is several peers of
  one format and one builder, which is the same shape as BMAD's
  Builder beside its modules [M].
- What a plugin cannot carry (an always-on CLAUDE.md) is the
  finding of `2026-08-29-claude-code-packaging.md` and bears on
  every option below.

### 3. Older analogies with documented experience

**Parts moved out of a core, with the reason stated.**
- Terraform 0.10 (announced 2017-06-09): providers left the single
  binary because "small bug fixes, new features, or security
  releases for a single provider are blocked until the next release
  of the main Terraform binary"; each provider got a repository
  with its own permissions and its own version, constrained from
  the user's configuration. Acknowledged cost: open pull requests
  did not migrate, and "this provider migration may cause
  disruption for some users in the short-term" [V: HashiCorp blog].
- Ansible 2.10 (2020): the one repository had become "too
  burdensome to maintain", with many modules "minimally maintained
  (or even broken!)"; the core kept the engine and a minimal set,
  everything else went to collections with their own repositories
  and release cycles [V: a community author's article of
  2020-02-21, not the vendor]. The backlog of 4,300 open issues and
  2,000 pull requests is from a search digest [S].
- IPython to Jupyter, "the Big Split" (IPython 4.0, August 2015):
  the language-independent parts left for repositories of their
  own, releasing at their own pace, with shims left behind so old
  imports worked with a warning [S: search digest of the IPython
  release notes; the project's blog post could not be fetched].
- What the three share [M]: the split came after the whole had
  grown and the boundary had shown itself in practice (providers,
  modules, the language line); the reason was the maintainers'
  capacity and the release train, not elegance; and each kept the
  old way working for a while.

**Parts moved back.**
- Segment, "Goodbye Microservices" (2018-07-10): one service per
  destination was introduced for isolation; at 140 services the
  shared libraries diverged ("Making changes to improve our
  libraries, knowing we'd have to test and deploy dozens of
  services, was a risky proposition") and "operational overhead
  increased linearly with each added destination"; they merged
  back and accepted weaker fault isolation [V].
- Superpowers and BMAD above are the same movement in this field.

**When to draw boundaries.**
- Fowler, "MonolithFirst" (2015-06-03): "Almost all the successful
  microservice stories have started with a monolith that got too
  big and was broken up", because "even experienced architects
  working in familiar domains have great difficulty getting
  boundaries right at the beginning"; the counter-view he records
  is that a system replacement, where the boundaries are already
  known, may start divided [V].
- Software product lines: the classic assumption is an up-front
  investment worth two to three products before core assets pay
  back, and the proactive way (core assets first) needs "predictive
  knowledge" of the products to come; reactive and extractive ways
  take the core out of products that already exist [S: search
  digest; the journal page returned 403].

**A platform with plugins against a closed tool.**
- VS Code runs extensions in a separate extension host so that they
  cannot affect startup, slow the interface or change it, and loads
  each only on its activation event: "misbehaving extensions should
  not impact the user experience" [V: VS Code API docs]. The price
  of an open door is a wall and a narrow API.
- Hugo has no plugins. The reasons a forum member collected from
  earlier discussions: more work for the team, a worse experience
  for users who must install extensions before a theme works,
  security, documentation [S: forum post of 2017-09-25, explicitly
  not a maintainer's statement]. Reuse came later as modules that
  mount content and templates, data and not code [S].
- Gatsby shows the other side: a plugin that pins an old major of
  the core as a peer dependency "won't work as expected with the
  latest Gatsby version", and authors stop maintaining [V: the
  vendor's blog, 2021-12-01].
- Pattern literature on the microkernel style names the standing
  costs: an extension API that cannot change without breaking
  plugins, version skew, and "pressure to add feature logic to the
  stable core" [S: search digest of several tutorials, not a
  practice report]. No first-hand practice report on microkernel
  against monolith in the operating-system sense was fetched; that
  part of the question stays unanswered here.

**Small tools joined by files.**
- McIlroy, 1978: "Make each program do one thing well" and "Expect
  the output of every program to become the input to another, as
  yet unknown, program"; Salus, 1994: text streams "because that is
  a universal interface" [V: through the encyclopedia article, not
  the originals]. The recorded criticism is of the user's side: the
  whole has no one who designs the experience across the tools [V,
  same page].
- What makes it work is that the contract is the format, known
  before either tool exists, and that it is poor on purpose [M].

### 4. Handing artefacts between stages or tools

- Discovery to delivery in one vendor's suite: an idea stays an
  object in the discovery tool; a "delivery ticket" is any issue in
  the delivery tool linked to it, one idea to many epics allowed;
  nothing of the idea's text is carried by the link itself, and
  what flows back is a computed progress bar and status from the
  linked issues [V: vendor's guide]. Copying fields across needs
  automation rules written by the user [S: community forum]. The
  contract is a link and a status, not a document.
- Files to a tracker: one-way publication with the file-side ID
  carried and drift reported, as
  `2026-10-03-where-requirements-meet-outside-git.md` found.
- Between the AI frameworks themselves the only hand-over found is
  a community schema that bridges one framework's workflow into
  another's skills [V: OpenSpec customization page lists it; its
  content was not read]. No two frameworks of this field publish a
  contract for each other's artefacts [M: absence in what was
  read, not proof].
- What a hand-over contract consists of wherever one was seen [M]:
  a stable identifier that travels, a statement of which side is
  the source of truth, a one-way flow of content, and at most a
  state flowing back. The forge already has all four inside itself:
  stable IDs, the ledger's Dependencies table, the rule that a
  render is never a source, finding states.

### 5. Where practice stands

- **Consensus [M over V]:** a small core that owns mechanism and
  format, with content in typed units outside it; extension through
  override or addition and never by editing shipped files; units
  namespaced; units declaring the core version they need (Spec Kit,
  Claude Code plugins; BMAD by pinning); community units listed and
  explicitly not reviewed.
- **Emerging [M over V]:** role bundles as a thin layer over
  modules (Spec Kit bundles, Claude Code dependency-only plugins,
  the knowledge-work collection); a builder shipped as a module for
  making modules (BMAD Builder, the plugin-management plugin, Spec
  Kit's development guide); the workflow itself as data (OpenSpec
  schemas).
- **Contested [M over V]:** whether third parties add to the
  ecosystem at all (open with a disclaimer at Spec Kit and BMAD;
  closed at Superpowers and Hugo; BMAD withdrew its community
  picker); whether a remote registry is worth running; and how
  much of any framework should exist beside the harness (Agent OS
  and Superpowers delete, BMAD and Spec Kit add).
- **Not found:** a maintainer's account, in this field, of several
  separate tools designed to hand artefacts to each other; and any
  measurement of users lost between tools. The costs of
  fragmentation above are from the older analogies.

## Options with trade-offs

All four as findings bear on them; the weighing is mine [M].

**A. Stay one tool.** The forge as it is, growing by layers and
by a user's own additions (THR.0300).
- Gives: one release train, one CLAUDE.md, no extension API to
  keep stable, nothing for a second person to mismatch. It is
  where Superpowers and Hugo stand by choice.
- Costs: every other job (THR.0420) is a fork that carries the
  whole mechanics and drifts; the core grows anyway (THR.0240);
  the pressure Spec Kit names as "bloating the core" has no outlet.
- Fits when: the forge's one job is the product, and other jobs
  are few and far.

**B. One tool with a general mode.** The same forge, plus a way to
work without a known artefact: ingest, research, logs, history and
elicitation with no chain behind them.
- Gives: the cheapest answer to "work without a known artefact",
  no boundary to draw yet, and a real second case from which a
  boundary could later be read - the reactive way of the product
  line literature, and the order Fowler reports as the one that
  worked.
- Costs: the general mode has no Map, as the brief already says;
  the nearest outside warning is Agent OS, whose generic
  scaffolding was the part the harness overtook, while its specific
  part survived. A general mode is the part of the forge most like
  what the harness itself offers.
- Fits when: there is one concrete case waiting (the brief names
  one) and no second chain is yet defined.

**C. A core plus frameworks as packages of instances.** The
mechanism stays in one place; a framework is a set of state files,
templates, reviewers and recipes, chosen per project.
- Gives: the field's consensus shape, with OpenSpec's schema as
  the closest model and BMAD's method-as-a-module as the proof that
  the first framework can be one among equals; Claude Code already
  offers namespacing, version ranges and bundles for it.
- Costs: an extension contract that must then stay stable or be
  versioned (the standing cost in every plugin ecosystem read);
  packages that break on an upgrade of the core unless they declare
  what they need and something checks it; two to three packages'
  worth of work before it pays back; and the core's CLAUDE.md
  cannot travel in a plugin. The documented retreats (BMAD's
  registry, Superpowers' repository) were both from distribution
  machinery, not from the idea of content outside the core - so the
  risk sits in the machinery, and the cheap form is directories in
  one repository first.
- Fits when: a second chain exists on paper in enough detail to
  test the boundary against, and the same person can still carry
  both.

**D. Separate forges handing artefacts through a contract.** Each
derivation a tool in its own right; an approved assignment of one
is the registered source of the next.
- Gives: each stays small and comprehensible; teams adopt one
  without the others; it is the direct reading of "one tool that
  does everything is not wanted", and the Unix lesson that a poor,
  fixed format is contract enough. The forge's own Dependencies
  table and `/ingest` already are that contract in small.
- Costs: the mechanics are copied and drift apart exactly as
  Segment's shared libraries did; each fork needs its own upkeep
  against every new harness version; nobody designs the experience
  across them; and in this field no maintainer was found doing it,
  so there is no experience to borrow.
- Fits when: the derivations have different owners, or differ in
  mechanism and not only in content.

The options are less exclusive than they look [M]: B is a step
that produces the evidence for C; D's contract is needed between
projects whatever the tool count; and C does not answer D's case of
a different owner.

**What evidence would tell which fits.**
- Whether a second chain, written out as state files and templates,
  can be added without touching CLAUDE.md - the test THR.0300
  already states. If yes for two different jobs, C is cheap and
  mostly there; if each needs the always-on file changed, the
  boundary is not where it was assumed.
- How much of a derivation is content and how much mechanism: one
  outlined case of THR.0420 (unattended runs, verification of an
  implementation) reads as new mechanism, which points to D for
  that case whatever is chosen for the others.
- Whether the general mode, tried once on a real case, yields
  anything that the bare harness with its own skills does not.
- Who would maintain each part, and how many people: every split
  read here followed the maintainers' capacity, not the design.
- How often the core's shapes still change. While the history, the
  ledger and the state files are still being reshaped release by
  release, any package written against them breaks often; a
  statement of what does not change between versions (the brief's
  upgrade section) comes before C, not after.

## Relevance to this project

- The principal's word against one tool that does everything and
  the idea of a core with frameworks do not contradict each other
  in the field's terms [M]: the frameworks read here avoid the one
  large tool precisely by keeping the core to mechanism and putting
  each job's content outside it. What the word rules out is A
  growing by absorption, not C.
- The two levels the brief sees (today's forge to which a user
  adds; a core beneath, separate from the artefacts) are the same
  two that Spec Kit and BMAD ended with: an override and addition
  layer for the user, and typed modules for a whole job. The field
  keeps them apart as different extension kinds with one resolution
  order, which bears on the brief's open question whether user
  modifications are the engine split or a level of their own: in
  the field they are a level of their own, on the same mechanism.
- The brief's doubt about the ambition has outside support. The
  two frameworks most like the forge in being one maintainer's work
  inside a moving harness both shrank: one deleted about 70 %, the
  other closed its core to new skills and keeps removing what the
  harness now does. Neither grew a module ecosystem.

**Recommendation** [M, on the findings above; a direction, not a
design].

1. Do not divide now. Take B as a trial on the one real case the
   brief names, with the mechanism untouched, and record what the
   general mode needed that the chain did not give and what it
   used unchanged. That record is the boundary, observed and not
   predicted.
2. Treat C as the likely destination and keep the way to it open
   at no cost: hold to the mechanism-versus-instance rule already
   written in THR.0300, and let the next layer (the BRD) be added
   as an instance, counting every place in CLAUDE.md and the
   skills that had to change. The count is the measure the brief
   asks for.
3. Decide C only when a second chain exists in enough detail to be
   written as a package, and then in its cheapest form -
   directories in the one repository, no registry, no installer -
   since the retreats on record were all from distribution
   machinery.
4. Keep D for the case where the owner or the mechanism differs,
   and write the hand-over contract regardless of the tool count,
   because projects already need it: an approved artefact with its
   stable IDs is registered as a source downstream, the upstream
   stays the source of truth, nothing flows back but a state.
5. Before any package is written by anyone but the core's author,
   state what does not change between versions and have packages
   declare the version they need, as Spec Kit and Claude Code's
   plugins do; without that, the cost on record is modules that
   break silently on upgrade.

What stays uncertain. Most quotations came through a summarising
fetch. The reasons behind BMAD's and Superpowers' retreats are not
stated by their maintainers and are read here from the sequence of
releases. Whether any team runs two of these frameworks in a
designed hand-over was not found, which is not proof that none
does. The microkernel-versus-monolith part rests on pattern
literature and one service-architecture report, not on operating-
system practice. No source measures users lost between tools.

## Sources

All fetched 2026-10-03.

AI frameworks:
- https://github.com/bmad-code-org/BMAD-METHOD (README)
- https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/CHANGELOG.md
  (v6.0.0-Beta.1 January 2026; v6.4.0 2026-04-24; v6.7.0
  2026-05-17; v6.11.0 2026-08-09; newest stable v6.12.0
  2026-09-03)
- https://github.com/bmad-code-org/bmad-builder
- https://docs.bmad-method.org/customize/add-modules/
- https://docs.bmad-method.org/how-to/upgrade-to-v6/ (redirect
  only; content from a search digest)
- https://github.com/github/spec-kit (README)
- https://github.com/github/spec-kit/blob/main/extensions/README.md
- https://github.com/github/spec-kit/blob/main/extensions/EXTENSION-DEVELOPMENT-GUIDE.md
- https://github.com/github/spec-kit/blob/main/presets/README.md
- https://github.github.io/spec-kit/guides/customization.html
- https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md
- https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md
- https://github.com/obra/superpowers (README)
- https://raw.githubusercontent.com/obra/superpowers/main/RELEASE-NOTES.md
  (v2.0.0 2025-10-12; v3.0.1 2025-10-16; v5.1.0 2026-04-30;
  v6.1.0 2026-06-30; newest v6.4.2 2026-09-25)
- https://github.com/obra/superpowers-skills (archived 2025-10-27)
- https://github.com/buildermethods/agent-os/discussions/310
  (January to February 2026)
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/powers/

Anthropic's packaging:
- https://code.claude.com/docs/en/plugins (full text)
- https://code.claude.com/docs/en/plugins/dependencies (full text)
- https://code.claude.com/docs/en/plugins/anthropic-marketplaces
  (full text)
- https://github.com/anthropics/knowledge-work-plugins

Older analogies:
- https://www.hashicorp.com/en/blog/upcoming-provider-changes-in-terraform-0-10
  (2017-06-09)
- https://www.jeffgeerling.com/blog/2020/collections-signal-major-shift-ansible-ecosystem
  (2020-02-21)
- https://ipython.readthedocs.io/en/7.x/whatsnew/version4.html
  (IPython 4.0, August 2015; search digest only)
- https://blog.jupyter.org/the-big-split-9d7b88a031a7 (fetch
  returned no content)
- https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/
  (2018-07-10)
- https://martinfowler.com/bliki/MonolithFirst.html (2015-06-03)
- https://cacm.acm.org/research/new-methods-in-software-product-line-practice
  (403; search digest only)
- https://code.visualstudio.com/api/advanced-topics/extension-host
- https://discourse.gohugo.io/t/does-hugo-support-hooks-event-listeners/8495/2
  (2017-09-25, a forum member's summary)
- https://www.gatsbyjs.com/blog/gatsby-plugin-not-working-but-why
  (2021-12-01)
- https://quality.arc42.org/approaches/plugin-architecture and
  tutorials of the microkernel pattern (search digest only)
- https://en.wikipedia.org/wiki/Unix_philosophy (for McIlroy 1978
  and Salus 1994)

Hand-over:
- https://www.atlassian.com/software/jira/product-discovery/guides/delivery/overview
- https://community.atlassian.com/forums/Jira-questions/I-would-like-to-sync-product-discovery-ticket-fields-with-a/qaq-p/2922331
  (search digest only)
