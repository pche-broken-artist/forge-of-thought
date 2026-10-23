---
date: 2026-10-23
project: forge
topic: a reviewer or a question on another model inside the forge
status: immutable
derived_from: the principal's word of 2026-10-23 (two cases: the forge's own reviewers and research run on another model; and a "criticise this" job formalised out of `??`, Claude composing the packet, one or several engines, a synthesis, then a walkthrough; both tempos, waiting and collecting later); research/2026-10-23-calling-another-model-from-the-forge-without-accounts.md (companion); CLAUDE.md (Isolated reviewers, Working methods); .claude/skills/challenger-contract/SKILL.md, .claude/skills/challenge/SKILL.md, .claude/agents/challenger-architect.md; 10-intent.md v5.30 (POS.0070, POS.0440, POS.0790, POS.0800, POS.0920, POS.0950, POS.1140, POS.1370, POS.1720); threads THR.0210, THR.0530; the sources repo-detection-challenge*.md of 2026-10-22 as the manual precedent; web sources below
---

# A reviewer or a question on another model inside the forge

## Question

Given a way to call another model from a script (the companion
note), how does the call fit the forge's mechanisms: what is sent so
that a challenger, a critic or a research runs on the other model
exactly as it runs on the session model; where the answer lands and
who numbers it; what the new job "criticise what Claude just said"
is in the forge's terms, where its packet and its answers live; how
several engines on one question are brought together without the
synthesis becoming the verdict; and what changes when the run is
not waited for.

## Key findings

**F1. What a reviewer gets today is three files and a path, and an
external engine can get the same.** [verified, CLAUDE.md Isolated
reviewers; the contract and the command] An isolated subagent
starts with CLAUDE.md and the instance file preloaded (POS.0950),
its persona file with the Lens, the contract skill named in its
front-matter, and a task of two words: the project path and the
target. Everything else it reads from disk: the chain, the
threads, the decisions, the earlier reports; the contract even says
CLAUDE.md "is read from disk in this run". An agentic CLI given the
same directories does the same reading. The packet for an external
run is therefore a prompt that says who it is ("you are the
challenger persona `architect`"), names the two files to read as
its instruction (`.claude/skills/challenger-contract/SKILL.md`,
`.claude/agents/challenger-architect.md`), names the project
directory and the target, and repeats the contract's one output
rule: return the report, write nothing. The persona and the
contract are not rewritten for the other model; they are the thing
sent. This is what POS.0800 meant by "composed by the principal" -
the persona is the forge's, the engine is interchangeable.

**F2. Two things must not travel: the instance file and the forge
as an executing workspace.** [verified, CLAUDE.md Isolated
reviewers; the companion note F7; THR.0210] The contract forbids
instance facts in a report because a report is a public file; the
session subagent carries the instance file and is trusted to obey.
An external engine given the engine root as a workspace could read
`CLAUDE.local.md` and, on some engines, would run the forge's hooks
and load its CLAUDE.md as its own instruction. Two mechanical
answers, both cheap: the run gets directories, never the root
(`.claude/`, `templates/`, `CLAUDE.md` as a file, the project
directory; `agy --add-dir` is repeatable), and the returned report
is scanned for the values of `CLAUDE.local.md` before it is filed -
the scan `docs-check.py` already does for every documentation page
(POS.0950) and which THR.0210 records as missing for reports. The
external run is the reason to build that scan; it then guards the
session reviewers' reports too.

**F3. Read-only is the engine's promise on one engine, a flag on
another and unknown on the third; the forge verifies instead.**
[mechanism; the companion note F2, F6, F7] Codex's default sandbox
is read-only, Claude's tools are listed, Antigravity's headless
behaviour on a denied write is undocumented. A reviewer may change
nothing; the forge can know whether it did: the script takes the
tree's state before the run (`git status --porcelain` and a hash of
the project's files for a project outside git) and refuses the
answer if anything changed. The guarantee then holds on every
engine, present and future, and costs one comparison.

**F4. The report's shape is asked for and checked, not hoped for.**
[verified, the contract's Output; the companion note F2, F6, F7] The
contract fixes the report's Markdown: front-matter, "Overall read",
"Challenges" with five fields each, "What is strong", "Questions I
cannot answer". A model of another family drifts from a shape more
than the one that was tuned on it. Every engine of the companion
note offers a schema option (`--json-schema`, `--output-schema`);
the forge can ask for one field, the report as Markdown, and check
its headings and fields by script before filing, the way the light
check reads shapes today (THR.0530 names it a program since
2026-10-22). A report that fails the shape is returned to the
principal as a failed run, not filed and not numbered. The
`reviewer:` line of the front-matter should say the engine and the
model it reported (`challenger persona architect (…, isolated
context, on antigravity gemini-3.1-pro)`); that is a change of the
contract's template and therefore the principal's decision, as is
whether the engine enters the report's file name beside the
persona (POS.1720 fixes the name's shape; a second challenge of one
persona on one day already differs by time and hash, so the name
needs no engine, and the ledger's row can show it from the
front-matter).

**F5. Filing, numbering and the ledger do not change.** [verified,
`/challenge` steps 1 to 4; CLAUDE.md Ledger] The command files the
returned text word for word, gives each challenge the next
`CHL.NNNN`, completes the name by `forge-report.py`, remakes the
ledger, presents the report and offers the walkthrough. None of
that knows which model wrote the text. The one addition is the
check of F4 between the return and the filing. The critic's road is
the same with `FND` and `reviews/`. Research on another engine is a
job of the same kind - the research skill as the instruction, the
note's shape as the schema - and lands in `research/` with its
index entry written by the command; a check on another engine adds
nothing, because a check is mechanical and is becoming a program
(THR.0530). Order of worth: challenger first, critic second,
research third, check never.

**F6. The "criticise this" job is not a reviewer; it is a
consultation, and its answers are sources.** [reasoning from
POS.1140 and POS.0070; the manual precedent of 2026-10-22] The
principal's `??` asks Claude's own opinion of what he has just
written; the new job asks another model's opinion of what Claude
has just said, with the conversation's substance in the packet.
That breaks the one property that makes a reviewer a reviewer: it
"never sees the working conversation" (POS.1140). So the job is a
different mechanism, and the forge already has its output kind:
on 2026-10-22 the principal carried the packet to Gemini by hand
and the forge stored the three answers as sources with an Origin
and a Role, and the intent cited them by path. The formalised job
keeps that: Claude composes the packet - what the matter is, how it
is being approached, where the work stands, what is asked - shows
it to the principal, sends it on his word, and the packet and each
engine's answer are ingested as one bundle of sources
(`sources/<slug>/` with its `00-INDEX.md`, POS.0180), the packet
Claude's by Origin, each answer its engine's. Nothing enters the
intent because an engine wrote it (POS.0070); the walkthrough
decides. The packet is the formalisation the principal asked for:
a fixed shape of four parts, composed from the conversation, which
is also what makes it readable by a model that saw none of it.

**F7. Several engines on one question: the field's two patterns and
the one the forge already has.** [verified, Karpathy's llm-council
repository 2025-11; the Comfy write-up 2026; preference-leakage
research as summarised in secondary sources] Karpathy's council
sends one question to several models, lets them rank each other's
answers anonymised, and has a chairman write the final answer. The
Comfy team runs one top model each from four labs on every labelled
pull request, two passes each, then one judge of one family reads
the ground truth and throws most of it out, capping at ten; their
argument is that "models from the same lineage share training
priors, so they share blind spots and false alarms" and that "four
of them agreeing is fake consensus"; they admit the clean
experiment is unrun and that the judge may prefer its own family.
The research on judges says the same: a model scores its own and
its siblings' outputs higher ("preference leakage"), the standard
mitigations being hidden authorship and a judge of another family
or a panel. A study often cited against ensembles (arXiv
2606.15689, 2026-04) does not in fact discuss ensembles; it finds
that all five models it tested miss performance bugs alike, a
shared blind spot across families. For the forge this settles two
things. The chairman is the principal: the forge has the
walkthrough, which is a chairman with a verdict line; no ranking
round is needed. And the synthesis is a layout, not a judgement:
Claude, who is one of the families, lays the answers side by side -
where they agree, where they differ, what each alone saw - marks
agreement as consistency and never as validation (POS.0790 already
says so), and puts its own view last and apart (POS.1370). The
engines are named in the layout, never anonymised: the principal
wants to know who said what.

**F8. Waiting and collecting later are one mechanism with a
spool.** [design, from the companion note F13] A run of minutes is
waited for in the session, as a subagent is; a run the principal
does not want to wait for is the same command with a flag: the
script detaches, writes into a spool directory of the project
(`runs/` or under `tmp/`; the name is the principal's) a job file
and, when done, the answer and the envelope, and exits. The map
(`/forge`) reads the spool like every other state made at read time
and reports "runs in flight" and "returned, not filed"; the filing
is the ordinary command's, run on the principal's word when he
returns - which is also when the shape check of F4 and the scan of
F2 run. The spool is state, never in git, like the ledger
(POS.1600); the filed report is the record. Two sessions never
collide on it because every job has the report's own name (date,
time, hash, POS.1720).

**F9. What the external run costs the forge in words.**
[reasoning] One script with the engine table (companion note);
`/challenge` and `/critique` take `--on <engine>[,<engine>]` and
run once per engine, filing one report each, never at once (the
command already says reports are filed one after another); a new
command for the consultation, with the packet's shape as its
template; the contract's `reviewer:` line gains the engine; the
scan of F2 and the check of F4 as parts of the filing step;
`/setup` names the optional CLIs; `/forge` reads the spool. No
agent file changes: the personas and lenses are what is sent.

## Options

**A. Reviewers on another engine through the existing commands, the
consultation as a command of its own.** The persona and contract
are the packet; filing unchanged; the consultation's outputs are a
bundle of sources. Pro: nothing of the chain's logic moves; the
isolation rule stays sharp (a reviewer never sees the conversation,
a consultation always does, and the forge names which is which).
Con: two commands grow a flag, one command is born, one template
line changes - four decisions for the principal.

**B. One new command for everything external (`/ask <engine>
<what>`).** Pro: one door. Con: a reviewer run and a consultation
land in different places with different numbering, so the one door
would carry two procedures; prime directive 10 prefers one mechanism
in one place, and the place of a challenger run is `/challenge`.

**C. A persona per engine (`challenger-gemini-architect`).** Pro: the
roster shows it. Con: the roster doubles with every engine and the
Lens is the same text; the engine is a parameter of the run, not a
persona. Rejected.

**D. The consultation's answers as challenges (`CHL`, in
`challenges/`).** Pro: they challenge substance. Con: they saw the
conversation and are not isolated; filing them as peer reviews would
blur the one distinction the forge makes between a reviewer and an
input. Rejected; they are sources, as on 2026-10-22.

## Relevance to this project

Recommendation: **A**, with the design points above, in this order
of building: the script and `/challenge --on antigravity` first
(the persona `architect` on the solution design is the natural
first run, the three sources of 2026-10-22 its manual baseline),
the scan of F2 and the shape check of F4 with it, the consultation
command second, the spool third, `/critique` and research when the
first two have run a few times.

What belongs to the intent (through `/forge intent`, not here):

- POS.0800 reworded: the direction kept, the mechanics fixed: the
  forge's own persona and contract sent to an engine named at the
  call, through one script, the engine's login the user's and
  outside the forge, Foundry one engine among several without
  priority.
- A new position for the consultation: what it is (a question with
  the conversation's substance, composed by Claude in a fixed packet,
  sent on the principal's word), what it is not (a reviewer), where
  its outputs land (sources, a bundle per consultation) and how
  several answers are laid out (F7).
- POS.0790 gains the engine naming and the "layout, not judgement"
  rule, or a new position cites it.
- THR.0210: the scan of a report for instance values is the guard
  rail the thread waits for; the external run gives it its reason.
- THR.0290 (research on another engine) and THR.0530 (what is a
  program): both touched, neither closed by this note.

What belongs to the brief the principal said he is writing: the
name of the consultation command and of the spool, which engines
come first, whether the engine enters the report's name, what the
packet's four parts are called, and how the quota's unknowability
is lived with (a run reports its usage after; no budget before).

## Sources

- CLAUDE.md of the engine (Isolated reviewers, Working methods,
  Ledger), `.claude/skills/challenger-contract/SKILL.md`,
  `.claude/skills/challenge/SKILL.md`,
  `.claude/agents/challenger-architect.md`, as of commit 4ccf0ee.
- projects/forge/sources/00-INDEX.md, the entries
  repo-detection-challenge, -2, -3 (2026-10-22).
- karpathy/llm-council, 2025-11-22, and its write-ups (Analytics
  Vidhya, 2025-12).
- Comfy, "How we got four rival AI labs to fight over our code
  reviews", blog.comfy.org, 2026.
- Kumar, Bararia, Raj, "Bigger Isn't Always Better: A Comparative
  Evaluation of LLMs for Automated Code Review", arXiv 2606.15689,
  2026-04-09.
- Secondary summaries of "Preference Leakage" (2025) and
  "MLLM-as-a-Judge Exhibits Model Preference Bias" (under review):
  promptlayer.com glossary, themoonlight.io review, tianpan.co
  2026-06-03.
- The companion note's sources for every engine fact.
