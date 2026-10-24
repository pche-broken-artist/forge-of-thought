---
date: 2026-10-24
project: forge
topic: how buyer-side tools generate an RFP from requirements today, and what they leave to people
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-24-rfp-from-the-chain/card-6-buyer-side-tools
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-6-buyer-side-tools; web sources below
---

# Buyer-side tools assemble an RFP from a template, a prompt and the buyer's answers; no tool opened derives it from a requirements document set, and every tool leaves the substance and the evaluation criteria to people

## In short

Six buyer-side tools were read from their own documentation: SAP
Ariba Sourcing, Zip Sourcing, JAGGAER, DeepStream, Procol's RFP
generator and Globality's Glo, plus a Microsoft Copilot training
demo that builds an RFP from a project document. None of them takes
a structured requirements document and maps its items to the
sections of an RFP. What they take is a template with event rules
(SAP Ariba, JAGGAER), an intake or purchase request (Zip), a short
prompt or uploaded documents read as text (DeepStream, Copilot), a
form with a requirements table and weighted criteria (Procol), or a
scoping conversation whose suggested answers the buyer accepts or
rejects one by one (Globality). What they produce is a structured
draft - sections, questions, event rules, a brief - that every
vendor tells the buyer to review before use. The evaluation
criteria and their weights are in every opened case a human input
or an extraction from a document the human wrote, never a
derivation. The only independent hands-on review found is a 2023
test of three general chatbots: a useful starting point, two of
three lacking "depth or specificity", human input "required to
cover all bases". The disconfirming query found no review saying
the tools emit boilerplate, but also no review saying they do not:
the field has vendor claims and one dated practitioner test, and
the vendors themselves concede that the substance is the buyer's.
The one unexpected find: the market's "generation" has the shape of
a render - sources plus a template plus instructions - not of a new
artefact; and a Coupa agent said to create RFP events from
contracts and requisitions could not be opened (403) and stays a
lead.

## Question

Card 6: how buyer-side tools generate an RFP from requirements
today, and what they leave to people.

- Question: What buyer-side sourcing platforms and AI RFP
  generators (the buyer's side only: tools that write and issue an
  RFP, never tools that answer one) take as input, what they
  produce automatically, what they ask the user to supply, and what
  independent reviews say of the result; against the alternative
  that no tool derives an RFP from requirements documents and all
  start from a questionnaire.
- Why it matters: The market's answer to "what can be derived
  automatically"; a derivation the market already sells need not be
  invented, and one it cannot sell is a warning.
- What would answer it: The vendors' own documentation of inputs
  and outputs (vendor claims) and independent reviews of the
  results.
- Where to look: buyer-side sourcing platforms' documentation
  (strategic sourcing modules of the large procurement suites,
  RFP-issuing tools), AI RFP generators aimed at buyers, analyst and
  user reviews; more than one route. Known items: at least two named
  buyer-side tools with their inputs and outputs described; one
  independent review of an AI-generated RFP.
- Disconfirming query: Expected: tools derive sections from
  requirements. Search for the opposite: reviews saying the tools
  produce boilerplate and the substance is still typed in.
- Stop rule: Nothing new from a differently-worded query, and each
  perspective of the card (procurement officer, evaluator) has a
  primary source; or about fifteen openings spent.

The baseline the note must beat: the planner's expectation that the
tools derive RFP sections from requirements, and its alternative
that none does and all start from a questionnaire. The note must
say, tool by tool and from the vendor's own page, what goes in and
what comes out, and whether anyone independent has judged the
result.

## Key findings

F1. **No buyer-side tool opened derives an RFP from a structured
requirements document; the inputs are a template, a request, a
prompt, a form or a conversation.** [consensus across the vendor
documentation opened; vendor claims, vendor documentation] SAP
Ariba Sourcing builds an RFP from a template, "a set of rules and
content that determines the functionality and initial content of a
particular event", and the event content "may be populated with
data from a sourcing request, the sourcing library, or a previous
event" (Creating a Quick Project, step 4) [5]. Zip Sourcing starts
from intake: "quick conversion of a purchase request to an RFx with
just one click", and its AI does "AI-driven event creation,
transforming this manual process by instantly importing and
generating RFx content" (section Autonomous Sourcing) [4]; its
current walkthrough says only that it "Launches RFx events directly
from intake requests" [10]. DeepStream says "Upload your files or
describe what you need" and that its assistant "helps you draft a
complete, structured RFP from a short prompt or supporting
documents" and can "update line items from an uploaded tender/spec"
(section eSourcing AI RFP generation) [2]. Procol's generator is a
form: five required fields (project title, issuing organisation,
scope of services, proposals due, contact), nine optional, a table
of key requirements with a priority each, and evaluation criteria
with weights, followed by "targeted follow-up questions" (How it
works, step 2); no document upload is mentioned [7]. Globality's Glo
"asks relevant scoping questions" and the buyer "can with a single
click accept or reject its high-quality suggested answers" (section
Glo creates briefs for you) [9]. The Copilot demo is the one case
where a requirements document is the input: "Using the project
requirements outlined above, draft an RFP using the following
template: [Contoso_RFP_Template.docx]" (Copilot Chat, step 5), after
a prompt that summarises the guidelines document into objectives,
scope, timeline, budget, compliance needs and selection criteria
[8]. The document is read as prose; no tool opened speaks of
requirement items carried into the RFP with their identity.

F2. **What comes out automatically is a structured draft: sections,
questions, event rules and line items; the vendors describe the
shape, not the substance.** [consensus among vendor pages; vendor
claims] DeepStream: "builds the full RFP in under a minute, then
tweak where required and launch" (hero), "Add new sections in
seconds (like ESG or safety compliance)" [2]. Procol: a preview "10
sections, written for you", the examples shown Introduction,
Background, Objectives, Scope of services; the ten sections are not
listed [7]. Globality: a brief that "can immediately be sent to
best-fit suppliers" and "a polished, more complete version of your
short phrase answers" [9]. SAP Ariba: the template fixes the event
rules, each "delegated to the event creator, read-only, or hidden"
(step 2) [5]. JAGGAER's shipped automation in 25.3 is "Bulk RFx
templates import that launches dozens or hundreds of events from one
file" (customer benefits bullets); AI drafting is roadmap: "JAI
Assist will expand from guided help to a more comprehensive
self-service enablement" in 26.1 [6]. The 2023 chatbot test produced
question lists: ChatGPT 3.5 gave 24 questions in six groups
(technical capabilities, user experience, integration and APIs,
security and compliance, pricing, licensing); Bing and Bard about
half as many [1].

F3. **The evaluation criteria and their weights are a human input
or an extraction from a document a human wrote; no tool opened
derives them.** [consensus among the pages that mention criteria at
all; vendor documentation] Procol asks for criterion and weight
("Weights should add up to 100%") as an input, while its FAQ lists
evaluation criteria among what it can generate - the page is not
consistent on this point [7]. The Copilot demo extracts them from
the guidelines: "Extract and summarize the key vendor selection
criteria from this document, including weight percentages and
evaluation factors" (Copilot Chat, step 4) [8]. Zip offers "guided
scoring, side-by-side vendor evaluations" without saying where the
scoring comes from [4]. SAP Ariba's lesson does not describe
scoring at all; its default RFP templates use "closed bidding,
meaning suppliers cannot see competitive information like the
current lead bid" [5]. Globality says its engine "provides best-fit
suppliers derived from unbiased multidimensional analysis" and does
not describe scoring of proposals [9].

F4. **Every vendor hands the substance and the review back to the
buyer, in its own words.** [consensus; vendor documentation] Procol
under its Generate button: "AI can make mistakes. Review the draft
before you use it." and "Procol is not responsible for the generated
text or how it is used."; its FAQ tells the user to "Check the RFP
for completeness, accuracy, and clarity" [7]. DeepStream, step 3:
"Iterate with the assistant (or tweak manually) until it is ready
for review and send" [2]. Globality: accept or reject each
suggestion [9]. DeepStream names chasing stakeholders for "one more
requirement" as a pain point and does not claim to solve it [2].

F5. **The one independent hands-on review found judges AI-drafted
RFP content a starting point that still needs a person for depth
and specificity.** [single source; practitioner test, 2023, general
chatbots, not a buyer-side platform] Joanna Martinez (Cloud Wars,
2023-09-11) gave ChatGPT 3.5, Bing AI and Bard the key facts of a
content-management-system purchase and compared them with her own
RFP: ChatGPT was "the most capable and reliable tool", Bing and Bard
"neither went far enough in depth or specificity", and under the
heading "AI is a great starting point but human intervention is
still required" she concludes that "thorough evaluation and
customization are necessary" and "human experience and input are
required to cover all bases" [1]. No independent review of a
platform's AI-generated RFP (SAP Ariba, Coupa, JAGGAER, Zip,
DeepStream, Globality) was found for 2024 to 2026 (Not found).

F6. **The analyst frame of the category, as far as it could be read,
names RFx support and automation of "parts of the sourcing process",
not generation from requirements.** [single source, a vendor's copy
of analyst excerpts; tertiary] Market Dojo's post of 2025-02-27
quotes the Gartner Market Guide for Sourcing Applications of
2025-01-30: "Standard sourcing applications support requests for
proposal, information, and quote (RFx)" and "An autonomous sourcing
solution uses AI and machine learning to automate parts of the
sourcing process"; the post's own words, not Gartner's, speak of
"increasing adoption of AI, automation, and generative AI (GenAI)"
[3]. The Gartner text itself was not opened; a second vendor copy of
the 2026 guide returned 404 (Opened and not used).

F7. **The card's alternative - all tools start from a questionnaire
- holds for half the field and not for the other.** [the agent's
reading of F1; vendor documentation] Procol and Globality start from
a form or a scoping conversation [7][9]; SAP Ariba and JAGGAER from
a template and a library [5][6]; Zip from an intake request [4][10];
DeepStream and the Copilot demo accept documents and prompts [2][8].
Both routes exist in the market. What no opened route offers is the
step between them: a document of requirement items becoming RFP
sections with the items still traceable.

Disconfirming query. Three wordings were run (a review of boilerplate
in AI-generated RFPs; ChatGPT-written RFPs as generic boilerplate; a
buyer's complaint of a generic template and requirements still typed
by hand). None returned an independent review in either direction;
the results were vendor pages that promise tailoring and concede
review, and the 2023 test above [1]. The expectation that tools
derive sections from requirements was not confirmed: sections come
from templates and prompts, and the requirements go in as the
buyer's typed or uploaded text (F1). The opposite - that the output
is boilerplate - is asserted by no source opened and measured by
none.

## Unexpected

The market's "AI RFP generation" has the shape of the forge's
render, not of a chain artefact: a template, a set of source
documents and an instruction produce the output, and the output is
reviewed and regenerated, never composed. The clearest instance is
the Copilot demo, whose RFP is literally "draft an RFP using the
following template" from a summarised requirements document [8];
DeepStream's "short prompt or supporting documents" [2] and SAP
Ariba's template plus library plus previous event [5] are the same
pattern in a platform. The card is answered as put; this is a lead
for the plan's hypothesis, offered as the agent's own reading.

A Coupa page titled "Standard Sourcing Event Creation Agent" is
described by the search engine as creating RFP events "from
contracts, requisitions, and requisition lines based on the most
relevant templates", with Navi then guiding the user through
"reviewing suppliers, adding questionnaires, and refining event
details". The page and Coupa's January 2026 release page both
returned 403 and were not read; this rests on a search engine's
summary alone and is a lead, not a finding. If it holds, it is the
closest thing found to derivation from existing structured records
- and the records are contracts and requisitions, not requirements.

Globality's output is a "brief" sent to suppliers, and its scoping
conversation - questions proposed, answers suggested, each accepted
or rejected with one click [9] - is an elicitation interview run by
the tool. The vendor merges what the forge keeps apart: the
elicitation of the intent and the document that goes out.

Where criteria appear, they are the buyer's input (F3). That the
market does not derive evaluation criteria from requirements is a
signal for the boundary card 5 draws, offered here only as an
observation from the pages opened.

## Not found

- An independent review, 2024 to 2026, of an RFP generated by a
  buyer-side platform's AI (searched: review of AI-generated RFP
  boilerplate; Spend Matters review of generative AI RFP creation;
  ChatGPT-written RFP generic test; buyer's complaint of a generic
  template). The only hands-on test found is 2023 and of general
  chatbots [1].
- Gartner's own text of the Market Guide for Sourcing Applications
  (2025 or 2026): only a vendor's excerpts were readable [3]; the
  second vendor's summary returned 404.
- Coupa's documentation of its sourcing event creation agent and of
  its January 2026 release: both pages returned 403.
- The WHO's internal "RFP generation agent" listing, which the
  search engine described as merging inputs from several
  stakeholders and flagging gaps in requirements: one URL returned
  404, the other an empty page with the title only.
- Globality's help-centre pages on project scoping and project
  brief modules (scope, line items, proposal requirements, pricing
  requirements): redirect then 404; only the 2023 blog could be
  read [9].
- Any measured figure for the accuracy of a tool's gap-flagging or
  of its generated questions; every time-saving figure found is a
  vendor's ("in under a minute" [2]; JAGGAER's "thousands of hours"
  without a stated basis [6]).
- User reviews on G2 or Capterra specific to the RFP-generation
  feature of a named tool: not searched for directly within the
  budget.
- Guidance from a procurement institute (NIGP, CIPS) on AI-drafted
  solicitations: one query returned government and vendor pages
  only, none opened.

## Options

The card asked for a fact; the options below are the agent's own
reading of how the project could use it and are offered only as
such.

1. Treat the RFP as a render: the chain's artefacts as inputs, an
   RFP template, instructions, and the human-supplied fields named
   as such. This matches every tool opened (Unexpected, first
   paragraph). Trade-off: the fields the market leaves to people -
   criteria and weights, commercial and legal gates, timeline - have
   no home in a render unless the recipe names them as inputs the
   principal supplies.
2. Treat the RFP as an artefact of the chain. The market offers no
   precedent for it: no tool opened composes an RFP with items of
   its own traced to requirement items. Trade-off: this is exactly
   the gap the market does not fill (F7), which can be read as the
   warning the card names or as the opening.

## Relevance to this project

Recommendation, as the agent's own: read the market as evidence for
the render reading of the hypothesis. Every buyer-side tool opened
produces an RFP the way the forge produces a render - template,
sources, instruction, regenerate - and every one hands the substance
back to the buyer; none composes RFP content from requirements with
traceability, and none derives evaluation criteria. This rests on
the vendors' own documentation (F1 to F4, F7), one dated independent
test (F5) and a copied analyst frame (F6); it is chosen against the
artefact reading because the market shows no precedent for an RFP
composed with items of its own, and against the conclusion that
derivation is impossible, because no source measures it either way.
The parts the market leaves to people - evaluation criteria and
weights, timeline, commercial and legal conditions - are what card 3
and card 5 should name as the person's supply. The Coupa agent is
the one lead that could change the picture and must be read before
the plan rests on this note.

Consult when: deciding whether the RFP is a render or an artefact;
listing what a person supplies to an RFP; weighing whether to look
at a buyer-side tool rather than build the derivation; and before
citing any claim that tools "derive" RFPs - the claim is the
vendors' and the independent evidence is one 2023 test.

## Sources

1. "Procurement Perspective: How Generative AI Performs In Building
   an RFP", Joanna Martinez, Cloud Wars (Acceleration Economy),
   2023-09-11 (byline),
   https://cloudwars.com/innovation-leadership/procurement-perspective-how-generative-ai-performs-in-building-an-rfp
   ; kind: secondary (practitioner's own test); read in full through
   a summarising fetch; original.
2. "AI RFP Generation for Procurement Teams", DeepStream
   Technologies Limited, undated (footer © 2025; badges name H2 2025
   and 2026),
   https://deep.stream/rfx-software-features/ai-rfp-generation ;
   kind: primary (vendor's own product page); read in full through a
   summarising fetch; original.
3. "Our Key Takeaways for Procurement Leaders from the 2025 Gartner
   Market Guide for Sourcing Applications", Market Dojo, no author
   named, 2025-02-27 (post date on page), citing the Gartner guide
   of 2025-01-30,
   https://marketdojo.com/resource/our-key-takeaways-for-procurement-leaders-from-the-2025-gartner-market-guide-for-sourcing-applications/
   ; kind: tertiary (a vendor's excerpts of an analyst report); read
   in full through a summarising fetch; copy, of the Gartner guide,
   which is paywalled and was not opened.
4. "Introducing Zip Sourcing: Use AI to source more to save more",
   Davide Russo, Zip, 2023-11-06 (byline),
   https://zip.com/blog/introducing-zip-sourcing-source-more-to-save-more-with-ai-powered-rfx
   ; kind: primary (vendor's own launch post); read in full through
   a summarising fetch; original.
5. "Beginning of RFP", lesson of the course SAP Ariba Overview for
   Indirect Spend, SAP Learning, undated (image paths carry
   "AR020_2502", not stated to be a date),
   https://learning.sap.com/courses/sap-ariba-overview-for-indirect-spend/beginning-of-rfp
   ; kind: primary (vendor's own training documentation); read in
   full through a summarising fetch; original.
6. "JAGGAER 25.3 Accelerates Sourcing Cycles, Strengthens Supplier
   Risk Controls, and Streamlines Intake", JAGGAER press release,
   dateline 2025-11-20, page header 2025-12-04 (both on page),
   https://www.jaggaer.com/press-release/jaggaer-25-3-release ;
   kind: primary (vendor's own release); read in full through a
   summarising fetch; original.
7. "RFP Software" (free RFP generator), Procol Tech Inc., undated
   (footer © 2026), https://www.procol.ai/tool/rfp-software/ ;
   kind: primary (vendor's own tool page); read in full through a
   summarising fetch; original.
8. "9 - Operations Demo", MS-4021 Copilot Immersion Experience,
   Microsoft Learning (GitHub Pages), undated ("Last updated" field
   blank),
   https://microsoftlearning.github.io/MS-4021-Copilot-Immersion-Experience/Instructions/Demos/9-Operations-Demo.html
   ; kind: primary (vendor's own training script); read partially
   through a summarising fetch, the RFP part (Copilot in Word steps
   2 to 8, Copilot Chat steps 3 to 7, the Outlook step); original.
9. "Autonomous Sourcing Meets Generative AI", Globality, no
   individual byline, 2023-02-18 (date on page; footer © 2015-2026,
   image path 2026/03, so possibly updated),
   http://www.globality.com/resources/innovation-blog/autonomous-sourcing-meets-generative-ai
   ; kind: primary (vendor's own blog on its own product); read in
   full through a summarising fetch; original.
10. "Zip Sourcing" (demo walkthrough page), Zip, undated (footer ©
    2026), https://zip.com/walkthroughs/zip-sourcing ; kind: primary
    (vendor's own product page); read in full through a summarising
    fetch; original; thin, one line used.

Not opened, never cited for content: the Coupa "Standard Sourcing
Event Creation Agent" use-case page (403) and Coupa's January 2026
release page (403); the WHO AI portal's RFP generation agent, two
URLs (404; empty page); Levelpath's summary of the 2026 Gartner guide
(404); Globality's help-centre scoping page, two URLs (redirect,
then 404).

## Opened and not used

- https://learning.globality.com/client-getting-started/1080020 -
  redirected to help.globality.com; no content.
- http://help.globality.com/client-getting-started/1080020 - 404.
- https://aiportal-admin.who.int/tool/rfp-generation-agent - 404.
- https://aiportal.who.int/tool/rfp-generation-agent - page returned
  its title only, no body.
- https://levelpath.com/research/2026-gartner-market-guide-for-sourcing-applications
  - 404; would have been a vendor's copy of the 2026 Gartner guide.
- https://ai.coupa.com/use-case/standard-sourcing-event-creation-agent/
  - 403.
- https://www.coupa.com/product-release/january-2026/ - 403.
- https://globality.com/innovation-blog/autonomous-sourcing-meets-generative-ai
  and
  http://globality.com/resources/innovation-blog/autonomous-sourcing-meets-generative-ai
  - redirects, superseded by [9].

## Search record

Queries, in order: AI RFP generator for buyers, create RFP from
requirements; SAP Ariba Sourcing create RFP event from template;
Coupa Sourcing AI generate RFP questionnaire; review of
AI-generated RFP boilerplate 2025 (disconfirming, first wording);
Gartner strategic sourcing suites RFx AI generation 2025; Globality
autonomous sourcing scoping questionnaire; Zip sourcing AI RFP from
intake; Spend Matters review of generative AI RFP creation; ChatGPT
writes RFP, generic boilerplate test (disconfirming, second
wording); SAP Ariba Joule generates sourcing event content; JAGGAER
JAI creates RFx from requirements; Coupa Navi agents sourcing event
creation and SOW to request; procurement association guidance on AI
drafting of solicitations; AI RFP builder disappointing, generic
template, requirements still written by hand (disconfirming, third
wording). Fourteen queries.

Openings: nineteen fetches, of which ten returned content and are
the sources [1] to [10]; nine returned a redirect, a 404, a 403 or
an empty page (Opened and not used). Every content-bearing read was
through the summarising fetch, so every source above is read through
a tertiary summary of the page and the note says so in Sources.

The run ended on the opening budget: at nineteen fetches it was
over the brief's "about ten to fifteen", with Coupa's primary and
the analyst's own text still unreachable. The second part of the
stop rule is met in part: the procurement officer's perspective has
primary sources ([2], [4], [5], [6], [7], [9]), the evaluator's only
what those same pages say of scoring ([4], [7], [8]) and the one
practitioner test [1]; the third disconfirming wording brought
nothing the first two had not.
