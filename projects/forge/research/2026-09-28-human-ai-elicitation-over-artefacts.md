---
project: forge
type: research
topic: elicitation between a human and an AI over an artefact - roles, structure, instruments, completion
date: 2026-09-28
derived_from: 00-brief-elicitation.md v0.5
status: immutable
---

# Elicitation between a human and an AI over an artefact

## Question

How is elicitation between a human and an AI over an artefact
defined in research and in current tools - who leads and who decides,
how the finding is structured, which instruments it uses, and when it
is complete - and what does that say about how the forge should
define the elicitation of an artefact in general?

The question is about the process of finding. What the resulting
documents contain is the subject of a separate note
(`2026-09-28-artefact-layers-from-idea-to-handover.md`) and is out
of scope here. The comparison with the forge stands only in the last
section.

Surveyed on 2026-09-28: the requirements and knowledge elicitation
disciplines (BABOK, SEBoK as the open reading of ISO/IEC/IEEE 29148
and 15288, cognitive task analysis, the literature on stopping and
saturation); mixed-initiative interaction and the guidelines for
human-AI interaction; the research of 2023 to 2026 on LLMs that
interview, ask clarifying questions, co-write and co-create; and the
definitions of six current tools and methods read at source (GitHub
spec-kit, Kiro, the BMad Method, Claude Code's structured questions,
a widely copied PRD prompt, Anthropic Interviewer).

Epistemic tags: **[C]** consensus across disciplines or sources,
**[P]** practice of the tools, not stated as a rule and not tested,
**[E]** emerging, resting on few or recent studies, **[X]**
contested or without agreement.

How the sources were read: every page listed under Sources was
opened in this session through a fetch tool that returns a model's
extraction of the page, not the raw page. Numbers and quotations are
given as the extraction returned them. Five pages that carry the
weight of the recommendation were fetched a second time,
independently, and the two readings agree in every number: Gero et
al., Maier et al., Chi et al., ReqElicitGym and spec-kit's
`clarify.md`. Everything else rests on one reading and is to be
checked against the source before it is quoted onward. Several
primary sources could not be opened (paywall, refused connection,
unreadable PDF); they are named under "What was not found" and
whatever is said of them is marked "unverified, from memory" or
"search result only".

## Key findings

### 1. The disciplines define elicitation as a process with several instruments; the interview is one of them [C]

The business analysis body of knowledge treats elicitation as a
knowledge area of five tasks: prepare for elicitation, conduct
elicitation, confirm elicitation results, communicate business
analysis information, manage stakeholder collaboration. The purposes
readable on the publisher's pages are, for conducting, "to draw out,
explore, and identify" information and, for confirming, "to check the
information" gathered (both truncated by the paywall). A secondary
reading states that the body of knowledge "recognises three types of
elicitation: collaborative, research and experiments": work with
people, work with documents and data, and work with a prototype or a
trial. That elicitation is "ongoing, not a phase" appeared in a
search result only and was not verified on the page.

The systems engineering body of knowledge (SEBoK 2.14, which cites
ISO/IEC/IEEE 29148:2018 and 15288:2023 as its primary references)
lists the same spread of instruments for eliciting stakeholder needs:
structured brainstorming workshops, interviews and questionnaires,
focus groups, visual and descriptive content, review of technical,
operational and strategy documentation, and feedback from
verification and validation.

Cognitive task analysis, the discipline of drawing knowledge out of
experts, runs in five phases of which elicitation is the second:
background preparation ("getting familiar with the domain"),
elicitation, analysis, knowledge representation, application. The
elicitor studies the domain before asking anything.

Sources: IIBA BABOK Guide chapter 4 index pages; BA Coach
(2020-10-04); SEBoK, Stakeholder Needs Definition (v2.14,
2026-05-18); Global Cognition, Cognitive Task Analysis (updated
2021-09-20).

### 2. Confirmation is a task of its own, and it is the only completion test the disciplines agree on [C]

In the body of knowledge, confirming what was elicited is a separate
task after conducting. In SEBoK the integrated set of needs must be
"correct, consistent, complete, and feasible", and the test is that
the team "has confirmation from the stakeholders" that their needs
are properly communicated, supported by traceability. Completeness
is thus not measured against the world but declared by the owner of
the need, on a text put back in front of him.

Unverified, from memory: the body of knowledge names the output of
conducting "elicitation results (unconfirmed)" and the output of
confirming "elicitation results (confirmed)", which is an epistemic
status carried on the material itself. The pages that would verify
this are behind the paywall.

### 3. No stopping rule proves completeness; the evidence is that elicitors, human and AI, stop too early [X for the rule; E for the evidence, one study of human analysts and recent benchmarks of models]

- Pitts and Browne (AMCIS 1998; the journal version of 2004 was not
  opened) studied how analysts decide that enough has been gathered.
  Their abstract: "the cognitive limitations of analysts result in
  flawed application and evaluation of stopping rules, producing
  premature termination", and "the use of a strategic prompting tool
  reduces the risk of premature stopping".
- Saturation, the stopping rule of qualitative research, is examined
  by Saunders et al. (Quality and Quantity, 2018). They find four
  different models under the one word and conclude that saturation
  is "essentially a predictive statement about the unobserved based
  on the observed": it cannot be tested, only argued.
- ReqElicitGym (2026-02-20) measures LLM interviewers against
  hidden requirements in 101 scenarios with a simulated user. The
  best-performing model reached a ratio of implicit requirements
  elicited of 0.32, that is, about two thirds of the implicit
  requirements stayed undiscovered; requirements about style stayed
  near zero; the models ended their interviews on their own after
  3.86 to 19.98 turns on average.
- LLMREI (2025-07-03), 33 interviews with students playing
  stakeholders: the interviewing chatbot elicited 60.94 % of the
  requirements completely and 12.76 % partially.
- RegretBench (2026-07-23) treats clarification as a sequence of
  decisions, "whether to ask, what to ask, when to stop, and when to
  answer", and reports that models with similar final accuracy
  differ substantially in their stopping decisions.

What practice puts in the place of a proof is a declared status. The
clearest instance found is spec-kit's clarify step (finding 5): it
stops when the critical ambiguities are resolved, when the human
says he is done, or when the quota of questions is spent, and then
reports every category of its map as Resolved, Deferred, Clear or
Outstanding. Kiro stops at approval gates: "Confirm when requirements
meet your needs".

### 4. Who leads and who decides: the tools give the pen to the AI and the approval to the human; none says who owns the words [P]

| Tool or method | Who writes | Who asks | Who decides | Stated stance |
|---|---|---|---|---|
| Kiro, requirements-first (page dated 2026-09-25) | the AI generates requirements, design and tasks from a prompt | not described; the human is told to be explicit in the prompt | the human confirms at each of three gates | "Your role: Review requirements for completeness" |
| Kiro, Quick Spec | the AI, all three documents in one pass | the AI, up front | no gates | for "well-understood features" |
| spec-kit, specify and clarify | the AI writes the spec and integrates every answer into it | the AI, from its own scan | the human answers; the AI recommends an option | none on roles |
| BMad Method | the AI, in a workflow led by a named agent | the AI facilitates | the human picks the method and accepts or discards | "guided collaboration ... without handing over judgment" |
| Claude Code, structured questions | the AI | the AI generates questions and options; the host application cannot add its own | the human selects or types | used "rather than guessing" |
| Anthropic Interviewer (2025-12-04) | the AI drafts the interview plan | the AI interviews | human researchers review the plan and the analysis | the interviewee is a respondent, not an author |

Three things follow. First, in every tool the initiative over the
questions is the AI's and the approval is the human's; the human
steers by the opening prompt and by the gate. Second, in every tool
the text is the AI's and the human edits or approves it. Third, no
tool's definition read here says who owns the wording or
distinguishes the human's words from the AI's in the artefact.

The classical disciplines split the roles differently: the elicitor
steers the process and owns the record, the stakeholder owns the
content and confirms it (findings 1 and 2).

Mixed-initiative interaction, the research tradition behind the
question of who holds the initiative, gives principles rather than
roles. The abstract of Horvitz's paper (CHI 1999) speaks of "an
elegant coupling of automated services with direct manipulation".
Unverified, from memory, since the paper's text could not be read:
its principles include considering uncertainty about the user's
goals, employing dialogue to resolve key uncertainties while
weighing the cost of bothering the user, allowing efficient direct
invocation and termination, and minimising the cost of poor guesses.
Its descendant, the eighteen guidelines for human-AI interaction
(Amershi et al., CHI 2019, read in the publisher's HAX library),
carries the same points: G2 "Make clear how well the system can do
what it can do", G8 "Support efficient dismissal", G9 "Support
efficient correction", G10 "Scope services when in doubt: engage in
disambiguation or gracefully degrade". A scoping review of twenty
years of mixed-initiative systems in visual analytics (2025, revised
2026) finds that the literature "lacks consensus on the definition of
mixed-initiative systems" **[X]**.

### 5. A coverage map is held by the elicitor and reported as status; it becomes an interrogation only when it is read out [P, with E support]

spec-kit's clarify command is the most explicit definition found of
a map that is not a questionnaire:

- the AI scans the specification against a fixed taxonomy of
  categories (functional scope, domain and data, interaction flow,
  quality attributes, integrations, edge cases, constraints and
  trade-offs, terminology, completion signals, and a catch-all) and
  marks each Clear, Partial or Missing;
- questions are generated only from the gaps, ranked by impact;
- "Maximum of 5 total questions across the whole session",
  "EXACTLY ONE question at a time", each with a sentence on why it
  matters and a recommended answer with its reason; the human may
  accept the recommendation in a word or answer freely;
- the queue of future questions is never shown;
- each answer is logged under a dated Clarifications heading as
  question and answer, and integrated into the specification at once;
- the closing report is a table of category against status:
  Resolved, Deferred, Clear, Outstanding.

The taxonomy is never put to the human. He sees at most five
questions and, at the end, the state of the whole map.

The same pattern in the other disciplines:

- The critical decision method of cognitive task analysis lets the
  expert tell the incident without interruption and then goes back
  over it in several sweeps with probes; the interviewers "are not
  asking questions in lock-step fashion".
- Anthropic Interviewer builds an interview plan that keeps the same
  research questions across all interviews and leaves room for
  tangents; a human reviews the plan before any interview runs.
- OntoAgent (RE 2026) gives the interviewing agent an "experience
  ontology" of concerns to select from before it words a question,
  and reports a 33 % improvement in the share of hidden requirements
  found over existing methods on the ReqElicitGym benchmark.
- Pitts and Browne's strategic prompting tool (finding 3) is a map
  in the same sense: prompts for the analyst, not questions for the
  user.

Two results on the shape of the single question. Shen, Singhal and
Breaux (2025-07-03) find GPT-4o's follow-up questions no worse than
human ones unguided, and preferred in 87 of 128 pairs when the model
was guided by a list of fourteen interviewer mistakes (among them:
failing to elicit tacit assumptions, asking for solutions, asking
long or vague questions, mixing several kinds of requirement in one
question). Zhang et al. (HCOMP 2026), fifteen voice interviews led
by a model: 28.7 % of the question turns stacked several questions
and lost information by it, deepening probes were 4.9 % of all
turns, and acknowledgements 27.1 %. One question at a time is thus
both the tools' rule and the measured weak point of an unguided
model.

### 6. When to ask and how much: the tools cap the questions at three to five and allow the informed guess; models left to themselves ask too little [P for the caps; E for the default behaviour, three studies that agree]

| Source | Cap | Format | Rule for asking |
|---|---|---|---|
| spec-kit, specify | 3 open markers in the draft | all together, options in a table | a marker only where the choice changes scope, several readings exist and no reasonable default exists; priority "scope > security/privacy > user experience > technical details" |
| spec-kit, clarify | 5 questions per session | one at a time, recommendation first | highest impact first; stop early if resolved |
| ai-dev-tasks, create-prd | 3 to 5 | numbered, lettered options, answered as "1A, 2C, 3B" | "Only ask questions when the answer isn't reasonably inferable" |
| Claude Code, AskUserQuestion | 1 to 4 questions per call, 2 to 4 options each | multiple choice, free text possible | when the task has "multiple valid approaches" |

No tool gives a reason for its number. A request to raise spec-kit's
limit exists in its issue tracker (search result only, not opened).

The research on models without such a scaffold points the other
way. Su and Cardie (2026-05-24) find that models recognise an
ambiguous question 60 to 80 % of the time when asked to judge it,
and ask a clarifying question in 0 to 5 % of cases when left to
answer; retrieved context makes them ask less. Zhang, Knox and Choi
(ICLR 2025) trace the habit to training on single turns and show a
modest gain from training on simulated future turns. ReqElicitGym
finds that "All LLMs strongly favor probing over clarification".
Over-questioning as a measured failure of models was looked for and
not found; it appears only as the concern the tools' caps answer.

The other direction of elicitation holds as well: Li, Tamkin,
Goodman and Andreas (2023, ICLR 2025) show in preregistered
experiments that a model asking open questions draws out responses
"often more informative than user-written prompts", with less
reported effort, and surfaces considerations the users had not
anticipated.

### 7. The further the AI goes into the drafting, the better the text and the weaker the human's ownership of it [E, four controlled studies that agree]

| Study | Design | Result |
|---|---|---|
| Gero et al., DIS 2026 | 253 writers, essay; AI at planning, at drafting, at revision, or none | ownership 6.74 with no AI, 6.30 planning, 5.57 revision, 4.28 draft (scale of 1 to 7); quality 5.69, 5.85, 5.79, 7.27 (scale of 0 to 9): "an ownership-quality tradeoff, in which an AI-generated draft buys high quality essays at a noticeable ownership cost" |
| Maier, Schneider and Feuerriegel, CHI 2026 | 486 and 640 participants, idea generation; the model rewrites on its own, or asks questions, or offers suggestions | "the model-led mode substantially improved idea quality but reduced idea diversity and users' perceived idea ownership"; the question mode "also improved idea quality, yet while preserving diversity and ownership" |
| Chi et al., 2026 | 470 participants, 332 of them at the follow-up; personal goals written by themselves or by a model from the same reflection | model-written goals far better formed (d of 2.26 in size); ownership 6.22 against 4.19; after two weeks 72.8 % against 46.6 % had acted on two or more goals; psychological ownership mediated the effect on every motivational outcome measured |
| Qin et al., CHI 2025 | 60 writers, ideation; the model from the start or after independent ideation | from the start: fewer original ideas and lower creative self-efficacy; the authors recommend delaying the model |

Two further results bear on whose thought the text is. Jakesch et
al. (CHI 2023, 1,506 participants): a writing assistant configured
to favour one view changed what the participants wrote and shifted
their opinions in a later survey. Sharma et al. (2023, revised
2025): five assistants consistently showed sycophancy, and people
"sometimes" prefer a convincingly written sycophantic answer to a
correct one. Wasi et al. (2024): people decline ownership of a
model's text and still submit it as theirs; being reminded of their
own contribution raises the sense of ownership.

The limits of this evidence are plain: short tasks, crowdworkers or
students, topics the participants did not bring themselves. No study
found measured a domain expert working for days on a document of his
own.

### 8. Drafting early is attested as a technique; its known cost is finding 7 and its known mitigations are few [P]

Prototyping is a named type of elicitation in the body of knowledge
("experiments", finding 1). The straw-man proposal, a knowingly
imperfect text put forward to provoke a reaction because people say
more readily what they do not want than what they want, is
described in practitioner sources (search results only; the pages
refused the fetch). No controlled study of the straw man was found.

Mitigations found at source:

- Gero et al. propose three: "Fade-out AI interactions", "Provide
  incomplete text that requires rewriting" and "Turn the chatbox
  into a writing space".
- Maier et al. propose that "the human initially generates ideas,
  while the LLM primarily asks questions that prompt elaboration and
  reflection".
- The BMad Method's "advanced elicitation" is a second pass over
  what the model has just produced: the model proposes five named
  reasoning methods (pre-mortem, first principles, inversion, red
  team against blue team, Socratic questioning and others), the
  human picks one, sees the original beside the proposed
  improvement, and chooses accept, discard, repeat or iterate. The
  draft is attacked before it is adopted.

### 9. The divergent and convergent model is the accepted picture of "wide finding, narrow choice"; nothing found tests it for work with an AI [C as a model, no evidence for the transfer]

The Design Council's Double Diamond shows two diamonds, each a
divergent movement followed by a convergent one: discover and
define, develop and deliver. The Council says of it that it is not
linear, a finding may "send them back to the beginning", and that
it is "not an instruction manual". The BMad Method's brainstorming
workflow follows the first diamond literally: towards a hundred or
more ideas, shifting the creative domain "to prevent clustering",
before anything is organised. Finding 7 adds what the picture does
not say: in the divergent half a model narrows the spread of ideas
unless the human goes first or the model is held to questions.

### 10. AI-led interviewing works where the human is a respondent; how it does where the human is the author is not shown [E]

Geiecke and Jaravel (CEPR discussion paper, 2024-11-22) built an
open platform for interviews led by one model and assessed it
"by drawing comparisons to human experts" and by respondents'
ratings; that the interviews were rated comparable to an average
human expert is a search result only. Anthropic Interviewer
(2025-12-04) ran 1,250 interviews of 10 to 15 minutes; 97.6 % of
participants rated their satisfaction 5 or higher and 96.96 % felt
the conversation captured their thoughts; the authors name the
limits themselves: self-report, no non-verbal cues, participants
who knew an AI was asking. LLMREI made about as many interviewer
mistakes as human interviewers. Against these stand the coverage
and depth results of findings 3 and 5. In all of them the human
answers and someone else writes; none is a case of two parties
finding one document.

### 11. How sure a claim is: the tools mark what is open, not what is unverified; words work, and the wording matters [P and E]

spec-kit marks what is undecided in the text itself, keeps a dated
log of question and answer, and ends on the four statuses of finding
5. Guideline G2 of the human-AI guidelines asks a system to make
clear how well it can do what it does. Kim et al. (FAccT 2024, 404
participants): an answer that expresses uncertainty in the first
person ("I'm not sure, but...") lowered agreement with the system
and raised the participants' accuracy by reducing overreliance on
wrong answers; the impersonal form ("It's not clear, but...") had a
weaker effect that was not significant. A systematic review of
generative AI in requirements engineering (238 papers, revised
2025-10-14) names hallucination as a barrier in 63.4 % of them and
finds 1.3 % of the studied applications in production. No tool read
here marks a single statement as verified, unverified or hypothesis.

## Options and trade-offs

The options concern how a definition of the elicitation of one
artefact type is framed in general, not any particular artefact.

**A. Gate model: the AI drafts, the human approves.** The shape of
Kiro and of most product tools: a prompt, a generated document, a
confirmation at the gate.
*For:* fastest; the best-formed text (finding 7); simple to define.
*Against:* the text and the questions are both the AI's; the
strongest evidence found says ownership falls and action on the
result with it; nothing in the model says what was looked at and
what was not.

**B. Interview model: the AI asks, the human answers, the AI
writes up.** The shape of spec-kit's clarify step, of the PRD
prompts and of the interviewing agents.
*For:* draws out what a prompt does not (finding 6, Li et al.); the
cap and the one-question rule keep it bearable; a coverage status
at the end.
*Against:* an interview is one instrument of several (finding 1);
models probe rather than clarify and stop early (findings 3 and 5);
the human is a respondent, and the write-up is still the AI's
wording.

**C. Process model with a map, stated roles and a declared
completion.** A definition that names, per artefact type: what the
finding starts from; what is true of the artefact at the end and
whose word closes it; who holds the initiative and who the decision,
by phase; a map of what must be looked at, walked by the AI and
reported as status rather than read out as questions; the
instruments beside the interview; the course. This is the shape of
the disciplines (findings 1, 2 and 5) applied to two parties.
*For:* the only option in which completion, roles and coverage each
have a stated place; consistent with every consensus finding.
*Against:* the most to define and to keep; no tool or study found
has tested it as a whole; its parts are evidenced, their
combination is not.

**D. Phased initiative.** Option C with the rule of finding 7 made
explicit: the human states his own thought first, the AI widens
after that, the AI's drafts are rough on purpose and are attacked
before they are adopted, and in the convergent half the AI asks
rather than rewrites.
*For:* follows the four controlled studies.
*Against:* the studies are of short tasks with lay participants; an
expert who wants a full proposal to react to may be slowed for a
risk that is his to take; the order cannot be forced on a thought
that arrives already written.

## What was not found

Looked for and not found:

- a definition, in research or in a tool, of elicitation between
  one human and an AI over a document as a named process with
  stated roles; the nearest are the workflows of the tools;
- any statement in a tool's definition of who owns the wording;
- a stopping rule that establishes completeness; every source
  substitutes confirmation, a status or a quota;
- a reason for the caps of three to five questions;
- a controlled comparison of one question per message against
  several at once; the nearest is the information lost to stacked
  questions in voice interviews (Zhang et al., 2026);
- a study of AI-led or co-led elicitation with a domain expert on
  his own real work over more than one sitting;
- a controlled study of the straw-man proposal as an elicitation
  technique;
- any tool that keeps the status verified, unverified or hypothesis
  on individual statements;
- a test of the divergent and convergent model for document work
  with an AI.

Found not to hold:

- that mixed-initiative interaction has an agreed definition (the
  scoping review says it does not);
- that models over-question by default: the measured default is the
  opposite, they answer where they should ask.

Could not be opened, and therefore not used as evidence:

- the body text of the BABOK Guide, chapter 4 (paywall; only the
  index and truncated purposes were readable);
- ISO/IEC/IEEE 29148:2018 itself (read only through SEBoK);
- Horvitz 1999 and Amershi et al. 2019 in full text (unreadable
  PDF, refused page); the first is represented by its abstract, the
  second by the publisher's guideline library;
- Bano et al. 2019 on interviewers' mistakes; Pitts and Browne 2004
  and 2007; Hoffman, Crandall and Shadbolt 1998 on the critical
  decision method; the full text of Geiecke and Jaravel;
- laddering and the repertory grid as interviewing techniques: the
  knowledge acquisition bottleneck of expert systems was confirmed
  from a tertiary source only, laddering not at all;
- the practitioner pages on the straw man.

## Relevance to this project

The forge's draft brief on elicitation holds that elicitation is a
process of finding in which the interview is one instrument beside
research and sources, and proposes seven blocks per artefact type:
Target, Inputs, Aim, Partner, Map, Instruments, Course.

What the outside confirms:

- The thesis is the disciplines' consensus, not a novelty (finding
  1): collaborative, research and experiment are the three types of
  elicitation, and preparation of the domain comes first.
- Aim as the one place of completion, closed by the principal's
  word, is what the disciplines do: completion is confirmed by the
  owner, never proven (findings 2 and 3).
- A Map that is "not a questionnaire", walked at the closing, is the
  pattern of spec-kit, of the critical decision method and of the
  prompting tool that kept analysts from stopping early (finding 5).
- Reflect back before the write is the disciplines' confirmation
  task; one question per message is the tools' rule and the measured
  weakness of an unguided model.
- Partner as a block of its own has no counterpart in any tool: the
  forge would state what the tools leave silent (finding 4).
- How sure a claim is, said in words, has support, with the detail
  that the first person works and the impersonal form hardly does
  (finding 11).

What the outside has and the draft does not:

- A recorded status per area of the Map at the closing walk. The
  draft asks whether each area was "consciously considered"; the
  practice found writes the answer down per area, in a small fixed
  set of states.
- A statement of the order of initiative. The draft describes the
  AI as the active one at the opening of a brief and draws its
  inspiration from a first answer that was a whole architecture.
  The controlled evidence (finding 7) points to the human's own
  statement first, the AI's widening after it, and rough rather than
  finished proposals.
- An attack on the AI's own draft before it is adopted (finding 8).

**Recommendation:** option **C**, which is the seven blocks as
drafted, with three additions put to the principal as positions for
the intent, each his to take or leave:

1. The closing walk of the Map records one state per area, in words
   the principal chooses (the outside uses resolved, deferred, clear
   and outstanding), so that "considered and left open" is visible
   and distinct from "not looked at".
2. The Partner block of every definition says who holds the
   initiative in the wide part of the finding and who in the
   narrowing, and the shared mechanism says once, for all
   artefacts, that the principal's own statement of the thought
   comes before the AI's proposal wherever the thought does not
   arrive already written.
3. A proposal of the AI's that is meant to draw out a reaction is
   offered rough and named as a proposal, and how sure its claims
   are is said in the first person.

Two matters are raised as questions rather than recommended, since
they touch what the principal has said he wants and the evidence is
of short tasks with lay participants:

- Does the active opening the draft gives the AI in a brief stand as
  written, against the finding that a model used from the start
  narrowed the ideas and lowered ownership?
- Does "draft early" keep the extreme form of the draft's
  inspiration, a whole proposal as the first answer, against the
  ownership and quality trade-off of finding 7?

Option D is the fallback if the principal wants the order of
initiative as a rule rather than as a stance. Options A and B are
what the tools do and what the forge's roles already exclude.

## Sources

All accessed 2026-09-28.

Tools and methods:

- GitHub spec-kit, command template `clarify.md` - https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/clarify.md - GitHub, undated (main branch)
- GitHub spec-kit, command template `specify.md` - https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/specify.md - GitHub, undated (main branch)
- GitHub spec-kit, README - https://github.com/github/spec-kit - GitHub, undated
- Kiro documentation, Specs - https://kiro.dev/docs/specs/ - Kiro, page dated 2026-08-27
- Kiro documentation, Requirements-First - https://kiro.dev/docs/specs/feature-specs/requirements-first/ - Kiro, page dated 2026-09-25
- BMad Method, README - https://github.com/bmad-code-org/BMAD-METHOD - BMad Code, undated
- BMad Method documentation, Skills and Agents - https://docs.bmad-method.org/reference/skills-and-agents/ - BMad Code, undated
- BMad Method, Advanced Elicitation (third-party mirror of the project's documentation; the project's own page now redirects) - https://mintlify.wiki/bmad-code-org/BMAD-METHOD/advanced/elicitation - undated
- Claude Code documentation, Handle approvals and user input - https://code.claude.com/docs/en/agent-sdk/user-input - Anthropic, undated
- snarktank, ai-dev-tasks, `create-prd.md` - https://raw.githubusercontent.com/snarktank/ai-dev-tasks/main/create-prd.md - GitHub, undated
- Introducing Anthropic Interviewer - https://www.anthropic.com/research/anthropic-interviewer - Anthropic, 2025-12-04

Disciplines:

- BABOK Guide, 4 Elicitation and Collaboration (index only, body behind paywall) - https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/4-elicitation-and-collaboration/ - IIBA, undated
- The Business Analysis Standard, Elicitation and Collaboration (index only) - https://www.iiba.org/knowledgehub/the-business-analysis-standard/5-applying-business-analysis-tasks/5-3-business-analysis-knowledge-areas/elicitation-and-collaboration/ - IIBA, undated
- Elicitation and Collaboration - https://bacoach.nl/2020/10/elicitation-and-collaboration/ - BA Coach, 2020-10-04 (secondary)
- Stakeholder Needs Definition - https://sebokwiki.org/wiki/Stakeholder_Needs_Definition - SEBoK v2.14, 2026-05-18
- W. Sieck, What is Cognitive Task Analysis? - https://www.globalcognition.org/cognitive-task-analysis/ - Global Cognition, updated 2021-09-20 (secondary)
- Knowledge acquisition - https://en.wikipedia.org/wiki/Knowledge_acquisition - Wikipedia, last edited 2026-07-02 (tertiary)
- M. Pitts, G. Browne, Investigating Evaluative Stopping Rules in Information Requirements Determination - https://aisel.aisnet.org/amcis1998/265/ - AMCIS 1998 Proceedings (abstract)
- B. Saunders et al., Saturation in qualitative research: exploring its conceptualization and operationalization - https://pmc.ncbi.nlm.nih.gov/articles/PMC5993836/ - Quality and Quantity 52(4), 2018 (online 2017)
- The Double Diamond - https://www.designcouncil.org.uk/resources/the-double-diamond/ - Design Council, undated

Mixed initiative and human-AI interaction:

- E. Horvitz, Principles of Mixed-Initiative User Interfaces (abstract only) - https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/ - Microsoft Research, CHI 1999
- HAX Design Library, the eighteen Guidelines for Human-AI Interaction - https://www.microsoft.com/en-us/haxtoolkit/library/ - Microsoft, undated (guidelines of Amershi et al., CHI 2019)
- S. Monadjemi et al., A Scoping Review of Mixed Initiative Visual Analytics in the Automation Renaissance (abstract) - https://arxiv.org/abs/2509.19152 - arXiv, 2025-09-23, revised 2026-06-09

LLMs that interview and ask:

- A. Korn, S. Gorsch, A. Vogelsang, LLMREI: Automating Requirements Elicitation Interviews with LLMs - https://arxiv.org/abs/2507.02564 and https://arxiv.org/html/2507.02564v1 - arXiv, 2025-07-03
- Y. Shen, A. Singhal, T. Breaux, Requirements Elicitation Follow-Up Question Generation - https://arxiv.org/html/2507.02858 - arXiv, 2025-07-03
- D. Jin et al., ReqElicitGym: An Evaluation Environment for Interview Competence in Conversational Requirements Elicitation - https://arxiv.org/html/2602.18306 - arXiv, 2026-02-20
- D. Jin et al., From Chat to Interview: Agentic Requirements Elicitation with an Experience Ontology (abstract) - https://arxiv.org/abs/2605.05828 - arXiv, 2026-05-07, RE 2026
- M. Salgado Neto, A. Araujo, R. de Souza Santos, Collaborative and AI-Supported Requirements Elicitation: An Empirical Study (abstract; read, not cited in a finding) - https://arxiv.org/abs/2606.24060 - arXiv, 2026-06-23
- H. Cheng et al., Generative AI for Requirements Engineering: A Systematic Literature Review (abstract) - https://arxiv.org/abs/2409.06741 - arXiv, 2024-09-10, revised 2025-10-14
- J. Su, C. Cardie, Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions - https://arxiv.org/html/2605.25284v1 - arXiv, 2026-05-24
- M. N. Ta et al., One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies (abstract) - https://arxiv.org/abs/2607.21143 - arXiv, 2026-07-23
- M. J. Q. Zhang, W. B. Knox, E. Choi, Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions (abstract) - https://arxiv.org/abs/2410.13788 - arXiv, 2024-10-17, ICLR 2025
- B. Z. Li, A. Tamkin, N. Goodman, J. Andreas, Eliciting Human Preferences with Language Models (abstract) - https://arxiv.org/abs/2310.11589 - arXiv, 2023-10-17; ICLR 2025 per search result
- F. Geiecke, X. Jaravel, Conversations at Scale: Robust AI-led Interviews with a Simple Open-Source Platform (abstract) - https://cepr.org/publications/dp19705 - CEPR DP19705, 2024-11-22
- H. Zhang et al., When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews - https://arxiv.org/html/2608.10412v1 - arXiv, 2026-08-11, HCOMP 2026

Co-writing, co-creation, ownership, reliance:

- K. I. Gero, T. Long, C. Schnitzler, P. S. Dhillon, From Planning to Revision: How AI Writing Support at Different Stages Alters Ownership - https://arxiv.org/html/2604.11009 - arXiv, DIS 2026
- S. Maier, M. Schneider, S. Feuerriegel, Partnering with Generative AI: Experimental Evaluation of Human-Led and Model-Led Interaction in Human-AI Co-Creation - https://arxiv.org/abs/2510.23324 and https://arxiv.org/html/2510.23324 - arXiv, 2025-10-27, revised 2026-03-09, CHI 2026
- V. B. Chi et al., Optimized but Unowned: How AI-Authored Goals Undermine the Motivation They Are Meant to Drive - https://arxiv.org/html/2605.12344v2 - arXiv, v2 of 2026-08-24
- P. Qin et al., Timing Matters: How Using LLMs at Different Timings Influences Writers' Perceptions and Ideation Outcomes in AI-Assisted Ideation (abstract) - https://arxiv.org/abs/2502.06197 - arXiv, 2025-02-10, CHI 2025
- M. Jakesch et al., Co-Writing with Opinionated Language Models Affects Users' Views (abstract) - https://arxiv.org/abs/2302.00560 - arXiv, 2023-02-01, CHI 2023
- A. T. Wasi, M. R. Islam, R. Islam, LLMs as Writing Assistants: Exploring Perspectives on Sense of Ownership and Reasoning - https://arxiv.org/html/2404.00027v3 - arXiv, 2024-04-22 (workshop paper, weak source)
- M. Sharma et al., Towards Understanding Sycophancy in Language Models (abstract) - https://arxiv.org/abs/2310.13548 - arXiv, 2023-10-20, revised 2025-05-10
- S. S. Y. Kim et al., "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust (abstract) - https://arxiv.org/abs/2405.00623 - arXiv, 2024-05-01, FAccT 2024
