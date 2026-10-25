---
id: THR.0740
concerns: intent, solution-design
origin: the principal
status: open
---

The forge sends work to a model of another family - a challenger, a
critic, a research, or a question about what Claude has just said -
through one mechanism, the user logged into that model once outside
the forge, the forge carrying no account; Gemini first, Microsoft AI
Foundry and anything else later. Opened 2026-10-23.

The principal's word of 2026-10-23: two cases. The forge's own
reviewers and research run on another engine as they run on the
session model. And the `??` of the working methods formalised into a
job: Claude composes what the matter is, how it is approached, where
the work stands and what is asked, sends it to one or several
engines, and the answers come back without the principal carrying
them by hand, as he did on 2026-10-22 with the three Gemini
challenges in `sources/`. Both tempos: waiting in the session, and
sending now and collecting later. One engine or several with a
synthesis, for both cases. Bounds: no administration in the forge,
no accounts, no configuration of who connects; the link may be a
CLI, a library or an MCP server. Priorities: Gemini now; Foundry,
which POS.0800 names, stays intended without priority; the general
case of almost any engine likewise.

Researched 2026-10-23, two notes:
`research/2026-10-23-calling-another-model-from-the-forge-without-accounts.md`
and
`research/2026-10-23-a-reviewer-or-a-question-on-another-model-inside-the-forge.md`.
What they found: Gemini CLI was replaced for personal accounts by
Antigravity CLI (`agy`) on 2026-06-18; `agy`, Codex CLI, Claude
Code and Copilot CLI share one headless shape (a prompt, a
directory, a final message, a JSON envelope with a schema option, a
login made once on the machine), so the link is one script with a
table of engines, a dozen lines each; a library is a model without
tools and needs a key, an MCP server is the same CLI call under a
hat and returns through the model, the Agent Client Protocol is for
a dialogue. The reviewer's packet is the forge's own persona and
contract, the engine reading the project from disk; the forge root
is never the engine's workspace, the report is scanned for instance
values before filing (the guard rail of THR.0210) and checked for
its shape, read-only is verified by comparing the tree. The
"criticise this" job is a consultation, not a reviewer, since it
carries the conversation; its packet and answers are a bundle of
sources. With several engines the principal is the chairman and
Claude lays the answers side by side, engines named, agreement as
consistency and never validation (POS.0790). Collecting later is a
spool read by the map.

POS.0800 is stale and must be revised with this, the principal's
word of 2026-10-23: it still says the challengers are "composed by
the principal in Microsoft AI Foundry" and that "the mechanics are
designed when taken up". The direction holds - a different family
over a CLI link - but what is composed is the forge's own persona
and contract, sent to whichever engine is named at the call; the
engine's login is the user's and outside the forge; Foundry is one
engine among several, without priority; and the mechanics are now
known from the research.

Open, for a brief the principal intends to write: the names of the
consultation command and of the spool; which engines come first;
whether the engine enters the report's file name beside the
persona; the parts of the packet; how the unknowable quota is lived
with (an engine reports its usage after a run, never before); and
then the round of the intent: POS.0800 reworded as above, a
position for the consultation, POS.0790 on the layout of several
answers. State 2026-10-23: researched, nothing designed, nothing
decided.

State 2026-10-24: the link built as `scripts/forge-engine.py` and run
for the research (POS.1880, SOL.0870): one script, a table of
engines, Antigravity's row first, a per-run profile denying the
forge's tree and the shell, read-only verified by comparing the
tree; POS.0800 reworded and POS.0790 given the layout of several
answers at intent 5.37. The quota question answered for the research
by POS.1870 (a budget of the day, spent one or two runs at a time).
Open from the list above: the consultation command and the spool
with their names; whether the engine enters a report's file name
beside the persona; `/challenge` and `/critique` on the link.

2026-10-25: two parts of the Later of the brief `research` are carried
here as well, so that all of it stands in one place: divergent probes as
agents of their own (an adjacent field, a named dissent, the new or
contested), and a pass over what the agents opened and did not use.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
