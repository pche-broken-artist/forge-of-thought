---
project: forge
type: research
topic: what providers and agent-tool makers other than Anthropic recommend for the architecture of an agent's instructions, and what of it is a portable standard
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (draft), section "A technical clean-up"
status: immutable
---

# Agent instruction architecture beyond Anthropic

## Question

What do the LLM providers and agent-tool makers other than Anthropic
recommend today for the architecture of the instructions given to a
coding or knowledge-work agent, and what of it is a portable standard?

The note serves the section "A technical clean-up" of the draft brief
`00-brief-next-gen.md`: standardise the architecture, take as much as
possible out of `CLAUDE.md`, keep the generality. Anthropic's own
guidance is the subject of a sibling note and appears here only where
others agree with it or differ.

## How to read the epistemic marks

- **[V]** verified at a source fetched on 2026-10-03. The fetch tool
  returns most pages as a summary made by a small model, with
  quotations; a quotation given here is as that tool returned it. The
  two pages of agentskills.io and the MCP specification page came back
  as raw text, so their quotations are firm; the others carry the
  small risk of a summariser's slip and should be re-read at the URL
  before a decision rests on one sentence.
- **[2]** taken from a secondary source (a search result, a page
  describing someone else's product).
- **[S]** this note's own synthesis.
- Status of a practice: **consensus**, **emerging**, **contested**.

All product facts are as of the fetch date. Most pages carry no
publication date of their own; where one was shown, it is given.

## Key findings

### 1. The always-on instruction file: AGENTS.md is the shared name

- AGENTS.md describes itself as "a README for agents: a dedicated,
  predictable place to provide the context and instructions to help AI
  coding agents work on your project". It is plain Markdown with no
  required headings ("AGENTS.md is just standard Markdown. Use any
  headings you like."). Nested files are allowed: "Agents
  automatically read the nearest file in the directory tree, so the
  closest one takes precedence." The site gives no size limit. [V]
  https://agents.md/
- Stewardship: "AGENTS.md is now stewarded by the Agentic AI
  Foundation under the Linux Foundation." The foundation was announced
  on 2025-12-09 with three founding projects: MCP (from Anthropic),
  goose (from Block) and AGENTS.md (from OpenAI); the platinum members
  listed include the large model providers and cloud vendors. [V]
  https://agents.md/ and
  https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- Who reads it, per the site's own list: Codex, Jules, Gemini CLI,
  GitHub Copilot coding agent, VS Code, Cursor, Windsurf, Amp, Aider,
  goose, opencode, Zed, Warp, Devin, Junie, RooCode, Kilo Code,
  Factory and others. Claude Code is not on the list the fetch
  returned. [V] https://agents.md/
- What AGENTS.md standardises is thin: a file name, a place, plain
  Markdown and nearest-file precedence. How it is merged, capped,
  scoped and imported differs per tool (below). **Consensus** on the
  name; **no standard** on the semantics. [S]

Per tool, what is always loaded:

| Tool | Always-on file(s) | Merge and scope | Size rule | Source |
|---|---|---|---|---|
| Codex | `~/.codex/AGENTS.md`, then one file per directory from repo root to cwd; `AGENTS.override.md` wins at each level | concatenated root down, "Files closer to your current directory override earlier guidance because they appear later in the combined prompt" | combined cap `project_doc_max_bytes`, 32 KiB by default; Codex "stops adding files once the combined size reaches the limit" | [V] https://learn.chatgpt.com/docs/agent-configuration/agents-md |
| Gemini CLI | `~/.gemini/GEMINI.md`, workspace and parent files, plus just-in-time files found when a tool touches a directory | "concatenates the contents of all found files, and sends them to the model with every prompt"; `@file.md` imports; file name configurable (`context.fileName`, may list `AGENTS.md`) | none stated | [V] https://geminicli.com/docs/cli/gemini-md/ |
| GitHub Copilot | `.github/copilot-instructions.md`; also `AGENTS.md` (nearest wins), or a root `CLAUDE.md` or `GEMINI.md` | path-specific `NAME.instructions.md` with `applyTo` globs, added to the repository-wide file when the path matches | "Instructions must be no longer than 2 pages" and "not task specific"; "short, self-contained statements" | [V] https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions and https://docs.github.com/en/copilot/concepts/prompting/response-customization |
| VS Code | the same files, plus `CLAUDE.md`, `.claude/rules` (with `paths`), organisation instructions | "additive"; `*.instructions.md` attached when `applyTo` matches a file the agent creates or modifies; nested `AGENTS.md` behind an experimental setting | "Keep your instructions short and self-contained. Each instruction should be a single, simple statement." | [V] https://code.visualstudio.com/docs/copilot/customization/custom-instructions |
| Cursor | rules with `alwaysApply: true`; `AGENTS.md` as the plain alternative | four modes per rule: always, by the agent's judgement of `description`, by `globs`, by manual @-mention; team, project, user rules | "Keep rules under 500 lines. Split large rules into multiple, composable rules." | [V] https://cursor.com/docs/context/rules |
| Windsurf | rules marked `always_on`; root `AGENTS.md`; global rules file | four modes: always on, model decision, glob, manual; a subdirectory `AGENTS.md` behaves as a glob rule | 12,000 characters per workspace rule file, 6,000 for the global file | [V] https://docs.devin.ai/desktop/cascade/memories (the Windsurf docs address redirected there on the fetch date) |
| Amp | `AGENTS.md` in cwd and parents up to home, user and system files; falls back to `AGENT.md` or `CLAUDE.md` | subtree files included when the agent reads files there; @-mentions pull in other files; `globs` front-matter for conditional guidance | none stated | [V] https://ampcode.com/docs/customize/agents-md |
| Cline | `.clinerules/` or `.cline/rules/`, global rules; also reads `.cursorrules`, `.windsurfrules`, `AGENTS.md` | `paths` front-matter makes a rule conditional; per-rule toggle | "Rules consume context tokens"; "Keep rules concise and link to external documentation when detailed reference is needed." | [V] https://docs.cline.bot/features/cline-rules |
| Aider | nothing by default; a conventions file is loaded with `--read` or `read:` in `.aider.conf.yml` | none | none stated; read-only files are cached | [V] https://aider.chat/docs/usage/conventions.html |

What the vendors say belongs in the always-on file, and what does not:

- Belongs: project overview, build and test commands, conventions,
  security notes, commit and review procedure (AGENTS.md site, Amp,
  GitHub). [V]
- Does not belong: what a linter enforces ("Copying entire style
  guides: Use a linter instead", Cursor; "Skip conventions that
  standard linters or formatters already enforce", VS Code), rare edge
  cases, task-specific procedure (GitHub), generic advice the model
  already knows (Windsurf). [V]
- Growth rule: "Start simple. Add rules only when you notice Agent
  making the same mistake repeatedly." (Cursor); "Start from an
  observed problem instead of adding customization by default."
  (VS Code). [V]
  https://code.visualstudio.com/docs/agents/concepts/customization
- Reasons are recommended: "Include the reasoning behind rules. When
  instructions explain why a convention exists, the AI makes better
  decisions in edge cases." (VS Code). [V]

Status: **consensus** that the always-on file is short, general,
non-procedural and grown from observed failures. The numbers differ
(two pages, 500 lines, 12,000 characters, 32 KiB), the direction does
not. Anthropic's public guidance points the same way [S, from general
knowledge of it, not fetched for this note].

One measured result, **contested** in its reach: an academic study,
"Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for
Coding Agents?" (arXiv 2602.11988, first version 2026-02-12, third
version 2026-09-29), reports that "providing context files does not
generally improve task success rates, while increasing inference cost
by over 20% on average", that agents do follow the instructions in the
files, and that repository overviews give no benefit. [V]
https://arxiv.org/abs/2602.11988 A search summary of the first version
adds that model-written files lowered success slightly and
developer-written files raised it slightly, and that the authors
advise human-written files with minimal requirements only. [2] The
study measures bug-fixing tasks in code repositories; whether it
carries to a process framework, whose instructions are the product and
not a hint, is open. [S]

### 2. On-demand procedures: the Agent Skills format is the one real cross-vendor standard

- The format: a directory with a `SKILL.md` (YAML front-matter, then
  Markdown) and optional `scripts/`, `references/`, `assets/`.
  Required front-matter: `name` (at most 64 characters, lowercase
  letters, digits and hyphens, "Must match the parent directory name")
  and `description` (at most 1024 characters, "what the skill does and
  when to use it"). Optional: `license`, `compatibility`, `metadata`
  (a free string map), `allowed-tools` (marked experimental). [V, raw
  text] https://agentskills.io/specification
- Progressive disclosure is part of the specification: "Metadata
  (~100 tokens): The name and description fields are loaded at startup
  for all skills"; "Instructions (< 5000 tokens recommended): The full
  SKILL.md body is loaded when the skill is activated"; resources
  "loaded only when required". "Keep your main SKILL.md under 500
  lines." "Keep file references one level deep from SKILL.md." A
  validator exists: `skills-ref validate ./my-skill`. [V, raw text]
- Origin and governance: "The Agent Skills format was originally
  developed by Anthropic, released as an open standard, and has been
  adopted by a growing number of agent products." Development is on
  GitHub under `agentskills/agentskills`. The page names no foundation
  as steward, unlike AGENTS.md and MCP. [V, raw text]
  https://agentskills.io/home
- Adoption, per the client list on that page: Codex and ChatGPT,
  Gemini CLI, GitHub Copilot, VS Code, Cursor, Amp, Junie, OpenCode,
  OpenHands, goose, Roo Code, Kiro, Factory, Mistral Vibe, Databricks,
  Snowflake, Spring AI, Claude Code and Claude, and some thirty more.
  [V, raw text]
- Each vendor's own page confirms it:
  - Codex: skills "build on the open agent skills standard"; loaded
    from `.agents/skills` in cwd, parents up to the repo root, and
    `$HOME/.agents/skills`; the initial list takes "at most 2% of the
    model's context window or 8,000 characters"; explicit invocation
    by `$skill`, implicit by description; an optional
    `agents/openai.yaml` carries vendor extras (UI metadata,
    `allow_implicit_invocation`, dependencies such as MCP servers).
    [V] https://learn.chatgpt.com/docs/build-skills
  - Gemini CLI: "Based on the Agent Skills open standard"; workspace
    skills in `.gemini/skills/` or `.agents/skills/`, the latter
    taking precedence within a tier; activation through an
    `activate_skill` tool with a consent prompt. [V]
    https://geminicli.com/docs/cli/skills/
  - GitHub Copilot: project skills in `.github/skills`,
    `.claude/skills` or `.agents/skills`; supported by the cloud
    agent, code review, the CLI and agent mode in the editors. [V]
    https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
  - Cursor: `.agents/skills/` and `.cursor/skills/`, and it "also
    loads skills from Claude and Codex directories"; the front-matter
    field `disable-model-invocation` turns a skill into a command run
    only by `/skill-name`. [V] https://cursor.com/docs/context/skills
  - Amp: `.agents/skills/`, `.claude/skills/` and user directories; a
    skill may bundle MCP servers (`mcp.json` or `mcpServers`). [V]
    https://ampcode.com/docs/customize/skills
  - Google ADK: skills follow the specification, loaded through a
    `SkillToolset` in three levels; marked experimental. [V]
    https://adk.dev/skills/
- Commands are being folded into skills. VS Code: "Prompt files are
  deprecated for Agent Host sessions", with a migration that converts
  prompts to skills. Cursor ships `/migrate-to-skills`, which converts
  slash commands and the rules applied by the agent's judgement, and
  leaves always-on and glob rules as rules. [V]
  https://code.visualstudio.com/docs/copilot/customization/prompt-files
  and https://cursor.com/docs/context/skills Gemini CLI still keeps a
  separate command format (TOML files with `{{args}}`, `!{...}` shell
  injection and `@{...}` file injection). [V]
  https://geminicli.com/docs/cli/custom-commands/
- Vendor guidance on writing a skill: "Keep each skill focused on one
  job"; "Prefer instructions over scripts unless you need
  deterministic behavior or external tooling"; "Write imperative steps
  with explicit inputs and outputs" (Codex). [V]

Status: **consensus** on the format, on progressive disclosure and on
`description` as the trigger. `.agents/skills/` as the neutral
directory is **emerging**: Codex, Gemini CLI, Copilot, Cursor and Amp
read it; several also read `.claude/skills/`. Whether Claude Code
reads `.agents/skills/` was not checked here (the sibling note's
ground). Everything beyond `name` and `description` in the
front-matter is vendor-specific. [S]

### 3. Scoping rules by path or by task

- By path: Copilot `applyTo`, Cursor `globs`, Windsurf glob mode, Amp
  `globs`, Cline `paths`, VS Code reading `.claude/rules` with
  `paths`; nested AGENTS.md everywhere it is read. Same idea, five
  spellings, no shared format. [V, sources of the table above]
- By task: a rule or skill whose `description` the model reads to
  decide (Cursor "Apply Intelligently", Windsurf "Model Decision",
  every skill). Cursor's migration tool treats such a rule as a skill
  in all but name. [V]
- By hand: @-mention of a rule, slash or `$` invocation of a skill.
  [V]

Status: **consensus** on the three scoping axes (path, model-judged
task, explicit call); **no standard** for path scoping. A framework
whose rules are scoped by task and not by file path can express all
its scoping in the portable form, the skill. [S]

### 4. Sub-agents

- Codex: custom agents are TOML files in `.codex/agents/` with `name`,
  `description`, `developer_instructions` and optional model, sandbox,
  MCP and skill settings; built-ins `default`, `worker`, `explorer`;
  recommended for "read-heavy tasks such as exploration, tests,
  triage, and summarization", with the warning that they "consume
  more tokens than comparable single-agent runs". [V]
  https://learn.chatgpt.com/docs/agent-configuration/subagents
- Gemini CLI: Markdown with YAML front-matter in `.gemini/agents/`
  (`name`, `description`, `tools`, `model`, `max_turns`, and more);
  "Each subagent runs in its own isolated context loop"; subagents
  "cannot call other subagents"; remote agents over the A2A protocol.
  [V] https://geminicli.com/docs/core/subagents/
- VS Code and Copilot: `.agent.md` files in `.github/agents`
  (formerly chat modes) with `tools`, `agents`, `model`, `handoffs`;
  the Claude format in `.claude/agents` is read too: "Both the VS
  Code .agent.md format (with YAML arrays for tools) and the Claude
  format (with comma-separated strings) are supported." [V]
  https://code.visualstudio.com/docs/copilot/customization/custom-agents
- OpenAI Agents SDK: two patterns, a manager that calls specialists
  as tools and a handoff that passes the conversation on; orchestration
  by the model or by code, the latter being "more deterministic and
  predictable, in terms of speed, cost and performance"; advice to use
  specialised agents and to "Invest in evals". [V]
  https://openai.github.io/openai-agents-python/multi_agent/
- Google ADK: an agent's `description` is "primarily used by other
  LLM agents to determine if they should route a task to this agent";
  shared rules for all agents go through a plugin, the older
  `global_instruction` parameter being deprecated. [V]
  https://adk.dev/agents/llm-agents/

Status: **consensus** on the concept (a named role, its own prompt,
restricted tools, isolated context, a description for routing, least
privilege). **No standard** for the file: TOML at Codex, three
dialects of Markdown front-matter elsewhere. The nearest thing to a
shared format is the Claude one, which VS Code reads. Preloading a
skill into a sub-agent exists at Codex (`skills.config`) and in the
forge's present harness; it was not found documented at Gemini CLI or
VS Code. [V for what was found; S for the comparison]

### 5. Deterministic steps: hooks and scripts

- VS Code states the principle most plainly: "Hooks are
  deterministic. A hook runs when its configured lifecycle event
  occurs", "independently of the language model". Events:
  SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PreCompact,
  SubagentStart, SubagentStop, Stop. Files in `.github/hooks/*.json`;
  `.claude/settings.json` is read behind a setting, with a difference:
  the local harness "ignores matcher values, so every command for the
  event runs". Status: preview. [V]
  https://code.visualstudio.com/docs/copilot/customization/hooks
- Codex: hooks in `.codex/hooks.json` or `config.toml`; events
  PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact,
  UserPromptSubmit, SubagentStart, SubagentStop, Stop, SessionStart,
  SessionEnd, Interrupt; JSON on stdin. [V]
  https://learn.chatgpt.com/docs/hooks
- Gemini CLI: hooks in `.gemini/settings.json`; events with other
  names (BeforeAgent, AfterAgent, BeforeModel, AfterModel,
  BeforeTool, AfterTool, PreCompress, SessionStart, SessionEnd,
  Notification); JSON on stdin and stdout, exit code 2 blocks; a
  `CLAUDE_PROJECT_DIR` variable is provided as a compatibility alias.
  [V] https://geminicli.com/docs/hooks/
- Scripts inside skills are part of the Agent Skills format
  (`scripts/`), and the skills guidance says when to move work there:
  "scripts are more reliable than LLM judgment for mechanical checks",
  and a helper the agent rewrites on every run is "a signal to bundle
  the script". [V, raw text]
  https://agentskills.io/skill-creation/evaluating-skills

Status: **consensus** that whatever must always happen belongs in a
hook or a script and not in prose; **emerging** convergence of hook
events on the names Claude Code uses (VS Code and Codex share most of
them; Gemini CLI does not); **no standard** for hook configuration.
A script called from a skill is portable; the wiring of a hook is
per harness. [S]

### 6. MCP as the shared tool layer

- "MCP provides a standardized way to connect LLMs with the context
  they need"; servers offer resources, prompts ("Templated messages
  and workflows for users") and tools; the current specification
  version fetched is dated 2025-11-25. [V, raw text]
  https://modelcontextprotocol.io/specification/2025-11-25
- Governance: contributed to the Agentic AI Foundation on 2025-12-09;
  the announcement speaks of more than 10,000 published servers. [V]
- Every tool surveyed configures MCP servers; skills and sub-agents
  can declare the servers they need (Codex `agents/openai.yaml`, Amp
  `mcp.json`, Gemini CLI and VS Code agent front-matter). [V]

Status: **consensus**, the most firmly governed of the three shared
layers. It standardises tools and data access, not instructions; its
"prompts" primitive is a possible but little-used carrier for
procedures. [S]

### 7. Packaging and distribution

- Gemini CLI extensions "package prompts, MCP servers, custom
  commands, themes, hooks, sub-agents, and agent skills"; installed
  from a git URL. [V] https://geminicli.com/docs/extensions/
- Codex names skills as "the authoring format for reusable workflows
  that can later be distributed through plugins"; VS Code has agent
  plugins that "distribute packaged customization sets". [V]

Status: **consensus** on the idea of a bundle (skills, agents, hooks,
MCP in one installable unit); **no standard**: each vendor has its own
manifest. The portable unit inside every bundle is the skill. [S]

### 8. Testing an instruction set

- agentskills.io gives a full method: test cases in `evals/evals.json`
  (prompt, expected output, files, later assertions); "run each test
  case twice: once with the skill and once without it (or with a
  previous version)"; "Each eval run should start with a clean
  context"; grade assertions with evidence, by script where
  mechanical; record tokens and time; remove assertions that pass
  without the skill; human review; iterate. It also warns: "Fewer,
  better instructions often outperform exhaustive rules", and
  "Reasoning-based instructions ... work better than rigid
  directives". [V, raw text]
  https://agentskills.io/skill-creation/evaluating-skills
- OpenAI describes the same for Codex: a small prompt set (ten to
  twenty cases, including ones where the skill must not trigger),
  runs through `codex exec --json` so that the trace is machine
  readable, deterministic checks on the trace, then rubric grading
  with a fixed output schema; four kinds of goal: outcome, process,
  style, efficiency. No date on the page. [V]
  https://developers.openai.com/blog/eval-skills
- VS Code offers only inspection: the references list of a response
  and the agent debug log show which instructions were loaded. [V]
- No vendor fetched documents a regression test for the always-on
  file itself; the academic study above is the only measurement of
  that layer found. [S]

Status: **emerging**. The method is agreed in outline (a prompt set,
a baseline, clean-context headless runs, deterministic checks first,
a model as judge second), the tooling is per vendor and young. [S]

### 9. Where the vendors agree, where practice is emerging, where they contradict

Consensus [S, over the verified findings]:
1. Three layers: a short always-on file, procedures loaded on demand,
   deterministic enforcement outside the prompt.
2. The always-on file is small, general, written as short statements
   with reasons, grown from observed failures.
3. A procedure is a skill: one job, a description that says when,
   body loaded on activation, detail in referenced files, scripts for
   the mechanical parts.
4. A role with its own context and restricted tools is a sub-agent,
   routed by its description.
5. External systems come in through MCP.

Emerging:
1. `.agents/skills/` as the vendor-neutral directory.
2. Commands and prompt files merging into skills.
3. Hook events converging on one vocabulary.
4. Eval-driven development of skills.
5. Reading each other's files (VS Code and Amp read `CLAUDE.md` and
   `.claude/`; Cursor reads `.claude/skills` and `.codex/skills`;
   Cline reads Cursor's and Windsurf's rule files).

Contradictions:
1. Precedence. Codex and Cursor: the nearer file wins. VS Code:
   "additive", no order. GitHub: personal over repository over
   organisation. Cursor: team over project over user.
2. Imports. Gemini CLI and Amp expand `@file` references inside the
   always-on file; the AGENTS.md convention and Codex's page say
   nothing of imports, so a file relying on them is not portable.
3. References out. Cursor and Cline recommend pointing to files
   instead of copying; GitHub lists "Requests to refer to external
   resources" among instructions that may not work on its surfaces.
4. Size. From 6,000 characters to 32 KiB, or no limit at all.
5. Sub-agent files: TOML against three Markdown dialects.
6. Hooks: different event names, different config files, different
   handling of matchers.
7. Worth of the always-on file itself: vendors recommend it; the one
   controlled study finds no general gain on coding tasks and a cost.

Not fetched, so not claimed: OpenAI's "A practical guide to building
agents" (the PDF could not be read by the tool), a Codex
best-practices page and a Codex customisation overview (addresses
tried returned 404), Cline's own pages on skills, workflows and
hooks, Windsurf's pages on workflows and skills beyond their mention.

## Options with trade-offs

The forge today, measured on 2026-10-03 [V, by reading the files]:
`CLAUDE.md` is 650 lines and 38,877 bytes; 22 skills, the largest
119 lines; three state files of 108 to 146 lines; 8 agent files; 9
PowerShell scripts; one hook; git denied by permission rules. Only
the three contract skills carry a `name` in their front-matter; the
others have `description` and harness-specific fields
(`argument-hint`, `disable-model-invocation`, `user-invocable`).

**Option A. Stay native to one harness, clean up inside it.**
Shrink `CLAUDE.md` by moving every rule that serves one command or
one artefact into its skill; keep the present front-matter.
- For: least work; uses the richest feature set (preloaded contracts,
  permission rules, the per-prompt hook).
- Against: nothing is gained for generality; the always-on file keeps
  a name most other tools read only as a fallback.

**Option B. A portable core with a thin harness adapter.**
Keep in harness-neutral form what the standards cover, and confine
the rest to named adapter files.
- Portable: the always-on text as plain Markdown without imports or
  harness syntax, readable as `AGENTS.md`; every procedure as a
  skill that conforms to the Agent Skills specification (`name`
  matching its directory, `description` with what and when, body
  under the recommended size, detail in referenced files, mechanical
  steps in `scripts/`); templates as plain files; scripts called from
  skills; MCP for any connection to outside systems.
- Adapter, per harness: sub-agent definitions, hook wiring,
  permission rules, the preloading of contracts into agents, the
  optional front-matter fields.
- For: follows every point of consensus; the skills become usable in
  the other tools as they stand; the adapter is small and its limits
  are written down.
- Against: the forge's guarantees live exactly in the adapter
  (isolated reviewers, git only through scripts, the walkthrough
  hook), so a second harness is still real work and untested until
  done; the neutral directory is not yet read everywhere.

**Option C. Generate per-harness files from one neutral source.**
A build step emits `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, rule files
and agent files from one description.
- For: widest reach; one source.
- Against: a generator to build and maintain; generated instruction
  files drift from what was tested; it contradicts the forge's own
  rule that one mechanism lives in one place unless the generator is
  that place; no second harness is in use to justify it.

**Option D. Move the mechanisms into an MCP server.**
State changes (ledger, history, IDs) become tools any host can call.
- For: the strongest portability and determinism for the mechanical
  half.
- Against: a program to write, run and version; the forge is a
  thinking process more than a tool set, and the elicitation,
  walkthrough and review conduct cannot move there.

On size, independent of the option: at 38,877 bytes the always-on
file is above Codex's default cap of 32 KiB, more than three times
Windsurf's limit for one rule file and far beyond GitHub's two pages,
so as it stands it would be truncated or refused by the nearest
alternatives. [V for the numbers, S for the comparison]

## Relevance to this project, with a recommendation

Epistemic status of this section: this note's own synthesis; the
decision is the principal's.

**Recommendation: option B as the direction of the clean-up, taken in
the order below, without committing to a second harness.**

1. Treat the three-layer split as the architecture to standardise on,
   since every vendor surveyed describes the same one: always-on text
   for what holds in every conversation, skills for procedures and
   for the rules of one artefact, hooks and scripts for what must
   happen whatever the model decides.
2. Apply one test to every paragraph of `CLAUDE.md`: does it hold in
   every conversation, whatever the command? What passes stays
   (roles, prime directives, the working methods in short, the map of
   kinds and IDs); what serves one command or one artefact moves to
   its skill, as the forge has already begun with the state files.
   The vendors' rule for the remainder: short statements with their
   reasons, no procedure.
3. Bring every skill to the letter of the Agent Skills specification
   (a `name` equal to the directory, a `description` saying what and
   when) and run the reference validator. It is cheap, and it is the
   one step that makes the larger part of the operating layer
   portable today. Keep the harness-specific front-matter fields, but
   know them as such.
4. Write down, in one place, what is unavoidably harness-specific:
   the agent files, the preloading of contracts, the hook, the deny
   rules, the model setting. That list is the adapter; its length is
   the honest measure of how bound the forge is.
5. Keep moving deterministic steps out of prose into scripts called
   from skills (Python, as already decided), and consider hooks for
   the few rules that must hold in a long conversation, as with the
   walkthrough hook. This is where vendors agree most strongly and
   where the brief's "automation" need meets the clean-up.
6. Do not rename `CLAUDE.md` to `AGENTS.md`, do not build a
   generator and do not build an MCP server now. Each is justified
   only by a concrete second harness or a concrete outside system,
   and neither exists yet. Keeping the always-on text free of imports
   and harness syntax keeps the rename a one-line step later.
7. For the brief's need "Testing how the engine behaves", the method
   both the skills standard and OpenAI describe fits the forge's
   shape: a small set of prompts per skill, run headless in a clean
   context, against the previous version as baseline, mechanical
   checks first, a model as judge second. The forge's isolated agents
   are already the clean context the method asks for.

What this does not settle: whether the forge's guarantees survive in
another harness. No source can answer that; only a trial in one
(Codex or Gemini CLI would be the nearest, both reading AGENTS.md and
skills, both with sub-agents and hooks) would.

## Sources

All fetched 2026-10-03.

- https://agents.md/ (no page date)
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation (2025-12-09)
- https://learn.chatgpt.com/docs/agent-configuration/agents-md (reached by redirect from developers.openai.com/codex/guides/agents-md; no page date)
- https://learn.chatgpt.com/docs/build-skills (redirect from developers.openai.com/codex/skills; no page date)
- https://learn.chatgpt.com/docs/agent-configuration/subagents (redirect from developers.openai.com/codex/subagents; no page date)
- https://learn.chatgpt.com/docs/hooks (redirect from developers.openai.com/codex/hooks; no page date)
- https://developers.openai.com/blog/eval-skills (no date shown in the fetched content)
- https://openai.github.io/openai-agents-python/multi_agent/ (no page date)
- https://agentskills.io/home (no page date)
- https://agentskills.io/specification (no page date)
- https://agentskills.io/skill-creation/evaluating-skills (no page date)
- https://modelcontextprotocol.io/specification/2025-11-25 (specification version 2025-11-25)
- https://geminicli.com/docs/cli/gemini-md/ (no page date)
- https://geminicli.com/docs/cli/skills/ (no page date)
- https://geminicli.com/docs/cli/custom-commands/ (no page date)
- https://geminicli.com/docs/core/subagents/ (no page date)
- https://geminicli.com/docs/hooks/ (no page date)
- https://geminicli.com/docs/extensions/ (no page date)
- https://adk.dev/agents/llm-agents/ (redirect from google.github.io/adk-docs; no page date)
- https://adk.dev/skills/ (no page date)
- https://code.visualstudio.com/docs/copilot/customization/overview (no page date)
- https://code.visualstudio.com/docs/agents/concepts/customization (no page date)
- https://code.visualstudio.com/docs/copilot/customization/custom-instructions (no page date)
- https://code.visualstudio.com/docs/copilot/customization/prompt-files (no page date)
- https://code.visualstudio.com/docs/copilot/customization/custom-agents (no page date)
- https://code.visualstudio.com/docs/copilot/customization/hooks (no page date)
- https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions (no page date)
- https://docs.github.com/en/copilot/concepts/prompting/response-customization (no page date)
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills (no page date)
- https://cursor.com/docs/context/rules (no page date)
- https://cursor.com/docs/context/skills (no page date)
- https://docs.devin.ai/desktop/cascade/memories (redirect from docs.windsurf.com/windsurf/cascade/memories; no page date)
- https://ampcode.com/docs/customize/agents-md (no page date)
- https://ampcode.com/docs/customize/skills (no page date)
- https://aider.chat/docs/usage/conventions.html (no page date)
- https://docs.cline.bot/features/cline-rules (no page date)
- https://docs.cline.bot/customization/overview (no page date)
- https://arxiv.org/abs/2602.11988 (v1 2026-02-12, v3 2026-09-29)
