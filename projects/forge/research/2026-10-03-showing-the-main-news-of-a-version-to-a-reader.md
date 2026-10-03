---
project: forge
type: research
topic: showing the main news of a version to a reader - the "what's new" piece beside the changelog
date: 2026-10-03
derived_from: 00-brief-next-gen.md (draft), section "Documentation and news"; RELEASE-NOTES.md as rendered 2026-10-02 (sections 4.49, 4.48); research/2026-09-05-good-release-notes.md
status: immutable
---

# Showing the main news of a version to a reader

## Question

How do well-regarded projects show a reader, as opposed to an
upgrader, the main news of a version: what the piece is, where it
lives, how it is written, and how it relates to the technical
changelog?

The question starts where `research/2026-09-05-good-release-notes.md`
stops. That note surveyed the changelog standards and nine projects'
release notes and found, as its finding 4, that "highlights are a
layer on top of the list, never instead of it"; it then recommended
the shape the forge's `RELEASE-NOTES.md` has today (one section per
release, Action required first, typed groups, one sentence per entry).
Nothing of that is repeated here. What is asked now is the other
piece: the forge's release notes serve the user who pulls an upgrade,
and its owner finds that neither they nor the README tell a reader
what the biggest news is (draft brief `00-brief-next-gen.md`,
"Documentation and news": "something like the biggest news, which
strikes the reader"). The structure of the documentation as a whole is
a sibling research and is left out.

**How this was read, and what the tags mean.** All pages were fetched
on 2026-10-03. The fetch tool does not return a page as it stands: a
small model reads the page and answers a question about it, so what is
given below in quotation marks is the wording as that model relayed
it, and long pages were truncated (the Kubernetes release post lost
its "Spotlight" section this way). Two pages came back as raw source
and are quoted with more confidence: the Claude Code "What's new"
index and its Week 37 digest. Each claim carries one tag:

- **[V]** verified at a source fetched for this note (through the
  summarising tool, with the caveat above);
- **[S]** taken from a secondary source (a search-result snippet, a
  forum thread, a vendor or blog article);
- **[O]** this note's own synthesis.

Epistemic status of a practice is given in words at the head of each
finding: consensus, emerging or contested.

## Key findings

### 1. "What's new" is a genre of its own, a second document beside the changelog (consensus among the large projects)

Every large project read keeps two pieces with two readers, and the
news piece always ends by pointing to the complete one. **[V]** for
each row, **[O]** for the pattern.

- **Python.** "What's New in Python 3.14" opens: "This article
  explains the new features in Python 3.14, compared to 3.13 ... For
  full details, see the changelog." It has named editors, a "Summary
  - Release highlights" head whose items are links to the feature's
  own section, then "New features" where one feature gets a headline,
  some 250 to 350 words, a runnable example, and a "See also". The
  changelog is a separate document built from per-change NEWS
  entries. The developer guide says when a change earns the second
  piece: "If the change is particularly interesting for end users
  (for example, new features, significant improvements, or
  backwards-incompatible changes), then an entry in the What's New in
  Python document ... should be added as well."
  (https://docs.python.org/3/whatsnew/3.14.html;
  https://devguide.python.org/core-team/committing/)
- **Rust.** `RELEASES.md` is the complete list; the release blog post
  "Announcing Rust 1.99.0" (2026-10-01) tells three features under
  "What's in 1.99.0 stable", each a headline with 75 to 150 words and
  a code example where one helps, then the list of stabilised APIs,
  then "Check out everything that changed in Rust, Cargo, and Clippy"
  with links. About 1,100 words in all.
  (https://blog.rust-lang.org/2026/10/01/Rust-1.99.0/)
- **Django.** Two layers of news over the notes: the release notes
  themselves open with "What's new in Django 6.0", four major
  features as short subsections (150 to 200 words, a code example,
  links into the documentation), then "Minor features" by area and
  the compatibility sections; and the weblog announcement names the
  same four in one line each, feature name then benefit ("Background
  Tasks: run code outside the HTTP request-response cycle with a
  built-in, flexible task framework."), about 280 words, linking to
  the release notes.
  (https://docs.djangoproject.com/en/6.0/releases/6.0/;
  https://www.djangoproject.com/weblog/2025/dec/03/django-60-released/)
- **Kubernetes.** The release blog post ("Kubernetes v1.37", 2026-08-26)
  has a release theme and logo, a "Spotlight on key updates" section,
  then features by maturity stage, and points to the full release
  notes; single features get their own blog posts over the following
  weeks (ten and more for v1.37). The Spotlight section itself was
  truncated by the fetch tool and was not read.
  (https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/;
  https://kubernetes.io/blog/)
- **VS Code.** The monthly release notes are news and list in one
  page: one welcome sentence naming the release's direction, a
  highlights list of six items, each "Name: what you can now do"
  ("Shared worktree folders (Experimental): Avoid repeated dependency
  installs and duplicated artifacts by reusing ignored folders across
  worktrees."), then the areas, each feature with its setting, a
  screenshot or clip and a link to the documentation.
  (https://code.visualstudio.com/updates, release 1.140, 2026-09-30)
- **TypeScript.** The announcement post is the news piece and is
  long (about 5,800 words for 7.0): each feature a headline, two to
  four paragraphs, code, the reasoning; breaking changes in their own
  part; written by the product manager.
  (https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
- **Astro.** Three layers: a release post per minor ("Astro 7.3 is
  here!", a bulleted list of the three or four highlights, then one
  section per feature with background, code and use, and a pointer to
  "the full changelog"), the changelog on GitHub, and a monthly
  "What's new in Astro" that is a community round-up, not a feature
  piece. (https://astro.build/blog/astro-730/;
  https://astro.build/blog/whats-new-september-2026/)
- **Node.js.** The exception that shows the rule: the release blog
  post is generated from the changelog ("Notable Changes" over
  "Commits"); news in the reader's sense appears only in a separate
  Announcements category.
  (https://nodejs.org/en/blog/release/;
  https://github.com/nodejs/node/blob/main/doc/contributing/releases.md)
- **Stripe.** No highlights at all at the level of a release: tables
  by product with a Breaking column, each row linking to a page of
  its own with "What's new", "Impact", "Changes". It is a changelog
  for integrators, not a news piece.
  (https://docs.stripe.com/changelog)

### 2. The closest model for the forge: Claude Code's weekly digest beside its changelog (emerging; one strong example)

The tool the forge runs inside has exactly the owner's problem and
answers it with a second page. **[V]**, read as raw source.

- The **changelog** is a per-version list of one-line bullets
  ("Added recovery for a prompt cleared with Ctrl+C: ..."), several
  versions a week, no highlights. In the tool, `/release-notes` shows
  it in a version picker.
  (https://code.claude.com/docs/en/changelog;
  https://code.claude.com/docs/en/commands)
- The **"What's new"** page is described as "A weekly digest of
  notable Claude Code features, with code snippets, demos, and context
  on why they matter", and introduces itself: "The weekly dev digest
  highlights the features most likely to change how you work. Each
  entry includes runnable code, a short demo, and a link to the full
  docs. For every bug fix and minor improvement, see the changelog."
  (https://code.claude.com/docs/en/whats-new)
- The index holds one card per week, newest first, tagged with the
  span of versions it covers (for example "v2.1.263-v2.1.269"): one
  headline feature in bold with a sentence, then "Also this week:"
  three more in one sentence, then a link to the week's page. The
  archive is the same page, scrolled.
- A week's page (Week 37) carries a meta line ("2 features"), then
  per feature: a title, the version it arrived in, a lede of two or
  three sentences that says what it does and what it costs, a picture
  or clip, a "try it" command, and one link to the documentation
  page; then "Other wins", ten one-liners each linking into the
  documentation; then "Full changelog for v2.1.263-v2.1.269".
  (https://code.claude.com/docs/en/whats-new/2026-w37)

What this shows for the forge's case **[O]**: when releases are many
and small, the unit of the news is not the release but a period (here
a week), the piece names the span of versions it digests, and it
features very few items (two in Week 37, one headline on every index
card).

### 3. The comparable AI frameworks: news in the GitHub Release, almost never in the README (emerging)

**[V]** for each, read on 2026-10-03.

- **GitHub Spec Kit.** README has no news block. Releases are the
  generated "What's Changed" list of pull-request titles ("chore: bump
  version to 1.1.0"). A reader learns nothing of what is new without
  reading titles. (https://github.com/github/spec-kit;
  https://github.com/github/spec-kit/releases)
- **BMAD Method.** README has no news block. Releases are
  hand-written: a headline paragraph of two or three sentences that
  says what changed for the user ("Build decides how much ceremony a
  change needs after investigating it, not before. Simple changes now
  get a two-section spec and finish in one session."), then Breaking,
  features, fixes.
  (https://github.com/bmad-code-org/BMAD-METHOD;
  https://github.com/bmad-code-org/BMAD-METHOD/releases)
- **OpenSpec.** The one README with a news block: a single line near
  the top, "New workflow now available! We've rebuilt OpenSpec with a
  new artifact-guided workflow. Run `/opsx:propose "your idea"` to get
  started." with a link to the documentation page of the feature.
  Releases are hand-written and titled by their theme ("v1.14.0 - Ten
  new tools, archived changes"), with one summary sentence over New,
  Improved, Fixed. (https://github.com/Fission-AI/OpenSpec;
  https://github.com/Fission-AI/OpenSpec/releases)
- **Superpowers.** README has no news block; it offers a sign-up for
  release announcements. `RELEASE-NOTES.md` in the repository root
  opens a version with an optional summary paragraph ("`writing-plans`
  produces leaner plans, faster. ...") over typed groups, each item a
  bold headline with an explanation.
  (https://github.com/obra/superpowers;
  https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md)

Pattern **[O]**: three of four put a short hand-written head over the
list of each release, which is finding 4 of the earlier note again;
only one carries news in the README, and there it is one line about
one feature with one link, not a section. None has a "what's new"
page of its own.

### 4. Placement: five places, each with a different reader

- **A block in the README (contested, rare).** The two README guides
  read name no news section: Make a README lists name, description,
  visuals, installation, usage, support, roadmap, contributing,
  authors, licence, project status, and sends changes to "a separate
  changelog file"; Standard Readme defines no news, changelog or
  status section and leaves only "Extra Sections". **[V]**
  (https://www.makeareadme.com/;
  https://github.com/RichardLitt/standard-readme/blob/main/spec.md)
  In practice a few projects put one announcement line near the top
  (OpenSpec above). The argument against is staleness: a README is
  read as the timeless description of the project, and a dated block
  that nobody takes down misleads; the argument for is that the
  README is the one page every newcomer and every returning user
  opens. **[O]**; no source read states either argument as a rule.
- **A "what's new" page in the documentation (consensus among
  projects with documentation).** Python, Django, Matplotlib, Claude
  Code: the page lives beside the documentation it links into, and
  its past editions stay as an archive. **[V]**
- **The GitHub Release body (emerging among small frameworks).** A
  hand-written title and summary over the list (BMAD, OpenSpec).
  **[V]** It reaches watchers of the repository by notification;
  it is not read by someone who lands on the README. **[O]**
- **A blog or announcement post (consensus among large projects).**
  Rust, Django, Kubernetes, TypeScript, Astro. It needs a blog and an
  audience that follows it. **[V]**
- **A notice in the tool after an upgrade (established in desktop
  products, thin evidence here).** Obsidian shows the release notes in
  a pop-up after an automatic update and offers a "Show release notes"
  command to see them again **[S]** (a forum thread,
  https://forum.obsidian.md/t/how-to-show-current-release-notes/83633);
  VS Code opens its release notes after an update, with a setting
  `update.showReleaseNotes` to turn it off **[S]** (search-result
  snippet only; the documentation page fetched did not state it);
  Claude Code offers the changelog on demand through `/release-notes`
  **[V]**. For command-line tools the known convention is restraint:
  `update-notifier` describes itself as informing "in a non-intrusive
  way", waits a check interval before notifying, and has three ways to
  opt out **[V]** (https://github.com/yeoman/update-notifier). No
  source read describes an agent framework that tells its user what
  is new after a pull; that would be new ground. **[O]**

### 5. Writing: few items, the unit is a capability with its benefit, plain voice

Consensus among the projects read; the pattern is **[O]**, each
instance **[V]**.

- **How many.** Rust three, Django four, Astro three or four, VS Code
  six, Claude Code one headline plus three per week (two on the full
  page). Linear's own advice (2020-05-18): lead with one to three
  significant changes, then gather the small ones; "Remember to write
  about things that are interesting to a human. Don't include
  everything you do." (https://linear.app/blog/startups-write-changelogs)
  Kubernetes' communications handbook says it in capitals: "NOT EVERY
  KEP NEEDS A HIGHLIGHT."
  (https://github.com/kubernetes/sig-release/blob/master/release-team/role-handbooks/communications/README.md)
- **The unit.** A feature the reader can use, named, with what it
  lets him do; never a change to the code or to a rule. Matplotlib's
  instruction for a "What's new" entry: "A description of the feature
  from the user perspective. This should include what the feature
  allows users to do and how the feature is used. Technical details
  should be left out when they do not impact usage".
  (https://matplotlib.org/stable/devel/api_changes.html) GitLab's
  guidance gives the frame: "In previous versions of GitLab, you
  couldn't... Now you can...", a title of about seven words, a
  required link to the documentation.
  (https://docs.gitlab.com/development/documentation/release_notes/)
- **The shape of one item.** A headline that is the feature's name;
  two or three sentences on what it is and why it matters; one
  example, command or picture; one link to the documentation page.
  Claude Code's digest, Rust's post, Django's major features and
  Linear's changelog (a titled entry with a hero image and a lead of
  two to four sentences, fixes and improvements listed below) all
  have it. (https://linear.app/changelog)
- **The lead-in line.** Where a version or period is summed up in one
  sentence, it names the direction, not the contents: VS Code's "This
  release expands agent workflows, improves worktree reuse, and adds
  enterprise AI controls."; OpenSpec's release titles.
- **Voice.** Second person and present tense, the feature as subject,
  no superlatives. What keeps the tone from marketing in the examples
  read is concreteness: the command to run, what it costs ("Every
  run ... is a real model call on your account"), the maturity label
  ("Experimental", "Research Preview", "Beta"). **[O]** The Google
  developer style guide was fetched for a rule on this and yielded
  only its general advice against overstating; no dedicated page on
  release communication was found there. **[V]** that nothing was
  found.
- **Audiences.** No source read names the three readers of the
  question (the upgrader, the returning user, the newcomer deciding
  whether to look) as such. The projects separate them by document:
  the changelog and the compatibility section for the upgrader, the
  "what's new" piece for the returning user, the README and the
  announcement for the newcomer. **[O]** A 2025 study of release-note
  generation reports that what readers want differs by kind of
  project and by role, without the same split. **[V]**
  (https://arxiv.org/html/2505.17977v1)

### 6. Lifecycle: per release for the large, per period for the frequent; the archive is the page itself

- Projects with a few releases a year write the news per release
  (Python, Django, Rust, Kubernetes). Projects that ship daily or
  weekly digest by period: Claude Code weekly over five to eleven
  versions, VS Code monthly, Linear by entry when there is something
  to tell. **[V]** Nobody read writes a news piece for every small
  release; where every release gets a post (Node.js), the post is the
  generated changelog. **[O]**
- The archive is the same page read downward (Claude Code index,
  Linear, Obsidian) or one page per version in the documentation
  (Python, Django). Past news is never deleted and never rewritten.
  **[V]**
- Staleness in a README: the only example found (OpenSpec) is one
  line, which is cheap to replace and cheap to remove. Nothing read
  says how such a line is retired. **[O]** A block that is generated
  at every release cannot go stale in content, only in relevance;
  that remark is this note's own.

### 7. Derivation: marked at the change, selected at the release (consensus among the large); a model drafts, a human signs (emerging)

- **Marked on the change record.** Python: the author adds a What's
  New entry with the change when it is "particularly interesting for
  end users". Matplotlib: one file per feature in
  `doc/release/next_whats_new/`, merged into the page at release.
  Node.js: the "Notable changes" section is filled from commits
  labelled `notable-change` or `semver-minor`, and "The ultimate
  decision rests with the releaser." Rust: a `relnotes` label opens a
  tracking issue where the text is proposed. OpenStack's reno: a
  release-note fragment has an optional `prelude` section, "General
  comments about the release. Prelude sections from all notes in a
  release are combined ... to produce a single prelude introducing
  that release", and "Usually only notes describing major features or
  adding release theme details should have a prelude." GitLab: the
  feature's own YAML item carries an optional `level` of `primary` or
  `secondary`, written by the product manager. Changesets: the
  summary says "WHAT the change is, WHY the change was made, HOW a
  consumer should update their code" and may run to as much markdown
  as wanted. **[V]**
  (https://docs.openstack.org/reno/latest/user/usage.html;
  https://github.com/changesets/changesets/blob/main/docs/adding-a-changeset.md;
  https://forge.rust-lang.org/release/release-notes.html; others as
  above)
- **Selected and written at the release, by hand.** Even where the
  candidates are marked early, the final cut is an editorial act with
  the bird's-eye view: Rust's release team discusses "what blog post
  topics we want" after the notes are compiled, a discussion called
  "pretty informal"; Kubernetes gathers suggestions from the groups,
  and the communications lead, the release lead and the enhancements
  lead decide at code freeze; Python's What's New has named editors.
  **[V]**
- **Generated by a model.** A 2025 research tool (SmartNote) ranks
  commits by a trained significance score and has a model write the
  notes; in its human evaluation it scored about 4 of 5 on
  completeness, clarity and organisation and 3.35 on conciseness, on
  23 projects and one model. **[V]** Practitioner writing is of one
  mind that such output is a draft: "Treat AI-generated release notes
  as a draft, never as a publish step. The model optimizes for
  plausible-sounding text, and a confidently invented 'fix' is
  indistinguishable from a real one until a user hits the gap."
  **[S]** (https://dev.to/nazar-boyko/ai-agents-for-release-notes-and-changelog-automation-kia;
  the fetch tool gave its date as 2024-06-19, the search listing
  suggested 2026; the date is not settled.) No source read reports a
  well-regarded project whose highlights are picked by a model
  without a human choosing. **[O]**

What the three ways share **[O]**: the selection is a judgement of
worth to the reader, and every project read gives that judgement to a
person; the difference is only whether candidates are flagged when
the change is made (cheap, fresh, many false positives) or looked for
at the release (needs the whole view, forgets).

## Options and trade-offs

For the forge the facts are: releases are frequent and small (4.46 to
4.49 within days); `RELEASE-NOTES.md` is a render for the user who
pulls, generated from the history log; the README is a render too; the
news the owner has in mind ("the new elicitation and what it is") was
built across several releases and is the main entry of none.
All options below are this note's synthesis.

**A. A short highlights head in the README.** A few lines near the
top: the news, each a name, a sentence and a link.
*For:* the one page every reader opens; the brief itself allows it
("perhaps the current news"); OpenSpec shows it can be one line.
*Against:* the README guides give it no place; with a release every
few days the block either changes constantly or lags; without a page
behind it there is nowhere for the "what it is" to stand, so the
block grows into the documentation the brief wants out of the README.
Works only as a pointer to B.

**B. A "what's new" page with its archive.** A document of its own
beside the release notes: newest news on top, each item a headline,
what it is and why it matters, an example, a link to the
documentation page; earlier editions below, never rewritten; every
edition names the span of versions it covers and links to their
sections in the release notes.
*For:* the consensus genre (Python, Django, Claude Code); gives the
"what it is" a home; separates the returning reader from the
upgrader without touching the release notes; the archive doubles as
the story of the project.
*Against:* a second outward document to keep; it needs documentation
pages to link to, which the sibling research is to settle; someone
must choose the items.

**C. Highlights at milestones or periods, not at every release.**
The news is written when there is news: at a major, or when a
capability built over several releases is complete, or per period.
*For:* matches how the forge's capabilities actually arrive; what
every frequent shipper read does (weekly, monthly); avoids inflating
a release of fixes into news.
*Against:* needs a rule or a decision for "when"; between editions
the newest news is silent on the last releases, which the pointer to
the release notes must cover. C is a property of B rather than a
rival to it.

**D. A notice in the tool after an upgrade.** After a pull that
brought new releases, the assistant says in the conversation what is
new: the Action required lines first, then the current news.
*For:* the forge's unique channel, since it runs inside an agent;
reaches the user at the moment the news is relevant, without his
opening any page; the desktop products do it (Obsidian, VS Code).
*Against:* thin evidence for agents, none for a framework like this;
the command-line convention is restraint and an opt-out; it serves
the upgrader and the returning user, not the newcomer; it is a
derivation of B and of the release notes and adds nothing if neither
is good; what it says depends on a model unless it reads a written
piece.

**E. Marking the change record at the write.** The history record of
a change carries a mark that it is news for the reader (reno's
prelude, Node's `notable-change`, GitLab's `level`), set when the
change is written and confirmed.
*For:* the judgement is made by the one who decided the change, while
it is fresh; the render then compiles and does not guess (the same
argument as row variant 2 of the earlier note); cheap.
*Against:* a new convention on the history record; a capability that
spans releases is no single record, so marks give candidates and
cannot replace the cut at the edition; without discipline everything
gets marked.

**F. A model writes the highlights from the release notes at render,
unmarked.**
*For:* nothing new to write.
*Against:* every source that discusses it treats model output as a
draft for a human; the selection is exactly the judgement nobody
read leaves to a model; two renders would choose differently.

## Relevance to this project

The earlier note's finding 4 said highlights sit as a head over the
list. That holds inside a release section, and three of the four
comparable frameworks do exactly that. It does not answer the owner's
complaint, because the complaint is about another reader. Every large
project read answers that reader with a second piece, not with a
better changelog; and the project nearest to the forge's situation,
the tool it runs in, digests many small versions into a periodic
"what's new" with one headline feature and the changelog one link
away.

**Recommendation** (findings and options for the principal's
decision, not a design):

1. **B with C as its rhythm:** one "what's new" piece beside the
   release notes, an edition when there is news and not at every
   release, each edition naming the versions it spans, few items,
   each a capability with what it is, why it matters, one example
   and one link. Past editions stay below as the archive. In the
   forge's terms this is a render with a recipe of its own; the
   release notes stay as they are, for the upgrader.
2. **A only as a pointer:** in the short README the brief wants, at
   most the headline of the current edition with a link, generated
   with the README so that it cannot lag; no news text in the README
   itself.
3. **E as the source of candidates, the cut at the edition by the
   principal:** a mark on the history record proposes; what becomes
   news is chosen when the edition is written, by a person, as in
   every project read. F is advised against as a selector; a model
   may draft the wording of an item already chosen.
4. **D later, and as a reader of 1:** a notice after a pull is the
   forge's own opportunity and the least proven; it is worth having
   only once the written piece exists for it to quote, and with a way
   to keep it quiet.

Points 1, 3 and 4 each introduce something new (a document, a mark on
the history record, a behaviour after a pull) and are therefore
proposals under prime directive 2, to be taken through the brief and
`/forge intent`, never adopted from this note.

**What stays uncertain.** Whether a one-line news pointer in a README
helps or harms was found argued nowhere; the stance above is
inference from two README guides and one example. The in-tool notice
rests on two secondary sources for desktop products and on no example
among agent frameworks. The Kubernetes "Spotlight" section and the
VS Code in-product behaviour were not read at source. All quotations
except those from the two Claude Code pages passed through a
summarising model and should be checked at the URL before being
quoted onward. No published guidance was found that names the three
audiences and assigns each a document; that mapping is this note's.

## Sources

All fetched 2026-10-03.

- Python, What's New in Python 3.14 - https://docs.python.org/3/whatsnew/3.14.html
- Python developer guide, committing (What's New and NEWS entries) - https://devguide.python.org/core-team/committing/
- Rust blog, Announcing Rust 1.99.0, 2026-10-01 - https://blog.rust-lang.org/2026/10/01/Rust-1.99.0/
- Rust Forge, release notes process - https://forge.rust-lang.org/release/release-notes.html
- Django 6.0 release notes - https://docs.djangoproject.com/en/6.0/releases/6.0/
- Django weblog, Django 6.0 released, 2025-12-03 - https://www.djangoproject.com/weblog/2025/dec/03/django-60-released/
- Django, submitting contributions (release notes required) - https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/
- Kubernetes blog, Kubernetes v1.37, 2026-08-26 (truncated by the tool) - https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/
- Kubernetes SIG Release, communications role handbook - https://github.com/kubernetes/sig-release/blob/master/release-team/role-handbooks/communications/README.md
- VS Code release notes 1.140, 2026-09-30 - https://code.visualstudio.com/updates
- TypeScript blog, Announcing TypeScript 7.0, 2026-07-08 - https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
- Node.js blog, releases - https://nodejs.org/en/blog/release/
- Node.js, release process (Notable changes) - https://github.com/nodejs/node/blob/main/doc/contributing/releases.md
- Astro blog, Astro 7.3, 2026-09-03 - https://astro.build/blog/astro-730/
- Astro blog, What's new in Astro, September 2026 - https://astro.build/blog/whats-new-september-2026/
- Next.js blog (index only; latest posts were security releases) - https://nextjs.org/blog
- Obsidian changelog - https://obsidian.md/changelog/
- Obsidian forum, how to show current release notes - https://forum.obsidian.md/t/how-to-show-current-release-notes/83633
- Linear changelog - https://linear.app/changelog
- Linear blog, on startups writing changelogs, 2020-05-18 - https://linear.app/blog/startups-write-changelogs
- Stripe API changelog - https://docs.stripe.com/changelog
- Claude Code changelog - https://code.claude.com/docs/en/changelog
- Claude Code, What's new (weekly digest index) - https://code.claude.com/docs/en/whats-new
- Claude Code, Week 37 digest - https://code.claude.com/docs/en/whats-new/2026-w37
- Claude Code, commands reference - https://code.claude.com/docs/en/commands
- GitHub Spec Kit, README and releases - https://github.com/github/spec-kit ; https://github.com/github/spec-kit/releases
- BMAD Method, README and releases - https://github.com/bmad-code-org/BMAD-METHOD ; https://github.com/bmad-code-org/BMAD-METHOD/releases
- OpenSpec, README and releases - https://github.com/Fission-AI/OpenSpec ; https://github.com/Fission-AI/OpenSpec/releases
- Superpowers, README and RELEASE-NOTES.md - https://github.com/obra/superpowers ; https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md
- Matplotlib, instructions for What's new and API change notes - https://matplotlib.org/stable/devel/api_changes.html
- OpenStack reno, usage (prelude section) - https://docs.openstack.org/reno/latest/user/usage.html
- GitLab, release notes for features - https://docs.gitlab.com/development/documentation/release_notes/
- Changesets, adding a changeset - https://github.com/changesets/changesets/blob/main/docs/adding-a-changeset.md
- GitHub, automatically generated release notes - https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
- Make a README - https://www.makeareadme.com/
- Standard Readme specification - https://github.com/RichardLitt/standard-readme/blob/main/spec.md
- update-notifier - https://github.com/yeoman/update-notifier
- SmartNote, an LLM-powered release note generator, 2025-05 - https://arxiv.org/html/2505.17977v1
- DEV Community, AI agents for release notes and changelog automation (date unsettled) - https://dev.to/nazar-boyko/ai-agents-for-release-notes-and-changelog-automation-kia
- Fetched without yield: Google developer documentation style guide (no page on release communication found); a Write the Docs guide page and a usability-research article on release notes (both 404).
