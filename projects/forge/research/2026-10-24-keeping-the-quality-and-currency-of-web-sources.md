---
date: 2026-10-24
project: forge
topic: keeping the quality and currency of web sources in an agent's research
status: immutable
derived_from: the principal's word of 2026-10-24 (the /research command to show a plan before searching; the research must not slide over the surface nor fill with junk); .claude/skills/research/SKILL.md; research/2026-10-23-a-reviewer-or-a-question-on-another-model-inside-the-forge.md; web sources below
---

# Keeping the quality and currency of web sources in an agent's research

## Question

How does a web-based research keep the quality and currency of its
sources: what the established criteria for judging a source are
(library and information-science frameworks, evidence hierarchies,
primary against secondary against tertiary), how recency is handled,
how findings are triangulated and citations verified (the
hallucinated-citation problem of LLM research and the mitigations
shown to work), how low-quality content is recognised and excluded
today (SEO content farms, AI filler, syndication, affiliate pages,
paywalled or summarised fetches), which instructions to a searching
agent demonstrably raise source quality, and what is known about
search-engine degradation and the share of AI-written text on the web
in 2025-2026.

The baseline it must beat is the current `/research` skill: three
clauses ("prefer primary and high-quality sources; note publication
dates; mark epistemic status consensus vs emerging vs contested") and
no rule on how a source is opened, dated, classified or verified, and
no record per source in the note. The companion note of 2026-10-23
already names the symptom: pages that "came through a summarising
fetch".

## Key findings

**F1. The information-science consensus moved from checklists to
lateral reading; a checklist evaluates the page, lateral reading
evaluates the publisher.** [consensus on the direction; the evidence
base is small studies] CRAAP (Currency, Relevance, Authority,
Accuracy, Purpose; Blakeslee, Meriam Library, 2004) is the checklist
most libraries still teach [1]. Its own field has discredited it as a
method: Caulfield traces the criteria to collection development
("designed - initially - for a single purpose: selecting library
resources on a limited budget") and summarises twenty years of use
with "it did not work"; students applied one criterion, not the set,
and did not "go outside the original document to locate identifying
information", which the experts did [2]; Meola made the same
objection in 2004 [6]. Wineburg and McGrew observed ten professional
fact checkers, ten historians and twenty-five undergraduates on live
sites: the fact checkers were fastest and most accurate because they
left the page at once and read laterally in new tabs about who was
behind it, "took bearings" before reading, and practised "click
restraint" (scanning a result list before clicking); historians and
students read vertically and were fooled by official-looking design
[4, 5]. Teaching the move works: in a matched-section course study
(N = 230) the share of students who both read laterally and judged
trustworthiness correctly rose from about 1% to 14-44% depending on
the task [5]. Caulfield's SIFT (2019) is the operational form: Stop;
Investigate the source ("sixty seconds to figure out where media is
from"); Find better coverage (what the consensus is, from more
trusted or deeper reporting); Trace claims, quotes and media to the
original context [3]. For an agent this means: a source is judged by
what others say of its publisher and by whether its claim survives
tracing upstream, never by its own look, byline or dates.

**F2. Source kind and evidence level are judgments per question, not
labels per document.** [consensus in library and evidence-based
practice] Library guides agree on the three kinds: primary is the
first-hand thing (the document, the data, the standard, the paper);
secondary comments on or interprets it; tertiary compiles (an
encyclopaedia, a textbook, a listicle) - and they stress the kind
depends on the question asked [9]. Evidence hierarchies (OCEBM 2011:
five levels per question type, systematic review of trials at the
top, mechanism-based reasoning at the bottom, graded down for risk
of bias, imprecision, indirectness, inconsistency and up for a large
effect; GRADE: four certainty levels, five downgrading domains) carry
the same two lessons: the hierarchy is per kind of question, and
"no evidence ranking system ... can be used without a healthy dose of
judgment" [7, 8]. Transferred to web research: the primary source of
a vendor fact is the vendor's documentation or changelog, of a
scientific claim the paper, of a regulation its text; a blog, a news
article or a vendor comparison is secondary; a search engine's AI
summary and a fetch-tool summary are tertiary. The note should name
the kind of each source and the kind of evidence behind each
finding.

**F3. Dating a page is multi-signal and every signal can lie; the
age of a link is measurable and a quarter of the web is gone.**
[consensus on mechanics; single sources on the figures] Google reads
a visible labelled date, `datePublished` / `dateModified` structured
data and other factors, and says why it uses several: "Google doesn't
depend on a single date factor because all factors can be prone to
issues" [10]. Anthropic's web search returns a `page_age` ("when the
site was last updated") per result and `cited_text` of up to 150
characters per citation [27]. A "recent timestamp" is one of the
features shown to raise the chance a page is cited by an answer
engine (252,000 controlled trials, six models), which means recency
is a signal publishers manufacture [21]. Pew found 38% of pages that
existed in 2013 gone by October 2023 and a quarter of all pages from
2013-2023 inaccessible; 23% of news pages and 21% of government pages
carried a broken link [15]. Rao et al. operationalise the difference
between a dead and an invented link: a URL that fails and has a
Wayback Machine snapshot is "stale", one with no snapshot ever is
"likely hallucinated" [16]. On which fields age in months: Google's
own freshness categories are recent events, regularly recurring
events and "frequently updated information" (its 2011 freshness
change touched about 35% of queries by one measure, 6-10%
noticeably) [14]; Anthropic's tool guidance classifies as
search-worthy "current prices, rates, scores, or statistics" and
"information about specific organizations, people, or products that
might have changed", against "established facts, math, science
fundamentals" [27]. This note found no study quantifying a staleness
half-life per field; the practical rule is the kind of claim, not a
number of months: a figure, a price, a version, a count, a market
share or a product capability is dated by its youngest source and
said to be so, a principle or a mechanism is not. The AI-share figures
of F6 are the demonstration: the web's composition moved from 36% to
about 50% AI-written articles within two years [35].

**F4. Citations of retrieval-free models were fabricated at 18-55%;
retrieval cut fabrication but moved the failure to wrong, dead,
syndicated and unsupported citations, and the agents that cite most
fabricate most.** [emerging: 2025-2026 preprints and two journalism
audits, consistent in direction] Without retrieval, 55% of GPT-3.5's
and 18% of GPT-4's bibliographic citations did not exist, and 43% and
24% of the real ones had substantive errors (Scientific Reports,
2023; verified against Google Scholar, Scopus, WorldCat, PubMed and
publisher sites) [23]. With retrieval, the Tow Center ran 1,600
queries against eight answer engines in February 2025: over 60%
wrong overall (Perplexity 37%, Grok 3 94%); more than half of the
Gemini and Grok 3 responses cited fabricated or broken URLs (Grok 3:
154 of 200 citations led to error pages); tools cited syndicated
copies instead of originals (Yahoo copies of USA Today, republished
Texas Tribune pieces) and answered from paywalled content their
crawlers were blocked from; ChatGPT hedged in 15 of 200 answers and
never declined; licensing deals brought no accuracy [24]. The EBU and
BBC had journalists of 22 public broadcasters in 14 languages grade
over 3,000 answers in 2025: 45% had at least one significant issue,
31% sourcing problems (missing, wrong or unsupporting sources), about
20% accuracy problems including outdated information [25]. On deep
research agents: across 53,090 URLs on DRBench, 3-13% of cited URLs
were hallucinated and 5-18% non-resolving; deep research agents cite
far more (113 and 41 URLs per query against 3-24) and hallucinate
more (10.7% pooled against 4.8%); Gemini 2.5 Pro deep research 13.3%
hallucinated against OpenAI deep research 3.5%, whose failures were
mostly stale links, "evidence of genuine retrieval" [16]. A second
framework fetched every cited page of 14 models and scored it: link
validity above 94% and relevance above 80% for the strongest, but
factual accuracy of the claim against its own source only 39-77%;
scaling tool calls from 2 to 150 lowered fact-check accuracy by about
42% - more searching did not make citations truer [17]. A
trajectory-level audit of six agents found reliability gaps in all,
the dominant cause hallucination propagating from one step to the
next [18]. A study of four consumer agents found 14-53% of claims
resting on sources searched but not cited, 15-20% of claims
ungrounded, and that "more frequent Web-search invocation does not
necessarily yield better response quality" [19]. LLM search engines
cite more diverse domains than Google (37% unique to them) but "do
not outperform" it on credibility, neutrality or safety [20].
Browsing raised calibration error in BrowseComp: access to the web
increased confidence in wrong answers [33]. OpenAI said of its own
product that it "may struggle with distinguishing authoritative
information from rumors, and currently shows weakness in confidence
calibration" [30]; an independent evaluation found it "frequently
prioritizes company blogs and SEO-spam over authoritative sources"
[32].

**F5. The mitigations with evidence are mechanical: resolve the URL,
classify it by archive, fetch the page and check the claim against
it; the gap no check closes is omission.** [emerging, with one
controlled result] Giving models a URL-liveness tool and letting them
self-correct cut non-resolving citations 6-79 times, to under 1%
(GPT-5.1 16.0% to 0.6%, Gemini 2.5 Pro 6.1% to 0.1%, Claude Sonnet
4.5 4.9% to 0.8%); a small model called the tool and ignored its
answer, so the gain depends on the model acting on the check [16].
Fetching the cited page and scoring the claim against it is the
evaluation method of [17] and [22], and the production method of
Anthropic's research system, which ends with a CitationAgent that
"identifies specific locations for citations" so that claims are
attributed to sources [26]. Willison's reading of the OpenAI card
holds for every such check: following the references catches most
fabrications; "misinformation by omission" - what the searches never
reached - cannot be seen in the report [31, 32]. Triangulation is
therefore two different things: agreement of independent primaries
raises confidence, agreement of copies and aggregators does not (F7),
and no agreement shows what was missed; the note must say what it
looked for and did not find.

**F6. Search results are measurably degraded by affiliate spam,
anti-spam updates hold only temporarily, and about half of new web
articles are machine-written, though they rank and get cited less.**
[the Webis study single but uncontested in substance; the AI-share
figures contested in method] The Leipzig and Weimar group tracked
7,392 product-review queries on Google, Bing and DuckDuckGo for a
year: "only a small portion of product reviews on the web uses
affiliate marketing, but the majority of all search results do";
higher-ranked pages were "more optimized, more monetized with
affiliate marketing, and they show signs of lower text quality"; all
three engines "fall victim to large-scale affiliate link spam
campaigns"; spam updates had a "temporary positive effect" in "a
constant battle" of "review spam entering and exiting search
results"; the line between benign content and spam "is becoming
increasingly blurred, and this situation is sure to worsen with the
advent of generative AI" (ECIR 2024) [34]. No follow-up by the group
was found; Google has since run spam updates in March and September
2026 against "scaled content abuse" [search coverage, not cited].
Google's spam policies define the kinds to exclude: scaled content
abuse ("many pages ... generated for the primary purpose of
manipulating search rankings", however produced), site reputation
abuse (third-party content on a host "mainly because of that host's
already-established ranking signals"), expired domain abuse, thin
affiliation (descriptions and reviews "copied directly from the
original merchant"), scraped content, doorway pages [11]; its rater
guidelines gained the first three in January 2025 and name generative
AI as one tool of scaled abuse while saying AI use alone does not
set the rating [13]; its stated principle since 2023 is to reward
quality "however it is produced" and to treat automation "with the
primary purpose of manipulating ranking" as spam [12]. On the share
of AI text, the estimates are not comparable because they measure
different things with disputed detectors: Graphite (55,400 Common
Crawl articles, three detectors averaged, false positives 1.4-1.8%)
finds "primarily AI" articles at 35.9% twelve months after ChatGPT,
about 48% at twenty-four, and a plateau near 50% since Q1 2025 (50.9%
in Q4 2025, 49.9% in Q1 2026), hypothesising the plateau is because
AI articles perform poorly in search [35]; its October 2025 study
found 86% of Google's ranking articles and 82% of articles cited by
ChatGPT and Perplexity human-written [36]; Ahrefs finds 74.2% of
900,000 new pages of April 2025 containing some AI text but only 2.5%
pure AI [37]; an Internet Archive study estimates about 35% of new
websites AI-generated or AI-assisted by mid-2025 and finds no
significant drop in factual accuracy, with a reviewer flagging the
detector unvalidated [38]. NewsGuard's tracker counts 3,749 "AI
Content Farm" news sites in 16 languages (June 2026; 49 in May 2023)
by four criteria that are a usable exclusion test: a substantial
share of AI content, published without meaningful oversight (leftover
chatbot error text), presented as human-run, undisclosed [39]. The
one safe reading: machine text is now about half of what is newly
published, a search result list still filters most of it, and a fetch
of an arbitrary page does not.

**F7. Copies are cited instead of originals, canonical tags are a
hint, and the cure is to go upstream.** [consensus in practice;
mechanism evidence thin] The Tow Center documented engines citing
syndicated and republished copies (F4) [24]; Bing's webmaster
guidance asks syndication partners for a canonical tag to the
original and prefers excerpts with a link back, and practitioners
note a canonical is "just a hint" [40]. Caulfield's "go upstream" and
SIFT's "trace to the original context" are the rule: the citation is
the first publisher, and a copy is cited only when the original is
unreachable, said as such [3].

**F8. A summarised or truncated fetch is a tertiary source wearing a
primary's URL, and bot-blocking makes "not opened" a normal state.**
[single sources, one of them this run] Claude Code's WebFetch
"answers `prompt` against it using a small fast model" by its own
description [41]; a filed report shows the summariser returning the
headline ("book 2 months ahead") of a page that listed three stores
with 35-, 60- and 61-day windows, the main model writing wrong dates
from it, and the issue closed "not planned" with the reporter asking
that dropped content be flagged [41]. In this run, a PDF came back as
an unreadable binary, four pages returned 403 (Stanford News, OpenAI,
Oxford CEBM, a blog), two long pages returned only their navigation
within the first 100,000 characters; Rao et al. exclude 403s as
"likely bot-blocking" [16]. Paywalls cut the other way: engines
answered from paywalled text their crawlers were barred from [24].
Users of such tools report they cannot tell whether a whole document
was read [search coverage]. For a note this means a source carries
how it was read (in full, partially with the range, through a
summarising fetch, not opened) and a finding that rests on a summary
alone says so.

**F9. What the vendors tell their own searching agents, and what is
shown to work.** [vendor reports, single-source each; no controlled
prompting study found] Anthropic reports that early agents
"consistently chose SEO-optimized content farms over authoritative
but less highly-ranked sources" and that "adding source quality
heuristics to our prompts helped resolve this issue"; its agents
"start wide, then narrow down" ("short, broad queries, evaluate
what's available, then progressively narrow"); its LLM judge scores
"source quality (did it use primary sources over lower-quality
secondary sources?)"; effort is scaled to the question ("simple
fact-finding requires just 1 agent with 3-10 tool calls") [26]. The
researcher briefing of Anthropic's shipped deep-research skill is the
most concrete vendor text found: fetch the full content of promising
pages because "snippets from search are easy to take out of context";
before including a finding ask whether it is speculation ("could",
"may", future tense), whether "this is the original source or an
aggregator? Prefer primary sources", whether the source is "generally
problematic (using false authority, pairing passive voice with
nameless sources, using general qualifiers without specifics,
parroting unconfirmed reports)"; "for recent topics, defer to search
results over your training data"; name conflicts explicitly, "don't
silently pick a conflicting source"; "noting 'I found no reliable
sources on X' communicates valuable signal"; every fact carries an
inline source or moves to a Gaps section; the report writer drops any
unsourced quantitative claim ("a report with 5 well-sourced claims is
better than one with 20 claims where half are unsourced"); about ten
tool calls, never above fifteen [28]. Google's Deep Research shows
its plan to the user to refine before it searches, then runs
sub-tasks in parallel or sequence [42]; the plan-first the principal
asked for is the vendors' practice. Anthropic's claude.ai system
prompt (September 2026) carries only the knowledge-cutoff rule
(say when knowledge "could be superseded" and point to search), no
source rules [29]. The closest controlled evidence on instructions is
negative: more tool calls lowered citation accuracy [17], more
searching did not raise quality [19], browsing raised overconfidence
[33]. Fewer, better-chosen openings beat breadth.

## Options

**A. Rules in the briefing only.** The agents' brief gains the
heuristics of F1, F2, F7, F9 as prose; the note's shape stays. Pro:
cheapest; Anthropic reports exactly this fixed the content-farm
choice [26]. Con: unverifiable after the fact; a note cannot be
checked for what its agent did not record; the summarising-fetch
problem (F8) stays invisible.

**B. Rules plus a record per source and per finding.** As A, and
the note records for every source its kind (primary / secondary /
tertiary), its date and how the date was found, how it was read (in
full, partially, summarised fetch, not opened), and whether it is the
original or a copy; every finding carries its epistemic status and
the kind of evidence behind it; a Gaps section says what was looked
for and not found. Pro: the quality of a note becomes auditable by a
reader and by a check; the shape is what Anthropic's own researcher
briefing demands [28]. Con: longer notes; the agent spends calls on
opening pages it would otherwise cite from a snippet (the cost is the
point).

**C. B plus mechanical verification at filing.** A script resolves
every cited URL, classifies failures as stale or likely hallucinated
by the Wayback Machine, and checks that each quoted passage occurs in
the fetched page; a failed URL or quote is returned to the agent (the
self-correction of [16]) or marked in the note. Pro: the one
mitigation with a measured effect (6-79 times fewer dead links); fits
the forge's line that a check is a program (THR.0530) and the shape
check of the companion note (F4 there). Con: a script to write and
maintain; 403 bot-blocking and paywalls produce noise that must be
labelled "unverifiable", not "wrong"; a quote check needs the agent
to quote, which the forge's copyright-conscious tools cap at short
passages anyway.

**D. Domain allow-lists or block-lists.** Anthropic's tool supports
both [27]. Pro: deterministic. Con: an allow-list kills discovery and
is a count-like rule against the forge's "kind, not count"; a
block-list chases 3,749 moving sites [39]. Not recommended as a rule;
a per-research block of a domain the principal names is fine.

**E. A second engine on the same question as triangulation.** The
companion note's mechanism. Pro: a different family, different blind
spots. Con: two engines citing the same copy is consistency, not
validation (POS.0790); it does not replace B or C.

## Relevance to this project

Recommendation: **B now, C as the next program**, E when the
companion note's script exists. In detail:

The agents' briefing (one question, one agent) demands:

1. Plan first, in the open: the questions, the kinds of source
   expected for each (the standard, the vendor doc, the paper, the
   audit), and what would count as not found; the principal confirms
   before any search (his word; Google's product does the same [42]).
2. Start wide, then narrow: short broad queries, read the result
   list before opening anything (click restraint), then open [26, 4].
3. Open the page or do not cite it: no finding from a search snippet
   or a search engine's summary; a summarising fetch is read as a
   tertiary source and said to be one; a page that would not open is
   listed as not opened, never cited for content [28, 41, 16].
4. Go upstream: cite the first publisher; a copy, a syndication, an
   aggregator or a vendor's write-up of someone else's result is cited
   only when the original is unreachable, and then as a copy [3, 24].
5. Read laterally before reading: who publishes this, what others
   say of them, what they sell; a page's own look, byline and dates
   count for nothing [4, 2].
6. Exclude by kind, not by list: affiliate and review pages whose
   content comes from the merchant, pages mass-produced without
   oversight (chatbot residue, no author, no date, generic name),
   third-party content riding a host's reputation, SEO-vendor blogs
   on their own market, undated pages for any time-sensitive claim
   [11, 39]; a vendor's own documentation about its own product is a
   primary source and is used.
7. Classify each source: kind (primary / secondary / tertiary), date
   and how dated (byline, structured data, archive snapshot, none),
   how read (full / partial with range / summarised / not opened),
   original or copy; classify each finding: consensus / emerging /
   contested / single source, with the kind of evidence named
   (controlled study, audit, vendor report, practitioner claim) [9,
   7, 8, 10].
8. Separate fact from speculation and conflict from agreement: future
   tense and "could" are speculation; two sources that disagree are
   both named; agreement of copies is not agreement [28, F7].
9. Say what was not found: "no reliable source on X" is a finding
   and goes into a Gaps section; a figure with no source is a gap,
   never an estimate [28, 31].
10. Keep the opening count modest and spend it on primaries: roughly
    ten to fifteen openings; more calls have been measured to lower
    accuracy, not raise it [17, 19, 28].
11. Never fabricate a source, a quote, a date or a figure; a quote is
    verbatim and short, with where in the page it stands.

The note's rules: every source in the Sources list with title,
author or organisation, date (and how known), URL, kind, how read,
original or copy; every finding with its status and its sources
inline; a Gaps paragraph; the youngest source's date named beside
any time-sensitive figure; the agent's search plan kept as a short
record so a reader sees what was looked for.

The synthesis (Claude, on the agents' return) checks before filing:
every cited URL resolves (by hand now, by the script of C later; a
403 is "unverifiable", not wrong); every quoted passage is in the
page; no finding rests on a snippet or a summarised fetch alone
without saying so; agreement across agents is reported as
consistency, never validation; the date of the youngest source per
time-sensitive finding; what every agent reported not finding, put
together. A note that fails these is returned to its agent as a
failed run, not filed - the same rule the companion note sets for a
reviewer's report shape.

What belongs to the intent (through `/forge intent`, not here): the
plan-first step of `/research`; the per-source record as part of the
research note's template; the mechanical check of C as a program
under THR.0530; the kind-based exclusion list as a rule of kind.

Consult when: writing or changing the `/research` skill and its
agents' briefing; adding a check for research notes; judging a source
the principal brings in through `/ingest`; deciding whether a finding
of an older note is stale (F3); reading any number about the web's
composition or an engine's behaviour (F6: the method decides what the
number means).

## Sources

1. "Evaluating Information: Applying the CRAAP Test", Sarah
   Blakeslee, Meriam Library, CSU Chico, LOEX Quarterly 31(3), 2004;
   as reproduced in library guides (Manchester Metropolitan,
   Princeton). Via search summaries only, not opened.
   https://libguides.princeton.edu/medialiteracy/craaptest
2. "A Short History of CRAAP", Mike Caulfield, hapgood.us,
   2018-09-14. Read in full.
   https://hapgood.us/2018/09/14/a-short-history-of-craap/
3. "SIFT (The Four Moves)", Mike Caulfield, hapgood.us, 2019-06-19.
   Read partially (first 100,000 characters).
   https://hapgood.us/2019/06/19/sift-the-four-moves/
4. "Lateral Reading and the Nature of Expertise: Reading Less and
   Learning More When Evaluating Digital Information", Sam Wineburg
   and Sarah McGrew, Teachers College Record 121(11), 2019 (working
   paper, Stanford History Education Group, 2017). Not opened
   (paywall; Stanford News returned 403); sample and findings via
   search summaries of Stanford News 2017-10-24 and the introduction
   of [5]. https://purl.stanford.edu/yk133ht8603
5. "Improving college students' fact-checking strategies through
   lateral reading instruction in a general education civics course",
   Brodsky, Brooks, Scimeca, Todorova, Galati, Batson, Grosso,
   Matthews, Miller, Caulfield, Cognitive Research: Principles and
   Implications 6:23, 2021-03-31. Read in large part (first 100,000
   characters). https://pmc.ncbi.nlm.nih.gov/articles/PMC8012470/
6. Marc Meola, "Chucking the Checklist", portal 4(3), 2004; via
   secondary summaries (ACRL C&RL News "Rethinking CRAAP"), not
   opened. https://crln.acrl.org/index.php/crlnews/article/view/24195
7. "OCEBM Levels of Evidence", OCEBM Levels of Evidence Working
   Group, Oxford Centre for Evidence-Based Medicine, 2011. Not opened
   (403); content via the Introduction document 2.1 and secondary
   tables in search summaries.
   https://www.cebm.ox.ac.uk/resources/levels-of-evidence/ocebm-levels-of-evidence
8. GRADE certainty of evidence: CDC ACIP GRADE Handbook, chapter 7,
   and BMJ Best Practice "What is GRADE?". Via search summaries, not
   opened.
   https://www.cdc.gov/acip-grade-handbook/hcp/chapter-7-grade-criteria-determining-certainty-of-evidence/
9. Library guides on primary, secondary and tertiary sources (CUNY
   CSI, James Cook University, UW-La Crosse, Virginia Tech). Via
   search summaries, not opened.
   https://library.csi.cuny.edu/psychology/primary-secondary-tertiary
10. "Provide a publication date to Google Search", Google Search
    Central documentation, undated page. Read in full.
    https://developers.google.com/search/docs/appearance/publication-dates
11. "Spam policies for Google web search", Google Search Central,
    last updated 2026-08-28. Read in full.
    https://developers.google.com/search/docs/essentials/spam-policies
12. "Google Search's guidance about AI-generated content", Google
    Search Central Blog, 2023-02-08. Read partially (body reached at
    offset 200,000).
    https://developers.google.com/search/blog/2023/02/google-search-and-ai-content
13. Google Search Quality Rater Guidelines, editions of 2025-01-23
    and 2025-09-11; via secondary coverage (ppc.land, SEOZoom), not
    opened. https://ppc.land/search-quality-rater-guidelines/
14. "Giving you fresher, more recent search results", Google Inside
    Search blog, 2011-11-03, with the 2011-11-07 clarification. Body
    did not render through the fetch; figures via Search Engine
    Watch, 2011-11-04.
    https://www.searchenginewatch.com/2011/11/04/google-gets-fresh-with-algorithm-update-affecting-35-of-searches/
15. "When Online Content Disappears", Pew Research Center, 2024-05-17.
    Via search summary carrying the report's sentences, not opened.
    https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/
16. "Detecting and Correcting Reference Hallucinations in Commercial
    LLMs and Deep Research Agents", Delip Rao, Eric Wong, Chris
    Callison-Burch, arXiv 2604.03173, 2026-04-03. Abstract read in
    full, body partially (first 100,000 characters).
    https://arxiv.org/abs/2604.03173
17. "Cited but Not Verified: Parsing and Evaluating Source Attribution
    in LLM Deep Research Agents", Onweller, Lumer, Huber, Ramchandani,
    Subbiah, Feld, arXiv 2605.06635, 2026-05-07. Abstract read.
    https://arxiv.org/abs/2605.06635
18. "Why Your Deep Research Agent Fails? On Hallucination Evaluation
    in Full Research Trajectory", Zhan, Fan, Huang, Guo, Huang, arXiv
    2601.22984, v1 2026-01-30, v3 2026-10-01. Abstract read.
    https://arxiv.org/abs/2601.22984
19. "Characterizing Web Search by Conversational LLM Agents: From
    Search Decisions and Strategies to Results and Responses", Amani
    et al. (12 authors, MPI-SWS and others), arXiv 2609.19244,
    2026-09-16. Abstract and body partially (first 100,000
    characters). https://arxiv.org/abs/2609.19244
20. "Source Coverage and Citation Bias in LLM-based vs. Traditional
    Search Engines", Zhang, Ye, Peng, Garimella, Tyson, arXiv
    2512.09483, 2025-12-10. Abstract read.
    https://arxiv.org/abs/2512.09483
21. "What Gets Cited: Competitive GEO in AI Answer Engines",
    Vishwakarma, Kumar, Jamidar, arXiv 2605.25517, 2026-05-25.
    Abstract read. https://arxiv.org/abs/2605.25517
22. "ReportBench: Evaluating Deep Research Agents via Academic Survey
    Tasks", Li, Zeng, Cheng, Ma, Jia, arXiv 2508.15804, 2025-08-14.
    Abstract read. https://arxiv.org/abs/2508.15804
23. "Fabrication and errors in the bibliographic citations generated
    by ChatGPT", William H. Walters and Esther Isabelle Wilder,
    Scientific Reports 13:14045, 2023-09-07. Read.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980/
24. "AI Search Has a Citation Problem", Klaudia Jaźwińska and Aisvarya
    Chandrasekar, Tow Center for Digital Journalism, Columbia
    Journalism Review, 2025-03-06. Read in full.
    https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
25. "News Integrity in AI Assistants", EBU and BBC with 22 public
    service media, 2025-10-21. Landing page read; report PDF not
    opened; the 45% / 31% / 20% figures via the BBC release as
    reported by InfoDocket and NPR.
    https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants
26. "How we built our multi-agent research system", Anthropic
    Engineering, 2025-06-13. Read in full.
    https://www.anthropic.com/engineering/multi-agent-research-system
27. "Web search tool", Claude Platform documentation, Anthropic,
    undated (tool versions to 2026-03-18). Read in full.
    https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
28. Anthropic deep-research skill, `references/researcher.md` and
    `references/report-writer.md`, as synced into this Claude Code
    installation (skills/synced/.../deep-research/). Read in full.
    Local files; no URL.
29. "Claude Opus 5.5 system prompts", release notes, Anthropic, entry
    of 2026-09-22. Read in full; no web-search instructions in it.
    https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5
30. "Introducing deep research" and "Deep research system card",
    OpenAI, February 2025. Not opened (403); the limitation sentence
    via contemporaneous press (Reuters syndication, 2025-02-02) and
    [31]. https://openai.com/index/deep-research-system-card/
31. "Deep research System Card", Simon Willison's weblog, 2025-02-25.
    Read in full.
    https://simonwillison.net/2025/Feb/25/deep-research-system-card/
32. FutureSearch, evaluation of OpenAI Deep Research, February 2025;
    via the LongTermWiki summary, not opened.
    https://www.longtermwiki.com/resources/386bc4dbf25d7d34
33. "BrowseComp: A Simple Yet Challenging Benchmark for Browsing
    Agents", OpenAI, arXiv 2504.12516, 2025-04. Via search snippet
    only, not opened. https://arxiv.org/pdf/2504.12516
34. "Is Google Getting Worse? A Longitudinal Investigation of SEO Spam
    in Search Engines", Janek Bevendorff, Matti Wiegmann, Martin
    Potthast, Benno Stein, ECIR 2024, LNCS pp. 56-71. PDF fetched but
    unreadable as text; abstract sentences via GIGAZINE 2024-01-17
    (read) and 404 Media 2024-01-16 (read).
    https://downloads.webis.de/publications/papers/bevendorff_2024a.pdf
35. "AI Now Writes as Many Online Articles as Humans Do", Graphite
    Five Percent research, 2026-05-15. Read in full.
    https://graphite.io/five-percent/research/ai-now-writes-as-many-online-articles-as-humans-do
36. Graphite, study of AI articles in Google results and ChatGPT and
    Perplexity citations, October 2025; via Axios 2025-10-14 and
    press summaries, not opened.
    https://www.axios.com/2025/10/14/ai-generated-writing-humans
37. "74% of New Webpages Include AI Content (Study of 900k Pages)",
    Ryan Law, Ahrefs, 2025-05-19. Via search summary, not opened.
    https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated
38. "The Impact of AI-Generated Text on the Internet", Dolezal, Alam,
    Graham, Bohacek, arXiv 2604.26965, 2026-04-14. Abstract read.
    https://arxiv.org/abs/2604.26965
39. "Tracking AI-enabled Misinformation: AI Content Farm sites",
    NewsGuard AI Tracking Center, last updated 2026-06-23. Read.
    https://www.newsguardtech.com/special-reports/ai-tracking-center/
40. "Does Duplicate Content Hurt SEO and AI Search Visibility?", Bing
    Webmaster Blog, December 2025. Via search summary, not opened.
    https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility
41. Claude Code issue 50647, "WebFetch summarizer model drops critical
    details from static HTML pages", opened 2026-04-19, closed
    2026-06-16 "not planned". Read; and the WebFetch tool's own
    description in this session.
    https://claudeissues.com/issue/50647-bug-webfetch-summarizer-model-drops-critical-details-from-static-html-pages
42. "Deep Research" overview, Google Gemini, undated. Via search
    summary, not opened.
    https://gemini.google/overview/deep-research/
