---
project: forge
type: research
topic: versions, a stable line beside development, and migration of the user's existing content
date: 2026-10-03
derived_from: 00-brief-next-gen.md (draft, "Upgrade and compatibility"); 10-intent.md (POS.0940, POS.0820, POS.0300, POS.0730); research/2026-08-29-framework-distribution-in-the-field.md; research/2026-10-03-what-a-write-touches-and-where-two-authors-collide.md (finding 5, option H)
status: immutable
---

# Versions, channels and the migration of the user's content

## Question

How do comparable frameworks and tools handle versions, a stable line
beside the one under development, and the migration of the user's
existing content to a new structure - and what follows for the forge,
where a project records no engine version (POS.0940), an artefact
stays valid under the conventions it was written to (POS.0820), the
release number is the intent's version (POS.0300, POS.0730) and two
people on one project with two engines produced documents of two
structures (the draft brief `next-gen`, "Upgrade and compatibility")?

How the engine is separated from the user's content, and what an
upgrade overwrites, is answered in
`2026-08-29-framework-distribution-in-the-field.md` and not repeated.
What in a project depends on the engine, and how two engines collide,
is finding 5 of
`2026-10-03-what-a-write-touches-and-where-two-authors-collide.md`;
its option H names four directions in one paragraph, and this note is
the survey behind them.

**Epistemic tags.** [V] verified on a page fetched on 2026-10-03.
[V-s] the same, but the fetch tool passes the page through a small
summarising model before returning it, so wording given in quotation
marks is the wording the tool returned and was not compared with the
page by eye; this holds for every fetched source except the three
Claude Code documentation pages, which arrived as raw text and are
tagged [V]. [S] taken from a search-result summary or another
secondary source, not opened at the primary. [H] the author's own
synthesis. Status words: consensus, emerging, contested.

## Answer in short

Tools whose users own content in a format the tool defines almost
all write a **format version into the content itself**, separate
from the tool's own version, and bump it rarely; the tool states
which formats it reads and refuses or warns on a newer one. The AI
spec frameworks mostly do not: they version the installed engine
files, find a legacy project by the presence of old files, and leave
the user's documents to be moved by hand. A stable line beside the
developing one is ordinary and cheap when it is a pointer that moves
at releases, expensive when it is a branch that receives backports.
Migration is everywhere ordered and forward-only; doing it by an AI
that follows a written guide is an emerging practice with published
examples and no evidence yet on reliability for prose documents.
The prompting case had two causes, and each has a standard remedy:
the collaborator followed the line under development (remedy: a
stable pointer), and nothing in the project said which conventions
it was at (remedy: a recorded format level and a reader that
compares).

## Key findings

### 1. The AI spec-driven and agent frameworks

| Framework | Version recorded where | Mismatch found by | Migration of user documents | Coexistence | Known to fail |
|---|---|---|---|---|---|
| BMAD Method | installer and manifest; channel per module | installer detects v4/v5 folders | manual: move files, tell the agent what is done | shims for retired skills until v7 | direct edits lost; duplicates after upgrade |
| Spec Kit | CLI; `.specify/integration.json` | `specify self check`; manifest | none needed, `specs/` never touched | n/a | overwritten or stale managed files |
| OpenSpec | CLI | `init`/`update` detect legacy files | automatic for its own files; one file by hand | none: one-way | non-interactive run skips cleanup without `--force` |
| Agent OS | none in the project | nobody; the user re-runs the script | by hand, "What's New" | n/a | customised commands merged by hand |
| Superpowers | plugin manifest | plugin update | optional file moves, stated in release notes | deprecation notices for one major | - |
| task-master | CLI | legacy paths detected | `task-master migrate` | legacy layout keeps working | - |

- **BMAD, v4 to v6.** The installer detects a v4 or v5 install and
  offers to back up and remove `.bmad-method`; a renamed folder and
  the old IDE command folders are removed by hand. The user's
  planning documents are not migrated: they are to be moved to
  `_bmad-output/planning-artifacts/`, and for work in progress the
  user runs sprint planning and tells the agent "which epics/stories
  are already complete"; mid-planning the guide says "Consider
  restarting with v6 workflows. Use your existing documents as
  inputs." Direct edits of agent files "are lost" [V-s, the upgrade
  guide as mirrored at mintlify.wiki; the project's own page
  redirected]. Issues filed on the upgrade concern duplicated agents
  after v4 to v6 (#1414, #1422) and missing agents after install
  (#2117), all closed [V-s, issue list only, bodies not read].
- **BMAD inside v6.** The changelog shows breaking changes at minor
  releases through 2026 (config from YAML to TOML at 6.4.0; skills
  renamed and merged at 6.11.0; a variable renamed at 6.12.0) and
  three mechanisms beside them: the installer migrates its own
  config keys and renames customisation files on the next run; a
  retired skill stays as a forwarding shim "until the v7 cut"; and
  modules follow a channel - `stable` by default, `next` for the tip
  of the main branch, or a pinned tag [V-s]. What the changelog
  calls for by hand is always the user's own overrides. Status:
  emerging; this is the most developed channel-and-shim practice
  among the AI frameworks surveyed [H].
- **Spec Kit.** Upgrade is two-part (tool, then project files); the
  guide marks `specs/` as never modified, so the user's documents
  need no migration, and the tool can be pinned (`specify self
  upgrade --tag vX.Y.Z`) and checked (`specify self check`) [V-s].
  What fails is the managed layer, not the content: closed issues
  report an upgrade overwriting extension- and preset-provided
  skills (#3849), `init --here --force` not updating existing
  scripts and templates (#2319), stale vendored scripts breaking
  newer integrations (#2293) [V-s, issue list only]. Older versions
  of the guide told users to back up the constitution and templates
  before `--force` [S].
- **OpenSpec, 1.0.** `openspec init` or `openspec update` detects
  and deletes its own legacy files (old command folders, its marker
  blocks in `CLAUDE.md` and `AGENTS.md`); active and archived change
  folders and specs are "Completely preserved"; one file,
  `openspec/project.md`, is left for the user to carry into
  `config.yaml` by hand. The migration is one-way [V-s]. In
  non-interactive mode the cleanup does not run without `--force`
  [S].
- **Agent OS.** Updating is replacing the base install and re-running
  the project script; the page fetched names no version check and
  sends the reader to "What's New" for what changed between majors
  [V-s]. v3 removed spec writing in favour of the host's plan mode
  and moved profile inheritance into `config.yml` [S].
- **Superpowers.** A plugin: the update reaches users through the
  plugin mechanism. Breaking changes are stated in dated release
  notes; where the user's files are affected the move is optional
  ("move existing files from docs/plans/ to new locations if
  desired", v5.0.0), existing worktrees "adopted in place" (v6.0.0),
  and removed commands first "show deprecation notices" for one
  major [V-s].
- **task-master.** The one framework here with a shipped migration
  command for the user's own files: `task-master migrate`, with
  `--dry-run` and `--backup`, for the move into `.taskmaster/`;
  projects in the legacy layout "will continue to work" until
  migrated [S, a mirror of the project's migration guide].

**Reading [H].** None of these records a format version inside the
user's documents. They get away with it because the user's documents
are loosely shaped prose the tool reads but does not parse, and
because a legacy state is recognisable by a file's presence. Where
the tool's own files are concerned they have all grown a version
record (manifest, channel, pin). The forge's documents are not
loosely shaped: history records, ledger tables, state words and
front-matter are a format the checks read strictly. On this axis the
forge belongs with the tools of finding 3, not with its peers.

### 2. Claude Code as a model of channels

- **Two channels of the tool.** `autoUpdatesChannel` is `"latest"`
  (default) or `"stable"`: "a version that is typically about one
  week old, skipping releases with major regressions". The package
  repositories and Homebrew offer the same two lines. `stable` is a
  delayed pointer on the same sequence of releases, not a branch
  with its own fixes [V].
- **Floors and ceilings.** `minimumVersion` is a floor for updates;
  managed settings `requiredMinimumVersion` and
  `requiredMaximumVersion` "make Claude Code refuse to start outside
  a version range" - an organisation can hold all its users inside
  one window [V].
- **Plugins.** A plugin's `version` is "not checked against semver";
  setting it "pins the plugin to that version until you change it",
  and "If you set "version": "1.0.0" and push new commits without
  changing it, users don't receive them"; omitting it makes users
  track commits. Channels are not a concept of the plugin system:
  "host two marketplaces whose entries point at different refs of
  the same plugin", or let users add `owner/repo#stable`. A rename
  is carried by an append-only `renames` map that migrates users'
  settings automatically; "There is no deprecation state" for a
  plugin [V].
- **How a feature declares the version it needs.** In prose, per
  feature ("Requires Claude Code v2.1.222 or later"), and by failure:
  a manifest using a newer field makes older clients fail to load
  the plugin [V]. A plugin has no field for the client version it
  requires [V, by absence in the field table].
- **Deprecations** are announced in the changelog and at run time
  (the npm install path deprecated at v2.1.15 with a migration
  command) [S].

### 3. Tools whose users own content in a format the tool defines

- **Jupyter notebooks.** The file carries `nbformat` and
  `nbformat_minor`. "When backward-compatible changes are made, the
  notebook format minor version is incremented. When
  backward-incompatible changes are made, the major version is
  incremented." Unknown new cell or output types "will be preserved"
  by an older reader [V-s]. The model case of a format version in
  the content plus a tolerant reader. Consensus.
- **Go modules.** "The go line declares the minimum required Go
  version for using the module." Since Go 1.21 an older toolchain
  "refuses to load a module or workspace that declares a minimum
  required Go version greater than the toolchain's own version" -
  and that refusal was backported into older release lines so that
  they, too, would stop [V-s]. The content names the tool it needs;
  the older tool stops instead of writing.
- **Rust editions.** "Each crate chooses its edition within its
  Cargo.toml file"; editions are opt-in, crates of different
  editions "must seamlessly interoperate", and `cargo fix` migrates
  mechanically, though "there may still be corner cases where manual
  changes are required" [V-s]. The strongest precedent for old and
  new structures coexisting indefinitely - bought by a compiler that
  carries every edition for ever.
- **Rails.** `bin/rails app:update` walks the user through changed
  files interactively; `config.load_defaults` in the application
  records which version's defaults the application lives under, and
  a generated `new_framework_defaults_X_Y.rb` lets new defaults be
  switched on one by one before the recorded number is raised.
  Advice: "slowly, one minor version at a time, in order to make
  good use of the deprecation warnings" [V-s].
- **Angular.** `ng update` runs migration schematics; an update must
  start "within one major version" of its target, so several majors
  are several ordered steps. Deprecated APIs stay "a minimum one
  major version"; each major is supported 24 months, half of it as
  LTS [V-s].
- **Django.** A feature deprecated in A.x keeps working with a
  warning and is removed two feature releases later; designated LTS
  releases get about three years of fixes; "feature releases every
  eight months or so" [V-s]. Schema migrations are files with
  declared dependencies, and two developers' conflicting migrations
  are detected and offered a merge [V-s].
- **Database schema migration (Flyway).** The schema history table
  is "a record of changes performed against the schema", with
  checksums; pending steps are those in the project and not in the
  table; an edited, already-applied migration is an error [V-s]. The
  recorded level lives with the data, the steps with the tool, and
  the steps are ordered and forward. Consensus across the genre [H,
  from general knowledge of Alembic and Rails as well].
- **Kubernetes.** Every object names its `apiVersion`. The
  deprecation policy: an element is removed only by a new API
  version (rule 1); objects "must be able to round-trip between API
  versions in a given release without information loss" (rule 2);
  and the preferred and storage version "may not advance until after
  a release supporting both the new version and previous version has
  been made" (rule 4b) - first everyone can read the new shape, only
  then does anyone write it. Stored objects in a stale version are
  rewritten by a storage version migration [V-s].
- **Terraform.** The 1.x promise is upgrade "requiring no changes to
  your configuration, no extra commands"; later releases may
  introduce "new storage formats for Terraform state snapshots", and
  downgrade is not promised [V-s]. Early versions refused any state
  written by a newer Terraform; this was relaxed once the state
  format itself was versioned and stable, so that only a new format
  version blocks an older tool [S, vendor support articles].
- **Docker Compose.** The counter-example: the top-level `version`
  is "only informative" and obsolete; "Compose always uses the most
  recent schema to validate the Compose file, regardless of the
  version field", and warns on unknown fields [V-s]. A version field
  can be dropped where the format evolves only by addition.
- **Static site generators.** Hugo deprecates in three logged phases
  - INFO for 3 minor releases, WARN for another 12, then ERROR and a
  failed build - and a theme may declare the Hugo versions it
  supports, with a warning on mismatch [V-s]. Docusaurus v3 broke
  existing content (MDX) and shipped a checker to run on the old
  version first ("preparing your site for Docusaurus v3 ...
  incrementally, under Docusaurus v2"), no codemod [V-s]. MkDocs
  2.0 is reported as a rewrite with no plugin compatibility and no
  migration path, answered by the main theme's authors with a new
  generator that reads the old configuration [S, from the party in
  the dispute; contested].
- **Note tools.** Logseq split into a file-based and a database
  product; a Markdown graph is imported one way into the database
  form, the two run side by side as separate graphs, and the old
  line is in maintenance mode [S].
- **AI-run migration.** Migration guides are beginning to ship as
  agent skills beside a codemod: the mechanical part scripted, the
  judgement left to an agent following the guide (a migration skill
  for one SDK's v6 to v7; a codemod plus a guide for another's v1 to
  v2) [S]. Emerging; no source found measures how reliably an agent
  migrates prose documents by a guide.

### 4. Versioning policy

- **Semantic versioning** rests on a declared public API; a major is
  an incompatible change of it, and 0.y.z promises nothing [V-s].
  For a framework made of instructions and document conventions
  nothing found defines "breaking". A working definition [H]: the
  public API is what a project holds on disk and what a user types -
  the shapes of the files, the field names and state words, where a
  file lives, the meaning of a recorded word, the names and
  arguments of commands. A change of any of these is breaking for an
  existing project; a rewording of an instruction is not, though it
  may change behaviour, which no version number can express (the
  draft brief's "Testing how the engine behaves" is that other
  question).
- **Calendar versioning** is recommended for a "large or
  constantly-changing scope" where a semantic number says little
  [V-s]. It answers "how old is my engine", not "does my project
  fit".
- **Long-term-support lines** (Node, Django, Angular) mean a second
  branch that receives fixes for years [V-s]. Every example found is
  maintained by a team; a delayed pointer (Claude Code's `stable`,
  BMAD's `stable` against `next`) gives a calmer line with no
  backporting [H].
- **Deprecation windows** are consensus wherever content outlives
  releases: warn first, remove at a stated later release (Django two
  feature releases, Angular one major, Hugo fifteen minors, BMAD
  until the next major) [V-s].

### 5. Across all of them

| Question | Consensus | Emerging | Contested |
|---|---|---|---|
| Where the version is recorded | in the content, as a format version separate from the tool's, where the tool parses the content | manifests and channels for the engine files of AI frameworks | whether to record at all where the format only grows (Compose) |
| Who detects a mismatch | the tool, at load; a newer format stops or warns an older tool | - | stop (Go) or warn (Hugo, Compose) |
| How migration runs | ordered, forward, one level at a time; the level raised by the step | an agent following a shipped guide | fully automatic against guided by hand |
| Coexistence | a bounded window with warnings | shims that forward an old name | indefinite coexistence (Rust) - its cost is carrying the past for ever |
| What fails | the user's direct edits of managed files; non-interactive runs skipping steps; stale leftovers after a rename | - | - |

One ordering rule recurs and bears directly on the prompting case
[H, from Kubernetes rule 4b and Go's backported refusal]: **the
ability to recognise a new format must be released, and reach every
reader, before anything writes that format.** An older engine cannot
refuse what it was never taught to look for.

## Options with trade-offs

**A. As today: no version in projects, a check after the upgrade
(POS.0940).** Nothing to maintain, and right for one person with one
engine. With two engines over one project the check becomes the
problem: each measures against its own conventions and each reports
the other's shape (finding 5 of the sibling note). POS.0820's
"valid under the conventions it was written to" cannot be evaluated,
because nothing says which conventions those were.

**B. A format level recorded in each project.** One number in the
project (the ledger header is where its state already lives),
raised only when the shape of project files changes - not at every
engine release. The engine states the level it writes; a reader
compares before a write. Makes a mismatch detectable in both
directions and makes POS.0820 checkable. Costs: reverses "a project
records no engine version" (though it records a format, not an
engine); each shape change must be noticed and numbered by the
maintainer; an engine older than the introduction of the comparison
stays blind, so the comparison must ship one release before the
first bump. Whether an older engine stops or warns is a choice;
stopping is the only form that prevents the case, and in a framework
of instructions a stop that must hold is better placed in a script
or hook than in prose [H].

**C. A stable line users follow while development runs ahead.**
Today `main` is called the released line but receives every `/save`
between releases, so whoever pulls `main` pulls work in progress
(sibling note, finding 5). Two shapes: a pointer (a tag or branch
that moves only at a release, which the pull of a user follows) or
development moved to a branch with `main` moving only at a release.
Either is cheap for a single maintainer; neither involves
backporting. Cost: users lag by one release cycle, and a fix they
need means a release. Alone it removes the prompting case only if
both authors follow the same line and upgrade together.

**D. Migrations as ordered steps with a recorded level.** Each
raise of the format level ships its migration: what moves where,
and how to verify it. Scripted (deterministic, costly to write for
prose documents, the forge has declined a migration tool knowingly),
or AI-run from a written step (matches how the forge already
migrates, and the emerging practice of finding 3), in either case
applied in order and closed by raising the recorded level in the
same write. Costs: a step must be written at the moment of the
change, which the `Action` field of a history record already asks
for (POS.0730) - the new part is tying it to a level and keeping it
after the release notes fold; an AI-run step is stochastic and wants
a check after it.

**E. Tolerant readers of old structures.** The checks and commands
accept a project at an older level for a stated window, reporting
one fact ("this project is N levels behind") instead of a finding
per old shape. Removes the back-and-forth migration between two
engines' checks. Costs: the engine carries its past, and in an
instruction framework every tolerated old shape is more text in the
context and more room for ambiguity; writing in two shapes at once
is the expensive half and nothing surveyed does it except compilers.
Reading tolerance within a short window is the affordable form.

## Relevance to this project

For the draft brief `next-gen`, "Upgrade and compatibility", which
asks for three things: a stable line, a statement of what does not
change between versions, and a way to bring a project to a new
structure.

**Recommendation [H].** B, C and D together in their light forms; E
only as far as B makes it free; A stays the behaviour for a project
no second engine touches.

1. **A stable pointer (C).** Collaborators and third parties pull
   releases, not saves; the maintainer's daily line runs ahead. This
   is the field's cheapest and most common device, and it restores
   the meaning POS.0550 already gives `main`.
2. **A format level in the project, separate from the engine's
   version (B).** Raised only when what a project holds changes
   shape or meaning; the list in finding 5 of the sibling note is
   what would have raised it so far. The engine compares before it
   writes into a project and stops when the project is ahead of it.
   Ship the comparison before the first raise.
3. **"What does not change" is the same list stated once.** The
   statement the brief asks for falls out of defining what raises
   the level: file shapes, field and state words, locations, the
   meaning of recorded words, command names. Everything else may
   change at any release without a migration.
4. **Migration as kept, ordered steps, run by Claude on the user's
   word (D).** One step per level, derived from the `Action` text
   written with the change, applied by one person at a known moment
   as one commit, verified by a check, closed by raising the level.
   For a shared project the order is Kubernetes' rule: all authors
   take the release that understands the new level first, then one
   of them migrates.
5. **Checks measure a project against its recorded level (E, the
   free part).** A project behind the engine is reported as behind,
   once, consistent with POS.0820; no long-term-support line and no
   writing in old shapes.

**What would have prevented the prompting case.** Point 1 alone, had
both authors followed the released line and taken releases together.
Point 2 would have turned what remained into a stop with a plain
message at the first write, instead of documents in two structures
found afterwards. Neither needs a migration tool.

**Positions this would touch**, to be proposed through
`/forge intent` and never silently: POS.0940 (a project records no
engine version; the whole migration path), POS.0820 (gains a way to
be evaluated), POS.0730 (the `Action` lines gain a level), POS.0300
and POS.0550 (what `main` is between releases). A recorded level and
a new ledger-header field are new conventions and the principal's to
decide.

## What stays uncertain

- Every fetched page but three came through a summarising model;
  quotations should be re-read at the source before any is cited
  outward.
- The frameworks' issue trackers were read as lists of titles only;
  what users reported in the bodies was not read. BMAD's upgrade
  guide was read at a mirror.
- Findings tagged [S] (task-master, Agent OS v3, Logseq, MkDocs 2.0,
  Terraform's relaxed state check, the AI-run migration examples,
  Claude Code's deprecations) rest on search summaries.
- No source measures how reliably an agent migrates prose documents
  by a written guide; the forge's own migrations to date are the
  only evidence at hand and were not examined here.
- Whether an instruction-level comparison stops an older engine
  reliably, or needs a script or hook, was not tested.

## Sources

All fetched 2026-10-03.

Primary, raw text: code.claude.com/docs/en/setup;
code.claude.com/docs/en/plugins-reference (plugin manifest
reference); code.claude.com/docs/en/plugins/host-marketplace.

Primary, through the summarising fetch:
raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/CHANGELOG.md;
mintlify.wiki/bmad-code-org/BMAD-METHOD/guides/upgrade-to-v6
(mirror; docs.bmad-method.org/how-to/upgrade-to-v6/ redirected);
github.com/bmad-code-org/BMAD-METHOD/issues (search "upgrade v6
migration");
raw.githubusercontent.com/github/spec-kit/main/docs/upgrade.md;
github.com/github/spec-kit/issues (search "upgrade overwrite");
raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/migration-guide.md;
buildermethods.com/agent-os/updating;
raw.githubusercontent.com/obra/superpowers/main/RELEASE-NOTES.md;
kubernetes.io/docs/reference/using-api/deprecation-policy/;
kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/;
docs.docker.com/reference/compose-file/version-and-name/;
nbformat.readthedocs.io/en/latest/format_description.html;
doc.rust-lang.org/edition-guide/editions/index.html;
go.dev/doc/toolchain;
developer.hashicorp.com/terraform/language/v1-compatibility-promises;
docs.djangoproject.com/en/dev/internals/release-process/;
docs.djangoproject.com/en/5.2/topics/migrations/;
angular.dev/reference/releases;
guides.rubyonrails.org/upgrading_ruby_on_rails.html;
docusaurus.io/docs/migration/v3;
documentation.red-gate.com/fd/flyway-schema-history-table-273973417.html;
gohugo.io/troubleshooting/deprecation/;
gohugo.io/configuration/module/; semver.org; calver.org;
nodejs.org/en/about/previous-releases;
martinfowler.com/bliki/TolerantReader.html (2011-05-09).

Secondary, search summaries only: a mirror of task-master's
docs/migration-guide.md at glama.ai;
github.com/buildermethods/agent-os/discussions/310;
github.github.com/spec-kit/upgrade.html (older wording);
github.com/Fission-AI/OpenSpec/releases/tag/v1.0.0;
support.hashicorp.com articles 4409188433427 and 4413462840851;
logseq.io and discuss.logseq.com on the database version;
zensical.org/compatibility/configuration/ and a third-party article
on MkDocs 2.0; ai-sdk.dev/docs/migration-guides/migration-guide-7-0;
ts.sdk.modelcontextprotocol.io/v2/migration/; an issue mirror on the
deprecation of Claude Code's npm install at v2.1.15.

Not reached: developer.hashicorp.com/terraform/language/state/upgrading
(404); the BMAD upgrade guide at its repository path (404).
