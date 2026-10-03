---
project: forge
type: research
topic: work without a known artefact and its working files - how agentic tools and established practice run open-ended work and where they keep what arises on the way
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (draft)
status: immutable
---

# Work without a known artefact, and its working files

## Question

How do agentic tools and established practices for knowledge work run
a piece of work whose output is not known in advance, and where do
they keep the working files, data and several outputs that arise on
the way?

The question comes from two sections of the draft brief `next-gen`:
"Work without a known artefact" (the example is a strategy; wanted
are ingest, research, logs, history and elicitation; the named price
is that a general elicitor has no map of what is to be found) and
"Further outputs and working files" (spreadsheets, data, several
output documents, with no place and no rule today).

Out of scope, and covered by earlier notes that are cited and not
repeated: how an elicitation between a human and an AI is defined
(`2026-09-28-human-ai-elicitation-over-artefacts.md`, below "the
elicitation note") and how layers of documents from idea to handover
are cut (`2026-09-28-artefact-layers-from-idea-to-handover.md`, below
"the layers note").

Surveyed on 2026-10-03: the vendor's own documentation of five
surfaces of Claude (projects, file creation, Research, Cowork with
its plugins, Claude Code's memory and plan mode); four engineering
texts of the same vendor on long-running agents and the prompting
guide; deep-research and notebook products of three other vendors;
four open frameworks for research agents and one agent builder's
account; reproducible-research practice (three papers and guides,
one project template); consulting and audit practice (secondary
pages only); and the handling of binary and large files under git
(git's own documentation, two hosting and tooling pages, one
community handbook).

Epistemic tags: **[C]** consensus across the sources read, **[P]**
practice of tools, stated by their makers and not tested
independently, **[E]** emerging, **[X]** contested. Each finding says
whether it is verified at a page fetched in this session, taken from
a secondary source, or this note's own synthesis.

How the sources were read: every page was opened through a fetch tool
that returns a small model's extraction of the page, not the raw
page; four pages of the vendor's documentation came back as full
Markdown and were read directly (the memory tool, the prompting
guide, Claude Code's memory page and its common-workflows page).
Quotations are as the tool returned them and were not compared with
the pages character by character; no page was fetched a second time.
Pages that refused the fetch are listed under "What was not found".
Product facts carry the date of the page where it showed one;
otherwise the date of the fetch stands.

## Key findings

### 1. When the deliverable is unknown, the tools frame the work by a plan the human confirms, and the plan is the first output [P]

Verified at the pages fetched, except where marked.

- **The vendor's own description of the problem.** Research is
  "open-ended problems where it's very difficult to predict the
  required steps in advance. You can't hardcode a fixed path for
  exploring complex topics, as the process is inherently dynamic and
  path-dependent" (Anthropic, 2025-06-13). In that system the lead
  agent "thinks through the approach and saves its plan to Memory to
  persist the context".
- **Deep-research products put a plan in front of the human.**
  Gemini: after the prompt, "Gemini will create a research plan for
  your topic", with "Edit plan" before "Start research" (help page,
  undated, fetched 2026-10-03). ChatGPT: the help page refused the
  fetch; a search summary of it says that deep research "may ask
  clarifying questions" and shows a proposed research plan the user
  can review and modify (search result only, not verified at the
  page). Claude's Research is described without a plan step: it
  conducts "multiple searches that build on each other while
  determining exactly what to investigate next" (help page updated
  2026-06-02).
- **Cowork** states its first step as "Analyzes your request and
  creates a plan", then "Breaks complex work into subtasks when
  needed" (help page, "updated this week", fetched 2026-10-03).
- **Claude Code's plan mode**: "Claude reads files and proposes a
  plan but makes no edits until you approve"; the plan can be opened
  in a text editor and changed before approval (documentation,
  undated).
- **Open frameworks.** GPT Researcher: "The planner generates
  research questions, while the execution agents gather relevant
  information." STORM has a "Pre-writing stage: The system conducts
  Internet-based research to collect references and generates an
  outline", and its collaborative variant keeps "a dynamic updated
  mind map" as the shared picture between human and system. LangChain's
  Open Deep Research is described by a search summary as running
  "user clarification, research planning, parallel execution ... and
  final report synthesis"; its repository page, fetched, shows it
  archived on 2026-08-21 and did not confirm a step named "research
  brief" (that name is unverified).

Two observations, this note's own. First, all of these still end in
one known kind of output, a report; the open part is the path, not
the form. None of the products read frames work whose result is
several things of unknown kind. Second, what the human confirms at
the start is a list of questions or steps, never a list of sections
of a document: when the artefact is unknown, the plan is made of
what is to be found out.

### 2. Across sessions, the state lives in files the agent writes: a goal file, a progress log, and a structured list of what is to be done [C among the makers of agents; P as evidence]

Verified at the pages fetched.

- **Three kinds of file, each with its own form.** The vendor's
  prompting guide (undated, current models): "Use structured formats
  for state data", "Use unstructured text for progress notes:
  Freeform progress notes work well for tracking general progress and
  context", "Use git for state tracking: Git provides a log of what's
  been done and checkpoints that can be restored". For research
  specifically it suggests the prompt: "develop several competing
  hypotheses. Track your confidence levels in your progress notes ...
  Update a hypothesis tree or research notes file to persist
  information and provide transparency."
- **The harness for long-running work** (Anthropic, 2025-11-26)
  keeps a feature list in JSON ("a comprehensive file of feature
  requirements expanding on the user's initial prompt"), a progress
  file, a start-up script and git. The first session is different in
  kind: an initializer "asks the model to set up the initial
  environment"; every later session is asked "to make incremental
  progress, then leave structured updates", and begins by reading:
  "Read the git logs and progress files to get up to speed". The
  authors expect the pattern to carry beyond code: "some or all of
  these lessons can be applied to ... scientific research or
  financial modeling."
- **The scientific-computing account** (Anthropic, 2026-03-23) names
  two files. The instruction file holds "the overall plan" and the
  project's deliverables. The progress file is "the agent's portable
  long-term memory, acting as a sort of lab notes", tracking "current
  status, completed tasks, failed approaches and why they didn't
  work, accuracy tables at key checkpoints, and known limitations",
  with the remark that "The failed approaches are important - without
  them, successive sessions will re-attempt the same dead ends."
- **The memory tool** (documentation, undated) makes the same
  pattern a default instruction: "ALWAYS VIEW YOUR MEMORY DIRECTORY
  BEFORE DOING ANYTHING ELSE", "As you make progress, record status /
  progress / thoughts etc in your memory", "ASSUME INTERRUPTION". Its
  multi-session pattern says to "set up memory files deliberately
  instead of writing them ad hoc as work progresses".
- **Context engineering** (Anthropic, 2025-09-29): "Structured
  note-taking, or agentic memory, is a technique where the agent
  regularly writes notes persisted to memory outside of the context
  window"; "Like Claude Code creating a to-do list, or your custom
  agent maintaining a NOTES.md file".
- **Another builder agrees.** Manus (2025-07-18): "we treat the file
  system as the ultimate context ... unlimited in size, persistent by
  nature, and directly operable by the agent itself"; "By constantly
  rewriting the todo list, Manus is reciting its objectives into the
  end of the context"; and compression is kept "restorable", for
  instance "the content of a web page can be dropped from the context
  as long as the URL is preserved". LangChain's Deep Agents names the
  same parts: planning, a "Filesystem", "Sub-agents" and "Persistent
  memory" (README, undated).
- **Claude Code's own memory** keeps an index and topic files: "a
  `MEMORY.md` index and one topic file per memory", loaded by the
  index and read on demand; it is "machine-local" and "not shared
  across machines" (documentation, undated). It is a memory of the
  collaboration, not of a project's substance.

The makers agree on the shape; none of the texts read reports a
controlled comparison of it against another shape. The evidence is
their own experience.

### 3. The chat products keep sources apart from outputs, but most give the working files no durable home [P]

Verified at the pages fetched.

- **Claude's file creation** makes "Excel spreadsheets (.xlsx),
  PowerPoint presentations (.pptx), Word documents (.docx), and PDF
  files" in "a sandboxed computing environment"; "You can download
  the files Claude creates or save them directly to Google Drive".
  The extraction of the page adds that files stay available within a
  conversation and are not persisted across separate conversations
  (page updated 2026-08-06; that sentence is the tool's paraphrase,
  not a quotation).
- **Claude Projects** are "self-contained workspaces with their own
  chat histories and knowledge bases"; the page read says nothing on
  whether generated outputs return to the project's knowledge.
- **Cowork** is the surface with a real working directory: "Claude
  can only read and write files in folders you've connected";
  projects have "their own files, links, instructions, and memory".
  Its plugins bundle "the skills, connectors, slash commands, and
  sub-agents for a specific job function" (repository README,
  undated); the README read prescribes no layout for working files.
- **Notebook tools ground answers in a closed set of sources.**
  Google's notebook product answers with "clear in-line citations"
  from uploaded sources and generates briefings, audio overviews,
  mind maps, slide decks and reports from them (help page, 2026; the
  extraction called the product "Gemini Notebook", a name not
  checked). Microsoft's Copilot Notebooks: "only uses the references
  you've added to the notebook to generate responses", and references
  "update in real-time as your project evolves" (support page,
  undated). The two differ on one point that matters here: one page
  describes sources as a set the answers are grounded in, the other
  as live references that change under the work.
- **Provenance** in all of these is the citation from a sentence of
  the output to a source. The vendor's research system does it as a
  separate pass: a citation agent "processes the documents and
  research report to identify specific locations for citations".

This note's synthesis: the products separate what came in (sources,
references, knowledge) from what was generated, as the forge does.
Between the two they have nothing: no kind for a file that is
neither an input nor a finished output. Where a durable place for
such files exists (Cowork, Claude Code, the agent harnesses), it is
a plain directory under the user's control, and its order is left to
the user or to a prompt.

### 4. Outside AI, the practices that handle open-ended work all fix three things: raw inputs immutable, derived things regenerable, and a dated log of what was done [C]

Verified at the pages fetched unless marked.

- **Raw is immutable.** Cookiecutter Data Science: "Raw data must be
  treated as immutable - it's okay to read and copy raw data to
  manipulate it into new outputs, but never okay to change it in
  place"; "Don't ever edit your raw data, especially not manually,
  and especially not in Excel." Wilson et al. (2017): "Where
  possible, save data as originally generated".
- **Derived is kept apart and can be made again.** The same template
  moves data from `raw` and `external` through `interim` to
  `processed` and asks to "Treat your data analysis pipeline as a
  directed acyclic graph". Wilson et al.: "Put raw data and metadata
  in a data directory and files generated during cleanup and analysis
  in a results directory", and "Create the data set you wish you had
  received". The research compendium, in rOpenSci's guide, is "both a
  container for the different elements that make up the document and
  its computations ... and ... a means for distributing, managing and
  updating the collection"; the guide's conventions, as the tool
  summarised them, are raw data kept apart and unchanged and outputs
  treated as disposable because they can be regenerated. The paper
  that states these principles (Marwick, Boettiger and Mullen, 2018)
  refused the fetch; its three principles of conventional
  organisation, separation of data, method and output, and a stated
  computational environment are unverified, from memory.
- **Hand-editing an intermediate file is the named fault.** Noble
  (2009) asks to avoid editing intermediate files by hand and to
  record every step in a driver script or a README, under one
  principle: "Someone unfamiliar with your project should be able to
  look at your computer files and understand in detail what you did
  and why."
- **A chronological notebook stands beside the files.** Noble: a
  dated document in the results directory with entries on what was
  done, what was seen, conclusions and next steps, and result
  directories named by date, because a purely logical naming stops
  making sense as the project's scope moves. Wilson et al.: "Add a
  file called CHANGELOG.txt to the project's docs subfolder". The
  agent builders arrived at the same file (finding 2: "a sort of lab
  notes").
- **Audit working papers**, secondary sources only (search summaries
  of pages on ISA 230; the standard itself and the US counterpart
  refused the fetch): the file must let an experienced auditor with
  no previous connection to the engagement understand what was done,
  what evidence was obtained and what was concluded; the final file
  is assembled within a stated time after the report (60 days is the
  figure given), and after assembly nothing is deleted or discarded
  before the retention period ends. That each paper carries who
  prepared it, when, from what source, who reviewed it and a
  cross-reference to the papers it supports is unverified, from
  memory. The model matters here because audit papers are largely
  hand-made working files, not regenerable outputs: their discipline
  is the label and the reference, not reproducibility.

### 5. When the form of the result is open, established practice starts from a written question and a tree of sub-questions, and states a provisional answer early [C in consulting practice, secondary sources; the mapping to the forge is this note's]

Secondary sources only; the primary page (McKinsey's own article on
its seven steps) timed out.

- A practitioner's page on the consulting firms' method (Slideworks,
  updated 2024-11-19) gives seven steps: "Define problem - What key
  question do we need to answer?", "Structure problem", "Prioritize
  issues", "Develop issue analysis/work plan - Where and how should
  we spend our time?", "Conduct analyses", "Synthesize findings",
  "Develop recommendations". The deliverable appears in the last
  step; the first four produce a question, a tree and a plan.
- The **problem statement worksheet** on that page holds: the main
  question, the context, the success criteria, "Scope and
  Constraints: Define what's included and what's not", the
  stakeholders, and the key sources of insight.
- The **issue tree** breaks the question into sub-questions; the
  **work plan** names for each issue the analysis, the source of
  data, the timing and who does it.
- The **early answer**: the same page asks to write down, at the
  start, the three to seven actions one expects to come out of the
  work; a search summary calls this the "Day 1 answer", a best
  hypothesis stated at once and revised as the evidence arrives.
- For strategy in particular, search summaries of Rumelt's *Good
  Strategy/Bad Strategy* give the "kernel": a diagnosis of the
  challenge, a guiding policy, and coherent actions (search result
  only; the book was not read).
- The Double Diamond's first diamond, discover then define, is the
  same order in design; see the elicitation note, finding 9.

This note's synthesis: the "map of what must be found" does not
vanish when the artefact is unknown. It changes its material. For a
known artefact the map is the areas the document must cover; for
open work it is the question, its boundaries, and the tree of
sub-questions with a state for each. It is found in the first phase
of the work and is itself revised; and every practice read makes the
framing statement nearly identical: the question, why it is asked,
for whom, by what one will know it is answered, and what is outside.
The elicitation note found the same for a research interviewer: a
plan drafted by the AI and reviewed by a human before any interview
(its finding 5).

### 6. Binary and tabular files under git: storing them works, comparing and merging them does not; the working practice is a text twin or a regenerating script [C]

Verified at the pages fetched.

- **Git can show a text view of a binary and cannot merge through
  it.** Git's documentation: "a word processor document can be
  converted to an ASCII text representation, and the diff of the text
  shown"; but "diffs generated by textconv are _not_ suitable for
  applying", and only the diff and log commands use the conversion.
- **A workbook is opaque to git.** "For Git, Excel workbooks are just
  binary files. This means they cannot be diffed via `git diff`"
  (xltrail, 2018-01-04). Wilson et al.: for office files and PDFs "It
  is not possible to pinpoint specific changes from 1 version to the
  next". Tools exist that diff or even merge workbooks cell by cell
  (Git XL, xlgit, xltrail: search results only, not tested and not
  read at source).
- **Size.** GitHub warns above 50 MiB and "blocks files larger than
  100 MiB"; it recommends repositories "ideally less than 1 GB". Git
  LFS "replaces large files ... with text pointers inside Git, while
  storing the file contents on a remote server". DVC keeps a small
  `.dvc` file as "a placeholder for the original data for the purpose
  of Git tracking" and describes pipelines with their dependencies
  and outputs so that derived data can be reproduced. The Turing Way
  (2024) lists DVC, Git LFS, git-annex, git submodules and DataLad,
  and names the costs of large files in git: slow clones, hosting
  limits, and the tedium of purging a file added by mistake.
- **Keep generated data out of version control, or decide it
  knowingly.** Cookiecutter Data Science ignores its `data/` folder
  by default. Wilson et al.: "Version control systems are not
  designed to handle megabyte-sized files".
- **Plain text beside the spreadsheet.** Broman and Woo's paper on
  data in spreadsheets refused the fetch; its recommendations (no
  calculations in the raw data file, no meaning carried by colour,
  data saved as plain text such as CSV) are unverified, from memory.
  Wilson et al. give the two accepted routes for a manuscript, which
  apply to any hand-edited document: an online tool with change
  tracking, or "a plain text format that permits version control".

What follows for small working files, this note's own reading: the
size machinery (LFS, DVC) answers a problem the forge's projects
mostly do not have. The problems they do have are the other two:
nobody can see what changed in a workbook between two commits, and
two people cannot both change it. No source read offers a cure
inside git for a hand-edited binary; the practices either generate
the binary from text or keep a text twin beside it.

### 7. What is known to fail [C unless marked]

| Failure | Where it is described |
|---|---|
| Doing everything at once in one sitting | "the agent tended to try to do too much at once - essentially to attempt to one-shot the app" (Anthropic, 2025-11-26) |
| Declaring the work done because some progress is visible | "a later agent instance would look around, see that progress had been made, and declare the job done" (same) |
| Leaving the state undocumented at the end of a session | same; answered by the progress file and the end-of-session update |
| Walking the same dead end again | "without them, successive sessions will re-attempt the same dead ends" (Anthropic, 2026-03-23); answered by recording failed approaches |
| Searching without end, or stopping short | "agents continuing when they already had sufficient results", "scouring the web endlessly for nonexistent sources" (Anthropic, 2025-06-13); "agentic laziness" (2026-03-23) |
| Memory files written ad hoc | the memory tool's page asks for files set up "deliberately instead of writing them ad hoc", and for a prompt against clutter: "Do not create new files unless necessary" |
| Raw inputs changed in place | Cookiecutter Data Science; Wilson et al. |
| Intermediate files edited by hand, so nobody can repeat the step | Noble (2009) |
| Directory names that stop meaning anything as the scope moves | Noble (2009), answered by dated directories and a notebook |
| Binary files whose changes cannot be seen or merged | git documentation; xltrail; Wilson et al. |
| Outputs made in a chat sandbox that do not outlive the conversation **[P]** | Claude file creation, as extracted (finding 3) |
| One workflow for work of every size **[E]** | the layers note, finding 10 |

Looked for and not found: a study measuring "aimless sessions" in
open-ended work with an AI, or comparing a framed start against an
unframed one. The failures above are builders' reports and
practitioners' rules.

## Options and trade-offs

The options are the four the question names. They are not exclusive;
the first two answer "work without a known artefact", the third
answers "working files", the fourth answers both by declining.

**A. A general artefact with a general elicitor whose first output
is the map itself.** A definition for "open work": its first round
finds the question, the reason, the boundaries, what would count as
an answer, and the tree of sub-questions; later rounds work the tree.
*For:* this is what every practice read does (findings 1 and 5); it
answers the brief's named price directly, since the map is found
rather than given; a state per sub-question gives the declared
completion the elicitation note asks for.
*Against:* the forge already has a document of this kind. The intent
holds positions, facts, rejections and, in its threads, open
questions with what it would take to decide them; a second document
of the same material would break "one mechanism lives in one place".
The honest form of option A may be a framing of the intent for open
work rather than a new artefact. What the intent's definition lacks
for that is small and is listed under Relevance.

**B. A workspace kind of project: core functions, no chain.** A
third project kind beside `thought` and `library`: ledger, sources,
research, a log, and free working space.
*For:* cheapest; matches Cowork and the agent harnesses, where the
structure is a directory, an instruction file and a progress file
(findings 2 and 3); nothing has to be decided about the form of the
result.
*Against:* it drops exactly what the brief asks to keep, the
elicitation, since without a definition there is no map and no
completion; the tools that work this way leave the order of the
directory to the user (finding 3), which is the "pile of files" the
question fears; and a library already is a project with no chain, so
the new kind must say how it differs.

**C. A document kind for working files, beside source and render.**
One new kind with its own rules: made and changed during the work,
by the principal or by Claude, in any format; registered so that it
is not an orphan; with a note of what it is, what it was made from
and what uses it.
*For:* fills the gap every surveyed product also has (finding 3);
the outside practice gives the rules ready made (findings 4 and 6):
a source stays immutable and a working file is a copy of it, never
the source changed in place; a file that a script or a recipe
produces is derived and may be overwritten; a file edited by hand is
labelled and logged, with a text twin where its content must be
citable or comparable; it holds whatever state it is in and is never
a source of truth for a position.
*Against:* a new kind, a new directory and probably a new ledger
table, each a convention to keep; the line between a working file,
a render and a later artefact needs a rule that holds in practice
(authorship is the existing rule and may be enough); binary files
under git stay undiffable whatever the kind is called, so the rule
buys order and traceability, not comparison.

**D. Leave such work to a separate tool.** Strategy work and its
spreadsheets go to Cowork, a notebook tool or plain Claude Code; the
forge takes over once there is an idea for the chain.
*For:* no new convention; in line with the principal's recorded word
against one tool that does everything (the brief, "The shape of the
whole"); those tools are good at making office files.
*Against:* the brief says what is wanted is the forge's core
(ingest, research, logs, history, elicitation), and none of the
tools read has an elicitation with a map, a history of changes with
reasons, or a rule for sources; chat-side files may not outlive a
conversation (finding 3); and the second need, working files in
today's projects, remains whatever is decided about the first.

## What was not found

- A product or framework that frames work whose result is several
  things of unknown kind. All end in a report or in code.
- A named kind, in any tool read, for a file between an input and a
  finished output.
- A controlled study of open-ended work with an AI that compares a
  framed start with an unframed one, or one layout of state files
  with another.
- A way to merge hand-edited office files inside git that a primary
  source vouches for.
- Not readable in this session, and therefore used only as marked:
  the ChatGPT help pages on deep research and on projects (refused);
  McKinsey's article on the seven steps (timed out); Marwick,
  Boettiger and Mullen 2018 and Broman and Woo 2018 (refused); PCAOB
  AS 1215 (refused); ISA 230 at the standard setter's site (not
  found) and two secondary pages on it (refused, not found).
- Not surveyed: Perplexity's workspaces, Notion-like tools,
  qualitative-research software, and the records-management
  standards. A further pass could add them; see the closing remark.

## Relevance to this project

**The forge is closer to open work than the brief assumes.** This is
this note's reading of the forge's own files, to be checked by the
principal. Of the three artefacts only the assignment is tied to a
form of result. The brief is "what the principal wants and why". The
intent's Map (`.claude/skills/forge/states/intent.md`) is already a
map of open work: the essence, the weight of every idea, the ground,
what is open and "what it would take to decide it", reality. Its
items are the outside world's working set under other names: THR is
the issue tree, POS the answers so far, FCT the evidence, REJ the
failed approaches that finding 2 calls the most important thing to
record. The ledger header's `terminal:` already lets a chain end
above the assignment. A strategy worked as brief, then intent with
`terminal: intent`, with research notes and sources, is possible
today; what comes out of it for others would be renders.

What is missing against the practices read:

1. **The first-round framing as a stated part of the Map**: the
   question, by what one will know it is answered, and the tree of
   sub-questions as the thing the first round finds (finding 5). The
   brief's "a general elicitor has no map" is answered by every
   source the same way: the map is the first thing found, and it is
   confirmed by the owner before the work runs (finding 1).
2. **A provisional answer stated early** and revised (finding 5).
   The forge has "draft early"; whether an early answer to the whole
   question belongs in the intent, and where, is the principal's.
3. **A place and a rule for working files** (findings 3, 4, 6). This
   holds for every project, as the brief says.
4. **A home for several outputs.** Today these are renders, each
   with a recipe. That fits outputs generated from the intent. It
   does not fit an output the principal composes or edits by hand,
   which by the forge's own boundary of authorship is an artefact;
   THR.0360 already holds this question (the layer with an external
   audience, the document polished in an editor and the way back),
   and this note adds nothing that decides it.

**Recommendation.** Three proposals for the principal, each his to
take or leave, to be worked in the brief `next-gen` and then through
`/forge intent`; findings and options, not a design.

1. **For work without a known artefact: option A in its small form,
   not a new artefact.** Treat open work as a thought project whose
   chain ends at the intent, and extend the intent's definition for
   that case with the framing of finding 5 as the first round's
   aim: the question, why, the boundaries, what would count as
   answered, the sub-questions as threads with a state each. Reason:
   the practices agree on this shape, the forge has the parts, and a
   second general artefact would restate the intent. The cost to
   name: the intent of such a project is long-lived and carries more
   threads than positions for a long time, and the forge has not run
   one; one real trial (the strategy the brief names) before any
   rule is written would show what breaks.
2. **For working files: option C, with the smallest rule set the
   outside practice supports.** A kind for files made and changed
   during the work, in a directory of their own, catalogued like the
   resources (what it is, what it was made from, what uses it), with
   four rules taken from findings 4 and 6: a source is never changed
   in place, a working file is a copy; a generated file names what
   generates it and may be overwritten; a hand-edited file is
   logged when it changes in substance, and a text twin (CSV or
   Markdown) is kept where its content is cited by a position or
   must be compared; a working file is never the source of truth for
   a position, which is cited into the intent as a fact with its
   path. Open and the principal's: the name of the kind, whether it
   has a ledger table or only an index, and whether data that can be
   regenerated is tracked in git at all.
3. **Not option B and not option D as the answer.** B gives the
   directory and drops the elicitation; D leaves the second need
   unanswered. D remains the right answer for one part: making the
   office files themselves is the separate tools' strength, and the
   forge already calls them through `/publish`.

One question to put to the principal before any of this, since the
recommendation rests on it: is the outcome of the strategy work
something he will hold (positions he can state and defend), with
documents for others made from it, or is it a set of documents he
composes by hand along the way? In the first case proposal 1 fits as
it stands; in the second the weight moves to THR.0360 and to
proposal 2.

Whether more research would change this: on the framing of open work
and on raw, derived and output, the sources agree and more reading
is unlikely to move the recommendation. Two things could: a closer
look at what the principal's own spreadsheets are (data, a model, or
a document in tabular form), which is a question for him and not for
the web; and the unread primary sources on audit working papers, if
the rule for hand-made working files is to be written in detail.

## Sources

All fetched 2026-10-03.

**Agentic tools and vendor guidance**

- How we built our multi-agent research system - https://www.anthropic.com/engineering/multi-agent-research-system - Anthropic, 2025-06-13
- Effective context engineering for AI agents - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents - Anthropic, 2025-09-29
- Effective harnesses for long-running agents - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents - Anthropic, 2025-11-26
- Long-running Claude for scientific computing - https://www.anthropic.com/research/long-running-Claude - Anthropic, 2026-03-23
- Memory tool - https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool - Anthropic documentation, undated (read as full Markdown)
- Prompting best practices - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices - Anthropic documentation, undated (read as full Markdown; reached by redirect from the page `claude-4-best-practices`)
- How Claude remembers your project - https://code.claude.com/docs/en/memory - Claude Code documentation, undated (read as full Markdown)
- Common workflows - https://code.claude.com/docs/en/common-workflows - Claude Code documentation, undated (read as full Markdown)
- Choose a permission mode (plan mode) - https://code.claude.com/docs/en/permission-modes - Claude Code documentation, undated (one sentence read)
- Get started with Cowork - https://support.claude.com/en/articles/13345190-get-started-with-cowork - Anthropic help centre, "updated this week"
- Create and edit files with Claude - https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude - Anthropic help centre, updated 2026-08-06
- What are projects? - https://support.claude.com/en/articles/9517075-what-are-projects - Anthropic help centre, "updated over a week ago"
- Using Research on Claude - https://support.claude.com/en/articles/11088861-using-research-on-claude - Anthropic help centre, updated 2026-06-02
- knowledge-work-plugins, README - https://github.com/anthropics/knowledge-work-plugins - Anthropic, undated
- Gemini Deep Research, help page - https://support.google.com/gemini/answer/15719111 - Google, undated (2026)
- Google's notebook product, help page - https://support.google.com/notebooklm/answer/16164461 - Google, undated (2026)
- How Microsoft 365 Copilot Notebooks works - https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works - Microsoft, undated
- Context Engineering for AI Agents: Lessons from Building Manus - https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus - Manus, 2025-07-18
- langchain-ai/open_deep_research, README - https://github.com/langchain-ai/open_deep_research - archived 2026-08-21
- langchain-ai/deepagents, README - https://github.com/langchain-ai/deepagents - undated
- assafelovic/gpt-researcher, README - https://github.com/assafelovic/gpt-researcher - undated
- stanford-oval/storm, README - https://github.com/stanford-oval/storm - undated
- ChatGPT Deep Research review - https://www.buildfastwithai.com/ai-tools/chatgpt-deep-research - Build Fast with AI, 2026 (weak source; read, not cited in a finding)

**Established practice**

- Cookiecutter Data Science, Opinions - https://cookiecutter-data-science.drivendata.org/opinions/ - DrivenData, undated
- G. Wilson et al., Good enough practices in scientific computing - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510 - PLOS Computational Biology, 2017
- W. S. Noble, A Quick Guide to Organizing Computational Biology Projects - https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424 - PLOS Computational Biology, 2009
- rOpenSci, rrrpkg: use of an R package to facilitate reproducible research - https://github.com/ropensci/rrrpkg - undated
- Research Compendium - https://research-compendium.science/ - undated
- BCG and McKinsey problem solving process - https://slideworks.io/resources/mckinsey-problem-solving-process - Slideworks, updated 2024-11-19 (secondary)

**Binary and large files under git**

- gitattributes - https://git-scm.com/docs/gitattributes - Git documentation, undated
- About large files on GitHub - https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github - GitHub, undated
- Git Large File Storage - https://git-lfs.com/ - undated
- Get Started with DVC - https://doc.dvc.org/start - DVC, undated
- The Turing Way, Version Control for Data - https://book.the-turing-way.org/reproducible-research/vcs/vcs-data - 2024
- Integrating Git with Spreadsheet Compare - https://www.xltrail.com/blog/git-diff-spreadsheetcompare - xltrail, updated 2018-01-04

**Search results only** (summaries returned by the search tool; the
pages were not opened or refused; used only where the text says so)

- ChatGPT help centre, Deep research in ChatGPT - https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt - refused the fetch
- Pages on ISA 230 audit documentation, among them https://www.learnsignal.com/blog/isa-230-audit-documentation-guide/ - refused the fetch
- Summaries of R. Rumelt, *Good Strategy/Bad Strategy*, among them https://concepts.dsebastien.net/concept/kernel-of-good-strategy/
- Workbook diff and merge tools: https://pypi.org/project/xlgit/ and Git XL
- Summaries of LangChain's Open Deep Research and Deep Agents

**Tried and not readable** (nothing is cited from these)

- McKinsey, How to master the seven-step problem-solving process: timed out.
- B. Marwick, C. Boettiger, L. Mullen, Packaging Data Analytical Work Reproducibly Using R (and Friends), The American Statistician, 2018: refused.
- K. Broman, K. Woo, Data Organization in Spreadsheets, The American Statistician, 2018: refused.
- PCAOB AS 1215, Audit Documentation: refused.
- IAASB, ISA 230: page not found.
- ChatGPT help centre, Projects in ChatGPT: refused.
