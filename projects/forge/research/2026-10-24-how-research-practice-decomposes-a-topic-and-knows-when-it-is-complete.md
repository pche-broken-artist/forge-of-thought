---
date: 2026-10-24
project: forge
topic: how research practice decomposes a topic into questions and knows when it is complete
status: immutable
derived_from: the principal's word of 2026-10-24 (the /research command to show a plan before searching: the topic split into questions, one agent per question, the plan decides the quality); .claude/skills/research/SKILL.md; research/2026-10-23-a-reviewer-or-a-question-on-another-model-inside-the-forge.md; web sources below
---

# How research practice decomposes a topic into questions and knows when it is complete

## Question

How does established research and review practice outside AI turn a
topic into researchable questions, build a search strategy from
them, and judge when the picture is complete: systematic and scoping
reviews (Cochrane, JBI, PRISMA), question frameworks (PICO and its
relatives, question hierarchies), search construction (concept
blocks, vocabulary, grey literature), snowballing, saturation and
stopping rules, the protocol registered before searching, the known
failures (too narrow, too broad, confirmation bias in the search),
and the way analysts and consultants (key intelligence topics,
analysis of competing hypotheses, issue trees) break a client's
question into sub-questions and assign them.

The baseline it must beat is the current `/research` skill: one
topic, Claude searches, one note; a topic found to be several
questions becomes several notes after the fact. No plan is shown
before the search, nothing says what would make the research
complete, and the splitting is discovered, not designed.

## Key findings

**F1. The question is framed before anything is searched, in a
fixed frame chosen for the kind of question; the frames are many,
the evidence that any one is better is thin.** [consensus on the
practice; single source on the comparison] Cochrane states the
question in PICO (population, intervention, comparison, outcome),
requires it to be feasible, interesting, novel, ethical and relevant
(FINER), and distinguishes three PICO levels: the review PICO set
at protocol stage, the PICO of each planned comparison, and the
PICO of the studies found [1, 2.1 and 2.3]. JBI frames a scoping
review as PCC (population, concept, context), the title, the
question and the inclusion criteria kept congruent, a primary
question optionally followed by sub-questions on "differing
conceptual foci" [4, 5]. Qualitative, service and policy questions
have PEO, SPIDER, SPICE and ECLIPSE; library guides count at least
25 frames beyond PICO [6]. Cooper's review of nine guidance
documents found that five of them make the question decide which
concepts are searched [9]. The one head-to-head test (Methley 2014)
found PICO more sensitive and SPIDER more specific, recommended PICO
for a comprehensive search and PICOS where time is short, and
advised against SPIDER because it misses papers [7]. Booth's
methodological review concludes that "poor empirical evidence
underpins current information practice" [8]. The frame's value is
that it forces the question's parts to be named before the search,
not that one frame is proven.

**F2. Scope is a continuum; the default when in doubt is broad,
then split, and a too narrow question is the more common error.**
[consensus within Cochrane] The Handbook's table of advantages and
disadvantages lists for a narrow scope: sparse evidence, no way to
explore differential effects, and that "scope could be chosen by
review authors to produce a desired result" [1, Table 2.3.a]. EPOC's
guidance says review authors "often propose an overly narrow focus"
that is in effect "a subgroup analysis of a broader question", with
five consequences: a high risk of an empty review, misleading
conclusions from sparse evidence, results not interpretable against
the whole evidence, no compelling reason why the same intervention
would act differently elsewhere, and overlapping reviews that
duplicate work. The good reasons for narrowing are two: the thing
is only relevant in one population or setting, or there are
compelling reasons it would function differently there. Interest,
manageability and readability "by themselves do not adequately
justify" a narrow question. "When in doubt, it is probably wiser to
start with a broad scope, and divide the review up into narrower
reviews if the original review becomes unwieldy", each part then
with its own protocol [3]. Lumping and splitting are a continuum
decided per comparison, not a binary, and the Handbook names logic
models (a drawn theory of how the thing works) as a tool for
"refining review questions" and "deciding on lumping or splitting"
[1, 2.3.2 and 2.5.1].

**F3. Decomposition exists because of working memory, and every
tradition caps the number of parts at about seven.** [consensus on
the principle; the numbers are heuristics] Heuer's chapter on
structuring analytical problems grounds decomposition and
externalisation (getting the problem onto paper) in Miller's
"magical number seven, plus or minus two", and shows that the
relations between variables grow geometrically: four variables have
six, eight have twenty-eight [25]. On hypotheses he writes: "There
is no 'correct' number of hypotheses to be considered ... More than
seven hypotheses may be unmanageable; if there are this many
alternatives, it may be advisable to group several of them together
for your initial cut" [25]. Cochrane's search guidance says
strategies "should avoid using too many different search concepts"
and that a typical strategy has three concept sets (population,
intervention, study design) with many synonyms inside each [2, Key
Points and 4.4.2]. Consulting practice stops an issue tree at two to
three levels below the root, where a leaf is "something a single
person could go measure or investigate directly this week"; deeper
is "organizing information rather than structuring a decision" [30,
single practitioner source]. Cochrane's rapid review guidance tells
the team to "limit the number of interventions and comparators" and
"limit the number of outcomes, with a focus on those most important
for decision-making" [22]. The shared rule across fields: few
parts, each rich inside, grouped rather than multiplied when they
exceed what one head holds.

**F4. The shapes of decomposition differ, but a sub-question always
has the same anatomy: one kind of evidence, one kind of source, an
owner, and a reason it matters to the decision.** [consensus across
practitioner traditions; each shape a single tradition's]
- *Business research hierarchy* (Cooper and Schindler): management
  dilemma, management question, research question(s), investigative
  questions ("the questions that must be answered before the
  research question can be resolved"), measurement questions [31,
  secondary].
- *Issue tree and hypothesis tree* (McKinsey tradition): a governing
  question split MECE (mutually exclusive, collectively exhaustive;
  check sibling branches for overlap, ask "what is missing"), then
  only the high-priority leaves turned into hypotheses with "the
  evidence that would prove or kill it" [30]. The work plan lists
  per issue: the hypothesis, the analyses in priority order, the
  data and its likely source, the end product, the person
  responsible, the due date; the hypothesis is revised as facts
  come in, "the goal is the right answer, not to prove the first
  guess" [32, secondary].
- *Key intelligence topics* (Herring 1999): the decision maker's
  needs are elicited and sorted into three categories, strategic
  decisions and actions, early warning, and the key players; the
  aim is "intelligence that management feels compelled to act
  upon"; practice then opens each topic into key intelligence
  questions [27, 28]. Military doctrine does the same with priority
  intelligence requirements broken into indicators and specific
  information requirements that drive a collection plan, and
  prioritises every indicator because collection capacity is
  always smaller than the requirements [29, secondary].
- *Fermi-ization* (Tetlock): "decompose the problem into its
  knowable and unknowable parts", and triage first: no effort on
  "clocklike" questions a rule of thumb answers or on "cloud-like"
  ones nothing answers [33].
- *Issue redefinition* (Heuer and Pherson): before decomposing,
  rephrase the question, ask why, broaden it, narrow it, take the
  opposite view, to see whether the question as posed is the one to
  answer [26, secondary description of the technique].

**F5. The question is tested by a limited scoping search before the
strategy is built, and the first thing looked for is whether the
answer already exists.** [consensus] Cooper's review finds two
preparatory tasks in the guidance: checking for existing or ongoing
reviews (registries such as PROSPERO) and an initial search "to
estimate the volume of relevant literature", which "should be
undertaken before the actual search strategy is developed" [9]. JBI
prescribes a three-step search for every review type: a limited
search of at least two databases, analysis of the text words and
index terms of what it returns, a second full search with all the
terms in all sources, then the reference lists of what was included;
the search "may be iterative as reviewers become more familiar with
the evidence base" [4, 5]. Cochrane's "novel" criterion is the same
check for related or overlapping reviews [1, 2.1]. For web research
the translation is direct: the first item of any plan is "has
someone already synthesised this, and in what words does the field
talk about it", and the vocabulary found there feeds the other
questions.

**F6. A search strategy is built as concept blocks, favours
sensitivity, uses several sources because no single one is enough,
and is peer reviewed and documented before it runs.** [consensus]
Terms are combined "with the OR Boolean operator to achieve
sensitivity within concepts" and the concepts with AND; both
controlled vocabulary and free text are used; searches "should seek
to maximize sensitivity whilst striving for reasonable precision";
NOT is avoided; no language limits and no arbitrary date limits;
"a search of MEDLINE alone is not considered adequate" and
"searching two or more databases lowers the risk of missing eligible
studies" [2]. Bramer measured it on 58 reviews: Embase alone found
85.9 percent of the included references, MEDLINE 78.8, Web of
Science 68.1, Google Scholar 34.4; the four together 98.3, and
Google Scholar, poor alone, added 13 percent of references found
nowhere else "possibly because it indexes full text" [10]. Beyond
databases the guidance names trial registers, grey literature
(reports, theses, conference abstracts), previous reviews on the
topic, reference lists of included studies, citation searching and
contacting people [2, 4.3]. "All search strategies should be peer
reviewed, before being run" with the PRESS checklist, which checks
the logic (orphan lines, wrong operators, limits that do not fit the
question) as much as the spelling [2, 4.2.2 and 4.4.8; 23]. The
search is documented so that it is reproducible, strategies copied
not retyped, decisions and correspondence recorded, in the sixteen
items of PRISMA-S [2, 4.5; 17]. For a web search the equivalents
are: several engines or source kinds per question, a query written
in the field's vocabulary and in plain words, and the queries kept
in the note.

**F7. Snowballing finds what databases miss; how much depends on
the topic, so it is planned as a supplement with a stated reason,
and every round is reported with the reason it stopped.**
[consensus that it is supplementary; the yield is contested]
Greenhalgh and Peacock audited the 495 sources of a review of
complex evidence: 30 percent came from the protocol-driven search
(25 percent databases, 5 percent hand search), 51 percent from
snowballing (44 percent reference tracking, 7 percent citation
tracking), 24 percent from personal knowledge and contacts; their
conclusion: "systematic reviews of complex evidence cannot rely
solely on protocol-driven search strategies" [11]. Wohlin's
guidelines run snowballing from a start set, backward through
reference lists and forward through citing papers, iterating until
no new paper is found, and found it a viable first strategy; the
later hybrid (database search plus snowballing) found 30 percent
more primary studies than either alone [12, 13]. The counter-case
is Wright 2014: citation searching on 40 included studies found nine
eligible ones, eight already found by the databases, one unique,
199 records read per hit, "may not be the best use of valuable time
and resources" [14]. The TARCiS consensus (27 methodologists, four
Delphi rounds) settles it by topic: for "difficult-to-search-for"
topics backward and forward citation searching "should be seriously
considered"; for easy topics covered by a sensitive search it is
"not explicitly recommended" and reference-list checking serves to
confirm the search's sensitivity; seeds are all included records;
if a round finds new eligible records, run another with them as
seeds; report the seeds, the direction, the dates, the number of
iterations "and the reason for stopping if the last round still
found eligible records" [15, 16]. Cochrane adds a diagnostic: if
citation searching finds many new records, "this may suggest that
the original searches were not optimal and should be revisited"
[2, 4.4.11]. A topic whose vocabulary is unsettled, which is the
normal case for the forge's topics, is the difficult-to-search kind.

**F8. There is no objective stopping rule; the field has eight
methods, uses two or three, and requires the reviewer to say why
searching ended.** [consensus that it is judgement; the methods
emerging or contested] Cochrane: "it is often difficult to decide
in a scientific or objective way when a search is complete"; the
suggestions are to stop "if adding in a series of new terms to a
database search strategy yields no new relevant records", and to
treat a missing PRESS dimension as a sign the search is not done
[2, 4.4.11]. Booth's review of the stopping literature lists eight
methods: capture-recapture, feedback from the commissioner, seeking
the disconfirming case, comparison against a known gold standard,
retrieval of known items, the law of diminishing returns, a priori
stopping rules, and theoretical saturation; "few have been formally
evaluated" [18]. Cooper found only one of nine guidance documents
(Petticrew and Roberts) says anything about when to stop, and that
how much searching is needed "remains unclear" [9]. In qualitative
synthesis Booth reports: no number of studies can be fixed in
advance because richness matters; reviewers "must explain why
searching ended"; the thresholds practitioners use are "the next
twenty papers offer nothing new" or two late finds that "did not
add anything new to the emerging synthesis"; typical syntheses hold
6 to 14 studies and one author puts about 40 as a practical
maximum; whether past yield predicts future yield "is currently
unknown" [8]. Capture-recapture, the one statistical method,
estimates the missed studies from the overlap between sources, but
one test gave 56 or 1,439 missing depending on the model [19].
Three of the eight methods cost nothing and transfer to any search:
retrieval of known items (did the search find what we already knew
should be there), diminishing returns stated as a rule in advance
(the last N sources added nothing), and the disconfirming case (a
search run to find the opposite).

**F9. Saturation has been measured where it can be: in homogeneous
fields with narrow objectives it arrives early; the number depends
on the purpose and the heterogeneity, and the fuller kind of
saturation takes about twice as long.** [consensus in qualitative
methods; the transfer to sources is a hypothesis of mine] Hennink
and Kaiser's systematic review of 23 empirical tests found
saturation reached within 9 to 17 interviews or 4 to 8 focus
groups, "most likely in studies with relatively homogeneous
populations and narrowly defined objectives"; multi-country work,
meta-themes and meaning saturation needed more [20]. Their primary
study separates code saturation (the range of issues is known,
reached at nine interviews) from meaning saturation (each issue is
understood, 16 to 24 interviews, some codes never) and lists what
moves the number: purpose, population, kind of codes, stability of
the codebook [21]. Malterud's "information power" replaces the
count by five dimensions: aim, sample specificity, use of theory,
quality of dialogue, analysis strategy [20]. Read as an analogy for
sources rather than people: a sub-question answered from one body
of guidance saturates in a handful of sources; one that spans
disciplines, or asks what a thing means rather than what exists,
needs more and should be planned as such.

**F10. A protocol written before the search is the norm; the
evidence says it makes deviation visible rather than preventing
it.** [consensus on the practice; contested on the effect] PRISMA
2020 item 24 requires the registration, where the protocol can be
read, and "describe and explain any amendments"; PRISMA-ScR item 5
asks the same of scoping reviews [17]. JBI makes the a priori
protocol "a distinct characteristic" of its method and allows the
question to change because scoping is iterative, provided
"deviations from the protocol with supporting justification should
be made transparent" [4]. Cochrane allows refinement as evidence
emerges but warns that "data-driven questions can generate false
conclusions based on spurious results" [1, 2.5.2]. The editors of
PLoS Medicine argued registration "helps minimize bias in the
conduct and reporting of the review", reduces duplication, and
makes it "obvious to readers whether there was a prespecified
protocol" [34]. The measurements are sobering: of 96 published
reviews compared with their PROSPERO records, 32 percent had changed
the primary outcome and 39 percent had never named one, with no
link to favourable results [35]; a 2017 study of 284 reviews found
21 percent registered and no association between registration and
less outcome reporting bias [36, seen only through a search
summary]; PROSPERO records themselves meet on average 4.8 of 19
PRISMA-P items [37]. The protocol's worth, then, is the audit
trail: what was planned, what changed, why. That is exactly what a
plan shown before the search and kept in the note gives.

**F11. Confirmation bias enters a search through the wording of
the query and the trail of citations, and the remedy in every
tradition is to search for the disconfirming case on purpose.**
[consensus on the mechanism; emerging on search engines] An audit
of Google Scholar and Semantic Scholar found that queries framed
toward "benefits" or "risks" returned results matching the frame,
more so on Google Scholar and on technology topics [38]. Cochrane
names citation bias: positive results are cited more, so following
reference lists "may produce a biased sample of studies"; Duyx's
meta-analysis confirms the citation advantage of positive results
[39]. Heuer describes the natural procedure as satisficing: pick
the intuitively likely answer, read the evidence for whether it
supports it, "look no further"; most such evidence "is also
consistent with other explanations". His remedy is to list all
reasonable hypotheses, ask of each "if this hypothesis is true,
what should I expect to be seeing or not seeing", score each item
of evidence for diagnosticity (evidence consistent with every
hypothesis has none), and "proceed by trying to disprove the
hypotheses rather than prove them", because consistent evidence
proves nothing and one inconsistent item can refute [25]. The
empirical record on the full ACH procedure is mixed: in a trial
with fifty analysts those trained in it did not follow all its
steps, the evidence that it reduced confirmation bias was mixed,
and it "may have increased judgement inconsistency and error"
[40]; its critics say it does not address how the hypotheses were
formed in the first place [41]. The portable parts are the cheap
ones: neutral query wording, one query per question written to
find the opposite, and the record of what was expected and not
found.

**F12. The bounded form of a review, the rapid review, is the
closest model to a one-person research with a time budget, and its
rules are explicit about what to cut.** [consensus, Cochrane's
guidance] Involve the people who will use the answer "to set and
refine the review question, eligibility criteria, and the outcomes
of interest"; write a protocol with the question and criteria;
limit interventions, comparators and outcomes to those most
important for the decision; date limits only with a justification;
always search the three core databases, add one or two specialised
sources or none, "limit grey literature and supplemental searching"
and do them after screening; have at least one search strategy
peer reviewed [22]. The 2024 update keeps 24 recommendations and
stresses asking first whether a rapid review is appropriate and
taking "a tailored, iterative approach" per review [24]. The cuts
are made at the plan, before searching, by the decision the review
serves, which is the principal's premise in method form.

**F13. Across every tradition the evidence that the structure
improves the outcome is thin; what the structure demonstrably buys
is transparency and an audit trail.** [consensus by absence] Booth
on search practice: "poor empirical evidence" [8]; Cooper: the
eight stages are a consensus of guidance documents, not a tested
model [9]; Thomason on structured analytic techniques: "a lack of
strong empirical evidence" that they debias [41]; Dhami on ACH
[40]. Nobody has shown that a planned research finds more or better
than an unplanned one of the same effort. What the plan reliably
gives is that the reader can see what was asked, where it was
looked for, what was not found and why the search stopped, which
is the condition for criticising it. For a forge whose reviewers
and principal judge the note afterwards, that is the property that
matters.

## Options

**A. A flat plan of few questions, each a card with fixed fields.**
The topic is reframed once (issue redefinition: rephrase, broaden,
narrow, reverse) and split into three to seven sub-questions; each
carries: the question in a frame (what, for whom, in what context,
against what), why it matters to the decision the research serves,
the kind of evidence that would answer it, where to look (source
kinds and engines named), the disconfirming query, and the stop rule
(known items that must turn up, the last N sources adding nothing).
One isolated agent per card, one note per card, then a synthesis
that lays the answers side by side. Pro: the shape of a work plan
(F4) and of a protocol (F10) in one page; bounded by F3; every
field is something the principal can judge before the search. Con:
a flat list hides the dependencies between questions; the first
sub-question (does a synthesis already exist, F5) must run before
the others can be finalised.

**B. An issue tree with hypotheses at the leaves.** The governing
question, two to three MECE levels, each leaf a hypothesis with the
evidence that would kill it; agents at the leaves. Pro: dependencies
visible, consultants' proven shape, the disconfirming search built
in. Con: a hypothesis-first tree carries Heuer's warning (F11) and
the critics' point that it does not say where the hypotheses came
from (F11); for a research meant to find what the world has solved,
leaves without a hypothesis are legitimate, and the practitioner
rule itself leaves exploratory leaves open to "generate hypothesis
candidates" [30]. Heavier to show and to judge than A.

**C. Two phases: a scoping agent first, then the plan.** One agent
runs the JBI first step (existing syntheses, vocabulary, volume,
F5), the plan is drafted from its return, the principal judges it,
the question agents run. Pro: the plan is written in the field's
words and knows what already exists; the question "is this a
research at all, or a lookup" (Fermi triage, F4) is answered before
the cost. Con: one more round and one more wait; for a topic the
project already knows the scoping agent repeats what the resource
indexes hold.

**D. The baseline: one agent, one note, split afterwards.**
Rejected by the evidence of F3 (one head, one context, many
relations) and by the principal's premise; kept here as the
comparison every plan must beat.

**E. Decomposition by source kind instead of by question** (one
agent for standards and handbooks, one for peer-reviewed methods,
one for practitioner texts). Pro: matches Bramer's lesson that
sources find different things (F6) and Greenhalgh's that protocol
and snowballing find different halves (F7). Con: the answers come
back sorted by where they were found, not by what was asked; the
synthesis has to redo the decomposition. Useful as a second axis
inside a card (where to look), not as the plan's axis.

## Relevance to this project

**Recommendation: A, with C's scoping step folded in as the plan's
first card whenever the topic is new to the project, and B's one
good part, a disconfirming query per card, made a fixed field.**
The plan is the protocol (F10): shown before the search, kept word
for word at the head of the synthesis note, every change to it
between plan and note recorded with its reason, which is the one
effect of protocols the evidence supports.

What the plan lists, per question (the card):
1. *The question* in a frame: what is asked, about whom or what, in
   what context, against what alternative (F1). Equal precision is
   not required; one part may be broad while another is narrow [1].
2. *Why it matters*: the decision or artefact of the chain it
   serves, in one sentence (Herring's "compelled to act upon",
   Cochrane's "important to people making decisions", F4, F12).
   A question with no sentence here is cut.
3. *What would answer it*: the kind of evidence (a standard, a
   measurement, a consensus statement, a practitioner's rule, a
   counter-example) and the kind of source where that evidence
   lives (F4, F6). One kind of evidence per card; a card that needs
   two is two cards.
4. *Where to look*: named source kinds and more than one engine
   or route (F6, F7); for an unsettled vocabulary, snowballing from
   the first good source declared in advance (F7).
5. *The disconfirming query*: one search written to find the
   opposite of what the principal or Claude expects, and what was
   expected (F11).
6. *The stop rule*: the known items that must turn up (retrieval of
   known items), and the diminishing-returns threshold stated in
   advance, "the last N sources added nothing new", with N chosen
   by the card's heterogeneity (F8, F9).

How the number of questions is bounded: by kind, not by count
(CLAUDE.md, Kind not count), and the kind rule of field 3 does the
bounding: one kind of evidence from one kind of source per card.
The number then falls where every tradition puts it, between three
and seven (F3); past seven Heuer's advice applies, group them for
the first cut, and if the groups still exceed seven the topic is
several researches, which is the skill's existing rule, now applied
before the search instead of after it. The first card, for a new
topic, is always F5's: does a synthesis exist, in what words does
the field speak, how large is the literature; its return may rewrite
the other cards before they run, and the plan says so.

How completeness is judged, at the synthesis, card by card, as
three statements the synthesis note makes explicitly (F8, F10,
F11): (a) each card has an answer, or a recorded "not found" naming
where it was looked for; (b) the card's stop rule was met, or the
reason searching ended is written (TARCiS's rule, Booth's "must
explain why searching ended"); (c) the disconfirming query ran and
what it found is reported, including nothing. The synthesis then
adds Cochrane's diagnostic: if snowballing found many sources the
planned queries missed, the plan's queries were weak, and the note
says so rather than hiding it in a good result. Agreement across
cards is laid out as consistency, never as validation, as the
companion note already requires for engines (research of
2026-10-23, F7). A note that fails (a) or (b) on any card is
reported as incomplete, not as done.

Two cautions from the evidence. The field's numbers (9 to 17
interviews, 6 to 14 studies, 98.3 percent with four databases) are
not transferable as numbers; they transfer as shapes: early
saturation on homogeneous ground, later on heterogeneous, no single
source enough. And nothing here proves that a planned research
finds more (F13); the claim the forge can honestly make for the plan
is that the principal sees the questions before they cost anything
and can criticise the answer afterwards against them.

Consult when: defining the plan step of `/research` and the fields
of a question card; writing the contract of the isolated research
agent (what it is given, what it must report: queries, sources,
the disconfirming search, the stop reason); deciding whether a
topic is one research with sub-questions or several researches;
judging a returned research that is thin or one-sided (check the
disconfirming query and the stop reasons first); deciding whether
snowballing is worth its cost on a topic (TARCiS: yes when the
vocabulary is unsettled); deciding how much of the plan may change
after the scoping card returns and how the change is recorded.

## Sources

1. Cochrane Handbook for Systematic Reviews of Interventions,
   version 6.5, Chapter 2 "Determining the scope of the review and
   the questions it will address" (Thomas, Kneale, McKenzie,
   Brennan, Bhaumik), Cochrane, 2024.
   https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-02
   Read in full (one fetch of the whole chapter).
2. Cochrane Handbook version 6.5, Chapter 4 "Searching for and
   selecting studies" (Lefebvre et al.), Cochrane, 2024.
   https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
   Read partially (sections 4.1 to 4.5; 4.6 on selection not read).
3. Cochrane Effective Practice and Organisation of Care (EPOC),
   "How narrow or broad should EPOC reviews be?", EPOC resources
   for review authors, 2017 (file dated 2019-03-13).
   http://epoc.cochrane.org/sites/epoc.cochrane.org/files/uploads/Resources-for-authors2017/how_narrow_or_broad_should_epoc_reviews_be.pdf
   Read in full (PDF converted with scripts/doc2md.py).
4. JBI Manual for Evidence Synthesis, Chapter 10 "Scoping reviews",
   sections 10.2 (protocol as distinct characteristic), 10.2.2
   "Developing your protocol" (deviations transparent), 10.2.5;
   JBI, current online edition.
   https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862619
   Read partially (introductions only; 10.2.3 and 10.2.6 could not
   be opened, their content taken from 5 and the search summaries).
5. QUT Library, "Scoping reviews: search" and "formulate", library
   guide quoting JBI Manual 11.2.4 and 11.2.5 (three-step search,
   PCC, breadth).
   https://libguides.library.qut.edu.au/scopingreviews/search
   Read in full (secondary, quoting JBI).
6. Library guides comparing question frameworks (UNC, Sheffield
   Hallam, Melbourne, Coventry), 2023 to 2025, via search summary
   only. https://guides.lib.unc.edu/pico/frameworks
7. Methley, Campbell, Chew-Graham, McNally, Cheraghi-Sohi, "PICO,
   PICOS and SPIDER: a comparison study of specificity and
   sensitivity in three search tools for qualitative systematic
   reviews", BMC Health Services Research, 2014. Abstract read via
   the Semantic Scholar API; full text not opened.
   https://doi.org/10.1186/s12913-014-0579-0
8. Booth, "Searching for qualitative research for inclusion in
   systematic reviews: a structured methodological review",
   Systematic Reviews, 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4855695/
   Read in large part (two of three segments).
9. Cooper, Booth, Varley-Campbell, Britten, Garside, "Defining the
   process to literature searching in systematic reviews: a
   literature review of guidance and supporting studies", BMC
   Medical Research Methodology, 2018.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC6092796/
   Read partially (abstract and first two thirds).
10. Bramer, Rethlefsen, Kleijnen, Franco, "Optimal database
    combinations for literature searches in systematic reviews: a
    prospective exploratory study", Systematic Reviews, 2017.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC5718002/ Read in full.
11. Greenhalgh, Peacock, "Effectiveness and efficiency of search
    methods in systematic reviews of complex evidence: audit of
    primary sources", BMJ, 2005.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC1283190/ Read in full.
12. Wohlin, "Guidelines for snowballing in systematic literature
    studies and a replication in software engineering", EASE 2014.
    https://doi.org/10.1145/2601248.2601268 Record only; the PDF
    mirrors refused the connection; procedure taken from search
    summaries of the paper and of library guides citing it.
13. Wohlin, Kalinowski, Felizardo, Mendes, "Successful combination
    of database search and snowballing for identification of
    primary studies in systematic literature studies", Information
    and Software Technology 147, 2022 (arXiv 2307.02612).
    https://arxiv.org/abs/2307.02612 Abstract read.
14. Wright, Golder, Rodriguez-Lopez, "Citation searching: a
    systematic review case study of multiple risk behaviour
    interventions", BMC Medical Research Methodology, 2014.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC4048585/ Read in full.
15. Hirt, Nordhausen, Fuerst, Ewald, Appenzeller-Herzog et al.,
    "Guidance on terminology, application, and reporting of citation
    searching: the TARCiS statement", BMJ 385:e078384, 2024; read
    through the University of Basel medical library's summary page
    of the ten recommendations.
    https://ub-easyweb.ub.unibas.ch/de/ub-medizin/tarcis/
    Read in full (summary page; the BMJ text not opened).
16. JBI Manual, section 4.2.6.2 "Citation searching".
    https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/652181517/4.2.6.2+Citation+searching
    Read in full.
17. Page et al., "The PRISMA 2020 statement: an updated guideline
    for reporting systematic reviews", BMJ, 2021 (items 5, 6, 7,
    24). https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/ Read
    partially. PRISMA-S (Rethlefsen et al., Systematic Reviews 2021,
    sixteen items) and PRISMA-ScR item 5 via search summaries only.
18. Booth, "How much searching is enough? Comprehensive versus
    optimal retrieval for technology assessments", International
    Journal of Technology Assessment in Health Care 26(4), 2010.
    https://www.cambridge.org/core/journals/international-journal-of-technology-assessment-in-health-care/article/abs/how-much-searching-is-enough-comprehensive-versus-optimal-retrieval-for-technology-assessments/420FE198E07703FB1AAFE762958CFE4A
    Abstract read (the eight methods listed there).
19. Motschall et al., "The number needed to read: are
    capture-recapture techniques feasible in searching literature
    for systematic reviews?", Cochrane Colloquium abstract, 2009;
    and a surgery capture-mark-recapture study (3 missed, 93 percent
    found). Via search summaries only.
    https://abstracts.cochrane.org/2009-singapore/number-needed-read-are-capture-recapture-techniques-feasible-searching-literature
20. Hennink, Kaiser, "Sample sizes for saturation in qualitative
    research: a systematic review of empirical tests", Social
    Science and Medicine 292, 2022 (online 2021). Abstract read via
    the Semantic Scholar API. https://doi.org/10.1016/j.socscimed.2021.114523
    Malterud, Siersma, Guassora, "Sample size in qualitative
    interview studies: guided by information power", 2016, via
    search summary only.
21. Hennink, Kaiser, Marconi, "Code saturation versus meaning
    saturation: how many interviews are enough?", Qualitative
    Health Research, 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC9359070
    Read in full.
22. Cochrane Rapid Reviews Methods Group (Garritty et al.),
    "Cochrane Rapid Reviews: interim guidance from the Cochrane
    Rapid Reviews Methods Group", March 2020 (published as Garritty
    et al., Journal of Clinical Epidemiology 130, 2021).
    https://methods.cochrane.org/sites/methods.cochrane.org.rapidreviews/files/uploads/cochrane_rr_-_guidance-23mar2020-final.pdf
    Read in full (PDF converted with scripts/doc2md.py).
23. McGowan, Sampson, Salzwedel, Cogo, Foerster, Lefebvre, "PRESS
    Peer Review of Electronic Search Strategies: 2015 guideline
    statement", Journal of Clinical Epidemiology 75, 2016. Via
    search summary and Cochrane Handbook 4.4.8 only.
    https://www.cda-amc.ca/sites/default/files/pdf/CP0015_PRESS_Update_Report_2016.pdf
24. Garritty et al., "Updated recommendations for the Cochrane
    rapid review methods guidance for rapid reviews of
    effectiveness", BMJ 384:e076335, 2024. Abstract read via the
    Semantic Scholar API; full text refused (403).
25. Heuer, Psychology of Intelligence Analysis, CIA Center for the
    Study of Intelligence, 1999; Chapter 7 "Structuring Analytical
    Problems" and Chapter 8 "Analysis of Competing Hypotheses".
    https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
    Chapters 7 and 8 read in full (PDF converted with
    scripts/doc2md.py).
26. Heuer, Pherson, Structured Analytic Techniques for Intelligence
    Analysis, CQ Press, 2010 and later editions: table of contents
    (Getting Started Checklist, Customer Checklist, Issue
    Redefinition) via search summaries; the Issue Redefinition
    steps from a secondary description, MCSI Library, "Analytics
    techniques". https://mcsi-library.readthedocs.io/ways-of-working/analytics-techniques.html
    Read in full (secondary; the book not opened).
27. Muller, "Key activities of competitive intelligence", South
    African Journal of Information Management 5(1), 2003, quoting
    Herring, "Key intelligence topics: a process to identify and
    define key intelligence needs", Competitive Intelligence Review
    10(2), 1999. https://sajim.co.za/index.php/sajim/article/download/205/200
    Read in full (PDF converted with scripts/doc2md.py; Herring's
    own article not opened).
28. Klue, "Get your KITs together" (KITs opened into key
    intelligence questions), practitioner blog, via search summary
    only. https://klue.com/blog/get-your-kits-together
29. US Army, "Priority Intelligence Requirement Management in
    Divisions and Corps", army.mil, and FM 34-2 training material
    on PIR, indicators, SIR and the collection plan; via search
    summaries only. https://www.army.mil/article/285410/priority_intelligence_requirement_management_in_divisions_and_corps
30. ThinkInsights, "Problem Structuring and Hypothesis-Driven
    Consulting Playbook (Issue Trees, MECE)", practitioner playbook,
    undated. https://thinkinsights.net/playbooks/problem-structuring-hypothesis-driven-consulting-playbook-issue-trees-mece
    Read partially (the public part; references section empty).
31. Cooper, Schindler, Business Research Methods, 9th edition,
    McGraw-Hill, 2006, Chapter 3 "The business research process",
    the management-research question hierarchy; via lecture slides
    and course summaries only.
    https://www.slideshare.net/slideshow/brm-3-11054036/11054036
32. Rasiel, Friga, The McKinsey Mind, 2001, and Rasiel, The
    McKinsey Way, 1999; the work plan fields and the hypothesis
    rule via a book summary only.
    https://manassaloi.com/booksummaries/2016/04/20/mcKinsey-mind-ethan-paul.html
33. Tetlock, Gardner, Superforecasting, 2015, appendix "Ten
    commandments for aspiring superforecasters" (triage,
    Fermi-ization), and Good Judgment, "Superforecasters' toolbox:
    Fermi-ization in forecasting"; via search summaries only.
    https://goodjudgment.com/superforecasters-toolbox-fermi-ization-in-forecasting/
34. The PLoS Medicine Editors, "Best practice in systematic
    reviews: the importance of protocols and registration", PLoS
    Medicine, 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3042995/
    Read in full.
35. Tricco et al., "A third of systematic reviews changed or did
    not specify the primary outcome: a PROSPERO register study",
    Journal of Clinical Epidemiology, 2016. Via the University of
    Bristol repository summary only.
    https://research-information.bris.ac.uk/en/publications/a-third-of-systematic-reviews-changed-or-did-not-specify-the-prim/
36. A 2017 meta-epidemiological study of 284 systematic reviews in
    high-impact journals (21 percent registered; no association
    between registration and outcome reporting bias), PubMed
    28242481. Seen only through a search summary; authors and
    journal not verified; the PubMed page could not be opened.
37. Booth A., Mitchell, Mott, James, Cockayne, Gascoyne, McDaid,
    "An assessment of the extent to which the contents of PROSPERO
    records meet the systematic review protocol reporting items in
    PRISMA-P", F1000Research, 2020.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7431973 Read in full.
38. Kacperski, Bielig, Makhortykh, Sydorova, Ulloa, "Examining bias
    perpetuation in academic search engines: an algorithm audit of
    Google and Semantic Scholar", First Monday 29(11), 2024 (arXiv
    2311.09969, v3 January 2025). https://arxiv.org/abs/2311.09969
    Abstract read.
39. Cochrane Handbook version 5.1, section 10.2.2.3 "Citation
    bias"; Duyx et al., "Scientific citations favor positive
    results: a systematic review and meta-analysis", Journal of
    Clinical Epidemiology, 2017. Via search summaries only.
    https://training-noproxy.cochrane.org/handbook/archive/v5.1/chapter_10/10_2_2_3_citation_bias.htm
40. Dhami, Belton, Mandel, "The 'analysis of competing hypotheses'
    in intelligence analysis", Applied Cognitive Psychology, 2019;
    and Dhami et al., "Effects of task structure and confirmation
    bias in alternative hypotheses evaluation", Cognitive Research:
    Principles and Implications, 2024. Via repository summaries
    only. https://strathprints.strath.ac.uk/69049/
41. Wikipedia, "Analysis of competing hypotheses", section on
    weaknesses and criticisms (citing Thomason 2010, van Gelder
    2008, Jones and Silberzahn 2013).
    https://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses
    Read in full (tertiary).

Not opened despite attempts: ICD 203 "Analytic Standards" (ODNI;
every mirror returned 404 or an empty page), the JBI Manual
sections 10.2.3 and 10.2.6, Garritty 2024 full text, Hennink and
Kaiser 2022 full text, Wohlin 2014 full text, Herring 1999, the
Heuer and Pherson book, Minto's Pyramid Principle (no primary
source found; MECE taken from 30 and 32).
