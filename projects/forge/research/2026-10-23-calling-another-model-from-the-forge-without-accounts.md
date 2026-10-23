---
date: 2026-10-23
project: forge
topic: calling another model from the forge without accounts
status: immutable
derived_from: the principal's word of 2026-10-23 (the forge is to send a critic, a challenger or a free question into Gemini and other models, logged in once outside the forge, the forge carrying no account, one mechanism for several engines if it can be had; CLI, library or MCP all allowed); 10-intent.md v5.30 (POS.0550, POS.0790, POS.0800, POS.0830, POS.0950, POS.1140, POS.1200); scripts/forge_tools.py (claude_headless, the one call of a model CLI the forge makes today); the three Gemini challenges of 2026-10-22 in sources/ (repo-detection-challenge*.md, the manual door); web sources below
---

# Calling another model from the forge without accounts

## Question

How does a Python script of the forge send a prompt and a set of
files to a model of another family - Gemini first, others later -
and get a Markdown answer back, when the user has logged into that
model once outside the forge and the forge itself carries no key, no
account name and no configuration? Which of the three roads - a
command-line tool on PATH, a library, an MCP server - meets that,
and does one of them give a shape that would carry a second and a
third engine without a second mechanism? Companion of
`2026-10-23-a-reviewer-or-a-question-on-another-model-inside-the-forge.md`,
which says what the forge does with the call.

The baseline is the manual door of 2026-10-22: the principal pasted
a question into Gemini, pasted the answer back, and the forge stored
it as a source. Anything proposed here must beat that in effort and
lose nothing of it in provenance.

## Key findings

**F1. Gemini CLI is no longer the Gemini door for a person; Antigravity
CLI (`agy`) is.** [verified, Google's announcement in the Gemini CLI
repository, discussion #27274, 2026-05-19; the banner of
geminicli.com, updated 2026-06-18] On 2026-06-18 Gemini CLI "stopped
serving requests" for Google AI Pro and Ultra subscribers and for
users of the free tier; they are moved to Antigravity CLI, "built in
Go", with "Agent Skills, Hooks, Subagents, and Extensions (now
Antigravity plugins)" retained and "asynchronous background
workflows" added. Gemini CLI stays Apache 2.0 and keeps working for
Gemini Code Assist Standard and Enterprise licences and for paid
Gemini API keys. A person with a Google account, free or paid, is
therefore on `agy`; a company with Code Assist or an API key may be
on either. Third-party guides written before June still describe
`gemini -p` as the way; they are stale for the principal's case.

**F2. Antigravity CLI has a headless mode built for scripts.**
[verified, antigravity.google/docs/cli/headless and
/docs/cli/reference] `agy -p "<prompt>"` (aliases `--print`,
`--prompt`) runs one prompt and exits. `--output-format text | json |
stream-json`; the `json` envelope carries `conversation_id`,
`status` (`SUCCESS`, `ERROR`, `CANCELED`, `INTERRUPTED`, `INVALID`,
`WAITING`, `RUNNING`), `response`, `error` on failure,
`duration_seconds`, `num_turns`, `usage` with token counts, and
`structured_output` when `--json-schema` is given (a schema string,
a path to a `.json` file, or a primitive type name). A successful
run exits 0, a failed one non-zero with the reason on stderr; an
unknown `--model` exits 1 instead of falling back. `--add-dir
<path>`, repeatable, adds a directory to the workspace; without it
the agent works in a scratch workspace under
`~/.gemini/antigravity-cli/scratch/` [third-party cheat sheet,
unverified]. `--model <slug>` with `agy models` listing the slugs,
`--effort low | medium | high | max`, `--agent <name>` with `agy
agents`, `--continue` and `--conversation <id>` to resume,
`--disable-slash-commands` so that a prompt's `/word` is not
expanded, `--sandbox` for OS containment where available,
`--dangerously-skip-permissions` to approve every tool call,
`--log-file`. Settings live in
`~/.gemini/antigravity-cli/settings.json`, with scoped allowances
under `permissions.allow` such as `command(git)`. The two official
pages disagree on `--print-timeout`: the headless page says the
default is five minutes, the reference says `0s`, wait until the
turn completes; a script sets it explicitly. No `@file` syntax and
no stdin prompt are documented for `agy`; the prompt is the flag's
argument and the files are read by the agent from the workspace.
What happens in headless mode to a tool call that would ask for
permission, when `--dangerously-skip-permissions` is not given, the
pages do not say [unverified; to be tried: the expected behaviour is
a denial, and the forge should test it on a throwaway copy before it
relies on a read-only run].

**F3. The login is the user's, made once, and the forge sees nothing
of it.** [verified, antigravity.google/docs/cli/headless and
/docs/getting-started] "Authenticate once with an interactive `agy`
session first"; headless runs "reuse cached credentials", and a run
with none "exits with an authentication required error" instead of
hanging, so a script can tell a missing login from a slow answer.
The migration guide says session tokens are kept in the operating
system's keyring. Four auth kinds exist: `oauth-personal`
(personal Free, Pro and Ultra plans), `oauth-business` (Gemini
Enterprise, preview, with a GCP project and location),
`gemini-api-key`, and `agent-platform` (API key or ADC). This is
exactly the shape the principal asked for: the same as git's
identity, resolved on the machine, named nowhere in the forge.

**F4. The quota is metered on the agent's work and is not knowable
before a run.** [verified in part: the plans ride on Google AI
subscriptions, a vendor blog of 2026-05 and the official credits
page; the windows and the lockouts are forum reports, unverified]
There is no Antigravity-only subscription; paid quota comes with
Google AI Pro and Ultra, free quota with a free account; the CLI's
credits page says the CLI "integrates with your subscription to
monitor and manage your AI Premium credits and usage quotas" and a
setting decides whether personal credits are drawn "when plan quotas
are exhausted". Limits meter agent work performed, not prompts
sent, and refresh in five-hour windows under a weekly cap [vendor
blog]; forum threads report lockouts of days. For the forge this
means a run's price is reported after, never promised before: the
`usage` field of the JSON envelope is the one number the forge can
record.

**F5. On Windows, `agy -p` under a pipe was broken until 1.1.1.**
[verified, issue #76 of google-antigravity/antigravity-cli, opened
2026-05-21, closed 2026-07-12] On 1.0.0 to 1.0.16, chiefly on
Windows 11, `agy -p` with stdout redirected or piped printed nothing
and exited 0; on macOS and WSL it hung. The causes were a console
redirect for the terminal renderer and a read of stdin even when the
prompt came from the flag; 1.0.15 fixed the first, 1.1.1 the second
and also made a server-side failure exit non-zero with the error on
stderr instead of a silent success. Lessons for a script: require
`agy` 1.1.1 or newer and say so, start the process with stdin
closed, read `status` in the JSON envelope and never trust exit 0
with an empty answer, and keep `--print` as the last flag because it
takes the next token as its prompt.

**F6. Codex CLI has the same shape under other names.** [verified,
OpenAI's non-interactive page, learn.chatgpt.com] `codex exec
"<prompt>"` streams progress to stderr and prints only the final
message to stdout; `--json` turns stdout into JSON Lines events
(`thread.started`, `turn.completed`, `item.*`, `error`); `-o <path>`
writes the final message to a file; `--output-schema <file>` asks
for a final answer that conforms to a JSON Schema; `--ephemeral`
leaves no session file on disk. It "reuses saved CLI authentication
by default", the ChatGPT login made once; `CODEX_API_KEY` is the
alternative, which OpenAI calls the right default for CI and the
forge does not need. The default sandbox is read-only, which is what
a reviewer wants; `--sandbox workspace-write` opens it. Codex insists
on a git repository and needs `--skip-git-repo-check` elsewhere.
Piped stdin becomes context beside the prompt, `codex exec -` makes
it the whole prompt. `codex exec resume --last` continues.

**F7. Claude Code is the third of the kind, and the forge already
calls it.** [verified, code.claude.com/docs/en/headless;
scripts/forge_tools.py, `claude_headless`] `claude -p "<prompt>"`
with `--output-format json` gives `result`, `session_id`,
`total_cost_usd` and a per-model cost breakdown; `--json-schema`
puts a conforming object in `structured_output`; `--append-system-
prompt` adds instructions, `--allowedTools` and `--permission-mode`
set what it may do, stdin is read up to 10 MB, exit 0 on success and
non-zero on failure, with a failure inside the run printed as the
result. Two facts matter for the forge: `--bare`, the recommended
mode for scripts and soon the default of `-p`, "doesn't use your
subscription login" and needs `ANTHROPIC_API_KEY`, so a script that
rides on the user's Claude subscription must not pass `--bare` and
then inherits the hooks, skills and CLAUDE.md of the directory it
runs in - which is what `/publish` lives with today; and a `-p`
session without `--bare` connects a project's MCP servers and runs
its hooks without a trust dialog. A run on the forge's own tree
would load the forge's CLAUDE.md and hooks; the same-family case is
of no interest here, but the fact fixes a rule: the external engine
is given the files it needs, never the forge as its workspace with
everything that executes.

**F8. GitHub Copilot CLI is a fourth, and the one that chooses the
model.** [verified for `-p` and `--model`, docs.github.com; the
model list unverified] `copilot -p "<prompt>"` runs non-interactively
and exits; `--model` picks among the models the plan allows, Claude
and GPT models named in the docs, Gemini not confirmed; the login is
GitHub's. It is a door to several families through one login, which
makes it a candidate the day the principal has that subscription.

**F9. The four agree on one shape; the adapter is a table, not a
program per engine.** [mechanism, from F2, F6, F7, F8] Every one of
them takes a prompt as an argument, works in a directory it may
read, runs its own tools, returns a final message, offers a JSON
output with the answer in one field and a schema option, reuses a
login made once on the machine, and signals failure by exit code
and by a field. They differ in the flag that names the extra
directories (`--add-dir`, Codex's `-C` or the cwd, Claude's
`--add-dir`), in the field that carries the answer (`response`,
the last `item` of the JSON Lines, `result`), in how a read-only
run is asked for (Codex's default, Claude's `--allowedTools Read,
Glob,Grep`, `agy` unknown), in the timeout flag and in the exit
codes. An adapter per engine is a dozen lines: the command line,
the field to read, how to say read-only, the version floor. One
script, one table, a word per engine.

| | Antigravity CLI | Codex CLI | Claude Code | Copilot CLI |
|---|---|---|---|---|
| one-shot flag | `agy -p` | `codex exec` | `claude -p` | `copilot -p` |
| login made once | Google account, keyring | ChatGPT login, `~/.codex/auth.json` | Claude account (not with `--bare`) | GitHub |
| JSON answer | `--output-format json`, field `response` | `--json` (JSON Lines) or `-o <file>` | `--output-format json`, field `result` | not documented |
| schema | `--json-schema` | `--output-schema <file>` | `--json-schema` | no |
| extra dirs | `--add-dir` (repeat) | cwd, `-C` | cwd, `--add-dir` | cwd |
| read-only | not documented; test | default sandbox | `--allowedTools` | not documented |
| web search | yes | yes | yes | unverified |
| model | `--model`, `agy models` | `--model` | `--model` | `--model` |
| timeout | `--print-timeout` | none documented | none; `--max-turns` | none documented |
| version floor | 1.1.1 (F5) | - | - | - |

**F10. A library is a raw model call, and the login is the weaker
half.** [verified, Google's genai and Antigravity SDK pages] The
Gemini API through `google-genai` takes `GEMINI_API_KEY` or, with
`vertexai=True`, Application Default Credentials from `gcloud auth
application-default login`; the Antigravity Python SDK
(`google-antigravity`, Python 3.10 or newer) documents the same two
roads and nothing about reusing the CLI's cached login. A key in the
user's environment is the user's and not the forge's, so the letter
of "the forge carries nothing" would hold; but a key is an account
artefact to be made, stored and rotated, which is what the principal
does not want to administer, and the free API tier is thin and
moving (Google has taken the rate tables out of its docs and points
to AI Studio; a claim that Pro models are paid-only on the API since
April is unverified). The deeper difference is that the library
gives a model, not an agent: no file tools, no web search, the forge
assembling the chain into the prompt itself - a path the forge left
behind when it made the reviewers agents that read from disk
(POS.1140). The library road is right for a one-sentence call, not
for a reviewer.

**F11. The MCP servers in the field are the CLI call under a hat.**
[verified by reading the projects' pages; the count is a sample]
Half a dozen community servers expose Gemini to Claude Code
(gemini-mcp-tool, ask-gemini-mcp, antigravity-cli-mcp-slim,
agy-bridge; agy-mcp archived 2026-08-04 in favour of the next) and
every one of them runs `gemini -p` or `agy -p` as a child process
and returns stdout; zen-mcp-server's `clink` does the same for
Gemini, Claude and Codex with role prompts under
`systemprompts/clink/` and presets under `conf/cli_clients/`, its
presets intentionally permissive (`--yolo`, bypass of the sandbox).
What MCP adds is a Node or Python server to install and register per
machine, a tool the session model may call on its own judgement, and
a surface that changes with its maintainer. What the forge needs is
the opposite: a run that starts on the principal's word, through a
script, with the files it names (CLAUDE.md, Isolated reviewers:
"No reviewer runs on Claude's own judgement"). MCP is the right door
when a conversation wants to ask a second model in passing; it is
not the door for a reviewer.

**F12. ACP is the protocol for a longer dialogue, not for a run.**
[verified, agentclientprotocol.com; the Gemini flag from secondary
sources] The Agent Client Protocol is JSON-RPC over stdio between an
editor and an agent, modelled on the Language Server Protocol,
reusing MCP's JSON where it can; Gemini CLI is its reference agent
(`gemini --experimental-acp`, reported stable as `--acp` since
0.50), Codex comes through `codex-acp`, Claude through
`claude-agent-acp`, Copilot in preview; Antigravity CLI is not on
the list of 46 agents; a Python SDK, `agent-client-protocol`,
exists. It gives a session, prompts, streamed updates and
permission requests over a long-lived process - more than a
one-shot needs, and a second protocol layer to keep up with. It is
the road to take if the forge ever wants the external model to ask
questions back during a run; today it is not needed.

**F13. "Send now, collect later" exists nowhere as a shelf part.**
[verified for what is documented; the design is a hypothesis]
Antigravity CLI runs background subagents inside a session and
speaks of asynchronous workflows, but documents no command that
starts a headless run and fetches its result in a later process;
Codex cloud tasks, Claude Code's `--cloud` and Google's Jules are
services bound to a repository and a hosted worker. For a run of
minutes the simple mechanism is the forge's own: start the engine
as a detached subprocess that writes its answer and a status file
into a spool directory, let the forge's map read the spool like any
other state made at read time, and let a command file what has
returned. The same adapter serves both tempos; the difference is a
flag and a spool.

## Options

**A. A CLI adapter in `scripts/`, Python, one table of engines.** The
engine named by a word (`antigravity`, `codex`, `claude`,
`copilot`), found on PATH, the version checked, the login the
user's; the job a prompt file and a list of directories; the answer
a Markdown file and the JSON envelope kept beside it for the usage
and the status. Pro: meets every bound the principal set, extends
by a row, has precedent in `forge_tools.claude_headless`, and no
dependency beyond the CLI the user installs and logs into. Con: the
flag surface of four young tools moves; the read-only guarantee is
uneven and must be checked after the run (the tree compared before
and after), not assumed.

**B. A library (`google-genai` or the Antigravity SDK).** Pro:
precise control of the call, structured output, no CLI on PATH. Con:
an API key or a Cloud project to administer, a model without tools
and without web search, the chain packed into the prompt by the
forge, one library per vendor. Rejected for the reviewers; open for
a future one-sentence call.

**C. An MCP server bridging to the CLI.** Pro: the session model can
ask in passing. Con: a server per machine, the call on the model's
judgement, the same `-p` underneath, a maintainer's surface.
Rejected as the mechanism; nothing stops the principal from
installing one for his own conversations.

**D. An ACP client.** Pro: a standard, streaming, questions back.
Con: a second protocol, flag churn, no Antigravity agent yet, more
than a one-shot needs. Deferred; the adapter of A can grow an ACP
row when a dialogue is wanted.

## Relevance to this project

Recommendation: **A**, as one script with one engine table,
synchronous first and a spool flag for the detached tempo (F13),
with these facts carried into the design:

- The forge names engines, never models: the model is the engine's
  default or a word the principal gives at the call, listed by the
  engine itself (`agy models`); no slug is written into the forge.
- The script requires a version floor where a bug is known (F5),
  starts the process with stdin closed, reads the engine's status
  field, and treats an empty answer with exit 0 as a failure.
- The run is given directories, never the forge root as a
  workspace: the engine's own tree may execute hooks and read what
  a reviewer must not see (F7, and the instance file; the companion
  note says how).
- Read-only is verified, not trusted: the script records the
  tree's state before the run and refuses the answer when the run
  changed anything.
- The engine, the model it reports and its usage are recorded with
  the answer, from the JSON envelope, not from memory.
- `/setup` names the CLIs as optional prerequisites the user
  installs and logs into himself, nothing more; `forge-status` can
  say which engines are on PATH, which is machine state found at
  run time, never an instance fact.

What this changes in the intent is POS.0800: the direction holds
(a different family over a CLI link) and the mechanics are now
known; "composed in Microsoft AI Foundry" becomes one engine among
several, without priority, and what is composed is the forge's own
persona and contract, sent to whichever engine is named. Proposed
through `/forge intent`, never here.

## Sources

- Google, "An important update: Transitioning Gemini CLI to
  Antigravity CLI", discussion #27274 in google-gemini/gemini-cli,
  2026-05-19.
- geminicli.com, automation tutorial and quota page, banner updated
  2026-06-18.
- antigravity.google/docs: cli/headless, cli/reference,
  cli/gcli-migration, getting-started (tab cli), cli/credits,
  sdk/overview.
- google-antigravity/antigravity-cli, issue #76, "agy --print / -p
  silently drops stdout when run with a non-TTY", 2026-05-21 to
  2026-07-12.
- OpenAI, Codex non-interactive mode (learn.chatgpt.com/docs/
  non-interactive-mode).
- Anthropic, "Run Claude Code programmatically"
  (code.claude.com/docs/en/headless).
- GitHub Docs, Copilot CLI programmatic reference and command
  reference; GitHub changelog 2025-10-03 on model selection.
- agentclientprotocol.com: introduction, agents, libraries/python;
  zed.dev/acp/agent/gemini-cli.
- BeehiveInnovations/zen-mcp-server, README and docs/tools/clink.md;
  the pages of gemini-mcp-tool, ask-gemini-mcp,
  antigravity-cli-mcp-slim, agy-mcp.
- Google, Gemini API OAuth quickstart and python-genai
  authentication; CloudZero, "Google Antigravity pricing", 2026-05.
- Google Developers Blog, "Meet Jules Tools", 2025-10.
