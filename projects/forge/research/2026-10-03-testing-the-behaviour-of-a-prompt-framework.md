---
project: forge
type: research
topic: how the behaviour of a prompt-based framework or agent is tested, so that a change of instructions, harness or model is caught before users meet it
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1, section "Testing how the engine behaves"
status: immutable
---

# Testing the behaviour of a prompt framework

## Question

How is the behaviour of a prompt-based framework or agent tested
today, so that a change of the instructions, of the harness or of the
model is caught before users meet it?

How to read the marks. Every finding carries one of three marks:
**[verified]** read at a source fetched on 2026-10-03 (the URL is
given); **[secondary]** taken from a source that reports on another;
**[synthesis]** this note's own reasoning, not found stated anywhere.
All pages were fetched on 2026-10-03; the date after a source is its
own publication or update date where the page gave one. Most pages
were read through a summarising fetch, so a quotation is as that
fetch relayed it; four pages were read in full text and are marked
"full text". Product facts here change fast.

## Key findings

### 1. The shared vocabulary and the consensus core

Source: Anthropic, "Demystifying evals for AI agents", published
2026-01-09,
https://anthropic.com/engineering/demystifying-evals-for-ai-agents

- [verified] The terms the field now shares: a *task* (one test with
  inputs and success criteria), a *trial* (one attempt; several are
  run because "model outputs vary between runs"), a *grader*, a
  *transcript* (the full record of a trial), the *outcome* (the state
  of the environment at the end, as distinct from what the agent
  said), the *evaluation harness* and the *suite*.
- [verified] Three kinds of grader. Code-based: fast, cheap,
  reproducible, easy to debug, but brittle to valid variation.
  Model-based (a rubric judged by a model): flexible, handles open
  output, but non-deterministic, costs money and needs calibration
  against human judgement. Human: the gold standard, slow and
  expensive.
- [verified] Two kinds of suite. A capability suite asks what the
  agent can do and starts at a low pass rate. A regression suite asks
  whether it still does what it did and "should have a nearly 100%
  pass rate"; tasks graduate from the first into the second.
- [verified] Non-determinism is handled by counting, not by hoping:
  pass@k (at least one of k trials passes) and pass^k (all k pass).
  The article's example: a 75 percent task run three times passes
  all three only about 42 percent of the time.
- [verified] Size: "20-50 simple tasks drawn from real failures is a
  great start."
- [verified] "It's often better to grade what the agent produced, not
  the path it took"; checking a rigid sequence of steps gives "overly
  brittle tests".
- [verified] Conversational agents often "require a second LLM to
  simulate the user"; success is then judged on the end state, on
  constraints over the transcript and on rubric-scored quality.
- [verified] Known ways an eval misleads: an ambiguous task, a
  broken task (a zero pass rate over many trials "is most often a
  signal of a broken task"), shared state between trials, grading
  stricter than the instructions, a one-sided problem set (only
  cases where the behaviour should occur).
- [verified] Evals are one layer among several: production
  monitoring, A/B tests (need days or weeks and enough traffic), user
  feedback, manual transcript review, human studies. "No single
  evaluation layer catches every issue."

Source: Anthropic platform docs, "Define success criteria and build
evaluations" (no date on the page),
https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

- [verified] Principles: task-specific, automated where possible, and
  volume over polish ("more questions with slightly lower signal
  automated grading is better than fewer questions with high-quality
  human hand-graded evals").

Status: **consensus** across Anthropic, OpenAI and Google (findings
2 to 5): start small from real failures; deterministic checks first,
a model judge only where code cannot decide; several trials per case;
a clean isolated environment per trial; read the transcripts.

### 2. What Claude Code offers

**`claude plugin eval`.** Source: Claude Code docs, "Test plugins
with evals" (full text; no date on the page, the feature needs
v2.1.269 or later), https://code.claude.com/docs/en/plugin-evals.md

- [verified] The command "runs your plugin against a suite of test
  cases and scores the results". Its stated uses include to "catch
  regressions when you change the plugin or a new model is released".
- [verified] A case is a directory under `evals/` with a `prompt.md`
  and graders. Six grader types: `regex`, `tool_used`, `tool_order`,
  `file_exists` (computed, free), `llm` and `baseline` (a judge model
  votes; two of three votes pass). "There are no custom-code
  graders."
- [verified] Each case runs three times by default; a case passes
  when its mean score meets `--threshold` (1.0 by default). Each run
  is repeated without the plugin, and the difference shows what the
  plugin contributed.
- [verified] CI use is documented: `--json`, exit codes, a cost
  ceiling (`--max-cost-usd`), and the advice to pin both models "so a
  model rollout isn't mistaken for a plugin regression".
- [verified] A case can continue an earlier conversation:
  `context.history_file` names a saved transcript and "the case's
  prompt becomes the next user turn". A `baseline` grader compares a
  run with a reference transcript by judge.
- [verified] Isolation, and the limit that matters most here:
  "Nothing personal or project-level loads. ... no `.claude/`
  directory, `CLAUDE.md`, or `.mcp.json` loads from above the
  workspace or inside it". Only what ships in the plugin under test
  is present.
- [verified] On native Windows there is no sandbox backend, so a
  suite that grants Bash or PowerShell is refused there: "run
  shell-granting suites under WSL2".
- [verified] `file_exists` counts only files created in the run; a
  file that was only edited is invisible to it and must be graded by
  its contents.
- [verified] The doc's own example: one case, six runs, 74 seconds,
  an estimated 0.41 USD. It warns that a usage or rate limit hit
  midway makes later runs score zero and "can look like a
  regression".

**The skill-creator's evals.** Sources: Claude Code docs, "Skills"
(no date), https://code.claude.com/docs/en/skills.md ; Agent Skills
site, "Evaluating skill output quality" (full text, no date),
https://agentskills.io/skill-creation/evaluating-skills ; Anthropic
blog, published 2026-03-03,
https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

- [verified] The skill-creator plugin keeps cases in
  `evals/evals.json` inside a skill, runs each case in a subagent
  with a clean context, with and without the skill, grades assertions
  with evidence, aggregates a benchmark, compares two versions blind,
  and tunes the description against should-trigger and
  should-not-trigger prompts. It runs inside a Claude Code
  conversation; it is an authoring loop, not a CI gate. The two tools
  do not read each other's files.
- [verified] The docs' general method for any skill: "run each one in
  a fresh session with the skill available and again with it turned
  off"; a project skill is turned off through `skillOverrides`.
- [verified] agentskills.io: start with two or three cases, add
  assertions after seeing the first outputs, use a script for
  mechanical checks ("scripts are more reliable than LLM judgment"),
  keep a human review beside the grades, and drop assertions that
  pass with and without the skill.
- [verified] The blog's reason for evals: "a skill that worked well
  last month might behave differently today". It separates
  capability-uplift skills, which a better model may make obsolete,
  from encoded-preference skills, which stay as long as they are
  faithful to the process.

**Headless runs.** Source: Claude Code docs, "Run Claude Code
programmatically" (full text, no date),
https://code.claude.com/docs/en/headless.md

- [verified] Without `--bare`, `claude -p` "loads the same context an
  interactive session would", including the project's hooks; with
  `--bare` it skips hooks, skills, commands, subagents, memory and
  `CLAUDE.md`.
- [verified] "`--bare` is the recommended mode for scripted and SDK
  calls, and will become the default for `-p` in a future release."
- [verified] Skills and custom commands work in `-p`: "Include
  `/skill-name` in the prompt string".
- [verified] Several turns are scripted with `--continue` or
  `--resume <session id>`. `--output-format stream-json` gives the
  whole transcript as events, subagent messages included
  (`--forward-subagent-text` adds their text); `--output-format json`
  reports `total_cost_usd`. `--permission-prompts none` removes the
  tools that need a person, `AskUserQuestion` among them.

**The Agent SDK.** Source: Claude Code docs, "Agent SDK overview"
(full text, no date),
https://code.claude.com/docs/en/agent-sdk/overview.md

- [verified] The SDK runs the Claude Code binary from Python or
  TypeScript with sessions, hooks and permissions; its table says
  skills, commands and memory "load automatically from your project's
  `.claude/`". A third-party tool's docs (finding 4) say the opposite
  default for its own SDK provider; which holds depends on version
  and options and is **uncertain** here.

**Pinning.** Sources: Claude Code docs, "Model configuration"
(no date), https://code.claude.com/docs/en/model-config.md ;
"Advanced setup" (full text, no date),
https://code.claude.com/docs/en/setup.md

- [verified] Aliases "update over time. To pin to a specific version,
  use the full model name".
- [verified] Claude Code itself updates in the background by default.
  The `stable` channel is "typically about one week old, skipping
  releases with major regressions"; a specific version can be
  installed, auto-update disabled, and a version range enforced by
  managed settings.

Status: **emerging**. The plugin eval command and the skill-creator's
evals are both from 2026; their formats differ and neither tests a
project's own `CLAUDE.md`.

### 3. What other vendors publish

- [verified] OpenAI, "Testing Agent Skills Systematically with Evals"
  (no date on the page), https://developers.openai.com/blog/eval-skills
  : define success before writing; a small set of 10 to 20 prompts,
  with negative controls where the skill should not fire; run the
  agent headless with a JSON event stream and check it by code ("the
  value here is that everything is deterministic and debuggable");
  then a rubric pass with a structured output schema; "let real
  failures drive coverage". The page says nothing on flakiness or
  cost.
- [verified] OpenAI, agent evals guide (no date),
  https://developers.openai.com/api/docs/guides/agent-evals : start
  from grading traces, then move "from individual traces to
  repeatable datasets and eval runs".
- [verified] Google ADK, "Evaluate" (no date),
  https://adk.dev/evaluate/ : test files for single sessions during
  development, evalsets for longer multi-turn sessions; it scores the
  tool trajectory against an expected one (default threshold 1.0,
  an exact match) and the final response (default 0.8); a model can
  generate the user's turns for a conversation scenario; runs from a
  CLI, a web UI or pytest.
- [verified] Microsoft Foundry, "Agent evaluators" (ms.date
  2026-09-25),
  https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators
  : built-in judge-model evaluators, "like unit tests for agentic
  systems", split into system evaluation (task completion, task
  adherence, intent resolution) and process evaluation (tool
  selection, tool input accuracy and others); many are marked
  preview. They take recorded messages as input, so they grade a
  transcript and do not run the agent.

Status: the method is **consensus**; one point is **contested**:
Google scores the path against an expected trajectory by default,
Anthropic advises against grading the path.

### 4. Open tools and what they fit

- [verified] promptfoo, "Evaluate coding agents" (updated
  2026-10-02),
  https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/ and
  its Claude Agent SDK provider page (no date),
  https://www.promptfoo.dev/docs/providers/claude-agent-sdk/ : a YAML
  suite that runs the Claude Agent SDK or Codex; a fresh copy of a
  working directory per test (`copy_working_dir`); assertions over
  the tool trajectory, a `skill-used` assertion, a model rubric, cost
  and latency, and custom JavaScript; `--repeat 3` to measure
  variance ("if a prompt fails 50% of the time, the prompt is
  ambiguous"); session resume for several turns; a canned answer to
  `AskUserQuestion`. By default the provider "does not look for
  settings files, CLAUDE.md, or slash commands"; `setting_sources:
  ['project', 'local']` turns that on. Fit: the closest open tool to
  a project that lives in `CLAUDE.md` and `.claude/`.
- [verified] Inspect (UK AI Security Institute and Meridian Labs),
  https://inspect.aisi.org.uk/ : dataset, solver, scorer; sandboxes
  in Docker and others; runs "arbitrary external agents like Claude
  Code, Codex CLI, and Gemini CLI"; model-graded scorers; a log
  viewer. Fit: research-grade suites; heavy for a handful of
  scenarios [synthesis].
- [verified] DeepEval, https://deepeval.com/docs/getting-started-agents
  : pytest-style agent metrics, but the agent must be instrumented in
  Python (`@observe`). Fit: agents written as code, not a CLI agent
  driven by instruction files [synthesis].
- [verified] LangSmith, multi-turn simulation (no date),
  https://docs.langchain.com/langsmith/multi-turn-simulation : a
  simulated user played by a model, or fixed responses; its own
  caveat: "there is less consistency than evaluating a single output
  from your app given a static input".

### 5. How comparable frameworks test their own prompts

Read from the repositories on 2026-10-03; a thing not seen in a
listing is reported as not seen, not as absent.

- [verified] GitHub Spec Kit, `CONTRIBUTING.md`,
  https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md :
  pytest covers code that "runs or controls execution without an
  LLM". For the prompts the rule is manual: "Any change that affects
  a slash command's behavior requires manually testing that command
  through a coding agent and submitting results with the PR".
- [verified] Superpowers, `docs/testing.md`,
  https://github.com/obra/superpowers/blob/main/docs/testing.md :
  two layers. Plugin tests in `tests/` for the code without a model.
  Skill behaviour evals through a harness named Quorum: "real LLM
  sessions of Claude Code / Codex / Gemini CLI, with an LLM actor and
  verifier judging skill compliance", plus deterministic post-checks.
  "Quorum scenarios are slow (3-30+ minutes each) and run real LLM
  sessions in permissive modes"; "only the static gates ... are safe
  for public CI; the natural follow-up remains a tiered model (static
  gates on PR, live sweep nightly + on-demand)". Where the eval
  scenarios live could not be confirmed: the repository listing shows
  no `evals/` directory and the page speaks of a separate eval lab,
  which was not found at the address tried.
- [verified] Superpowers, the skill
  `writing-skills/testing-skills-with-subagents.md` (raw file on
  `main`): test-driven writing of a skill. Run the scenario without
  the skill and record how the agent fails, write the skill against
  those failures, then close the loopholes. "If you didn't watch an
  agent fail without the skill, you don't know if the skill prevents
  the right failures." Scenarios combine pressures (time, sunk cost,
  authority). Skills that are pure reference need no such test.
- [verified] BMAD Method, `CONTRIBUTING.md`,
  https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CONTRIBUTING.md
  : a validator of file references
  (`uv run tools/validate_file_refs.py --strict`) and a line in the
  PR template on how the change was tested. No model-run test of
  agent behaviour was seen in the contributing guide or in the
  top-level listing.
- [verified] OpenSpec, `test/` listing,
  https://github.com/Fission-AI/OpenSpec/tree/main/test : unit and
  end-to-end tests of the CLI, and tests named `*-docs-claims` and
  `vocabulary-sweep`, which by their names check the documents
  against the code. No model-run test was visible by file name.

Status [synthesis]: among comparable frameworks, static checks of the
files are **common**, a manual run before a merge is the **norm**,
and a live behavioural suite is **rare** (one of four, and that one
not in public CI). Nobody surveyed gates every change on live model
runs.

### 6. The techniques, one by one

| Technique | Can prove | Cost and upkeep | Flakiness | Known not to work |
|---|---|---|---|---|
| Static checks of the instruction files | references resolve, front-matter parses, nothing is stated twice | near zero | none | says nothing about conduct |
| Deterministic checks on produced files | the outcome: what was written, where, in what shape | low; one fixture and assertions per scenario | only the agent's, not the grader's | brittle if it pins exact wording |
| Checks over the transcript (tool used, order, absence) | a rule of process was kept: a skill fired, a tool was never called | low | low | a required sequence of steps breaks on valid variation (Anthropic) |
| Model-graded rubric | qualities code cannot see: tone, one item per message, a question asked rather than assumed | judge calls; needs calibration by reading transcripts | the judge varies, more on long text (plugin-evals doc) | vague rubrics; a small judge marking format, not substance |
| Scripted user (fixed turns) | a multi-turn path under known answers | low to run; scripts break when the flow legitimately changes | moderate: the agent may ask something the script did not foresee | long scripts |
| Simulated user (a model plays the user) | robustness over many conversational paths | highest; two models per run | highest (LangSmith's own caveat) | as a release gate |
| Golden transcript | as a starting point for the next turn, or as a reference for a judge | low | n/a | exact comparison of a new run with a stored one |
| Regression suite per release | what passed still passes | grows with every case; needs an owner | handled by several trials and a threshold | a threshold of 1.0 on judged cases |
| Pinning the model and the harness | separates "we changed" from "they changed" | none | n/a | pinning for ever: the pin expires and users run the new model anyway |
| Staged release of an instruction change | real use on a few before all | needs users and a channel | n/a | A/B needs traffic (Anthropic) |

Marks for the table: the first, fourth, fifth, sixth and ninth rows'
last column and the whole seventh row are [synthesis] from findings
1 to 5; the rest restates [verified] findings above.

Pin versus track is **contested** only in appearance [synthesis]:
the sources that speak of it ask for both, a pinned model for the
gate and a second run on the new model when one ships.

## Options with trade-offs

All [synthesis], built on the findings above.

**A. Static checks only.** What the forge already has in its checks
(conformance of the operating layer with itself). Proves the files
agree, not that the model obeys them. Cost nil. Would not have caught
a change of conduct.

**B. A handful of scripted scenarios with file-level assertions,
run by hand before a release.** A script (Python, per the forge's
own rule for new scripts) copies a small fixture project to a
throwaway directory, drives the real engine through `claude -p`
without `--bare` so that `CLAUDE.md`, the skills, the agents and the
per-prompt hook load, sends the scripted turns with `--resume`, saves
the `stream-json` transcript, and asserts on the files and on the
transcript. Each scenario runs three times. Proves that the rules
whose breach leaves a trace still hold. Cost: minutes and a few
dollars per run by the figures above, unmeasured for the forge;
upkeep is one fixture and one script per scenario. Flakiness is the
agent's only. Limits: a fixed script cannot follow an agent that asks
an unforeseen question; it sees no quality of elicitation.

**C. B plus a judge for what code cannot see.** A second model reads
the saved transcript against short PASS and FAIL conditions (one item
per message, the verdict line present, a question asked where a gap
was planted, a reflection before the write). Adds judge cost and the
duty to read transcripts until the judge is trusted. Advisory, not a
gate.

**D. Package the engine as a plugin and use `claude plugin eval`.**
Buys the built-in harness: isolation, three runs, baseline, report,
CI exit codes, cost ceiling. Does not fit today: project `CLAUDE.md`
and `.claude/` are not loaded in a run, so the always-loaded core
would have to ship inside the plugin; shell-granting suites do not
run on native Windows; no custom-code graders. It becomes the natural
choice if the engine split delivers the engine as a plugin.

**E. promptfoo over the Agent SDK.** An open harness that can load
project settings, copy the working directory per test, repeat, and
mix code, trajectory and rubric assertions. Buys reporting and
caching for the price of a Node dependency and a third party's
provider between the forge and Claude Code.

**F. A graded suite in CI with a simulated principal.** Scenario
sweeps nightly, a model playing the principal, trend charts. The
only option that explores paths nobody scripted. The one comparable
framework that has it keeps it out of public CI and reports 3 to 30
minutes per scenario. Too much for a framework with a handful of
users.

**Across all: pin and re-run.** Keep the gate on a pinned full model
name; when a new model or a new Claude Code version arrives, run the
same suite once against it before adopting it. The `stable` channel
gives about a week of distance from a regressed harness release.

## Relevance to this project

What would be tested [verified by reading the engine]: an
always-loaded `CLAUDE.md`, some twenty skills (one per command, three
reviewer contracts, the walkthrough method), eight agents, a
per-prompt hook, scripts. The forge differs from the frameworks
surveyed in one respect that shapes the choice [synthesis]: its
conduct is conversational and gated on the principal's word, so most
of its rules are about what happens *between* turns (nothing written
before `write`, one version per round, one item per message), not
about one prompt and one answer. Single-turn eval tools cover the
triggering of a skill; they do not cover a round.

**Recommendation: option B, the smallest thing that would have caught
a regression**, with the pin-and-re-run rule. Reasons:

- The rules most costly to lose are the ones that leave a trace in
  files or in the transcript, and so can be checked by code, the
  cheapest and least flaky grader: no file changed before the
  confirmation; one version bump for a round, with its history
  records appended and `last_change` derived; a reviewer's report
  filed where the command says and its ledger row written; no git
  call outside the scripts; the skill invoked for its command; a
  check that finds nothing files nothing.
- It tests the engine as users run it, `CLAUDE.md` and hook included,
  which neither Claude Code eval tool does today.
- It follows the consensus: start from real failures, a few cases,
  three trials, outcome over path. The scenarios should be the
  failures already met in use, not an inventory of every rule.
- It is the first layer of every larger option: the same scenarios
  and assertions carry over to C, D or E unchanged in substance.

What it will not catch, to be said plainly: the quality of
elicitation and of the reviewers' findings, drift in long real
sessions, and anything nobody wrote a scenario for. Those stay with
use, and with option C when it is wanted.

Three risks to carry [verified facts, synthesis as risk]: `--bare` is
announced as the future default of `-p`, so the harness must state
the loading it relies on rather than inherit it; a usage limit hit
mid-suite looks like a regression; the scripted turns must be few,
because a script is the part that breaks when the flow changes for
good reasons.

Open for the principal, not decided here: when the suite runs (before
every release, or only on a change of the operating layer and on a
new model or harness); whether a failed scenario blocks, given that
the forge's reviewers are advisory; and whether the engine split
makes option D the target.

## What stays uncertain

- Whether the Agent SDK loads project settings by default: the Claude
  Code overview and promptfoo's provider page disagree.
- Where Superpowers' eval scenarios live and how its simulated user
  is built; only the summary page was read.
- BMAD and OpenSpec were read from listings and one guide each; a
  behavioural suite elsewhere in those repositories is not excluded.
- No cost or duration figure for the forge's own scenarios exists;
  the figures cited are other projects' examples.
- How `claude plugin eval` and the skill-creator's evals will
  converge, and whether either will load a project's `CLAUDE.md`.
