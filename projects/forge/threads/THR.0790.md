---
id: THR.0790
concerns: intent
origin: the principal
status: open
---

What the forge looks like from GitHub, and what of it is to be
mended: tests, the entry threshold, the bus factor and the threads
as issues. On 2026-11-03 the principal had the repository read
through `gh`, the metadata, the releases, the issues and pull
requests, the discussions, the Pages site, the traffic of fourteen
days, the stars and the forks, with the local clone beside it, and
asked what is good and what is bad. What was read, as facts of that
day: 12 stars, 2 forks, 13 watchers; one issue and one pull request,
both closed, the pull request from an outside author and merged;
four discussions, three of them the principal's release
announcements; the community profile at 85 per cent, README,
licence CC BY 4.0, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY,
fourteen topics and the documentation on GitHub Pages present, the
issue and pull request templates the only two things missing; four
releases, v3.0 to v6, each with a discussion; 152 commits on 45
days between 2026-08-30 and 2026-11-02, 143 of them the
principal's, under three author names on one email; CLAUDE.md of
884 lines and 55 KB, the skills 2 244 lines, the scripts 6 891
lines of Python, the documentation 102 generated pages; the forge's
own intent with 461 positions, 75 rejections, 57 decisions, 91
reviews and 11 challenges; no tests in the tree, the fixtures only
in `tmp/`, no CI but the Pages build; the homepage field of the
repository empty, the wiki enabled and unused. The traffic: 390
views by 43 people, the most read pages after the overview the
install page, the documentation index and the setup page; 959
clones by 515 people, a ratio of crawlers and scrapers, not of
adoption; the referrers github.com and Microsoft Teams; the stars
in one wave from 2026-10-28 to 2026-10-31, colleagues by their
names.

What is good, in Claude's reading: the profile is complete but for
the two templates; the release discipline, tags, announcements and
release notes with a "For you" at every change, is beyond what a
project of this size usually has; the forge running on itself, the
positions, the rejections, the decisions and the reviews, is the
strongest argument an evaluator gets, the method shown and not
described; outside contribution exists, a merged pull request, an
issue, two forks, within two months; and the readers go past the
front page, the install page being the second most read, with 12
stars out of 43 unique viewers a good rate.

What is bad or at risk, in Claude's reading: no formal tests and no
CI for some 7 000 lines of Python, the portability of CLAUDE.md
Persistence a writing rule and not a run, the first thing a
contributor looks for and the first thing a change breaks; a high
entry threshold, CLAUDE.md loaded whole into every session with the
skills and the hook on every prompt, a README of nine sections with
the quickstart fifth, an install page of 239 lines and a first
result of 283, philosophy before the first command, and the
condition of a paid Claude Code narrowing the audience; the house
vocabulary, principal, render, recipe, ledger, walkthrough, verdict
line, consistent inside and opaque to a reader who skims, with no
glossary in one place; the workshop and the engine in one
repository, so that a user clones the author's thinking with the
tool, which THR.0780 already works; a bus factor of one, the author
under three names in the history; the clones not to be read as
adoption, the real reach being the views and their sources sharing
at work, a company wave and not an organic one; and the small
things of GitHub, the empty homepage, the unused wiki, the missing
templates, and 29 open threads in `threads/` where no visitor finds
them, no roadmap visible from outside.

The principal's preliminary conclusion, not yet a position: tests
yes, the trials made so far formalised into a suite and a CI run,
so that the portability rule becomes a run; the threshold
undecided, perhaps the README made more human; the three names
cleaned without rewriting history, one email behind all three so
GitHub already counts one contributor, a `.mailmap` at the engine
root for git's own tools; and the thought whether the open threads
become GitHub issues, so that where the forge wants to go is
visible from outside. Should this reading be wanted again, the
forge's way is a lens or a check of its own, `github`, a decision
for the round, never an ad hoc file in `reviews/`. Not worked now;
to be taken as a round over the intent when the principal has the
strength for it. Read beside THR.0780, the workshop as a repository
of its own, which decides where the threads would live. Opened
2026-11-03.

2026-11-07: the tests done, POS.1930 to POS.1960 and the brief
`tests` mined, 221 tests green locally and in CI on Linux and
Windows; the `.mailmap` done 2026-11-03. Open: the README more
human, the threads as issues, the two GitHub templates, the
homepage field.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
