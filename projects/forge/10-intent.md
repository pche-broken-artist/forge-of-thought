---
version: 4.64
date: 2026-10-09
status: draft
last_change: 4.64 (2026-10-09): what a README carries has one owner, the readme skeleton (POS.1450; FND.1130).
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
including integration. **The chain ends where the project needs it
to:** below the intent a project takes the layers it needs, and many
end at the intent. Every design decision below is made with that
growth in mind, which is why files and IDs are numbered with gaps and
why the name says thought, not assignment.

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
  presented as facts); the record's "no warnings unless asked"
  rejected by the principal — he wants to be told of problems, holes
  and contradictions, as a question.
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
  (`00-brief*.md`), kept in whatever language they are written
  in; a render may be in any language its recipe declares, a
  translation being a render. The boundary narrowed to the artefacts
  2026-09-10. The working-conversation language is
  per-instance configuration, not a system rule: it is set in
  `CLAUDE.local.md` (POS.0950) and read from there by every command —
  never written into the operating layer, and never presented
  outward. The README and other outward-facing renders state only the
  output-language rule.
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
  requirement sets, open threads, TBC items before a handover, proposals
  of a source — is worked one item at a time, in order of weight. Every
  item ends in one proposition, worded so that `accept` has exactly one
  meaning — yes to what is in front of the principal, also where the
  proposition goes against the reviewer's suggestion — and the message
  closes with the verdict line `(a)ccept / (m)odify / (r)eject /
  (p)ark`. The verdict words are one set for every walkthrough, whatever
  produced the list: `accept`, `modify` (a discussion opens and the
  solution found is put forward to be accepted), `reject`, `park` and
  `obsolete`; the producing command says only what `accept` writes. The
  principal may answer the line with a single letter when that letter is
  his whole message; no other word of the forge has a letter, so that
  nothing which writes or saves can be set off by a slip. Decided
  2026-09-27. Verdicts are carried in the conversation and written once
  at the round's end (POS.0190). Whatever produces a list ends by
  offering a walkthrough — `/critique`, `/challenge`, the `/forge` map,
  a comparison made on request — and the principal may call for one at
  any moment.
- **POS.0860 Propose, never decide.** Claude criticises, challenges,
  inspires and lays out options; the principal composes (POS.0010,
  POS.0070). Nothing enters content because Claude proposed it.
  The sign `??`, alone at the end of the principal's message or as
  his whole message, asks for Claude's honest opinion of what he has
  just written: three points at most, marked as Claude's own,
  nothing written or filed. It is not the isolated challenger, who
  does not know the conversation, and it adds to Claude's duty to
  say at once what does not fit (POS.0020), never replaces it.
  Decided 2026-09-27; one sentence
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
  intent and propagates from there down the whole chain the project
  has: the assignment, the BRD, the solution design are each brought
  to it. Only wording is fixed downstream directly. The change may
  come from below: when solving shows that what is wanted cannot be
  had, or must be wanted differently, the intent changes first and
  the layers follow (POS.0140).
- **POS.0910 Recommend, do not push.** Every option Claude lays out
  comes with its recommendation and reason, stated once; a declined
  recommendation is not re-argued unless new facts appear.
- **POS.1470 Plain speech.** Every message to the principal opens with
  the outcome in plain sentences, what was done, what was not, what is
  proposed; detail follows only where needed, and the message ends with
  one simple question, never a compound one. A thread, a position or a
  decision is named to him by what it is, in words; its ID follows in
  brackets as an address, never alone. A map names the few live matters
  in words and gives the rest as a count. No metaphor and no invented
  word stands for a mechanism of the forge: the thing is said in a plain
  clause. Reason: the principal reads the first lines and expects the
  point there; he carries no IDs in his head, and a word Claude made up
  explains nothing (2026-09-05, 2026-09-29). Decided 2026-10-09, brought
  from the assistant's memory into the forge.
- **POS.1480 A rule says the kind, never the count.** A rule Claude
  proposes says what kind of content belongs and what does not; it never
  sets a count, a length or an always/never harder than the principal's
  own words. When a rule has failed to hold, the answer is not a
  stricter number but the question what kind of content slipped through.
  Reason: a numeric limit is easy to check and so Claude reaches for it,
  but it cuts meaning where the matter needs more words and answers a
  problem of kind with a rule of amount; the principal named "reason in
  one sentence" as Claude's typical extreme (2026-09-29), and the same
  swing before it (the brief `elicitation` 0.4). The division by kind,
  never amount, already governs what an intent, a brief and an
  assignment hold. Decided 2026-10-09, brought from the assistant's
  memory into the forge.
- **POS.1460 Step by step.** Any action needing the principal's consent,
  a write, a commit, a push, a rename, anything hard to reverse, arrives
  as one step with the exact operation, its target and the reason
  stated, and runs on his word; a plan he has seen is not consent for
  its steps, and a batch of sensitive operations is never run as one.
  The birth of a new versioned document is such a step (POS.1090).
  Reason: consent is given to a concrete operation, never to its
  description, because a step hard to reverse must be seen by the
  principal at the moment it happens, not in a plan read earlier. A yes
  is a yes and nothing else is: a remark, a question or a counter-thought
  in answer to "shall I change it?" is input for a revised proposal
  shown again, never a licence to edit, in handed-over work as in joint
  work; on 2026-10-03 a remark that opened a larger question was taken
  as a go-ahead and the core file was edited six times before the
  principal stopped it, and handing over covers making the proposal,
  never changing it while he judges it. The
  method stood in CLAUDE.md, Working methods, since 2026-09-05 without a
  position of its own; given one 2026-10-09 when the documentation
  writers found no reason to give for it.
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
- **POS.1170 A rule that must hold in a long conversation is repeated at
  every prompt by a hook, not trusted to CLAUDE.md alone.** The run
  record of `health` showed the one-item walkthrough breaking about
  thirteen times with the rule fully in context and a memory note beside
  it (F.02): text loaded once dissolves as the conversation grows. What
  is repeated is the one-item rule itself, with the verdict line that
  closes a proposition (POS.0850) and a pointer to the full shape, and
  three lines of conduct, the principal's rules. That is also the first
  instance of the pattern THR.0240 asks for: always-on is one sentence
  and a pointer, the detail is a file read when its situation arises. A
  hook is context, not enforcement — the nearest thing to a wall the
  harness offers. A trial, judged by behaviour (P.04).
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

### Elicitation
- **POS.1300 What elicitation is.** Elicitation is the process by
  which the principal and Claude find an artefact together and form
  the knowledge it holds. It is not any conversation of theirs, and
  in its meaning it is not a conversation at all: the conversation
  is the medium, the interview (POS.0870) is one instrument,
  research and sources are others. Three things are kept apart: the
  map (what must be found for the artefact to be complete), the
  process (how the map is walked) and the template (where the result
  lands); the map stands before the template, because a template can
  be filled and still miss what the artefact is for: the map says what
  has to be found, the template only where it lands (reason given
  2026-10-09). Elicitation differs by
  artefact: the talk over a brief, over an intent and over a BRD are
  three different talks, and every artefact type has a definition of
  its own (POS.1310). Not elicitation: composing a recipe, which is
  configuration from known options and not the finding of knowledge;
  `/setup`; the walkthrough of a reviewer's findings, which has its
  shape already and nothing per artefact in it. Decided
  2026-09-28 from `00-brief-elicitation.md`.
- **POS.1310 The shape of a definition.** The elicitation of one
  artefact type is defined in seven blocks, in reading order: **Target**
  (the artefact's file and its template), **Inputs** (what the finding
  starts from), **Aim** (what the elicitation achieves and when the
  artefact is complete: the one place where completion is stated),
  **Partner** (Claude's stance: what he does, what he does not do, who
  steers the finding and who the decisions), **Map** (what must be
  found, POS.1320), **Instruments** (only the mechanisms of the forge
  this artefact uses in a way of its own, cited and never described) and
  **Course** (the ways in, the order, and what is offered when the Aim's
  completion is reached; it states no completion of its own). Every
  definition carries all seven, so that the shape can be checked; a
  block empty on purpose says so with the reason and is never silently
  left out. Aim and Partner do not repeat each other: Aim says what is
  true of the artefact at the end, Partner what Claude does beyond that,
  citing the Aim. Outside the definition, as shared mechanism cited and
  never repeated (POS.1070): the form of the conversation (POS.0850),
  one write per round (POS.0190), versioning with history and ledger
  (POS.0310), creation from the template, the language question
  (POS.0060), ending by naming the state. The definition is the one
  `/forge` works by (POS.0580) and stands beside the artefact's template
  as a pair: how we get there, and what is to come out. The genre files
  of `/recipe` (POS.0770) map onto the shape without loss, Genre and
  Skeleton to Target, Role to Partner, the elicitation checklist to Map;
  the seven blocks themselves are for the artefacts of the chain. The
  rules of particular artefacts live in the definitions: what a brief
  carries in the brief's, what the intent and its threads hold in the
  intent's, completeness and the Requirement style in the assignment's.
  CLAUDE.md keeps of each artefact what it is, how it joins the chain,
  and a pointer. The definitions of the four artefacts of today's chain
  are the state files `brief.md`, `intent.md`, `assignment.md` and
  `solution-design.md`; POS.1330, POS.1340 and POS.1350, and for the
  solution design POS.1400 with POS.1420, say what each is to achieve
  and why. Present shape 2026-10-02, from `00-brief-elicitation.md`.
- **POS.1320 A Map is a map of what must be found, not a
  questionnaire.** It names, in the artefact's own vocabulary, what
  the finding looks at or consciously verifies; it prescribes neither
  the headings of the
  document nor the order of the conversation, and it is neither a
  list of questions nor a list of criteria. It is walked at the
  moments its definition names, as the question whether each area
  has been consciously considered; an area may stay empty when it
  was considered and found not to apply. At the walk Claude says of
  each area how it stands: found, considered and left open,
  considered and found not to apply, or not looked at. It is said
  aloud and nothing is recorded. How an area is found is the
  situation's: a question, a research step, a source. Present shape
  2026-10-02, from `00-brief-elicitation.md`.
- **POS.1330 The definition of the brief's elicitation.** What it is to
  achieve: a brief as POS.0110 has it. Claude is active at the opening
  and forms the record when the principal says to write, and never
  decides what goes in. Present shape 2026-10-03, from
  `00-brief-elicitation.md`.
- **POS.1340 The definition of the intent's elicitation.** What it is to
  achieve: an intent that chisels the briefs into what the principal
  holds, positions, facts, threads and rejections with their reasons,
  placed on a horizon where he sees one; coherent, nothing twice, every
  position with its provenance (POS.0120), passed through a reality
  check before a lower layer is derived; complete for now when no thread
  blocks the next layer, never finished. Claude composes the wording and
  challenges, the principal the substance; a thread closes only on his
  word. The recipients, the objective and the success criteria are found
  here as soon as he sees them, in the section "Candidate structure for
  the layer below", so that the layer takes them over instead of
  finding them first. No fate is recorded part by part at mining
  (REJ.0210). Present shape 2026-10-09, from `00-brief-elicitation.md`.
- **POS.1350 The definition of the assignment's elicitation.** What it
  is to achieve: an assignment as POS.0130 has it, such that the
  recipients can act without the principal in the room and know the end
  and the reason well enough to act rightly where the plan no longer
  fits. It is found in a joint pass of three phases and no new kind of
  interview: questions up front only for what the intent does not
  answer, a recast of the whole with a provenance map, a walkthrough by
  group. Why not item by item: most items are craft derived from the
  intent and a verdict on each is ceremony. Why not "read the whole":
  without the map one sees what is there, not what is missing. The
  wording is Claude's, the substance the principal's (POS.0140). Present
  shape 2026-10-03, from `00-brief-elicitation.md`.
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
  when the BRD gets its definition in the brief `brd` (THR.0360). The
  division is the forge's own and is tried, not assumed. Decided
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
- **POS.1380 The order of the work.** The
  elicitation comes first; then the brief `brd`, the first instance
  of the shape of POS.1310; then the brief `engine-split`
  (THR.0230). The elicitation can be solved in today's engine
  without deciding the split, and self-contained definitions are the
  prerequisite of a later split, never the other way round: once the
  definitions stand on their own, the split is a decision about
  roots and installation, a move of files. The definitions are not
  tried before they are used: they live in the state files of
  `/forge`, are used on real work at once and mended there as the
  work shows. Reason: whatever goes wrong is restored from git, and
  a trial would mean changing every definition twice, in the intent
  and in its file, and moving it over afterwards. A change of what a
  definition is to achieve goes through the intent first. What in
  CLAUDE.md contradicted the definitions was brought current with
  them, and the other rules of particular artefacts left CLAUDE.md
  for the definitions after the `single-source-of-truth` check
  (POS.1140). Locked artefacts are untouched by the change. Present
  shape 2026-10-03, from `00-brief-elicitation.md` and the
  principal's word.
- **POS.1410** How an artefact is composed is the principal's
  choice, made artefact by artefact: he finds it with Claude by
  elicitation, or he hands it over with a few sentences of what he
  wants, and Claude composes the whole and returns it for his
  judgement. Authorship is his either way: the author is the one who
  sends a thing into the world and answers for it, and Claude is a
  tool. Found together, the rule holds as it stands: where Claude is
  unsure he asks and fills no gap by assumption. Handed over, Claude
  works the definition alone: its Map says what must be found, he
  finds it from what he was given, from research and from the
  sources, and he says what he assumed and what he chose, with what
  it was chosen against, so that the principal judges decisions and
  not prose: in what he returns as a short list of what the principal
  might have decided otherwise, and in the artefact in plain words at
  the place each stands (POS.1370), until the principal has judged
  it. Work handed over keeps the bounds he sets and comes back as a
  proposal: nothing is derived from it and nothing is done on it
  before he has judged it. What a test can tell of work handed over
  is told by a test and not by his reading; his judgement is for what
  no test can tell. Every definition is written so that it can be
  worked either way. Reason: his attention is the scarce thing, and
  whether a matter deserves it is his to say, not the forge's.
  Decided 2026-10-03.

### Document chain
- **POS.0100** Files in the chain are numbered in tens (`00-brief.md`,
  `10-intent.md`, `20-assignment.md`) so later layers — a BRD
  (`30-brd.md`), a solution design — can be added without renaming
  anything that exists.
- **POS.0110** A brief is the principal's text of one whole of thinking:
  what he wants and why, with what he chose to take from the finding
  around it. It is free-form: any structure the principal finds useful
  (prose, headings, tables, use cases), no required content and no IDs;
  only a minimal YAML header. It holds thoughts to be processed, not
  decisions: they may be changed, reworked or dropped when mined, and
  only the intent turns them into positions. No structure is *required*,
  because a required one would force premature tidiness, and none is
  forbidden; a summary the principal orders into a brief is stored as
  shown, never re-narrated. A brief is rough on purpose, neither perfect
  nor detailed: the chiselling is the intent's, and a brief polished
  until the intent has nothing left to do has gone too far. Its usual
  shape is light: the topics of the whole, each with a few sentences of
  what the principal wants of it, the research that verifies or limits
  it cited beside it, and what is still open. It is composed in a round
  or two and then mined. It is where thoughts are thrown in before they
  are sifted: not all of them survive, and the sifting is the intent's.
  It is not the record of the finding. The finding is wide (research,
  sources, the principal's ideas and Claude's) and gathers as many ideas
  as it can; what goes into the brief and what stays out is the
  principal's decision, made on what was found. What stays out lives in
  `research/` and `sources/` where it is a finding or a source, and
  otherwise nowhere (REJ.0180). Nothing in a brief marks authorship:
  what is in it the principal approved, whoever first said it
  (REJ.0220). Two marks stay, because they carry something other than
  authorship: `(source: <path>)` stands where the identity of a source
  supports, limits or contradicts the thought, and becomes a fact with
  provenance at mining; what merely inspired the thought carries no mark
  and stays discoverable through the research note; a short `(remark:
  …)` stands where a reservation or an uncertainty must stay visible,
  named by what it is and not by who made it, so that it reads the same
  whatever model the forge runs on; a suggestion or an alternative the
  principal did not take is gone, unless he says it stays. A brief is
  versioned like every artefact (POS.0300): a draft until the principal
  approves it, 1.0, and changed after that as any artefact is. It is not
  locked and not immutable: what it said at any version stands in its
  history and in git. Three origins are equally legitimate and the forge
  does not distinguish them: the brief arrives finished from outside and
  is stored as it came; it is begun outside and finished with Claude in
  the forge; or it is born in the forge from the first word. `/forge
  brief [name]` is the door for the latter two, and how a brief is found
  there is POS.1330. A brief is the provenance of its whole: a position
  mined from it cites it with its version, and drift is measured against
  that version. Present shape 2026-10-03, from `00-brief-elicitation.md`
  and the principal's word.
- **POS.0920** A project may have more than one brief, and the ledger
  tracks how far each is mined. The founding brief is `00-brief.md`;
  every later whole of thinking that would otherwise land in the intent
  as a batch of unproven positions is born as `00-brief-<name>.md` —
  same header, same states, same rules. A brief is mined into the single
  intent when the principal says so, approved or not: positions cite the
  brief and its version as provenance; a whole that dies on the way
  leaves the brief as it stands and one REJ in the intent with the
  reason, so the trace survives either way. The ledger's Briefs table
  carries one row per brief; "how much" is a judgement recorded in its
  note and in the provenance of the positions, never a metric.
  Rationale: a big new whole needs a place where the thought can be
  tempered before it enters the trunk — like a git branch — without a
  new document kind; THR was wrong for it (a thread is a question, not a
  body of work), and a working space with positions before the merge (a
  branch document) was judged heavy for now (THR.0170).
- **POS.0120** `10-intent.md` is the working document: the consolidated
  *current* state of the principal's intent. Not an append-only log; it
  is rewritten for coherence each round, with changes recorded in its
  history. It exists because chat context dies and anything of value
  must live in a file: it is the document to read when returning to a
  project after weeks, instead of excavating old conversations. A
  position says what the principal holds and why it holds, in as many
  words as it takes to be understood without loss of meaning, and names
  what it comes from, a brief or a source; it is dated once. What does
  not belong in it is the way to it: why it was changed, what was said
  on the way, trials, measurements, counts, findings settled, what
  others do, which research turned it. All of that is written into the
  history in the same step that writes the position, while the whole
  context is at hand; a record of the history may carry what was said
  and how the change was reached. Dated once means one date, the day the
  position took its present shape; earlier steps are found by searching
  the history for the position's ID, and a position cites no record of
  the history. A number stays only where it is the rule or a threshold,
  never as a measurement. Text leaves a position only into the history,
  word for word (POS.0310). An item says what is to be achieved and why.
  What realises it, a file among it, is named in the solution design
  where the project has one (POS.1420), and the realisation is the
  file's. Where a project has no solution design, the item names the
  file, and where the output is only part of a file, a section of
  CLAUDE.md among them, or the file does not exist yet, it keeps the
  full information, since another change may rewrite that part and the
  detail would be lost. Where the item and what realises it say
  different things, that is a finding, never mended in silence. The
  threads live in a file of their own beside the intent, `threads.md`,
  one for the project: the intent says what holds, the threads what is
  being worked. Every thread names, right after its ID and in square
  brackets, the artefact it concerns, as `/forge` names it; several
  where it concerns several. A thread says what is open and where it
  came from, and carries the working debate for as long as it is
  unsettled: what was said, what was tried, the plan of a change under
  way, the proposals that await a decision. It is where an unfinished
  conversation is saved. A settled thread leaves the file and is kept
  whole: what holds goes into the intent, and the record of its closing
  in the intent's history carries the thread's last wording word for
  word in `Was`. The file is part of the intent as the history is,
  freely rewritten, with no version and no history of its own and no row
  in the ledger; the intent's history records the birth and the closing
  of a thread, not every saving of its debate. Present shape 2026-09-29.
- **POS.0130** `20-assignment.md` is the distilled handover document for
  the recipients: complete, precise, structured, self-contained,
  versioned. It carries the whole in-scope substance of the intent —
  nothing is left out for the sake of brevity, and a silent omission is
  a defect; leaving a matter out is legitimate only as an explicit
  delegation (a DEL or TBC item). There is no size target in either
  direction: length is whatever fidelity requires, and the defect is
  excess of the wrong kind (solving instead of assigning), never length
  as such (the size targets dropped 2026-08-15: the goal is to have it
  right, not short). The name "assignment" was kept deliberately; it
  does not preclude further layers below it.
- **POS.0140** Substance changes go intent-first and then propagate to
  the assignment; wording-only fixes may edit the assignment directly. If
  the principal dictates substance straight into the assignment, the
  corresponding intent update is proposed in the same step.
- **POS.0150** Drafting early is a legitimate elicitation tool, not a
  violation of sequence. Concrete text sharpens critique.
- **POS.0160** Supporting documents (the kinds: POS.1080):
  `decisions.md` (append-only, DEC), `ledger.md` (single source of truth
  for state, freely rewritten), `reviews/`, `challenges/`, `research/`
  (all immutable, dated); the resource indexes are POS.0840's. The
  ledger cites and never copies: under Waiting on principal a matter
  that has an ID gets one line — the ID, a few words, its state — and
  its substance stays in the thread or the record; free text only for a
  matter with no ID yet, which gets one at the next write; an unfinished
  conversation is saved into its thread of the intent, a write of
  whatever is agreed so far, never into the ledger. Added 2026-09-14
  (`sources/forge-run-record-health.md`, P.15, P.09, G.10).
- **POS.0170** Feedback from recipients has no channel of its own. The
  principal processes it and feeds conclusions back through
  `/forge intent`.
- **POS.0180** External inputs (transcripts, offers, documents,
  standards) live in `sources/` per project: immutable once registered,
  plain slug filenames, each in one form — text, or a functional binary
  (POS.1040). They may arrive at any stage of a project's life — before
  the brief as material for writing it, during intent work, or after.
  Origin dates are metadata, not ceremony: recorded best-effort in the
  ledger and never demanded from the principal. The principal may drop
  files into `sources/` manually at any time; `/ingest` without
  arguments sweeps the directory: it registers new files and reports
  files changed since registration with a question — what to do with
  each. The meaning depends on the project's kind (POS.0960): in a
  `thought` project a changed source is a breach of immutability to be
  settled (a new source beside it, the original restored, or the change
  knowingly accepted); in a `library` project it is the normal case, the
  owner's maintenance (POS.0970) — the ledger date moved, the index
  entry corrected. `/ingest` stores, registers and catalogues — nothing
  more. Registration does not imply intake: what a source is for is
  individual — a standard to verify against, inspiration, a meeting
  record, material to absorb — and is recorded as free-text Role in the
  directory's `00-INDEX.md` (POS.0840): the principal's word, asked for
  once after registration and left empty until he gives it, never
  inferred unasked (POS.1040); the ledger row is registration only. The
  principal alone directs how and when a source is used, in whatever
  work he chooses. When source content does enter the intent, it is his
  explicit act, cited with provenance to the file; what someone said in
  a meeting is never silently promoted to the principal's own position.
  A set of related files — a downloaded site with its index, a document
  with attachments — may live as a subdirectory `sources/<slug>/`: one
  source, one ledger entry, immutable as a whole from registration.
  File-level detail is not lost: provenance in the intent cites
  individual files by path, and the bundle's index or extract lists its
  contents. If a bundle's files ever need separate fates, a file may be
  split out to its own ledger row — the ledger is freely rewritten.
  Isolated files stay directly in `sources/`. Every bundle carries a
  `00-INDEX.md` catalogue in the shape POS.0840 owns; `/ingest` creates
  it at registration when the bundle lacks one and validates a supplied
  one against the contents, origin dates best effort, never asked for.
  Text extracts are produced by one script of the forge, never by ad-hoc
  parsing — no Python PDF reading, no manual transcription.
- **POS.0840** Resources have an index. Every `sources/` and `research/`
  directory carries a `00-INDEX.md` (the resource index): a light
  catalogue so that Claude — and the principal — know what resources
  exist and what they are for without re-reading the files. It is a
  working aid, not a record of thinking: it tracks nothing (no
  processing state, no positions) and is an automatic input of no
  command. `/forge`, `/critique` and the challengers do not confront the
  chain with the material on their own; a contradiction between the
  intent and a source is not a finding, because the source may be a
  counter-example, a mere inspiration or a record of what someone else
  said. Claude reaches for a file by its own judgement or when the
  principal asks ("check the assessment against the requirements in file
  X"). Each entry has fixed fields in free text. The ledger holds
  registration only — a Sources table and a Research table, no content
  columns — so that nothing is described in two places. A bundle keeps
  its own `00-INDEX.md` inside and appears in the top index as one entry
  pointing into it: two levels, never deeper, and the top index never
  repeats the bundle's contents. The bundle index is the same catalogue
  one level down. One shape for every index, because Role and Use for
  are what an index is for and a table does not carry them (decided
  2026-09-04). The index is freely rewritten like the ledger while the
  files under it stay immutable.
- **POS.0190** Artefacts are written once per iteration round, not once
  per answer — and this holds for any working conversation over the
  intent or open items (a `/forge intent` interview, a thread sweep,
  resolving findings), whatever the entry door. Answers are carried in
  the conversation and reflected back; at the round's natural end Claude
  asks whether to write and writes on the principal's confirmation — one
  version bump however many answers the round contained, with one
  record in the history per change (POS.0310). The principal may at
  any moment order a write of whatever is agreed so far. Writing after
  every exchange buries the substantive change under changelog churn
  and makes the history unreadable. Clarified 2026-09-26: a correction that lands on text
  written moments ago belongs to the round that wrote it and is carried
  like any other answer; an ordered write of what is agreed so far does
  not close the round unless he says so. The name the method carries is
  POS.1210's. "Written" means a file: whenever Claude reports something
  as written, it names the file and section; whatever is carried in the
  conversation only is said to be nowhere yet, and Claude never says
  nothing is lost while anything lives only in the conversation. Added
  2026-09-14 from the run record of `health` (P.01, F.01).
- **POS.0710** A project may spawn renders: audience-specific outputs
  generated from the chain — a pitch for the group, an architecture
  picture, an executive summary, the repository README. A render is
  never edited by hand; the iterated thing is its **recipe**
  (`recipes/<recipe>.md`): inputs (one artefact or several), audience,
  instructions and the literal output template in one file, versioned by
  the house scheme and composed conversationally with the principal.
  `/render <recipe>` regenerates the output mechanically, undated,
  overwritten freely; the files made from a render are POS.0590's. Every
  render opens with its provenance, citing the recipe and every input
  with their versions. A render assigns nothing and is not part of the
  chain: the artefacts remain the sole source of truth. The boundary
  between the two is authorship, not audience: a chain artefact is
  composed by the principal (Claude proposes, the principal composes), a
  render is generated from artefacts — an article the principal writes
  is a layer of the chain, its translation is a render. Dated hand-made
  editions of the earlier derivative convention remain in place as
  legacy history. Recipes are tools, not records of thinking: they carry
  a version and an updated date in front-matter — enough for a render to
  cite — and no status field, because a recipe is never approved and
  stays 0.x for life. Being versioned, a recipe keeps its history in the
  companion like every versioned kind (POS.0310); the companion records
  what changed in the recipe at its own grain, the substantive turns
  live in the intent. Recipes are deliberately loose: the template fixes
  the structure and what information appears where, never the wording —
  a presentation recipe says what belongs on a slide, not its phrasing
  or its placement on a picture. Each rendering re-derives the words
  from the current inputs; fixing the text in the template would turn
  the recipe into the render and make the inputs meaningless. A render
  may also serve as an input of another render — a deck slide citing an
  architecture picture as `render: <file>` — provided the citing recipe
  declares it among its Inputs, so provenance and staleness track the
  dependency.
- **POS.0720** README.md is a render of the forge project. README.md is
  never edited by hand: content fixes go into the recipe or the inputs,
  and the file is regenerated: a process change is complete only once
  the intent is updated and the README re-rendered.
- **POS.0730** Release notes are a log of releases, not a story.
  `RELEASE-NOTES.md` in the repository root is a render (`/render
  release-notes`) for one reader: the user of the engine who has cloned
  it and takes upgrades through `forge-pull`. One section per release of
  the engine — every `/release` (POS.1100), the version being the
  intent's, 3.12 as much as 3.0 — newest first; inside it fixed groups
  in a fixed order — one sentence per change from the user's side with a
  pointer (a position, a decision, a command, a script). At a major the
  minors since the previous major are folded into it — the house
  scheme's own reading of a major ("the next approved version,
  incorporating all changes since"). The sections are derived at the
  release from the records of the history log since the previous release
  (POS.0310). One thing is never derived: what the reader must do is
  written with the change, in the `Action` field of its record, and the
  render carries it into *Action required* word for word. A thought
  project's release notes work the same way from the histories of all
  its chain artefacts but the brief — intent, assignment, later layers —
  for the recipients tracking it. Reason: a reader wants to see plainly
  what was added, changed and removed. Decided 2026-09-05.
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
- **POS.1390** An intent says what the principal wants and why, and
  it does not solve. What he wants, what he does not want, what is
  the case, what is open and what he dropped belong to it; how the
  things he wants are realised belongs to the solution design. The
  test of a sentence: would it still hold if the thing were realised
  in a wholly different way? If it would, it is intent; if not, it is
  solution. A principle the principal sets for the solution, what the
  realisation must respect whatever its shape, is intent; the
  mechanism that honours it is solution. What the principal wants the
  user to be able to do, and what must be true when it is done, is
  intent, a command he asks for by name among it. How the command
  does it, what it is built of, its steps and their order and the
  checks it runs, is solution. The division is by kind of content,
  never by who said it: an idea of the principal's about how to build
  something is solution too. Reason: an intent that carries the
  solution cannot be read as what is wanted, and nobody can be asked
  for a proposal of the whole solution over it. Decided 2026-10-03.
- **POS.1400** The solution design is an artefact of the chain,
  `40-solution-design.md`: how the things wanted are realised. It is
  derived from the lowest layer the project has above it, the intent
  alone, the assignment or the BRD, and whatever stands above it is
  its input. No layer below the intent is a condition of another: a
  project takes the layers it needs, and many end at the intent,
  where what is wanted needs no solution written down. It is worth
  writing where the way is not obvious, where a choice has a price,
  or where two hands would solve the same matter differently if it
  were not written down; whether it is, the principal says. A layer a
  project does not have is not missing: `/forge` and the checks say
  nothing of it, and the ledger declares no end of the chain. Each
  artefact names its inputs in its definition; the number in a file
  name orders the files and prescribes no sequence. What others do
  with an assignment handed to them is their own run of the forge
  (POS.0700). From the artefacts of the chain the thing must be
  buildable without a look at the finished product: the product is
  what is built, never a source of its own design. How deep the chain
  must go for that is the project's: the solution design gives the
  architecture, a technical specification the detail where the one
  who builds needs it. Present shape 2026-10-04.
- **POS.1420** The solution design describes the solution as it stands
  and is kept current, as the intent is: its body is the present state
  and its history stands beside it. It is read by whoever realises the
  solution, a person or an agent, without the principal in the room. It
  is made of items, under a short prose head on how the parts work
  together. One prefix is its own: SOL, a part of the solution or a
  matter that holds across parts: what it is and what it answers for,
  which positions it realises, cited by their IDs and never restated,
  and where it is realised. Where a part rests on a real choice, the
  item says the choice, what it was chosen against and what it costs;
  where there was no real alternative, it says so and invents none. What
  is open is a TBC with its owner, with what would close it and with
  whether it blocks realisation. Where a part is realised in a file of
  its own, the item names the file and the detail is the file's; where
  it is only part of a file, or no file exists yet, the item carries the
  detail. The document holds what cannot be read off the thing itself:
  why, against what, at what price, and how the parts fit. A check keeps
  it true against what realises it. When it is complete is its
  definition's. Decided 2026-10-03.

### Structure and style of an assignment
- **POS.0200** Structured items with stable IDs beat prose, even at very
  high abstraction. Narrative is confined to Purpose & Context and
  Objective. Reason: an item with a stable ID can be cited, reviewed,
  traced into the layer below and changed one at a time; prose cannot
  be pointed at (given 2026-10-09).
- **POS.0210** An assignment assigns; it does not solve. What keeps a
  document an assignment is the kind of content, never its amount.
  The formerly enumerated ban — stakeholder matrices, RACI, impact
  analyses, MECE decompositions, tables of contents — originated in
  one early case and is not a universal rule: any such apparatus may
  appear where the principal judges it part of setting direction; it
  is the recipients' machinery only when it belongs to executing
  delivery. Decided 2026-08-17.
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
  stance is a new POS. Without a prefix of its own, a fact would have
  passed for a position. A thread (THR) carries its origin — the
  principal's word, a document by path, or Claude's synthesis — so that
  a hypothesis of Claude's stays visibly his until the principal takes
  it up; what Claude has worked out is never a FCT, since a fact is
  the principal's word or a source's. Origin is marked from 2026-09-14
  on, the principal's word being the default that needs no mark; no
  retrofit (`sources/forge-run-record-health.md`, P.08, F.04).
- **POS.0240** Every assignment carries a Terms section, so it can be
  forwarded without oral tradition. Defined Terms are capitalised in
  item text.
- **POS.0250** Requirements are written as shall / shall not, in full
  correct sentences, one idea per item, each written once.
  Would, could, should, might, may and MoSCoW wording are not used.
  Reason: shall is testable and binds; the softer verbs leave the
  recipient to guess what is required, and MoSCoW puts a priority
  where completeness belongs (given 2026-10-09).
- **POS.0260** No priorities and no priority column. Everything in an
  assignment is essential; an exception carries a note reading
  *optional*.
- **POS.0270** Testability is recommended, never required. Assignments
  are deliberately high-level; delegating concretisation through a DEL
  item is a legitimate outcome.
- **POS.0280** Success criteria are wanted but not compulsory. Delegating
  them to the recipients as a deliverable ("define success criteria and
  return") is a legitimate outcome, not a defect.
- **POS.0290** An item must not depend on an external link to be
  understood, agreed or later tested. Negative mandates (out of scope,
  do-not) rank equally with positive ones. FR / NFR markers may appear in
  item text where they help; they are never part of the ID.

### Versioning and state
- **POS.1080** A project's documents fall into five groups, and
  the kinds the table lists; the kind determines what a document is, who
  writes it, whether it is versioned and how it behaves. "Document" is
  the word for every file of a project; "artefact" is reserved for the
  documents of the chain — the ones the principal composes, the
  reviewers read and the renders are generated from. The table is the
  one page from which all of this is read, in the intent, in CLAUDE.md
  and in the README alike:

  | Group | Kind | Meaning | Written by | Versioned | Behaviour |
  |---|---|---|---|---|---|
  | artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
  | records | history | what changed in a versioned document, and why | forge | — | append-only |
  | records | decisions | the principal's decisions with reasons | forge | — | append-only |
  | records | review, challenge | one dated reviewer run | reviewer agent | — | immutable |
  | state | ledger | single source of truth for state | forge | — | freely rewritten |
  | state | index | catalogue of a resource directory | forge | — | freely rewritten |
  | state | map | the documentation map: one entry per page, everything a page is made from | generated | — | freely rewritten by the documentation run |
  | rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
  | rendering | render | audience-specific output, never a source of truth | generated | — | overwritten by /render |
  | rendering | page | a page of the documentation, or its index; never a source of truth | generated | — | overwritten by the documentation run |
  | resources | source | external input as it arrived | external, /ingest | — | immutable |
  | resources | research | durable answer to one question | Claude, /research | — | immutable |

  Which artefacts the forge has is the listing of
  `.claude/skills/forge/states/`, one definition each; they are
  listed nowhere else. The map is state of the project that owns the
  documentation and is never shown to the documentation's reader; the
  pages and the index are what he reads (POS.1450). Every versioned kind keeps its history in an
  append-only companion `<file>.history.md` (POS.0310); an integer version is
  approved, and a recipe never is. A functional binary — a `.potx`
  template, a graphic — is a source (POS.1040), so a library's assets
  fall under resources without a kind of their own; a library carries
  no artefacts and no records but its recipe's history companion, the
  other groups unchanged. The
  assignment is not "frozen" in any sense the file would show: it is
  rewritten freely between approvals like the intent, and what the
  recipients hold is a version reached by a link into git.
  Decided 2026-09-04.
- **POS.0300** Versioning follows the group BRD convention: integers
  denote signed-off versions. Drafts run 0.1, 0.2 …; 1.0 is approved;
  1.1, 1.2 … are changes made after approval, not yet approved
  themselves; 2.0 is the next approved version. Status in front-matter
  (`draft | approved | superseded`) must agree with the
  number. A major of the forge intent closes a set of features the
  principal names and passes more than a minor before its tag: every
  check, `single-source-of-truth` included, both critic lenses and one
  challenge, their findings settled or deferred by his word. The word
  closes the major; the test says what the word attests (2026-09-06).
- **POS.0310** Every versioned document keeps its history in an
  append-only companion `<file>.history.md` beside it, never in its
  body: the body is the current state, the companion the record. One
  rule without exception: brief, intent, assignment, every later
  artefact and the recipe alike. The history is a log. One record is one
  change and one line; records are appended at the end of the file and
  never rewritten, so the order of the file is the order of the changes.
  A version may hold several records, of the same item too. `Was` is
  word for word the part of the wording that ceased to hold. A record of
  creation needs no reason: the wording is in the document. The history
  of every versioned document is the same log. Where a change touches an
  item, the record names its ID; where it touches what has no ID, the
  record names the place: the heading of the section, or the file name
  where the change is of the document as a whole. In the forge's own
  project a change of the operating layer that touches no item of the
  intent is recorded under the subject `operating layer`, one record a
  round, so that the release notes can derive from it. `Was` is written
  wherever wording leaves an item or a place; a record of a change to
  the document as a whole carries none. The kinds of a record are
  `created`, `changed`, `closed` (a thread or an open question settled),
  `removed` (an item leaves the document and its ID is never used again)
  and `approved` (of the document as a whole: the approval of a brief or
  of a major). Every record names its author: the one who decided the
  change, by the handle the instance gives its principal, never the one
  who typed it. The field is there from the first record because a log
  is never rewritten and a field it lacks cannot be added to what was
  written. A record may carry `Action:`, what the user must do after the
  change, written with the change by whoever made it; the release notes
  are derived from the records (POS.0730). The record is written in the
  same step as the change it records, and the reflection before a write
  shows both: the new wording of every item touched and the record the
  history will receive, `Was` included. Before Claude proposes a change
  to an item, he searches the history and its archive for the item's ID.
  What he finds is said in the proposal only where it bears on the
  change, a direction once tried and dropped above all. The history is
  searched, never loaded whole. The log is the single primary: the
  commit messages `/save` and `/release` draft and the release notes are
  derivations by mechanism, which POS.1070 permits. The companion is
  part of its document: not a row of the ledger, handed over with it by
  the link into git. A history written before the log is kept as it
  stands, immutable, as the archive beside the log; nothing is
  converted, its rows are a record and stay in the words they were
  written in, and the history of an item is a search of both. Present
  shape 2026-09-29.
- **POS.0320** Immutable documents (reviews, challenges, sources,
  research) are never edited — a source from its registration, the
  others from creation; corrections happen downstream.
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
  lenses, the shared behaviour of each kind written once (POS.1120).
  Both take an optional target, an artefact named as `/forge` names it
  (`brief`, `brief-<name>`, `intent`, `assignment`, later layers as they
  come); without one, the whole chain, so that one file or one
  transition can be reviewed alone. Neither runs at a save; `/release`
  offers `critique essence` once and runs no reviewer on its own — the
  one lens that guards what a release publishes, the drift of the chain
  (decided 2026-09-05, POS.1100).
- **POS.0410** The critic has two lenses, because one critic hunted
  formalities and never guarded the chain. `clarity` reads each artefact
  on its own. `essence` reads the chain: for every adjacent pair (brief
  → intent, intent → assignment, every later layer) it first distils,
  blind, the essence of the downstream artefact in a few sentences, then
  the upstream's the same way, and compares; a finding is a difference
  of essences, not of texts. A target narrows `clarity` to that artefact
  and `essence` to that artefact against its parent — a transition is
  addressed by its downstream artefact, since every layer has exactly
  one parent, so no arrow is ever typed. Decided 2026-09-03.
- **POS.0420** `/challenge <persona> [artefact]` reviews the thinking
  through a chosen persona — one isolated agent per persona
  (`challenger-<persona>`), each defined by the blind spots it exists to
  find. The target may be any artefact of the chain, the whole chain
  when none is named. The contract is invariant whatever the persona:
  three to seven sharp challenges, each with a severity (dealbreaker |
  major | minor, ordered by it — a fatal flaw is never buried among
  cosmetics), a falsifiable "what would change my mind" and an epistemic
  status (consensus | active debate | emerging practice | my judgement);
  no fabrication — a precise "I don't know" beats an invented figure,
  and anything reconstructed from memory is flagged. The contract has
  one owner, the skill `challenger-contract` (POS.1120). What a persona
  goes after is its own Lens. The first persona is `cto` (CTO register):
  no stake in the principal being right; unstated assumptions, whether
  the stated objective is the real problem, second-order effects,
  organisational reality, failure modes, missing dimensions, the serious
  counter-case; the second is `architect`, for the solution design: he
  takes what is wanted as given and asks whether this is the way to get
  it; further personas — a strategist, a business analyst with the BRD —
  are created from the lens-file skeleton by the principal's decision
  when first needed, and only where their blind spots genuinely differ:
  personas that would say the same things in different words are noise.
  Bare `/challenge` lists the roster and recommends a fit for the
  project's subject.
- **POS.1120** The shared behaviour of a kind of reviewer is a contract,
  written once — never a copy. Each kind — the critic, the challenger,
  check (POS.0540), whatever comes after — owns one contract, and every
  lens, persona or check file of that kind carries its Lens section and
  nothing else of the shared behaviour. One contract per kind, because
  the shared texts differ almost whole; the few sentences common to all
  stay in each contract in its own words — three contracts and no common
  one, reopened only if a fourth kind repeats them. A contract is
  addressed to every lens of its kind, never a template with
  placeholders. The contract owns conduct, subject, way of working,
  report shape and ledger step; the lens file owns what it reads, what
  it goes after, its categories and its own report sections; a lens is a
  specialisation, never a replacement: it may make a rule stricter,
  never rename, drop or duplicate one; the protocol changes in the
  contract. The contract never names a lens; the lens file does. Decided
  2026-09-06.
- **POS.0430** Nothing blocks. There are no hard quality gates;
  checklists and findings are advisory and the principal alone decides
  what is published.
- **POS.0440** Every finding and challenge is either fixed or explicitly
  rejected with a recorded reason (DEC). Rejecting and parking are
  legitimate outcomes; silently ignoring is not. An accepted challenge
  is mended wherever it needs to be, and one that mends nothing was not
  accepted. A challenge of a layer below the intent is mended in that
  layer and changes nothing above it, unless it shows that what is
  wanted cannot be realised or only at a price not worth paying: then a
  thread is opened in the intent, citing the challenge, and what is
  wanted is decided there. The states in the ledger carry the words of
  the verdicts (POS.0850); `open` is a state only, not yet judged, and
  `resolved` stays the critic's, a fix that is in the document. The
  finding state `overruled` is retired (2026-09-27): it reads as
  `rejected` wherever it survives, the immutable reviews and the
  decision records keep the word they were written with, and a project's
  ledger is converted through a finding of the `light` check, on the
  principal's word or never.
- **POS.0450** An artefact is best challenged before the next layer is
  first derived from it — the intent before the first assignment, one
  day a BRD before the solution design — while accepted challenges are
  still cheap to absorb. Whether it runs again later — after a draft,
  before approval — is left to the judgement of whoever is running the
  process; no rule prescribes it.
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
- **POS.0510** Commands are entry points into phases, not the only
  permitted door; the core rules apply in ordinary conversation too.
- **POS.0530** This work is reasoning-heavy and token-light, so the
  strongest available model tier is the default — the session model,
  chosen once, with no per-agent pins (POS.0930).
- **POS.0540** Mechanical conformance runs on the same mechanism as the
  critic and the challenger (POS.1120): its own contract skill, one
  agent per kind of check, a roster, a run by hand. Whether it is called
  a review is not decided and does not matter to the mechanism, which
  takes further kinds as they come. The checks are POS.1140's. Read-only
  and advisory: they report and propose, the principal decides what is
  fixed. They check conformance, never substance or document quality —
  that remains the critic's and the challenger's territory.
- **POS.0550** The engine is persisted in git with a remote of its own,
  `main` the released line, branches allowed and left to git (POS.1110);
  every user project is likewise a repository with whatever remote and
  visibility its owner gives it. The scripts in `scripts/` are the only
  door to git — reading state included, no exceptions, enforced for
  Claude by POS.1200; how many there are is whatever the door needs,
  never a rule. No remote is configured anywhere in the forge: git
  carries that information itself. Immutability of documents remains a
  process rule enforced by convention, not by git: git protects nothing
  from a commit that rewrites a file, the rule costs nothing, and a
  mechanism would be one more layer to maintain that still would not
  stop a hand edit (reason given 2026-10-09).
- **POS.1200 The scripts-only door to git is a wall of the harness, not
  conduct alone; a commit carries no attribution.** The rule of POS.0550
  — the scripts in `scripts/` are the only door to git, reading state
  included — is enforced by the harness. The rule binds the forge, not
  the principal: his own git from the shell is his. Claude Code no
  longer adds or proposes a `Co-Authored-By` or `Claude-Session`
  trailer: the commit message is the one the principal confirmed, word
  for word. Decided 2026-09-21 by the principal.
- **POS.0570** The project's full conformance and the renders belong to
  the release, the bookkeeping check to the save. `/release` (POS.1100)
  settles the findings of its checks with the principal before the
  release commit. The recommended procedure, never a gate: nothing
  blocks (POS.0430). The full check left the save because it cost
  minutes and a walkthrough every time. The staleness of a render is
  never a check finding, the README and the release notes included: the
  release regenerates those two anyway, so the finding was void at every
  release and noise everywhere else (decided 2026-09-27); the `/forge`
  map shows staleness, and a render is regenerated only on the
  principal's word (POS.0810).
- **POS.1100** Save and release are two commands. `/save` runs the
  `light` check (POS.1140) and then commits and pushes on whatever
  branch is checked out, through `forge-save`, no render, seconds.
  `/release` runs on `main` only and refuses elsewhere, naming the
  branch: its checks, with their walkthrough (POS.0570); the README and
  release notes from the settled sources (POS.0730, POS.1000, POS.0810);
  the release commit "release <intent version>" and, at an approved
  major, the tag `v<major>`. The release number is the intent's version
  (POS.0730). Any other tag on request, `/save --tag` or `/release --tag`,
  on a branch as well. Only the major's tag has a fixed name, so
  `/check` and the release notes can rely on it: an integer is a
  released major, anything else a snapshot. Why two: the renders cost
  minutes and tokens beyond reason at every save, and the two-speed save
  had existed in practice for weeks; with the renders at the release
  only, the README on `main` is current at every release and stale in
  between visibly (the `/forge` map), never silently. Decided
  2026-09-05; alternatives REJ.0160, REJ.0170.
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
  next commit lands, and nothing that rewrites history. The forge
  stays a single-user tool per instance, more people means more
  instances and coordination by git (bearing on THR.0090). Decided
  2026-09-05 with POS.1100.
- **POS.0580** Work on the chain is invoked by target state, never by
  verb: `/forge <state>` (`/forge intent`, `/forge assignment`) —
  knowing the name of the target artefact is knowing the command, with
  nothing to memorise as layers are added. Each artefact's definition
  declares its own inputs — so the chain is a star, not a fixed line: a
  future layer branches from any artefact by adding one definition. A
  definition is that of the elicitation of its artefact, in the seven
  blocks of POS.1310, and stands beside the artefact's template as a
  pair.
- **POS.0590** Everything the forge produces is Markdown, renders
  included: a presentation is a `.md` saying what is on each slide
  (mermaid for pictures). The forge still ends at content, but it
  carries its delivery-format tools at its edge: one turns a Markdown
  deck render into a `.pptx`, another a Markdown render into a `.docx`.
  The Markdown render remains the sole source of truth; the generated
  file is an output of second order — regenerated at will, never edited
  by hand. All other format conversion stays outside the forge, as git
  is for persistence. An output is made in two steps, each with its own
  command, divided by cost so that the expensive conversion runs as
  seldom as possible (the principal's, decided 2026-09-27). `/render`
  generates the Markdown and, where the recipe names a format, the plain
  file beside it: deterministic, cheap, repeated freely. `/publish`
  makes the designed file through a model and its document skills into
  `published/`: only on the principal's command, never by `/render`, by
  `/release` or on Claude's own judgement; it makes a file and sends
  nothing anywhere. `/publish` takes the render as it lies on disk and
  never renders — a render is made by a model and is never the same
  twice, so a second one would publish a text the principal has not
  read; a stale render is named before the conversion and the word is
  his. A recipe that names no format ends at the Markdown. The word is
  `publish` by the principal's choice; it agrees with "only the
  principal publishes" (POS.0430).
- **POS.0770** Recipe composition may be guided by genre: `/recipe
  <genre>` mirrors the `/forge` star (POS.0580) — one definition per
  genre carrying the elicitation checklist, with the genre's canonical
  skeleton extending the base recipe shape, never replacing it. The
  first genre is `presentation` — a slide-by-slide deck definition whose
  render is turned into a PowerPoint file. The genre is named
  "presentation" rather than "deck" for company-wide legibility at
  rollout.
- **POS.0830** The forge runs beyond Windows. `scripts/` is the only
  platform-bound layer, and its scripts are written to run unchanged on
  Linux and macOS. Instance facts are out of the scripts: no remote URL,
  no author identity, no first-run initialisation — git configuration is
  the user's (POS.0950). Portability is verified by running the set on
  Linux (WSL suffices); until then it is a writing rule, not a claim.
  The scripts are Python, decided 2026-10-02 on the feedback of the
  forge's users and done 2026-10-09, the per-prompt hook included:
  `python` on PATH is their one prerequisite, the same Python the
  document conversion needed already, and a system that has only
  `python3` gives it that name (THR.0150 closed). How they are
  written and what they share is the solution design's (SOL.0620).
- **POS.0940** The engine does not know the projects. `git init` and the
  remote are the user's one-off act: `/new-project` and `/spinoff`
  create files only and never touch git, and a project starting "not
  under git" is a property, not a defect. A project without a
  repository, or with a repository and no origin, is a legitimate shape
  — a sensitive project kept local; the second keeps the history the
  renders and recipes rely on, the first does not. Upgrade is
  `forge-pull` on the engine — a fast-forward of `main`. A project
  records no engine version: `/check` measures it against the current
  conventions. That is the whole migration path of any instance, the
  principal's and a third party's alike: after `forge-pull`, `/check
  light` and `/check project` on each project say what the conventions
  changed (which check owns what: POS.1140), the release notes' Action
  required lines say what to do, and Claude migrates on the user's word;
  no migration tool exists, knowingly. Shapes rejected: REJ.0150.
  Decided 2026-08-29.
- **POS.0950** The engine carries no instance facts. Who the principal
  is (by role) and what language the conversation runs in live in
  `CLAUDE.local.md`, a file of the instance kept out of the repository,
  and everything there reaches every subagent, the isolated reviewers
  included (THR.0240). Therefore only what must be always-on and is
  harmless in a public report lives there; the git identities — names,
  e-mail addresses, hosts — live in the user's own git configuration
  outside the engine, and instance facts are forbidden in a reviewer's
  report. `CLAUDE.md` names the principal and the conversation language
  only as things that exist, never by value; the document language is
  the project's own (POS.0060). The scripts carry no URL and no identity
  (POS.0830). The commit identity is git's business, not the forge's: it
  is resolved per git host by the user's own configuration, and the
  forge sets no identity anywhere. Reversed 2026-09-16, written
  2026-09-18: an identity kept by the forge duplicated what the user's
  own configuration already resolved, every repository carried the same
  identity twice, and the forge had gained a file, a template and three
  identity steps for a case that had not occurred. The two-roles case,
  one host serving two identities, is accepted as a risk the user
  resolves by hand. What the forge keeps: `/setup` (POS.1050) offers to
  write that configuration and the one global guard, so that a commit in
  a repository on a host with no identity fails aloud instead of
  silently taking a default, and a save commits nothing until git
  resolves an identity for the repository. A subagent sees the
  session's whole context, CLAUDE.md as the session read it and the
  assistant's memory included, and may take it for the file on disk;
  so every agent that writes an outward-facing file says in its
  definition that instance facts are not material and that an input
  is read from disk, and the generated files are scanned mechanically
  before they are kept (found 2026-10-04 at the release of 4.58 and
  2026-10-09 in the documentation trial; THR.0580 closed 2026-10-09).
- **POS.0930** One model for the whole forge. Every command, chain state
  and reviewer runs on the session model, so that the strongest model
  the forge runs on is a decision and never an accident of a pin that
  has aged. Speed is bought with context, not with weaker models:
  `/render` generates in an isolated subagent that sees only the recipe
  and its inputs, never the working conversation — the same principle as
  the reviewers', applied to a mechanical job. Per-command pinning to a
  faster model is rejected for now: the routine commands are a small
  share of the work and slow for the size of the context they carry, not
  for the model, and every pin is a convention to keep. A per-recipe
  model for the render is deferred until a recipe is genuinely
  mechanical, since a smaller model drifts from a recipe that leaves it
  room (the drift POS.0810 guards against). The session model is chosen
  in one deliberate place — an instance preference. The one exception is
  the headless conversions behind `/publish`: a headless run has no
  session model, so each needs a default of its own — an explicit
  parameter, not an aged pin. The same lever carries the checks: every
  check executes its own definition in an isolated subagent that sees
  only the files, returning the report for the walkthrough in the
  session, and `/release` launches its renders in parallel (which
  command renders what is POS.1100's); the working conversation is spent
  on verdicts, not on reading. The documentation writer is the case
  the deferral waited for: a mirrored page leaves the model no room,
  so a mirrored page is written on a faster model and a derived page,
  like the planner, on the session model, the choice made
  mechanically by the page's entry, never per run; the trial of
  2026-10-09 showed Opus more complete on derived pages and Sonnet
  sufficient on mirrored ones (THR.0340). Present shape 2026-09-02,
  the writer decided 2026-10-09.
- **POS.1070** One mechanism lives in one place and is used from there.
  Whatever the forge already has a procedure for — a command, a skill, a
  script, an agent — is invoked through that procedure whenever its
  situation arises, never re-described ad hoc: `/release` regenerates
  the README and release notes through `/render` and ends by running
  `/save`, git is touched through the scripts in `scripts/` (POS.0550),
  reviews run through the reviewer agents. A command that needs
  another's mechanism references it by path and adds nothing of its own
  to how it runs; the rules of a mechanism — isolation, wrapping,
  provenance, what may be read — are written once, in its own
  definition. Restating a procedure in a second place is a defect: the
  two copies drift, and the copy without a rule silently loses it. The
  `single-source-of-truth` check carries the standing rule over the
  whole operating layer, run on the principal's word and never at a
  release on its own (POS.1140), so that the rule costs a release
  nothing and the sweep is honest when it runs. Where a shape had no
  owner at all, it gets a skeleton rather than a second description. A
  restatement is steps, rules or a shape repeated; a one-line reminder
  at the point of action that names its owner — "not under git is a
  fact, not a defect (CLAUDE.md, Persistence)" — is not one, since it is
  what Claude reads when he acts and the citation keeps it honest
  (decided 2026-09-27).
- **POS.1090** The harness enforces the principal's word where it can.
  Claude is kept from the user's sensitive paths, and web access is
  approved by the user per domain. A command that writes, scaffolds,
  commits or regenerates — `/save`, `/release`, `/spinoff`, `/setup`,
  `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
  `/render`, `/publish` — is guarded by the harness, so that Claude cannot start it on his own
  judgement: the principal invokes it by slash, or asks in words and
  Claude follows the command's definition read by path. Maps, reports
  and rosters (`/forge`, `/ledger`, `/check`, `/critique`, `/challenge`,
  `/research`, `/recipe`) stay Claude's to start, since he is meant to
  propose them. The guarantee of Step by step (CLAUDE.md, Working
  methods) thereby rests on the harness as well as on CLAUDE.md. Decided
  2026-09-05. Step by step names one more such step since 2026-09-14:
  the birth of a new versioned document — a brief, a recipe, a layer of
  the chain — happens on the principal's word, never as a by-product of
  another operation (`sources/forge-run-record-health.md`, P.05, F.06).
- **POS.1140** Check runs on the reviewer mechanism — POS.0540 decided
  it, this is the shape. One command `/check <check> [slug]`, bare the
  roster; the roster open. The first checks, each owning one concern and
  none another's: `project` — structure, IDs, language, immutables,
  recipes and renders; `light` — front-matter against the companion and
  the form of its log, the ledger against the files, dependencies,
  resource indexes, fit for a save; `engine` — the core against itself
  and the forge intent, the rename sweep; `single-source-of-truth` — the
  whole operating layer for restatements and direct operations
  (POS.1070), the honest sweep, expensive by design, run on the
  principal's word before a major or after a round on the operating
  layer, never by `/release` on its own, a project on request. The check
  `history` reads a document with its history and reports where the
  division between them does not hold, by what POS.0120 says belongs
  where. Run on the principal's word. A rule an older position
  attributes to `/check` as one procedure belongs to the check that owns
  its concern by this list — bookkeeping, ledger, dependencies and
  indexes to `light`, structure, recipes and renders to `project` —
  never to two. Composition is the caller's and checks never call each
  other. The word for a check's variants is "check" — the light check,
  the project check — the mechanism's name serving for its members. A
  check's findings are filed like a critic's: FND of the project's one
  sequence, a dated report in `reviews/`, a row in the ledger, settled
  by walkthrough, a rejected one by a DEC and then not raised again; a
  run that finds nothing files nothing. Reason: one mechanism for every
  reviewer. A finding without an ID has no place for its verdict, so a
  rejected one returns at the next run, and a user cannot tell why one
  reviewer's findings are kept and another's are not. The session
  gives the IDs and files the report, never the agent: the IDs of a
  project's findings are given in one place, and a check that every
  save runs would otherwise write into the project at every save
  (reason given 2026-10-09). Present shape
  2026-10-02; the `/research` point stays in THR.0290.
- **POS.1190 The forge explains itself from its own definitions.** `/man
  [command|method]`, alias `/manual`, is the forge's manual — a reader,
  never a text of its own (POS.1070). Named after the Unix manual,
  `/help` being a built-in of Claude Code. Decided 2026-09-18 for the
  newcomer's first hour and for the reader who opens the repository.

### Naming
- **POS.0600** The system is named **Forge of Thought**: thoughts are
  the raw material — of whatever kind, nothing is presumed about them —
  and forged assignments are the product. Chosen with the full-chain
  vision in mind (assignment → BRD → architecture → full realisation
  deck). Repository `forge-of-thought`
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
  only where version 1 of the chain happens to end.

### Growth path
- **POS.0700** The principal intends to keep extending the engine
  downward: thoughts are forged as far as he needs them taken. The BRD
  layer is certain to come; solution architecture and integration are
  intended; a strategy layer is possible if it proves to make sense.
  Which layers are added, and in what order, is open — possibly all of
  these, possibly none yet. Nothing is approved for construction: the
  mechanics of a layer (commands, agents, reviewer calibration) are
  designed when that layer is actually taken up, not in advance.
  The layers below the assignment grow in the same project, by the
  same principal's hand, when he chooses to take his own thought
  further — a BRD as his next layer, not as someone else's
  deliverable. What a recipient does with an assignment in his own
  instance is his own forge run: the assignment becomes his brief, by
  his hand today (an assignment is self-contained for exactly that),
  by a command of its own only when that day comes (THR.0090). The
  chain never spans two principals (2026-09-06).
- **POS.1430** A new kind of artefact is added to the forge by one
  command, `/new-artefact <name>`, so that the chain grows without
  anyone having to know by heart what a kind of artefact is made of.
  The command leads to everything a kind needs and forgets none of
  it: what the artefact is, for whom, from what it is derived and
  why, held as a position of the forge intent before anything is
  built; its definition and its template as a pair (POS.1310); the
  prefixes of its items where it needs its own; whether it needs a
  challenger of its own and what the critic must know of it; and
  where it is realised, in the solution design. The command decides
  nothing: how the kind is composed is the principal's choice as for
  any artefact (POS.1410), and each of these is born on his word. The
  first artefact of the new kind is not the command's: it is made
  through `/forge <name>` on real work, and that is the trial of the
  definition (POS.1380). For now the command adds to the engine, for
  every user of it. A user is to be able to add an artefact of his
  own as easily, kept at his own place; where that place is waits for
  THR.0300 and THR.0230. Types other than an artefact, a whole chain,
  a reviewer, a genre, are not this command's (THR.0480). Reason: a
  kind added by hand took a search for everything it touches, and two
  of the things it needs, a prefix and a challenger, are easily
  forgotten. Decided 2026-10-04.
- **POS.0760** The forge is split into a public engine and user projects
  in repositories of their own. The engine — the core together with
  `projects/forge` — is public and contains nothing sensitive and no
  instance facts (POS.0950, POS.0980); users keep their projects
  wherever they choose and are themselves responsible for what those
  contain and where they live, generated decks carrying corporate
  branding included. Decided on 2026-08-29 from
  `00-brief-public-engine.md`.
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
  project. The boundary for the public `projects/forge`: nothing
  company-specific by name — no company name, no URLs, no e-mail addresses, no content of
  the company projects; the slugs of the company projects stay, since
  that projects of those names exist and travelled the chain is a
  process fact, not content (THR.0210 draws the line); a
  forbidden-term list is no guard, since a grep catches names, not
  content. The public forge project holds nothing outside that
  boundary, its immutable documents included — rewritten once before
  publication, immutability knowingly broken, recorded in the ledger
  and nowhere in the files; the brief is English for the same reason,
  a one-time yield of POS.0060. The public repository has a fresh
  history; the full record is on the company host, archived
  read-only, its last complete state tagged `pre-split`. Until a
  public exemplar exists (THR.0200) the README carries no example
  project. Present shape 2026-08-30 (from `00-brief-public-engine.md`).
- **POS.0990** The public face. The engine lives at a public repository
  of the principal's, named `forge-of-thought` — the bare word "forge"
  is overloaded on every code host and says nothing in a search — under
  the licence **CC BY 4.0**: anyone may use and adapt the engine, and
  must credit the author and link to the repository. The README
  therefore names one person, the licence holder — the author with a
  contact address — as a fixed text of the readme recipe, and this is
  not an instance fact: it is who the work is by, whoever runs an
  instance. The `LICENSE` file carries the licence's verbatim legal
  code. Decided 2026-08-30.
- **POS.1440** The forge is open to those who use it. What it wants of
  them most is feedback and ideas; a finished change is welcome too,
  on the forge's own rule: a change of how the forge behaves goes
  through the chain before it is built, a document that is a render
  through its recipe, and nobody sends a change he has not tried
  himself. A visitor is told how, where the readers of GitHub look
  for it. What enters the forge stays the principal's decision
  (POS.0070). Decided 2026-10-04.
- **POS.1000** Every project has a README and, if it is a thought
  project, release notes — both renders of the project's own recipes
  (`recipes/readme.md`, `recipes/release-notes.md`, `output:` in the
  project root), exactly as the engine has them (POS.0720, POS.0730;
  POS.0810 for the review of the regenerated output): the recipe is what
  is iterated, the render is never edited by hand, and every `/release`
  of the project regenerates both after its check (POS.1100). A library
  has a README only — a catalogue of what it holds and how to use it,
  from its ledger and indexes — since release notes are derived from the
  history of an intent, which a library does not have; its history is
  git. The two recipes are genres of `/recipe`, scaffolded by
  `/new-project` and expected by `/check`; the ledger's Renders table
  carries them like any render. Every README closes with one fixed
  sentence, part of the readme genre, so that whoever finds the project
  knows what runs it (principal's decision 2026-08-30). The engine's own
  README is the one exception: the sentence exists to point a visitor to
  the engine, and the engine's README is that destination.
- **POS.1450** The documentation of a project is a set of pages, one
  topic each, kept with the project and readable where it is published
  and in a clone, with an index that lists every page and names each
  reader's path through them. Three readers, in this order: the user who
  clones the thing and works with it; the extender who adds to it; the
  evaluator who never runs it and wants to understand what it is and how
  it works, and gets the concept pages and nothing made for him alone.
  Five sections by the reader's journey, the same for every project:
  Start (how-to: what the thing is, what must be on the machine, the
  first setup, the first result), Use (one page per job the thing has a
  command or a procedure for), About (one page per concept and per kind
  of artefact or part, the reasons included), Extend (what it is made
  of, how a change is made, proved and recorded, one page per kind of
  addition), Reference (the commands, the rosters, the conventions, the
  layout, the scripts, the templates, a glossary; mirrors its owners,
  never explains). Each page is of one kind, how-to, explanation or
  reference, opens with what it is for and for whom, and stands on its
  own. A section or a page with no material is left out, never left
  empty: a project that is not installed has no install page, and that
  is no gap. The documentation is generated from the project's documents
  and never composed or maintained by hand: a page either mirrors the
  files that own its topic or is derived from named evidence, and says
  which; a page cannot drift from what it mirrors. The README is cut
  to what orients and points, its chapters the readme skeleton's
  (`templates/recipe-readme.md`, the one owner); English only, a
  translation a render. It is made by
  a command of its own, `/document [slug]`, in one run that asks
  nothing: a plan of the pages first, the map, then every page made
  alone from its entry in the map and from the files the entry names,
  read from disk, nothing else; what the inputs do not support is left
  out and reported, never guessed. A run regenerates only the pages
  whose inputs changed, decided mechanically from the inputs, never by
  judgement, so that a run is cheap and the page names stay stable. A
  page is not a render: no recipe stands behind it and `/render` is
  untouched (REJ.0240). No instance fact reaches a page (POS.0950).
  Facts no file owns, the install commands, the prerequisites, the
  public address of the repository, have one place in the project that
  both the README and the documentation read. A release never
  regenerates the documentation: it reports the age of the index against
  the intent's version and offers `/document`; the pages pass under the
  principal's eyes as every regenerated render does (POS.0810). Reason:
  the README was the whole documentation of the engine and poor as one,
  three things at once; a page of one topic can say a thing well, and
  people inside the company and outside it should understand the forge
  and use it in full. The first version of the engine's documentation
  was generated 2026-10-09 (79 pages); what the documentation of a
  project other than the engine reads is THR.0590. Decided 2026-10-09
  from the brief `documentation`.
- **POS.1010** A project may carry an icon: `logo.png` in the project
  root, supplied by the principal, picked up as the repository avatar by
  hosts that do so. Optional — a project without an icon is complete. No
  `assets/` directory exists; one is introduced only when images beyond
  the logo appear.
- **POS.1020** A project registers what it relies on outside its own
  repository. The ledger carries a Dependencies table with one row per
  document of another repository the project cites: a deck template
  named in a recipe, a library document an index entry or a position
  refers to. Registration only, like sources: what the document is for
  lives where it is used. No version is recorded — a library document is
  maintained by its owner and cited as a moving target by design
  (POS.0970). Rationale: a cross-repository citation is a dependency
  taken knowingly (POS.0970) — knowingly means written down where state
  lives, not discovered when a render loses its template.

- **POS.1030** The forge's behaviour lives in the engine, never in the
  assistant's private memory. Claude Code keeps a per-directory memory
  outside the repository; whatever it learns there about how the forge
  should work — a working method, a rule of a command, a convention — is
  written into CLAUDE.md, the commands or the templates and removed from
  memory, so that every instance of the forge behaves the same and a new
  user meets the same forge as the principal. Memory is left with what
  is personal to one principal — his idiom, his private choices — and
  instance facts go to `CLAUDE.local.md` (the commit identity is
  git's, POS.0950). Decided 2026-08-30.
- **POS.1040** A source has one form. A file in `sources/` is either
  text or a functional binary, never both by default. At `/ingest` every
  binary file — isolated or inside a bundle — gets one question: convert
  to Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and that
  extract is the source; the original is not copied into the project.
  No: the binary is the source as a functional thing — a deck template,
  a graphic, a logo. Keeping both is the exception, on the principal's
  explicit word. Reason: the repository carries what the forge works
  with — text — and a binary nobody reads from git is weight without
  use; a binary that is used as a thing is kept because it is used.
  Three additions of 2026-09-14 from the run record of `health`:
  `/ingest` takes text pasted into the conversation as well as a file
  (P.10, G.04); before storing, personal matter — a named private
  person, an identifying detail, health, anything of the kind — stops
  the command and asks (P.11, G.09), because a source is immutable
  from its registration and travels into git, so what has entered
  cannot be taken back and the question must come before the store
  (reason given 2026-10-09); and the role of a source is the
  principal's word, never inferred — after registration Claude always
  asks "what is it for?", and he answers with the role or tells Claude
  to infer it, which is then written marked *(inferred)* (P.06, F.05).
- **POS.1050** First run is one command. After cloning the engine,
  `/setup` prepares the instance: it fills the facts of the instance in
  an elicitation interview — the conversation language first, then who
  the principal is by role, since the first correction of a newcomer's
  run was the language of the first question
  (`sources/forge-run-record-health.md`, P.15, G.13, 2026-09-14) — and
  it sets the session model to **Fable**, without asking: the strongest
  available model is the forge's default (POS.0530), the whole forge
  including the blind reviewers runs on it (POS.0930), and a newcomer's
  first minute is no place for a model decision. `/setup` never
  overwrites. The interview closes with the git identity, which is git's
  (POS.0950): `/setup` asks for the hosts the user pushes to, a name and
  an e-mail for each, and offers to write his git configuration for
  them, together with a global guard, never overwriting existing
  content, all written on the user's word; declined, printed for him to
  apply by hand. `/setup` runs no git operation — the user's git
  configuration files are the one thing it may edit outside the engine,
  on his word. Named `/setup`, not `/init`: Claude Code's built-in
  `/init` generates a CLAUDE.md, and the collision would send a newcomer
  to exactly the wrong action at the most sensitive moment. Decided
  2026-09-01.
- **POS.1060** A project arrives through the scripts-only door.
  `/import-project <git-url>` brings an existing project into the forge:
  it clones the repository, through the forge's clone script (POS.0550),
  into `projects/<repository name>`; a nonconforming name is fixed by
  renaming the directory afterwards. The script carries no identity and
  sets none (POS.0830, POS.0950). Work then starts by selecting the
  project — `/forge <slug>` — because the engine does not track it and
  cannot guess it.

## Facts

None: what this project rests on as fact is how Claude Code behaves,
worked out by Claude; what Claude has worked out is never a FCT
(POS.0230).

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
- **REJ.0140** `local/` as the home of user-local files. Dropped on
  2026-08-29: it existed only to keep company material out of the
  repository, which the gitignored `projects/*` now does; deck templates
  live in a library project (POS.0970) and are named by path.
- **REJ.0150** Shapes of the engine/projects relation rejected on
  2026-08-29: git submodules, subtree and worktrees — they model a
  dependency, which this relation is not; the engine as a template
  repository and copying the engine into projects — every comparable
  project that does so ends in manifests, override layers and
  migrations; a plugin as the only shape now (THR.0190).
- **REJ.0160** Stale-only rendering at the save: one command, `/save`
  regenerating only a render whose recipe or input moved in that save, a
  `stale (skipped <date>)` mark in the ledger for a render skipped on
  the principal's word. Rejected 2026-09-05: it saves perhaps a third of
  the engine's saves and nothing on projects, whose README input — the
  ledger — moves at every operation, and it adds a staleness state that
  `/save`, `/forge` and `/check` must all read alike; the two-command
  shape of POS.1100 saves everything and adds nothing.
- **REJ.0170** A fixed working branch with a forge switch that merges: a
  `work` branch per repository, one script creating and switching it,
  `/release` merging it into `main`. Rejected 2026-09-05 as the first
  step towards the wrapper of git the principal does not want — merge
  and conflict logic in the forge's hands, two branches a non-developer
  must understand — while forcing a branch on those who do not need one.
  The switching half survives as the voluntary `forge-branch` of
  POS.1110; the merging half stays git's.
- **REJ.0180** A second home for what the finding of a brief yields
  and the brief does not take: an intent 0.1 as a draft beside a
  draft brief, a "notes" record kind (P.07 of
  `sources/forge-run-record-health.md`), or a new artefact before
  the brief. Rejected 2026-09-28: the brief holds the principal's
  choice (POS.0110), and what he does not take needs no home: a
  finding or a source has `research/` and `sources/`, and what merely
  fell by in the conversation is gone with it.
- **REJ.0190** A "parked" document kind without a mining state, for
  matter set aside from a layer (`sources/forge-run-record-health.md`,
  P.12, G.06). Rejected for now,
  2026-09-14: parked matter lives as a THR of the intent or under a
  Parked heading of the artefact it came from; moving it into a brief
  was the error, not a missing kind.
- **REJ.0200** An edit mechanism for large artefacts so that
  temporary scripts disappear (the second half of P.10, G.04,
  `sources/forge-run-record-health.md`).
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
  before every block that is not the principal's own. Dropped
  2026-09-28: nothing in a brief marks authorship (POS.0110), and a
  mark that names a model reads differently on every model the forge
  runs on. What carried
  something other than authorship stays as `(source: <path>)` and
  `(remark: …)` (POS.0110).
- **REJ.0230** The status `in_review`, and the standing rule that an
  intent consolidated by Claude from the conversation carries it
  until every position has been walked through, with no lower layer
  derived before (POS.1180, decided 2026-09-14). Dropped 2026-10-02:
  the rule was made in haste for one case, and that case had a
  wholly different cause, a save in haste of three days of talk
  written nowhere. A walkthrough of an intent runs when the principal
  asks for one; the statuses are `draft`, `approved` and `superseded`
  (POS.0300).
- **REJ.0240** A recipe per page, the documentation as renders of
  `/render`. Considered 2026-09-08 (THR.0340, the guide and the
  reference as renders into `docs/`). Dropped 2026-10-07: eighty pages
  would mean eighty recipes to iterate by hand, and a recipe is a tool
  the principal shapes, while a page is to come from the project's
  documents with no hand in between; the map replaces the recipes, one
  generated entry per page.
- **REJ.0250** A site or a wiki for the documentation now. Dropped
  2026-10-09: GitHub shows Markdown pages and the README of a directory
  as it stands, so pages in the repository are readable without a build,
  a host or a second place to keep current; a site stays possible later
  over the same pages.
- **REJ.0260** A hand-kept file of the philosophy in the project root.
  Dropped 2026-10-09: the why lives in the brief and the intent already,
  and a hand-kept copy would drift from them; the About pages are
  derived from those two, the pitch stays a render.

## Candidate structure for the layer below

Not applicable: this project's handover artefacts are the core itself
(`CLAUDE.md`, `templates/`, `.claude/`) and `README.md`. A
`20-assignment.md` would duplicate them for an audience that does not
exist; see the ledger.
