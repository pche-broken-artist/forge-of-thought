---
project: forge
type: research
topic: what Anthropic recommends today for building a framework on Claude Code (memory, skills, subagents, hooks, permissions, plugins, headless use, engineering guidance) and where the forge's operating layer follows or departs from it
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (draft), section "A technical clean-up"; research/2026-10-03-operating-layer-architecture-and-debt.md (inventory, debts, options A to D); research/2026-10-03-agent-instruction-architecture-beyond-anthropic.md; research/2026-08-29-claude-code-packaging.md and research/2026-10-02-running-reviewers-without-the-conversation.md (re-verified, not repeated); the engine's files as they stand on 2026-10-03 (CLAUDE.md, .claude/skills/**, .claude/agents/*, .claude/settings.json, scripts/hook-walkthrough.ps1); 10-intent.md searched by ID, never loaded whole
status: immutable
---

# Anthropic's guidance for Claude Code, and where the forge departs

## Question

What does Anthropic recommend today for building a framework on
Claude Code, and where does the forge's operating layer depart from
it?

The note serves the section "A technical clean-up" of the draft brief
`next-gen` and the options C and D of the internal note
`2026-10-03-operating-layer-architecture-and-debt.md`, which that note
left dependent on "what Claude Code itself offers". It gives findings
and options, not a redesign.

## How it was read, and the marks

All sources were fetched on 2026-10-03. The documentation pages of
`code.claude.com/docs` carry no date of their own; the newest version
they name is v2.1.288, and the "What's new" index runs to the week of
7 to 11 September 2026. Dated sources carry their date below.

The fetch tool answers through a small model. For most documentation
pages it returned the page's Markdown as it stands (the `.md`
address), so quotations from them are firm. Three pages came back as
a model-made digest with quotations: `hooks.md`, `sub-agents.md` and
the first reading of `skills.md`; the four engineering articles and
the blog post likewise. A sentence quoted from those should be
re-read at the address before a decision rests on it alone.

- **[V]** verified at a page fetched as raw text.
- **[Vs]** verified at a page that came back as a digest with
  quotations.
- **[O]** observed in this session's harness, not documented.
- **[F]** verified in the forge's own file.
- **[S]** this note's synthesis.

## Key findings

### 1. Memory and instructions

- What belongs in CLAUDE.md: "Keep it to facts Claude should hold in
  every session: build commands, conventions, project layout, 'always
  do X' rules. If an entry is a multi-step procedure or only matters
  for one part of the codebase, move it to a skill or a path-scoped
  rule instead." [V] `memory.md`
- Size: "target under 200 lines per CLAUDE.md file. Longer files
  consume more context and reduce adherence." A file is loaded whole
  up to 4 MiB; "Shorter files produce better adherence." A warning is
  shown at startup when a file is over the recommended length. [V]
  `memory.md`. The best-practices page is blunter: "Bloated CLAUDE.md
  files cause Claude to ignore your actual instructions!" and, for
  each line, "Would removing this cause Claude to make mistakes? If
  not, cut it." [V] `best-practices.md`
- Style: instructions "concrete enough to verify", grouped "under
  markdown headers and bullets. Organized sections are easier for
  Claude to follow than dense paragraphs." Emphasis only on the one
  line that is skipped: "If you emphasize many lines, none of them
  stands out." [V] `memory.md`, `best-practices.md`
- Status of the file: "CLAUDE.md content is delivered as a user
  message after the system prompt"; "context, not enforced
  configuration"; "there's no guarantee of strict compliance". What
  must run at a fixed point is to be a hook. [V] `memory.md`
- Imports (`@path`, four hops, an approval dialog for a path outside
  the working directory) "help you organize a long file but don't
  reduce its context cost, because imported files also load at
  launch." [V] `memory.md`
- Path-scoped rules: `.claude/rules/*.md`, found recursively; without
  `paths` they load at launch like CLAUDE.md; with `paths` (globs,
  the only front-matter field a rule has) they load "when Claude uses
  the Read, Write, or Edit tool on a file matching the pattern".
  User-level rules live in `~/.claude/rules/`. The note on the same
  page: "For task-specific instructions that don't need to be in
  context all the time, use skills instead." [V] `memory.md`
- Nested and local files: every CLAUDE.md and CLAUDE.local.md from
  the working directory up to the filesystem root loads at launch,
  concatenated root down; files in subdirectories load when Claude
  reads a file there. Block-level HTML comments are stripped before
  the content reaches the model. [V] `memory.md`
- Compaction: "Project-root CLAUDE.md survives compaction: after
  `/compact`, Claude re-reads it from disk and re-injects it". [V]
- Subagents: a subagent that is not a fork starts with its own system
  prompt, the task message, "every level of the CLAUDE.md hierarchy
  the main conversation loads, including ... `CLAUDE.local.md`",
  a git status snapshot, and the preloaded skills. It does not get
  the conversation, the output style or the session's auto memory.
  New since the note of 2026-10-02: the agent field `omitClaudeMd`
  (v2.1.271) launches a subagent "without the user, project, and
  local CLAUDE.md files ... Use it for subagents that take everything
  they need from the delegation prompt". [Vs] `sub-agents.md`; the
  CLAUDE.md part also [V] `features-overview.md`
- AGENTS.md: read natively since v2.1.277, by default only when no
  CLAUDE.md or CLAUDE.local.md stands in the working directory or
  above it; "Not read: `AGENTS.local.md`, `AGENTS.override.md`, or
  anything under a `.agents/` directory". [V] `memory.md`. This
  settles the point the sibling note left open: Claude Code does not
  read `.agents/skills/`.
- Tools for upkeep: `/doctor prompt-audit` (v2.1.283) reports
  "instructions written for older models, references to files or
  commands that don't exist, and files that contradict each other"
  across CLAUDE.md, rules, skills, commands, subagents and output
  styles; the `InstructionsLoaded` hook logs which instruction files
  load and why. [V] `memory.md`

Where Anthropic stands against the other vendors (sibling note): the
same direction, a short always-on file grown from observed mistakes,
with a harder number (200 lines against 500 at Cursor or 32 KiB at
Codex) and one mechanism the others lack, the subagent that can be
started without the always-on file. [S]

### 2. Skills

- "Custom commands have been merged into skills." A skill is the
  recommended form; `.claude/commands/` keeps working. [Vs]
  `skills.md`
- Front-matter today, in full, all optional except that
  `description` is recommended [Vs] `skills.md`: `name` (defaults to
  the directory name), `description`, `when_to_use` (both together
  cut at 1,536 characters in the listing), `argument-hint`,
  `arguments` (named positional arguments), `disable-model-invocation`,
  `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`,
  `effort`, `context` (`fork`), `agent`, `background` (with `fork`
  only; default `true`, v2.1.218), `hooks`, `paths`, `shell`
  (`bash` or `powershell`, for the injected commands), `metadata`,
  `license`, `compatibility`. Outside Claude Code only the fields of
  the Agent Skills specification are accepted, and an upload with
  `argument-hint` "fails with a hard error".
- Arguments: `$ARGUMENTS` is the whole string; `$ARGUMENTS[N]` is
  "0-based", and `$N` is its shorthand, "such as `$0` for the first
  argument or `$1` for the second"; `$name` for an argument declared
  in `arguments`; indexed arguments "use shell-style quoting". When
  no placeholder receives a value, the input is appended as
  `ARGUMENTS: <value>`. Further substitutions: `${CLAUDE_SESSION_ID}`,
  `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`,
  and for plugin skills `${CLAUDE_PLUGIN_ROOT}` and
  `${CLAUDE_PLUGIN_DATA}`. [Vs] `skills.md`
- The 0-based indexing is not only documented. [O] In this session
  the forge's `/ledger` skill, whose body reads "the ledger of
  project $1", was invoked with the arguments `alpha beta` and was
  rendered as "the ledger of project beta".
- Invocation control: `disable-model-invocation: true` means the
  description is not in context and only the user starts the skill;
  the documentation recommends it "for workflows with side effects".
  It also keeps the skill from being preloaded into a subagent and
  from being run by a scheduled task. `user-invocable: false` hides a
  skill from the menu and leaves it to the model. [Vs] `skills.md`,
  [V] `best-practices.md`
- Progressive disclosure: the listing of names and descriptions is
  always in context (a budget of 1 per cent of the context window);
  the body loads on invocation; supporting files load when read;
  scripts are "executed, not loaded". "Keep `SKILL.md` under 500
  lines." [Vs] `skills.md`. The authoring guide adds "Keep references
  one level deep from SKILL.md", because "Claude may partially read
  files when they're referenced from other referenced files", and a
  table of contents for a reference file over 100 lines. [V]
  platform.claude.com, skill authoring best practices
- Life of a loaded skill: the body "enters the conversation as a
  single message and stays there"; "Claude Code does not re-read the
  skill file on later turns"; after compaction the latest invocation
  of each skill is re-attached, "keeping the first 5,000 tokens of
  each", within 25,000 tokens for all. So "write guidance that should
  apply throughout a task as standing instructions" and "put the most
  important instructions near the top". [Vs] `skills.md`
- Dynamic context injection: `` !`command` `` and a fenced `` ```! ``
  block run "before the skill content is sent to Claude. The command
  output replaces the placeholder"; `shell: powershell` chooses the
  shell; `disableSkillShellExecution` turns it off by policy. [Vs]
- Forked skills: `context: fork` starts "a new subagent of the type
  set in the `agent` field and gives it the skill content as its
  prompt"; the agent is a built-in one or "any custom subagent from
  `.claude/agents/`", fixed in the front-matter, not chosen at
  invocation. It runs in the background unless `background: false`,
  and a backgrounded fork has "the narrower tool set that applies to
  background subagents". It "only makes sense for skills with
  explicit instructions". [Vs] `skills.md`
- Skills calling skills: not found on the page. What is documented
  is that Claude, and a subagent, can invoke any listed skill through
  the Skill tool, and that a subagent preloads the skills named in
  its `skills` field. A skill citing another skill's file by path is
  plain file reading and has no status of its own. [Vs, by absence]
- Scope by path: `paths` on a skill limits automatic loading to work
  on matching files. Nested `.claude/skills/` directories below the
  start directory load when Claude first works there. [Vs]
- Control from outside the file: `skillOverrides` in settings (`on`,
  `name-only`, `user-invocable-only`, `off`); permission rules
  `Skill(name)`. [Vs]
- Authoring guidance [V] platform.claude.com: "The context window is
  a public good"; "Default assumption: Claude is already very smart";
  match "degrees of freedom" to how fragile the task is (free text
  where many paths are right, "Run exactly this script" where one
  is); one term for one thing; no time-bound content in the body, an
  "Old patterns" section for what was; "Prefer scripts for
  deterministic operations"; the plan, validate, execute pattern, in
  which the model writes a structured plan file and a script checks
  it before anything is applied; and "Create evaluations BEFORE
  writing extensive documentation."
- Measuring: `/skill-doctor` (v2.1.252) reports what each skill
  costs and how often it is used; the `skill-creator` plugin runs
  test cases with and without a skill. [Vs]

### 3. Subagents and other multi-agent features

- Front-matter today [Vs] `sub-agents.md`: `name`, `description`
  (both required), `tools`, `disallowedTools`, `model` (an alias, a
  full ID or `inherit`), `permissionMode`, `maxTurns`, `skills`
  ("The full skill content is injected"), `mcpServers`, `hooks`,
  `memory` (`user`, `project`, `local`: a directory of its own with a
  `MEMORY.md`), `background`, `omitClaudeMd`, `effort`, `isolation`
  (`worktree`), `color`, `initialPrompt`, `experimental`. For an
  agent shipped in a plugin, `hooks`, `mcpServers` and
  `permissionMode` are ignored.
- Nesting: three layers below the main conversation by default
  (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`); an agent without `Agent`
  in `tools` cannot spawn. Holds as the note of 2026-10-02 has it.
- Foreground and background: in an interactive session "fork mode" is
  on by default (v2.1.232), and then "Claude Code runs the subagent
  in the background ... and Claude can't ask for the foreground";
  "Background subagents run with a smaller built-in tool set than
  foreground subagents". [Vs] What that smaller set leaves out was
  not read; it bears on reviewers that write their own report.
- When to use which [V] `features-overview.md`, [Vs] `sub-agents.md`:
  the main conversation for work with back-and-forth; a subagent when
  "the work is self-contained and can return a summary" or tool
  restrictions are wanted; a skill for "reusable prompts or workflows
  that run in the main conversation context"; "A subagent can preload
  specific skills. A skill can run in isolated context using
  `context: fork`."
- Review by a fresh context is itself recommended: "A reviewer
  running in a fresh subagent context sees only the diff and the
  criteria you give it, not the reasoning that produced the change",
  with the caution that "A reviewer prompted to find gaps will
  usually report some, even when the work is sound". [V]
  `best-practices.md`
- Dynamic workflows: a JavaScript script that calls `agent()`,
  `pipeline()`, `parallel()`; saved in `.claude/workflows/` and run
  as `/<name>`; shippable in a plugin's `workflows/`; "No direct
  filesystem or shell access from the workflow itself"; "No mid-run
  user input"; needs approval per run or a `Workflow(<name>)` allow
  rule; on paid plans, switchable off by `disableWorkflows`. [V]
  `workflows.md`. The page still does not document a custom agent
  type for `agent()`.
- Agent teams: "experimental and disabled by default"; a teammate
  does not get the `skills` of the subagent definition it is spawned
  from. [V] `agent-teams.md`. Not a base to build on yet. [S]

### 4. Hooks

- Events named on the reference page [Vs] `hooks.md`: SessionStart,
  Setup, InstructionsLoaded, UserPromptSubmit, UserPromptExpansion,
  PreToolUse, PermissionRequest, PermissionDenied, PostToolUse,
  PostToolUseFailure, PostToolBatch, MessageDisplay, Notification,
  SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop,
  StopFailure, TeammateIdle, PreCompact, PostCompact, CwdChanged,
  DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove,
  PreModelSwitch, PostModelSwitch, Elicitation, ElicitationResult,
  ConfigChange, SessionEnd.
- What the ones that matter here can do [Vs]: UserPromptSubmit adds
  context or blocks the prompt; UserPromptExpansion can block a typed
  command as it expands; PreToolUse returns allow, deny, ask or
  defer, can rewrite the tool input (`updatedInput`) and add context;
  PostToolUse can add context, replace the tool output and block;
  SubagentStart adds context to a starting subagent; SubagentStop and
  Stop can block the end of a run and receive
  `last_assistant_message`, SubagentStop also `agent_id`,
  `agent_type` and `agent_transcript_path`; SessionStart and
  PostCompact add context. A hook's added context or plain output is
  capped at 10,000 characters.
- Handlers: `command`, `http`, `mcp_tool`, `prompt` (one model call
  that returns a decision) and `agent` (a verifying subagent, marked
  experimental). [Vs]
- Where hooks live: settings files, managed policy, a plugin's
  `hooks/hooks.json`, the front-matter of a skill ("the rest of the
  session once the skill is invoked", with `once`) and of a subagent
  ("while that subagent is running"). The `if` field takes one
  permission-rule pattern. [Vs]
- When to use one: "Unlike CLAUDE.md instructions which are advisory,
  hooks are deterministic and guarantee the action happens." [V]
  `best-practices.md`. "Put guardrails in hooks. An instruction like
  'never edit `.env`' in CLAUDE.md or a skill is a request, not a
  guarantee. A `PreToolUse` hook that blocks the edit is
  enforcement. If a rule must hold every time, make it a hook rather
  than a prompt instruction." [V] `features-overview.md`

### 5. Settings, permissions, sandbox

- Rules: "evaluated in order: deny, then ask, then allow"; a deny in
  any scope wins; "PreToolUse hook decisions don't bypass permission
  rules". [V] `permissions.md`
- Bash and PowerShell rules: Claude Code splits compound commands,
  and "Deny and ask rules apply when any subcommand matches them,
  including a command nested inside a subshell". But a rule "doesn't
  match the same program invoked in a different form, so a deny or
  ask rule covers the invocation Claude usually produces and isn't a
  security boundary around the program": `Bash(curl *)` does not stop
  `/usr/bin/curl` or `sh -c 'curl ...'`. For enforcement that does
  not depend on the command text the page names the sandbox and a
  PreToolUse hook. [V] `permissions.md`
- Modes: `default` (Manual), `acceptEdits`, `plan`, `auto`,
  `dontAsk`, `bypassPermissions`. Since v2.1.283 "auto mode is the
  built-in starting permission mode for interactive terminal and VS
  Code sessions on every plan and provider": a classifier reviews
  actions instead of the user. "Explicit ask rules still force a
  prompt." The classifier reads the user's messages and "your
  CLAUDE.md content", and treats "boundaries you state in the
  conversation as a block signal", but "Boundaries are not stored as
  rules ... For a hard guarantee, add a deny rule instead." [V]
  `permission-modes.md`
- Sandbox: "The sandbox runs on macOS, Linux, and WSL2. On native
  Windows, Claude Code runs commands unsandboxed." [V]
  `sandboxing.md`
- Managed settings can fix rules for an organisation
  (`allowManagedPermissionRulesOnly`, `allowManagedHooksOnly`,
  a managed CLAUDE.md, `disableSkillShellExecution`). [V]
- Project `settings.json` and hooks "load only from `<cwd>/.claude/`
  with no parent-directory fallback". [V]
  `agent-sdk/claude-code-features.md`

### 6. Plugins and marketplaces

- A plugin carries: skills, commands, agents, hooks, MCP and LSP
  servers, output styles, workflows, themes, monitors, executables in
  `bin/`, a `settings.json` of which "Only `agent` and
  `subagentStatusLine` take effect", `userConfig` values asked at
  enable time, channels, and an `evals/` directory. [V]
  `plugins/manifest-reference.md`
- Always-on instructions: still no CLAUDE.md and no rules. "A
  `CLAUDE.md` at the plugin root isn't loaded as context, and `claude
  plugin validate` warns when it finds one. To include instructions
  that load into Claude's context, put them in a skill." [V] The
  note of 2026-08-29 holds on this point.
- One always-on carrier the older note did not have: a plugin's
  output style with `force-for-plugin: true` is applied
  "automatically whenever the plugin is enabled, without requiring
  users to select it". An output style is "sent with every request";
  a custom one leaves out Claude Code's software-engineering
  instructions unless `keep-coding-instructions: true`, and is the
  documented way to make Claude "something other than a software
  engineer". It reaches the main conversation and forks, not other
  subagents. [V] `output-styles.md`. Anthropic's blog reserves output
  styles for "significant role changes (code assistant to general
  assistant)". [Vs] blog, 2026-06-18
- Versions: the manifest's `version` pins users to the cached copy
  until the string changes; without it the commit SHA is the version.
  Auto-update is on for Anthropic's official marketplace and "off for
  every other marketplace" unless set. A plugin directory with a
  manifest placed under `.claude/skills/` loads in place as a
  "skills-directory plugin", project-scope only from the primary
  working directory and after the trust dialog. [V]
  `plugins/loading.md`
- `claude plugin eval` (v2.1.269): cases of a prompt and graders
  (`regex`, `tool_used`, `tool_order`, `file_exists`, and the
  model-judged `llm` and `baseline`; "There are no custom-code
  graders"), each case run three times with the plugin and three
  times without, a JSON result for CI. Each run is a fresh `claude
  -p` child in a temporary home "with only your plugin loaded":
  "Your user settings, hooks, `CLAUDE.md` files, MCP servers, other
  installed plugins, memory, and skills are absent." It needs a
  plugin directory or a skills-directory plugin. [V]
  `plugin-evals.md`
- Changed since 2026-08-29: `--add-dir` now loads the added
  directory's `.claude/agents/` as well as its skills and commands.
  [Vs] `skills.md`

### 7. Headless and programmatic use

- `claude -p` loads what an interactive session loads; user-invoked
  skills work ("Include `/skill-name` in the prompt string");
  `--output-format json`, `--json-schema`, `--allowedTools`,
  `--permission-mode`, `--agent`, `--agents`, `--settings`,
  `--append-system-prompt`. `--bare` skips hooks, skills, agents,
  plugins, memory and CLAUDE.md, and "will become the default for
  `-p` in a future release". [V] `headless.md`
- The Agent SDK reads the same files when `settingSources` includes
  them; skills "must be created as filesystem artifacts". [V]
- Routines (cloud, schedule or API or GitHub trigger) are a research
  preview and run on a cloned GitHub repository; local scheduling is
  `/loop` and the desktop app's tasks. [V] `routines.md`
- Bearing: a forge script that starts `claude -p` (the `claude`
  engine of the conversions) today inherits the engine's CLAUDE.md,
  hook and skills, and would stop doing so the day `--bare` becomes
  the default unless it names what it needs. [S]

### 8. Anthropic's engineering writing

- Context engineering (2025-09-29): context is "a finite resource
  with diminishing marginal returns"; aim for "the minimal set of
  information that fully outlines your expected behavior", at the
  "right altitude" between brittle hard-coded logic and vague
  guidance; a hybrid of files loaded up front and retrieval "just in
  time"; for long work, compaction, notes kept outside the context
  window, and subagents that return a condensed summary. [Vs]
- Building effective agents (2024-12-19): "find the simplest solution
  possible, and only increasing complexity when needed"; a workflow
  is orchestration "through predefined code paths", an agent directs
  itself; the patterns named are prompt chaining, routing,
  parallelization, orchestrator-workers and evaluator-optimizer;
  frameworks are warned against where they hide the prompts. [Vs]
- Writing tools for agents (2025-09-11): a tool is "a contract
  between deterministic systems and non-deterministic agents"; fewer,
  consolidated tools; build them against evaluations. [Vs]
- Harnesses for long-running agents (2025-11-26): state lives in
  files (a feature list, progress notes, git), each session starts by
  reading them and ends by leaving a clean state, work proceeds one
  item at a time. [Vs]
- Steering Claude Code (blog, 2026-06-18): "Keep CLAUDE.md under 200
  lines, give it an owner, and review changes to it like code";
  "Instructions that are procedural ... belong in a skill rather
  than in CLAUDE.md"; hooks "for anything that should happen
  deterministically"; bundle as a plugin "to share a coherent setup
  across teammates or projects". [Vs]

Status: all of the above is Anthropic's own consensus, stated in more
than one place. Emerging and still moving: auto mode as the default,
`claude plugin eval`, workflows, `omitClaudeMd`, forced output styles.
Experimental by Anthropic's own word: agent teams, `agent` hooks,
routines.

## The comparison with the forge

| # | Subject | Anthropic today | The forge today [F] | Verdict |
|---|---|---|---|---|
| 1 | Size of the always-on file | under 200 lines; longer "reduce adherence" | CLAUDE.md 650 lines, plus CLAUDE.local.md | departs; known (THR.0240), not decided |
| 2 | Kind of content in it | facts and "always do X"; procedures to skills, part-of-tree rules to path rules | 285 lines serve named commands (internal note, finding 3) | departs; the move has begun (POS.1380, state files, walkthrough) |
| 3 | Form of the text | headers and bullets, short verifiable statements | long hard-wrapped paragraphs carrying several rules each | departs; deliberate as house style (prose for humans, 72 columns), not weighed against adherence |
| 4 | Commands as skills | skills are the form | all 18 commands are skills (POS.1130) | follows |
| 5 | Side-effect commands | `disable-model-invocation: true` | nine commands carry it (POS.1090) | follows, to the letter |
| 6 | Positional arguments | `$0` is the first argument; `arguments:` gives names | bodies use `$1` for the first and `$2` for the second (`/new-project`, `/render`, `/publish`, `/ledger`, `/spinoff`, `/man`, `/import-project`, `/forge`, `/recipe`) | a defect, observed: `$1` receives the second argument |
| 7 | Size and layering of skills | body under 500 lines, references one level deep | largest skill 119 lines; state and genre files as supporting files | follows; cross-skill citations by path go beyond one level |
| 8 | Skill `name` | optional in Claude Code, defaults to the directory | only the contracts carry it | follows Claude Code; departs from the open specification only (sibling note) |
| 9 | Reviewers | subagent, restricted tools, `skills` preloaded, fresh context | exactly that, `model: inherit` (POS.0400, POS.1120, POS.0930) | follows; the strongest match |
| 10 | What a reviewer's context holds | CLAUDE.md by default; `omitClaudeMd` to leave it out | every reviewer carries all 650 lines and the instance file (THR.0240, POS.0950) | native answer exists since v2.1.271, unused |
| 11 | Isolated generation | forked skill, or a named agent | five implementations (internal note, finding 2); `/render` composes a prompt for `general-purpose` | departs; `context: fork` was set aside for the reviewers only (POS.1140) |
| 12 | Filing a subagent's output | SubagentStop hook with the final message; hooks in agent front-matter | reviewers write files and ledger rows themselves, or the command does | departs; THR.0500 open, note of 2026-10-02 |
| 13 | A rule that must hold every turn | a hook | `UserPromptSubmit` hook prints five lines (POS.1170) | follows; for reminding, not for enforcing |
| 14 | A rule that must not be broken | PreToolUse hook, deny or ask rule, sandbox | two deny patterns for git; consent, "scripts only" and "ask before your own command" are text | departs; THR.0400 open |
| 15 | Permission mode | auto is the default start mode | no `defaultMode` in the engine's settings; consent is a prose rule | exposed: what asks is now decided by a classifier unless the engine says otherwise [S] |
| 16 | Deterministic steps | scripts called from skills; injected command output; plan, validate, execute | IDs, ledger rows, history records, `last_change`, rosters are done by the model from prose | departs; this is option D |
| 17 | Rosters | the skill listing and the agent descriptions are already in context | five dispatchers scan directories; a written Commands table | partly redundant with the platform for commands and reviewers; states and genres have no native roster |
| 18 | Testing behaviour | evaluations first; `claude plugin eval`, skill-creator | nothing | departs; the brief names it |
| 19 | Distribution | plugin, marketplace, versions | a clone launched from its root (POS.0760; a plugin as the only shape rejected, REJ.0150) | deliberate; holds against today's docs |
| 20 | Role of the session | output style for a non-engineering role | the forge runs on Claude Code's software-engineering system prompt | not considered so far |
| 21 | Citations of intent IDs in instructions | "Only add context Claude doesn't already have" | 93 citations of POS, THR, REJ in 33 operating files | departs; to the model they are tokens without content unless the intent is read [S] |

What the forge follows without remark: skills as the unit of
procedure, supporting files read on demand, restricted reviewer
tools, isolation as the source of a review's worth, a hook for what
dissolves in a long conversation, state kept in files and not in the
conversation (the ledger, the threads, the history, which is what
the long-running-harness article describes), research before
inventing. [S]

What the forge does that the platform has no answer for [S, against
the pages fetched]:
- the write discipline itself: one write per round, on the
  principal's word, reflected back first. The platform offers
  permission prompts per tool call, not consent per round of work;
- one item per message in a walkthrough. Only a reminder is
  available; a `Stop` hook of type `prompt` could in principle judge
  a reply before it ends, which is untried and would cost a model
  call per turn;
- a workspace of many repositories under one engine. Settings and
  hooks load from the launch directory only, skills up to the
  repository root: the forge's "launch from the engine root" is the
  only arrangement in which everything resolves, as the note of
  2026-08-29 found and today's pages confirm;
- the migration of a project's documents when the engine's shapes
  change. Plugins version the tool, nothing versions the data;
- a user's own types layered over a central core without name
  collisions. The nearest native pieces are plugin namespacing
  (`/plugin:skill`) and the precedence of project over plugin
  agents; neither is a model of "core plus user additions" for
  states, lenses or checks;
- a test of the always-on file. `claude plugin eval` leaves CLAUDE.md
  out of every run by design.

### The departures, ranked by what they cost

1. **Positional arguments (row 6).** Cheapest to mend and already
   costing: every command that names `$1` gets the wrong token or an
   empty one and works only because the model repairs it from the
   appended `ARGUMENTS:` line or from context. It also answers the
   internal note's debt 5: `arguments:` with names is the native
   "one way to resolve the arguments". [O], [Vs]
2. **The always-on file (rows 1 to 3, 10).** Paid on every turn and
   in every reviewer run, in tokens and, by Anthropic's own repeated
   statement, in adherence. It is also the part no native test can
   reach.
3. **Consent kept in prose while the default mode moved (rows 14,
   15).** The forge's "step by step" rests on the model asking. With
   auto mode as the starting mode, a write or a script run that the
   classifier judges routine proceeds without a prompt; the
   classifier does read CLAUDE.md and spoken boundaries, but the
   documentation itself says a hard guarantee needs a rule. On
   native Windows there is no sandbox beneath it. The internal
   note's hypothesis that a compound command passes the git deny
   rule is refuted for the tool as documented (each subcommand is
   matched, and `Bash(git *)` also catches `git -C`); what does pass
   is another form of the program, such as a full path or `sh -c`.
4. **Bookkeeping by the model (rows 12, 16).** Costs tokens at every
   write, allows the ID race, and cannot be tested. Anthropic's
   guidance is unambiguous that such steps are a script's.
5. **No evaluations (row 18).** The cost is not paid daily; it is
   what makes rank 2 expensive to mend, since every move out of
   CLAUDE.md is a change of behaviour nobody can measure.
6. **Several ways to run an isolated generation (row 11).** A cost
   of maintenance, not of behaviour.
7. **Citations of intent IDs, the house prose style, the software
   engineering system prompt (rows 3, 20, 21).** Unmeasured; each is
   a hypothesis about adherence worth one trial, not a rebuild.

## Options with trade-offs

**On option C of the internal note (shared steps become definitions
of their own; command-serving sections leave CLAUDE.md).** Anthropic's
guidance supports the direction without reserve: procedures belong in
skills, the always-on file is to stay under 200 lines. Three things
the platform adds to the option, and one warning:

- C1. *Skills as the destination* (the forge's present course). For:
  on-demand, testable by `claude plugin eval`, portable. Against: a
  loaded skill is not re-read, and after compaction only its first
  5,000 tokens return, within 25,000 for all skills, whereas the
  root CLAUDE.md is re-read whole. A rule moved into a skill is
  therefore weaker late in a long session than the same rule in
  CLAUDE.md. The forge's long working conversations are exactly that
  case. The most important lines of each definition belong at its
  top.
- C2. *Path-scoped rules as a middle tier.* A rule in
  `.claude/rules/` with `paths` loads whenever a matching file is
  read or written, whatever command is running, and reloads after
  compaction when the file is touched again. The forge's rules are
  largely rules of a kind of file (a source is immutable, a history
  is append-only, an assignment is written with shall), and its
  kinds have fixed paths (`projects/*/sources/**`,
  `projects/*/*.history.md`, `projects/*/20-assignment.md`). For:
  the rule follows the file, not the command, which covers the case
  where an artefact is touched outside `/forge`. Against: untried in
  nested, gitignored project repositories; a second home for rules
  beside the state files unless one of the two is chosen per rule
  (prime directive 10); specific to this harness, where a skill is
  portable.
- C3. *Reviewers without CLAUDE.md.* `omitClaudeMd: true` in the
  eight agent files removes the largest block of every reviewer's
  context and keeps the instance file out of it, which serves
  POS.0950 better than a prose ban. Against: each contract must then
  carry or cite everything a reviewer needs (the ID scheme, the
  document kinds); a behaviour change that needs a before-and-after
  run of one critic and one check.
- Warning for "shared steps as definitions of their own": skills
  composing skills is not a documented mechanism, and references two
  levels down are read partially. A shared step is safer as a
  supporting file cited directly from each skill that uses it, or as
  a script, than as a skill that other skills are told to follow.

**On option D (bookkeeping into scripts).** Supported at every level
of Anthropic's writing, and the platform offers three ways to wire a
script that the internal note did not have:

- D1. *Called by the model from the skill* (as the git scripts are
  today). Simplest; the model still decides to call it.
- D2. *Injected before the model sees the skill*: `` !`script` `` in
  the skill body with `shell: powershell` (or a Python call). The
  roster of members, the next free ID, the project resolved from the
  arguments arrive as facts in the prompt. For: removes six kinds of
  roster and the argument guessing with no model step. Against: runs
  at invocation only, so it suits reading state, not writing it; can
  be switched off by policy (`disableSkillShellExecution`); a
  per-invocation process.
- D3. *Run by the harness at an event*: `SubagentStop` matched on
  the reviewer's name to file its report (the recommendation of the
  note of 2026-10-02, whose facts hold today and whose input fields
  are now listed: `agent_type`, `agent_transcript_path`,
  `last_assistant_message`); `PostToolUse` on Write and Edit under
  `projects/` to run a fast validator of front-matter against
  history and feed the result back; `PreToolUse` with an `if`
  pattern to turn the forge's save script, or any raw `git`, into an
  ask or a deny. For: no model takes part. Against: hooks live in
  the launch directory's settings only; each is a process; the forge
  on native Windows has no sandbox to back them.
- The plan, validate, execute pattern of the authoring guide fits
  the write of a round: the model writes the round's changes as one
  structured file, a script validates it against the skeletons and
  applies IDs, history records, `last_change` and ledger rows. It is
  the internal note's "first step" (debt 2) with a native precedent.
  The price THR.0500 names stays: the script must read the shapes
  from the templates, or the shape lives twice.

**Option E, not in the internal note: the engine in plugin shape as
a test bed, not as distribution.** `claude plugin eval` needs a
plugin directory and loads nothing else. A manifest beside the
engine's skills, agents and hooks would let the forge's procedures be
run headless, three times each, against graders that cost nothing
(`tool_used`, `regex` over a produced file, `file_exists`). For: it
is the only native way to see "whether behaviour held" that POS.1380
and THR.0240 ask for, and it leaves POS.0760 and REJ.0150 untouched,
since nobody installs anything. Against: CLAUDE.md is absent from
every run, so only what has already moved into skills, agents and
hooks is tested, and a case that depends on a prime directive would
need it supplied by the plugin (a skill, a SessionStart hook or a
forced output style); every run is paid model usage; whether the
engine's layout (skills under `.claude/skills/`, agents under
`.claude/agents/`) can be addressed by one manifest without moving
files was not tried.

**Option F, to be weighed and not assumed: an output style for the
forge's role.** The one native always-on carrier that sits in the
system prompt and can ship in a plugin. For: the forge is not
software engineering, and the default system prompt is written for
that; roles and prime directives are the kind of text an output
style is meant for. Against: one style is active at a time and the
user can switch it; it does not reach subagents; nothing enforces
it; it would be a second always-on home beside CLAUDE.md.

## Relevance to this project, with a recommendation

Epistemic status: synthesis; the decisions are the principal's.

1. **Mend the positional arguments now**, apart from any
   architecture: either renumber to `$0`, `$1`, or declare
   `arguments:` and use names, which also gives the one definition
   of "resolve the project" the internal note found missing. It is a
   wording fix of the operating layer and needs no position.
2. **Option B of the internal note stands**, and Anthropic's pages
   give its anatomy native names: always-on text (CLAUDE.md, at most
   an output style), path rules, skills with supporting files and
   scripts, agents with preloaded contracts, hooks, settings. A
   standard that says which of these a rule of each kind lives in is
   the decision the clean-up needs first.
3. **C before D only where it can be seen to hold.** Take option E
   as the precondition of C: a small eval suite over the commands
   that already stand on their own, then move a section out of
   CLAUDE.md and run it again. This is Anthropic's "evaluations
   first" and the forge's POS.1380 said in the platform's terms.
   Within C, try C3 (`omitClaudeMd` on the reviewers) first: it is
   one line per agent, reversible, and removes the cost THR.0240
   records.
4. **D is the larger gain and the safer one**, because a script does
   not change what the model is told, only what it no longer has to
   do. Start where the internal note points, the write of a round,
   in the plan, validate, execute shape; wire the reviewers' filing
   through `SubagentStop` as the note of 2026-10-02 recommends; use
   injected command output for rosters and the next ID.
5. **Decide the permission stance explicitly.** Either the engine's
   settings name the mode it is designed for, or the operations the
   principal must see (the save and release scripts, writes under
   `projects/`) get `ask` rules, which hold in auto mode as well.
   This is the native half of THR.0400 and of the brief's question
   where the owner's word protects something.
6. **Do not adopt** agent teams, routines or workflows as a base
   now: experimental, plan-bound or unable to write files. Do not
   make the plugin the distribution shape on today's evidence:
   CLAUDE.md still cannot ship in one, and the workspace of nested
   repositories still needs the launch from the engine root.
7. **Run `/doctor prompt-audit` once** over the operating layer as a
   second opinion beside the check `single-source-of-truth`; it is
   built for stale references and contradictions across exactly
   these files.

## What stays uncertain

- How background subagents' "smaller built-in tool set" affects a
  reviewer that writes its own report, and whether it explains the
  refusal observed on 2026-10-01: not read.
- Whether path-scoped rules fire for files inside the nested,
  gitignored project repositories: untried.
- Whether `claude plugin eval` can address the engine's present
  layout: untried.
- The exact input of `SubagentStop` and the full event table come
  from a digest of the hooks page, not its raw text.
- How far a 650-line CLAUDE.md actually lowers adherence in the
  forge's use: Anthropic states the direction and gives no measure;
  the forge's own record (POS.1170) is one data point for it.
- Every version number above is as the pages stated it on the fetch
  date; the platform changes weekly.

## Sources

All fetched 2026-10-03. Documentation pages carry no date.

- https://code.claude.com/docs/llms.txt
- https://code.claude.com/docs/en/memory.md
- https://code.claude.com/docs/en/skills.md (digest with quotations)
- https://code.claude.com/docs/en/sub-agents.md (digest with quotations)
- https://code.claude.com/docs/en/hooks.md (digest with quotations)
- https://code.claude.com/docs/en/features-overview.md
- https://code.claude.com/docs/en/best-practices.md
- https://code.claude.com/docs/en/permissions.md
- https://code.claude.com/docs/en/permission-modes.md
- https://code.claude.com/docs/en/sandboxing.md
- https://code.claude.com/docs/en/output-styles.md
- https://code.claude.com/docs/en/headless.md
- https://code.claude.com/docs/en/workflows.md
- https://code.claude.com/docs/en/agent-teams.md
- https://code.claude.com/docs/en/routines.md
- https://code.claude.com/docs/en/agent-sdk/claude-code-features.md
- https://code.claude.com/docs/en/plugins/components.md
- https://code.claude.com/docs/en/plugins/manifest-reference.md
- https://code.claude.com/docs/en/plugins/loading.md
- https://code.claude.com/docs/en/plugin-evals.md
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29; digest)
- https://www.anthropic.com/engineering/building-effective-agents (2024-12-19; digest)
- https://www.anthropic.com/engineering/writing-tools-for-agents (2025-09-11; digest)
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (2025-11-26; digest)
- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more (2026-06-18; digest)

Not fetched, so not claimed: the hooks guide, the settings reference,
the Agent SDK references, the scheduled-tasks and plugin marketplace
pages, the changelog.
