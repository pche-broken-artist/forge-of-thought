---
project: forge
type: research
topic: what operating Claude Code for many users in a company involves in administration, data and security, and cost, and what that asks of a framework distributed on top of it
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1, section "Operation in a company"
status: immutable
---

# Operating Claude Code for many users in a company

## Question

What does operating Claude Code for many users in a company involve
today, in administration, data and security, and cost, and what does
that ask of a framework distributed on top of it?

Left out on purpose: the threshold of entry for a non-developer
(installation, first run, surfaces other than the terminal), which is
a sibling research.

How to read the marks. Every finding carries one of four marks:
**[verified]** read at a source fetched on 2026-10-03 (the URL is
given); **[verified, summarised]** the page was fetched on 2026-10-03
but the fetch tool returned a summary made by a small model, so
wording and figures are as that summary relayed them and should be
re-read at the page before they are quoted onward; **[vendor claim]**
the vendor's own statement about itself, verified only as being
stated; **[synthesis]** this note's own reasoning, found stated
nowhere. No secondary sources (press, blogs) were used. The Claude
Code documentation pages carry no publication date; they are dated
here by the fetch and by the client version numbers they cite (up to
v2.1.285). Prices, limits, setting names and plan features change
fast: every figure below is a figure of 2026-10-03.

Pages read in full text (the fetch returned the page's own Markdown):
costs, data-usage, permissions, permission-modes, admin-setup,
managed-settings, server-managed-settings, zero-data-retention,
legal-and-compliance, security, third-party-integrations,
champion-kit, plugins/org, analytics, and the platform page on data
residency. Pages read through a summary: model-config, sub-agents,
monitoring-usage, the two support articles, the pricing page, the
Enterprise administrator guide, and the four GitHub repositories.
The Anthropic Trust Center (https://trust.anthropic.com) could not be
read by the fetch (script-rendered), so nothing is cited from it
directly.

## Key findings

### 1. Plans and access

Sources: https://code.claude.com/docs/en/admin-setup ;
https://code.claude.com/docs/en/third-party-integrations ;
https://code.claude.com/docs/en/costs ; https://claude.com/pricing ;
https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan ;
https://academy.claude.com/tutorials/claude-enterprise-administrator-guide

- [verified] A company reaches Claude Code through one of five kinds
  of provider, and the choice "affects billing, authentication, which
  compliance posture you inherit, and which Claude Code features your
  developers can use": Claude for Teams or Enterprise (per-seat
  subscription, "the default recommendation"), the Claude Console
  (API, pay as you go), Amazon Bedrock, Google Cloud's Agent Platform
  (formerly Vertex AI), Microsoft Foundry; a sixth, Claude Platform
  on AWS, is listed in the comparison table. (admin-setup,
  third-party-integrations)
- [verified] Individual consumer plans (Pro, Max) also include Claude
  Code but have no organisation to manage: no central policy from an
  admin console, no organisation analytics. (costs)
- [verified] How usage is counted differs by route. On Teams and
  seat-based Enterprise plans "each member's Claude Code usage draws
  from a per-seat allowance that resets on a rolling five-hour window
  and a weekly window", shared with Claude chat and Cowork, its size
  set by the seat tier (Standard or Premium); usage inside the
  allowance "isn't metered in dollars". Past the allowance a company
  may turn on usage credits with spend limits at organisation, group
  or member level. On the Console and on cloud providers usage is
  billed per token to the organisation. (costs)
- [verified, summarised] Prices on 2026-10-03 as the pricing page's
  summary gave them: Pro 17 USD a month billed annually or 20
  monthly; Max "from 100 USD" a month (5x and 20x tiers; the 20x
  price was not relayed and is not verified here); Team Standard
  seat 20 USD a month annually or 25 monthly; Team Premium seat 100
  annually or 125 monthly, "5x more usage than standard seats";
  Enterprise "seat price + usage at API rates", 20 USD per seat per
  month billed annually, with SSO, SCIM, audit logs, compliance API,
  a HIPAA-ready offering and role-based access. The exact size of a
  seat allowance in tokens or messages is not published on any page
  read. (pricing)
- [verified, summarised] Enterprise comes in two billing shapes:
  newer plans are usage-based with no per-seat limit ("billing
  follows consumption at API rates"); older ones are seat-based with
  Chat + Claude Code or Premium seats. Claude Code is included with
  every Team seat. (support article 11845131)
- [verified] Features differ by route: cloud sessions, routines, Code
  Review, Remote Control and the Chrome extension "aren't available
  through Console API keys or cloud-provider credentials alone".
  (admin-setup)
- [verified] Model defaults and availability are not uniform. Cloud
  providers resolve model aliases to a built-in default "which can
  lag the newest release and may not yet be enabled in your account";
  the documentation recommends pinning versions there.
  (third-party-integrations)
- [verified, summarised] The default model is Opus 5.5 on Pro, Max,
  Team, Enterprise, the API, Bedrock, Agent Platform and Claude
  Platform on AWS, and Sonnet 4.5 on Microsoft Foundry. (model-config)
- [verified] Provisioning: "SSO, SCIM provisioning, and seat
  assignment are configured at the Claude account level", outside
  Claude Code. Teams includes SSO; Enterprise "adds domain capture,
  role-based permissions, and compliance API access". (admin-setup,
  third-party-integrations)
- [verified, summarised] The Enterprise administrator guide names
  SAML 2.0 and OIDC for SSO, SCIM (recommended) or just-in-time
  provisioning, and the roles Primary Owner, Owner and Member.
  (administrator guide, undated)
- [verified] A user whose seat lacks Claude Code access sees "You
  haven't been added to your organization yet". (admin-setup)

### 2. Central administration

Sources: https://code.claude.com/docs/en/admin-setup ;
https://code.claude.com/docs/en/managed-settings ;
https://code.claude.com/docs/en/server-managed-settings ;
https://code.claude.com/docs/en/permissions ;
https://code.claude.com/docs/en/permission-modes ;
https://code.claude.com/docs/en/plugins/org ;
https://code.claude.com/docs/en/model-config

- [verified] Organisation policy is "managed settings that take
  precedence over local developer configuration": no user, project,
  local or command-line value overrides them, apart from a few
  security-sensitive exceptions where a stricter lower value still
  counts. Array settings such as `permissions.allow` and
  `permissions.deny` merge across sources, "so developers can extend
  managed lists but not remove from them". (admin-setup,
  managed-settings)
- [verified] Four delivery mechanisms, in priority order:
  server-managed (the claude.ai admin console, or a self-hosted
  Claude apps gateway); an OS policy (macOS plist
  `com.anthropic.claudecode`, Windows registry
  `HKLM\SOFTWARE\Policies\ClaudeCode`); a file
  (`/Library/Application Support/ClaudeCode/managed-settings.json` on
  macOS, `/etc/claude-code/managed-settings.json` on Linux and WSL,
  `C:\Program Files\ClaudeCode\managed-settings.json` on Windows,
  each with an optional `managed-settings.d/` drop-in directory); and
  the Windows user registry `HKCU\SOFTWARE\Policies\ClaudeCode`,
  which is writable without elevation and is "a convenience default
  rather than an enforcement channel". (admin-setup,
  managed-settings)
- [verified] Server-managed settings need a Teams or Enterprise plan
  and the Owner or Primary Owner role; the client fetches them at
  startup and hourly. Their limits: they "apply uniformly to all
  users in the organization. Per-group configurations are not yet
  supported"; they are skipped when the user sets a third-party
  provider variable or a non-default `ANTHROPIC_BASE_URL`; and the
  page itself says they "operate as a client-side control, not a
  security boundary. On unmanaged devices, a user doesn't need admin
  or sudo access to bypass them". Settings that run shell commands,
  and any hook definition, need the user's approval in a security
  dialog before they apply. (server-managed-settings)
- [verified] What managed settings can enforce, by the keys the
  documentation names:
  - permission rules (`permissions.allow`, `permissions.deny`) and
    their lock `allowManagedPermissionRulesOnly`, which "makes
    managed settings the only settings source of permission rules";
  - permission modes: `permissions.defaultMode`,
    `permissions.disableBypassPermissionsMode`,
    `permissions.disableAutoMode`;
  - sandboxing: `sandbox.enabled`, `sandbox.network.allowedDomains`,
    with the locks `sandbox.network.allowManagedDomainsOnly` and
    `sandbox.filesystem.allowManagedReadPathsOnly`;
  - an organisation-wide CLAUDE.md "loaded in every session, can't be
    excluded" (a file at the managed policy path, or the `claudeMd`
    key);
  - MCP servers: `allowedMcpServers`, `deniedMcpServers`,
    `allowManagedMcpServersOnly`, `managedMcpServers`, or a deployed
    `managed-mcp.json`;
  - plugins and marketplaces: `strictKnownMarketplaces`,
    `blockedMarketplaces`, `disableSideloadFlags`,
    `disableCommandPluginSources`, `extraKnownMarketplaces`,
    `enabledPlugins`;
  - hooks: `allowManagedHooksOnly`, `allowedHttpHookUrls`;
  - `strictPluginOnlyCustomization`, which blocks "skills, agents,
    hooks, and MCP servers from user and project sources, so they can
    only come from plugins or managed settings";
  - login and provider: `forceLoginMethod`, `forceLoginOrgUUID`,
    `allowedProviders`;
  - models and effort: `availableModels`, `enforceAvailableModels`,
    `model`, `maxEffortLevel`; on Enterprise also server-side model
    restrictions, a default model and per-role effort limits from the
    admin console;
  - versions: `minimumVersion`, `requiredMinimumVersion`,
    `requiredMaximumVersion`;
  - telemetry: the managed `env` block with
    `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.
  (admin-setup, managed-settings)
- [verified] Auto mode. "With Claude Code v2.1.283 or later, auto
  mode is the built-in starting permission mode for interactive
  terminal and VS Code sessions"; it is available on all plans, on by
  default on Team and Enterprise, and an administrator turns it off
  with `permissions.disableAutoMode`. It needs a recent model (Opus
  4.6 or Sonnet 4.6 or later on the Anthropic API; a narrower list
  on Bedrock, Agent Platform and Foundry; Haiku is never supported).
  When auto mode is not available the session starts in Manual, where
  every edit and most shell commands ask. (permission-modes)
- [verified] Hooks and rules. "PreToolUse hook decisions don't bypass
  permission rules": a matching deny rule blocks and a matching ask
  rule still prompts whatever the hook returned, managed deny rules
  included. A managed deny cannot be overridden by any other level.
  (permissions)
- [verified] Distributing shared configuration, plugins or skills to
  every user has three documented roads:
  1. the repository itself: a project's `.claude/settings.json`,
     skills and agents travel with the clone, and
     `extraKnownMarketplaces` with `enabledPlugins` in it apply once
     the contributor has trusted the folder;
  2. a plugin from a marketplace (a git repository, a URL or a local
     path), which managed settings can register and force-enable on
     every machine (`extraKnownMarketplaces` plus `enabledPlugins`);
     a private git marketplace is cloned with the user's own git
     credentials, and a pre-built seed directory serves machines
     with no git-host access;
  3. the managed CLAUDE.md for instructions.
  Release channels (a stable and an early-access marketplace pointing
  at different refs of the same plugins) are a documented pattern,
  assigned per user group through endpoint-managed settings or a
  gateway policy, not through server-managed settings. (plugins/org)
- [verified] What managed settings cannot do, by the documentation's
  own list: per-user or per-group targeting from the admin console,
  restricting entries inside an allowed marketplace other than by
  naming each, hiding `/plugin`. (plugins/org)
- [synthesis] How this carries a framework like the forge. The forge
  today travels by road 1: a public repository whose `.claude/`
  directory holds its skills, agents, hooks and deny rules. Three
  managed locks break that road without any error the forge would
  see: under `strictPluginOnlyCustomization` its project-level
  skills, agents and hooks do not load at all; under
  `allowManagedHooksOnly` its per-prompt hook (and the gate hook of
  THR.0400, if built) is among the hooks an organisation may switch
  off (the exact effect list is on a page not read here); under
  `allowManagedPermissionRulesOnly` its own deny rules, which make
  the scripts the only door to git, are ignored. A company that
  locks customisation to plugins can run the forge only as a plugin
  from a marketplace it has allowed. Whether the forge can be
  packaged as a plugin while its projects stay separate repositories
  was not examined here.

### 3. Data and security

Sources: https://code.claude.com/docs/en/data-usage ;
https://code.claude.com/docs/en/zero-data-retention ;
https://code.claude.com/docs/en/security ;
https://code.claude.com/docs/en/legal-and-compliance ;
https://code.claude.com/docs/en/monitoring-usage ;
https://platform.claude.com/docs/en/manage-claude/data-residency

- [verified] What is sent. "Claude Code runs locally. To interact
  with the LLM, Claude Code sends data over the network. This data
  includes all user prompts and model outputs", encrypted in transit
  with TLS 1.2 or later. In practice that covers every file the
  model reads in a session. (data-usage)
- [verified] Training by plan. Consumer plans (Free, Pro, Max): "We
  will train new models using data from Free, Pro, and Max accounts
  when this setting is on (including when you use Claude Code from
  these accounts)". Commercial plans (Team, Enterprise, API, third
  party platforms): "Anthropic does not train generative models using
  code or prompts sent to Claude Code under commercial terms", unless
  the customer opts in. (data-usage)
- [verified] Retention. Consumer: five years when the user allows
  model improvement, thirty days when not. Commercial: thirty days
  standard; zero data retention "available to qualified accounts for
  Claude Code on Claude for Enterprise", "not included in the
  standard Enterprise plan", enabled per organisation by the account
  team. Transcripts sent with `/feedback`, `/bug` or `/share` are
  kept five years. Locally, the client stores "session transcripts
  locally in plaintext under `~/.claude/projects/` for 30 days by
  default" (`cleanupPeriodDays`). (data-usage)
- [verified] Zero data retention has a price in features: cloud
  sessions, Claude Tag, Artifacts, feedback submission and Remote
  Control are disabled at the backend; chat on claude.ai and Cowork
  are not covered; and the Fable models "require data retention by
  default", so a ZDR organisation may not be able to use them and
  the `best` alias then resolves to Opus. Flagged sessions may still
  be retained up to two years. (zero-data-retention)
- [verified] Data residency. On the first-party API inference can be
  pinned per request or per workspace to `"us"` or left `"global"`;
  "Only `us` and `global` are available", workspace storage geo is
  `"us"` only, and US-only inference costs 1.1 times the standard
  rate. On Bedrock and Google Cloud the region is that of the
  endpoint. No European residency option for the first-party API was
  found on the pages read; a company that needs one is pointed, by
  the admin-setup table, at inheriting its cloud provider's controls.
  The last sentence is [synthesis]. (data-residency, admin-setup)
- [verified] Compliance attestations as Anthropic states them: the
  security page names "SOC 2 Type 2 report, ISO 27001 certificate,
  etc." at the Trust Center; a BAA extends to Claude Code traffic
  only with ZDR enabled. [vendor claim]; the Trust Center itself was
  not readable, so the full list of attestations is not verified
  here. (security, legal-and-compliance)
- [verified] The security model of Claude Code: a permission system
  (rules allow, ask, deny; modes Manual, acceptEdits, plan, auto,
  bypass); an optional OS-level sandbox for shell commands with
  filesystem and network isolation; a workspace trust dialog; and
  the statement that "permission rules and sandboxing cover
  different layers. Denying WebFetch blocks Claude's fetch tool, but
  if Bash is allowed, `curl` and `wget` can still reach any URL.
  Sandboxing closes that gap". On prompt injection the page lists
  safeguards and says "no system is completely immune to all
  attacks"; its advice for untrusted content is to review commands,
  not to pipe untrusted content to Claude, and to use virtual
  machines. Credentials are stored in the macOS Keychain, in a mode
  0600 file on Linux, and on Windows in a file under the user
  profile's access controls. MCP servers are not security-audited by
  Anthropic. (security, admin-setup)
- [verified] Audit. Settings changes in the admin console produce
  audit events "available through the compliance API or audit log
  export. Contact your Anthropic account team for access"; the
  Compliance API is an Enterprise feature. Request-level audit
  logging needs a gateway between users and the provider. The
  company's own trail of what sessions did is OpenTelemetry.
  (server-managed-settings, admin-setup)
- [verified] Telemetry to Anthropic and how to turn it off: usage
  metrics (`DISABLE_TELEMETRY=1`), error reports
  (`DISABLE_ERROR_REPORTING=1`), feedback
  (`DISABLE_FEEDBACK_COMMAND=1`), surveys
  (`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`), or all at once with
  `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. "Metrics never include
  your code, prompts, or file paths." On Bedrock, Agent Platform,
  Foundry and Claude Platform on AWS these are off by default. Two
  things run on every provider: the session quality survey and the
  WebFetch domain check, which sends the hostname (not the path) to
  `api.anthropic.com`. (data-usage)
- [verified, summarised] The company's own telemetry: OpenTelemetry
  export (`CLAUDE_CODE_ENABLE_TELEMETRY=1`) of metrics (sessions,
  tokens, cost, active time, edit decisions) and events (prompts,
  API requests, tool results, tool decisions, skills activated,
  plugins loaded), deliverable to all users through managed
  settings; prompt text, responses and tool details are redacted
  unless switched on. (monitoring-usage)
- [verified] Terms a distributor must know. "Customers may not pay
  for, resell, or intermediate Claude usage on their end users'
  behalf. Each end user must authenticate with their own" key,
  subscription or provider credential; the binary must not be
  modified; and "Advertised usage limits for Pro and Max plans
  assume ordinary, individual usage". (legal-and-compliance)
- [synthesis] What a security review typically asks, and what the
  documentation answers: is our data trained on (no on commercial
  terms; yes by default-on setting on consumer plans); how long is
  it kept (thirty days, or zero by arrangement on Enterprise); where
  is it processed (global or US on the first-party API, the cloud
  region otherwise); what can the agent touch on the machine
  (whatever the user can, bounded by permission rules and the
  sandbox); who can change the policy (Owners; managed settings);
  what is logged (audit events on Enterprise, OpenTelemetry in the
  company's own stack); which third parties see data (each MCP
  server and connector on its own terms). None of these answers
  comes from the framework; all come from the plan and the managed
  settings the company chose.

### 4. Cost

Sources: https://code.claude.com/docs/en/costs ;
https://code.claude.com/docs/en/sub-agents ;
https://code.claude.com/docs/en/model-config ;
https://code.claude.com/docs/en/permission-modes ;
https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide ;
https://github.com/ryoppippi/ccusage

- [verified] The published average: "Across enterprise deployments,
  the average cost is around $13 per developer per active day and
  $150-250 per developer per month, with costs remaining below $30
  per active day for 90% of users." [vendor claim], for developers
  on default settings, not for a framework that runs several
  isolated agents per operation. The page's own advice: "start with
  a small pilot group and use the tracking tools below to establish
  a baseline before wider rollout". (costs)
- [verified] What drives cost: "Token costs scale with context size";
  the full conversation is sent with every request and re-read at
  the cached rate; a break longer than the cache lifetime reprocesses
  the whole context (the lifetime "is an hour on a subscription and
  drops to five minutes once you're drawing on usage credits; on an
  API key or cloud provider, it's five minutes by default"); thinking
  tokens are billed as output; "every subagent ... sends its own
  requests on top of the main conversation's"; agent teams use
  "approximately 7x more tokens than standard sessions". Prompt
  caching is on by default on every provider. (costs,
  third-party-integrations)
- [verified] Model choice is the lever the documentation names first:
  "Sonnet handles most coding tasks well and costs less than Opus.
  Reserve Opus for complex architectural decisions or multi-step
  reasoning ... For simple subagent tasks, specify `model: haiku`".
  Unexpectedly high spend "usually traces back to long sessions that
  were never cleared or to Opus left as the default model". (costs)
- [verified, summarised] The mechanics for a cheaper model on
  subagents: the `model` field of an agent definition (`inherit`, an
  alias or a full ID); `CLAUDE_CODE_SUBAGENT_MODEL` as a default
  that a definition's own field overrides; and
  `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`, which forces one model onto
  every subagent and overrides `model: inherit`. A model blocked by
  `availableModels` is substituted without failing. (sub-agents,
  model-config)
- [verified, summarised] The Enterprise consumption guide recommends
  Sonnet for everyday tasks, Opus for complex work and Haiku for
  high-volume light tasks, with effort level as a second lever; it
  gives no per-user dollar figure in the summary read. (consumption
  guide)
- [verified] Auto mode has a cost of its own: on Enterprise and on
  API or cloud-provider accounts "classifier calls count toward your
  token usage", mainly for shell commands and network operations.
  (permission-modes)
- [verified] Seeing and capping spend, by route. Teams and
  Enterprise: a spend report per user and per model (usage-credit
  spend only), spend limits at organisation, group and member level,
  and on Enterprise an Analytics API. Console: workspace spend
  limits, a per-user dashboard, the Claude Code Analytics API. Cloud
  providers: the cloud's own billing and budgets; nothing reaches
  Anthropic's dashboards, so per-user attribution needs
  OpenTelemetry or a gateway. "OpenTelemetry export works on every
  setup and is the only option that streams per-user token and cost
  metrics into your own observability stack in near real time." A
  managed `modelPricing` table makes the client show contracted
  rates. (costs)
- [verified] Reading usage locally: `/usage` shows the session's
  tokens and, on subscription plans, a breakdown that attributes
  recent usage to "skills, subagents, plugins, and individual MCP
  servers"; `/context` shows what fills the window; `/insights`
  writes a report on how one works. (costs)
- [verified, summarised] `ccusage` is a community tool (MIT) that
  reads the local usage data of Claude Code and other agents and
  reports cost by day, week, month and session; its page states no
  transmission of data. (ccusage)
- [verified] Guidance on size of instructions: "Aim to keep CLAUDE.md
  under 200 lines by including only essentials", moving workflow
  instructions into skills, which load on demand. (costs)
- [synthesis] On a cheaper model for mechanical steps versus one
  model throughout: Anthropic's guidance is unambiguous and points
  one way (match the model to the job; a smaller model for simple
  subagent work). It is general guidance for coding; no page read
  measures what a weaker model costs in the quality of a review. The
  forge's rule that everything runs on the session model is
  therefore a choice against the vendor's default advice, defensible
  for reviewers whose worth is their judgement, weaker for steps
  that are mechanical (bookkeeping checks, a render through a fixed
  recipe). One measurement exists in the forge's own records
  (THR.0410, the README render on another model), and it was not a
  clean comparison.

### 5. Monitoring and support in operation

Sources: https://code.claude.com/docs/en/analytics ;
https://code.claude.com/docs/en/champion-kit ;
https://code.claude.com/docs/en/third-party-integrations ;
https://academy.claude.com/tutorials/claude-enterprise-administrator-guide ;
https://github.com/github/spec-kit ;
https://github.com/bmad-code-org/BMAD-METHOD ;
https://github.com/obra/superpowers

- [verified] Adoption dashboards. Teams and Enterprise: daily active
  users, sessions, lines accepted, accept rate, a leaderboard, and
  contribution metrics through a GitHub app (pull requests and lines
  attributed to Claude Code). Console: usage and spend per member.
  Every measure offered is a measure of code. Nothing in them counts
  documents written or decisions reached, so for analysts they show
  activity (users, sessions, tokens) and nothing of outcome. The
  last sentence is [synthesis]. (analytics)
- [verified] Anthropic's rollout guidance in the Claude Code
  documentation: invest in shared CLAUDE.md files; "creating a 'one
  click' way to install Claude Code is key to growing adoption";
  start with guided, small uses; have one central team configure
  integrations. A champion kit describes the internal advocate: share
  real prompts in the channels people already read, answer in
  public, run a weekly thread, hand off to a second champion within
  thirty days; and for questions of security and data, "refer this
  question to your administrator ... champions should not improvise
  this answer". A communications kit exists (listed in the
  documentation index; not read). (third-party-integrations,
  champion-kit)
- [verified, summarised] The Enterprise administrator guide gives a
  four-phase playbook: technical setup; change management and launch
  with success measures and two or three champions per department; 
  training (sessions, workshops, weekly office hours); scaling with
  a centre of excellence. It suggests a pilot of 50 to 100 users
  before broad rollout. [vendor claim], undated. (administrator
  guide)
- [verified, summarised] Comparable open frameworks, as their
  repository pages read on 2026-10-03:
  - GitHub Spec Kit (MIT): contributions through a contributing
    guide; the user's own additions as "extensions, presets,
    bundles" with a community catalogue beside the core; support
    through issues and discussions; no telemetry statement on the
    page.
  - BMAD Method (MIT, with trademark protection of the name):
    contributions by pull request under a contributing guide; a core
    with separate modules; support through Discord, issues and
    discussions; no data statement on the page.
  - Superpowers (MIT): distributed as a plugin through the official
    Claude Code marketplace and to other agents; it states that it
    does not "generally accept contributions of new skills", only
    improvements under its own skill-writing rules; support through
    Discord, issues and a commercial address for enterprise support;
    it declares an optional telemetry of version usage with an
    opt-out variable and honours Claude Code's opt-outs.
- [synthesis] Three patterns for a user-made type returning to the
  core are visible there: a curated core that takes almost nothing
  (Superpowers); a core plus a catalogue of community extensions
  that live outside it and are listed, not merged (Spec Kit); a core
  plus modules (BMAD). None of the three pages describes a path by
  which an extension is promoted into the core; that step, where it
  happens, is an ordinary pull request judged by the maintainer.
  Only one of the three says anything about what it sends where.

### 6. What is verified, what is vendor claim, what moves

- Verified at the documentation: the mechanisms (plans, managed
  settings and their keys, delivery paths, training and retention
  policy by plan, the telemetry switches, the subagent model
  mechanics, the terms on authentication).
- Vendor claim: the average cost per developer; the compliance
  attestations; the rollout playbook's success measures; "metrics
  never include your code".
- Fast-moving or unsettled: prices and seat allowances (the
  allowance size is unpublished); which models a plan or provider
  offers and which is the default; auto mode as the starting mode
  (changed at v2.1.283); the managed keys themselves (many entries
  cite a minimum client version from the last months); model
  availability under ZDR; the per-group limit of server-managed
  settings ("not yet supported").
- Not verified here: the Trust Center's contents; the size of seat
  allowances; the Max 20x price; the exact effect list of
  `allowManagedHooksOnly` and of `allowManagedPermissionRulesOnly`;
  the sandbox's behaviour on Windows; whether European data
  residency exists on any first-party plan.

## What this asks of a framework distributed on top of Claude Code

All [synthesis], from the findings above.

What it must document:
- what the framework itself adds to the data flow, which for a
  framework of prompts and local scripts is nothing of its own: it
  sends no telemetry, calls no service, and everything a session
  reads (sources, intents, research) goes to the model provider the
  user is signed in to, under that plan's terms. Saying so in plain
  words is the data statement;
- which network access it asks for (web research, the git remotes,
  any conversion tool) and that each can be denied;
- that on a consumer plan the content of a project may be used for
  training unless the user turns the setting off, and that local
  transcripts hold the same content in plaintext;
- what it needs from the harness to work at all: project-level
  skills, agents and hooks loading; its permission rules being
  honoured; subagents; a model of a given class.

What it should leave to managed settings: who may use which model,
which permission mode sessions start in, which domains are reachable,
which marketplaces and MCP servers are allowed, telemetry, spend
limits. These are the company's, and a framework that sets them in
its own project settings is overridden anyway.

What it must not assume:
- that every user may run the strongest model (an organisation can
  restrict models per role; ZDR can exclude a model family; a cloud
  provider may lag);
- that an automatic permission mode is available (it can be disabled
  for the organisation, and falls back to Manual on unsupported
  models), or that it is absent (it is now the starting mode);
- that its hooks run or its deny rules apply (three managed locks
  switch project-level customisation off);
- that subagents run on the model it named (`model: inherit` is
  overridden by `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`);
- that a seat allowance is large enough for its heaviest operation,
  or that the user sees a dollar figure at all;
- that the user can reach a public git host from his machine.

## Options with trade-offs

**A. Document and leave it to the company.** One page: what the
forge needs from Claude Code, what it sends where (nothing of its
own), what a company should decide before use, with links to the
vendor's pages rather than copies of them. Cheapest, never stale in
the details, honest about whose decision each matter is. Its
weakness: an administrator must translate it into settings himself,
and the forge learns of a broken environment only from a confused
user.

**B. Ship recommended managed settings and a data statement.** A
sample `managed-settings.json` fragment (deny rules that match the
forge's own, domains it needs, the model list it was tried on) and a
statement a security reviewer can file. Shortens a company's review
and makes the forge's requirements testable. Its cost: the keys
change with client versions (several cited here are weeks old), so
the sample must be maintained and dated; and a sample from an
unknown open project is read by a security team as a claim to be
checked, not as authority.

**C. A cost profile.** Keep one model throughout as the default, and
offer a documented second profile in which named mechanical steps
(the bookkeeping check, a pandoc-bound render, an index sweep) run
on a smaller model, by the agent's `model` field or by the
environment variable. It follows the vendor's first advice and lets
a company on metered billing choose. Its cost: two behaviours to
keep working and to test; a weaker check that misses a finding is a
silent failure; and without measurements of the forge's own
operations in tokens the saving is a guess. A profile presupposes
those measurements (per operation, per model), which `/usage`
attribution, OpenTelemetry or `ccusage` can supply.

**D. A contribution path from a user's types to the core.** Three
shapes are in use elsewhere: a closed curated core; a catalogue of
extensions listed beside the core; modules. For a framework with
one maintainer the catalogue costs least and promises least: a
user's type lives in his own repository, is listed, and enters the
core only by the maintainer's decision through an ordinary pull
request. Its cost: a catalogue needs naming rules and a stated
compatibility with engine versions, which are other threads of the
same brief.

**E. Package the forge as a plugin.** Not asked for as an option,
but the findings raise it: a marketplace plugin is the one form that
a locked-down organisation can allow, force-enable, pin to a release
channel and audit. Its cost is a rebuild of how the engine is
delivered, and it touches the split of engine and projects; it
belongs to that question and is only named here.

## Relevance to this project

For the brief `next-gen`, section "Operation in a company": almost
everything under "data and security" and "costs" is decided by the
plan a company buys and the managed settings it deploys, not by the
forge. What is the forge's own is narrower than the section
suggests: a truthful statement of what it reads and sends, a list of
what it needs from the harness, knowledge of what its operations
cost, and behaviour that degrades visibly, not silently, when a
company has restricted the model, the permission mode or
project-level customisation.

Recommendation (this note's own, to be decided by the principal):

1. Take option A now, as part of the documentation the brief
   already wants: one page on operation in a company, with the data
   statement in it. It needs no change to the engine.
2. Before anything on cost is decided, measure: tokens and cost per
   forge operation (a save, a release, each reviewer, a render) on
   the session model. The duration watch of THR.0410 is the
   neighbour; the same runs can yield both. Option C is decided on
   those numbers, not before, and the rule of one model throughout
   stands until then.
3. State in the forge what it must not assume (the list above) and
   make the two silent failures loud: a start-of-session notice when
   the forge's hooks or deny rules are not in effect, and a reviewer
   report that names the model it ran on. Whether and how is a
   design question for the intent, not for this note.
4. Hold option B until a first company actually reviews the forge;
   write the sample from that review's questions, not ahead of them.
5. Carry option D into the brief's section on user modifications,
   where the naming and compatibility questions already live, and
   option E into the engine-split question.

For THR.0400 (a gate in front of the tools): the documentation
confirms two things the thread left to be tried. A `PreToolUse` hook
cannot loosen a deny or ask rule, so a gate built as a hook can only
add strictness; and an organisation can switch project hooks off
altogether, so a gate that lives only in the project's settings is
not a guarantee in a company. The hard guarantee, where one is
wanted, is the company's managed deny rules and sandbox; the
forge's hook is a courtesy on top. Whether "ask" from a hook holds
in auto mode was not settled by the pages read.

For THR.0210 (the public boundary): nothing in Claude Code's
administration guards what a user commits to a public repository.
Managed settings govern what the agent may do, not what content
lands in which repository. With more people working over a public
engine the boundary stays the forge's own matter (a rule, a check, a
sweep), as the thread already has it.

Consult the vendor pages again before acting on any figure or key:
the documentation changed visibly within recent client versions.
