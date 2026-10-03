---
project: forge
type: research
topic: where requirements written by different people meet in an external system of record, and how files and that system are kept in step
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (Several people on one project; Connection to the systems around)
status: immutable
---

# Where requirements meet outside git

## Question

Where and how do requirements written by different people in
docs-as-code or AI spec-driven workflows meet in an external system of
record (Jira, Confluence, Azure DevOps, GitHub Issues, Linear), and
how is the synchronisation between the files and that system done?

Epistemic tags, on every claim: [V] verified on a page fetched on
2026-10-03; [2] taken from a secondary source or from a search-result
summary, the page itself not fetched; [S] my own synthesis. A caution
on [V]: the pages were read through a fetch tool that summarises, so
quoted phrases are as that tool returned them and should be checked
at the URL before being quoted onward. Maturity is marked as
consensus, emerging or contested.

## Answer in one paragraph

In the field the text of a requirement almost never meets in the
tracker. Where several people write specs as files, their work meets
in git (branches, pull requests, a shared planning repository), and
the tracker receives a derived, one-way mirror of the finished
breakdown: epics, stories, tasks, each stamped with the file-side ID,
with only the status read back [V][S]. Every serious integration found
declares the files the source of truth and treats a hand edit in the
tracker as drift to be reported, not merged [V]. True two-way sync of
content exists only between trackers (Linear with Jira, the commercial
sync products), and its own vendors describe loops, conflicts, user
mapping and status mismatch as standing problems, and position it as a
transition aid [V]. The opposite school, the tracker or the wiki as
the home of the requirement text (the Atlassian line: Confluence page
or Jira work item as the spec, plugins that key requirements inside
Confluence), is real and established, but it is an alternative to
files, not a way to join them [V]. The official MCP servers of
Atlassian, GitHub, Microsoft and Linear now let an agent read and
write almost everything in those systems, so the technical barrier to
publishing and to pulling inputs is gone; what remains is permission,
authentication effort and the risk of untrusted content steering the
agent [V].

## Key findings

### 1. How the AI spec-driven frameworks hand over to trackers

- **Spec Kit core: one command, one direction, create only** [V].
  `/speckit.taskstoissues` reads `tasks.md` and creates one GitHub
  issue per task through the GitHub MCP server's `issue_write`, titled
  `T001: <description>`; it lists existing issues to skip tasks
  already covered; it writes nothing back into `tasks.md`, updates no
  existing issue and reads no status. It refuses to create issues in a
  repository that does not match the git remote. Identity is the task
  ID carried in the issue title. Source:
  github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md.
- **Spec Kit community catalogue: eight tracker or wiki extensions**
  [V] (raw catalogue file, extensions/catalog.community.json): three
  for Jira (`jira` 2.1.0, 2026-03-05; `jira-sync` 0.4.0, 2026-06-24;
  `jira-mirror` 0.24.0, 2026-08-31), one for Azure DevOps (1.0.0,
  2026-03-03), three for GitHub Issues (two of them the other way:
  generate specs from existing issues), one for Confluence. None is
  maintained by the Spec Kit team [S, from the repository owners].
- **The two engineered Jira bridges both chose one-way** [V].
  `spec-kit-jira-sync`: "The filesystem is the single source of truth.
  Jira is a unidirectional, read-only mirror." Epic per repository,
  story per spec, subtask per phase; identity by labels
  (`speckit-spec:NNN`); it reads Jira only to detect drift (a teammate
  moved a status, edited a subtask), warns by name and asks before
  overwriting, or aborts with `--on-drift=abort`; if Jira cannot be
  read reliably it writes nothing ("fail-closed").
  `spec-kit-jira-mirror`: despite the two-way arrow in its
  description, it mirrors `spec.md`, `plan.md`, `tasks.md` into Jira;
  identity is a durable identifier in an HTML comment line in both the
  document and the ticket; it reads summary and description, "never
  its comments"; when routing resolves to another project than the one
  recorded it refuses with zero writes. Sources:
  github.com/ashbrener/spec-kit-jira-sync,
  github.com/Fyloss/spec-kit-jira-mirror.
- **BMAD: nothing in the core, community bridges** [V]. The official
  documentation (docs.bmad-method.org) names no tracker; stories and
  sprint status live in files (`sprint-status.yaml`) [V for the
  absence, 2 for the file's role]. A community module mirrors
  `sprint-status.yaml` to GitLab or GitHub issues after the workflow
  runs [V, claudepluginhub.com/plugins/jrevillard-bmad-issue-tracking].
  A community tool `bmad-atlassian-sync` pushes stories and epics to
  Jira and publishes pages to Confluence one-way; it writes
  `jira_key`, `confluence_page_id`, `last_synced_at` and a `sync_hash`
  into the Markdown front-matter, pulls back status and assignee only,
  and resolves status conflicts by a never-downgrade rule. It has no
  stars and 23 commits: evidence of a pattern, not of adoption [V,
  github.com/3d-stories/bmad-atlassian-sync].
- **OpenSpec: no tracker in the core; people meet in a git
  repository** [V]. The README names no tracker integration. Its
  answer to several people and several repositories is Stores (beta):
  "A store is just a git repo. You commit, push, pull, and review it
  yourself"; "Plans get branches, pull requests, and review for free";
  "OpenSpec never clones, syncs, or pushes anything on its own."
  Sources: github.com/Fission-AI/OpenSpec and
  docs/stores-beta/user-guide.md. A methodology author's skill
  (2026-05-29) links OpenSpec to Linear with an explicit split:
  Linear owns the business context and stakeholder-facing status, the
  repository owns design and implementation; the issue's state
  follows the lifecycle, and at archive the final specs are mirrored
  into Linear documents [V,
  intent-driven.dev/blog/2026/05/29/linear-openspec-skill-based-sdd/].
- **Kiro: MCP only, mostly inward** [V]. The specs documentation names
  no tracker integration. Kiro's own blog shows trackers reached
  through MCP servers the user configures, with the worked example
  reading issues in and turning them into specs. Sources:
  kiro.dev/docs/specs/,
  kiro.dev/blog/unlock-your-development-productivity-with-kiro-and-mcp/.
- **claude-task-master: no tracker integration in the README**; a
  hosted companion product for teams is referenced, details not
  stated there [V, github.com/eyaltoledano/claude-task-master].
- **Microsoft's Spec Kit training unit on teams** (dated 2026-01-28,
  updated 2026-07-03) [V]: collaboration is by feature branch per
  specification and pull request; one named owner per specification;
  task assignment "in tasks.md or your project management system"; a
  central specification repository is offered for stakeholders outside
  the code, with the warning that "it adds overhead for keeping
  specifications synchronized". No tracker sync is described. Source:
  learn.microsoft.com/en-us/training/modules/spec-driven-development-github-spec-kit-enterprise-developers/10-scale-spec-driven-development-team-collaboration.

Status: consensus among these frameworks that files in git are the
source of truth and that a tracker, if any, is a downstream mirror of
the work breakdown [S]. Emerging: drift-aware reconcile engines with
stable identity, all from 2026 and all community work [V for dates].

### 2. Requirements-as-code tools

- **Sphinx-Needs** [V]: the `needservice` directive imports items
  from an external service (GitHub issues documented) at build time,
  one way, under an `id_prefix`. The vendor's commercial connector
  (ubConnect, licence required) has `from-jira` (import to
  `needs.json`), `to-jira` (create issues from needs) and
  `refresh-status`. Its own words: "content flows one way: need
  content is written into Jira, and only the issue status is read
  back." Identity: `jira_key` on the need, a label
  `ubconnect-need:<need id>` on the issue, a state file with the
  mapping, and a reconcile that rebuilds a lost state file by querying
  Jira. Updating issues already created when a need changes is stated
  as out of scope. Sources:
  sphinx-needs.readthedocs.io/en/stable/directives/needservice.html,
  ubconnect.useblocks.com/stable/features/jira.html.
- **StrictDoc** [V]: exports HTML, RST, ReqIF, PDF, JSON, Excel;
  imports ReqIF and Excel; no tracker integration documented. Two
  identities per item: a human UID and an auto-generated machine
  identifier (MID) that survives a change of UID or title. Source:
  strictdoc.readthedocs.io (user guide).
- **Doorstop** [V]: one YAML file per item in git, publish and export
  to files; no tracker integration on the documentation front page.
  Source: doorstop.readthedocs.io.
- The exchange format of the regulated world is ReqIF, a file handed
  over, and Jira-side plugins import it creating one issue per
  requirement with a reference to the original ID [2, search summary
  of a vendor's documentation].

Status: consensus in this family that the tracker is not where
requirement text is authored; the boundary is crossed by a published
file or by a one-way create with status read-back [S].

### 3. The tracker or wiki as the home of requirements

- **Atlassian's own guidance** (knowledge-base article dated
  2025-09-26) [V]: requirements are gathered on a Confluence page,
  issues are created from it, and the two are linked; for more it
  names three plugins (R4J, RMsis, Requirement Yogi). Source:
  support.atlassian.com/jira/kb/using-jira-for-requirements-management/.
- **Requirement Yogi** [V]: the requirement text stays in Confluence
  under a requirement key; Jira stores a link to the key, not the
  text; links remember which baseline of the requirements they point
  to. Source: docs.requirementyogi.com/data-center/jira-links.
- **Atlassian's 2026 guide on spec-driven development** [V, page
  truncated on fetch]: "In Jira, that spec lives in the work item you
  already run on"; a work item holds the full spec of a task or one
  slice of a larger one. It does not address spec files in git.
  Source:
  atlassian.com/software/jira/guides/agentic-engineering/spec-driven-development-jira.

Status: contested [S]. The framework authors put the spec in the
repository, the tracker vendor puts it in the work item. Both are
coherent; they differ in who the author is (people in a web editor
against people with an agent in files) and neither side describes a
maintained merge of the two.

### 4. One-way publish against two-way sync

- **Docs-as-code publishing to a wiki is one-way everywhere found**.
  `mark` (Markdown to Confluence): target page named by header
  comments or front-matter in the file; "Mark treats your repository
  as the source of truth"; a hand edit in Confluence is overwritten at
  the next run [V, github.com/kovetskiy/mark]. Another publisher
  states that pages in the target space must not be changed by hand or
  the tool may be unable to synchronise [2, search summary of the
  package page, which failed to load].
- **Two-way sync, as described by those who sell it** [V]. A sync
  vendor's guide (2024-04-11, updated 2026-07-07) names: sync loops
  (each side's update triggers the other, indefinitely, unless changes
  are marked as sync-originated); simultaneous edits, called
  "inevitable" in a bidirectional setup, with no built-in resolution,
  rules written per field; user identity mapping, "one of the most
  consistently cited pain points"; wrong field mapping. It notes that
  fields can be given different directions. Source:
  exalate.com/blog/jira-issue-sync/.
- **Linear's Jira sync** [V]: fields sync both ways, but a Jira status
  with no Linear counterpart does not update; a Linear change that
  violates a Jira constraint updates Linear only; deletion does not
  propagate; assignee depends on each user linking accounts; it is
  positioned for running a pilot or a gradual transition. Source:
  linear.app/docs/jira.
- Further failure modes from vendor and community posts [2]: fields
  dropping out silently when missing from an edit screen, rich text
  that one side cannot represent, rate limits burned by loops.

Status: consensus [S]. One-way publish with the repository as source
is the settled pattern for documents. Two-way sync is a commercial
product category for ticket fields between trackers, with known
failure modes; no source found does two-way sync of long structured
requirement text between Markdown and a tracker. The stable middle
form is per-field direction: content goes out, status comes back.

### 5. Identity across the boundary

Four techniques recur [V for each instance above, S for the list]:

1. The file-side ID travels into the tracker in a visible, searchable
   place: issue title prefix (Spec Kit core), label (jira-sync,
   ubConnect), custom field or hidden comment line (jira-mirror).
2. The tracker's key travels back into the file's metadata
   (`jira_key`, `confluence_page_id` in front-matter) or into a state
   file beside it (ubConnect).
3. A content hash or last-synced stamp on the file side detects what
   changed since the last publish (`sync_hash`).
4. Reconcile before write: query the tracker by the file-side ID
   first, so that a lost mapping never creates duplicates.

A stable ID that is never renumbered is the precondition of all four
[S]. StrictDoc's second, machine identity exists precisely because
human IDs do get renamed [V].

### 6. What the official MCP servers allow today

- **Atlassian (Rovo MCP Server)** [V]: generally available, cloud
  hosted, endpoint `https://mcp.atlassian.com/v2/mcp`; the legacy SSE
  endpoint unsupported after 2026-06-30. OAuth 2.1 or, if the admin
  enables it, API tokens for headless use. Claude Code is among the
  listed clients. Cloud only is what the pages show; Data Center is
  not mentioned. Jira: read issue, comments, changelog, links,
  boards, sprints; JQL search; create and edit issue, transition,
  comment, create issue link and remote link, upload attachment,
  convert hierarchy. Confluence: read page, versions and a diff of
  versions, comments, attachments, export; CQL search; create and
  update content, comments, labels, move, archive, restore a version.
  Delete and manage tool groups are off until an admin enables them;
  no Confluence delete is listed. Admins grant by permission group
  (read, write, search, delete, manage); every action runs with the
  user's own permissions; audit log available. Usage limits are by
  plan, numbers not on the pages fetched. Sources:
  support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/,
  github.com/atlassian/atlassian-mcp-server,
  support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/.
- **GitHub** [V]: generally available; remote server hosted by
  GitHub with OAuth, or local (required for Enterprise Server).
  Issues: create and update (`issue_write`), read with sub-issues and
  parents, sub-issue hierarchy, comments, issue types, custom fields,
  labels, search; Projects toolset; a `--read-only` flag. Source:
  github.com/github/github-mcp-server.
- **Azure DevOps** [V]: the remote server is in preview (public
  preview since 2026-03-17 [2]); page dated 2026-09-21. Endpoint
  `https://mcp.dev.azure.com/{organization}`; Microsoft Entra ID
  only, organisation must be Entra-backed. Claude Code is supported
  only with a custom Entra app registration and admin consent; Claude
  Desktop cannot use the remote server and needs the local one. Work
  items: get, batch, revisions, comments, saved queries, backlogs,
  search; create, update, batch update, add child, comment, link and
  unlink. Wiki: list, get page, search, create or update page.
  `X-MCP-Readonly` header and toolset filter. The remote page covers
  Azure DevOps Services only; the local server is where new work no
  longer goes. Sources:
  learn.microsoft.com/azure/devops/mcp-server/remote-mcp-server,
  github.com/microsoft/azure-devops-mcp.
- **Linear** [V]: hosted server at `https://mcp.linear.app/mcp`, with
  a read-only endpoint beside it; OAuth 2.1, API keys; tools to find,
  create and update issues, projects and comments. Source:
  linear.app/docs/mcp.

Status: consensus that every major tracker now ships a vendor MCP
server with write tools and a read-only switch; emerging and uneven
in authentication effort (Azure DevOps with Claude Code needs tenant
administration) [S].

**The limit that matters is not capability but trust** [V][2]. A
research note of 2026-08-14 describes two prompt-injection paths
against Atlassian's assistant inside Jira and Confluence (not the MCP
server), one fixed, one reported unresolved at publication, and
advises treating any ingested content as untrusted input [V,
labs.cloudsecurityalliance.org/research/csa-research-note-atlassian-rovo-prompt-injection-20260814-c/].
A 2025 demonstration against the Atlassian MCP path used a support
ticket written by an outsider to steer an internal user's agent [2,
search summary of reports on that research]. Atlassian's own page
says to use least privilege and review high-impact changes [V]. The
risk grows with three things together: private data, content written
by others, and a way to send data out [2].

### 7. Inputs flowing the other way

- Frameworks pull tracker items in on demand through MCP and turn
  them into a spec (Kiro's example; two Spec Kit extensions; the
  Linear skill, where a backlog issue becomes the business brief)
  [V]. The item is read at a moment in time; none of these keeps the
  spec following later edits of the ticket [S].
- Sphinx-Needs imports at build time under a prefix, so imported
  items are visibly foreign and never edited locally [V].
- Batch export of a wiki space to Markdown for an AI's use is an
  established tool category [2]; its stated weakness is staleness and
  its stated strength is a clean, reviewable, local copy. Live
  connectors are fresh but leave no record of what was read [2][S].
- The Atlassian server exposes page versions and a version diff, and
  the Jira changelog [V], so a pull can be pinned to a version and a
  later change detected: the raw material for a snapshot with
  provenance [S].

Status: emerging [S]. No source found states a settled practice for
keeping pulled inputs as dated, cited snapshots; the frameworks treat
a pulled ticket as prompt context, not as a registered source.

## Options with trade-offs

**A. Git stays the only meeting point.** Several people meet in the
project repository (or a shared planning repository, as OpenSpec
Stores), by branch and review. For: it is what every framework
surveyed does; no second truth; identity is already stable. Against:
everyone who contributes needs git and the tool; the collision
problem of the brief (IDs, history, ledger rewritten by every change)
stays to be solved inside the files; people outside the tool see
nothing unless something is published.

**B. One-way publish of a finished artefact into a tracker or wiki.**
At a release, items become issues or a page; each carries the item ID
and the version; the tracker key is recorded on the file side; only
status, if anything, is read back; a hand edit on the other side is
reported as drift. For: the settled pattern, with working examples of
identity and reconcile; the official MCP servers suffice, no sync
product needed; it answers "outputs are to go into the company's
systems" without a second source of truth. Against: comments and
edits made in the tracker do not return by themselves (they come back
as feedback through the principal, or as an ingested source); a
re-publish after a new version needs a rule for issues already in
work; it does nothing for two authors colliding upstream.

**C. The tracker as the place where separate people's artefacts
meet.** Each person works a project of his own and publishes; the
combined view (the whole BRD, the hierarchy across authors) exists
only in the tracker. For: no shared files, so no file collisions;
matches the estimate that analysts mostly work each on his own topic;
the recipients already live in the tracker. Against: no surveyed
framework does this, so there is no precedent to copy; cross-author
consistency (overlaps, contradictions, shared constraints, ID
collisions between projects) is checked nowhere, since the forge's
reviewers read files; the moment the combined content is edited in
the tracker, the tracker has become the source of truth and the
option has turned into two-way sync with its known failure modes.

**D. Live connectors for inputs.** Tickets, pages and meeting notes
are read through MCP instead of ingest by hand. Two forms: read and
use directly, or read and store as a snapshot with the system's ID,
version and date, then treat it as any source. For: removes the
island; the snapshot form keeps provenance and immutability, and the
version diff tells when a source has moved. Against: the direct form
leaves no record and breaks citation; content written by others can
carry instructions to the agent; authentication is an administrative
act in some systems; a cloud-only server does not reach an on-premise
installation.

## Relevance to this project

The brief asks at which level several people meet: git and the same
files, or lower down in another system. The field's answer is plain
on one half and silent on the other. Plain: requirement text written
as files meets in git, and trackers receive a derived copy; nobody
surveyed merges separately written requirement text inside a tracker.
Silent: none of the surveyed frameworks has the forge's particular
difficulty, a change that rewrites history, ledger and intent
together, so their "use branches and pull requests" does not show
that A is comfortable here; that is a question for the neighbouring
research on several people on one project, not this note.

Recommendation, as findings for the brief and not a design:

1. Treat the two sections as two separate questions. "Where do
   people meet" and "how does the forge connect to the systems
   around" have different answers in the field; the tracker is an
   answer to the second and not to the first [S].
2. For outputs, prefer B: one-way publish of a released artefact,
   item IDs carried across, tracker keys recorded on the file side,
   status at most read back, drift reported. The forge's stable
   `PREFIX.NNNN` IDs and its publish-on-command step are already the
   two preconditions the working examples rely on [S]. In the forge's
   vocabulary such an output behaves like a render or a published
   file: never a source of truth.
3. Do not adopt C as the meeting point for requirement text. If
   separate people's BRDs are to be seen together in a tracker, that
   is B done by several projects into one tracker project, with the
   cross-author consistency still to be checked on the file side;
   where it would be checked is an open question to put to the
   principal, not something the field answers.
4. Rule out two-way sync of content as a stated non-goal; per-field
   direction (content out, status back) is the furthest the evidence
   supports.
5. For inputs, prefer the snapshot form of D: a connector as a
   quicker door to the existing ingest, storing what was read with
   the remote ID, version and date, read-only by configuration. This
   also bears on THR.0510 (live reference material by nightly
   export): the field offers both batch export and live read, and
   the snapshot form is the one that keeps the forge's rule that a
   source is immutable and cited.
6. Which systems, cloud or on-premise, and who may grant an agent
   write access are instance facts that decide feasibility more than
   anything above; they belong to the brief's "Operation in a
   company" and need the principal's answer before any of this is
   designed.

## What stays uncertain

- Adoption of the community bridges is unknown; several are weeks or
  months old, one has no users visible. They show what careful
  authors chose, not what works at scale.
- Usage limits of the Atlassian server by plan, and whether a Data
  Center installation is reachable, were not established.
- The accepted content format for Confluence writes (Markdown
  against the native format) and its fidelity for tables were not
  verified.
- Kiro's and task-master's hosted team products may contain tracker
  features not shown on the pages fetched.
- Practice inside companies (as opposed to published tools) is not
  visible from the web; the "contested" finding of section 3 may be
  settled differently in regulated industries.

## Sources

All fetched 2026-10-03 unless marked [2] above.

- github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md
- raw.githubusercontent.com/github/spec-kit/main/extensions/catalog.community.json
- github.com/ashbrener/spec-kit-jira-sync
- github.com/Fyloss/spec-kit-jira-mirror
- learn.microsoft.com/en-us/training/modules/spec-driven-development-github-spec-kit-enterprise-developers/10-scale-spec-driven-development-team-collaboration (2026-01-28, updated 2026-07-03)
- docs.bmad-method.org
- github.com/3d-stories/bmad-atlassian-sync; claudepluginhub.com/marketplaces/3d-stories-atlassian-sync
- claudepluginhub.com/plugins/jrevillard-bmad-issue-tracking
- github.com/Fission-AI/OpenSpec; github.com/Fission-AI/OpenSpec/blob/main/docs/stores-beta/user-guide.md
- intent-driven.dev/blog/2026/05/29/linear-openspec-skill-based-sdd/ (2026-05-29)
- kiro.dev/docs/specs/; kiro.dev/blog/unlock-your-development-productivity-with-kiro-and-mcp/
- github.com/eyaltoledano/claude-task-master
- sphinx-needs.readthedocs.io/en/stable/directives/needservice.html
- ubconnect.useblocks.com/stable/features/jira.html
- strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide.html
- doorstop.readthedocs.io/en/latest/
- support.atlassian.com/jira/kb/using-jira-for-requirements-management/ (2025-09-26)
- docs.requirementyogi.com/data-center/jira-links
- atlassian.com/software/jira/guides/agentic-engineering/spec-driven-development-jira
- github.com/kovetskiy/mark
- exalate.com/blog/jira-issue-sync/ (2024-04-11, updated 2026-07-07; vendor)
- linear.app/docs/jira; linear.app/docs/mcp
- support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/
- support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/
- github.com/atlassian/atlassian-mcp-server
- github.com/github/github-mcp-server
- learn.microsoft.com/azure/devops/mcp-server/remote-mcp-server (2026-09-21); github.com/microsoft/azure-devops-mcp
- labs.cloudsecurityalliance.org/research/csa-research-note-atlassian-rovo-prompt-injection-20260814-c/ (2026-08-14)

Not fetched, cited as [2] from search summaries: reports of the 2025
demonstration against the Atlassian MCP path; the announcement of the
Azure DevOps remote server's public preview; the package page of a
second Markdown-to-Confluence publisher (failed to load); vendor and
community posts on further sync failure modes; tools for batch export
of a wiki to Markdown; a Jira plugin's ReqIF import; a community
thread on what breaks syncs (page returned its title only).
