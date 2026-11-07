---
date: 2026-11-07
project: forge
topic: where the boundary between the engine and the forge framework runs through the files a user clones
status: immutable
engine: claude
model: engine default
usage: —
run: —
derived_from: no plan; the principal's word of 2026-11-07 in the round over THR.0780, read beside THR.0230; the tree of the engine at commit b7a21e5, no web source
---

# The boundary between the engine and the forge framework runs through four things, not through the tree

<!-- A research note of one question, made by the session agent from
a reading of the engine's own files, not from the web: the sections
of the template that ask for web sources say so. Immutable from its
filing (CLAUDE.md, Document kinds). -->

## In short

Sorted file by file, the tree a user clones falls cleanly into the
engine (the universal mechanics) and the forge framework (what makes
the forge the forge: the chain, the reviewers' content, the recipe
genres, the working methods) almost everywhere: in `.claude/agents`,
in `templates/`, in most skills and most scripts. The boundary runs
through four things only: `CLAUDE.md`, which carries both layers in
one file; the three scripts that know the chain by name
(`forge-ledger`, `forge-check`, `forge-migrate`); the forge skill,
whose state map is a mechanism over the framework's definitions; and
the walkthrough hook, an engine mechanism carrying framework text.
Everything "between" is one shape: a mechanism that names the forge's
artefacts instead of reading them from the definitions. Sure as a
reading of the tree on the day; a reading, not a run.

## Question

Where does the boundary between the engine and the forge framework
run through the files a user clones today, file by file, and which
files carry both? The vocabulary is the principal's of 2026-11-07:
the engine is the mechanics that would serve any framework; the forge
framework is the agents, the reviewers, the elicitation, the chain;
the projects are what a user makes. Asked so that THR.0230, which
asks whether the forge can be split into an engine and the rest, has
a list instead of a definition in words, and so that THR.0780, the
cut of the forge's own project from the engine, is seen to be a
different cut. Known items: THR.0230's three layers and its sketch of
the boundary; SOL.0500, where *engine* means the whole repository
against the projects. The baseline the note must beat: THR.0230's
own sketch, which names the layers but no file.

## Key findings

**F1. The engine, the content-blind mechanics.** [single source: the
tree at b7a21e5] Git: `forge-save`, `forge-pull`, `forge-status`,
`forge-clone`, `forge-branch`, `forge-config`, `forge_repos`,
`hook-git`; `.gitattributes`, `.gitignore` and their templates; the
skills `save`, `pull`, `import-project`, `setup`, `end`;
`templates/CLAUDE.local.md`; `.claude/settings.json`. Documents and
versioning: `forge_docs`, `forge-report`, `forge-history`,
`forge_tools`; the templates `history`, `decisions`, `project`,
`index`, `index-bundle`; the skills `history`, `ledger`, `ingest`,
`man` and `manual`; `doc2md`. Rendering: the skills `render`,
`publish`, `recipe`; `md2pptx`, `md2docx`, `md2video`; the templates
`recipe` and `html-player`. Research: the skill `research`,
`forge-engine`, `forge-cite`, the templates `research` and
`research-plan`. Documentation: the skill `document`, the
`docs-contract`, the agents `docs-planner` and `docs-writer`,
`docs-check`, `docs-index`, `docs-state`, `docs_map`,
`templates/docs-map`. The reviewers as a mechanism: the skills
`critique`, `challenge`, `check` and the three contracts, and the
checks of bookkeeping, `check-light`, `check-project`,
`check-history`, `check-single-source-of-truth`. The skeletons of an
extension: `artefact-definition`, `critic-definition`,
`challenger-definition`, `check-definition`. Work products: the skill
`work` and `templates/work`. `tests/` with its fixture, `pytest.ini`,
the CI workflow; `tmp/`.

**F2. The forge framework, what makes the forge the forge.** [single
source: the tree] The chain: the five definitions of
`.claude/skills/forge/states/` and the templates `brief`, `intent`,
`assignment`, `brd`, `solution-design`, `thread`. The reviewers'
content: `critic-clarity`, `critic-essence` (it knows the drift of
the chain), the three challenger personas, `check-brd`. The recipe
genres: the templates `recipe-readme`, `recipe-release-notes`,
`recipe-presentation`, `recipe-screenplay`. The working methods: the
skill `walkthrough` and the method paragraphs of `CLAUDE.md`. The
extension of the forge itself: the skill `new-artefact`, which writes
into the forge's own project, and `check-engine`, which reads the
forge intent.

**F3. Between: one file of both layers, or a mechanism that names the
chain.** [single source: the tree]

| File | Why |
|---|---|
| `CLAUDE.md` | one file, both layers: Persistence, Repository layout, Versioning, Ledger and Isolated reviewers (the mechanism) are the engine's; Prime directives, Working methods, Document chain, the ID prefixes of the artefacts and Requirement style the framework's |
| `.claude/skills/forge/SKILL.md` | the state map is a mechanism; the chain it walks is the framework's |
| `scripts/forge-ledger.py` | the ledger is a mechanism; its tables know the artefact prefixes (POS, THR, REJ, FCT) and the files of the chain, 17 mentions |
| `scripts/forge-check.py`, `forge_check.py` | the clauses of the light and project checks know threads, the intent and the brief, 19 mentions; the module is the engine's, the clauses partly the framework's |
| `scripts/forge-migrate.py` | the shapes of the files of a release, the chain's files by name, 13 mentions |
| `scripts/hook-walkthrough.py` | an engine mechanism, a per-prompt hook, carrying framework text, the walkthrough rule |
| the skill `new-project` | scaffolds by kind; the files of the chain it lays down are the framework's |
| the skill `migrate` | the mechanism is the engine's, the shapes it brings the chain's |
| the skill `spinoff` | a mechanism bound to the requirement groups of an assignment |
| `templates/ledger.md` | the tables of findings and challenges are the engine's, the artefact rows the chain's |
| `tests/test_forge_check.py` | tests clauses that know the artefacts |
| `docs/` | generated from both; `docs/videos/` is a project's render living in the engine (POS.1540) |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | renders of the forge's own project describing the whole |

**F4. Not a layer: the repository's own.** [single source: the tree]
`LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `logo.png`,
`.mailmap`.

**F5. Every "between" has one shape.** [Claude's own inference from
F3] A mechanism that names the forge's artefacts, their files, their
prefixes, their sections, instead of reading them from the
definitions in `states/`. The work a split would have to do is
therefore one kind of work: those mechanisms read the chain from the
definitions and the prefixes from the definitions' heads, and
`CLAUDE.md` splits in two. Where the chain is read from the
definitions already, the forge skill's map, the boundary is clean.

## Unexpected

The cut THR.0780 makes, the forge's own project out of the engine's
repository, does not touch this boundary at all: it parts the
thinking about the forge from the engine with the forge framework on
it. The two threads are often said in one breath and are two
different cuts. [from the reading; the principal's word of 2026-11-07]

## Not found

How much of `CLAUDE.md` by lines is each layer's: not measured, the
file was read by section. Whether the three scripts could read the
prefixes from the definitions' heads today: not tried; the heads were
not read for it.

## Relevance to this project

For THR.0230: the list stands in for the definition in words; the
split, if taken up, is the work of F5, bounded and of one kind, plus
the division of `CLAUDE.md`. For THR.0780: nothing; the cut of
2026-11-07 goes elsewhere (POS.1980). Chosen against writing the
boundary into THR.0230 as prose: a thread would not carry a table,
and the list goes stale by itself, which a dated note says and a
thread does not. Claude's own: F5 and the note's title.

Consult when: THR.0230 is taken up; a mechanism is written that names
an artefact of the chain; `CLAUDE.md` is split; a second framework on
the engine is outlined; the boundary is drawn again after the chain
has grown.

## Sources

1. The tree of the engine at commit b7a21e5 (2026-11-06), read on
   2026-11-07: `git ls-files` outside `projects/forge/` and `docs/`;
   kind primary; read in full as a listing, the files of F3 opened
   where the listing did not decide; original.
2. `projects/forge/threads/THR.0230.md` and `THR.0780.md` as they stood
   on 2026-11-07; primary; in full; original.

## Opened and not used

None.

## Search record

`git ls-files` of the engine with `projects/forge/` and `docs/` folded;
`grep -c` over `scripts/*.py` for the artefact prefixes and the files
of the chain (POS., THR., REJ, FCT, 10-intent, 00-brief, assignment,
solution-design, brd); the listing of `.claude/skills/forge/`; the
header of `hook-walkthrough.py`; the directories of `docs/` by count.
No disconfirming query: a reading of a tree, not a search of the web.
Ended when every tracked file had a row.
