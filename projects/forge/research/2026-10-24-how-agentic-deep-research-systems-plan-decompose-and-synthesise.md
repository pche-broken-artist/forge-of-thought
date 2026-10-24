---
date: 2026-10-24
project: forge
topic: how agentic deep-research systems plan, decompose and synthesise, and what is known to work
status: immutable
derived_from: the principal's word of 2026-10-24 (the /research command to show a plan before searching: the topic split into questions, one agent per question, the plan decides the quality); .claude/skills/research/SKILL.md; research/2026-10-23-a-reviewer-or-a-question-on-another-model-inside-the-forge.md; web sources below
---

# How agentic deep-research systems plan, decompose and synthesise

## Question

How do today's agentic "deep research" systems - the commercial ones
(OpenAI, Google, Anthropic, Perplexity, Microsoft, xAI), the open and
academic ones (STORM, GPT-Researcher, the Open Deep Research family,
WebThinker, Agent Laboratory and the 2025-2026 RL agents) - plan,
decompose, search, iterate and synthesise; what do they show the
user before searching; and what does the published evidence say
about which of these designs make a research better, and about how
they fail?

The baseline it must beat is the forge's `/research` today: one
Claude in the session searches the web for one question, writes one
note with findings, options and a recommendation, indexes it. No plan
is shown, no agent is isolated, nothing separates gathering from
writing, nothing checks the citations. The redesign wants a plan
shown to the principal first - the topic split into simpler
questions, one isolated agent per question, one note per question,
then a synthesis - and wants to trust that the result is relevant,
current, deep, free of junk and does not overlook what is
interesting.

## Key findings

**F1. Three ways to start, and the field has names for them. The
plan shown for confirmation is the rarest; most systems plan
silently.** [consensus on the facts; the taxonomy is one survey's]
The survey of Huang et al. (v2, 2025-09) sorts deep-research agents
by how they treat the user before searching: *planning-only*
(a plan from the prompt alone, no question asked - "most DR agents",
Grok, Manus, H2O among them), *intent-to-planning* (clarifying
questions first, then an internal plan - OpenAI Deep Research) and
*unified intent-planning* (a preliminary plan is produced and the
user confirms or revises it - Gemini Deep Research) [14]. The
primary sources agree: Google's launch post says Deep Research
"drafts a multi-step research plan" that the user can "revise or
approve" before work begins, "under your supervision" [7]; the
product page says "you control the plan" and lists the steps
planning (breaking the question into sub-tasks), searching,
reasoning (a thinking panel shows what it has learned) and
reporting [8]. Third-party guides describe the card as having
"Edit plan" and "Start research" buttons and the plan as a list of
stages - research websites with sub-questions, analyse results,
create report [47]. In Google's API the same plan review is
*opt-in* (`collaborative_planning`), off by default, refined over
several turns and then approved by turning the flag off [9].
OpenAI's help centre, which I could not open (403), is quoted by the
search engine as saying that in Chat "the model will create a
proposed research plan, which you can review and modify", while in
Work or Codex it asks clarifying questions instead [3]; OpenAI's
Isa Fulford said the clarification step "helps users be more
specific about their needs" [6]. Microsoft's Researcher asks
clarifying questions the user may answer or skip with "Go ahead";
its documentation names no plan [12]. Perplexity asks nothing and
"refines its research plan as it learns" [10]. Anthropic's
engineering post has the lead agent save its plan to memory and
never mentions showing it [1]; Anthropic's current `deep-research`
skill (read on disk) asks follow-up questions only when they "would
meaningfully impact how research is conducted", keeps the user
informed through a to-do list and asks no confirmation of the
decomposition [2]. LangChain's Open Deep Research clarifies
(`allow_clarification` defaults to true) and then condenses the
conversation into a *research brief* that becomes "the reference
point for the research and writing phases" - a brief, not a plan,
and not confirmed [19]. NVIDIA's AI-Q blueprint has a clarifier
agent that drafts a plan the user approves or rejects, the approved
plan then injected into the researcher's prompt; it can be switched
off [44].

**F2. What the shown plan contains is thin everywhere: sub-questions
and stages, never the agents' briefs, never stop rules.** [verified
on the pages] Gemini's plan is a list of research sub-questions plus
"analyse" and "report" stages [8][47]. OpenAI's instruction agent in
the cookbook turns the clarified request into research instructions
with explicit rules: "maximize specificity", "fill in unstated but
necessary dimensions as open-ended" (write "no specific constraint"
rather than guess), "avoid unwarranted assumptions", name the output
language, the preferred sources and the format [5]. LangChain's
brief does the same condensation [19]. None of the systems I found
shows the user how the work will be divided among agents, how many
there will be, what each is told, when each stops, or how the result
is checked - the things that in Anthropic's own account decide the
quality (F4). Gemini's plan is also drawn from the model's knowledge
before any search; WebWeaver's authors criticise exactly this
"outline-first" habit as "limited by the LLM's internal, possibly
outdated knowledge" [25].

**F3. There is no published ablation of plan confirmation. The
indirect evidence for it is real but circumstantial.** [emerging; my
reading of several sources] I found no study that isolates "the user
confirmed the plan" as a variable. What exists: IntentRL (2026-02)
names the "autonomy-interaction dilemma" - an autonomous run on an
ambiguous query is long, expensive and often unsatisfactory - and
reports that clarifying latent intent before research raises intent
hit rate and downstream task performance, beating the built-in
clarify modules of the closed systems [43]. ResearchRubrics, the
Scale AI benchmark (ICLR 2026), finds the leading agents under 68 %
rubric compliance and attributes the shortfall "primarily" to
"missed implicit context and inadequate reasoning about retrieved
information", implicit reasoning and synthesis together being
45-50 % of failures; its authors call for architectural change, not
prompt polish, and do not propose clarification [30]. The PING study
of six agents finds that most intent hallucination is "neglecting
user restrictions rather than deviating from the task" [38].
LangChain's lesson is that a condensed brief keeps "later phases
aligned with what the user wants" [19]. My inference, marked as
such: a plan the principal reads surfaces implicit context and
restrictions *before* the tokens are spent, which is where the
benchmarks locate the biggest losses; but the gain is argued, not
measured, and the one measured intervention (IntentRL) is
clarification by questions, not plan approval.

**F4. Decomposition: the orchestrator-worker pattern with a few
narrowly briefed parallel workers is the dominant engineered design;
the brief is the lever.** [consensus among the engineering
write-ups; the figures are vendor claims] Anthropic's Research
system has a lead agent that "plans a research process based on
user queries" and spawns subagents with their own context windows,
which act as "intelligent filters" condensing what they find; the
lead synthesises, decides whether more is needed, may spawn more,
and a separate CitationAgent attaches citations at the end [1].
Delegation failed when vague: subagents duplicated searches and
misread tasks until each was given "a clear objective, output
format, tool and source guidance, and task boundaries" [1]. Effort
is scaled by rules written into the prompt: simple fact-finding, one
agent and 3-10 tool calls; a direct comparison, 2-4 subagents with
10-15 calls each; complex research, more than 10 subagents with
divided responsibilities; the lead launches 3-5 at once [1]. The
reported result - Opus 4 lead with Sonnet 4 subagents beating a
single Opus 4 by 90.2 % on an internal eval - comes with the
finding that on BrowseComp three factors explained 95 % of the
variance and token usage alone 80 %, and that the system burns about
15 times the tokens of a chat [1] (vendor claim; the 90.2 % is
widely repeated by secondary sources from this one post). Anthropic's
current skill, read on disk, puts the same design in a table: 1
researcher for a single fact, 3 for "few natural angles" (the
default "when in doubt"), 4 for distinct facets or criteria, 5 for
independent entities or regions, 6+ for a large enumerable set; the
subtopics are to be "mutually exclusive and collectively
exhaustive", and for each subtopic the coordinator considers whether
"multiple independent points of view" are needed; each subagent's
prompt has fixed fields - the narrow topic, an objective, key
questions, suggested source types, constraints propagated from the
original question (temporal, geographic), the output path - and the
researcher is told that others cover adjacent areas, to run about 10
and never more than 15 tool calls, to prefer short queries, to fetch
full pages because snippets mislead, and to write its note in a fixed
shape: per key question a takeaway, cited findings (one source per
line, a contradiction written as "contradicted by"), inferences and
gaps [2]. LangChain's supervisor decides whether the brief splits
into independent sub-topics, gives each sub-agent "one sub-topic and
no other part of the brief", runs up to 5 units concurrently, up to
6 supervisor reflection rounds and 10 tool calls per researcher step
by default, and compresses each sub-agent's result into "a detailed
answer to its sub-question with sources" before the supervisor sees
it [19]. GPT-Researcher's planner-executor generates 3 sub-queries by
default; its deep mode is a tree of breadth 3-4 and depth 2 with
concurrency 4, about 5 minutes and 0.40 USD on o3-mini [18]. Tongyi's
"Heavy" mode runs several agents on the same question by different
routes, each returning a compressed report, which a synthesis model
merges; the compressed reports exist because "full trajectories
would exceed context limits with just 2-3 agents" [27].

**F5. The other camp: one agent trained end to end, no
decomposition, long loops.** [verified; the argument is each
vendor's] OpenAI's Deep Research is one o3 fine-tuned by RL on
browsing tasks, running 5-30 minutes [6]; the survey classifies both
OpenAI's and Gemini's products as single-agent [14]. Kimi-Researcher
argues against multi-agent workflows as needing "frequent manual
updates as models and environments change"; its single agent
averages 23 reasoning steps and 200+ URLs per task, cross-checks
sources even on simple questions, and its context management
(keeping what matters, discarding documents) is what lets a run pass
50 iterations where a naive agent fails at about 10; in an ablation
the model trained with it used 30 % more iterations and performed
better [28]. WebResearcher names the disease of the single long
context "context suffocation and noise contamination" and cures it by
periodically consolidating findings into an evolving report [26];
Search-o1 adds a "Reason-in-Documents" step because retrieved pages
are "verbose" and noisy and must be refined before they enter the
reasoning [21]. This camp is not open to the forge as a design
choice - it needs a trained model - but its two lessons are: the
loop must be long (dozens of steps), and raw pages must never be
poured into the context that reasons.

**F6. More agents is not better; the gain is bounded by how
independent the questions are.** [emerging; several independent
2026 studies agree] SAIGE (2026-09), on Deep Research Bench II and
three other benchmarks with one base model, varied the agent cap
(4-6) and recursion depth (1-3): raising either "generally lowered
scores and raised token use" (one benchmark: 71.8 at 4 agents, 67.3
at 5, 64.0 at 6; input tokens 185M to 352M); generic multi-agent
methods fell below the single agent on densely coupled tasks and
beat it on sparse ones (55.2 vs 51.5 on Deep Research Bench II); the
conclusion is that "multi-agent superiority is bounded by task
structure rather than universal", and the fix is to spawn children
only at dependency boundaries that can run independently and to
fetch context on demand rather than push it all up front [40].
WideSeek-R1 shows the other face: on *broad* information seeking
(WideSearch) a 4B model with parallel subagents matches a 671B single
agent and gains "consistently" as subagents are added [41]. An
empirical study of automated-research teams (2026-05) finds
independent subagents with a merging coordinator "resilient,
high-throughput" but low in diversity, fixed-role teams diverse but
fragile, and unrestricted agent-to-agent chatter a cause of crashes
[42]. LiveResearchBench (ICLR 2026), across 17 systems, finds
"planners dispatching specialized sub-agents correlate with better
average performance" yet multi-agent systems average lower coverage
(about 72 vs 78) and much better citation association (62 vs 38)
than the single-agent deep-research models [31]. MAST, the taxonomy
of 1,600+ multi-agent traces, groups the 14 failure modes into
system design (specification), inter-agent misalignment and task
verification [39]. The reading: split where the questions are
independent, keep the count small (the local skill's 3-5, SAIGE's
4), never let agents talk to each other.

**F7. Breadth comes from perspectives, not from more queries; STORM
measured it.** [single strong source; peer-reviewed] STORM (NAACL
2024) discovers N=5 perspectives by reading the tables of contents
of related Wikipedia articles, adds a "basic fact writer", and runs
for each a simulated conversation of M=5 turns in which a writer
asks and an expert answers from searched, reliability-filtered
sources; the outline is drafted from the topic alone and then
refined with the conversations [16]. Its ablation is the one direct
measurement I found of what decomposition by viewpoint buys: without
the perspectives the number of unique references collapses from
99.8 to 54.4 while outline recall barely moves; without the
grounded conversations outline recall drops sharply (soft heading
recall 86.3 to 78.0) and references fall to 39.6 - "reading relevant
information is key to asking effective questions" [16]. Wikipedia
editors judged 25 points more STORM articles organised and 10 points
more broad than the outline-driven baseline, and named two failure
modes that any synthesis step must guard: "source bias transfer"
(seven of ten editors found articles emotional or unneutral, traced
to the sources) and "over-association of unrelated facts" (red
herrings, overspeculation) [16]. Co-STORM (EMNLP 2024) turns the
same idea to the user's "unknown unknowns": agents discuss the topic
and ask questions on the user's behalf while a dynamic mind map
organises what surfaces; 70 % preferred it to a search engine,
78 % to a RAG chatbot [17].

**F8. Iteration: everyone re-plans after first results; the open
question is when to stop, and the known bias is stopping on the
first evidence.** [consensus on the mechanism; the biases are
emerging findings] Anthropic's lead "decides whether more research
is needed" and may spawn more subagents; one of its observed
failures is "continuing to search after sufficient results were
already available", another "endless web searching for nonexistent
sources" [1]. Its current skill allows exactly one extra round, only
for "critical gaps", and makes the coordinator write out that it
will then move to the writer "regardless of what results you get
back" [2]. LangChain caps the supervisor at 6 reflection rounds and
"scales the amount of research to the request" because users do not
want simple requests to take over 10 minutes [19]. TTD-DR (Google,
2025-07) gives the loop a direction: a plan is drawn first, then an
initial draft is written from the model's knowledge as a "noisy"
start, each new search question is generated from the current
draft's gaps, each answer revises the draft, up to 20 steps, and the
loop stops when the plan is covered or the cap is hit; in its
ablation this "denoising with retrieval" adds 8-15 points of win
rate over the already self-evolving backbone and by step 9 holds
51 % of the final report's information [24]. WebWeaver's planner
alternates searching and revising an outline whose sections cite
evidence IDs in a memory bank; successive outline rounds raise
comprehensiveness 48.9 to 50.8 and insight 46.3 to 48.4 [25].
FutureSearch's Deep Research Bench trace analysis finds models
"satisficing rather than optimizing" - stopping at the first
acceptable answer, o3 at times declaring data unavailable and
guessing - and finds *forgetting* earlier findings the strongest
predictor of a low score, with thinking models looping on identical
tool calls [32]. PING names two biases across all six agents it
tested: an "anchor effect" (early retrieval over-weighted, later and
better chunks used less) and a "homogeneity bias" (repeated
evidence preferred over rarer, heterogeneous evidence; small
clusters ignored more than large ones of equal relevance); a
stronger backbone does not remove them [38]. Anthropic's one tested
search heuristic is "start wide, then narrow down": short broad
queries first, assess, then narrow, because agents open with long
specific queries that return little [1]. BrowseComp shows accuracy
rising "smoothly" with test-time compute and best-of-64 voting
adding 15-25 points, but also that browsing *worsens* calibration
(Deep Research 91 % calibration error) - more evidence makes the
model more confident, not more right [33].

**F9. Synthesis: one writer, after all research, from compressed
notes; parallel writing of sections failed.** [consensus among the
engineered systems] LangChain tried sub-agents writing report
sections in parallel and got "disjointed" reports; it now restricts
multi-agent work to research and writes the report in one LLM call
from the brief plus all findings [19]. Anthropic's lead
synthesises, then the CitationAgent places citations [1]; its skill
spawns one report writer that reads the notes only, plans
"signpost" headers, writes a bottom-line-up-front paragraph and 3-5
sections, and is told that "a report with 5 well-sourced claims is
better than one with 20 claims where half are unsourced" - any major
claim without an inline URL in the notes is dropped [2]. Tongyi's
synthesis model reads compressed reports, never trajectories [27].
WebWeaver measures the alternative to one-shot writing: a writer that
drafts section by section, retrieving only the evidence the outline
cites for that section and pruning it afterwards, against
"brute-force" feeding of everything: insight 42.7 to 50.0,
readability 43.8 to 49.8, citation accuracy 86.7 to 93.4; the
authors tie feed-all to "lost in the middle" effects and
hallucination [25]. On conflicts between sub-findings I found no
system with a formal step: Anthropic's researcher is told to write
"contradicted by" and never to "silently pick a conflicting source"
[2]; Kimi "refines its hypotheses" when sources conflict [28];
Gemini "flags inconsistencies" [8]; the rest is the writer's
judgement. My inference: conflict handling is where the forge's
walkthrough already does more than the field - the field leaves it
to the model.

**F10. Citations: the orchestrator is where they break; raw
single-document snippets and a hard rule fix most of it.** [emerging;
three independent 2026 studies point the same way] "Who is the Agent
to Blame?" (EMNLP 2026) tests each agent of three open systems
against its own inputs: agents summarising a single document make
few mistakes (AI-Q's snippet searcher 3.8 %), researchers that
synthesise several documents many (70.8 %), and 84.7 % of the
errors in AI-Q's final report originate at the orchestrator, mostly
citation errors; two interventions - giving the orchestrator the raw
single-document snippets for each cited URL instead of the
researchers' synthesised notes, and the instruction "do NOT use
information which is not backed by citations" - each raise citation
recall about 5 points and precision from 87.6 to 94.1 / 91.0 with
report quality flat [37]. Rao, Wong and Callison-Burch (2026-04)
checked 53,090 citation URLs from 10 systems: 3-13 % are
hallucinated (no Wayback record), 5-18 % non-resolving; deep
research agents cite more per query *and* hallucinate URLs at
higher rates than search-augmented chat models; a URL-liveness tool
in the agent's hands cut non-resolving citations to under 1 % [36].
DeepResearch Bench's FACT scores show the trade-off: Gemini 2.5 Pro
Deep Research 111 effective citations at 81 % accuracy, OpenAI 41 at
78 %, Perplexity 31 at 90 %, Claude 3.7 Sonnet with search 32 at
94 % [29]; WebWeaver later reports 93 % at 200 citations [25].
LiveResearchBench finds that "most citation errors are unsupported
claims rather than invalid URLs", that length "doesn't reliably
indicate quality" and is inflated by citation formatting, and names
Manus using "fictional links" [31]. ReportBench separates statement
hallucination (content deviates from the cited source) from citation
hallucination (the reference is fabricated) [35]. LiveResearchBench's
verdict on the field is that most systems are "deep searchers rather
than deep researchers" [31].

**F11. What the benchmarks measure, and where the commercial
products stand.** [verified figures; the ranking changes monthly]
BrowseComp (OpenAI, 2025-04): 1,266 short-answer questions needing
persistent browsing; Deep Research solved about half at launch,
humans 29 % within two hours; aggregators report ~90 % for the top
models by mid-2026 and near-saturation, which I could not verify
against a primary source [33][48]. GAIA: Hugging Face's open
reproduction reached 55 % on validation against OpenAI's 67 %, and
found that letting the agent write actions as code rather than JSON
was worth about 22 points [20]. Humanity's Last Exam with search:
OpenAI 26.6, Perplexity 21.1, Kimi 26.9, Tongyi Heavy 38.3 (each a
vendor figure) [10][24][27][28]. DeepResearch Bench (2025-06): 100
PhD-level tasks, RACE for report quality (comprehensiveness, insight,
instruction following, readability, reference-based) and FACT for
citations; its LLM judge agreed with experts (71 %) slightly more
than experts with each other (68 %) [29]. ResearchRubrics
(ICLR 2026): 2,593 expert rubrics, tasks placed on three axes -
conceptual breadth, logical nesting depth, exploration (how
underspecified the goal is); Gemini 0.677, OpenAI 0.664, Perplexity
0.566 compliance [30]. LiveResearchBench (ICLR 2026): 100 live-web
tasks, 17 systems, five dimensions [31]. FutureSearch's Deep
Research Bench: 89 tasks in 8 categories on a frozen web; best
single score 0.51 (o3) against a noise ceiling of about 0.8; in a
small sample the commercial Deep Research products were *not*
reliably better than the same vendor's chat model with search -
ChatGPT-o3 beat o3 Deep Research, Perplexity Pro beat Perplexity
Deep Research, while Gemini Deep Research did beat Gemini with search
[32]. Mind2Web 2 (NeurIPS 2025): 130 tasks, agent-as-a-judge with
tree rubrics; OpenAI Deep Research at 50-70 % of human performance
in half the time [34]. Google's own claim for Gemini 2.5 Deep
Research is a 2-to-1 rater preference over other providers [49]
(vendor claim). Deep Research Comparator (CMU/Amazon) finds human
side-by-side votes aligned with the static benchmarks overall but
diverging on fine-grained metrics [45].

**F12. What the ablations say helps, in order of the evidence's
weight.** [my synthesis of F4-F11; each item cites its study]
(a) Isolated contexts for independent sub-questions, few of them:
Anthropic's 90.2 % [1], WideSeek on broad tasks [41], Tongyi Heavy
(HLE 32.9 to 38.3, BrowseComp 43.4 to 58.3) [27], bounded by SAIGE
[40]. (b) A draft or outline that steers the next searches: TTD-DR
[24], WebWeaver [25]. (c) Grounded questions - read, then ask:
STORM's ablation [16]. (d) A verification pass of the citations by
tool, not by the model: urlhealth [36], the two AI-Q interventions
[37]. (e) Self-evolution (several variants of each step, judged and
merged): TTD-DR's largest single gain, 21-35 points of win rate [24]
- expensive, and the one item here without independent replication.
(f) Context management in long loops: Kimi's 30 % more iterations
[28], WebResearcher [26]. (g) Clarifying intent before the run:
IntentRL [43]. What hurts: more than about four agents or deeper
recursion [40]; parallel writing [19]; vague briefs [1]; raw pages
in the reasoning context [21][26]; feeding everything to the writer
[25]; synthesised multi-document notes as the writer's only input
[37]; agent-to-agent communication [42]; and, as a human-only
catch, agents "favoring SEO content farms over authoritative
sources like academic PDFs", fixed at Anthropic by source-quality
heuristics in the prompt [1].

**F13. The failure modes, named and sourced.** [consensus; each
item attributable] Shallow coverage - "deep searchers rather than
deep researchers" [31], satisficing [32]. Hallucinated citations
3-13 % of URLs [36]; unsupported claims commoner than fake URLs [31];
statement vs citation hallucination [35]. Over-long reports with
length no proxy for quality [31] - contested by ResearchRubrics,
where longer reports scored higher, attributed to density [30].
Drift from the question - the PING "intent" class, mostly neglected
user restrictions [38]. Anchoring to early evidence and homogeneity
bias [38], forgetting [32], duplicate work and over-search [1],
source bias transfer and over-association [16], over-confidence
grown by browsing [33], and the gap the Rubrics name first: missed
implicit context [30]. "Sycophancy to the plan" as such I did not
find named in any study; the nearest measured phenomena are PING's
anchor effect (the first results, not the plan) and TTD-DR's and
WebWeaver's argument that a plan or outline fixed before evidence is
limited by prior knowledge [24][25][38].

## Options

**A. Plan as a list of briefs, confirmed in a walkthrough; one
round; one writer; a mechanical URL check.** The plan the principal
sees is the set of questions, each already in the shape of the
agent's brief (F4): the narrow question, its objective, the key
sub-questions, the kinds of source to prefer, the constraints (time
window, geography, language), and a perspective where the topic has
sides (F7); plus the global stop rule and the count. One isolated
agent per brief, 3-5 as a rule, each writing one note of fixed
shape with gaps and contradictions; then one writer in the session
composing the note from the notes alone, dropping unsourced claims;
then a script checking every URL before filing (F10). Pro: it is
what the two best-documented engineered systems converged on
[1][2][19], it fits the forge's isolation rule (the agents never
see the conversation) and its walkthrough, and it gives the
principal the one thing no product gives him - the briefs. Con: the
plan is drawn from Claude's knowledge before any search, the
weakness WebWeaver names (F2); a second round is needed when the
agents' gaps show the split was wrong.

**B. Scout, then plan.** As A, but one short wide-search agent runs
first (minutes, a dozen calls) and returns a map of the field - the
names, the camps, the dates, what is fresh - from which Claude draws
the plan. Pro: answers the outline-first weakness directly; the
plan's questions are grounded as STORM's ablation says questions must
be (F7); best for topics outside Claude's knowledge or moving
monthly. Con: one more wait before the principal sees anything; the
scout's own biases (anchoring, F8) can shape the plan; costs a run.

**C. Draft-steered research (TTD-DR).** Claude writes a draft answer
from what it knows, marks the gaps, and the plan's questions are the
gaps; the agents fill them; the draft is revised. Pro: the strongest
measured iteration gain (F8); the principal sees, in the draft, what
Claude already believes and can strike it. Con: the draft anchors
the research on Claude's priors - the exact failure the principal
wants to avoid ("does not overlook interesting things"); a draft is
also what the forge calls "draft early" and is an elicitation tool,
which may confuse the two uses.

**D. Perspectives instead of questions (STORM).** The plan lists
viewpoints (the architect, the regulator, the sceptic, the
practitioner) and each agent asks from one. Pro: the only ablated
mechanism for breadth and for unknown unknowns (F7). Con: viewpoints
overlap in what they read, so the notes duplicate; the forge's
challengers already are personas, and a research is not a challenge.
Works well as one brief among the questions ("what do the sceptics
of X say"), not as the whole plan.

**E. One agent, long loop, no plan.** The trained single-agent
products (F5) are not a design the forge can adopt; a single Claude
subagent on a long loop is, and it is right for a narrow factual
question where the local skill, too, uses one researcher (F4). Not
an option for a research that is several questions.

## Relevance to this project

Recommendation: **A as the shape, with B's scout as an option
Claude proposes in the plan when the topic is outside its knowledge
or fast-moving, and D as one brief inside the plan whenever the
topic has sides.** Not C: the forge's reason for the plan is to see
the questions before the answers, and a draft would put Claude's
answer first.

What the plan should contain, so that the walkthrough decides
quality and not only scope (F2, F4): for every question its brief in
full - the question, the objective in one sentence, two to five key
sub-questions, the kinds of source to prefer and to avoid, the
constraints carried from the topic (time window, region, language,
"as of" date), and the one perspective it asks from where there is
one; the count of agents and the rule that fixed it (one per
independent question, none for a question another answers); the stop
rule each agent gets (meet the objective, or nothing new, or the call
budget); whether a second round is allowed and for what (gaps the
agents name, nothing else); what the writer will do with a claim
without a source (drop it) and with a conflict between notes (lay it
out, never pick); and the check that runs before filing (every URL
resolves). The plan is worked as a walkthrough, one question per
message, with the verdict line; `(m)odify` is the normal verdict on
a brief, and the plan is written nowhere until confirmed (prime
directive 9).

How the agents are briefed (F4, F5, F10): the brief above, the
instruction that others cover the neighbouring questions, "start
wide then narrow", about 10 and never more than 15 tool calls, fetch
the page and never trust the snippet, prefer the primary source,
note the date of everything, and the note's fixed shape - per key
sub-question a takeaway, cited findings one per line with the
source's URL and date, "contradicted by" where sources differ,
inferences marked as the agent's own, gaps with the reason. Nothing
from the conversation reaches an agent; the brief is the whole
context, as a reviewer's is today (the companion note of 2026-10-23,
F1). The agents run in parallel and never speak to each other (F6).

Iteration (F8): one round by default; a second only to close gaps
the notes name, proposed to the principal with the gaps listed, never
run on Claude's judgement; no third. The stop rule is in the brief,
not in the coordinator's mood.

Synthesis (F9, F10): one writer, in the session, from the notes
only, after all agents return; the note's `Key findings` carry the
agents' citations as they stand, never re-summarised from memory;
every finding carries its epistemic status (consensus / emerging /
contested / single source / vendor claim) and its date; conflicts
between notes are laid out side by side as the forge already does
for several engines (companion note F7) - agreement is consistency,
not validation; Claude's own view comes last and apart (POS.1370).
Before the note is filed, a script resolves every URL and reports
the dead and the never-existing ones (F10); a note with a
non-resolving citation is not filed until it is removed or marked.
That script is new and is the principal's decision.

What the forge should expect and say aloud (F6, F11): a research of
four agents costs an order of magnitude more than today's single
search; the quality gain the literature measures is real for
independent questions and absent or negative for a tightly coupled
one, so the plan should say when it proposes one agent only; and no
benchmark shows the commercial products reliably ahead of a good
model with search on everyday questions - the principal's word that
"the plan makes the quality" is consistent with the evidence, which
locates the losses in missed context, shallow coverage and broken
citations, not in the searching.

Consult when: the `/research` definition is written (the plan's
fields, the brief's fields, the note's shape, the stop rule); a
research returns thin or junk-filled and the question is whether to
add agents (do not, past four) or change the briefs; a URL check for
reports and notes is designed (THR.0210's guard rail for instance
values is the same step); the question of a "scout before plan"
comes up for a fast-moving topic; a reviewer or research on another
engine is briefed (the brief's fields here are the packet); or the
field is re-checked - this note dates from 2026-10 and the
benchmarks and products move monthly, the API plan-review flags of
Google (04-2026 previews) and the deep-research agents of 2026
being the most perishable facts.

## Sources

Status words: *read* - the page was fetched and its content
extracted in full; *partial* - the first part of a long page
(abstract, or the first 100k characters) only; *summary* - known
only through search-result snippets or a secondary write-up; *not
opened* - the fetch was refused.

1. Anthropic, "How we built our multi-agent research system",
   2025-06-13, https://www.anthropic.com/engineering/multi-agent-research-system - read.
2. Anthropic, `deep-research` skill with `references/researcher.md`
   and `references/report-writer.md`, synced into the user's Claude
   Code installation, undated (2026) - read in full on disk.
3. OpenAI Help Center, "Deep research FAQ",
   https://help.openai.com/en/articles/10500283-deep-research-faq -
   not opened (HTTP 403); quoted via search snippets only.
4. OpenAI, "Introducing deep research", 2025-02-02,
   https://openai.com/index/introducing-deep-research/ - not opened
   (403); its figures taken from [6] and [24].
5. OpenAI Cookbook, "Introduction to deep research in the API -
   agents", archived page, undated,
   https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api_agents - read.
6. Sequoia Capital, "How OpenAI Built its Groundbreaking Deep
   Research Product ft. Isa Fulford", 2025-05-09,
   https://inferencebysequoia.substack.com/p/how-openai-built-its-groundbreaking - read.
7. Google (Dave Citron), "Try Deep Research and our new experimental
   model in Gemini", 2024-12-11,
   https://blog.google/products/gemini/google-gemini-deep-research/ - read.
8. Google, Gemini Deep Research overview page, current (Gemini 3),
   https://gemini.google/overview/deep-research/ - read.
9. Google AI for Developers, "Deep Research agent" (Interactions
   API, previews tagged 04-2026),
   https://ai.google.dev/gemini-api/docs/deep-research - partial.
10. Perplexity, "Introducing Perplexity Deep Research", 2025-02-14,
    https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research - read.
11. Microsoft 365 blog, "Introducing Researcher and Analyst in
    Microsoft 365 Copilot", 2025-03-25,
    https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/ - read.
12. Microsoft Learn, "What is Researcher Agent in Microsoft
    Copilot?", ms.date 2026-02-19,
    https://learn.microsoft.com/microsoft-365/copilot/researcher-agent - read.
13. xAI docs (tools overview, tool usage details, multi-agent),
    https://docs.x.ai/developers/tools/overview - summary; DeepSearch
    itself is undocumented there; the 10-step and "seven layers"
    claims of secondary guides (tryprofound.com, suprmind.ai) are
    uncorroborated.
14. Huang, Y. et al., "Deep Research Agents: A Systematic
    Examination and Roadmap", arXiv 2506.18096 v2, 2025-09-03,
    https://arxiv.org/html/2506.18096v2 - partial.
15. Zhang et al., "Deep Research: A Survey of Autonomous Research
    Agents", arXiv 2508.12752, 2025-08-18 - abstract only.
16. Shao, Y. et al. (Stanford OVAL), "Assisting in Writing
    Wikipedia-like Articles From Scratch with Large Language Models"
    (STORM), NAACL 2024, arXiv 2402.14207 v2,
    https://arxiv.org/html/2402.14207v2 - partial.
17. Jiang, Y., Shao, Y., Ma, D., Semnani, S., Lam, M., "Into the
    Unknown Unknowns" (Co-STORM), EMNLP 2024, arXiv 2408.15232 -
    abstract.
18. GPT-Researcher docs, "Deep Research" and "Config",
    https://docs.gptr.dev/docs/gpt-researcher/gptr/deep_research and
    https://docs.gptr.dev/docs/gpt-researcher/gptr/config - read.
19. LangChain, "Open Deep Research", 2025-07-16,
    https://www.langchain.com/blog/open-deep-research - read; the
    repository README and `configuration.py`,
    https://github.com/langchain-ai/open_deep_research - read
    (Deep Research Bench rank 6, score 0.4344, 2025-08-02).
20. Hugging Face, "Open-source DeepResearch - Freeing our search
    agents", 2025-02-04, https://huggingface.co/blog/open-deep-research - read.
21. Li, X. et al. (RUC-NLPIR), "Search-o1: Agentic Search-Enhanced
    Large Reasoning Models", arXiv 2501.05366, 2025-01-09 - abstract.
22. Li, X. et al. (RUC-NLPIR), "WebThinker", NeurIPS 2025, arXiv
    2504.21776 - summary (search results only).
23. Schmidgall, S. et al. (AMD, JHU), "Agent Laboratory: Using LLM
    Agents as Research Assistants", arXiv 2501.04227 - summary.
24. Han, R., Lee, C.-Y., Pfister, T. et al. (Google), "Deep
    Researcher with Test-Time Diffusion" (TTD-DR), arXiv 2507.16075
    v1, 2025-07-21, https://arxiv.org/html/2507.16075v1 - read.
25. Alibaba Tongyi Lab, "WebWeaver: Structuring Web-Scale Evidence
    with Dynamic Outlines for Open-Ended Deep Research", arXiv
    2509.13312 v3, 2025-10-07 (ICLR 2026 version on OpenReview),
    https://arxiv.org/html/2509.13312v3 - partial.
26. Alibaba-NLP, "WebResearcher" (IterResearch), arXiv 2509.13309
    v2, 2025-09-20 - abstract.
27. Alibaba Tongyi Lab, "Tongyi DeepResearch Technical Report",
    arXiv 2510.24701 v3, 2026-05-18, https://arxiv.org/html/2510.24701 - partial.
28. Moonshot AI, "Kimi-Researcher", 2025-06-20,
    https://moonshotai.github.io/Kimi-Researcher/ - read.
29. USTC group (authors not captured by my fetch), "DeepResearch
    Bench: A Comprehensive Benchmark for Deep Research Agents", arXiv
    2506.11763, 2025-06-13, https://arxiv.org/html/2506.11763 - partial.
30. Sharma, M. et al. (Scale AI), "ResearchRubrics", arXiv
    2511.07685 v1, 2025-11-10, ICLR 2026,
    https://arxiv.org/html/2511.07685v1 - partial.
31. Authors not captured, "LiveResearchBench", arXiv 2510.14240 v5,
    2026-04-18, ICLR 2026, https://arxiv.org/html/2510.14240 - partial.
32. FutureSearch, "Deep Research Bench: Evaluating AI Web Research
    Agents", arXiv 2506.06287, 2025-05/06,
    https://arxiv.org/html/2506.06287 - partial.
33. OpenAI, "BrowseComp: A Simple Yet Challenging Benchmark for
    Browsing Agents", arXiv 2504.12516, 2025-04-16,
    https://arxiv.org/html/2504.12516v1 - read.
34. Gou, B. et al. (OSU), "Mind2Web 2: Evaluating Agentic Search
    with Agent-as-a-Judge", NeurIPS 2025, arXiv 2506.21506 - summary.
35. Authors not captured, "ReportBench: Evaluating Deep Research
    Agents via Academic Survey Tasks", arXiv 2508.15804, 2025-08-14 -
    abstract.
36. Rao, D., Wong, E., Callison-Burch, C., "Detecting and Correcting
    Reference Hallucinations in Commercial LLMs and Deep Research
    Agents", arXiv 2604.03173, 2026-04-03 - abstract.
37. Authors not captured, "Who is the Agent to Blame? Localizing
    Faithfulness and Citation Mistakes in Agentic Deep Research",
    arXiv 2608.24306, 2026-08-25, EMNLP 2026,
    https://arxiv.org/html/2608.24306 - partial.
38. Authors not captured, "PING taxonomy / DeepHalluBench", arXiv
    2601.22984 v3, 2026-10-01, https://arxiv.org/html/2601.22984 - partial.
39. Authors not captured (UC Berkeley group), "Why Do Multi-Agent
    LLM Systems Fail?" (MAST), arXiv 2503.13657 v3, 2025-10-26 -
    abstract.
40. Authors not captured, "Rethinking Multi-Agent Collaboration:
    When More Is Less" (SAIGE), arXiv 2609.19759 v2, 2026-09-18,
    https://arxiv.org/html/2609.19759v2 - read (all but the last
    2k characters).
41. Authors not captured, "WideSeek-R1: Exploring Width Scaling for
    Broad Information Seeking via Multi-Agent Reinforcement
    Learning", arXiv 2602.04634 v3, 2026-03-12 - abstract.
42. Authors not captured, "An Empirical Study of Multi-Agent
    Collaboration for Automated Research", arXiv 2603.29632 v2,
    2026-05-09, https://arxiv.org/html/2603.29632v2 - read.
43. Authors not captured, "IntentRL: Training Proactive User-intent
    Agents for Open-ended Deep Research via Reinforcement Learning",
    arXiv 2602.03468, 2026-02-03 - abstract.
44. NVIDIA, AI-Q Research Assistant Blueprint docs, "Clarifier
    Agent", https://docs.nvidia.com/aiq-blueprint/2.1.0/architecture/agents/clarifier.html - summary.
45. CMU and Amazon, "Deep Research Comparator: A Platform For
    Fine-grained Human Annotations of Deep Research Agents", arXiv
    2507.05495 v2, 2025 (The Web Conference 2026) - summary.
46. "MiroFlow", arXiv 2602.22808, 2026 - summary (single- vs
    multi-agent ablation: multi-agent wins 2 of 3 benchmarks, loses
    on GAIA-Val).
47. Third-party guides to Gemini's plan card: ai-toolbox.co, "How
    to use Gemini Deep Research 2026"; The New School IT, "How to use
    Deep Research in Google Gemini" - summary.
48. Leaderboard aggregators on BrowseComp (benchlm.ai, as of
    2026-07; benchmarklist.com) - summary; unverified against primary
    sources.
49. Press coverage of Deep Research on Gemini 2.5 Pro (Android
    Police via Yahoo Tech, 2025-04) quoting Google's 2-to-1 rater
    preference - summary; vendor claim.
