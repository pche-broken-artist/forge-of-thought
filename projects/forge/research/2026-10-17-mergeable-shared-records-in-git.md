---
date: 2026-10-17
project: forge
topic: mergeable shared records in git
status: immutable
derived_from: the principal's word of 2026-10-17 (work of several people, branches or windows on one project collides in the ledger, the histories and the indexes, never in the artefact); 10-intent.md v5.12 (POS.1110, POS.1490, REJ.0170); threads.md (THR.0090); CLAUDE.md (Ledger, Versioning & status, Document chain); web sources
---

# Mergeable shared records in git

## Question

How do git-based projects keep their shared record files - the
changelog, the decision log, the index, the registry, the lockfile -
from conflicting when several branches, windows or people write
them, and what does the field's answer say about the forge's
cascade, where one change in one artefact writes the artefact, its
history, the ledger and sometimes a thread or an index?

Companion: `2026-10-17-git-merge-drivers-and-their-limits.md`, the
mechanics of what git itself offers. Out of scope here, by the
principal's word: the collision of sequential counters (item IDs,
version numbers) when two branches each take the next free one; a
step of its own.

## The forge's cascade, measured

What one operation writes today (read from the skills, 2026-10-17):

| Operation | Files written | Of which shared and append-at-the-tail |
|---|---|---|
| a position written into the intent | `10-intent.md` (the item and the front-matter counter), `10-intent.history.md` (records appended), `ledger.md` (Documents row, Waiting on principal), often `threads.md`, sometimes `decisions.md` | the history, the ledger, the threads, the decisions |
| `/research` | `research/<date>-<topic>.md` (new, unique), `research/00-INDEX.md` (entry appended), `ledger.md` (Research row) | the index, the ledger |
| `/check`, `/critique`, `/challenge` | `reviews/…` or `challenges/…` (new, unique), `ledger.md` (Findings or Challenges rows, each later re-edited for its state) | the ledger |
| `/render`, `/publish`, `/work`, `/ingest` | the output (unique), `ledger.md` (one row), `sources/00-INDEX.md` for an ingest | the ledger, the index |

The artefact itself is the one file that merges well: an item is a
block of text with its own ID, two branches adding two items touch
two places. Every other file the cascade writes has one of three
shapes, and each shape conflicts for a reason of its own:

1. **Derived state.** The ledger's tables Briefs, Documents,
   Renders, Published, Work, Sources, Research, Dependencies mirror
   what the files already say: a version in a front-matter, a
   provenance in a render, a file in a directory. Two branches both
   rewrite the mirror, and git sees two edits of one table.
2. **Append-only logs.** The history logs, `decisions.md`,
   `threads.md`, the Findings and Challenges tables, the index
   entries: every writer appends at the tail, so every pair of
   branches collides on the same last lines. This is the textbook
   changelog conflict.
3. **Sequential counters.** `version:` in the front-matter and the
   next free ID: two branches each take the same next value and the
   merge is clean in git's eyes and wrong in the forge's (the "known
   hole" of POS.1110). Not this note's.

## Key findings

**F1. The field's first answer to shape 2 is one file per record,
assembled at release.** [consensus] Changelog tooling converged on
"news fragments": every change is its own small file in a
directory, and a release step concatenates them into the changelog
and deletes them. towncrier (Twisted, pytest, pip, PyInstaller),
scriv, reno and changesets all work this way; the stated reason is
exactly that one single file "that developers all write to"
produces merge conflicts (towncrier README; PyInstaller
development docs). Decision logs reached the same place
independently: projects that kept one `DECISIONS.md` report that
"any two open PRs conflicted there" and moved to one file per
decision with a generated index (archkeel PR 37; PenniLogic/docs
issue 70; it-minds/troupe issue 437). ADR practice has been one
file per decision from the start, the log being an index of them.
The one thing the fragment does not solve, the same sources say, is
the identifier: "a decision needs one thing more than a changelog
entry: an id that's unique without two branches agreeing on it"
(ascribe issue 381) - the counter problem, deferred here.

**F2. The field's answer to shape 1 is: do not merge a derived
file, regenerate it.** [consensus] Lockfiles are the mature case.
npm ships `npm-merge-driver`; the pattern is take one side, rerun
the generator (`npm i --package-lock-only`), validate (`npm ls`),
commit (boneskull/package-lock-merge-driver; npm/npm-merge-driver).
`derived-merge` goes one step further and merges the lockfile as a
map keyed by identity, where distinct additions never conflict and
only two different values for one key do. For generated
documentation the same rule holds: committed generated files
"conflict on every merge from main: 84 of 88 conflicts" and "the
only correct resolution is to regenerate on the merged tree"
(adewale/agentic-mermaid issue 304); mdsmith installs a merge
driver that, on a conflict in a generated block, "re-runs the
directive and keeps the regenerated body, so the conflict never
reaches you". Whether to commit the generated file at all is
answered both ways; where it is committed, the governance pattern
is a check-only hook that fails when the file is stale and prints
the regeneration command, never a hook that regenerates and stages
silently (Livepeer generated-artifact policy).

**F3. git's built-in `merge=union` is not an answer for a record
file.** [verified on git's documentation and on field reports] The
documentation itself says the union driver "tends to leave the
added lines in the resulting file in random order and the user
should verify the result. Do not use this if you do not understand
the implications" (gitattributes). Reports from projects that used
it on changelogs and ledgers list the failures: the blank line or a
whole line at the seam written once or lost (btclib-org issues
453, 1460, 1582), a line edited on both sides kept twice
(choiceoh/stkernel PR 1222), a line one branch removed brought back
(dsifry/metareview PR 211), and `git rebase` exiting 0 on all of
it. A union driver that is safe for records exists in git only for
notes: `git notes merge --strategy=cat_sort_uniq`, "equivalent to
cat | sort | uniq", a set union of lines (git commit a6a09095).
That is the shape a record-aware driver must have: lines as a set,
deduplicated, ordered by a key, never positional.

**F4. Structured merge drivers exist, Markdown tables are not
among their formats, and no driver runs where a merge request is
merged.** [verified] mergiraf merges by syntax tree for code and
JSON, YAML, TOML; Weave claims Markdown among its formats
(unverified beyond the listing); cfgmerge and git-json-merge cover
config formats; nothing found merges a Markdown table or a bullet
log by record. Every driver is registered in `.git/config`, which
git does not share: the repository tracks only `.gitattributes`,
and each clone must register the driver itself, which is why
derived-merge does it from a `postinstall` hook and Weave from a
`setup` command. And the hosting platforms merge without drivers:
GitLab.com does not support custom merge drivers at all,
self-managed GitLab only by an administrator's configuration, and
the built-in `union` is ignored when a merge request is merged
(GitLab issues 17325, 18830; GitLab docs, Git attributes);
Bitbucket has the same open tickets (BCLOUD-20234, BSERV-19161);
GitHub's web merge is not documented to honour drivers. The
companion note has the mechanics.

**F5. The event-sourcing shape fits the forge's records and is
emerging in git-native tooling.** [emerging] Append-only events in
files with distinct names, content-hash IDs, and projections
rebuilt from the events rather than merged (troupe-run/troupe
issue 1, a design in progress; the general event-sourcing
literature on rebuildable projections, Azure Architecture Center).
Beads, a git-backed tracker for coding agents, moved from
sequential to hash IDs in 0.20.1 precisely so that "concurrent
task creation by multiple agents or branches no longer collides",
and later moved its source of truth from a JSONL file to a database
with cell-level merge (gastownhall/beads README). Pointer for the
counter step, not a finding of this note.

**F6. Requirements tooling in git stores one item per file.**
[verified on Doorstop's docs] Doorstop keeps every requirement as a
YAML or Markdown file in a directory, the document being the
directory; the index and the published views are generated. Nothing
found on how it handles the next-UID collision across branches.

## Options for the forge

| Option | What it is | Merges locally | Merges in a merge request | Cost | Verdict |
|---|---|---|---|---|---|
| A. `merge=union` on the ledger, the histories, the decisions | one line in `.gitattributes` | silently wrong at the seam (F3) | ignored | none | not an option |
| B. a record-aware merge driver for the logs | a forge script: lines as a set of records, union, dedup, sorted by date and version; registered by `/setup` in every repository (F3, F4) | yes, in `/save`'s rebase and in `git merge` | ignored; the conflict then comes to the clone and the driver resolves it there | one script, one `.gitattributes` per project, one `/setup` step | right for the histories and `decisions.md`, wrong for the ledger (which is not a log but a mirror) |
| C. the ledger derived | a script generates `ledger.md` from the documents; what the ledger alone knows today moves into the documents it describes (below); a conflict is resolved by regenerating; `/check light` becomes the check-only hook of F2 | yes, by regeneration | the conflict comes to the clone and is regenerated away | the script; moving the ledger-only facts; the ledger's kind changes from `state` written by the forge to generated like `docs-map.md` | the principled fix for shape 1 |
| D. one file per record for the logs | `decisions/DEC.NNNN.md`, a settlement record per finding, a view generated | yes, by construction | yes, by construction | many small files; a history round makes several records a day, too many files for a log | right for decisions and for findings' settlements, wrong for the history log |
| E. the cascade written once, at `/save` | every operation writes only its own file; the ledger and the indexes are regenerated at the save | reduces the window, not the conflict | - | a step towards C | not a destination; C makes it unnecessary |

What the ledger alone knows today and would need a home in the
documents under C: the mined state and note of a brief (into the
brief's front-matter), a source's date and its origin (into the
index entry or a front-matter), a research note's `Derived from`
(into the note's front-matter, where this note already carries
it), a render's provenance (already in the render's front-matter),
a published file's state (into a sidecar or derived from dates),
the state and resolution of a finding or a challenge (into the
history record that settled it, or a settlement file per D), and
Waiting on principal (derived from the open threads, the open
TBCs, the parked findings; the free-text lines are the one
residue). Each is a small move; together they are the design.

## Relevance to this project

The forge already has every piece the field's answer is made of:
the records carry IDs, the artefacts carry front-matter with the
version, the renders carry provenance, `docs-map.md` is already a
generated state file that no one writes by hand, and `/save`
rebases locally, which is where a merge driver runs. What the forge
does not yet do is treat the ledger as what it is, a projection,
and the logs as what they are, sets of records.

**Recommendation, in the order to take it:**

1. **Make the ledger a derived file** (option C): one script,
   `scripts/forge-ledger.py` or a name the principal chooses,
   regenerates `ledger.md` from the documents; every skill that
   writes a ledger row today calls the script instead; a merge
   conflict in the ledger is settled by running it; `/check light`
   compares the committed ledger with a fresh generation and reports
   staleness as a finding. The facts the ledger alone holds move
   into the documents first, in the walkthrough this note offers.
   This removes the ledger from every collision at once, for two
   people, two branches or two windows alike, and it is the change
   that fixes the complaint as stated.
2. **Give the append-only logs a record-aware merge driver**
   (option B): one script that merges a history log, `decisions.md`
   and the index as sets of records, registered by `/setup` and by
   `/new-project` through the project's `.gitattributes`; the
   histories keep their shape, one record per line, which is what
   makes the set union safe. Where the merge happens on the server
   the conflict comes back to the clone unmerged and the driver
   settles it there, in `/save`'s rebase (POS.1490); the forge
   says so and does not promise more.
3. **Take the counters next** (shape 3), as the principal said:
   IDs and version numbers that two branches can take without
   agreeing; Beads' hash IDs and the ADR projects' reasoning are
   the starting pointers. Until then the two drivers above make
   every collision but the counters' disappear.

What this does not touch: the artefacts themselves, the chain, the
immutability of records (a set union never edits a record), the
rule that the forge never merges on its own judgement (POS.1490:
the driver runs inside the merge the user ordered, exactly as git's
own text driver does today).

## Sources

- git, gitattributes documentation, merge drivers and the `union`
  warning: https://git-scm.com/docs/gitattributes
- git, `git notes merge` strategy `cat_sort_uniq`, commit a6a09095
  (2010): https://git.lorimer.id.au/gitweb.git/diff/a6a09095a08339afc8468d053ff978ed4662a1d5
- towncrier: https://github.com/twisted/towncrier
- PyInstaller, Changelog Entries: https://pyinstaller.org/en/stable/development/changelog-entries.html
- Test and Code 202, Using Towncrier (towncrier, scriv, reno compared): https://pythontest.com/testandcode/episodes/202-using-towncrier-to-keep-a-changelog/
- archkeel PR 37, one file per decision after a conflict committed unresolved: https://github.com/rapiddweller/archkeel/pull/37
- PenniLogic/docs issue 70, per-decision files and a generated index: https://github.com/PenniLogic/docs/issues/70
- it-minds/troupe issue 437, decisions one file each so pull requests stop conflicting: https://github.com/it-minds/troupe/issues/437
- ascribe issue 381, a decision needs an id two branches need not agree on: https://github.com/ascribed-dev/ascribe/issues/381
- npm/npm-merge-driver: https://github.com/npm/npm-merge-driver
- boneskull/package-lock-merge-driver (validates with `npm ls`): https://github.com/boneskull/package-lock-merge-driver
- derived-merge, a lockfile merged as an identity-keyed map: https://github.com/ShawezA/derived-merge
- agentic-mermaid issue 304, committed generated files conflict on every merge: https://github.com/adewale/agentic-mermaid/issues/304
- mdsmith, git-native: a merge driver that regenerates generated blocks: https://raw.githubusercontent.com/jeduden/mdsmith/HEAD/docs/features/git-native.md
- Livepeer, generated artifact and hook governance (check-only hooks): https://docs.livepeer.org/docs-guide/policies/generated-artifact-and-hook-governance
- btclib-org issues 453, 1460, 1582 and portanode PR 462, `merge=union` losing lines at the seam: https://github.com/btclib-org/portanode/issues/453 , https://github.com/btclib-org/btclib-node/issues/1460 , https://github.com/btclib-org/.github/issues/1582 , https://github.com/btclib-org/portanode/pull/462
- choiceoh/stkernel PR 1222, a ledger under `merge=union`, same-line edits kept twice: https://github.com/choiceoh/stkernel/pull/1222
- dsifry/metareview PR 211, union bringing back a removed line; web merges not honouring drivers: https://github.com/dsifry/metareview/pull/211
- mergiraf: https://terminaltrove.com/mergiraf/
- Weave, entity-level merge driver: https://raw.githubusercontent.com/Ataraxy-Labs/weave/main/README.md
- jelmer/awesome-merge-drivers: https://github.com/jelmer/awesome-merge-drivers
- GitLab, Git attributes (custom drivers: self-managed only, invoked only on a non-trivial conflict): https://docs.gitlab.com/user/project/repository/files/git_attributes
- GitLab issues 17325 (`merge=union` ignored in merge requests) and 18830 (custom drivers in MRs): https://gitlab.com/gitlab-org/gitlab-foss/-/issues/17325 , https://gitlab.com/gitlab-org/gitlab/-/issues/18830
- Bitbucket tickets BCLOUD-20234, BSERV-19161: https://jira.atlassian.com/browse/BCLOUD-20234 , https://jira.atlassian.com/browse/BSERV-19161
- troupe-run/troupe issue 1, an event store in git, one immutable file per append: https://github.com/troupe-run/troupe/issues/1
- Azure Architecture Center, Event Sourcing pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
- Beads, git-backed tracker with hash IDs: https://github.com/gastownhall/beads
- Doorstop, requirements management using version control: https://github.com/doorstop-dev/doorstop
