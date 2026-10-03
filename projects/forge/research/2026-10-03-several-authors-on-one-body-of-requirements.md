---
project: forge
type: research
topic: how several authors work on one body of requirements so that one coherent document comes out
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1 (section "Several people on one project")
status: immutable
---

# Several authors on one body of requirements

## Question

How do established tools and practices organise the work of several
authors on one body of requirements or specification documents, so
that one coherent document comes out: what is the unit of ownership
(document, section, item), how are concurrent edits prevented or
merged, how is the identity of items kept, who decides, and what is
known to work badly?

The facts behind the question. The draft brief `next-gen` says that
work of several people on one project is today very unpleasant: IDs
collide, and a change never touches one file, since it rewrites the
history, the ledger and more. Its estimate is that collisions will
be few, because analysts mostly work each on a topic of his own. It
leaves open the level at which the matter is solved: git and the
same files, or lower down, where the outputs of different people
meet.

Not answered here: the mismatch of engine versions between two
people on one project (the brief's "Upgrade and compatibility"), and
how the history of an item is recorded
(`2026-09-29-change-history-of-document-items.md`).

Surveyed on 2026-10-03: requirements kept as text (Doorstop,
StrictDoc, Sphinx-Needs, OpenFastTrace), commercial requirements
tools (Jama Connect, IBM DOORS Next, Polarion, Azure DevOps),
proposal processes (PEP, Kubernetes KEP, Rust RFC, IETF, decision
records, design documents at one large software company),
docs-as-code practice (code owners, changelog fragments, git merge
drivers), real-time co-editing (Confluence, Google Docs) and the AI
spec-driven frameworks (GitHub Spec Kit, BMAD Method, OpenSpec,
Kiro).

Epistemic tags: [V] wording returned as a quotation from the page
itself, fetched 2026-10-03; [S] taken from a search summary or a
secondary page; [Y] this note's own synthesis or recall, not checked
at a source. Pages were read through a fetch tool that condenses
them, so a [V] quotation is as that tool returned it. Status per
finding: consensus / emerging / contested.

## Answer in one paragraph

Nowhere in the survey do several people own one document together.
Every practice that produces one coherent text names one owner or
editor per unit and routes everyone else through review; what
differs is the size of the unit. The proposal processes and the AI
frameworks own by document; the commercial tools own and lock by
item, which needs a server; git-based practice owns by file, never
below it, so "ownership of a group of items" in git means a file
per group. Concurrent work is kept apart rather than merged: a
branch, a change set, a change folder, a lock; and merging is
described as a cost to minimise, not a feature to lean on. Item
identity survives several authors only where the number comes from
one counter outside any working copy (a server, an editor, a pull
request number) or is a name; "next free number in my copy" is
reported as a defect in three unrelated tools. A shared append-only
file is a known source of conflicts with a known cure, one file per
entry. Real-time co-editing gives up exactly what a chain of
versioned documents rests on: versions, attribution and review. For
the forge: one owner per document with contributions by review as
the stated rule, separate projects joined lower down as the normal
way for analysts on separate topics, and two mechanical matters
(where an ID comes from, and the shape of the shared files) settled
whichever is chosen.

## Findings

### A. Requirements kept as text in git

1. **Doorstop: one file per item, and the next number collides.**
   [V, Doorstop item reference] "The UID of an item is defined by
   its file name without the extension"; "By default, the number is
   automatically assigned by Doorstop. Optionally, a user can
   specify a name for the UID during item creation." [V, Doorstop
   issue 84, opened 2014-06-06, closed, label "research"] The issue
   "Determine the best way to prevent duplicate IDs" describes two
   branches each assigning the same next ID because each working
   copy knows a different last item. The discussion and the outcome
   were not visible to the fetch. One file per item means two people
   editing different items never touch the same file. Status:
   consensus that the file per item removes text conflicts; the
   numbering defect is known and, as far as seen, answered only by
   names.
2. **StrictDoc: one document file, composed from smaller ones.**
   [V, StrictDoc feature map] "The 'Composable Documents' feature
   in StrictDoc enables users to create composite documents made up
   of smaller, independent SDoc documents." [V, user guide]
   "StrictDoc does not impose any limitations on the format of a
   UID"; an optional machine identifier (MID) can be generated per
   node beside the readable UID. The guide gives no advice on
   several authors or on merge conflicts; the web editor writes
   back to the text files and committing is left to git. A command
   for assigning UIDs automatically exists [S]; how it behaves
   across branches was not read. Status: emerging.
3. **Sphinx-Needs: the ID is written by hand, and separate
   projects are joined by reference.** [V, configuration]
   `needs_id_required` "Forces the user to set an ID for each need
   ... So no ID is autogenerated any more"; an automatic ID is a
   hash of the title, stable only while the title is. Needs of
   another project are referenced through `needs_external_needs`,
   with an optional ID prefix per source to keep identifiers
   apart, or imported from its `needs.json`. Status: consensus
   within the tool.
4. **OpenFastTrace: not reached.** The user guide returned 404 at
   every address tried. [Y, recall, unverified] Its item IDs are
   built from an artefact type, a name and a revision rather than
   from a counter. Nothing is rested on this.

### B. Commercial requirements tools

5. **Jama Connect: the item is the unit, locked while edited.**
   [V, help, "Using and managing locked items"] "A system lock is
   applied to items that use workflows. A user lock is applied
   manually when you lock an item or automatically whenever an item
   is being edited"; "Organization admins and project admins can
   unlock items that were locked by any user." Concurrent edits of
   one item are prevented, not merged. Status: consensus among the
   server tools.
6. **Jama Connect: agreement is reached in a review with named
   roles.** [V, help, "How reviews work"] A moderator "Starts the
   review and facilitates the discussion", an approver "Signs off
   and approves items in review", "All feedback is associated with
   a specific revision of the document." [S] A review can be
   started from a baseline; the vendor recommends about 250 items
   and 25 participants for a review. Status: consensus.
7. **Jama Connect: a branch is a duplicated project.** [V, help,
   "Reuse and synchronization"] "Projects are branched by project
   duplication. Synchronization is enabled during project
   duplication and differences are monitored between containers
   and items"; "Create a project baseline just after duplication."
   Whether the differences are applied per item by hand or
   automatically the page did not say. Status: consensus as the
   vendor's practice.
8. **DOORS Next: a change set per person, delivered to a stream,
   and a warning against many streams.** [V, IBM documentation
   7.1] "Your personal stream can contain multiple change sets but
   only one change set from any specific component"; the change
   set is delivered from the banner of the application. [V,
   jazz.net configuration management FAQ] "create a new stream
   only when necessary and when you are ready to start working in
   it; minimizing the number of concurrent work streams reduces
   the complexity of delivering across multiple streams." [S, IBM
   ideas portal through a search summary] Merge at delivery works
   at the level of the whole artefact, and users have asked for it
   at the level of the attribute; if one artefact of a change set
   collides, the whole set goes to the resolution screen. Status:
   consensus that branching of requirements exists; contested how
   well merging works.
9. **Polarion: concurrent editing of one document, with conflicts
   classed safe or hard.** [V, vendor blog, 2021-04-20] "A new
   icon in the Document Editor toolbar shows the number of people
   working with the Document"; the release "improved the way
   Polarion automatically merges concurrent structural changes:
   moving, indenting, adding, or removing items, headings, and
   paragraphs within a Document"; the dialog uses "distinct red
   and yellow coloring to indicate whether Polarion can safely
   merge changes or not." [S] A hard conflict overwrites an
   earlier edit and the user merges back by hand; branched
   documents are merged by a three-way merge per work item.
   Status: consensus as a description of the product.
10. **Azure DevOps: one assignee per item, one counter for all.**
    [V, Microsoft Learn, 2026-06-16] "Each work item receives a
    unique identifier within an organization or project
    collection"; "A work item can have only one assignee at a time.
    If multiple people share work, create separate work items for
    each responsible person." What happens when two people save the
    same item was searched for and not found. Status: consensus.

### C. Proposal processes with many authors

11. **PEP: authors own the text, editors own the number, a council
    decides.** [V, PEP 1, last modified 2026-09-27] Authors pick
    "the next available PEP number not used by a published or
    in-PR PEP", and the editors confirm it: "Once approved, they
    will assign your PEP a number." "The final authority for PEP
    approval is the Steering Council." Others change a PEP by pull
    request, and substantive changes are "first proposed on the
    PEP's discussion thread." Ownership is transferred explicitly.
    Status: consensus.
12. **Rust RFC: the number is the pull request's.** [V, RFC
    repository README] The file starts as `0000-my-feature.md`:
    "This is going to be the PR number and we'll rename the file
    accordingly if the RFC is accepted." A sub-team decides after a
    final comment period. "Only very minor changes should be
    submitted as amendments. More substantial changes should be
    new RFCs, with a note added to the original RFC." Status:
    consensus.
13. **Kubernetes KEP: authors, reviewers and approvers are named
    in the document, the number comes from a tracking issue.** [V,
    KEP template] The steps: file an enhancement issue, copy the
    template directory under the issue number, fill `kep.yaml`
    with authors, owning group and status; "Merge early and
    iterate. Avoid getting hung up on specific details and instead
    aim to get the goals of the KEP clarified and merged quickly";
    "One KEP corresponds to one feature for its whole lifecycle."
    [V, KEP process] "The approvers are the individuals who decide
    when to move this KEP to the `implementable` state." Status:
    consensus.
14. **IETF: an editor writes down what the group decided, and is
    not the one who judges agreement.** [V, RFC 2418] "A working
    group generally designates a person or persons to serve as the
    Editor for a particular document", responsible that "the
    contents of the document accurately reflect the decisions that
    have been made by the working group"; the chair and the editor
    are recommended to be different people. [V, RFC 7322] "The
    total number of authors or editors on the first page is
    generally limited to five individuals"; contributors are
    listed apart and do not sign off. Status: consensus.
15. **Decision records: one owner per record, others contribute
    through him.** [V, AWS Prescriptive Guidance] "Every team
    member can create an ADR, but the team should establish a
    definition of ownership for an ADR"; "Other team members can
    always contribute to an ADR. If the content of an ADR changes
    before the team accepts the ADR, the owner should approve
    these changes." [S, several project pages through a search
    summary] Sequential ADR numbers collide when two records are
    written at once; the remedies seen are a provisional number
    until merge, renumbering of the later one, or the pull request
    number. Status: consensus on ownership; the numbering is a
    known nuisance with no single answer.
16. **Design documents: an author, co-editing while drafting,
    review after.** [V, Malte Ubl, 2020-07-06] "You write the doc.
    Sometimes together with a set of co-authors"; "the vast
    majority of design docs at Google are created in Google Docs
    and make heavy use of its collaboration features." The cycle
    is creation and rapid iteration, review, implementation,
    maintenance. The co-editing serves an unversioned narrative
    document, not a set of identified items. Status: consensus in
    that setting.

### D. Docs-as-code practice

17. **Review by merge request is the collaboration mechanism.**
    [V, Write the Docs] The practices named are issue trackers,
    version control, plain text markup, code reviews and automated
    tests. No drawbacks are listed by that source. Status:
    consensus.
18. **Ownership in git stops at the file.** [V, GitHub Docs] "Code
    owners are automatically requested for review when someone
    opens a pull request that modifies code that they own";
    patterns name files and directories; "the last matching
    pattern takes the most precedence"; with branch protection the
    approval of an owner is required. Neither GitHub nor GitLab
    [V, GitLab Docs] offers ownership of a section inside a file.
    Status: consensus.
19. **A file every change appends to is a conflict machine; the
    cure is one file per entry.** [V, GitLab blog, 2018-07-03]
    With one changelog file, "Whenever one branch was merged, it'd
    create a conflict in the other", "a major source of delays in
    development, as contributors would have to rebase their branch
    in order to resolve the conflicts." Placeholder lines did not
    help. The solution kept: "each changelog entry would be its own
    YAML file in a `CHANGELOG/unreleased` folder", compiled at the
    release. The towncrier, reno and Changesets tools of the
    earlier note work the same way. Status: consensus.
20. **Git can merge appended lines by itself, with a warning.** [V,
    gitattributes] The `union` driver takes "lines from both
    versions, instead of leaving conflict markers. This tends to
    leave the added lines in the resulting file in random order
    and the user should verify the result. Do not use this if you
    do not understand the implications." Status: consensus as a
    description; its use for structured records is contested [Y].

### E. Real-time co-editing

21. **Confluence: everyone edits one shared draft, and the version
    belongs to whoever publishes.** [V, Atlassian, "Collaborative
    editing"] "Up to 12 people can edit the same page at the same
    time"; "We're saving all the time in collaborative editing,
    but we don't save versions in a draft"; "All page changes are
    currently attributed to the person that publishes the page,
    rather than the person who made each specific change";
    discarding a shared draft discards everyone's changes, and
    "there's no way to get a discarded draft back." Status:
    consensus as a description.
22. **Google Docs: versions are grouped and may be merged.** [V,
    Google Docs Editors Help] Named versions exist so that
    "versions aren't merged", up to 40 per document; "revisions
    for your file may occasionally be merged." Who edited a
    passage can be shown on request. Status: consensus.
23. **What co-editing gives up.** [Y] No stable version between
    publications, attribution by publisher or by passage rather
    than by decision, no review gate before a change is in the
    text, and no record of the reason. Notion was not surveyed.

### F. AI spec-driven frameworks

24. **Spec Kit: the same numbering defect, reported by a team.**
    [V, Spec Kit discussion 497, opened 2025-09-23] "When you are
    working in a team and everyone branches off a common branch to
    develop different features, their number will naturally
    conflict." The replies propose finishing the specification
    before the team branches, or treating the tool as one among
    several; one holds that it struggles with team workflows as
    such. [S] A later fix addressed duplicate feature numbers
    across branches and worktrees. The framework's README says
    nothing on several people on one spec. Status: emerging; the
    defect is acknowledged, the answer unsettled.
25. **BMAD Method: one owner per document, parallel work below a
    shared spine.** [V, "Plan Inside an Organization", undated]
    "The PRD is the document the organization owns"; "each
    document has exactly one owner, because each has exactly one
    skill that writes it"; several people work on separate epics,
    and "the spine is what makes that safe, because it records the
    calls two people would otherwise make differently"; a change
    goes to the PRD first, in an update mode that "surfaces
    conflicts with earlier decisions before applying anything."
    [V, "Adopt BMad Across a Team"] Team settings are committed,
    personal ones are gitignored. Status: emerging.
26. **OpenSpec: a change is a folder of its own, and sharing is
    git.** [V, concepts] "Multiple changes can exist simultaneously
    without conflicting"; "Two changes can touch the same spec file
    without conflicting, as long as they modify different
    requirements." [V, stores guide, beta] "Sharing work is git,
    on purpose ... Plans get branches, pull requests, and review
    for free"; "References are read-only context"; [V, README] "a
    platform team owns the specs; product teams reference them
    read-only." What happens when two changes modify the same
    requirement was not found. Status: emerging.
27. **Kiro: a spec per feature, shared through the repository.**
    [V, Kiro documentation, specs best practices] "Specs are
    designed to be version-controlled, making them easily shareable
    across your team"; separate specs per feature let team members
    work on different features at once; for several teams a
    central specifications repository referenced by submodule or
    package. Nothing on two people in one spec. Status: emerging.

## What the findings say to the five sub-questions

**Unit of ownership.** The document in every process that has no
server (findings 11 to 15, 25, 27); the item where a server holds
the items (5, 9, 10); the file in git, never less (18). Ownership
of a group of items inside one file exists nowhere in the survey.
Status: consensus.

**Concurrent edits.** Prevented or kept apart far more often than
merged: a lock (5), a personal change set (8), a branch with a pull
request (11 to 13, 26), a change folder (26), a file per item (1).
Where merging exists it is by item and the vendor warns to keep it
rare (8), or it distinguishes safe from hard conflicts and leaves
the hard ones to a person (9). Status: consensus.

**Identity of items.** Safe sources of a number: one server counter
(10), an editor who assigns (11), the number of the pull request or
the issue (12, 13), a name or a hand-written ID (1, 3). Unsafe: the
next free number as seen from one working copy (1, 15, 24). A
prefix per source keeps joined projects apart (3). Status:
consensus on the defect; no single remedy.

**Who decides.** One named owner, editor or approver in every case;
the one who writes down is in two cases deliberately not the one
who judges agreement (6, 14). Status: consensus.

**What works badly.** Sequential numbering from a working copy (1,
15, 24); one shared file that every change appends to (19); many
parallel streams of one requirement set (8); merge at a grain
coarser than the edit (8); a co-edited draft as a record (21, 22).
Status: consensus, each on its own evidence.

## Options with trade-offs

All four are [Y], measured against the findings.

**(a) One owner per document, contributions by review.** The shape
of findings 11 to 15 and 25. One person composes each artefact;
another contributes by a proposal the owner takes in: a merge
request, or a whole of his own that the owner mines. Coherence and
authority stay with one head, and the forge's rule that the
principal alone decides is untouched. The cost: the second person
is a contributor, not an author; the owner is a bottleneck; and a
contribution made on a branch still rewrites the shared files
(history, ledger), so the mechanical collisions remain unless they
are treated on their own.

**(b) Ownership per group of items in one document.** Each group of
an artefact has its owner, the document is one. Closest to "analysts
each on a topic of his own" inside one project. Git cannot enforce
it below the file (finding 18), so it is either a convention with a
check, or the document is split into a file per group and composed
(findings 1, 2). The decision across groups, and the items that
belong to none (purpose, context), still need one owner. The
document stops being one file a reader opens.

**(c) Separate documents or projects per author, joined lower
down.** Each person runs his own chain; the outputs meet in a
later layer or outside the forge (findings 3, 25, 26, 27). No
collision at all inside a project, no change to the single
principal. The join is where the cost moves: someone must own the
joined layer, overlaps and contradictions between the parts are
found late, and item IDs of the parts need to stay distinguishable
(a prefix per source, finding 3). A genuinely shared topic is not
served.

**(d) Co-editing.** Several people in one text at once. Fast for
an early draft of narrative (finding 16). It gives up versions,
attribution and review (findings 21 to 23), has no carrier in
Markdown files under git, and with an AI in each seat it would mean
two conversations writing the same items at once. The server tools
that come nearest (finding 9) do it with item-level conflict
handling the forge does not have.

Independent of the choice, two mechanical matters decide how
unpleasant the work is:

- **Where a new ID comes from.** Remedies in the field: a single
  allocator, a number taken from outside the working copy, a name,
  a reserved range per author, a provisional ID settled at the
  merge (findings 1, 11, 12, 13, 15).
- **The shape of files every change touches.** One file per
  record, compiled or read together (finding 19), against one
  appended file with conflicts resolved by hand or by a union merge
  that needs verifying (finding 20).

## Relevance to this project

Recommendation: **(a) as the stated rule, (c) as the normal way for
separate topics, (b) and (d) not pursued**; and the two mechanical
matters taken up as questions of their own. All of it [Y].

- **(a) fits what the forge already is.** One principal per
  artefact is the forge's own premise, and every process surveyed
  that yields one coherent text has it. The forge already has a
  vessel for a second person's whole of thinking: a later brief
  (`00-brief-<name>.md`), mined into the single intent by its
  owner. Whether a second person's contribution arrives as such a
  brief, as a merge request, or both, is the open point.
- **(c) matches the brief's own estimate** that analysts mostly
  work each on a topic of his own, and its second level ("lower
  down, where the outputs of different people meet"). The forge has
  the pieces: a project per topic, libraries, the spin-off. What
  the field adds is that the joined layer needs one owner and a
  shared record of the calls the parts must make alike (finding
  25), and that IDs need telling apart across the parts (finding
  3).
- **(b) is not supported by any practice found** without either a
  server or a file per group, and both change what a forge
  document is.
- **(d) contradicts the chain**: versions, history and decisions
  by one principal are what it would give up.
- **IDs.** The forge allocates "the next ten" from the working
  copy, the pattern reported as a defect in findings 1, 15 and 24.
  The remedies that need no server are a reserved range per author
  (the existing rule that a new group starts at the next hundred
  is close to it), a provisional ID settled at the merge, or a
  check at the merge that fails on a duplicate. Which one is the
  principal's to choose; none is proposed here.
- **Shared files.** The history companion and the ledger are
  touched by every change, the case of finding 19. The ledger is
  freely rewritten state and could be merged by regenerating or
  re-checking; the history is append-only and is the nearer
  relative of the changelog. One record per file is the field's
  cure; whether its cost is worth it at the forge's expected rate
  of collisions is a judgement, and the brief expects few.
- **Who writes down and who decides.** Two processes separate the
  editor from the judge of agreement (findings 6, 14). Where two
  people share a topic, naming which of them is the principal of
  the artefact is the least that the field does everywhere.

Nothing here is done by this note. It serves the section "Several
people on one project" of the brief `next-gen`; whatever is taken
from it enters by the principal's word, through `/forge brief
next-gen` or `/forge intent`.

Left uncertain: how the server tools behave when two people save
the same item (not found for Azure DevOps; Jama prevents it by a
lock); the real quality of merging in DOORS Next (one ideas-portal
entry through a search summary); OpenFastTrace and Notion (not
reached); the outcome of the Doorstop numbering issue; and whether
any team has reported experience with two people, each with an AI
assistant, composing one specification. For the last, nothing was
found, and the frameworks' own guidance is recent and thin.

## Sources

All fetched 2026-10-03 unless marked as a search summary.

- Doorstop, *Item reference*,
  https://doorstop.readthedocs.io/en/latest/reference/item.html
- Doorstop, issue 84, *Determine the best way to prevent duplicate
  IDs* (2014-06-06),
  https://github.com/doorstop-dev/doorstop/issues/84
- StrictDoc, *User guide* and *Feature map*,
  https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide.html,
  https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_02_feature_map.html
- Sphinx-Needs, *need* directive and *Configuration*,
  https://sphinx-needs.readthedocs.io/en/latest/directives/need.html,
  https://sphinx-needs.readthedocs.io/en/latest/configuration.html
- OpenFastTrace, user guide,
  https://github.com/itsallcode/openfasttrace (the guide returned
  404; not read)
- Jama Connect Help, *Using and managing locked items*,
  https://help.jamasoftware.com/ah/en/create-content/items/using-and-managing-locked-items.html
- Jama Connect Help, *How reviews work*,
  https://help.jamasoftware.com/ah/en/getting-to-know-jama-connect-features/how-reviews-work.html
- Jama Connect Help, *Reuse and synchronization*,
  https://help.jamasoftware.com/ah/en/getting-to-know-jama-connect-features/reuse-and-synchronization.html
- Jama Connect Help, *Roles for review workflow*,
  https://help.jamasoftware.com/ah/en/reviews-in-jama-connect/roles-for-review-workflow.html
  (through a search summary)
- IBM Documentation 7.1, *Working with DOORS Next change sets in
  personal streams*,
  https://www.ibm.com/docs/SSYMRC_7.1/com.ibm.rational.gcapp.doc/topics/working_with_rm_change_set.html
- jazz.net, *Frequently-asked questions about CLM configuration
  management*,
  https://jazz.net/wiki/bin/view/Deployment/ConfigurationManagementFAQ?rev=16
- IBM ideas portal, entries on merge at delivery in DOORS Next,
  https://ibm-ai-apps.ideas.ibm.com/ideas/ENGRMDN-I-1018 (through a
  search summary)
- Siemens, *Polarion ALM 21 R1: what's new and noteworthy*
  (2021-04-20),
  https://blogs.sw.siemens.com/polarion/polarion-alm-21-r1-whats-new-and-noteworthy/
- Microsoft Learn, *About work items and work item types*
  (2026-06-16),
  https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items
- PEP 1, *PEP Purpose and Guidelines* (last modified 2026-09-27),
  https://peps.python.org/pep-0001/
- Rust RFCs, README,
  https://github.com/rust-lang/rfcs/blob/master/README.md
- Kubernetes, KEP template and *KEP process*,
  https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md,
  https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md
- RFC 2418, *IETF Working Group Guidelines and Procedures* (1998),
  https://www.rfc-editor.org/rfc/rfc2418.html
- RFC 7322, *RFC Style Guide* (2014),
  https://www.rfc-editor.org/rfc/rfc7322.html
- AWS Prescriptive Guidance, *Architectural decision record
  process*,
  https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- ADR numbering, several project pages, among them
  https://docs.clan.lol/decisions/03-adr-numbering-process (through
  a search summary; the page redirected and was not read)
- Malte Ubl, *Design Docs at Google* (2020-07-06),
  https://www.industrialempathy.com/posts/design-docs-at-google/
- Write the Docs, *Docs as Code*,
  https://www.writethedocs.org/guide/docs-as-code/
- GitHub Docs, *About code owners*,
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitLab Docs, *Code Owners*,
  https://docs.gitlab.com/user/project/codeowners/
- GitLab, *How we solved GitLab's CHANGELOG conflict crisis*
  (2018-07-03),
  https://about.gitlab.com/blog/solving-gitlabs-changelog-conflict-crisis/
- Git, *gitattributes*, https://git-scm.com/docs/gitattributes
- Atlassian, *Collaborative editing*,
  https://confluence.atlassian.com/display/DOC/Collaborative+editing
- Google Docs Editors Help, *Find what's changed in a file*,
  https://support.google.com/docs/answer/190843
- GitHub Spec Kit, discussion 497 (2025-09-23),
  https://github.com/github/spec-kit/discussions/497
- BMAD Method, *Plan Inside an Organization* and *Adopt BMad
  Across a Team*,
  https://docs.bmad-method.org/plan/plan-inside-an-organization/,
  https://docs.bmad-method.org/customize/adopt-bmad-across-a-team/
- OpenSpec, *Concepts*, README and *Stores user guide* (beta),
  https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md,
  https://github.com/Fission-AI/OpenSpec/blob/main/README.md,
  https://github.com/Fission-AI/OpenSpec/blob/main/docs/stores-beta/user-guide.md
- Kiro, *Specs: best practices*,
  https://kiro.dev/docs/specs/best-practices/
