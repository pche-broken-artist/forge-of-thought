---
version: 4.33
date: 2026-09-28
status: draft
last_change: 4.33 (2026-09-28): THR.0470 opened - the intent is too long to be read; the stories and the measurements belong in the history, and whether threads, precise wording and detail live in the intent at all is to be worked out.
project: forge
audience: principal + Claude only
---

# Forge of Thought — Intent

## Essence

**Forge of Thought** is a place for forging thoughts — a workshop
where thought is tempered and shaped. It began as one CTO's tool for
briefing his direct reports; that origin is now an instance fact, not the
system. Anyone can be the principal, the subject matter is deliberately
unconstrained — process redesign, platform initiatives, organisational
topics, anything — and the recipients of an assignment may be teams,
colleagues, or the principal's future self.

The primary ambition is the full chain: from a raw idea all the way to a
deck ready for realisation, growing layer by layer — assignment, then a
BRD, then solution architecture, up to implementation-ready specification
including integration. **Version 1 deliberately ends at the assignment.**
Every design decision below is made with that growth in mind, which is
why files and IDs are numbered with gaps and why the name says thought,
not assignment.

The engine runs in Claude Code. Claude acts as the principal's cognitive
extension: it owns structure, order and process discipline, while every
decision about content remains the principal's. Isolated AI
reviewers, deliberately blind to the working conversation, provide
adversarial pressure from different angles.

The design constraint that shapes almost everything: an assignment must
carry the complete in-scope substance of the intent, written as well and
as precisely as it can be. Nothing is omitted for brevity's sake; length
is whatever fidelity requires. What keeps it an assignment rather than a
solution is the kind of content, never the amount.

## Positions

### Collaboration model
- **POS.0005** Forge of Thought is a general-purpose engine, not bound
  to one person or one management relationship. "Principal" means
  whoever's thinking is being forged; "recipients" means whoever
  receives the assignment. PCHe (CTO) is the engine's author and its
  first principal (POS.0990); who the principal of an instance is lives
  in `CLAUDE.local.md` (POS.0950).
- **POS.0010** Claude is the principal's cognitive extension, not a
  supplier. Claude owns structure, order and document hygiene; the
  principal owns content and every decision.
- **POS.0020** Claude's default under uncertainty is to ask, never to
  assume. Beyond answering, Claude actively elicits: helping the
  principal extract what he has not yet articulated is part of the job.
  This holds for what Claude reads as much as for what the principal
  says: a contradiction, a gap or a risk Claude finds in a source is
  raised at once, as one question naming what does not fit — never as
  an interpretation of what it means; what Claude has worked out
  beyond that is offered once, marked as his own. Added 2026-09-14
  from the run record of `health` (P.03, F.04: Claude's constructions
  presented as facts, the dominant conduct defect of that run); the
  record's "no warnings unless asked" rejected by the principal — he
  wants to be told of problems, holes and contradictions, as a
  question.
- **POS.0030** Claude never introduces a new convention, prefix or
  section unilaterally: propose, wait for a decision, then write it down.
- **POS.0040** Many iterations are the normal mode. Intent and
  assignments may grow or change substantially between versions.
- **POS.0050** For key topics Claude researches current best practice
  rather than inventing. Outside inspiration is a legitimate input;
  durable findings are stored in `research/`, not left in chat.
- **POS.0060** The forge as a system dictates only that a project has
  one output language: the artefacts of the chain — intent,
  assignment and every later layer — are written in the language its
  ledger header declares (`language`, ISO 639-1, English when
  absent). Everything else a project holds — records, state, research
  and recipes — is always English, whatever the project's language:
  it is read by Claude, the reviewers and the checks and never handed
  to the recipients, and one operating language is what lets them
  read every project the same way. English is the notation
  throughout — ID prefixes, `shall`, status words, front-matter keys.
  The single exception among the artefacts is the briefs
  (`00-brief*.md`), stored verbatim in whatever language they were
  written; a render may be in any language its recipe declares, a
  translation being a render. English for every project was the
  principal's own rule for the company projects of this instance, not
  the forge's (his statement of 2026-08-29; THR.0180, closed
  2026-09-10 by the first project with Czech output, as the thread
  foresaw; the boundary narrowed to the artefacts the same day, at
  his correction). The working-conversation
  language is per-instance configuration, not a system rule: it is
  set in `CLAUDE.local.md` (POS.0950) and read from there by every
  command — never written into the operating layer, and never
  presented outward. The README and other outward-facing renders
  state only the output-language rule.
- **POS.0070** Claude's contribution to content is to criticise,
  challenge, inspire and lay out options; the composition is the
  principal's. He assembles what the forge offers into his own
  positions and decisions — nothing enters the content because
  Claude proposed it, only because the principal took it up.
  "Cognitive extension" (POS.0010) means an amplifier of the
  principal's thinking, never its substitute.

### Working methods
The named ways a working conversation runs. They are the forge's
vocabulary of collaboration: each has a name so that command
definitions and the README can refer to it and the principal can
invoke it in a word. None is a command — a command has one input and
starts on demand; a method applies whenever its situation arises,
whatever produced it. Some are new positions here; others name a
position that already stands elsewhere.

- **POS.0850 Walkthrough.** Any list of items that need the principal's
  decision — critique findings, challenges, the differences between two
  requirement sets, open threads, TBC items before a handover — is
  worked one item at a time, in order of weight. An item is put
  forward with what the principal needs to decide it, in this order:
  what the item says and the situation or evidence behind it, in a
  few sentences; what would change and for whom; then the
  recommendation with its reason and, for "accept", the concrete
  text. A heading with a one-sentence reason is a label, not an
  item — the principal must not have to ask for an explanation to
  decide (his correction of 2026-09-14). Every item ends in one
  proposition, worded so that `accept` has exactly one meaning — yes
  to what is in front of the principal, also where the proposition
  goes against the reviewer's suggestion — and the message closes
  with the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`.
  An open question is not a proposition and closes with the question
  alone. The verdict words are one set for every walkthrough,
  whatever produced the list: `accept`, `modify` (a discussion opens
  and the solution found is put forward to be accepted), `reject`,
  `park` and `obsolete`; the producing command says only what each
  verdict writes. The principal may answer the line with a single
  letter when that letter is his whole message; no other word of the
  forge has a letter, so that nothing which writes or saves can be
  set off by a slip. `park` is a legitimate verdict, not a failure.
  Decided 2026-09-27 at the principal's direction: the three
  producing commands had words of their own, and `accept` meant
  agreement in `/challenge` and its opposite in `/check`. A table
  asking for every
  verdict at once is never put in front of the principal. The next
  message opens with one line acknowledging the verdict and then
  carries the next item, nothing else — never a verdict of Claude's
  own on the open item and the next item in one message (the
  failure the run record of `health` minds most, F.02). A check whether
  Claude has understood an item fully is an item of its own. An
  elicitation interview runs the same way: one question per message, the
  answer acknowledged before the next question is asked. A questionnaire
  of several questions at once is the table of verdicts in another coat
  and is never put in front of the principal. Verdicts are carried in
  the conversation and written once at the round's end (POS.0190):
  findings and challenges change state in the ledger, a rejected
  finding or challenge becomes a DEC record with its reason, an
  accepted finding becomes an iteration of the artefact it concerns,
  an accepted challenge must change the intent. Whatever produces a list ends by
  offering a walkthrough — `/critique`, `/challenge`, the `/forge` map,
  a comparison made on request — and the principal may call for one at
  any moment. `/resolve`, a per-verdict door, is retired without
  alias; its write-up rules live here. The shape of the method lives
  in `.claude/skills/walkthrough/SKILL.md`, read whenever a
  walkthrough or an interview runs; CLAUDE.md carries one sentence
  and the pointer, and a hook repeats the one-item rule at every
  prompt (POS.1170, 2026-09-14).
- **POS.0860 Propose, never decide.** Claude criticises, challenges,
  inspires and lays out options; the principal composes (POS.0010,
  POS.0070). Nothing enters content because Claude proposed it.
  The sign `??`, alone at the end of the principal's message or as
  his whole message, asks for Claude's honest opinion of what he has
  just written: three points at most, marked as Claude's own,
  nothing written or filed. It is not the isolated challenger, who
  does not know the conversation, and it adds to Claude's duty to
  say at once what does not fit (POS.0020), never replaces it.
  Decided 2026-09-27 at the principal's direction; one sentence
  under this method and no method of its own, for the size of
  CLAUDE.md (THR.0240).
- **POS.0870 Elicitation interview.** Claude draws out by questions
  what the principal has not yet articulated, rather than filling
  gaps by assumption (POS.0020); the heart of `/forge intent`. The
  interview is the form a conversation takes; elicitation itself is
  the process of finding an artefact, which uses research and
  sources beside the interview (POS.1300).
- **POS.0880 Draft early.** An early draft is an elicitation tool,
  not an output: concrete text sharpens the principal's reaction
  (POS.0150).
- **POS.0890 Reflect back.** Before anything is written, Claude
  restates what it understood the principal to have said, so that the
  write is a confirmation and not a surprise; the companion of
  write-once-per-round (POS.0190).
- **POS.0900 Intent-first.** A change of substance goes into the
  intent and propagates from there; only wording is fixed downstream
  directly (POS.0140).
- **POS.0910 Recommend, do not push.** Every option Claude lays out
  comes with its recommendation and reason, stated once; a declined
  recommendation is not re-argued unless new facts appear.
- **POS.1160 In pieces.** The principal may send one longer thought
  as several messages, a piece at a time, and close it with a word
  such as "done". Until that word Claude answers each piece with at
  most one line of acknowledgement — no question, no analysis, no
  warning — because the pieces are incomplete and a question would
  ask what he is about to write. After it the pieces are one input,
  read and worked as a whole; and one input is one write (POS.0190),
  so a brief dictated this way moves one version per block, not per
  sentence. Not a mode and no magic: one input split for the sender's
  comfort. Decided 2026-09-14 from the run record of `health`
  (`sources/forge-run-record-health.md`, P.02, P.14, F.02, G.08), in
  the principal's own words.
- **POS.1170 A rule that must hold in a long conversation is
  repeated at every prompt by a hook, not trusted to CLAUDE.md
  alone.** The run record of `health` showed the one-item walkthrough
  breaking about thirteen times with the rule fully in context and a
  memory note beside it (F.02): text loaded once dissolves as the
  conversation grows. The harness's `UserPromptSubmit` hook adds
  context at every prompt; the engine's `.claude/settings.json`
  carries one such hook. It prints two lines on the walkthrough —
  the one-item rule itself, since 2026-09-27 with the verdict line
  that closes a proposition (POS.0850), and a pointer to
  `.claude/skills/walkthrough/SKILL.md` for the full shape when a
  walkthrough or an interview runs — and, since 2026-09-20, three
  lines of conduct: where the forge has a script the script is used,
  git included; a command of Claude's own, beyond plain reading, is
  explained and approved first; nothing is written, run or changed
  that was not agreed and approved (the principal's rules; THR.0400
  holds the gate that would enforce them). That is also the
  first instance of the pattern THR.0240 asks for: always-on is one
  sentence and a pointer, the detail is a file read when its
  situation arises; the CLAUDE.md paragraph on the walkthrough shrank
  to that sentence. A hook is context, not enforcement — the nearest
  thing to a wall the harness offers. A trial, judged by behaviour:
  decided 2026-09-14 (P.04; the pointer the principal's idea, the
  repeated sentence Claude's addition). The hook's command is anchored
  at the project root: `.claude/settings.json` invokes it in exec form,
  `pwsh` with `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.ps1`
  among its `args`. A relative path is resolved against the session's
  working directory, not the engine root, and stopped resolving on
  2026-09-26 when Claude moved that directory with a `cd` of its own,
  so the hook fell silent mid-conversation; the placeholder always
  names the root the session started in, and the exec form hands the
  path to the program without a shell. Corrected and verified the same
  day by the hook firing again.
- **POS.1210 One write per round.** A working conversation is one
  round, and what is agreed in it is carried and written once at its
  end, on the principal's word (POS.0190, which owns the rule, its
  reason and its clarification). The method exists for its name: the
  principal invokes it in a word, and it stands beside the walkthrough,
  whose verdicts reach the write this way (POS.0850). The word that
  orders the write is `write`, typed in full: Claude reflects the
  whole round back and writes on the principal's yes, and offers the
  word beside the verdict line when the round looks finished, so
  that the principal always sees both ways on (his of 2026-09-27).
  Named 2026-09-26
  at his direction, so that the lesson of that day lives in the forge
  and not only in the assistant's memory; the rule itself is unchanged
  since 4.9.

### Elicitation
- **POS.1300 What elicitation is.** Elicitation is the process by
  which the principal and Claude find an artefact together and form
  the knowledge it holds. It is not any conversation of theirs, and
  in its meaning it is not a conversation at all: the conversation
  is the medium, the interview (POS.0870) is one instrument,
  research and sources are others. Three things are kept apart: the
  map (what must be found for the artefact to be complete), the
  process (how the map is walked) and the template (where the result
  lands); the map stands before the template. Elicitation differs by
  artefact: the talk over a brief, over an intent and over a BRD are
  three different talks, and every artefact type has a definition of
  its own (POS.1310). Not elicitation: composing a recipe, which is
  configuration from known options and not the finding of knowledge;
  `/setup`; the walkthrough of a reviewer's findings, which has its
  shape already and nothing per artefact in it. That elicitation is
  a process with several instruments is the consensus of the
  disciplines and no novelty of the forge (research
  `2026-09-28-human-ai-elicitation-over-artefacts.md`). Decided
  2026-09-28 from `00-brief-elicitation.md`.
- **POS.1310 The shape of a definition.** The elicitation of one
  artefact type is defined in seven blocks, in reading order:
  **Target** (the artefact's file and its template), **Inputs**
  (what the finding starts from), **Aim** (what the elicitation
  achieves and when the artefact is complete: the one place where
  completion is stated), **Partner** (Claude's stance: what he does,
  what he does not do, who steers the finding and who the
  decisions), **Map** (what must be found, POS.1320),
  **Instruments** (only the mechanisms of the forge this artefact
  uses in a way of its own, cited and never described) and
  **Course** (the ways in, the order, and what is offered when the
  Aim's completion is reached; it states no completion of its own).
  Every definition carries all seven, so that the shape can be
  checked; a block empty on purpose says so with the reason and is
  never silently left out. Aim and Partner do not repeat each other:
  Aim says what is true of the artefact at the end, Partner what
  Claude does beyond that, citing the Aim. Outside the definition,
  as shared mechanism cited and never repeated (POS.1070): the form
  of the conversation (POS.0850), one write per round (POS.0190),
  versioning with history and ledger (POS.0310), creation from the
  template, the language question (POS.0060), ending by naming the
  state. The definition lives in the state file of `/forge`
  (POS.0580) and stands beside the artefact's template as a pair:
  how we get there, and what is to come out. The genre files of
  `/recipe` (POS.0770) map onto the shape without loss, Genre and
  Skeleton to Target, Role to Partner, the elicitation checklist to
  Map; the seven blocks themselves are for the artefacts of the
  chain. The rules of particular artefacts that CLAUDE.md carries
  (Document chain 1 to 3, Requirement style, prime directive 8) are
  what moves into the definitions, in the order POS.1380 sets. The
  definitions of the three artefacts of today's chain are POS.1330,
  POS.1340 and POS.1350, in full; the state files are derived from
  them, as every part of the operating layer is derived from the
  intent. Decided 2026-09-28 from `00-brief-elicitation.md`.
- **POS.1320 A Map is a map of what must be found, not a
  questionnaire.** It names, in the artefact's own vocabulary, what
  the finding looks at; it prescribes neither the headings of the
  document nor the order of the conversation, and it is neither a
  list of questions nor a list of criteria. It is walked at the
  moments its definition names, as the question whether each area
  has been consciously considered; an area may stay empty when it
  was considered and found not to apply. How an area is found is the
  situation's: a question, a research step, a source. The precedent
  inside the forge is the elicitation checklist of a genre file;
  outside it, a coverage map held by the one who elicits and never
  read out as questions (research
  `2026-09-28-human-ai-elicitation-over-artefacts.md`). Decided
  2026-09-28 from `00-brief-elicitation.md`.
- **POS.1330 The definition of the brief's elicitation.** The seven
  blocks of POS.1310, in the wording agreed in
  `00-brief-elicitation.md`, word for word.

  **Target.** `00-brief.md` (bare) or `00-brief-<name>.md` (with a
  name — a later whole of thinking born during the project's life).
  Shape of the result: `templates/brief.md` — a YAML header, then
  free form: any headings, tables or lists the principal finds
  useful, no IDs, no conventions of the chain. What a brief is, its
  language and its lifecycle from draft to the lock: CLAUDE.md,
  Document chain 1.

  **Inputs.** The principal's thought, however it arrives. Around
  it, gathered during the elicitation: research notes (`research/`),
  sources (`sources/`) and Claude's own proposals. The existing
  intent and ledger are read only to know what already stands, never
  to shape the text.

  **Aim.** The brief puts the idea together: what the principal
  wants and why, with what he chose to take from the finding around
  it, in whatever structure serves the thought. The finding is wide
  (research, sources, his ideas and Claude's) and the brief is not
  its record: what goes in and what stays out is the principal's
  decision, made on what was found. What stays out lives in
  `research/` and `sources/` where it is a finding or a source, and
  otherwise nowhere. The brief is rough on purpose, neither perfect
  nor detailed: the chiselling is the intent's, and a brief polished
  until the intent has nothing left to do has gone too far. Nothing
  in it is yet a position. The brief is complete when the principal
  says so and locks it; the Map is walked before the lock is
  offered.

  **Partner.** The brief is the principal's text, and Claude's part
  changes on the way. At the opening Claude is the active one: he
  inspires, brings how the same thing is done elsewhere and how
  original the idea is, verifies what can be verified, and proposes
  research and ingest (Instruments); a proposal of his, however
  large, serves the finding and is not the brief. Then the brief is
  written, and it is mainly the principal's text. Claude moves him
  to describe what he wants, why and what he does not want, and
  writes it down whole by whole as they have talked it over. Claude
  may work on the text: translate it, mend its grammar, and put an
  idea of his own into it in his own wording where the principal has
  accepted it; what he has formulated he reflects back before it is
  written. What he does not do is take the text over: he does not
  decide what goes in, and he does not chisel it into an intent.

  Claude holds the form. A brief says what the idea is and why; it
  may carry a mechanism where the mechanism is part of the idea.
  Once the talk turns to taking it apart and agreeing it piece by
  piece (definitions, blocks, wording), Claude says in one sentence
  that this is the intent's work and does not develop it. The
  principal decides whether it stays in the brief as one open line
  or is let go. No walkthrough runs over the text of a brief and no
  IDs enter it.

  What Claude thinks of it he says when asked (`??`, CLAUDE.md,
  Working methods). What does not fit he says at once and unasked,
  in one sentence: a wrong assumption, a contradiction, a risk
  (CLAUDE.md, prime directive 1). What goes into the brief and what
  stays out is the principal's to say.

  **Map.** The Map is of the finding, not of the brief: it names
  what the finding looks at, and what of it enters the brief is the
  principal's choice. The brief has no required content, and the Map
  prescribes neither headings nor the order of the conversation. It
  is walked once, at the closing, before the lock is offered: has
  each area been consciously considered? An area may leave nothing
  in the brief. The walk asks and does not mend: a tension, an
  alternative left undecided or a boundary left vague may stay in
  the brief as it is, since resolving them is the intent's work.
  - the thought in the principal's words: what he wants, why, and
    what prompted it;
  - the world around it: what exists that does the same or the
    opposite, and what of it is inspiration, counter-example or
    proof that the wheel exists;
  - the material: the sources and research the thought rests on,
    gathered and registered, so that the intent can cite them;
  - what is still open: what was not decided or verified during the
    finding.

  **Instruments.** `/research <topic>`: durable findings into
  `research/`, indexed. `/ingest [file]`: outside material into
  `sources/`, registered and indexed. Both are steps of the
  elicitation, proposed by Claude and run on the principal's word.
  Claude proposes a research step against a named need: an
  uncertainty, a comparison, an inspiration. After it he says what
  it changed in the thought, what stays uncertain and whether more
  research is likely to change anything; whether to go on is the
  principal's to say. What the research did not find, or found not
  to hold, is a finding like any other and stands in the research
  note; it enters the brief where the principal takes it.

  **Course.** Resolve the project and the file; create the brief
  with its companion and ledger row if it does not exist; stop if it
  is approved — a new whole is a new brief. However the text
  arrives: pasted whole — store it verbatim and ask whether it is
  finished, if so lock at once; begun outside — store what came,
  then work from where it stops; born here — the principal opens
  with a rough idea and Claude works from the first word as the
  Partner says, verifies, confronts, proposes, draws out, and
  accumulates the principal's answers as his text, not as a summary
  of them; a summary or a structured proposal he asks to record is
  stored as shown, never re-narrated. Write once per round on his
  confirmation; lock only on his explicit word; end by naming the
  state and, if locked, proposing `/forge intent`.

  Before the lock the principal may have Claude give the brief a
  structure: the text gathered under headings in a logical order,
  what repeats pointed out, the grammar mended. Claude adds nothing,
  drops nothing and rewords no thought; he shows the structure
  before it is written, and the headings are the principal's to
  rename. The step is the principal's to ask for, never a condition
  of the lock.

  Decided 2026-09-28 from `00-brief-elicitation.md`. With the
  translation, the mending of grammar and the structure before the
  lock, the definition replaces the earlier rule never to translate,
  restructure or tidy the text of a brief. Two sentences of the
  brief's text are not carried here, since they speak of the mining
  and not of the definition: the one that leaves that rule to the
  mining, settled by this position, and the one naming three matters
  left open for the intent, which are THR.0440 (a) to (c).
- **POS.1340 The definition of the intent's elicitation.** The seven
  blocks of POS.1310. Aim, Partner, Map, Instruments and Course are
  in the wording agreed in `00-brief-elicitation.md`, word for word;
  Target and Inputs are those of the state file as it stood on
  2026-09-28, to which the brief refers.

  **Target.** `10-intent.md`. Shape of the result:
  `templates/intent.md`.

  **Inputs.** The locked briefs (`00-brief.md` and any
  `00-brief-<name>.md` with status approved; a draft brief is not
  yet an input), `decisions.md`, the ledger; sources only as the
  principal directs.

  **Aim.** The intent chisels the briefs into what the principal
  holds: from the briefs, the sources and the conversation it keeps
  what matters as positions, what is the case as facts, what is
  undecided as threads and what was dropped as rejections with the
  reason. Every idea is weighed twice — good or bad, feasible or
  not — and placed on a horizon where the principal sees one: a
  proof of concept, the first version, a later one, or good but far
  away. Everything coherent, nothing twice, every position with its
  provenance, and the whole passed through a final reality check
  before a lower layer is derived. It is complete for now when no
  thread blocks the next layer; it is never finished.

  **Partner.** Claude helps the principal reach the Aim: mines the
  briefs with him whole by whole, probes contradictions, gaps and
  unstated assumptions, reflects a brain-dump back as structure
  before it is written, offers options with trade-offs, proposes
  research where a thread needs outside grounding, and runs the
  final reality check with him. He composes the wording, the
  principal the substance; a thread closes only on his word.

  **Map.** What the intent finds, whatever the order; where it lands
  is the template's. Walked at the round's end, before a lower layer
  is proposed or the intent is approved; an area may stay empty when
  it was considered and found not to apply.
  - the essence: what the principal wants and why, as of today;
  - the weight of every idea: what he holds and why, what he dropped
    and why, what he deferred, which is not dropped;
  - the ground: what is the case, and on whose word or which source;
  - the horizon: where he sees one, what is a proof of concept, the
    first version, later, or good but far away;
  - what is open: what is undecided, what it would take to decide
    it, and which of it blocks the layer below;
  - the briefs as wholes: whether the substance of each is in the
    intent, was dropped, or was knowingly left behind;
  - what the layer below will need: the recipients, the objective
    and the success criteria, as soon as he sees them;
  - reality: what of it is feasible, and where the wheel already
    exists.

  **Instruments.** `/research <topic>`: proposed where a thread
  needs outside grounding, run on the principal's word. A source
  enters only as the principal directs (CLAUDE.md, Document chain
  5). `/challenge <persona> intent`: the independent reality check,
  offered once the joint one is done, never run on Claude's own
  judgement. The walkthrough of every position, where the intent was
  consolidated by Claude (CLAUDE.md, Document chain 2).

  **Course.** Resolve the project and read the inputs and the intent
  as it stands. The ways in: no intent yet, and the locked briefs
  are consolidated into the first one, which waits for its
  walkthrough (CLAUDE.md, Document chain 2); a brief pending or
  partial, and it is mined whole by whole, one brief at a time; an
  open thread, a new word of the principal's or what the recipients
  sent back, and the round starts there. Briefs are offered before
  threads. Within a round one theme at a time; the reality check
  comes last, before a lower layer is proposed. On the write,
  resolved threads move into positions or rejections and the Mined
  column of every brief touched is kept (write once per round,
  versioning and ledger: CLAUDE.md). End by naming what changed and
  what stays open; when the Aim's completion is reached, propose the
  next state, or the approval where the chain ends at the intent: a
  recommendation, never a gate.

  Where the recipients, the objective and the success criteria live:
  today only in the assignment (Objective, Purpose & Context,
  Success Criteria with SCR — optional, delegated or absent). The
  intent has no place for them but one that is easily forgotten: the
  section "Candidate structure for assignment", an optional staging
  area before distillation. They are substance, so intent-first says
  they are found above: that section is where the intent carries the
  recipients, the objective and the success criteria as soon as the
  principal sees them — positions with IDs like everything in the
  intent, no new section, no new prefix; the intent's Map names it
  and its Aim includes it. The assignment then distils them too,
  instead of finding them first.

  Decided 2026-09-28 from `00-brief-elicitation.md`. What the
  brief's second review holds against "weighed twice" is THR.0440
  (e); no fate is recorded part by part at mining (REJ.0210).
- **POS.1350 The definition of the assignment's elicitation.** The
  seven blocks of POS.1310. Aim, Partner, Map, Instruments and
  Course, with the joint pass, are in the wording agreed in
  `00-brief-elicitation.md`, word for word; Target and Inputs are
  those of the state file as it stood on 2026-09-28, to which the
  brief refers.

  **Target.** `20-assignment.md`. Shape of the result:
  `templates/assignment.md`.

  **Inputs.** `10-intent.md`, `decisions.md`, the ledger.

  **Aim.** The assignment carries the in-scope substance of the
  intent to the recipients, complete and precise, so that they can
  act on it without the principal in the room: who they are, what
  must be true at the end, what is theirs to decide and bring back,
  what they shall not do, and what the principal has left open on
  purpose. It is complete when nothing the recipients would need is
  left to assumption — delegated or open on purpose is complete,
  silent is not.

  **Partner.** Claude first reads the intent against what the
  assignment needs — recipients, objective, delegation, success
  criteria, horizon — and asks up front only what the intent lacks:
  who the recipients are, what is delegated and what specified,
  whether success criteria are present, delegated or deliberately
  absent, what is later. Then he drafts the whole from the intent
  with a provenance map (group → items → positions; positions that
  landed nowhere, items that came from nowhere), guards completeness
  and drift by it, and raises what the intent is silent on as a TBC
  rather than filling it. The two then walk the draft through group
  by group, the map in view, a question on one item opening it and
  closing it in place; a substance change is proposed to the intent
  first. The wording is Claude's, in the Requirement style; the
  substance the principal's.

  **Map.** What the assignment finds, most of it in the intent and
  the rest by asking; where it lands is the template's. Walked
  twice: before the recast, to see what the intent leaves
  unanswered, and at the end of the joint pass; an area may stay
  empty when it was considered and found not to apply.
  - the recipients: who they are, what they already know and what
    they will do with the assignment;
  - the objective: what must be true at the end;
  - the cut: what of the intent is theirs now, what is expressly
    later and what is out of scope;
  - the line between assigning and solving: what is specified, what
    is theirs to decide and bring back, what is left open on purpose
    and whose it is;
  - the boundaries: what they shall not do, what is not to be
    challenged, and what the whole rests on;
  - success: criteria present, delegated or deliberately absent;
  - the words: what must be defined so that the assignment is read
    without the principal in the room.

  **Instruments.** The provenance map (phase 2 below): a tool of the
  pass, no part of the assignment. The walkthrough by group (phase 3
  below): one item of the walkthrough is one group of the
  assignment. `/critique essence`: the independent test of drift,
  offered after the joint pass, never run on Claude's own judgement.

  **Course.** Resolve the project and read the intent and the
  assignment as it stands; say whether the intent is ready to be
  derived from (CLAUDE.md, Document chain 2), never as a gate. The
  ways in: no assignment yet, and the joint pass runs whole, in its
  three phases below; an assignment that stands and an intent that
  moved, and the pass runs on what changed, the provenance map
  showing what the change touched; a wording fix, made in the
  assignment directly. A substance change asked for in the
  assignment goes to the intent first (CLAUDE.md, Working methods).
  End by naming what changed; when the Aim's completion is reached,
  offer `/critique essence`, then the approval: a recommendation,
  never a gate.

  The joint pass, in three phases and no new kind of interview:

  1. Questions up front — one per message, only what is the
     principal's and the intent does not answer. None where the
     intent answers everything; rarely more than six, and where more
     are needed the intent is not ready and the work returns to it.
  2. The recast — Claude writes the whole draft from the intent, and
     with it the provenance map: group → items → the positions they
     came from, plus the in-scope positions that landed nowhere (to
     be none) and the items with no position (drift, to be none).
     The map is a tool of the pass, not part of the assignment.
  3. The walkthrough by group — one item of the walkthrough is one
     group (`### <Group>`): what it covers, from which positions,
     what in it is DEL or TBC, what is optional or later. A verdict
     per group; a question on a single item opens a sub-item and
     closes it before moving on. Dozens of items pass in a handful
     of messages and nothing is skipped, the provenance visible at
     each. After the pass, `/critique essence` offered as the
     independent test of drift; its findings, an ordinary
     walkthrough.

  Why not item by item: most items are craft derived from the intent
  and a verdict on each is ceremony. Why not "read the whole":
  without the map one sees what is there, not what is missing.

  Decided 2026-09-28 from `00-brief-elicitation.md`. What the
  brief's second review holds against "the words" as an area of a
  Map and against the number six is THR.0440 (f) and (g).
- **POS.1360 The horizon lives in all three layers, each carrying
  its own kind, nothing twice.** The intent carries the judgement:
  why this is a proof of concept, this the first version, this
  later, and what was deferred, which is not what was rejected; it
  is found and carried in free form, a word in a position being
  enough. The assignment carries the boundary: what is assigned now
  and what is expressly later, so that the recipients neither build
  it nor design it away; no reasons, those stay in the intent; an
  optional note, only where the recipients would otherwise build
  something that is later. The BRD carries the phasing: what each
  version delivers, in what order, with what dependencies; there the
  horizon is mandatory, even if only as the statement that
  everything is in the first version. "Later" in an assignment is
  not out of scope: out of scope is never done, later is done, only
  not now. The shape for the intent and the assignment is not solved
  here, and the whole is the principal's stance for now, confirmed
  when the BRD gets its definition in the brief `brd` (THR.0360). No
  outside model of a horizon divided among layers was found, so the
  division is the forge's own and is tried, not assumed (research
  `2026-09-28-artefact-layers-from-idea-to-handover.md`). Decided
  2026-09-28 from `00-brief-elicitation.md`.
- **POS.1370 How sure a claim is, is said in words.** Whatever
  Claude brings as knowledge says in plain words whether it is
  verified and on what, unverified, or a hypothesis; a claim never
  gains certainty by being written into an artefact. Words, not
  marks: no mark of certainty is introduced, as no mark of
  authorship or of acceptance is kept (POS.0110). The rule is
  Claude's conduct and therefore holds in every layer of the chain
  and in the conversation, not in the brief alone; it is the
  companion of POS.0020, which keeps Claude's constructions from
  passing for facts. Decided 2026-09-28 from
  `00-brief-elicitation.md`.
- **POS.1380 The order of the work, and what proves it.** The
  elicitation comes first; then the brief `brd`, the first instance
  of the shape of POS.1310; then the brief `engine-split`
  (THR.0230). The elicitation can be solved in today's engine
  without deciding the split, and self-contained definitions are the
  prerequisite of a later split, never the other way round: once the
  definitions stand on their own, the split is a decision about
  roots and installation, a move of files. The proof is conduct, not
  the number of lines CLAUDE.md loses: the three definitions are
  written whole first, swept for restatement by the
  `single-source-of-truth` check (POS.1140), and tried on real work,
  one run from a brief through the intent to an assignment, before
  any rule leaves CLAUDE.md; a rule leaves only once its definition
  has been seen to hold. The situations to try: a finished brief
  locked without an interview, a raw idea, a brief that needs no
  research, a brief locked with a tension left unresolved, an
  assignment drafted with no question asked, a drift the provenance
  map catches (`sources/forge-elicitation-brief-review.md`). Locked
  artefacts are untouched by the change. Decided 2026-09-28 from
  `00-brief-elicitation.md`.

### Document chain
- **POS.0100** Files in the chain are numbered in tens (`00-brief.md`,
  `10-intent.md`, `20-assignment.md`) so later layers — a BRD
  (`30-brd.md`), a solution design — can be added without renaming
  anything that exists.
- **POS.0110** A brief is the principal's own text of one whole of
  thinking, composed and then locked: what he wants and why, with
  what he chose to take from the finding around it. It is
  free-form: any structure the principal finds useful (prose,
  headings, tables, use cases), no required content and no IDs; only
  a minimal YAML header (project, title, date, author, version,
  status, last_change). It holds thoughts to be processed, not
  decisions: they may be changed, reworked or dropped when mined,
  and only the intent turns them into positions. No structure is
  *required*, because a required one would force premature
  tidiness, and none is forbidden; a summary the principal orders
  into a brief is stored as shown, never re-narrated. A brief is
  rough on purpose, neither perfect nor detailed: the chiselling is
  the intent's, and a brief polished until the intent has nothing
  left to do has gone too far. It is not the record of the finding.
  The finding is wide (research, sources, the principal's ideas and
  Claude's) and gathers as many ideas as it can; what goes into the
  brief and what stays out is the principal's decision, made on what
  was found. What stays out lives in `research/` and `sources/`
  where it is a finding or a source, and otherwise nowhere
  (REJ.0180). Nothing in a brief marks authorship: what is in it the
  principal approved, whoever first said it (REJ.0220). Two marks
  stay, because they carry something other than authorship:
  `(source: <path>)` says where a claim is from and becomes a fact
  with provenance at mining; a short `(remark: …)` stands where a
  reservation, an uncertainty or a suggestion was raised that the
  principal did not adopt, named by what it is and not by who made
  it, so that it reads the same whatever model the forge runs on.
  A brief has two states: *draft* while it is being composed, and
  *approved* (version 1.0) once the principal locks it; immutability
  runs from the lock, not from the file's creation. Three origins
  are equally legitimate and the forge does not distinguish them:
  the brief arrives finished from outside and is locked on arrival;
  it is begun outside and finished with Claude in the forge; or it
  is born in the forge from the first word. `/forge brief [name]` is
  the door for the latter two, and how a brief is found there is
  POS.1330. `/new-project` creates `00-brief.md` at scaffold time
  with the pre-filled header. A locked brief is the provenance
  anchor of its whole: the record against which later drift is
  measured. Present shape 2026-09-28, from
  `00-brief-elicitation.md`; the shape of 2026-09-14, in which a
  brief born by elicitation held the whole pile with Claude's part
  marked, is history 4.9. What stands of that day is its cause:
  Claude never reports as written what lives only in the
  conversation (POS.0190).
- **POS.0920** A project may have more than one brief, and the ledger
  tracks how far each is mined. The founding brief is `00-brief.md`;
  every later whole of thinking that would otherwise land in the
  intent as a batch of unproven positions is born as
  `00-brief-<name>.md` — same header, same states, same rules. A
  locked brief is mined into the single intent: positions cite the
  brief as provenance; a whole that dies on the way leaves the brief
  locked and one REJ in the intent with the reason, so the trace
  survives either way. The ledger's Briefs table carries one row per
  brief — version, status and a mining state `pending | partial |
  mined | dropped` with a free-text note (what remains for *partial*,
  the REJ for *dropped*); "how much" is a judgement recorded in that
  note and in the provenance of the positions, never a metric.
  `/forge` shows pending and partial briefs as next steps, `/forge
  intent` offers them for mining, `/check` compares the table with the
  directory. Rationale: a big new whole needs a place where the
  thought can be tempered before it enters the trunk — like a git
  branch — without a new document kind; THR was wrong for it (a
  thread is a question, not a body of work), and a working space with
  positions before the merge (a branch document) was judged heavy for
  now (THR.0170). Closes THR.0110 (opened 0.8, 2026-08-02).
- **POS.0120** `10-intent.md` is the working document: the consolidated
  *current* state of the principal's intent. Not an append-only log; it
  is rewritten for coherence each round, with changes recorded in its
  Version History. It exists because chat context dies and anything of
  value must live in a file: it is the document to read when returning to
  a project after weeks, instead of excavating old conversations.
  A position is a stance with its reason and its citations, dated
  once. How it was reached — trials, measurements, counts, findings
  settled, what others do — is the history row's, the ledger's or a
  research note's, never the position's. Dated once means one date, the
  day the position took its present shape; earlier steps are named by
  their history row, not by date. A number stays only where it is the
  rule or a threshold, never as a measurement — a measurement enters a
  reason in words (CHL.0180, 2026-09-06).
- **POS.0130** `20-assignment.md` is the distilled handover document for
  the recipients: complete, precise, structured, self-contained,
  versioned. It carries the whole in-scope substance of the intent —
  nothing is left out for the sake of brevity, and a silent omission is
  a defect; leaving a matter out is legitimate only as an explicit
  delegation (a DEL or TBC item). There is no size target in either
  direction: length is whatever fidelity requires, and the defect is
  excess of the wrong kind (solving instead of assigning), never length
  as such (the size targets dropped 2026-08-08 and 2026-08-15, history
  1.12 and 1.15: the goal is to have it right, not short). The name "assignment"
  was kept deliberately after considering alternatives; it does not
  preclude further layers below it.
- **POS.0140** Substance changes go intent-first and then propagate to
  the assignment; wording-only fixes may edit the assignment directly. If
  the principal dictates substance straight into the assignment, the
  corresponding intent update is proposed in the same step.
- **POS.0150** Drafting early is a legitimate elicitation tool, not a
  violation of sequence. Concrete text sharpens critique.
- **POS.0160** Supporting documents (the kinds: POS.1080): `decisions.md` (append-only, DEC),
  `ledger.md` (single source of truth for state, freely rewritten),
  `reviews/`, `challenges/`, `research/` (all immutable, dated); the
  resource indexes are POS.0840's. The ledger cites and never copies:
  under Waiting on principal a matter that has an ID gets one line —
  the ID, a few words, its state — and its substance stays in the
  thread or the record; free text only for a matter with no ID yet,
  which gets one at the next write; an unfinished conversation is
  saved into its thread of the intent, a write of whatever is agreed
  so far, never into the ledger. The `project` check reports a line
  that carries a thread's, a decision's or a history row's text
  instead of citing it. The ledger header may declare `terminal:`,
  the artefact the project's chain ends at, assignment when absent;
  `/forge` and the checks then say nothing of a missing assignment.
  Added 2026-09-14 (P.15, P.09, G.10): the `health` ledger's Waiting
  section carried a rule, a proposal and ten talking points, and this
  project's own carried the story of every round — two hundred and
  fifty lines of prose duplicating threads, decisions and history,
  which no check read, since the single-source rule was written for
  mechanisms and the check for the operating layer. The sweep of this
  ledger is a step of its own on the principal's word.
- **POS.0170** Feedback from recipients has no channel of its own. The
  principal processes it and feeds conclusions back through
  `/forge intent`.
- **POS.0180** External inputs (transcripts, offers, documents,
  standards) live in `sources/` per project: immutable once registered,
  plain slug filenames, each in one form — text, or a functional
  binary (POS.1040).
  They may arrive at any stage of a project's life — before the brief
  as material for writing it, during intent work, or after. Origin
  dates are metadata, not ceremony: recorded best-effort in the ledger
  (content | file | ingested) and never demanded from the principal.
  The principal may drop files into `sources/` manually at any time;
  `/ingest` without arguments sweeps the directory: it registers new
  files and reports files changed since registration (modification
  time against the ledger date) with a question — what to do with
  each. The meaning depends on the project's kind (POS.0960): in a
  `thought` project a changed source is a breach of immutability to
  be settled (a new version beside it, or knowingly accepted); in a
  `library` project it is the normal case — the extract is
  regenerated, the ledger date moved, the index entry corrected.
  `/ingest`
  stores, registers and catalogues — nothing more. Registration does
  not imply intake: what a source is for is individual — a standard to
  verify against, inspiration, a meeting record, material to absorb —
  and is recorded as free-text Role in the directory's `00-INDEX.md`
  (POS.0840), taken from the principal in a sentence when he offers
  one, never demanded; the ledger row is registration only. The
  principal alone directs how and when a source is used, in whatever
  work he chooses. When source content does enter the intent, it is
  his explicit act, cited with provenance to the file; what someone
  said in a meeting is never silently promoted to the principal's own
  position. A set of related files — a downloaded site with its index,
  a document with attachments — may live as a subdirectory
  `sources/<slug>/`: one source, one ledger entry, immutable as a
  whole from registration. File-level detail is not lost: provenance
  in the intent cites individual files by path, and the bundle's index
  or extract lists its contents. If a bundle's files ever need
  separate fates, a file may be split out to its own ledger row — the
  ledger is freely rewritten. Isolated files stay directly in
  `sources/` as before. Every bundle carries a `00-INDEX.md`
  catalogue in the shape POS.0840 owns; `/ingest` creates it at
  registration when the bundle lacks one and validates a supplied one
  against the contents, origin dates best effort, never asked for.
  Text extracts are produced by
  `scripts/doc2md.ps1` (engine: markitdown, installed separately),
  never by ad-hoc parsing — no Python PDF reading, no manual
  transcription. `/ingest` runs the script file by file on every
  binary the principal chooses to convert (POS.1040), in bundles as
  well as for isolated files; the output is `sources/<slug>.md`, the
  source itself.
- **POS.0840** Resources have an index. Every `sources/` and
  `research/` directory carries a `00-INDEX.md` (the resource index):
  a light catalogue so that Claude — and the principal — know what
  resources exist and what they are for without re-reading the files.
  It is a working aid, not a record of thinking: it tracks nothing (no
  processing state, no positions) and is an automatic input of no
  command. `/forge`, `/critique` and the challengers do not confront
  the chain with the material on their own; a contradiction between
  the intent and a source is not a finding, because the source may be
  a counter-example, a mere inspiration or a record of what someone
  else said. Claude reaches for a file by its own judgement or when
  the principal asks ("check the assessment against the requirements
  in file X"). Each entry has fixed fields in free text — for sources
  *What / Origin / Role / Use for*, for research *Question / Answer in
  short / Consult when*; Role is free text with recurring examples (a
  standard to verify against, inspiration, a counter-example, a
  meeting record), never a fixed vocabulary. The ledger holds
  registration only — a Sources table and a Research table, no content
  columns — so that nothing is described in two places. A bundle keeps
  its own `00-INDEX.md` inside and appears in the top index as one
  entry pointing into it: two levels, never deeper, and the top index
  never repeats the bundle's contents. The bundle index is the same
  catalogue one level down: a YAML header (bundle, project, date,
  origin), one paragraph saying what the whole is and why it entered
  sources, and one entry per file in the same fields;
  `templates/index-bundle.md` is the full skeleton `/ingest` creates
  the file from, its entry carried verbatim from `templates/index.md`.
  One shape for every index, because Role and Use for are what an
  index is for and a table does not carry them (decided 2026-09-04,
  history 3.23). The index is freely rewritten like the ledger while
  the files under it stay immutable. `/ingest` and `/research` write
  the entry when they place the file (the bare `/ingest` sweep fills
  gaps), `/new-project` scaffolds both indexes from
  `templates/index.md`, and the `light` check verifies index against
  directory — a file without an entry or an entry without a file.
- **POS.0190** Artefacts are written once per iteration round, not once
  per answer — and this holds for any working conversation over the
  intent or open items (a `/forge intent` interview, a thread sweep,
  resolving findings), whatever the entry door. Answers are carried in
  the conversation and reflected back; at the round's natural end
  Claude asks whether to write and writes on the principal's
  confirmation — one version bump and one Version History row however
  many answers the round contained. The principal may at any moment
  order a write of whatever is agreed so far. Writing after every
  exchange buries the substantive change under changelog churn and
  makes the Version History unreadable. Clarified 2026-09-26, after
  this intent went from 4.21 to 4.25 in one conversation because
  Claude took every order to write as closing the round and gave each
  of the principal's following corrections a version and an
  append-only history row of its own: a correction that lands on text
  written moments ago belongs to the round that wrote it and is
  carried like any other answer; an ordered write of what is agreed so
  far does not close the round unless he says so. The name the method
  carries is POS.1210's. "Written" means a file:
  whenever Claude reports something as written, it names the file and
  section; whatever is carried in the conversation only is said to be
  nowhere yet, and Claude never says nothing is lost while anything
  lives only in the conversation. Added 2026-09-14 from the run record
  of `health` (P.01, F.01 — the costliest failure of that run: ten
  hours of "nothing will be lost" while Claude's part of the pile was
  in no file).
- **POS.0710** A project may spawn renders: audience-specific outputs
  generated from the chain — a pitch for the group, an architecture
  picture, an executive summary, the repository README. A render is
  never edited by hand; the iterated thing is its **recipe**
  (`recipes/<recipe>.md`): inputs (one artefact or several), audience,
  instructions and the literal output template in one file, versioned
  by the house scheme and composed conversationally with the
  principal. `/render <recipe>` regenerates the output mechanically
  into `renders/<recipe>.md` — or the recipe's optional `output:`
  path — undated, overwritten freely, history in git; the files made
  from a render are POS.0590's. Every render
  opens with YAML front-matter provenance citing the recipe and every
  input with their versions; the ledger's Renders table mirrors it. A
  render assigns nothing and is not part of the chain: the artefacts
  remain the sole source of truth. The boundary between the two is
  authorship, not audience: a chain artefact is composed by the
  principal (Claude proposes, the principal composes), a render is
  generated from artefacts — an article the principal writes is a
  layer of the chain, its translation is a render. Visible YAML provenance was chosen
  over an invisible comment deliberately: provenance is control
  information, the audience rarely meets raw Markdown, and GitLab does
  not display front-matter. Dated hand-made editions of the earlier
  derivative convention remain in place as legacy history. Recipes are
  tools, not records of thinking: they carry a version and an updated
  date in front-matter — enough for a render to cite — and no status
  field, because a recipe is never approved and stays 0.x for life.
  Being versioned, a recipe keeps its Version History in the companion
  like every versioned kind (POS.0310); the companion records what
  changed in the recipe at its own grain, the substantive turns live
  in the intent. Recipes are deliberately loose: the template fixes the
  structure and what information appears where, never the wording — a
  presentation recipe says what belongs on a slide, not its phrasing
  or its placement on a picture. Each rendering re-derives the words
  from the current inputs; fixing the text in the template would turn
  the recipe into the render and make the inputs meaningless. A
  render may also serve as an input of another render — a deck slide
  citing an architecture picture as `render: <file>` — provided the
  citing recipe declares it among its Inputs, so provenance and
  staleness track the dependency.
- **POS.0720** README.md is a render of the forge project. Its recipe lives
  at `projects/forge/recipes/readme.md` with `output:` pointing at the
  repository root; the natural inputs are this intent and CLAUDE.md.
  README.md is never edited by hand: content fixes go into the recipe
  or the inputs, and the file is regenerated: a process change is
  complete only once the intent is updated and the README re-rendered.
- **POS.0730** Release notes are a log of releases, not a story.
  `RELEASE-NOTES.md` in the repository root is a render (`/render
  release-notes`, recipe `recipes/release-notes.md`) for one reader:
  the user of the engine who has cloned it and takes upgrades through
  `forge-pull`. One section per release of the engine — every
  `/release` (POS.1100), the version being the intent's, 3.12 as much
  as 3.0 — newest first, headed `<version> — <date>`; inside it fixed
  groups in a fixed order — *Action required* (what the user must do
  in their projects after pulling), *Added*, *Changed*, *Removed*,
  *Fixed*, *Rejected* (a direction dropped, with its REJ or DEC) —
  one sentence per change from the user's side with a pointer (a
  position, a decision, a command, a script), empty groups omitted, a
  release that changes nothing for the user carrying that one line.
  An approved major is headed "approved", opens with two to four
  sentences of highlights and names its tag among them where one
  exists; no other narrative, and no Unreleased section — nothing is
  unreleased at the moment of a render, which only `/release` runs.
  At a major the minors since the previous major are folded into it:
  the major's section carries every Notes line of the span in the six
  groups, a line superseded by a later minor dropped so that only the
  final state remains, and the sections of those minors disappear
  from the file — the house scheme's own reading of a major ("the
  next approved version, incorporating all changes since") and the
  field's folding of pre-releases into the final release; the detail
  per version stays in the history companion. Between majors every
  release keeps its section. The sections are compiled, not
  distilled: every line comes from the Notes block of the intent's
  Version History rows (POS.0310), pruned and ordered by the render,
  never classified by it. Released sections are carried over verbatim
  from the previous edition and never change retroactively; only
  factual corrections ordered by the principal touch one, through the
  recipe. A thought project's release notes work the same way from
  the Notes of all its chain artefacts but the brief — intent,
  assignment, later layers — for the recipients tracking it (genre
  skeleton `templates/recipe-release-notes.md`, `/recipe
  release-notes`). Reason: a reader wants to see plainly what was
  added, changed and removed — the shape the written standards and
  the established projects share (research
  `2026-09-05-good-release-notes.md`), and the one the forge's first
  render had inverted. Decided 2026-09-05 by walkthrough, closing
  THR.0310 (history 3.35–3.38, where the migration of the whole
  history is recorded).
- **POS.0810** Regenerated renders pass under the principal's eyes.
  Regeneration is stochastic: the same inputs never guarantee the
  same words, so an unreviewed regeneration is an unreviewed edit of
  an outward-facing document. Two light defences, neither of them a
  gate (POS.0430): a recipe pins load-bearing wording as fixed
  text — what is pinned regenerates verbatim (a title, a claim, a
  fixed line) while everything else re-derives freely — and a
  `/release` that regenerated renders reports in its summary
  what materially changed in them, so the principal rules on the
  delta before the release commit without reading a full diff. A render is
  regenerated only by `/release` (POS.1100) or by the principal's
  explicit `/render`; Claude never regenerates on its own judgement — it
  reports staleness and offers (decided 2026-08-30). The README and the
  release notes are regenerated by every `/release`; every other
  render is as stale as the principal lets it be. No check reports
  the staleness of any render, those two included (POS.0570): the
  `/forge` map shows it.
- **POS.0960** A project has a kind, `kind: thought | library`, declared
  in the YAML header of its ledger, default `thought` — today's projects
  unchanged. The rules of a kind live in the engine; the project carries
  only the data marker, and its optional `CLAUDE.md` stays polish, never
  kind rules (that would copy the engine into the project).
  `/new-project` scaffolds by kind, the `/forge` map reads a library as
  material rather than as a project waiting for a brief, `/check`
  requires no chain of a library and reports a project that is not a
  repository — with the one-line way to initialise it — as a fact, never
  as a defect (POS.0940). "Chain" was considered as a kind name and
  dropped: nothing could be pictured under it.
- **POS.0970** A library is a project of kind `library` — no chain: a
  ledger, `sources/` and `research/` with their indexes,
  `recipes/readme.md` and the README it renders (POS.1000) — a
  collection of documents used across projects, prefix `lib-`, its own
  repository and therefore its own visibility. Nothing is redefined:
  `/ingest` by file or link, or an upload and a sweep, registration and
  index as everywhere. Two kinds of material exist: a thought project's
  sources are inputs as of a date and immutable; a library's documents
  are maintained by an owner who is also their author — overwrite, or a
  new version beside, is the owner's choice (a deck template's previous
  version is irrelevant; a requirement-writing convention may usefully
  say "supports v1 and v2"). Another project cites a library document by
  path. The citation is a cross-repository dependency taken knowingly:
  only someone with both repositories can read it, the assignment is
  self-contained anyway, the version in the citation is a visible,
  unguarded pin, and a check is added when it hurts. The library is not
  a condition of publication: the intention is decided, the
  implementation comes with the first library.

### Structure and style of an assignment
- **POS.0200** Structured items with stable IDs beat prose, even at very
  high abstraction. Narrative is confined to Purpose & Context and
  Objective.
- **POS.0210** An assignment assigns; it does not solve. What keeps a
  document an assignment is the kind of content, never its amount.
  The formerly enumerated ban — stakeholder matrices, RACI, impact
  analyses, MECE decompositions, tables of contents — originated in
  one early case and is not a universal rule: any such apparatus may
  appear where the principal judges it part of setting direction; it
  is the recipients' machinery only when it belongs to executing
  delivery. (THR.0120 closed by this decision, 2026-08-17.)
- **POS.0220** IDs use the format `PREFIX.NNNN` with three-letter
  prefixes, numbered in tens, each new group starting at the next
  hundred. IDs are global and stable, never renumbered; items may move
  between groups freely. Groups are plain headings with no IDs, no
  metadata and no lifecycle; depth is capped at two levels.
- **POS.0230** Prefix vocabulary, aligned with the group BRD standard
  where an equivalent exists: REQ, OOS, CON, ASM, DEL, TBC, SCR in the
  assignment; POS, THR, REJ, FCT in the intent; FND, CHL, DEC
  internally. No universal standard for prefixes exists; this is a
  house convention derived from the group's own. A fact (FCT) is what
  is the case — stated by the principal on his word, or by a source
  cited to its file; verification is never demanded. A position (POS)
  is what the principal holds or wants. Making a source's fact his own
  stance is a new POS. Added 2026-09-10 for the first project whose
  intent had to carry what is so beside what is wanted: without a
  prefix of its own, a fact would have passed for a position. A
  thread (THR) carries its origin — the principal's word, a source by
  path, or Claude's synthesis — so that a hypothesis of Claude's
  stays visibly his until the principal takes it up; what Claude has
  worked out is never a FCT, since a fact is the principal's word or
  a source's. Origin is marked from 2026-09-14 on, the principal's
  word being the default that needs no mark; no retrofit (P.08, F.04:
  nothing in the `health` intent said whether a thread came from the
  principal, a source or Claude).
- **POS.1180** An intent consolidated by Claude from the conversation,
  rather than composed item by item with the principal, is
  `in_review` until every position has been walked through, and no
  lower layer is derived before that walkthrough. In `health` the
  intent 0.1 was written in six minutes from three days of talk — 31
  positions and threads Claude had distilled — the scheduled
  walkthrough never ran, and 26 positions were confirmed en bloc
  because the report built from them had been read: the authorship
  rule of the intent inverted, the principal auditing a document
  instead of recognising his own (F.03, DEC.0030 of that project).
  Ordinary work, where positions are composed in the conversation, is
  untouched. Decided 2026-09-14 (P.08).
- **POS.0240** Every assignment carries a Terms section listing the
  prefixes and any domain terms it actually uses, so it can be forwarded
  without oral tradition. Defined Terms are capitalised in item text.
- **POS.0250** Requirements are written as shall / shall not, in full
  correct UK English sentences, one idea per item, each written once.
  Would, could, should, might, may and MoSCoW wording are not used.
- **POS.0260** No priorities and no priority column. Everything in an
  assignment is essential; an exception carries a note reading
  *optional*.
- **POS.0270** Testability is recommended, never required. Assignments
  are deliberately high-level; delegating concretisation through a DEL
  item is a legitimate outcome, and the critic reports untestable wording
  as a recommendation, not a finding.
- **POS.0280** Success criteria are wanted but not compulsory. Delegating
  them to the recipients as a deliverable ("define success criteria and
  return") is a legitimate outcome, not a defect.
- **POS.0290** An item must not depend on an external link to be
  understood, agreed or later tested. Negative mandates (out of scope,
  do-not) rank equally with positive ones. FR / NFR markers may appear in
  item text where they help; they are never part of the ID.

### Versioning and state
- **POS.1080** A project's documents fall into five groups and
  thirteen kinds, and the kind determines what a document is, who
  writes it, whether it is versioned and how it behaves. "Document" is
  the word for every file of a project; "artefact" is reserved for the
  documents of the chain — the ones the principal composes, the
  reviewers read and the renders are generated from. The table is the
  one page from which all of this is read, in the intent, in CLAUDE.md
  and in the README alike:

  | Group | Kind | Meaning | Written by | Versioned | Behaviour |
  |---|---|---|---|---|---|
  | artefacts | brief | the idea put together: what the principal wants and why, with what he chose from the finding | principal; Claude may work on the text | yes | locked at 1.0, then immutable |
  | artefacts | intent | current understanding for principal and Claude: positions, facts, threads, rejections | Claude, principal composes | yes | rewritten freely |
  | artefacts | assignment | the direction handed to the recipients, self-contained | Claude, principal composes | yes | rewritten freely |
  | artefacts | later artefacts (BRD, RFP, article…) | further layers, each derived from the one above | Claude, principal composes | yes | rewritten freely |
  | records | history | what changed in a versioned document, and why | forge | — | append-only |
  | records | decisions | the principal's decisions with reasons | forge | — | append-only |
  | records | review, challenge | one dated reviewer run | reviewer agent | — | immutable |
  | state | ledger | single source of truth for state | forge | — | freely rewritten |
  | state | index | catalogue of a resource directory | forge | — | freely rewritten |
  | rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
  | rendering | render | audience-specific output, never a source of truth | generated | — | overwritten by /render |
  | resources | source | external input as it arrived | external, /ingest | — | immutable |
  | resources | research | durable answer to one question | Claude, /research | — | immutable |

  Every versioned kind keeps its Version History in an append-only
  companion `<file>.history.md` (POS.0310); an integer version is
  approved, and a recipe never is. A functional binary — a `.potx`
  template, a graphic — is a source (POS.1040), so a library's assets
  fall under resources without a kind of their own; a library carries
  no artefacts and no records but its recipe's history companion, the
  other groups unchanged. The
  assignment is not "frozen" in any sense the file would show: it is
  rewritten freely between approvals like the intent, and what the
  recipients hold is a version reached by a link into git — the word
  was dropped because it described the handover, not the document.
  Decided 2026-09-04 (history 3.23).
- **POS.0300** Versioning follows the group BRD convention: integers
  denote signed-off versions. Drafts run 0.1, 0.2 …; 1.0 is approved;
  1.1, 1.2 … are changes made after approval, not yet approved
  themselves; 2.0 is the next approved version. Status in front-matter
  (`draft | in_review | approved | superseded`) must agree with the
  number. A major of the forge intent closes a set of features the
  principal names — 4.0 closes the engine's operating layer: the git
  doors, the release notes, the contracts, the skills layout, the
  checks — and passes more than a minor before its tag: every check,
  `single-source-of-truth` included, both critic lenses and one
  challenge, their findings settled or deferred by his word. The word
  closes the major; the test says what the word attests (CHL.0190,
  2026-09-06).
- **POS.0310** Every versioned document keeps its Version History
  (Version | Modification | Author | Date — human-readable, what changed
  and why) in an append-only companion `<file>.history.md` beside it,
  never in its body: the body is the current state, the companion the
  record. One rule without exception — brief, intent, assignment, every
  later artefact and the recipe alike; a brief that arrives finished
  has one row, a brief born in the forge one per round. The document's
  front-matter carries version, date, status and a machine-written
  `last_change:` line summarising the newest row, written by the same
  write step that appends the row, never by hand, so the two cannot
  drift. The row of a chain artefact other than the brief — the
  intent, the assignment, every later layer — closes with a **Notes**
  block: after the prose, one line per change that reaches the reader
  of the release notes, each opening with its group (Action required,
  Added, Changed, Removed, Fixed, Rejected) and carrying a pointer, or
  the one line "nothing for the reader"; written with the row, by
  whoever made the change, so that the release notes (POS.0730) are
  compiled from fresh lines and never classified afterwards. A Notes
  line has two sides, in this order: what changed — the fact, with its
  pointer — and then, after "For you:", what it means for the reader:
  what they can now do, must do or can no longer do. Neither side
  alone is a line: a fact without its consequence describes the
  system, a consequence without its fact loses what changed, and no
  recipe can supply a missing side, since the render compiles and does
  not rewrite. The brief has no Notes (its history is a draft and a
  lock, mined into the intent's rows), nor has a recipe (a tool, not
  the project's content). The row in the companion is the single
  primary: the commit messages `/save` and `/release` draft and the
  release notes are derivations by mechanism, which POS.1070 permits —
  a record rendered twice is not a procedure stated twice. The
  companion is part of its document: not a row of the ledger, handed
  over with it by the link into git, read by a reviewer that needs the
  document's trajectory and by nobody who needs its current state —
  every command and isolated agent that loads the document is spared
  a history that had outgrown the substance. A Version History
  table in the body of a document is a `/check` finding, fixed by
  moving it into the companion — that is how a project migrates to
  this convention (POS.0820), on the principal's word, project by
  project, each saved by its own `/save`; a colleague's project meets
  the rule at its next `/check` after `forge-pull`. Present shape
  2026-09-05 (history 3.21, 3.35–3.37; research
  `2026-09-03-version-history-placement.md`, whose split by kind the
  principal rejected as two rules for one thing, and
  `2026-09-05-good-release-notes.md`); closes THR.0260 and THR.0310.
- **POS.0320** Immutable documents (a locked brief, reviews, challenges,
  sources, research) are never edited — a brief from its lock, a source
  from its registration, the others from creation; corrections happen
  downstream.
- **POS.0330** State lives in files, never only in conversation. A
  session can be ended at any point without loss; `/ledger` re-orients
  from the ledger. One project per session is the hygienic default.
- **POS.0820** Artefacts do not expire with the conventions.
  Conventions evolve continuously and `/check` measures against the
  current ones — but an artefact remains valid under the conventions
  it was written to: nonconformance of a finished or dormant project
  is a fact to report, never a defect to chase. Bringing a project
  to newer conventions is an explicit migration decision of the
  principal, made per project and never assumed.

### Review
- **POS.0400** Isolated kinds of review of one shape: the critic
  (document quality, findings FND) and the challenger (substance of the
  thinking, challenges CHL). Both run as isolated subagents on the
  session model that never see the working conversation — that blindness
  is the source of their value; both are invoked by hand by the
  principal, `/critique <lens>` and `/challenge <persona>`; both produce
  an immutable dated report and ledger rows; both are settled by
  walkthrough (POS.0850). The challenger has personas, the critic has
  lenses: one agent file each, the shared behaviour of the kind
  preloaded from one contract skill (POS.1120), only the Lens section
  its own (the engine check guards the preload, POS.1120). Both take
  an optional target, an artefact named
  as `/forge` names it (`brief`, `brief-<name>`, `intent`, `assignment`,
  later layers as they come); without one, the whole chain, so that
  one file or one transition can be reviewed alone (2026-09-03). Neither runs at a save; `/release` offers `critique essence` once,
  in a sentence, and runs no reviewer on its own — the one lens that
  guards what a release publishes, the drift of the chain (decided
  2026-09-05 at the THR.0220 round, POS.1100).
- **POS.0410** The critic has two lenses, because one critic hunted
  formalities and never guarded the chain (history 3.10). `clarity`
  reads each artefact on its own: ambiguity, internal contradiction,
  duplication, scope hygiene, Requirement style, the advisory
  checklist. `essence` reads the chain: for every adjacent pair
  (brief → intent, intent → assignment, every later layer) it first
  distils, blind, the essence of the downstream artefact in a few
  sentences, then the upstream's the same way, and compares —
  substance lost without a trace (REJ, DEC, DEL, TBC, the ledger's
  mining state), substance added without provenance, meaning shifted,
  provenance that does not hold; a finding is a difference of
  essences, not of texts, and the report carries both distillations.
  A target narrows `clarity` to that artefact and `essence` to that
  artefact against its parent — a transition is addressed by its
  downstream artefact, since every layer has exactly one parent, so
  no arrow is ever typed. Regression against resolved findings is
  every lens's first step over its own reports, the retired single
  critic's reports divided between them by category; FND IDs stay one
  global sequence; each run produces a delta report (new / verified
  resolved / still open / newly obsolete). Untestable wording and
  missing delivery-stage apparatus are findings of no lens. Decided
  2026-09-03.
- **POS.0420** `/challenge <persona> [artefact]` reviews the thinking
  through a chosen persona — one isolated agent per persona
  (`challenger-<persona>`), each defined by the blind spots it exists to
  find. The target may be any artefact of the chain, the whole chain
  when none is named — each challenge then names the artefact it
  concerns: the challenger reads the whole chain for context and
  challenges the substance of the target. The contract is
  invariant whatever the persona: no stake in the principal being right;
  unstated assumptions, whether the stated objective is the real
  problem, second-order effects, organisational reality, failure modes,
  missing dimensions, the serious counter-case; three to seven sharp
  challenges, each with a severity (dealbreaker | major | minor, ordered
  by it — a fatal flaw is never buried among cosmetics), a falsifiable
  "what would change my mind" and an epistemic status (consensus |
  active debate | emerging practice | my judgement); no fabrication — a
  precise "I don't know" beats an invented figure, and anything
  reconstructed from memory is flagged. The contract has one
  owner, the skill `challenger-contract` (POS.1120): every persona file
  names it in its front-matter and writes only its own Lens — who it is
  to the principal and which blind spots it exists to find
  (POS.1120 for the guard of the preload).
  The first persona is `cto` (CTO register);
  further personas — a strategist, a business analyst — are created from
  the lens-file skeleton by the principal's decision when first needed, and only
  where their blind spots genuinely differ: personas that would say the
  same things in different words are noise. Bare `/challenge` lists the
  roster and recommends a fit for the project's subject. Challenge files
  carry the persona in their name (`YYYY-MM-DD-challenge-<persona>.md`);
  the CHL sequence stays global per project.
- **POS.1120** The shared behaviour of a kind of reviewer is a contract
  skill, preloaded — never a copy. Each kind — the critic, the
  challenger, check (POS.0540), whatever comes after — owns one skill
  `.claude/skills/<kind>-contract/SKILL.md` (`critic-contract`,
  `challenger-contract`, `check-contract`; the suffix because `check/`
  is the command, POS.1130), named in the front-matter (`skills:`) of
  every lens, persona or check file of that kind, which then carries
  its front-matter and its Lens section and nothing else; Claude Code
  injects the whole skill at launch. One skill per kind, because the
  shared texts differ almost whole; the few sentences common to all
  stay in each contract in its own words — three contracts and no
  common skill, reopened only if a fourth kind repeats them. A
  contract is addressed to every lens of its kind, never a template
  with placeholders: it opens by citing CLAUDE.md, Isolated
  reviewers, the one owner since POS.1070, for what the contract
  owns (conduct, subject, way of working, report shape, ledger step),
  what the lens file owns (what it reads, what it goes after, its
  categories, its own report sections) and the overlap rule — a lens
  is a specialisation, never a replacement: it may make a rule
  stricter, never rename, drop or duplicate one; the protocol changes
  in the contract — because the contract lands after the lens's own
  text and the agent must know which yields. The contract never names a lens;
  the lens file does. The skill is `user-invocable: false` (out of the
  `/` menu; its description stays in the session's context —
  `disable-model-invocation` would also forbid the preload) with a
  description saying it is preloaded. `templates/critic.md`,
  `templates/challenger.md` and `templates/check.md` are the skeletons
  of a lens file; the engine check verifies that every skill an agent
  names exists, since a missing one is skipped silently. Facts of the
  mechanism: the skill arrives at the end of the first user message,
  after the task, not in the system prompt; a headless `--agent` run
  preloads nothing, so reviewers run as subagents only. Decided
  2026-09-06 after a trial (history 3.40), built and confirmed on
  every kind the same day (3.41–3.46). Closes THR.0270.
- **POS.0430** Nothing blocks. There are no hard quality gates;
  checklists and findings are advisory and the principal alone decides
  what is published.
- **POS.0440** Every finding and challenge is either fixed or explicitly
  rejected with a recorded reason (DEC). Rejecting and parking are
  legitimate outcomes; silently ignoring is not. An accepted challenge
  must change the intent, otherwise it was not accepted. The states
  in the ledger carry the words of the verdicts (POS.0850): findings
  `open | resolved | rejected | parked | obsolete`, challenges `open
  | accepted | rejected | parked | obsolete`; `open` is a state only,
  not yet judged, and `resolved` stays the critic's, a fix that is
  in the document. The finding state `overruled` is retired
  (2026-09-27): it reads as `rejected` wherever it survives, the
  immutable reviews and the decision records keep the word they were
  written with, and a project's ledger is converted through a
  finding of the `light` check, on the principal's word or never.
- **POS.0450** An artefact is best challenged before the next layer is
  first derived from it — the intent before the first assignment, one
  day a BRD before the solution design — while accepted challenges are
  still cheap to absorb. Whether it runs again later — after a draft,
  before approval — is left to the judgement of whoever is running the
  process; no rule prescribes it. (THR.0040 → DEC.0020, generalised
  from "before the first draft" when the challenger was opened to any
  artefact; the reasoning of the decision is unchanged.)
- **POS.0790** Isolation is not independence. The author, the critic
  and the challengers share one model family; what that family
  systematically cannot see, none of them will find, and agreement
  between the reviewers is therefore never treated as validation —
  it only means the artefact is consistent under one set of priors.
  The calibration point lies outside: review by humans or by a
  different model family, invited at the principal's discretion —
  independent different-family challengers are planned (POS.0800).
  External human review of the forge by experienced practitioners
  has already taken place and shaped it through the ordinary door,
  like any other input. A challenge may inspire, but supplied
  content follows POS.0070 — nothing enters the intent because a
  reviewer wrote it, only because the principal composed it — and an
  accepted challenge may change the intent by subtraction as readily
  as by addition (POS.0440 read accordingly).
- **POS.0800** Independent challengers will be built: challenger
  personas running on a different model family than the author's,
  composed by the principal in Microsoft AI Foundry and invoked from
  the forge over a CLI link, so that `/challenge` can send in a lens
  with genuinely different priors. The direction is decided; the
  mechanics are designed when taken up.

### Operating environment
- **POS.0500** The engine is one git repository, `forge-of-thought`
  (POS.0990), full name **Forge of Thought** in documents: the universal
  core in the root (`CLAUDE.md` for the agent, `README.md` for humans,
  `templates/`, `scripts/`, `.claude/`) together with `projects/forge`,
  the system's own project. User projects live under `projects/<slug>/`
  as git repositories of their own, ignored by the engine (POS.0940); a
  per-project `CLAUDE.md` is polish only where genuinely needed.
- **POS.0510** Commands are entry points into phases, not the only
  permitted door; the core rules apply in ordinary conversation too.
- **POS.0520** Protection relies on Claude Code's permission system,
  not an OS-level sandbox: commands and file operations run under
  permission prompts and allowlists, shared deny rules in
  `.claude/settings.json` block sensitive paths (`~/.ssh`, `~/.aws`)
  and raw `git` (POS.1200), and web access is approved per domain on
  first use. OS-level
  sandboxing was tried on 2026-08-04 and deliberately dropped: it is
  unavailable on Windows, where enforcing it meant no shell at all.
- **POS.0530** This work is reasoning-heavy and token-light, so the
  strongest available model tier is the default — the session model,
  chosen once, with no per-agent pins (POS.0930).
- **POS.0540** Mechanical conformance runs on the same mechanism as
  the critic and the challenger (POS.1120): its own contract skill,
  one agent per kind of check, a roster, a run by hand. Whether it is
  called a review is not decided and does not matter to the
  mechanism, which takes further kinds as they come. The checks and
  their composition are POS.1140's. Read-only and advisory: they report and
  propose, the principal decides what is fixed. They check
  conformance, never substance or document quality — that remains the
  critic's and the challenger's territory.
- **POS.0550** The engine is persisted in git with a remote of its own,
  `main` the released line, branches allowed and left to git
  (POS.1110); every user project is likewise a repository with
  whatever remote and visibility its owner gives it. The scripts in
  `scripts/` are the only door to git — reading state included, no
  exceptions, enforced for Claude by POS.1200; how many there are is
  whatever the door needs, never a rule. The scripts that serve the engine and every project that is a
  repository (`projects/<slug>/.git`): `forge-save.ps1`
  (stage–commit–push; bare, the engine and every project with changes,
  each its own commit; with a slug, that repository — `forge` meaning
  the engine; auto-generated commit message unless given; remote
  changes reconciled by rebase; without an origin, commit and a note;
  `-Tag <name>` sets a tag on the commit and pushes it, POS.1100; never
  `git add -f`, never `git clean`), `forge-pull.ps1` (fast-forward
  only, refuses over unsaved work; bare, the engine — which is the
  upgrade — and every project with a remote; with a slug, one),
  `forge-status.ps1` (engine and every project: unsaved changes, the
  branch it is on, last commit, origin or "not under git"; changes
  nothing), `forge-clone.ps1` (brings an existing project in,
  POS.1060: clones a repository into `projects/<repository name>`,
  never overwriting, and reports the commit identity git resolves
  for it) and `forge-branch.ps1`
  (creates a branch or switches to one, `main` included, bare reports
  the branch and lists the branches, and nothing else, POS.1110). No
  remote is configured anywhere in the forge: git carries that
  information itself. Immutability of documents remains a process rule
  enforced by convention, not by git.
- **POS.1200 The scripts-only door to git is a wall of the harness,
  not conduct alone; a commit carries no attribution.** Since
  2026-09-21 the engine's `.claude/settings.json` denies Claude the
  `git` command in both shells (`Bash(git *)`, `PowerShell(git *)`
  under `permissions.deny`): the rule of POS.0550 — the scripts in
  `scripts/` are the only door to git, reading state included — that
  had stood as conduct in CLAUDE.md and in the per-prompt hook
  (POS.1170) is now enforced by the permission system of POS.0520,
  tried and holding in both shells. The rule binds the forge, not
  the principal: his own git from the shell is his. In the same file
  `attribution.commit` is empty and `attribution.sessionUrl` is
  false, so Claude Code no longer adds or proposes a `Co-Authored-By`
  or `Claude-Session` trailer: the commit message is the one the
  principal confirmed, word for word — the commit 1fe1dae of
  2026-09-16 had carried both trailers unseen by him. Decided
  2026-09-21 by the principal.
- **POS.0570** The project's full conformance — the `project` check,
  for the engine `engine` too — and the renders belong to the release,
  the bookkeeping check to the save; which checks run where is
  POS.1140's. `/release` (POS.1100) runs the checks it composes and settles their findings with the
  principal before the release commit: fixed, or explicitly accepted;
  deferred findings are recorded in the ledger under "Waiting on
  principal". The recommended procedure, never a gate: nothing blocks
  (POS.0430). `/release` then renders what POS.1100 names,
  unconditionally, with no staleness test. The renders come after the
  check and its walkthrough, not before: a render made from the
  settled sources is current by construction, whereas one made before
  it goes stale whenever a finding bumps the intent. The full check
  left the save because it cost minutes and a walkthrough every time.
  The staleness of a render is never a check finding, the README and
  the release notes included: the release regenerates those two
  anyway, so the finding was void at every release and noise
  everywhere else (decided 2026-09-27); the `/forge` map shows
  staleness, and a render is regenerated only on the principal's word
  (POS.0810). Present shape 2026-09-06 (history 3.23, 3.30, 3.33,
  3.44), the check rule 2026-09-27.
- **POS.1100** Save and release are two commands. `/save` runs the
  `light` check (POS.1140) and then commits and pushes on whatever
  branch is checked out, through `forge-save`, no render: a message
  proposed and confirmed, the script run, seconds. `/release` runs on
  `main` only and refuses elsewhere, naming the branch: the checks
  POS.1140 composes, with their walkthrough (POS.0570); the README and
  release notes from the settled sources (POS.0730, POS.1000,
  POS.0810); the release commit "release <intent version>" and, at an
  approved major, the tag `v<major>` — both `/save` run by `/release`
  with the release message, not a second procedure (POS.1070). Named
  without a slug it asks which repository, never sweeps; it offers
  `critique essence` once and runs no reviewer on its own (POS.0400).
  The release number is the intent's version (POS.0730). Tags:
  `v<major>` at every release of an approved major, proposed by
  `/release` and confirmed by word — a rule of the procedure, not a
  gate in the script; any other tag on request, `/save -Tag` or
  `/release -Tag`, on a branch as well, the name free, `v<intent
  version>` proposed when none is given; the script pushes the tag
  with the commit and keeps it without an origin. Only the major's tag
  has a fixed name, so `/check` and the release notes can rely on it:
  an integer is a released major, anything else a snapshot. Why two:
  the renders cost minutes and tokens beyond reason at every save, and
  the two-speed save had existed in practice for weeks; with
  the renders at the release only, the README on `main` is current at
  every release and stale in between visibly (the `/forge` map), never
  silently. Decided 2026-09-05 (history 3.33); closes THR.0220;
  alternatives REJ.0160, REJ.0170.
- **POS.1110** Branches are voluntary and belong to git. Whoever wants
  one gets it through one forge command — `forge-branch <name>` creates
  the branch or switches to it, `forge-branch main` switches back — and
  never types git; merge, rebase and conflicts stay git's, by hand or by
  merge request, and `forge-status` reports the current branch. Nothing
  forces a branch: whoever does not use them works on `main`, saves and
  now and then releases, and sees none of this. The forge's only
  knowledge of a merge is that `/release` runs on `main` after it and
  its checks find what two branches broke — the known hole, left
  until it happens: two parallel branches taking the same next free ID.
  The boundary against the wrapper of git the principal does not want:
  the script does creation and switching, which only change where the
  next commit lands, and nothing that rewrites history. Grounded in a
  colleague's practice (history 3.33); the forge stays a single-user
  tool per instance, more people means more instances and
  coordination by git (bearing on THR.0090). Decided 2026-09-05 with
  POS.1100.
- **POS.0580** Work on the chain is invoked by target state, never by
  verb: `/forge <state>` (`/forge intent`, `/forge assignment`) —
  knowing the name of the target artefact is knowing the command, with
  nothing to memorise as layers are added. Bare `/forge` reports the
  map: which artefacts exist at what versions, which states can be
  worked from here, which renders are stale, and a recommended next
  step. Mechanics: a thin dispatcher (`.claude/skills/forge/SKILL.md`)
  plus one definition file per state
  (`.claude/skills/forge/states/<state>.md`, a supporting file of the
  dispatcher, POS.1130), each declaring its own
  inputs — so the chain is a star, not a fixed line: a future layer
  branches from any artefact by adding one file, the dispatcher
  untouched. A state file is the definition of the elicitation of
  its artefact, in the seven blocks of POS.1310, and stands beside
  the artefact's template as a pair. `/clarify` and `/draft` were
  retired without aliases on 2026-08-15.
- **POS.0590** Everything the forge produces is Markdown, renders
  included: a presentation is a `.md` saying what is on each slide
  (mermaid for pictures). The forge still ends at content, but it
  carries its delivery-format tools at its edge: `scripts/md2pptx.ps1`
  (POS.0740) turns a Markdown deck render into a `.pptx`,
  `scripts/md2docx.ps1` (POS.1150) a Markdown render into a `.docx`.
  The Markdown render remains the sole source of truth; the generated
  file is an output of second order — regenerated at will, never
  edited by hand. All other format conversion stays outside the
  forge, as git is for persistence. An output is made in two steps,
  each with its own command, divided by cost so that the expensive
  conversion runs as seldom as possible (the principal's, decided
  2026-09-27). `/render` generates the Markdown and, where the
  recipe names a format, the plain file beside it through pandoc:
  deterministic, cheap, repeated freely. `/publish` makes the
  designed file through a model and its document skills into
  `published/`: only on the principal's command, never by
  `/render`, by `/release` or on Claude's own judgement; it makes a
  file and sends nothing anywhere. `/publish` takes the render as
  it lies on disk and never renders — a render is made by a model
  and is never the same twice, so a second one would publish a text
  the principal has not read; a stale render is named before the
  conversion and the word is his. The two files never share a
  place, or the next render would overwrite the designed file with
  the plain one. A recipe that names no format ends at the
  Markdown. The format and what each step needs stand in the
  recipe's `## Format` section, which replaces the Build
  instructions of the presentation genre and is never copied into
  the render: the render carries content only, or the plain file
  would carry the instructions as text. The ledger's Published
  table says what each published file was made from and its state:
  `current` set by `/publish`, `stale` by every `/render` of that
  recipe — a date could not tell, since a render may run twice a
  day. The word is `publish` by the principal's choice, over
  `build`, Claude's recommendation; it agrees with "only the
  principal publishes" (POS.0430). CLAUDE.md carries the principle
  of the two steps — which command makes which file, who may start
  each — and the conduct of each step is its skill's alone
  (`/render`, `/publish`), the sweep of 2026-09-27 having found the
  steps restated there.
- **POS.0740** `scripts/md2pptx.ps1` generates a PowerPoint file from
  a Markdown deck definition through headless Claude Code
  (`claude -p`) with Anthropic's official pptx skill (plugin
  `document-skills` from the `anthropics/skills` marketplace,
  installed separately per user, as markitdown is for `doc2md`). The
  conversion is done by a model, never by a deterministic converter,
  because deck definitions are deliberately free-form and may
  themselves contain instructions for the LLM — slide content,
  speaker notes, diagrams to redraw as native shapes, visual
  directions. Template handling: `-Template <path>` names a `.potx`
  file by path — typically a document of a library project
  (POS.0970), e.g. `projects/lib-<name>/sources/<name>.potx`; without
  the parameter Claude designs the visual style itself. There is no
  default template and no bare-name lookup. The output defaults to the input's directory
  and basename with a `.pptx` extension, so a deck generated from
  `renders/<recipe>.md` lands as `renders/<recipe>.pptx`, tracked in
  git like any render output; `-Out` overrides. The headless run's
  model is chosen by `-Model`, default opus; a presentation recipe
  may recommend one in its Format section. Since 2026-09-27 the
  script has two engines (POS.0590): `-Engine claude`, the default
  and all of the above, is the engine of `/publish`, which names
  the recipe by path (`-Recipe`) so that the model reads the Format
  section there; `-Engine pandoc` makes a plain deck for reading,
  one slide per second-level heading, and is the engine of
  `/render`. The pandoc engine was run once, on 2026-09-27: the
  executive pitch gave a deck of six slides.
- **POS.1150** `scripts/md2docx.ps1` converts a Markdown render into
  a Word file through `pandoc` — a deterministic conversion, unlike
  `md2pptx` (POS.0740), because a document render is plain Markdown
  carrying no instructions for a model. Styles come from a reference
  document named by path (`-Reference`, a `.docx` or a Word template
  `.dotx`/`.dotm`, typically a document of a library project,
  POS.0970); without it pandoc's built-in styles apply — no default
  reference and no bare-name lookup. The page is A4 by default:
  pandoc's built-in reference names no page size and Word then falls
  back to US Letter, so without `-Reference` the script writes the
  page size into pandoc's own built-in reference (`-PageSize A4 |
  Letter`, A4 when absent); with `-Reference` the page setup is the
  reference document's own, since a template decides its own paper.
  The render's provenance front-matter is metadata to pandoc
  and does not appear in the document. Mermaid diagrams land in the
  document as blocks of code: rendering them to pictures needs
  `mermaid-cli`, a further dependency the principal has not decided
  on (Waiting on principal in the ledger). Word is the target and
  PDF is not: pandoc writes Word without a further engine, and a PDF
  is the recipient's one click from Word. The output defaults to the
  input's directory and basename with a `.docx` extension, tracked
  in git like any render output; `-Out` overrides. pandoc is
  installed by the user, as markitdown is for `doc2md`; the script
  installs nothing. Decided 2026-09-12; the template extensions
  2026-09-19, the A4 default 2026-09-20. Since 2026-09-27 the
  script has two engines (POS.0590): `-Engine pandoc`, the default
  and all of the above, is the engine of `/render`; `-Engine
  claude` makes the designed document through headless Claude Code
  and the official docx skill, the reference document as the
  template it starts from, the recipe named by path (`-Recipe`),
  and is the engine of `/publish`. The route through a model had
  been set aside on 2026-09-12 as a way to Mermaid pictures
  (THR.0370); the principal takes it now for the design of the
  document. The claude engine was run three times on 2026-09-27,
  on the CTO pitch without a reference document. Two runs made the
  file in minutes; one ran over ten minutes without a result and
  was stopped, the cause not known. The machine carries neither
  the library the docx skill expects nor the tools that show the
  model its pages (LibreOffice, Poppler), and the model is told to
  install nothing: it writes the document's XML directly and
  designs without seeing the result - enough for a page of text,
  untried for tables, pictures or a template. The engine runs
  under whatever configuration directory and login the calling
  shell has: a run from a plain terminal failed at once on an
  expired login.
- **POS.0770** Recipe composition may be guided by genre:
  `/recipe <genre>` mirrors the `/forge` star (POS.0580) — a thin
  dispatcher (`.claude/skills/recipe/SKILL.md`) plus one definition file
  per genre (`.claude/skills/recipe/genres/<genre>.md`, a supporting
  file of the dispatcher, POS.1130) carrying the
  elicitation checklist, with the genre's canonical skeleton in
  `templates/recipe-<genre>.md` extending the base recipe shape,
  never replacing it. Bare `/recipe` lists the roster; a recipe
  outside any genre stays legitimate, composed conversationally from
  `templates/recipe.md`; naming an existing recipe iterates it
  through the same lens. The first genre is `presentation` — a
  slide-by-slide deck definition whose render `md2pptx.ps1` turns
  into a PowerPoint file — distilled from the first deck recipe;
  its interview covers audience and register, the one
  message, inputs (including renders as picture sources), dramaturgy,
  speaker notes and traceability citations, on-slide density, diagram
  policy, language, vocabulary discipline, confidentiality, and the
  Format section, which stays in the recipe (POS.0590). The genre is named "presentation" rather than
  "deck" for company-wide legibility at rollout.
- **POS.0830** The forge runs beyond Windows. `scripts/` is the only
  platform-bound layer, and its scripts are written to run unchanged
  on Linux and macOS: they are PowerShell 7, which is itself
  cross-platform (`pwsh`, one install on a non-Windows machine), and
  they use nothing Windows-only — paths composed with `Join-Path` or
  forward slashes, no `cmd`, registry or Windows-only cmdlets,
  `$IsWindows` only where the platform genuinely differs, external
  tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH,
  and usage
  examples in the scripts' help free of Windows-specific paths and
  invocations. Instance facts are out of the scripts: no remote URL,
  no author identity, no first-run initialisation — git configuration
  is the user's (POS.0950). Portability is verified by running the set on Linux
  (WSL suffices); until then it is a writing rule, not a claim.
- **POS.0940** Mechanism of the engine/projects split. The engine is a
  clone; the projects are nested git repositories in a gitignored
  `projects/*` with `projects/forge` re-included (`!projects/forge`; the
  pattern must be `projects/*`, not `projects/`, or the re-include fails
  silently). The engine does not know the projects: the scripts
  recognise a project by the presence of `projects/<slug>/.git` —
  without it, status reports "not under git" and save and pull skip it;
  with it, they commit and push to its origin. `git init` and the remote
  are the user's one-off act: `/new-project` and `/spinoff` create files
  only and never touch git, and a project starting "not under git" is a
  property, not a defect. A project without a repository, or with a
  repository and no origin, is a legitimate shape — a sensitive project
  kept local; the second keeps the history the renders and recipes rely
  on, the first does not. Upgrade is `forge-pull` on the engine — a
  fast-forward of `main`; the engine receives the git tag `v<major>` at
  every release of an approved major of this intent, and any tag on
  request (POS.1100). A project records no engine version: `/check`
  measures it against the current conventions. That is the whole
  migration path of any instance, the principal's and a third party's
  alike: after `forge-pull`, `/check project` on each project says what
  the conventions changed, the release notes' Action required lines say
  what to do, and Claude migrates on the user's word; no migration tool
  exists, knowingly (DEC.0100). Verified by test (research
  `2026-08-29-git-engine-projects-separation.md`); shapes rejected:
  REJ.0150. Decided 2026-08-29 (history 2.21); closes THR.0130.
- **POS.0950** The engine carries no instance facts. Who the principal
  is (by role) and what language the conversation runs in live in
  `CLAUDE.local.md` at the engine root — gitignored, created from
  `templates/CLAUDE.local.md` and filled by `/setup` on a new machine
  (POS.1050); the root is where Claude Code looks for it, and
  everything there reaches every subagent, the isolated reviewers
  included (THR.0240). Therefore only what must be always-on and is
  harmless in a public report lives there; the git identities —
  names, e-mail addresses, hosts — live in the user's own git
  configuration outside the engine (below), and CLAUDE.md, Isolated
  reviewers, which every reviewer contract cites, forbids instance
  facts in a report (CHL.0170; the split of an
  existing instance file is the user's act on the release notes'
  word). The session model lives in `.claude/settings.local.json`
  (POS.0930). `CLAUDE.md` names the principal and the conversation
  language only as things that exist, never by value; the document
  language is the project's own (POS.0060). The scripts carry no URL and no
  identity (POS.0830). The commit identity is git's business, not
  the forge's: it is resolved per git host by the user's own
  configuration — one `includeIf "hasconfig:remote.*.url:<host
  pattern>"` stanza per host in `~/.gitconfig`, pointing at a file
  `~/.gitconfig-<host>` that carries that host's `user.name` and
  `user.email` — and the forge sets no identity anywhere: no roster
  file, no local `git config user.*` at a project's creation or
  import. Reversed 2026-09-16, written 2026-09-18 (intent 4.12): from
  3.46 to 4.11 the identity was a property of the project, set
  locally in every repository and proposed by the command layer from
  a roster in `identities.local.md`, and the per-host include was
  rejected because a host is only a correlate of the identity and
  fails where one host serves two roles. In the field the roster
  duplicated what the user's includes already resolved, every
  repository carried the same identity twice, and the forge had
  gained a file, a template and three identity steps for a case that
  had not occurred. The two-roles case is accepted as a risk the
  user resolves by hand with a local `git config user.*` of his own,
  which git lets win over the include. What the forge keeps:
  `/setup` (POS.1050) offers to write the stanzas and the one global
  guard — `user.useConfigOnly = true` with no global
  `user.name`/`user.email`, so that a commit in a repository on a
  host with no stanza fails aloud instead of silently taking a
  default (a surviving global identity defeats the guard, and
  `/setup` says so) — and `forge-save` checks that git resolves an
  identity for the repository and, where it resolves none, reports
  it with the command to set one and commits nothing until it is.
  Resolves the scripts part of THR.0090.
- **POS.0930** One model for the whole forge. Every command, chain
  state and reviewer runs on the session model; the reviewer agents
  declare `model: inherit` explicitly, so that the strongest model the
  forge runs on is a decision and never an accident of a pin that has
  aged. Speed is bought with context, not with weaker models:
  `/render` generates in an isolated subagent that sees only the
  recipe and its inputs, never the working conversation — the same
  principle as the reviewers', applied to a mechanical job — and a
  command's `effort:` remains the lever for routine turns should one
  ever need it. Per-command pinning to a faster model is rejected for
  now: the routine commands are a small share of the work and slow for
  the size of the context they carry, not for the model, and every pin
  is a convention to keep. A per-recipe `model:` is deferred until a
  recipe is genuinely mechanical, since a smaller model drifts from a
  recipe that leaves it room (the drift POS.0810 guards against). The session model is chosen in one
  deliberate place, `.claude/settings.local.json` — an instance
  preference, gitignored (POS.0950). The one exception is
  `scripts/md2pptx.ps1`: a headless run has no session model, so the
  script needs a default of its own (`-Model`, POS.0740) — an
  explicit parameter, not an aged pin. The same lever carries the
  checks: every check executes its own definition in an isolated
  subagent that sees only the files, returning the report for the
  walkthrough in the session, and `/release` launches its renders in
  parallel (which command renders what is POS.1100's); the working
  conversation is spent on verdicts, not on reading. Present shape
  2026-09-02 (history 2.13, 3.10); closes THR.0160.
- **POS.1070** One mechanism lives in one place and is used from
  there. Whatever the forge already has a procedure for — a command,
  a skill, a script, an agent — is invoked through that procedure
  whenever its situation arises, never re-described ad hoc:
  `/release` regenerates the README and release notes through
  `/render` and ends by running `/save`, git is touched through the
  scripts in `scripts/` (POS.0550), reviews run through the reviewer
  agents. A command that needs another's mechanism references it by
  path and adds nothing of its own to how it runs; the rules of a
  mechanism — isolation, wrapping, provenance, what may be read — are
  written once, in its own definition. Restating a procedure in a
  second place is a defect: the two copies drift, and the copy without
  a rule silently loses it. The `single-source-of-truth` check carries
  the standing rule — a restated procedure, a reviewer file restating
  what its contract skill owns (POS.1120), a direct operation where a
  script, command or agent exists — over the whole operating layer,
  run on the principal's word and never at a release on its own
  (POS.1140), so that the rule costs a release nothing and the sweep
  is honest when it runs. Where a shape had no owner at all, it gets
  a skeleton rather than a second description: the bundle catalogue
  (`templates/index-bundle.md`), the library reduction of the ledger
  (`templates/ledger.md`'s header), the state vocabularies of
  findings and challenges and the reading of an older state word
  (`templates/ledger.md`'s Findings and Challenges comments), the
  reading of an older recipe's `## Build instructions` as Format
  (`templates/recipe.md`'s Format comment). A restatement is steps,
  rules or a shape repeated; a one-line reminder at the point of
  action that names its owner — "not under git is a fact, not a
  defect (CLAUDE.md, Persistence)" — is not one, since it is what
  Claude reads when he acts and the citation keeps it honest
  (decided 2026-09-27 at the sweep). Raised by the principal
  2026-09-02 after a render made outside `/render` arrived unwrapped
  (history 3.10).
- **POS.1090** The harness enforces the principal's word where it
  can. A command that writes, scaffolds, commits or regenerates —
  `/save`, `/release`, `/spinoff`, `/setup`, `/new-project`,
  `/import-project`, `/ingest`, `/render`, `/publish` — carries
  `disable-model-invocation: true` in its
  front-matter, so that Claude cannot start it on his own judgement:
  the principal invokes it by slash, or asks in words and Claude
  follows the command's definition read by path, as the dispatchers
  do. The state and genre files behind `/forge` and `/recipe` carried
  the same field while they were registered as commands; since
  POS.1130 they are supporting files registered as nothing and need
  no guard. Maps, reports and rosters (`/forge`, `/ledger`, `/check`,
  `/critique`, `/challenge`, `/research`, `/recipe`)
  stay model-invocable, since Claude is meant to propose them. The
  guarantee of Step by step (CLAUDE.md, Working methods) thereby
  rests on the harness as well as on CLAUDE.md, and the descriptions of the guarded
  commands leave the always-on context. Decided 2026-09-05 at the
  walkthrough of the harness critique (FND.0210, FND.0190). Step by
  step names one more such step since 2026-09-14: the birth of a new
  versioned document — a brief, a recipe, a layer of the chain —
  happens on the principal's word, never as a by-product of another
  operation (P.05, F.06: a second recipe and its render created
  without a word, a brief written under `/forge intent`).
- **POS.1130** The commands are skills. Every command lives as
  `.claude/skills/<name>/SKILL.md`; `.claude/commands/` no longer
  exists. The state files of `/forge` and the genre files of `/recipe`
  are supporting files of their dispatcher
  (`.claude/skills/forge/states/<state>.md`,
  `.claude/skills/recipe/genres/<genre>.md`): read by path, registered
  as nothing, carrying a description and no registration field. The
  reviewers' contracts (POS.1120) are skills of the same directory,
  not user-invocable. "Command" stays the word for what the user
  invokes by slash; "skill" names the file shape, commands and
  contracts alike. Grounds: in Claude Code custom commands have been
  merged into skills — a command file and a skill of one name create
  the same `/name` and work the same way, existing command files keep
  working, skills are the recommended form — and a skill adds what
  this layer wants: supporting files without registration, `context:
  fork` with an agent type (set aside, POS.1140), named `arguments`.
  No context gain: a command's body and a skill's alike load only
  when invoked, so THR.0240 is untouched. A skill shadows a command of
  the same name, so a migration is whole, never partial. Every
  `argument-hint` is quoted: a front-matter with CRLF line endings and
  an unquoted hint of two bracketed items fails to parse, and the
  harness then shows the body's first line as the description.
  Decided and migrated 2026-09-06 (history 3.43); closes THR.0330,
  resolving FND.0260.
- **POS.1140** Check runs on the reviewer mechanism — POS.0540 decided
  it, this is the shape. One command `/check <check> [slug]`, bare the
  roster; one contract skill `check-contract` — conformance only,
  read-only, findings only with `file:line`, the rule's owner and one
  fix, ranked by severity; a report returned to the session, nothing
  filed and no ID sequence, since a check's findings are settled at
  the walkthrough and recorded by the session where they change
  something; one agent per check, `check-<name>`, front-matter and
  Lens only, from `templates/check.md`; the roster open, a new check
  one file. The first checks, each owning one concern and none
  another's: `project` — structure, IDs, assignment style, language,
  immutables, recipes and renders; `light` — front-matter against the
  companion, the ledger against the files, dependencies, resource
  indexes, fit for a save; `engine` — the core against itself and the
  forge intent, the rename sweep; `single-source-of-truth` — the
  whole operating layer for restatements and direct operations
  (POS.1070), the honest sweep, expensive by design, run on the
  principal's word before a major or after a round on the operating
  layer, never by `/release` on its own, a project on request. A rule
  an older position attributes to `/check` as one procedure belongs
  to the check that owns its concern by this list — bookkeeping,
  ledger, dependencies and indexes to `light`, structure, recipes and
  renders to `project` — never to two. Composition is the caller's
  and checks never call each other: `/save` runs `light`; `/release`
  runs `light` and `project`, for the engine `engine` too, launched
  at once; anything else is the principal's word. The engine is
  checked as `/check engine`, the forge project as `/check project
  forge`; `/check-forge` is gone. The word for a check's variants is
  "check" — the light check, the project check — the mechanism's name
  serving for its members. `context: fork` is set aside: the field
  fixes the agent type in a skill's front-matter, so it cannot serve
  a dispatcher that chooses an agent by argument; the isolation stays
  what `/critique` and `/challenge` do — the Agent tool with the
  target path and nothing else (POS.0930). Decided 2026-09-06 by
  walkthrough of THR.0290 and built the same day (history 3.44); the
  `/research` point stays in THR.0290.
- **POS.1190 The forge explains itself from its own definitions.**
  `/man [command|method]`, alias `/manual`, is the forge's manual —
  a reader, never a text of its own (POS.1070). Bare, it lists the
  commands from the Commands table of CLAUDE.md and the working
  methods from its Working methods section, one line each. With a
  command, it prints that command's purpose and arguments from the
  `description` of its skill and the roster the command dispatches
  over — checks, lenses, personas, genres or states — each with the
  `description` of its own file and, where the file carries one, its
  Lens or Checklist section, so that the user knows what a check
  looks for before running it. With a method, the paragraph of
  CLAUDE.md and the skill that holds the method's shape. Named after
  the Unix manual, `/help` being a built-in of Claude Code; the alias
  is a second skill whose whole body invokes the first, since a skill
  has no alias field. Decided 2026-09-18 for the newcomer's first
  hour and for the reader who opens the repository (THR.0390).

### Naming
- **POS.0600** The system is named **Forge of Thought**: thoughts are
  the raw material — of whatever kind, nothing is presumed about them —
  and forged assignments are the product. Chosen with the full-chain
  vision in mind (assignment → BRD → architecture → full realisation
  deck); "Assignment Studio" was dropped because it named only the first
  segment and only the first audience. Repository `forge-of-thought`
  (POS.0990), slug `forge` for the system's own project under
  `projects/`, full name in documents; the short form "Forge" is
  expected in daily speech.
- **POS.0610** Project slugs are lowercase and hyphenated on disk;
  display names may differ. Programme naming is used where a family of
  initiatives is expected: FLOW (Future Lean Operating Way), first
  instance FLOW:BA → slug `flow-ba`. Names must be legible to the
  audience, not only to the principal.
- **POS.0620** The README subtitle is "*A workshop where thought is
  tempered and shaped.*" Any subtitle or one-line description must
  present the forge as a place and space where thoughts are forged; it
  must not name the assignment as the goal, because the assignment is
  only where version 1 of the chain happens to end. "Forging thoughts
  into assignments" was dropped for exactly that reason; "A forge for
  thought" was dropped as a tautology of the name.

### Growth path
- **POS.0700** The principal intends to keep extending the engine
  downward: thoughts are forged as far as he needs them taken. The BRD
  layer is certain to come; solution architecture and integration are
  intended; a strategy layer is possible if it proves to make sense.
  Which layers are added, and in what order, is open — possibly all of
  these, possibly none yet. Nothing is approved for construction: the
  mechanics of a layer (commands, agents, reviewer calibration) are
  designed when that layer is actually taken up, not in advance. An
  earlier `/elaborate` mechanics proposal was withdrawn as premature.
  The layers below the assignment grow in the same project, by the
  same principal's hand, when he chooses to take his own thought
  further — a BRD as his next layer, not as someone else's
  deliverable. What a recipient does with an assignment in his own
  instance is his own forge run: the assignment becomes his brief, by
  his hand today (an assignment is self-contained for exactly that),
  by a command of its own only when that day comes (THR.0090). The
  chain never spans two principals (CHL.0140, 2026-09-06).
- **POS.0760** The forge is split into a public engine and user projects
  in repositories of their own. The engine — the core together with
  `projects/forge` — is public and contains nothing sensitive and no
  instance facts (POS.0950, POS.0980); users keep their projects
  wherever they choose and are themselves responsible for what those
  contain and where they live, generated decks carrying corporate
  branding included. Decided on 2026-08-29 from
  `00-brief-public-engine.md`; the mechanism is POS.0940.
- **POS.0780** The forge is a general tool for forging thoughts, and
  a forge run ends where its owner is satisfied: the outcome is an
  artefact the principal stands behind — nothing further. An intent
  may be immaterial and carry no delivery at all; the chain's
  mechanics are domain-agnostic — the same machinery that forges a
  platform assignment would forge a D&D campaign: an intent of the
  story, then materials rendered for the DM. Sponsorship, funding,
  adoption and delivery outcomes are outside the forge's scope and
  outside its sight. The door stays open, not closed: the forge may
  one day feed a delivery chain, and experience from use flows back
  through the ordinary door — the principal, via `/forge intent`
  (POS.0170) — as input like any other; whether a delivery side
  would be grown layers of the forge or a separate framework is
  deliberately undecided (THR.0140). The forge itself is developed
  at the principal's discretion and pace, by his needs and by the
  feedback its company rollout returns: direction may be named
  (POS.0700), destinations and deadlines are not.
- **POS.0980** Publication. The engine is the principal's to publish: it
  was built outside any work assignment and lived on the company's git
  only because it carried work information not yet separated. The
  audience, in order: rollout in the company first, at the same time a
  public project around which a community may form, and a showcase of
  the principal's work; the split also lets access be granted per
  project, where before a collaborator had to be on everything. The
  boundary for the public `projects/forge`: nothing company-specific by
  name — no company name, no URLs, no e-mail addresses, no content of
  the company projects; the slugs of the company projects stay, since
  that projects of those names exist and travelled the chain is a
  process fact, not content (THR.0210 draws the line); a
  forbidden-term list is no guard, since a grep catches names, not
  content. The public forge project holds nothing outside that
  boundary, its immutable documents included — rewritten once before
  publication, immutability knowingly broken, recorded in the ledger
  and nowhere in the files; the brief is English for the same reason,
  a one-time yield of POS.0060. The public repository has a fresh
  history (DEC.0080); the full record is on the company host, archived
  read-only, its last complete state tagged `pre-split`. Until a public exemplar exists (THR.0200) the README carries
  no example project. Separating the company projects from the engine
  without publishing would have been a fallback only if publication
  were long and complicated; it was not. Present shape 2026-08-30
  (history 2.21, 3.0; from `00-brief-public-engine.md`; research
  `2026-08-29-split-migration-runbook.md`).
- **POS.0990** The public face. The engine lives at a public repository
  of the principal's, named `forge-of-thought` — the bare word "forge"
  is overloaded on every code host and says nothing in a search — under
  the licence **CC BY 4.0**: anyone may use and adapt the engine, and
  must credit the author and link to the repository. The README
  therefore names one person, the licence holder — the author with a
  contact address — as a fixed text of the readme recipe, and this is
  not an instance fact: it is who the work is by, whoever runs an
  instance. The `LICENSE` file carries the licence's verbatim legal
  code. Decided and executed 2026-08-30, with the first public commit.
- **POS.1000** Every project has a README and, if it is a thought
  project, release notes — both renders of the project's own recipes
  (`recipes/readme.md`, `recipes/release-notes.md`, `output:` in the
  project root), exactly as the engine has them (POS.0720, POS.0730;
  POS.0810 for the review of the regenerated output): the recipe is what
  is iterated, the render is never edited by hand, and every `/release`
  of the project regenerates both after its check (POS.1100). A library has a
  README only — a catalogue of what it holds and how to use it, from its
  ledger and indexes — since release notes are compiled from the
  Notes lines of an intent's history rows, which a library does not
  have; its history is git. The two recipes are genres of `/recipe` (skeletons
  `templates/recipe-readme.md`, `templates/recipe-release-notes.md`),
  scaffolded by `/new-project` and expected by `/check`; the ledger's
  Renders table carries them like any render. Every README closes with
  one fixed sentence, part of the readme genre: reading the repository
  needs nothing beyond a Markdown viewer, maintaining and evolving it
  needs Forge of Thought — the engine, linked
  (github.com/pche-broken-artist/forge-of-thought) — so that whoever
  finds the project knows what runs it (principal's decision
  2026-08-30). The engine's own README is the one exception: the
  sentence exists to point a visitor to the engine, and the engine's
  README is that destination (3.6).
- **POS.1010** A project may carry an icon: `logo.png` in the project
  root, supplied by the principal, picked up as the repository avatar by
  hosts that do so. Optional — a project without an icon is complete;
  `/check` does not report its absence. No `assets/` directory exists;
  one is introduced only when images beyond the logo appear.
- **POS.1020** A project registers what it relies on outside its own
  repository. The ledger carries a Dependencies table — path, library,
  used by, note — with one row per document of another repository the
  project cites: a deck template named in a recipe, a library document
  an index entry or a position refers to. Registration only, like
  sources: what the document is for lives where it is used. No version
  is recorded — a library document is maintained by its owner and cited
  as a moving target by design (POS.0970). `/check` verifies that every
  registered path exists on disk and reports a library that is not
  cloned alongside; an index entry or recipe pointing outside the
  project without a row is a finding. The `/forge` map says which
  libraries the project needs, and the project's README carries the same
  line. `/ingest` registers the row when the principal directs a project
  to a library document instead of copying it. Rationale: a
  cross-repository citation is a dependency taken knowingly (POS.0970) —
  knowingly means written down where state lives, not discovered when a
  render loses its template.

- **POS.1030** The forge's behaviour lives in the engine, never in the
  assistant's private memory. Claude Code keeps a per-directory memory
  outside the repository; whatever it learns there about how the forge
  should work — a working method, a rule of a command, a convention — is
  written into CLAUDE.md, the commands or the templates and removed from
  memory, so that every instance of the forge behaves the same and a new
  user meets the same forge as the principal. Memory is left with what
  is personal to one principal — his idiom, his private choices — and
  instance facts go to `CLAUDE.local.md` (the commit identity is
  git's, POS.0950). Decided 2026-08-30 at the audit before the first
  fresh deployment (history 3.0).
- **POS.1040** A source has one form. A file in `sources/` is either
  text or a functional binary, never both by default. At `/ingest`
  every binary file — isolated or inside a bundle — gets one question:
  convert to Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and
  that extract is the source — tracked in git, registered in the
  ledger, catalogued in the index with Origin "extract of `<original>`
  (markitdown)", immutable from registration; the original is not
  copied into the project, and where it already lies in `sources/` it
  is added to `sources/.gitignore` and stays local. No: the binary is
  the source as a functional thing — a deck template, a graphic, a
  logo — copied, registered and catalogued as is, with no extract.
  Text files get no question. Keeping both is the exception, on the
  principal's explicit word. The ledger's Sources column reads Form
  (`text | extract of <original> | binary`); the `light` check treats
  a binary without an extract and an extract without its original as
  the normal case. Reason: the repository carries what the forge works
  with — text — and a binary nobody reads from git is weight without
  use; a binary that is used as a thing is kept because it is used.
  Transition: the convention applies from its date on; extracts made
  before keep their `.extract.md` names, and a binary already in git
  beside its extract leaves the index on the principal's word, never
  automatically. Decided 2026-08-30 (history 3.1). Three additions of
  2026-09-14 from the run record of `health`: `/ingest` takes text
  pasted into the conversation as well as a file, storing it as
  `sources/<slug>.md` with a two-line header and registering it like
  any file (P.10, G.04: 32 sources arrived by paste and were stored by
  hand and by temporary scripts); before storing, personal matter — a
  named private person, an identifying detail, health, anything of
  the kind — stops the command and asks, store as it is, redact before
  registration or drop, never stored first and asked afterwards, and
  unconditionally, no rule in the project needed (P.11, G.09,
  simplified by the principal); and the role of a source is his word,
  never inferred — after registration Claude always asks "what is it
  for?", and he answers with the role or tells Claude to infer it,
  which is then written marked *(inferred)* — with the reply after
  registration three lines at most: the file and its index entry,
  what the source adds to the intent in one line or "nothing new",
  and that question (P.06, F.05: every source once triggered a page
  of analysis).
- **POS.1050** First run is one command. After cloning the engine,
  `/setup` prepares the instance: it fills `CLAUDE.local.md` from
  `templates/CLAUDE.local.md` in an elicitation interview — the
  conversation language first, then who the principal is by role,
  since the first correction of a newcomer's run was the language of
  the first question (P.15, G.13, 2026-09-14) — and it creates
  `.claude/settings.local.json` with
  the session model set to **Fable**, without asking: the strongest
  available model is the forge's default (POS.0530), the whole forge
  including the blind reviewers runs on it (POS.0930), and a
  newcomer's first minute is no place for a model decision. The
  command says in one sentence that Fable was set and that `/model` or
  editing the file changes it at any time. `/setup` never overwrites:
  an existing instance file or `settings.local.json` is reported as it
  stands, not replaced. The interview closes with the git identity,
  which is git's (POS.0950): `/setup` asks for the hosts the user
  pushes to, a name and an e-mail for each, and offers to write the
  `includeIf` stanzas into the global git configuration file git
  actually reads (found through `--show-origin`, the stanza paths
  absolute — `~` in git's hands and in the shell's may differ, as on
  the principal's machine on 2026-09-16), each `~/.gitconfig-<host>`
  created with its `[user]` when missing, together with the global
  guard `user.useConfigOnly = true` — the file read first, never
  overwriting existing content, an existing stanza or guard reported
  and left — all written on the user's word; declined, printed for
  him to apply by hand. Where the file carries a global `user.name`
  or `user.email`, `/setup` says the guard only bites once that
  identity is removed and offers the removal, again only on his word.
  `/setup` runs no git operation — the user's git configuration files
  are the one thing it may edit outside the engine, on his word. Named
  `/setup`, not `/init`: Claude Code's built-in `/init` generates a
  CLAUDE.md, and the collision would send a newcomer to exactly the
  wrong action at the most sensitive moment. Decided 2026-09-01 after
  a newcomer's first run (history 3.7–3.8).
- **POS.1060** A project arrives through the scripts-only door.
  `/import-project <git-url>` brings an existing project into the
  forge: it calls `scripts/forge-clone.ps1` (POS.0550), which clones
  the repository into `projects/<repository name>` — no slug
  parameter: the directory falls out of the repository's name, and a
  nonconforming name is fixed by renaming the directory afterwards —
  refuses to overwrite an existing directory, and reports facts: the
  last commit, the origin, the commit identity git resolves for the
  fresh clone, and whether the project carries a ledger with a `kind:`
  header (its absence is a fact, not a defect). The script carries no
  identity and sets none (POS.0830, POS.0950): it reports the
  identity git resolves for the clone from the user's own
  configuration, and a clone for which git resolves none is caught
  by `forge-save`, which reports and commits nothing (POS.0950). Work
  then starts by selecting the project —
  `/forge <slug>` — because the engine does not track it and cannot
  guess it.

## Open threads

- **THR.0090** Multi-principal use. Current working assumption: a second
  principal receives Forge — including the `forge` project itself — via
  git and runs their own instance. How genuine multi-user operation
  would work is an open point for the future; deliberately not being
  worked on now. One case named 2026-09-06 (CHL.0140, POS.0700): an
  assignment handed to a colleague's instance as his brief — how it
  is seeded, how the IDs continue, where the essence lens finds a
  parent; this thread's, when it is taken up.
- **THR.0140** The delivery side. Whether the forge's output one day
  feeds a delivery chain as grown layers of the forge or hands over
  to a separate delivery framework is open and deliberately not
  worked on now; it is taken up when a subject project first needs
  the linkage — flow-ba is a natural candidate.
- **THR.0150** Replacing the PowerShell scripts with POSIX `sh`.
  Considered: a single `scripts/*.sh` set (POSIX, no bashisms — macOS
  ships bash 3.2), run on Windows in Git Bash, which comes with Git
  for Windows and is required by Claude Code anyway — so no platform
  gains a dependency, unlike the `pwsh` install POS.0830 asks of
  non-Windows users; from PowerShell the call is
  `sh ./scripts/<name>.sh …`, Claude calls them directly. The
  principal is undecided whether to do it at all; no priority while
  PowerShell 7 suffices. If taken up: the set is replaced whole, never
  run side by side. Already excluded: a dual `.ps1` + `.sh` set (two
  truths drift apart) and a rewrite in Python (a dependency without
  benefit; Python stays only for markitdown).
- **THR.0170** Branch documents. Considered on 2026-08-27 alongside
  POS.0920 and deferred as too heavy for now: a working document per
  large whole (`branches/<name>.md` — a verbatim seed followed by
  positions and threads worked like the intent, states `open | merged
  | dropped`, merged into the intent with provenance or dropped to a
  REJ). To be taken up only if a brief in draft turns out to need
  structured, position-level work before it can be locked and mined;
  until then a draft brief is the branch.

- **THR.0190** A plugin as a later distribution layer. Claude Code
  plugins would give the only real upgrade channel and project =
  repository, but a plugin carries no `CLAUDE.md`, and commands are
  discovered only up to the repository root — so it forces changes
  nobody needs yet: shortening the core to a bootstrap skill injected by
  a SessionStart hook (as Superpowers does; its repository `CLAUDE.md`
  is for contributors only), rewriting the commands from
  `projects/<slug>/` to the repository root, solving multi-project
  operations. A `CLAUDE.md` split is not a cheap step: 435 lines, and
  moving half the rules from always-on to on-demand is a behaviour
  change ("200 lines" is a recommendation, not a limit). `@import` of
  the forge `CLAUDE.md` into a user's works but carries only
  `CLAUDE.md`, not commands and agents. No preparation now; taken up
  when `forge-pull` proves an insufficient upgrade channel. Research:
  `2026-08-29-claude-code-packaging.md`,
  `2026-08-29-framework-distribution-in-the-field.md`.
  2026-09-14: to be merged into the brief `engine-split` (THR.0230),
  after THR.0350. The research
  above answered a different question — how
  the forge reaches users with projects of their own, where the clone
  with nested repositories won (POS.0940), rightly — and is not
  reused for the three-layer question; that question gets research of
  its own.
  2026-09-28, from `00-brief-elicitation.md`: the objections
  recorded here largely fall once CLAUDE.md stays in the engine and
  a framework is a package of instances; for the brief
  `engine-split`.
- **THR.0200** The public face: an exemplar project for the README — the
  forge itself, or one created later; the company projects cannot
  travel. Until one exists the README carries a one-sentence placeholder
  (readme recipe 0.24). Repository name and licence settled in POS.0990.
- **THR.0210** A guard rail for the public boundary. The rewrite before
  publication (POS.0980) found the leak surface where the challenge
  predicted it: the forge project's own artefacts quoting the substance
  of subject projects — a sentence of a company intent in a CTO
  challenge, a deck's name in a position. A grep before a push is a net,
  not a rule. Wanted: a standing rule that `projects/forge` never
  carries the *content* of a subject project — only process facts: that
  a project exists, its versions, dates and counts — and a home for it:
  CLAUDE.md, the challenger and critic prompts (they read the subject
  projects as evidence), a check as a sweep, or all three. Opened
  2026-08-30 at the principal's direction.
  **Parked 2026-09-03** by the principal: the risk is small while he
  knows of it, and a rule with its checks would add weight the forge
  does not need now; not closed, to be taken up when the boundary is
  next at stake (a publication of a further project, a reviewer run on
  `projects/forge` with subject projects in reach). Claude's proposed
  solution, recorded for that day: a check, not a critic lens, and
  not the check alone. Not a lens, because the critic reads the chain
  and the leak surface lies outside it — challenges, research notes,
  templates, recipes, README — and a lens runs on the principal's word
  while the boundary must hold before every push; the matter is a
  convention of the repository, which is the engine check's job at
  every `/release` of the engine. Not the check alone, because a check
  catches a leak after it is written, and challenges, reviews and
  research are immutable from creation and written by isolated agents
  that read subject projects as evidence — a leak there is repaired
  only by breaking immutability again. Hence two homes: a check of
  its own owning the rule (POS.1140) (the engine — core, operating
  layer, `projects/forge` with its immutable documents — carries no
  content of any subject project; a process fact is admissible:
  existence, slug, kind, versions, dates, states, counts, commands run;
  content is not: a position, a requirement, a quoted or paraphrased
  sentence, a deliverable's name, a person, an organisation, a host;
  verified by reading, never by a term list, POS.0980), and one
  sentence under Inputs in both contract skills (POS.1120) citing
  that item, reaching every agent.
  CLAUDE.md deliberately left out: the rule concerns one project, not
  every session, and THR.0240 argues against another sentence in the
  core. A position under the next free POS number records the
  decision when it falls.
  At stake again 2026-09-20: a company name stood in an unsaved line
  of the ledger and was caught by hand before any save. Found the
  same day and left as they are, the principal to say: three mentions
  of a library's name, which carries the company's, in history rows
  already published — the intent's row 3.23 and rows 0.2 and 0.3 of
  the executive pitch recipe; append-only records. The principal's
  proposal of that day: a check, perhaps `light`, that nothing
  specific to his work for a company reaches the engine's git.
  Claude's sketch, offered once: a sweep for names over the engine
  only, since private projects are meant to carry company matter, the
  names held in `CLAUDE.local.md` so that the list itself never
  reaches git; the rule on content stays a rule. A neighbour of the
  gate of THR.0400. To be taken up; nothing decided.
- **THR.0230** Can the forge be split into an engine and the rest?
  One of three separate tasks the principal named on 2026-09-26, and
  the only one this thread carries; the other two are THR.0420, the
  derivations of the forge for other jobs, and THR.0300, everything
  a user makes for himself. Opened
  2026-09-03 at the principal's direction; a large rebuild if taken up,
  to be worked out first and decided later — the principal is not sure
  it is a good idea. The idea: whatever every framework needs alike is
  lifted out of the forge into an engine they share — git through the
  scripts, the ledger and its upkeep, versioning and Version History,
  the ID scheme, isolated agents on the session model, recipes and
  renders, sources and research with their indexes, `/save` and
  `/check`, `/setup` and the instance facts — so that a new framework is
  written as content only. Forge of Thought becomes the first framework
  on that engine, not the engine itself; the picture is several small
  cooperating frameworks on one engine, not one large one that absorbs
  everything (much could be pushed into the forge, but CLAUDE.md is
  already large — THR.0240 — and the separation helps there). The
  frameworks that would sit on such an engine are THR.0420's, and
  the boundary is drawn against its cases, outlined there in varying
  depth: the product framework and the project-management one in
  enough detail to draw it against, the test analysts' version so far
  by its artefacts alone.
  What they show about the boundary: the chain is the framework's
  (its artefacts, their number, order and templates); "everything is
  Markdown" is a forge rule — the engine carries recipe and render, the
  framework names the output form; a dependency between frameworks is
  the Dependencies mechanism across a framework boundary; the ledger's
  tables are partly the framework's (tasks); agent types beyond the two
  (a verifier) are the framework's.
  *Agents.* Critic and challenger alike: the mechanism — isolated
  subagent, ledger record, states, walkthrough — is the engine's, the
  prompt content the framework's. Challenger personas are the
  framework's (a UX challenger, a challenger of a work plan). For the
  critic a nested point: what is generic (consistency, formal
  correctness) and what is the framework's — in the forge the drift
  brief → intent → assignment, perhaps further down.
  *How the engine reaches a framework at every session* — no decision
  now, every path recorded: one engine repository with the frameworks as
  directories in it (simplest, one `forge-pull` upgrades everything, but
  one CLAUDE.md and one command tree for all); the engine as a Claude
  Code plugin with each framework a repository of its own (the cleanest
  boundary; the finding of THR.0190 applies — a plugin carries no
  CLAUDE.md, so a bootstrap skill by SessionStart hook — the largest
  rebuild); engine and framework as two repositories joined by `@import`
  and a clone alongside (CLAUDE.md travels, commands and agents do not —
  copied or linked). THR.0190 is from now read as part of this question
  and stays a thread of its own.
  *Order of work.* The second framework must exist in outline before the
  boundary can be drawn; the engine is not built ahead of it. Where the
  engine is thought: decided 2026-09-07 — as a brief born in the forge
  (`00-brief-<name>.md`, the way `00-brief-public-engine.md` was),
  carrying the boundary list, the outline of the second framework and
  the target shape; mined into the intent once locked. A project of its
  own only afterwards, by spinoff of the decided part, if the decision
  calls for one.
  THR.0220 was settled on today's forge at 3.33 (POS.1100) as an engine
  matter that carries over; THR.0210 stays open on the same
  recommendation. CHL.0150 (2026-09-06, parked until after 4.0): since
  3.0 every new position has been the engine's and the boundary is
  being drawn by accretion; taken up after 4.0 if the split proves
  useful.
  2026-09-14 the principal drew a picture of three layers, and on
  2026-09-26 corrected it into the three separate tasks named above.
  What is left to this thread: an engine that owns the mechanics,
  ideally a thing of its own, the technical shape unknown and a
  further git-inside-git nesting unwanted, with the forge as one
  framework on it, through which he releases substantial new
  functionality on git. Whether that split is within our powers at
  all is what the thread asks. It is worked as one brief
  `engine-split` born in the forge (`/forge brief engine-split`)
  together with THR.0190, which closes into it at its birth; the
  name is his of 2026-09-26, after `layers` said nothing he could
  read back and `frameworks` was overtaken the same day when the
  three tasks parted. The two connections are one-way and
  conditional: if the forge is split, the derivations of THR.0420
  can live on the engine instead of each carrying a copy of the
  mechanics, and nothing in THR.0300 waits for the split at all.
  A matter for the brief, Claude's observation of 2026-09-26: the
  word *engine* today means the forge's own repository against the
  projects (POS.0500), so the deeper engine this brief proposes
  overloads it, and the brief settles that vocabulary before it
  settles anything else. His reasons for
  taking it up soon: every further change makes the split harder;
  against it, the BRD layer and the field feedback (THR.0350) are
  wanted quickly. Order agreed 2026-09-14: THR.0350 first, since the
  brief is to be born by co-elicitation, the technique the
  run record faulted. The order of the briefs is POS.1380's since
  2026-09-28: `brd` first, then `engine-split`. The
  brief's first item is research of its own into what Claude Code
  offers today for an engine carrying several frameworks — the
  packaging research of 2026-08-29 served the
  engine/projects split and is not reused. Whether every new position
  should name its layer waits for the brief to say what the layers
  are. CHL.0150 stays parked with the brief.
  2026-09-28, from `00-brief-elicitation.md`, material for the brief
  `engine-split` and nothing decided. The two ideas of the split, a
  thin engine of its own and a large forge into which frameworks are
  installed like plugins, are one thing seen from two ends, and the
  question they open is what the unit of installation is. A Claude
  Code plugin cannot carry CLAUDE.md as always-on context and
  carries everything else (research
  `2026-08-29-claude-code-packaging.md`), which divides by itself:
  the engine is the repository with CLAUDE.md and the mechanisms, a
  framework is a package of instances (definition pairs, lenses,
  personas, checks, genres). The cost is the one CHL.0110 named: the
  rules of particular artefacts must first move from CLAUDE.md into
  the definitions, which is what the elicitation per artefact does
  (POS.1310). The installation mechanism is a research question.
- **THR.0240** The size of CLAUDE.md. 523 lines on 2026-09-03 and
  growing with every iteration; THR.0190 already records that a split
  moves rules from always-on to on-demand and is a behaviour change, not
  a cut. To be dealt with sooner or later whatever becomes of THR.0230,
  which would help. Opened 2026-09-03 at the principal's direction. To
  think through: what must be always-on, what can live in commands,
  skills and templates and be read when its situation arises, and how
  the effect is measured — by behaviour, never by line count. Measured
  2026-09-06 at the THR.0270 trial (POS.1120): every reviewer subagent
  receives, in its first user message before the task, the whole
  CLAUDE.md together with `CLAUDE.local.md` (then still carrying the
  git identities, since moved out, POS.0950), the assistant's memory
  file and the git status — about 600 lines, the largest block of its
  context, several times its own agent body and contract together; the
  instance facts of `CLAUDE.local.md` (principal, language, git
  identities) thereby reach an isolated reviewer that needs none of
  them. The cost of CLAUDE.md is paid once per reviewer run, not once
  per session. The single-source-of-truth check of 2026-09-06 (history
  3.49) took CLAUDE.md from 636 to 584 lines by citation alone; what
  must be always-on is still this thread's question. First instance
  of the answer, 2026-09-14: the walkthrough paragraph became one
  sentence and a pointer to a skill, with a hook repeating the hard
  sentence at every prompt (POS.1170) — always-on is one sentence and
  a pointer, the detail a file read when its situation arises.
  The single-source-of-truth check of 2026-09-20 found seventeen
  restatements; nine were settled the same day (history 4.16) and
  eight low ones deferred until after THR.0390, whose condition fell
  when that thread closed on 2026-09-26 — they are on the table
  again, with no date set. They reach
  into the wording of CLAUDE.md and into the Commands table the
  README and `/man` derive from: state vocabularies enumerated in
  three places, the critic contract restating prime directive 8, the
  brief's rules restated in two state files, genre checklists beside
  their skeletons, index fields and ledger columns restated by
  `/ingest` and `/research`, the bundle index entry as a declared
  copy, sentences echoed inside CLAUDE.md and in skills, rosters
  written out by name. The report is not filed; a re-run of the check
  gives them again.
  2026-09-28: the elicitation per artefact (POS.1310) is the move of
  the rules of particular artefacts out of CLAUDE.md into their
  definitions. The brief's estimate is 43 to 53 lines fewer of 663
  in the always-on part, the state files growing by about as much;
  the line count is an effect, the proof is conduct (POS.1380).
- **THR.0250** Two suggested functions: an expander and an essence
  manager. A tip the principal received on 2026-09-03 — where from not
  recorded. The essence manager got its detail the same day: at the end
  of the chain a blind agent, without context, distils the essence of
  the final document by itself, and that essence is checked against the
  brief to see how far the whole intent drifted. The `essence` lens of
  the critic (POS.0410) is that mechanism applied to every adjacent pair
  of the chain; whether an end-to-end distillation is a further thing or
  the same lens run brief-to-last-layer is open. The expander has a name
  only. Parked until more detail arrives.
- **THR.0290** Research on the reviewer mechanism. What `/research`
  gains from kinds — the principal's idea of 2026-09-04 alongside the
  checks, which became POS.1140 — deferred on 2026-09-06 by his word:
  one command with one output today; taken up when a second way of
  researching appears. Opened 2026-09-04; the check half closed at
  3.44.
- **THR.0300** Everything a user makes for himself, kept at his own
  place and not in the forge's git. Not agents alone: agents, checks,
  critics, challengers, research, whatever a user writes for his own
  use, with no ambition of contributing it to the engine — the
  principal's word of 2026-09-26, widening his idea of 2026-09-04,
  which named reviewers, checks and other agents. One of the three
  separate tasks of that day (THR.0230, THR.0420), and the one that
  is a matter of today's forge and waits for nothing. Offered as
  possibly interesting, no priority. It would need a place the engine
  does not know and
  `forge-pull` never overwrites, on the pattern of `CLAUDE.local.md`
  and `settings.local.json` (gitignored), and the rosters of
  `/critique`, `/challenge` and `/check` would list what lies there
  beside the engine's own. Open: how a local agent takes the shared
  contract skill (POS.1120), what happens when the engine renames or
  reshapes it, and
  whether Claude Code's own user-level agents already serve. Opened
  2026-09-04. Merged on 2026-09-14 into the brief of THR.0230 as a
  third layer and taken back out on 2026-09-26 by the principal's
  correction, which also widened it from agents to everything a user
  writes for himself.
  2026-09-28, from `00-brief-elicitation.md`, material and nothing
  decided. The elicitation is to be user-definable like a check, and
  the boundary that says where to stop is mechanism versus instance.
  The engine owns the mechanism: the `/forge` dispatcher, the shape
  of a state file, the contract of a template, the shape of the
  conversation, the numbering of layers. An instance is one pair of
  files, state file plus template; a user-defined check is an
  instance of the check contract, a user-defined artefact an
  instance of the same kind. The engine never defines an instance,
  the user never changes the mechanism. The test: does CLAUDE.md
  have to change for it? If not, it is this thread's; if yes, it is
  a derivation (THR.0420). Order: the shape first (POS.1310), then
  the extension point. Open: where a user's definition lives so that
  `forge-pull` never overwrites it; a remark in the brief, for
  `engine-split`: if the mechanism is one, the dispatcher reads both
  roots, the engine's and the local one.
- **THR.0320** A harness lens. The principal's direction of
  2026-09-05: the critic roster gets a lens `harness` that reviews
  the operating layer — CLAUDE.md and the skills, commands and agents
  of `.claude/` — against current Claude Code conventions, and the
  knowledge comes from the official plugins (`plugin-dev`, whose
  `skill-reviewer` and `skill-development` carry the conventions for
  skills, commands and agents; `claude-md-management`, whose
  `claude-md-improver` reads CLAUDE.md), while the output is the
  classic critic's: a dated immutable report in `reviews/`, FND in
  the ledger, settled by walkthrough like every lens (POS.0400,
  POS.0410). The trial of the same day is the evidence that the
  shape fits a foreign agent (`reviews/2026-09-05-critique-harness.md`,
  FND.0190–0280, filed under THR.0290). Open: the mechanism by which
  `/critique harness` reaches the plugin — a mapping in `.claude/skills/critique/SKILL.md`
  from the lens to the plugin agent with the skeleton's Output section
  carried in the prompt, or an own `critic-harness` agent naming the
  critic contract and the plugin's skills alike in its front-matter
  (`skills:`, the field verified 2026-09-06, POS.1120); the plugin as an
  engine dependency — named by `/setup` and CLAUDE.md, and what the
  lens does when the plugin is absent; whether
  `claude-md-improver`'s rubric, written for codebases (build
  commands, architecture map), serves a constitution like the forge's
  CLAUDE.md beyond its conciseness criterion; the regression step of
  every lens, which the trial skipped. Relation: the first concrete
  kind of THR.0290, and the shape of the operating layer it reviews
  is POS.1120's and THR.0240's question. Opened 2026-09-05.

- **THR.0340** The README split from the documentation. The README is
  today the engine's whole documentation — 829 lines on 2026-09-08,
  longer than CLAUDE.md, sixteen chapters that are three things at
  once: an invitation (why, what you get, quickstart), a user's guide
  (the flow, roles, the chain, the reviewers, the commands) and a
  reference (conventions, setup, scripts). Decided in substance
  2026-09-08 at the principal's direction: the split must come — a
  short README that invites and points, the guide and the reference as
  renders of their own recipes into `docs/` (the mechanism exists: a
  recipe's `output:` path, POS.1070; the ledger's Renders table;
  `/release` re-rendering them). Decided order: after THR.0230, not
  before — the engine/framework boundary divides today's README
  between two repositories (setup, scripts, conventions, the reviewer
  mechanism and the mechanical commands to the engine; the chain, the
  lenses and personas, the requirement style and `/forge` to the
  forge), so a `docs/` cut made now would be cut again along that
  line. Open: whether the conventions chapter is rendered at all or
  the documentation points to CLAUDE.md, which is readable as it
  stands; the cost of more renders per `/release` (the README alone
  takes five to eight minutes today; the measurements are
  `research/2026-09-14-save-and-release-duration.md`). Trigger: the boundary drawn by
  the brief of THR.0230. Opened 2026-09-08. Also here, since it is
  the README's: the footer (`_Last updated_`) is kept for now and the
  principal will give further input (noted 2026-09-14 from the
  ledger).

- **THR.0350** Lessons of the first run in the field. The record of
  the forge applied to a private project of the principal's,
  10–13 September 2026, is registered as
  `sources/forge-run-record-health.md`: a timeline, eight failures,
  thirteen things that worked, thirteen engine gaps and sixteen
  proposals (P.01–P.16), item-numbered for citation. To be analysed
  properly and learned from — a walkthrough of the proposals, one at
  a time — when the principal has the time; deferred 2026-09-13 at
  his word, nothing decided. What he stated the same day, in his own
  words, to be worked from — his stance, not yet positions:
  - A brief that is born by joint elicitation carries Claude's part
    too: he speaks, sources are ingested as they arrive, and the two
    of them work the sources into the brief; the brief is then worked
    into the intent. That is the wanted model. The record's "brief =
    the principal's words only" (G.01) is not the model but a
    misreading of it; what broke the run was Claude saying "written"
    while nothing was written (F.01). Open: whether the brief marks
    what he said and what Claude said (Claude's recommendation of
    2026-09-13: yes, lightly, block by block, since the intent later
    asks whose word a position rests on; not decided). P.07 of the
    record (an intent draft beside a draft brief) is thereby set
    aside as the wrong fix.
  - The walkthrough is the failure he minds most: one item, worked
    until it is agreed, and only then the next; never a proposed
    resolution and the offer of the next item in one message. To be
    made to hold, not promised again.
  - The report of that project need not have been a new artefact:
    in the wanted model the brief is led by elicitation over the
    research and the ingested sources, worked into the intent, and
    the report is a render of it. How the later artefacts are handled
    is to be worked out as part of this thread.
  - To consider: a mechanism that puts a fresh sentence into the
    context at every prompt (the harness's hook that runs on each user
    message, `UserPromptSubmit`, adding context), so that the rules
    that matter — the one-item walkthrough above all — do not drift in
    a long conversation. Opened 2026-09-13.
  Priority given 2026-09-14: the first thread to be worked, before the
  briefs `brd` and `engine-split` (THR.0230) — that brief is to be
  born by the co-elicitation the record faulted (F.01, G.01, P.07, the
  marking of whose word is whose), so that technique must hold first.
  Walked through the same day, one proposal per message, directly
  into the intent (the record is the anchor; a brief of it would have
  been a copy):
  - P.01 accepted → POS.0190. P.02 accepted in the principal's own
    words as In pieces → POS.1160. P.03 accepted without the
    "no warnings" part → POS.0020. P.04 accepted as a trial, the
    hook and the `walkthrough` skill → POS.1170, POS.0850. P.05
    accepted → POS.1090 (Step by step). P.06 accepted with the
    principal's addition, the role always asked → POS.1040.
  - P.07 rejected → REJ.0180. P.08 accepted, origin on THR only →
    POS.0230, POS.1180; the marking of whose word is whose in a
    co-elicited brief decided yes, lightly → POS.0110. P.09 split:
    `terminal:` accepted → POS.0160; the layer opened as THR.0360.
    P.10 the pasted-text half accepted → POS.1040, the editing
    mechanism rejected → REJ.0200. P.11 accepted, unconditional →
    POS.1040. P.12 rejected for now → REJ.0190. P.13 deferred into
    THR.0360 with Claude's view of what a render is. P.14 covered by
    POS.1160 and POS.0190. P.15 accepted, the ledger cites → POS.0160;
    `/setup` asks the language first → POS.1050. P.16 not worked —
    too specific for now.
  - Of the principal's stance of 2026-09-13: the co-elicited brief
    is POS.0110; the walkthrough shape POS.0850 with a new depth rule
    from his correction; the report of `health` as a render is
    THR.0360's; the per-prompt hook is POS.1170.
  Still to do from this thread: the sweep of this project's ledger
  (POS.0160), and the observation of the hook in the next
  walkthroughs.
  2026-09-28: the model of the co-elicited brief stated here on
  2026-09-13 was turned. A brief holds the principal's choice from
  the finding, not the pile, and carries no mark of authorship
  (POS.0110, POS.1330).

- **THR.0360** A layer with an external audience. The first real run
  below the intent (project `health`,
  `sources/forge-run-record-health.md`, D.05, G.05) needed a report
  for a third party, not an assignment: a layer built ad hoc without
  a state file, a template or a recipe genre, every write a bundle
  across five documents. Whether it is a layer of its own (`report`),
  a generic `layer`, or a case of the BRD layer's mechanics, is worked
  in the brief `brd`, where the mechanics of layers below the intent
  are designed (POS.0700). Belongs here too (P.13, G.07) — Claude's
  view of 2026-09-14, not decided: the render is the Markdown; a
  `.docx` or `.pptx` is a conversion of a render or of an artefact,
  cheap and deterministic where it can be, with a row of its own,
  never blurred into "render"; a document the principal polishes in
  an editor is an artefact he composes, never a render, and the forge
  needs the way back — `doc2md`, a comparison, carry-over
  intent-first — because editing in an editor and having Claude
  absorb it is a way of working he finds comfortable. Of that view
  the conversions are decided since 2026-09-27 (POS.0590): a plain
  file made with the render, a designed file made by `/publish`
  with a ledger table of its own; the rest stays undecided. The `timeline`
  recipe genre waits for a second need (W.12). The brief `brd` is to
  be born (`/forge brief brd`) from the conversation over a
  colleague's fork of the engine — its files not transferred, its
  mechanisms walked through point by point — and from
  `research/2026-09-07-brd-layer-fork-analysis.md`; POS.0700 closes
  into positions of its own and CHL.0030 under DEC.0060 is revisited
  in that round (the principal's direction of 2026-09-07). Opened
  2026-09-14 from THR.0350; origin: the principal's word and the
  record.
  2026-09-28: the brief `brd` is the first instance of the
  definition shape (POS.1310, POS.1380), and the horizon returns in
  it: mandatory in the BRD, its shape in the intent and the
  assignment still to be solved (POS.1360).
- **THR.0370** Mermaid diagrams in Word. `scripts/md2docx.ps1`
  (POS.1150) converts a render to Word through pandoc and leaves
  Mermaid blocks as code. Agreed in the walkthrough of 2026-09-12 but
  not built: the route would be `mermaid-cli` rendering each block to
  PNG through headless Chrome before pandoc runs (a pandoc Lua
  filter), installed by the user one-off like markitdown and pandoc —
  never by the script, never `npx` fetching at run time, no online
  service. Open: whether to take the dependency at all, and global
  versus repository-local installation. The LLM route (a sibling of
  `md2pptx.ps1` on the `document-skills:docx` skill) was set aside on
  2026-09-12: it would end at a picture too, with less determinism.
  On 2026-09-27 the principal took that route for another purpose,
  the design of the document: it is the `claude` engine of
  `md2docx.ps1` behind `/publish` (POS.0590, POS.1150). Mermaid in
  the plain file stands as it was.
  Word to PDF is the recipient's, never the forge's (POS.1150).
  Deferred 2026-09-12 by the principal — "needs more thought"; opened
  as a thread 2026-09-14 from the ledger.
- **THR.0380** Executive pitch, loose ends. The five-slide deck
  (`recipes/executive-pitch.md` 0.4, `renders/executive-pitch.md` and
  `.pptx` of 2026-09-11) stays in `projects/forge` with the default
  deck template (decided 2026-09-10). Open from the render run: the
  S03 counts rest on the recipe's Template alone, no input carries
  them; and the headless build had no `document-skills:pptx` skill
  available and built the deck with python-pptx instead — to watch at
  the next build. Opened 2026-09-14 from the ledger.
- **THR.0400** A gate in front of the tools. On 2026-09-20 Claude
  read git state directly, past the scripts, twice, and on a bare yes
  to one change wrote its consequences as well — with the rules fully
  in context and the session in an automatic permission mode, so that
  nothing stopped it. The principal's three rules of that day: where
  the forge has a script, the script is used; a command of Claude's
  own, beyond plain reading, is explained and approved first;
  nothing is written, run or changed that was not agreed and
  approved. Done the same day, as the soft half: the per-prompt hook
  prints the three rules beside its two walkthrough lines
  (POS.1170). Open, the hard half: a `PreToolUse` hook,
  `scripts/hook-gate.ps1` in Claude's proposal, that reads each
  command and each write before it runs and answers deny (raw `git`,
  raw `pandoc` or `markitdown`, with the script to use instead),
  allow (plain reading; writes to the session's scratch and to
  memory) or ask (a state-changing forge script, any other command
  of Claude's own, a write into the repository). Known before it is
  built: telling reading from acting, and `git` as a command from
  the word in a string, is a heuristic, so what is unsure asks; the
  price is a dialog per write, an isolated render included; whether
  "ask" holds in an automatic permission mode, and whether the hook
  leaves the principal's own `!` commands alone, is to be tried, not
  assumed. Whether writes are gated file by file or left to the
  reminder is undecided. Deferred by the principal until the forge
  has been shown to the group (THR.0390): the script needs tuning
  and there is no time for it now; that condition fell when THR.0390
  closed on 2026-09-26, and nothing is scheduled in its place.
  Claude's reading of 2026-09-26,
  offered once: the "deny raw `git`" part of the hard half is done
  by the deny list of POS.1200, so what the gate still owes is
  `pandoc`, `markitdown` and the ask on writes.
  A silent refusal of a save, 2026-09-26, the first save since the
  deny list was added: `./scripts/forge-save.ps1 forge -m <message>`
  was refused by the permission layer with no dialog and no reason
  given, the script never starting. Six probes settled what did it. A
  one-line command carrying `git ` inside quotes runs; a two-line one
  runs; a here-string carrying the word runs; the message's exact
  sentence printed by `Write-Output` runs; the save whose here-string
  carried that sentence was refused; the same save with that one
  sentence reworded went through (commit 6cfd6f2). So no pattern
  matched a word. What was refused was the pair of a state-changing
  call and a text saying that raw git is denied to Claude — a
  judgement of content and intent, so the automatic permission mode's
  classifier and not the deny list; POS.1200 is not at fault.
  Research of the same day adds that no rule could have been more
  precise anyway: a rule cannot target a tool's primary content field,
  and `Bash(command:…)` is ignored with a startup warning. Two
  remedies were weighed and neither taken: `-MessageFile` on
  `forge-save.ps1`, so that no prose rides on the command line (the
  principal: a file is not a good solution); and dropping the prose
  statement of the ban to leave only the deny rule, his own proposal,
  against which stands that the trigger was the commit message and not
  the rule's prose, and for which stands that the ban is today written
  three times (the deny list, CLAUDE.md, the hook) — whether the
  classifier reads the hook's line as well is not verifiable from
  here. Left as it is on his word of 2026-09-26 and watched. What the
  incident adds to this thread's own case: the refusal explained
  nothing, where a gate of the forge's own would have named the rule
  and the script to use instead. The loop to expect: the forge's
  commit messages describe the forge's rules, git among them, so the
  pair will recur.
  The sweep of THR.0210 — names
  from `CLAUDE.local.md` searched in what is about to be saved — is
  a neighbour of this gate and stays that thread's. Opened
  2026-09-20 (Claude's proposal, the principal's rules).
- **THR.0410** The duration of `/save` and `/release`. Watched since
  2026-09-14, the measurements so far in
  `research/2026-09-14-save-and-release-duration.md` (POS.1100,
  POS.0810); the watch continues at the next releases, and what
  follows from the measurements is not decided. One observation of
  2026-09-20: a render of the README reads the whole intent and ran
  close to eight minutes. Opened 2026-09-20 from a line of the ledger
  that had stood without an ID since 4.10.
- **THR.0420** Derivations of the forge for other jobs. The forge as
  it stands serves the forging of a thought into an assignment; the
  principal wants versions of it that serve other work, and said on
  2026-09-26 that this is a task of its own, separate from the engine
  question (THR.0230) and from a user's own additions (THR.0300). One
  tool that does everything is explicitly not wanted: a derivation is
  reached by extending, rebuilding or forking the forge, and each
  stands as a framework in its own right. Three cases are named so
  far. The version for online product managers is the product
  framework: a screen described functionally per module, one artefact
  per module, HTML prototypes rendered from them — one and the same
  thing, by the principal's word of 2026-09-26. A version for test
  analysts, his word of the same day: their primary work is producing
  test cases and test strategies, and that is the work such a version
  would serve — the outline as far as it goes today. A
  project-management framework, his of 2026-09-03: inputs from the
  forge's assignments; later meeting inputs over which an agent runs
  unattended, sorting tasks and new requirements into artefacts —
  Markdown or otherwise — or handing them on through MCP;
  verification of an implementation against its assignment; a
  high-level idea. The two outlined ones were held in THR.0230 until
  the tasks parted; that thread's boundary analysis rests on their
  outlines, which is why they are described here in full. A derivation needs no engine — a fork
  carries the whole forge and is cut down — so the connection to
  THR.0230 is one-way and conditional: if the forge is split, the
  derivations can live on the engine instead of each carrying a copy
  of the mechanics. Whether each derivation gets a brief of its own,
  and which is taken first, is undecided; nothing is scheduled.
  Opened 2026-09-26 from THR.0230 at the principal's direction.
  2026-09-28: the line against THR.0300 is drawn there (mechanism
  versus instance, the test on CLAUDE.md). Without it a user's local
  additions grow into a derivation, and the one tool that does
  everything comes in through the door for user artefacts.
- **THR.0430** A command that ends a session. It verifies that
  nothing lives only in the conversation — an unwritten round, a
  repository with changes (`forge-status`), a stale render — and
  says what a shutdown would lose; then it records in the ledger the
  time spent and the tokens burnt in the session. Claude cannot
  measure either from inside the conversation; the harness can:
  `/cost` reports the session, and the transcripts under
  `~/.claude/projects/` carry usage and timestamps per message, so a
  script can sum them per project by working directory, for past
  sessions too — a lower bound where a project was worked on more
  than one machine. Open: the name of the command, the ledger's
  shape for the figures (a table, or a line in the header), whether
  the sum is per session or cumulative, and the research of the
  transcript format before any script. Opened 2026-09-27 at the
  principal's direction.
- **THR.0440** What the brief `elicitation` and its second review
  left open. Origin: the brief and
  `sources/forge-elicitation-brief-review-v0.4.md`; the
  recommendations are Claude's, offered once. (a) Whether the
  brief's Map names the boundaries, what is not wanted and what is
  out of scope; Claude: yes, as a fifth area, since the Partner
  already asks what he does not want. (b) Whether the Course of a
  brief offers the lock as soon as the talk turns to the intent's
  work; Claude: yes, once, as a recommendation and never a gate.
  (c) Whether a brief born in the forge carries marks and citations
  at all; Claude: a source is cited where its identity supports,
  limits or contradicts the thought, and mere inspiration stays
  discoverable through the research note. (d) `(remark: …)` covers
  three states that behave differently; Claude: keep it for a
  reservation or an uncertainty that must stay visible, an
  unadopted suggestion being normally gone. (e) "Every idea is
  weighed twice" in the intent's Aim; Claude: each material idea
  judged for its value and for feasibility wherever either
  distinction matters. (f) A Map is defined as what must be found,
  while "the words" of the assignment's Map is something verified;
  Claude: "found or consciously verified", the area renamed
  self-containment. (g) The number of questions up front as the
  sign that the intent is not ready; Claude: the boundary is
  unresolved substance against handover detail, a large number is
  evidence of it and not its definition. (h) Whether an alternative
  the principal did not take may stay visible in a brief; Claude:
  no rule needed, what goes in is his to say, a note included.
  A matter closed here changes the wording of its definition
  (POS.1330 to POS.1350). Opened 2026-09-28.
- **THR.0450** What the researches of 2026-09-28 propose beyond the
  brief. Origin: Claude's synthesis from
  `research/2026-09-28-artefact-layers-from-idea-to-handover.md`
  and
  `research/2026-09-28-human-ai-elicitation-over-artefacts.md`;
  nothing decided. (a) The order of initiative. Four controlled
  studies agree that the further an AI goes into the drafting, the
  better the text and the weaker the human's ownership of it, and
  that a model used from the start narrows the ideas; their limit is
  short tasks with lay participants, none a domain expert on a
  document of his own. Against them stand two things the principal
  wants: the active opening of POS.1330 and an early draft in its
  extreme form, a whole proposal as the first answer (POS.0880).
  The question is whether both stand as written. Claude: they
  stand, with the principal's own statement of the thought first
  wherever it does not arrive written, and Claude's proposal
  offered rough and named as a proposal. (b) A state said per area
  when a Map is walked, so that "considered and left open" differs
  from "not looked at"; Claude: said aloud at the walk, nothing
  written, since a recorded state is a new convention and hardens
  into a gate. (c) The assignment's completion stated as doctrine
  states it, the recipients acting rightly when the plan no longer
  fits, and one sentence admitting that a live briefing beside the
  document is normal. (d) One sentence in the outward-facing
  renders on what a brief is here: elsewhere the word names a short
  direction written for someone else. (e) For the brief `brd`: a
  future possibility is never used to justify the present proposal.
  (f) Three choices of the forge have no outside model and are
  hypotheses to be tried: a locked brief in the owner's words as
  provenance, the horizon divided among the layers (POS.1360), and
  "polished too far" as a defect of a brief (POS.0110). Opened
  2026-09-28.
- **THR.0460** `/recipe` and `/forge`: one dispatcher or two.
  Today the states of `/forge` and the genres of `/recipe` are one
  mechanism written twice in different shapes. A recipe is composed
  and not found (POS.1300), so the seven blocks are not its shape;
  whether `/recipe` becomes `/forge recipe <genre> [name]` is a
  question of mechanism, left open as a small matter. A remark in
  the brief: one mechanism would unify the language question and
  "composed from the skeleton"; against it stands that `/forge` is
  the door of the chain. Opened 2026-09-28 from
  `00-brief-elicitation.md`.
- **THR.0470** The intent is too long to be read. At 4.32 the forge
  intent has 2 997 lines, and the principal finds it so talkative
  that a human cannot read it: an intent is to be structured
  decisions and the understanding of the aim. His word of
  2026-09-28, to be worked from and nothing decided: the stories,
  the reasons told with them and the measurements belong in the
  history, exactly there, and the history is to be worked with
  more; whether threads belong in the intent at all; whether it was
  a mistake to make no assignment for the forge; whether the intent
  may refer to a file that holds the detail, the wording of the
  elicitation definitions for one, meant generally; whether large
  files are split into smaller ones with a master index saying what
  is where, for artefacts in general. Agreed in principle, his word
  of the same day: detail lives in the intent until the file that
  performs it exists and has been seen to hold, and then the intent
  keeps the stance, the reason and a pointer. Open beside it:
  whether a position keeps its reason in one sentence (POS.0120)
  once the story has gone to the history. Claude's count and
  estimate of the same day, the estimate unverified: the threads
  are 711 lines; the stories, the measurements and the closed
  matters inside threads about 510; operating detail about 320; the
  three definitions in full 318 (POS.1330 to POS.1350); two groups,
  Open threads and Operating environment, carry more than half of
  the surplus. Claude's recommendations, offered once: the stories
  are struck first, each checked against its history row before it
  goes; threads move into a companion of the intent on the pattern
  of the history companion, one version with the intent, the ledger
  keeping its line per thread; no assignment for the forge, since
  it would be a third copy beside the intent and the operating
  layer, the hole being that precise wording has no home before it
  is built; a position refers to a file of a kind that exists (a
  script's header, a skill, a template, a research note, a locked
  brief) and no new kind of document is added; splitting comes last
  and for the intent alone. Opened 2026-09-28.

Note: the ID THR.0120 was inadvertently used twice — first for the
readme-recipe thread (opened 1.14, closed 1.16), then for the
assignment-apparatus boundary (opened 1.24, closed 2.4). Citations of
THR.0120 from POS.0210 and version 2.4 refer to the latter. Recorded
as-is; IDs are never renumbered. Likewise POS.0005 and REJ.0125,
outside the numbering in tens, and the group Working methods starting
at POS.0850 rather than at a hundred, stand as they are by DEC.0110
and DEC.0130.

## Rejected directions

- **REJ.0010** `clarifications.md` as an append-only Q&A log. Rejected
  because it left the current state of intent scattered across brief, log
  and assignment, with no single place answering "what do I want now".
  Replaced by `10-intent.md`.
- **REJ.0020** Workstreams as first-class entities with their own IDs and
  lifecycle. Rejected as structure for its own sake; plain heading groups
  plus stable global IDs achieve the same at lower cost.
- **REJ.0030** Hard quality gates blocking approval. Rejected: these are
  assignments for people, and the principal decides what ships.
- **REJ.0040** A templated brief with chapters (goal, high-level idea,
  and so on). Rejected; see POS.0110.
- **REJ.0050** Priority tags on items (`critical`, `important`,
  `nice-to-have`). Originally wanted as an optional attribute, dropped in
  favour of the group BRD convention: everything is essential, exceptions
  are noted as *optional*.
- **REJ.0060** Separate templates per genre of assignment. Rejected in
  favour of one universal skeleton with optional sections, so that
  everything arriving from the principal has a consistent shape.
- **REJ.0070** A dedicated feedback channel for comments coming back from
  the recipients. Rejected; see POS.0170.
- **REJ.0080** Merging document review and substantive challenge into one
  reviewer. Rejected: an agent doing both does neither properly, and the
  formal audit benefits from a clean context while the substantive
  challenge benefits from a different register entirely.
- **REJ.0090** Composite naming such as `BA-FLOW` for the BA initiative.
  Rejected because it destroys the word; `FLOW:BA` keeps both the
  programme and the instance legible.
- **REJ.0100** Single-letter and hyphenated ID prefixes (`R-001`,
  `P-01`). Replaced by three-letter dotted `PREFIX.NNNN` aligned with the
  group BRD standard.
- **REJ.0110** MAJOR.MINOR versioning with MAJOR meaning a scope change.
  Replaced by the group convention where integers denote approval; a
  scope change is a reason for re-approval anyway.
- **REJ.0120** "Mandate" and "charter" as the name of the handover
  document. Mandate rejected outright by the principal; charter carries
  project-management ceremony and implies a project, which many
  assignments are not. "Assignment" retained.
- **REJ.0125** The founding framing "a CTO's tool for briefing his direct
  reports (heads)" as the system's identity. Dropped by the principal on
  2026-07-31: it describes the first instance, not the engine.
  Superseded by the general-engine framing (POS.0005).
- **REJ.0130** "Cascade" as the system name: literally names the
  waterfall. "Foundry" rejected for collisions (Azure AI Foundry,
  Palantir Foundry). "Continuum", "Strata", "Idea Forge" and Czech
  "Kovárna" considered; **Forge of Thought** chosen.
- **REJ.0140** `local/` as the home of user-local files (POS.0750,
  adopted 2.1). Dropped on 2026-08-29: it existed only to keep company
  material out of the repository, which the gitignored `projects/*` now
  does; deck templates live in a library project (POS.0970) and are
  named by path (POS.0740).
- **REJ.0150** Shapes of the engine/projects relation rejected on
  2026-08-29 (research `2026-08-29-git-engine-projects-separation.md`,
  `2026-08-29-framework-distribution-in-the-field.md`): git submodules,
  subtree and worktrees — they model a dependency, which this relation
  is not; the engine as a template repository and copying the engine
  into projects — every comparable project that does so ends in
  manifests, override layers and migrations; a plugin as the only shape
  now (THR.0190).
- **REJ.0160** Stale-only rendering at the save (option A of THR.0220):
  one command as today, `/save` regenerating only a render whose recipe
  or input moved in that save, a `stale (skipped <date>)` mark in the
  ledger for a render skipped on the principal's word. Rejected
  2026-09-05: it saves perhaps a third of the engine's saves and
  nothing on projects, whose README input — the ledger — moves at every
  operation, and it adds a staleness state that `/save`, `/forge` and
  `/check` must all read alike; the two-command shape of POS.1100 saves
  everything and adds nothing.
- **REJ.0170** A fixed working branch with a forge switch that merges
  (option C of THR.0220): a `work` branch per repository, one script
  creating and switching it, `/release` merging it into `main`.
  Rejected 2026-09-05 as the first step towards the wrapper of git the
  principal does not want — merge and conflict logic in the forge's
  hands, two branches a non-developer must understand — while forcing a
  branch on those who do not need one. The switching half survives as
  the voluntary `forge-branch` of POS.1110; the merging half stays
  git's.
- **REJ.0180** A second home for what the finding of a brief yields
  and the brief does not take: an intent 0.1 as a draft beside a
  draft brief, a "notes" record kind (P.07 of
  `sources/forge-run-record-health.md`), or a new artefact before
  the brief. Rejected 2026-09-14 and again 2026-09-28, with the
  reason changed. Then the brief itself was the home, since it held
  the whole pile; now the brief holds the principal's choice
  (POS.0110), and what he does not take needs no home: a finding or
  a source has `research/` and `sources/`, and what merely fell by
  in the conversation is gone with it.
- **REJ.0190** A "parked" document kind without a mining state, for
  matter set aside from a layer (P.12, G.06). Rejected for now,
  2026-09-14: parked matter lives as a THR of the intent or under a
  Parked heading of the artefact it came from; moving it into a brief
  was the error, not a missing kind.
- **REJ.0200** An edit mechanism for large artefacts so that
  temporary scripts disappear (the second half of P.10, G.04).
  Rejected 2026-09-14: the temporary scripts were Claude's choice, not
  a gap of the engine — the harness's exact-replacement edit tool
  exists and is the rule (no shell for reading or editing project
  files, the principal's word of 2026-09-14).
- **REJ.0210** A recorded fate for every part of a brief at mining.
  Written into the draft of `00-brief-elicitation.md` and dropped
  before its lock, 2026-09-28, as complexity without need: mining
  would turn into bookkeeping. The intent's Map looks at each brief
  as a whole instead (POS.1340).
- **REJ.0220** Marks of authorship in a brief: *(Claude)* in italics
  before every block that is not the principal's own, the rule of
  2026-09-14. Dropped 2026-09-28: what is in the brief the principal
  approved, whoever first said it, and a mark that names a model
  reads differently on every model the forge runs on. What carried
  something other than authorship stays as `(source: <path>)` and
  `(remark: …)` (POS.0110).

## Candidate structure for assignment

Not applicable: this project's handover artefacts are the core itself
(`CLAUDE.md`, `templates/`, `.claude/`) and `README.md`. A
`20-assignment.md` would duplicate them for an audience that does not
exist; see the ledger.
