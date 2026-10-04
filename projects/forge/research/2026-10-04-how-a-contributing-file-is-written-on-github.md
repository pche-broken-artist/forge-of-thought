---
project: forge
type: research
topic: how a CONTRIBUTING file is written on GitHub — where it lives and where GitHub shows it, what it holds by GitHub's own guidance and by the common templates, how long it is in three neighbours of the forge (Spec Kit, OpenSpec, BMAD), how projects demand that a substantial change be written down before it is built, how they treat contributions made with AI, and whether the community health files raise a repository's visibility
date: 2026-10-04
derived_from: the principal's word of 2026-10-04 (a CONTRIBUTING for the forge that above all encourages feedback and ideas, takes finished changes by pull request on the rule that a functional change is recorded in the chain, and a change of a document goes through its recipe; "in the scope and structure GitHub uses"); the Community Standards page of the forge's repository as read on 2026-10-04; POS.0170, POS.0720, POS.0980, POS.0990 of 10-intent.md v4.57
status: immutable
---

# How a CONTRIBUTING file is written on GitHub

## Question

What does a CONTRIBUTING file hold and how is it shaped, by GitHub's
own guidance and by the practice of projects close to the forge, so
that the forge's file is written in the scope and structure a visitor
of GitHub expects?

## Method and epistemic status

Read on 2026-10-04: two pages of GitHub Docs, the Open Source Guides
page on starting a project, the CNCF template, the CONTRIBUTING files
of three neighbours (github/spec-kit, Fission-AI/OpenSpec,
bmad-code-org/BMAD-METHOD) and the README of rust-lang/rfcs. Each
page was read through a summarising fetch, not line by line: headings
and quoted sentences are as the fetch returned them, and the lengths
are its estimates. Publication dates were not shown on the pages;
all are the versions live on the day. obra/superpowers has no
CONTRIBUTING at the path tried (404).

Marks: **[C]** stated by the source itself; **[P]** practice seen in
the files read, three projects and no survey; **[X]** not established.

## Key findings

### 1. Where it lives and where GitHub shows it [C]

GitHub Docs, "Setting guidelines for repository contributors": the
file may stand in `.github/`, in the repository root or in `docs/`,
and where several exist that order decides. GitHub then links it in
three places: a Contributing tab in the repository overview beside
the README, a link in the sidebar, and the pages where an issue or a
pull request is created. A personal account or an organisation can
hold default files for all its repositories in a repository named
`.github`.

### 2. What it is for and what it holds [C]

- GitHub Docs: for the owner it says "how people should contribute";
  for the contributor it helps to submit "well-formed pull requests"
  and open "useful issues". Suggested content: steps for good issues
  and pull requests, links to documentation and to a code of conduct,
  expectations of behaviour.
- Open Source Guides, "Starting an Open Source Project", lists six
  things: how to file a bug report, how to suggest a feature, how to
  set up the environment and run tests, the types of contributions
  wanted, the roadmap or vision, and how contributors should or
  should not get in touch. On tone: "a warm, friendly tone and
  offering specific suggestions for contributions ... can go a long
  way". It also says to link the file from the README.
- The CNCF template states the goal in one sentence: "The goal of a
  CONTRIBUTING.md file is to increase the number of successful
  contributors to your project." Its sections: Introduction, Ways to
  Contribute, Come to Meetings, Find an Issue, Ask for Help, Pull
  Request Lifecycle, Development Environment Setup, Sign Your
  Commits, Pull Request Checklist. It advises to start "with a
  limited list of paths to contributing" and to split developer
  documentation into separate files.

The common skeleton across the three: a welcome, the ways to
contribute, how to report and suggest, what to do before a pull
request, what a pull request must carry, where to ask.

### 3. Three neighbours, three sizes [P]

| Project | Length (estimate) | Headings | Opens with |
|---|---|---|---|
| OpenSpec | about 280 lines | 5: Contributing; Open a discussion or an issue first; Decide whether it needs a change proposal; Make your change; Open the PR | "Thanks for helping improve OpenSpec. Every change starts here, including small ones." |
| BMAD-METHOD | about 850 lines | 20, from Our Philosophy over Reporting Issues, Before Starting Work and Pull Request Guidelines to Prompt & Agent Guidelines | "Thank you for considering contributing! We believe in Human Amplification, Not Replacement ..." |
| Spec Kit | about 1 050 lines | 21, most on evidence, review rubric, testing and AI contributions | "Hi there! We're thrilled that you'd like to contribute to Spec Kit." |

The shortest of the three is built as a path in the order a
contributor walks it, and it is the one whose rule is closest to the
forge's.

### 4. A substantial change is written down before it is built [P]

- OpenSpec: "PRs without a linked issue or a prior discussion may be
  closed", and "A new feature, a significant refactor, or anything
  that changes OpenSpec's architecture needs an OpenSpec change
  proposal first." The project asks contributors to use its own
  method on itself.
- Spec Kit: a large change "that materially impacts the work of the
  CLI or the rest of the repository" must be "discussed and agreed
  upon by the project maintainers"; it has a section "Does Spec Kit
  use Spec Kit?".
- BMAD: "Before you write code: talk to us on Discord. If your change
  adds features, restructures code, or touches more than a couple of
  files, confirm with a maintainer that it fits."
- Rust RFCs draw the line by kind of change. An RFC is needed for
  "any semantic or syntactic change to the language that is not a
  bugfix"; none for "rephrasing, reorganizing, refactoring", for
  improvements measured by objective criteria, or for changes
  "invisible to users". Feedback is sought before the RFC is written.

Two things recur: the line between a small change and a substantial
one is drawn by what the change touches, and the conversation comes
before the work.

### 5. Contributions made with AI are named in the file [P]

All three neighbours carry a rule, and they differ:
- Spec Kit: any AI assistance "must be disclosed in the pull request
  or issue".
- OpenSpec: "If a coding agent wrote the code, say which agent and
  model, and confirm you tested it. AI-generated code is welcome when
  it has been verified."
- BMAD: "we expect most contributions involve AI assistance ... What
  we require is heavy human curation. You must understand every line
  you're submitting".

### 6. Whether the files raise visibility [X]

GitHub Docs, "About community profiles for public repositories": the
checklist "checks to see if a project includes recommended community
health files" (README, CODE_OF_CONDUCT, LICENSE, CONTRIBUTING,
security policy, issue templates) so that maintainers see whether the
project "meets the recommended community standards" and contributors
can "decide if you'd like to contribute". The page says nothing of
search, ranking, Explore or recommendations. One search for a source
that ties the files to ranking found none. What is established is the
link GitHub shows at the moment of an issue or a pull request, and
the Contributing tab.

### 7. The forge's repository today [C]

Community Standards page, read 2026-10-04: Description, README and
License present; Code of conduct, Contributing, Security policy,
Issue templates and Pull request template missing. Issues are enabled
and none was ever opened. Whether Discussions are enabled could not
be read from the page.

## Options and trade-offs

**A. A short file built as a path** (the OpenSpec shape, about a
hundred lines or fewer): welcome; feedback and ideas first; before a
pull request; what a functional change must carry; a document is
changed through its recipe; contributions made with AI; contact. For:
a visitor reads it whole; it puts the wanted contribution, feedback,
first. Against: says little on review and none on tooling.

**B. A full guide** (the BMAD or Spec Kit shape): adds philosophy,
issue kinds, pull request size, commit messages, a review rubric,
validators. For: answers every question. Against: the forge has no
build, no tests and no second maintainer for most of those sections
to describe, and CNCF's own advice is to start with a limited list.

**C. A file that is a render**, as the README is, generated from the
intent by a recipe. For: it cannot drift from the forge's rules.
Against: the rule for contributions is a stance not yet in the
intent, so the position comes first either way; and a render is
regenerated only at a release.

On where it stands: the root, where a visitor of the file listing
sees it, or `.github/`, which keeps the root clean and wins where
both exist.

## Relevance to this project and recommendation

Recommendation, Claude's: **option A, in the repository root, with
the principal's rule as its centre**. The forge's rule, that a
functional change is recorded in the chain before it is built, is of
the same family as OpenSpec's change proposal and Rust's RFC, so a
reader of GitHub will know the pattern; the forge can say, as
OpenSpec and Spec Kit do, that it is made by its own method. The line
between what needs the chain and what does not should be drawn by
kind of change, as Rust draws it: a change of how the forge behaves
needs the intent, and the solution design where it solves something;
a fix of wording or of a broken path does not. A document that is a
render (the README, the release notes) is changed through its recipe
(POS.0720), which a contributor cannot know unless the file says so.
A sentence on AI belongs in it, since all three neighbours have one
and the forge is itself worked with an AI; which of the three stances
is the principal's to choose.

Three matters the file touches and the note cannot settle:
1. The rule for contributions is a stance of the principal that
   stands nowhere in the intent; POS.0170 says only that feedback
   from recipients has no channel of its own. By Intent-first it is a
   position before it is a file.
2. Whether the file is written by hand or is a render of a recipe
   (option C), and so what kind of document it is.
3. The channel for feedback: Issues are enabled and unused; whether
   Discussions are on is not known; the README gives an e-mail.

Not answered here: the other missing files (code of conduct, security
policy, issue and pull request templates). Each is a question of its
own.

## Sources

- GitHub Docs, Setting guidelines for repository contributors:
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
- GitHub Docs, About community profiles for public repositories:
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- Open Source Guides, Starting an Open Source Project:
  https://opensource.guide/starting-a-project/
- CNCF, CONTRIBUTING template:
  https://contribute.cncf.io/projects/best-practices/templates/contributing
- github/spec-kit, CONTRIBUTING.md:
  https://raw.githubusercontent.com/github/spec-kit/main/CONTRIBUTING.md
- Fission-AI/OpenSpec, CONTRIBUTING.md:
  https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/CONTRIBUTING.md
- bmad-code-org/BMAD-METHOD, CONTRIBUTING.md:
  https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/CONTRIBUTING.md
- rust-lang/rfcs, README.md:
  https://raw.githubusercontent.com/rust-lang/rfcs/master/README.md
- The forge's Community Standards page:
  https://github.com/pche-broken-artist/forge-of-thought/community
