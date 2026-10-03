---
project: forge
type: research
topic: when an AI agent may decide and act on its own and when it waits for a person - vendor mechanics, levels of autonomy, human-factors findings, practice of delegated routine decisions, the handover of a whole task, and agents that decide for the owner
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1, section Automation; research/2026-10-03-where-the-forge-asks-for-the-principals-word.md; 10-intent.threads.md, THR.0400; research/2026-09-28-human-ai-elicitation-over-artefacts.md
status: immutable
---

# When an agent may decide and when it waits

## Question

When may an AI agent decide and act on its own and when must it wait
for a person, as the vendors, the research and practice state it
today, and how is a whole task handed over to an agent so that the
person only judges the result?

This note is the outside half of
`2026-10-03-where-the-forge-asks-for-the-principals-word.md` (below:
the internal note). That note catalogues the forge's 37 consent
points in four classes: **I** irreversibility or outward effect,
**A** the principal's authorship of substance, **C** cost, **B**
bookkeeping. It is not repeated here; its classes and its
recommendation are tested against what the world does. Findings and
options, not a design.

## How the sources were read

Everything was fetched on 2026-10-03. The fetch tool returns, for
most pages, a small model's extraction of the page and not the page.
Each statement carries one of these marks:

- **[V]** verified on the raw page: the tool returned the page's own
  Markdown and it was read directly (the Claude Code documentation
  pages on permission modes, auto mode configuration, checkpointing,
  routines, best practices, agent teams, permissions and sandboxing;
  the two Microsoft Learn pages).
- **[E]** from the fetch tool's extraction of a page that was opened;
  quotations are as the extraction returned them and are to be
  checked at the source before they are quoted onward.
- **[S]** secondary: a search result or a third party's account; the
  primary page was not read.
- **[M]** from memory, unverified.
- **[O]** this note's own synthesis.

Status of agreement: **consensus**, **emerging** or **contested**,
said per finding.

Could not be opened: OpenAI's "A practical guide to building agents"
(the PDF came back unreadable), OpenAI's deep research help page
(refused), PubMed pages (cookie wall; two abstracts were read through
Europe PMC instead), the Harvard Data Science Review study "Bias in
the Loop" (refused), the JMIR review of alert overrides (empty).
What is said of them is marked [S].

## Key findings

### 1. The vendors agree on what waits for a human: the irreversible, the outward and the high-stakes. None requires a human for every action. [consensus]

- Anthropic, "Building effective agents" (2024-12-19) [E]: agents
  "plan and operate independently" once the task is clear, "can then
  pause for human feedback at checkpoints or when encountering
  blockers", and "it's also common to include stopping conditions
  (such as a maximum number of iterations) to maintain control".
- Anthropic, framework for safe and trustworthy agents (2025-08-04)
  [E]: "Humans should retain control over how their goals are
  pursued, particularly before high-stakes decisions are made"; the
  same text grants that "the right balance between autonomy and
  oversight varies dramatically across scenarios".
- Anthropic, "Measuring AI agent autonomy in practice" (2026-02-18)
  [E]: "Oversight requirements that prescribe specific interaction
  patterns, such as requiring humans to approve every action, will
  create friction without necessarily producing safety benefits";
  what matters is "whether humans are in a position to effectively
  monitor and intervene".
- OpenAI, practical guide to building agents (2025) [S, two
  secondary accounts]: human intervention is planned for two
  triggers, an agent exceeding failure thresholds and actions that
  are high-risk, sensitive or irreversible, "until confidence in the
  agent's reliability grows"; tools are rated by risk.
- OpenAI Agents SDK [E]: approval is a property of the tool
  (`needs_approval`, true or a function deciding per call); a
  decision can be made sticky (`always_approve`, `always_reject`).
- Google, approach for secure AI agents (2025) [E, abstract only]:
  "agents must have well-defined human controllers, their powers must
  be carefully limited, and their actions and planning must be
  observable".
- Microsoft, Copilot Studio guidance on autonomous agents (page
  dated 2026-01-16) [V]: "Implement human oversight for critical
  actions: For high-stakes tasks, keep a human in the loop"; least
  privilege; "Maintain detailed logs of everything the agent does";
  and "Small, incremental expansions of responsibility are safer
  than giving the agent too much autonomy all at once".
- Microsoft Agent Framework (page dated 2026-09-28) [V]: approval is
  marked per tool (`approval_mode="always_require"`); a harness adds
  "standing 'always approve' rules, and optional heuristic
  auto-approval".

The shared shape [O]: the gate is attached to a **class of action
declared in advance** (a tool, a path, a kind of effect), never to
"every action", and it is paired with three other controls: limited
powers, a log, and a way to stop.

### 2. How one product draws the line: Claude Code's modes [V unless marked]

Read on the raw documentation pages.

- **Modes.** Manual (`default`) asks before edits, commands and
  network; `acceptEdits` lets file edits run; `plan` reads and
  proposes, and edits stay blocked until the plan is approved;
  `auto` runs "Everything, with background safety checks";
  `dontAsk` denies whatever would prompt; `bypassPermissions` is for
  "Isolated containers and VMs only". Auto mode is now the built-in
  starting mode of interactive sessions.
- **How auto mode decides.** A fixed order, first match wins: (1)
  the user's allow, ask and deny rules; (2) "Read-only actions and
  file edits in your working directory are auto-approved"; (3)
  everything else goes to a separate classifier model; (4) a block
  returns its reason to the agent. The classifier sees "user
  messages, tool calls other than read-only lookups ... and your
  CLAUDE.md content"; tool results are stripped. The engineering
  account (2026-03-25) [E] gives the reasons: the agent's own prose
  is stripped "so the agent can't talk the classifier into making a
  bad call", and tool outputs because that is "where hostile content
  enters the context".
- **What it blocks by default** is a long list of exactly the
  internal note's class I: force push; "Irreversibly destroying
  files that existed before the session"; production deploys;
  sending sensitive data out; sensitive content into a commit, a
  push or a public repository; "Merging a pull request no human has
  approved, approving Claude's own pull request, or disabling CI
  checks"; changing its own oversight. What it allows by default
  includes local file operations in the working directory and
  "Pushing to any branch of the repository you're working in,
  including the default branch".
- **The word given.** "The classifier treats boundaries you state in
  the conversation as a block signal ... Claude's own judgment that
  a condition was met does not lift it." An approval must "name the
  action and its specifics" and covers one action: "General requests
  don't count as explicit intent. Asking Claude to 'clean up the
  repo' doesn't authorize force-pushing". But a boundary stated in
  conversation "can be lost if context compaction removes the
  message"; "For a hard guarantee, add a deny rule".
- **Deterministic gates beside the classifier.** "Deny rules block
  in every mode, including `bypassPermissions`." An explicit ask
  rule such as `Bash(git push *)` is "evaluated before the
  classifier and always force[s] a permission prompt, even in auto
  mode"; ask rules match the command as written, so a differently
  written command slips past, and "For a checkpoint that inspects
  the full command text, add a PreToolUse hook". A `PreToolUse`
  hook can answer allow, deny, ask or defer [E], and "PreToolUse
  hook decisions don't bypass permission rules" [V]. Whether a
  hook's own `ask` produces a prompt in auto mode is not stated on
  the pages read.
- **Fallback to the person.** "if the classifier blocks an action 3
  times in a row or 20 times total, auto mode pauses and Claude Code
  resumes prompting." No verdict means denial, not execution.
- **Stated limits.** "Auto mode reduces permission prompts but does
  not guarantee safety. Use it for tasks where you trust the general
  direction, not as a replacement for review on sensitive
  operations." Measured [E]: 0.4 % false positives on real traffic
  (n=10,000) and a 17 % false-negative rate on real overeager
  actions (n=52); "It is not a drop-in replacement for careful human
  review on high-stakes infrastructure."
- **Undo.** Checkpoints snapshot files before each prompt and
  `/rewind` restores them, but "Checkpointing does not track files
  modified by Bash commands", usually not a subagent's edits, and
  nothing remote; "Not a replacement for version control".
- **Sandbox.** Operating-system limits on what shell commands can
  reach let commands run without a prompt; it covers shell commands
  only and "On native Windows, Claude Code runs commands
  unsandboxed".
- **Unattended runs.** Routines "run autonomously as full Claude
  Code cloud sessions ... without stopping for approval"; what
  bounds them is scope (repositories, network, connectors: "Scope
  each of those to what the routine actually needs"), work pushed
  to `claude/`-prefixed branches with branch protection as the
  wall, and review after the fact: each run is a session "where you
  can see what Claude did, review changes, and create a pull
  request". The stored prompt "can't act as approval or consent for
  actions during the run". And: "A green status ... does not mean
  the task in your prompt succeeded."

OpenAI's coding agent has the same anatomy [E]: a sandbox ("The
sandbox defines technical boundaries. The approval policy decides
when the agent must stop and ask before crossing them"), approval
policies from `untrusted` to `never`, and an optional reviewer agent
(finding 7).

What this shows [O]: the product gates protect against **harm**. A
write inside the working directory is approved by rule, before any
classifier. Nothing in the automatic mode protects "nothing written
that was not agreed": the incident THR.0400 records happened in such
a mode and is, by the documentation, the mode working as designed.
The only vendor mechanisms that hold the forge's stricter rule are
Manual mode, explicit ask and deny rules, and a hook.

### 3. Levels of autonomy: the level is a design decision, and the "approver" level has a named weakness [emerging as frameworks; consensus on the weakness]

- Feng, McDonald and Zhang, "Levels of Autonomy for AI Agents"
  (2025-06-14) [E]: five levels by the user's role: operator,
  collaborator, consultant, approver, observer. At the approver
  level the user is engaged only at a blocker or a consequential
  action; the risk named there: "User disengagement can lower the
  care with which they approve actions", and a misaligned agent
  might "gradually convince disengaged users to approve risky
  actions". The level is "a deliberate design decision, separate
  from its capability". The forge as defined sits between
  collaborator and consultant [O].
- Mitchell, Ghosh, Luccioni and Pistilli (2025-02-04, revised
  2025-10-20) [E]: "risks to people increase with the autonomy of a
  system: The more control a user cedes to an AI agent, the more
  risks to people arise"; fully autonomous agents should not be
  built. A position paper: contested as a conclusion, uncontested
  as a direction of risk.
- The classical frame: Parasuraman, Sheridan and Wickens (2000) [E,
  abstract] give "types and levels of automation" over four
  functions: information acquisition, analysis, decision selection,
  action implementation. The lesson that carries over [O]: a system
  may be highly automated in gathering and analysing and low in
  deciding; "who decides" is one dial of four. That the
  ten-step scale behind it includes "executes unless the human
  vetoes" and "informs the human after" is [M].
- EU AI Act, Article 14 [E]: for high-risk systems, oversight must
  be effective, and the overseer must "remain aware of the possible
  tendency of automatically relying or over-relying on the output"
  (automation bias); for one class of system, no action unless
  "separately verified and confirmed by at least two natural
  persons". The law thus names both failure and remedy; it does not
  apply to a document workshop, and is cited for its vocabulary.

### 4. Human factors: asking every time fails, and so does passive monitoring [consensus, decades old; the LLM-era numbers emerging]

- **Asking every time.** Anthropic's own figure [E]: "Claude Code
  users approve 93% of permission prompts", and "Over time that
  leads to approval fatigue, where people stop paying close
  attention to what they're approving". The product documentation
  says the same in plain words [V]: "After the tenth approval you're
  clicking through rather than reviewing." In medicine the same
  pattern is measured as alert fatigue: reviews report that most
  decision-support alerts are overridden [S; one search result gave
  a range of 46 to 96 %, not read at source].
- **Monitoring instead.** Bainbridge, "Ironies of Automation"
  (Automatica, 1983) [E, through an encyclopedia article]: the
  operator left to monitor does not practise, yet is expected to
  step in at "the rare but crucial interventions". Endsley and Kiris
  (Human Factors, 1995) [E, abstract]: the out-of-the-loop problem;
  the shift "from active to passive information processing" was the
  likely cause of lost awareness, and the level of control the
  operator keeps moderates it. Parasuraman and Manzey (Human
  Factors, 2010) [E, abstract]: complacency arises under multiple-
  task load; automation bias produces errors of omission and of
  commission.
- **Reviewing an AI's proposal.** Schroeder, Roy and Kabbara
  (2025-07-21) [E, abstract], preregistered, 410 annotators:
  shown LLM suggestions, people were not faster but more confident,
  and "strongly took the LLM suggestions, significantly changing the
  label distribution". Rosbach et al. (2026) [E, abstract]: in
  pathology, AI help improved performance and brought a 7 %
  automation bias rate; time pressure made it more severe. A 2026
  study of 2,784 participants verifying AI-extracted values [S]:
  attitude toward AI predicted who accepted wrong suggestions.
- **What practice does instead** [O, assembled from findings 1, 2
  and 5]: fewer and weightier questions; approval by class or
  policy; limits enforced by the environment and not by attention;
  reversible actions with an undo; review of the result after the
  fact with a log; a circuit breaker that returns control when the
  automation misfires. Anthropic's usage data [E] shows the shift in
  the wild: full auto-approve rises from about 20 % of sessions for
  new users to over 40 % with experience, while interruptions rise
  from 5 % to 9 % of turns; and "On the most complex tasks, Claude
  Code asks for clarification more than twice as often as humans
  interrupt it": the agent stopping itself is part of the oversight.

The two halves pull against each other, and the literature does not
resolve it with a formula [O]: every question removed makes the
remaining ones better attended, and moves the person one step toward
the monitor who skims. The internal note's rejection of its option
3 (one reflection of forty items) has this literature behind it.

### 5. Adjacent practice: routine decisions are delegated by class defined in advance, with a guard on each [consensus]

- **Change management.** ITIL's three kinds [E, a vendor's account
  of 2025-03-17; S for the rest]: a standard change is "a low risk,
  preauthorized change which is relatively common and follows a
  known procedure"; a normal change is assessed and authorised by a
  change authority in proportion to its risk; an emergency change
  may be approved "after the change is applied". The class is
  defined by the **type of change and its procedure**, decided once
  by the authority, not by a rating given to each instance by whoever
  proposes it [O].
- **Code review.** GitHub auto-merge [E]: "merges a pull request
  automatically after all required reviews and status checks pass".
  Code owners [E]: review is required from the owners "of the
  changed files", so the gate follows the **path touched**.
  Dependabot [E]: the documented example auto-merges patch-level
  updates only, with required status checks as the stated guard.
  That lint and formatting bots commit without review is common
  practice [M].
- **Finance.** The four-eyes or maker-checker rule [S]: no single
  person executes a sensitive operation; low-value recurring
  payments to known parties go a lighter route; the known failure
  is the signature "for appearance", and the stated condition is
  that the checker has "sufficient information, authority and time".
  Thresholds invite splitting [S].
- **Delegation of authority** in organisations (limits by amount
  and kind, the delegator stays accountable, exercise is audited by
  sample) is [M], not researched here.

The guards that recur [O]: a class written down beforehand; a
mechanical test that the instance belongs to it (checks green, patch
level, path); an audit trail; reversibility; and a route back to the
normal process for whatever does not fit.

### 6. Handing over a whole task: a contract before, evidence after, and a place apart for the result [consensus on the contract; emerging on the rest]

- **The contract.** Anthropic's multi-agent research system
  (2025-06-13) [E]: each delegated task needs "an objective, an
  output format, guidance on the tools and sources to use, and clear
  task boundaries"; without them agents "misinterpreted the task or
  performed the exact same searches"; effort is budgeted in the
  prompt ("Simple fact-finding requires just 1 agent with 3-10 tool
  calls ..."). Routines [V]: "the prompt must be self-contained and
  explicit about what to do and what success looks like". Best
  practices [V]: "The most useful specs are self-contained: they
  name the files and interfaces involved, state what is out of
  scope, and end with an end-to-end verification step"; and the
  spec itself is best drawn out by interview: "have Claude interview
  you first".
- **Plan approval before, or result review after.** Plan mode [V]
  is the first; the documentation limits it: "Planning is most
  useful when you're uncertain about the approach ... If you could
  describe the diff in one sentence, skip the plan." OpenAI's deep
  research [S] asks clarifying questions and, in one surface, shows
  a research plan the user can edit before the run. Routines are the
  second: no approval during, a session and a draft pull request
  after. The two are combined in practice, not opposed [O].
- **Presenting the result so that it can be judged.** "Have Claude
  show evidence rather than asserting success ... Reviewing evidence
  is faster than re-running the verification yourself, and it works
  for sessions you weren't watching" [V]. Research reports carry a
  citation per claim, placed by a separate pass [E]. "If you can't
  verify it, don't ship it" [V].
- **A place apart.** Unattended work lands on its own branch and is
  offered as a pull request; the default branch is behind
  protection [V]. The result is a proposal by construction.
- **What goes wrong.** "Claude stops when the work looks done";
  "Claude produces a plausible-looking implementation that doesn't
  handle edge cases" [V]. A reviewer agent adds its own distortion:
  "A reviewer prompted to find gaps will usually report some, even
  when the work is sound ... Chasing every finding leads to
  over-engineering" [V]. People anchor on the proposal (finding 4).
  Ownership of the text falls the further the AI goes into the
  drafting: finding 7 of
  `2026-09-28-human-ai-elicitation-over-artefacts.md`, not repeated
  here. Human testers still find "hallucinated answers on unusual
  queries ... or subtle source selection biases" that automated
  evaluation misses [E].

### 7. An agent that decides for the owner: accepted as a safety filter on actions, warned against as the judge of the work [emerging for the first; consensus in the research for the second]

- **Where it exists.** Claude Code's classifier (finding 2) and
  OpenAI's auto-review [E]: "Auto-review replaces manual approval at
  sandbox boundaries with a separate reviewer agent"; it sees "a
  compact transcript plus the exact approval request", "hidden
  assistant reasoning is not included"; after a denial the agent is
  told "Do not pursue the same outcome via workaround"; a circuit
  breaker trips after "3 consecutive denials or 10 denials within a
  rolling window of the last 50 reviews"; it "can still make
  mistakes" and "should complement, not replace, good sandbox
  design, monitoring, and organization-specific policy".
- **What both have in common** [O]: the decider rules on one
  question, may this action run, against a written policy; it is
  kept blind to the acting agent's reasoning; it fails closed; it
  hands back to the person when it keeps refusing; and the things
  the owner declared as his (ask rules) never reach it. Neither
  gives a verdict on whether the work is right, and the classifier
  explicitly blocks an agent approving its own pull request or
  merging one "no human has approved".
- **A vendor's own agent-approves-agent step is not a review.** In
  agent teams [V]: "Claude Code approves the plan in the lead's
  session as soon as the request arrives, without the lead reviewing
  it"; and "A teammate can't approve a permission prompt or supply
  consent on your behalf".
- **Documented failure modes of a judging agent.** Panickssery,
  Bowman and Feng (2024) [E, abstract]: an LLM evaluator "scores its
  own outputs higher than others' while human annotators consider
  them of equal quality". Kim, Garg, Peng and Garg (ICML 2025) [E,
  abstract], over 350 models: "models agree 60% of the time when
  both models err", and the larger and more accurate models are the
  more correlated, across providers; the effect is shown for
  LLM-as-judge. Park and Choi (2026) [E, abstract]: agents grading
  their own long-running work claimed improvement in every cycle
  while "56% showed zero or negative real-world progress"; the gap
  closed only where the criteria were "verifiable within the
  artifact itself".
- **Where it helps.** A second agent in a fresh context, seeing the
  result and the criteria but not the reasoning, is recommended as a
  check before a person counts work as done [V]; as an addition to
  the person's judgement, not in its place.

Contested [O]: how far a different model, or a judge given only
external evidence, removes the correlation. The papers read say
partly at best.

## What the outside says of the four classes

All of this section is [O], resting on the findings above.

| Class | Outside precedent for delegating | Warned against | The guard the precedent pairs with it |
|---|---|---|---|
| **I** irreversible or outward | Narrow: a plain push to the working repository is allowed by default in one product; everything else in the class is on every vendor's "human" list | Force push, destroying what predates the session, content reaching a public surface, an agent merging or approving its own work | A deterministic rule (deny, ask), not the model's care; scope limits; the gate on the outward step even when all else runs free |
| **A** authorship of substance | None. No product gate protects it: gates are about harm, not about whose thought the text is | Review of an AI proposal as the person's only contribution (anchoring, lost ownership) | The person states the aim first (interview, spec); the result arrives as a proposal in a place apart; adoption is his act |
| **C** cost | Strong: budgets, effort rules, stopping conditions, hourly caps, a breaker; consent once per task is the norm | A run with no ceiling; a "green" status read as success | A stated bound in the contract and a stop rule the harness enforces |
| **B** bookkeeping | Strong: the standard change, auto-merge on green checks, patch-level updates, lint bots | Classing by a rating the proposer gives; signatures for appearance | A class written beforehand by type and by what is touched; a mechanical test of membership; a log; reversibility; the normal route for what does not fit |

On the internal note's recommendation:

- **Its option 2 (bulk settlement of class B findings) has the
  strongest precedent of all**, with one correction the precedent
  makes. The note asks whether "low" is a fair proxy for
  "bookkeeping" and observes that severity is the reviewer's. The
  outside never classes by the proposer's rating: a standard change
  is a type with a known procedure, and required review follows the
  path touched. Translated: a finding is routine by **what its fix
  touches** (a ledger row, a front-matter field, an index entry),
  and is never routine where the fix touches the wording of a rule
  or of an artefact, whatever its severity. The two findings rightly
  rejected by DEC.0150 and DEC.0160 would have been outside such a
  class.
- **Its option 3 (reflection only) is the monitor's position** the
  human-factors literature warns of; the rejection stands.
- **Its option 4 (merging confirmations of a save and a release)**
  matches "approval by policy": the message is derived from records
  already confirmed. The precedent's guard is that the outward step
  itself (the push) keeps its gate, which the forge already has in
  the typed command.
- **Its option 5 (consent once per task for class C)** is the
  outside norm, provided the bound is stated and enforced.
- **Its option 6 (never delegate I and A)** is the consensus for I.
  For A the outside offers no mechanism at all, which is a stronger
  reason, not a weaker one.
- **THR.0400.** A gate that asks at every write would recreate the
  condition for which a vendor measured 93 % approvals. The outside
  pattern is a small set of deterministic rules on the steps that
  matter, and one question of the thread is answered by the
  documentation: an explicit ask rule does prompt in the automatic
  mode, and a deny rule holds in every mode. Whether a hook's `ask`
  does is still to be tried.

## Options with trade-offs

Options the internal note did not have; its own six stand as they
are.

**A. A catalogue of standard changes.** The routine class is written
down once, by the principal's decision, as kinds of fix and the
files they may touch; whatever matches is applied without a verdict,
shown in the reflection and recorded; whatever does not match goes
to the walkthrough. *For:* the strongest precedent; the class is
his, decided once, so the delegation is itself an act of his word.
*Against:* a catalogue to keep; the membership test must be
mechanical or it becomes a judgement again.

**B. Gate by path, not by action.** Deterministic ask and deny rules
on the few outward or protected steps (the scripts that save and
release, the operating layer's files), everything else ungated.
*For:* holds in every permission mode; no heuristic. *Against:*
rules match the command as written, so a differently written command
passes; it guards harm, not consent inside the workspace, so the
rule "nothing written that was not agreed" still rests on conduct.

**C. A whole task under a contract, landing apart.** The handover
names objective, boundaries, a budget, a stop rule, the form of the
result and the evidence to bring; the result is born in a place of
its own and enters the chain only by the principal's adoption.
*For:* the documented shape of every long-running product; keeps "no
action beyond the word" because the word is the contract. *Against:*
anchoring and lost ownership are measured for exactly this shape;
the contract must be drawn out first, which costs the questions it
saves later; a research-heavy task returns a list someone must
still judge.

**D. An agent as sorter, never as judge.** A separate agent, blind
to the working conversation, puts each finding into "matches the
catalogue" or "for the principal", and can only escalate.
*For:* the one form of deciding agent the outside accepts: one
narrow question, a written policy, failing toward the person.
*Against:* the forge runs on one model, and correlated error is the
documented weakness of a same-model judge; where option A's test is
mechanical the sorter adds nothing; a 17 % miss rate was measured
for a vendor's far more tested classifier.

**E. A breaker.** Any delegation lapses back to asking after a
stated sign of misfire (a delegated fix the principal strikes, a
check that fails after an automatic fix). *For:* both vendors do it;
it bounds the cost of a wrong class. *Against:* one more rule to
hold in a long conversation.

**F. Fewer findings at the source.** Reviewers and checks told what
counts as a finding and what does not; a check not run twice in one
flow. *For:* a vendor says outright that a reviewer asked for gaps
reports some regardless; the burden the internal note counts is in
part made by the checks. *Against:* a narrower check misses more; it
touches the reviewers' contracts.

**G. Earned widening.** A delegation starts narrow and is widened by
the principal's decision after it has run clean, as two vendors
advise. *For:* matches how the forge has removed ceremony before.
*Against:* slow; needs someone to keep the count.

## What was not found

- A vendor mechanism that protects authorship or "no action beyond
  the consent given" inside the workspace; every gate found is about
  harm.
- Any source that recommends an agent as the final judge of another
  agent's substantive work; any measured result for a document
  workshop as against code.
- A controlled comparison of plan approval before with result review
  after.
- Evidence on a single expert delegating routine verdicts over
  weeks; the human-factors results are from operators, clinicians
  and crowdworkers.
- Whether a `PreToolUse` hook's `ask` prompts in the automatic mode.

## Relevance to this project and recommendation

For the section Automation of `00-brief-next-gen.md`. The
recommendation is this note's own, offered once.

The brief asks where the owner's word protects something and where
it is only ceremony. The outside answers in the same four classes
the internal note found, with one sharpening: the line between
ceremony and protection runs by **what an action touches**, declared
beforehand, never by how important the acting agent thinks it is.

1. **Keep the word, unchanged, on class I and class A.** For I this
   is every vendor's rule. For A it is more: nothing outside the
   forge guards it, the automatic mode approves a write in the
   workspace by rule, and the measured effect of judging a finished
   proposal is anchoring. The forge's rules here are stricter than
   the market's on purpose, and the reason holds.
2. **Delegate class B as a standard change (option A), not as a
   severity.** This is the internal note's option 2 with the class
   defined by kind of fix and file touched, decided once by the
   principal, tested mechanically, shown in the reflection, logged.
   The reflection before the write stays, as the one place where he
   still sees the whole.
3. **Give the word for class C once per task, with a bound and a
   stop** (the internal note's option 5), as part of the contract of
   option C.
4. **Treat "a task handed over whole" as a contract plus a place
   apart (option C)**, and say in the brief what it costs: the
   result is a proposal, its adoption into the intent stays his act,
   and the prior note's finding on ownership applies in full. A
   task such as the documentation, a render-like output, carries
   less of that cost than one that would write positions.
5. **Do not build an agent that gives verdicts for the owner.** The
   outside accepts a deciding agent only as a filter on one narrow
   question with a written policy and a fall-back to the person.
   If a sorter is wanted (option D), let it escalate only, and
   prefer the mechanical test where one exists.
6. **Settle THR.0400 with deterministic rules on the outward steps
   (option B) before any gate on every write**, and add a breaker
   (option E) to whatever is delegated.
7. **Look at the source of the burden as well (option F)**: part of
   what a release asks is made by checks that report by design.

Both things the forge's rules were made to protect survive this:
authorship, because nothing in classes A and I moves and a handed-
over task returns as a proposal; and no action beyond the word
given, because each delegation is itself a word of his, given once,
for a class or a task whose edge is written down.

What stays uncertain: whether a mechanical test of "routine" can be
written for the forge's findings; how much of the measured anchoring
applies to an expert on his own material; the real behaviour of ask
rules and hooks in the automatic mode on the forge's platform, which
the documentation states and no one here has tried; and the content
of the sources that could not be opened.

Consult when: deciding which of the principal's words may be given
once for a class or a task, shaping the handover of a whole task,
weighing an agent that decides for the owner, or settling the gate
of THR.0400.

## Sources

All fetched 2026-10-03. The mark says how each was read.

Vendors:

- Building effective agents - https://www.anthropic.com/engineering/building-effective-agents - Anthropic, 2024-12-19 [E]
- Our framework for developing safe and trustworthy agents - https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents - Anthropic, 2025-08-04 [E]
- Measuring AI agent autonomy in practice - https://www.anthropic.com/research/measuring-agent-autonomy - Anthropic, 2026-02-18 [E]
- Claude Code auto mode (engineering account) - https://www.anthropic.com/engineering/claude-code-auto-mode - Anthropic, 2026-03-25 [E]
- How we built our multi-agent research system - https://www.anthropic.com/engineering/multi-agent-research-system - Anthropic, 2025-06-13 [E]
- Claude Code documentation, Choose a permission mode - https://code.claude.com/docs/en/permission-modes - Anthropic, undated [V]
- Claude Code documentation, Configure auto mode - https://code.claude.com/docs/en/auto-mode-config.md - Anthropic, undated [V]
- Claude Code documentation, Configure permissions - https://code.claude.com/docs/en/permissions.md - Anthropic, undated [V, in part]
- Claude Code documentation, Hooks - https://code.claude.com/docs/en/hooks - Anthropic, undated [E]
- Claude Code documentation, Checkpointing - https://code.claude.com/docs/en/checkpointing - Anthropic, undated [V]
- Claude Code documentation, Configure the sandboxed Bash tool - https://code.claude.com/docs/en/sandboxing - Anthropic, undated [V, in part]
- Claude Code documentation, Automate work with routines - https://code.claude.com/docs/en/routines.md - Anthropic, undated [V]
- Claude Code documentation, Best practices - https://code.claude.com/docs/en/best-practices.md - Anthropic, undated [V]
- Claude Code documentation, Orchestrate teams of Claude Code sessions - https://code.claude.com/docs/en/agent-teams.md - Anthropic, undated [V]
- Codex documentation, Sandboxing - https://learn.chatgpt.com/docs/sandboxing.md - OpenAI, undated [E]
- Codex documentation, Auto-review - https://learn.chatgpt.com/docs/sandboxing/auto-review - OpenAI, undated [E]
- OpenAI Agents SDK, Human-in-the-loop - https://openai.github.io/openai-agents-python/human_in_the_loop/ - OpenAI, undated [E]
- A practical guide to building agents - https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf - OpenAI, 2025 (unreadable; known through: https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/ of 2025-04-17 [E] and search results [S])
- Deep research FAQ - https://help.openai.com/en/articles/10500283-deep-research-faq - OpenAI (refused; search result only) [S]
- An introduction to Google's approach for secure AI agents - https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/ - Google, 2025 (abstract) [E]
- Design autonomous agent capabilities - https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/autonomous-agents - Microsoft, 2026-01-16 [V]
- Using function tools with human in the loop approvals - https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval - Microsoft, 2026-09-28 [V]

Frameworks and human factors:

- K. J. K. Feng, D. W. McDonald, A. X. Zhang, Levels of Autonomy for AI Agents - https://arxiv.org/html/2506.12469v1 - arXiv, 2025-06-14 [E]
- M. Mitchell, A. Ghosh, A. S. Luccioni, G. Pistilli, Fully Autonomous AI Agents Should Not be Developed (abstract) - https://arxiv.org/abs/2502.02649 - arXiv, 2025-02-04, revised 2025-10-20 [E]
- R. Parasuraman, T. B. Sheridan, C. D. Wickens, A model for types and levels of human interaction with automation (abstract); R. Parasuraman, D. H. Manzey, Complacency and bias in human use of automation: an attentional integration (abstract) - https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ext_id:21077562%20OR%20ext_id:11760769%20OR%20ext_id:8849495&resultType=core&format=json - Europe PMC records; IEEE Trans. SMC 2000, Human Factors 2010 [E]
- M. R. Endsley, E. O. Kiris, The out-of-the-loop performance problem and level of control in automation (abstract) - https://trid.trb.org/View/427017 - Human Factors 37(2), 1995 [E]
- Ironies of Automation (on L. Bainbridge, Automatica 19(6), 1983) - https://en.wikipedia.org/wiki/Ironies_of_Automation - Wikipedia, last edited 2026-07-11 (tertiary) [E]
- EU AI Act, Article 14, Human oversight - https://artificialintelligenceact.eu/article/14/ - undated mirror of the regulation [E]
- H. Schroeder, D. Roy, J. Kabbara, Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks (abstract) - https://arxiv.org/abs/2507.15821 - arXiv, 2025-07-21 [E]
- E. Rosbach et al., Stuck on Suggestions: Automation Bias, the Anchoring Effect, and the Factors That Shape Them in Computational Pathology (abstract) - https://arxiv.org/abs/2603.11821 - arXiv, 2026-03-12, revised 2026-09-28 [E]
- Bias in the Loop - https://hdsr.mitpress.mit.edu/pub/nrcn4h7d - Harvard Data Science Review, 2026 (refused; search result only) [S]
- Review of overridden alerts in computerized physician order entry - https://medinform.jmir.org/2020/7/e15653/ - JMIR Medical Informatics, 2020 (empty; search result only) [S]

Agents judging agents:

- A. Panickssery, S. R. Bowman, S. Feng, LLM Evaluators Recognize and Favor Their Own Generations (abstract) - https://arxiv.org/abs/2404.13076 - arXiv, 2024-04-15 [E]
- E. Kim, A. Garg, K. Peng, N. Garg, Correlated Errors in Large Language Models (abstract) - https://arxiv.org/abs/2506.07962 - arXiv, 2025-06-09, ICML 2025 [E]
- H. Park, B. Choi, When Do Agent Loops Mistake Stagnation for Progress? (abstract) - https://arxiv.org/abs/2607.25152 - arXiv, 2026-07-27, revised 2026-09-29 [E]

Adjacent practice:

- Automatically merging a pull request - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request - GitHub, undated [E]
- About code owners - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners - GitHub, undated [E]
- Automating Dependabot with GitHub Actions - https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions - GitHub, undated [E]
- Change management for IT (ITIL 4 change types) - https://www.splunk.com/en_us/blog/learn/change-management.html - Splunk, 2025-03-17 (secondary to ITIL) [E]
- Four-eyes principle and maker-checker (several practitioner glossaries) - search results only [S]
