---
project: forge
type: research
topic: how Claude Code can run the forge's reviewers and file their reports without the working conversation taking part
date: 2026-10-02
derived_from: 10-intent.md v4.42 (POS.0400, POS.0540, POS.1120, POS.1140); the principal's question of 2026-10-02 during the walkthrough of a check report
status: immutable
---

# Running the reviewers and filing their reports without the conversation

## Question

The forge has three kinds of isolated reviewer: critic, challenger,
check. Today the session launches each with the Agent tool; a critic
and a challenger write their own report and ledger rows, a check
returns its report to the session and files nothing. The principal
wants one mechanism for all three, with the findings of a check filed
like any other, and asked whether the whole mechanism can leave the
session: a command told which reviewers to run, which runs them,
files the reports, numbers the findings and updates the ledger,
without the conversation's context.

What does Claude Code offer for that today? Docs fetched live on
2026-10-02 from `code.claude.com/docs` (pages name versions up to
v2.1.271; none carries a date). The reference of the workflow runtime
was read from the bundled skill `workflow-authoring` of the running
harness. Epistemic tags: [V] verified on the page or in the bundled
reference, [S] the docs are silent and this is inferred, [O] observed
in the forge's own session, not documented.

## Answer in one paragraph

Yes, and in more than one way. Four mechanisms can launch reviewers
without the conversation: a skill that runs as an isolated agent, a
saved workflow, a hook that fires when a reviewer finishes, and a
script outside the harness. They are not rivals: the mechanism has
two jobs that separate cleanly. Launching needs a model or a runtime;
filing (the next free ID, the report file, the ledger row) is
bookkeeping and needs neither, so it belongs to a script whichever
launcher is chosen. The one mechanism that takes filing out of every
model is the `SubagentStop` hook: it can match a reviewer by its
agent name and receives the reviewer's final message, so the harness
itself can hand the report to the script. That requires the reviewer
to return its whole report as its final message, which the check does
today and the critic and the challenger do not.

## Findings

### 1. A subagent may launch subagents

- [V] "By default, a subagent can spawn subagents of its own, up to
  three layers below the main conversation. At the depth limit,
  Claude Code withholds the `Agent` tool from every subagent except a
  fork." The limit is `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`.
  (`sub-agents`)
- [V] "To keep one subagent from spawning while nesting is on, such
  as a reviewer that should stay read-only, omit `Agent` from its
  `tools` list." The forge's reviewers already do. (`sub-agents`)
- Bearing: a runner agent on the first layer can launch the reviewers
  on the second. The forge's own record of 2026-09-06 set
  `context: fork` aside because the field fixes one agent type and
  cannot choose a reviewer by argument (POS.1140); with nesting the
  fixed agent is the runner, and the runner chooses.

### 2. A skill can run as an isolated agent

- [V] "Add `context: fork` to your frontmatter when you want a skill
  to run in isolation. Claude Code starts a new subagent of the type
  set in the `agent` field and gives it the skill content as its
  prompt." "The subagent doesn't see your conversation history."
  (`skills`)
- [V] The `agent` field takes "built-in agents (`Explore`, `Plan`,
  `general-purpose`) or any custom subagent from `.claude/agents/`".
  (`skills`)
- [S] The docs do not say whether the value can be chosen at
  invocation, nor whether a forked skill may launch subagents; by
  finding 1 it may where its agent's `tools` carry `Agent`.

### 3. What a subagent starts with

- [V] "Each subagent starts with a fresh, isolated context window. It
  doesn't see your conversation history, the skills you've already
  invoked, or the files Claude has already read." Its context holds
  its own system prompt, the task message, and every CLAUDE.md the
  main conversation loads, `CLAUDE.local.md` included.
  (`sub-agents`)
- [V] `skills`: "Skills to preload into the subagent's context at
  startup. The full skill content is injected." (`sub-agents`)
- [S] Whether `skills` preloads when the agent runs as the main
  session through `claude --agent` is not stated. The forge recorded
  on 2026-09-06 that a headless `--agent` run preloads nothing
  (POS.1120); nothing found today contradicts it.

### 4. Workflows

- [V] "The workflow runtime executes the script in an isolated
  environment, separate from your conversation. Intermediate results
  stay in script variables instead of landing in Claude's context."
  (`workflows`)
- [V] "No direct filesystem or shell access from the workflow itself.
  Agents read, write, and run commands. The script coordinates the
  agents." (`workflows`)
- [V] A saved script lives in `.claude/workflows/` and "runs as
  `/<name>`"; it takes input through `args`. (`workflows`)
- [V] An `agent()` call can name a custom agent type: `agentType`
  "uses a custom subagent type ... resolved from the same registry as
  the Agent tool". This stands in the bundled reference only; the
  docs page does not mention the option.
- [V] A run needs approval: in manual and accept-edits modes at every
  run unless "don't ask again" was chosen for that saved workflow;
  `Workflow(<name>)` as a permission rule approves one by name.
  (`workflows`)
- [V] Dynamic workflows are a feature of paid plans, switched on in
  `/config` on Pro, and can be turned off by a setting or by an
  organisation. The page names behaviour changes across v2.1.202 to
  v2.1.271. (`workflows`)
- [V] No timestamps inside a script; a date is passed in through
  `args`. (bundled reference)

### 5. A hook fires when a subagent finishes

- [V] `SubagentStop` takes a matcher on the agent type, with the
  values of `SubagentStart`: "`general-purpose`, `Explore`, `Plan`,
  custom agent names". (`hooks`)
- [V] "Hooks that need the final assistant text of the current turn
  should use `last_assistant_message` on Stop and SubagentStop
  instead of reading the transcript." (`hooks`)
- [S] The full input of `SubagentStop` is not laid out on the page.
  The Agent SDK page shows `agent_id` and `agent_transcript_path`.
  Whether the message arrives whole however long it is, whether the
  hook fires for a reviewer launched from a nested agent or a
  workflow, and what it receives when a reviewer is stopped half-way
  are not stated.

### 6. Outside the harness

- [V] `claude -p --agent <name>` runs an agent as the session, with
  `--output-format json` or `stream-json` for a script to capture the
  result. (`cli-reference`)
- [V] The Agent SDK loads `.claude/agents/` and `.claude/skills/`
  when `settingSources` includes `project`, and preloads skills into
  a subagent through its `skills` field. (`agent-sdk/typescript`)
- Bearing: a script would need the preload that finding 3 leaves
  open, or a Node or Python program as a new dependency of the
  engine (POS.0830 keeps `scripts/` to PowerShell), and runs under
  whatever login the calling shell has, which has failed the forge
  once (POS.1150).

### 7. A subagent writing its own report

- [S] The docs name no rule that keeps a subagent from writing a
  file; background subagents have `Write` and `Edit`.
- [O] On 2026-10-01 a general-purpose subagent of this session, told
  to write its report to a file, was refused with "Subagents should
  return findings as text, not write report files". Whether the same
  meets a reviewer with `Write` in its own `tools` is untested; the
  last critic run that wrote its report was on 2026-09-06.
- [O] Nothing stops two reviewers of one kind from running at once,
  and each takes the next free ID and edits the ledger itself. It has
  not collided because it has not been done.

## Options

Filing is the same in all four: a script of the engine takes a
report, gives its findings the next free IDs under a lock, writes the
dated file and the ledger rows. The options differ in what launches
the reviewers and what calls the script.

| | Launches | Calls the script | For | Against |
|---|---|---|---|---|
| A. Hook | the dispatchers of today, through the Agent tool, the path and nothing else | the harness, at `SubagentStop`, matched by agent name | no model touches the filing; works whoever launched the reviewer and however many run at once; the smallest change | the input of the hook is only partly documented and must be tried; a reviewer stopped half-way must be told from one that finished |
| B. Forked skill | a runner agent started by a skill with `context: fork`, which launches the named reviewers | the runner, one report after another | one command for every reviewer, told which to run; the session receives a summary only | the runner is a model following a procedure; every report passes through its context; one more layer of agents |
| C. Workflow | a saved script, each reviewer by `agentType` | an agent at the end of the script | the fan-out is code, resumable, in the background | the script cannot write, so the filing still needs an agent; approval at each run; a feature of a plan that can be switched off; a young interface |
| D. Script | `claude -p` or the Agent SDK | the same script | nothing of the session at all | the contract preload is unproven without the SDK; a new dependency with it; the login of the shell |

A and B are not exclusive: with the hook doing the filing, a runner
has nothing left to do but launch.

## Relevance to this project

Recommendation: separate the two jobs, and build the filing first.

1. A script of the engine files a report: IDs, file, ledger rows, one
   run at a time. It serves critic, challenger and check alike, and
   it is what makes two reviewers at once safe.
2. Every reviewer returns its whole report as its final message and
   writes nothing. The three contracts change in their Output
   section; the agents lose `Write` and `Edit`.
3. The hook of option A calls the script. Before it is built, one
   trial settles what the docs leave open: what `SubagentStop`
   receives for a forge reviewer, whether the message is whole, and
   whether it fires for a reviewer run in the background. If the
   trial fails, the dispatcher calls the script itself with the text
   the reviewer returned; nothing else in the design changes.
4. One command for every reviewer (option B) is a second step and a
   matter of its own, beside the question of one dispatcher or two
   (THR.0460) and of how a new type is added (THR.0480). It is not
   needed for the findings of a check to be filed.

What this note does not settle: the name of the script and of the
command, how a report marks the findings the script is to number, and
whether a run of a check that finds nothing leaves a file. Those are
the principal's.

## Sources

- https://code.claude.com/docs/en/sub-agents.md
- https://code.claude.com/docs/en/skills.md
- https://code.claude.com/docs/en/workflows.md
- https://code.claude.com/docs/en/hooks.md
- https://code.claude.com/docs/en/cli-reference.md
- https://code.claude.com/docs/en/agent-sdk/typescript.md
- https://code.claude.com/docs/en/agent-sdk/hooks.md
- the bundled skill `workflow-authoring` of Claude Code, as loaded in
  the session of 2026-10-02

The last three pages were read through an agent of the session and
not re-fetched; the first four were fetched again and the quotes
above checked against them.
