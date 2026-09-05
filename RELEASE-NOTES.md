---
project: forge
render: release-notes
generated: 2026-09-05
recipe: recipes/release-notes.md v0.6
inputs:
  - projects/forge/10-intent.history.md
  - projects/forge/10-intent.md v3.34
  - projects/forge/decisions.md
  - RELEASE-NOTES.md (previous edition, released sections)
---

# Forge of Thought — Release Notes

An Unreleased section covering the changes since the last approved
major, then one section per approved major version of the system,
newest first. The fine-grained change log lives in the intent's
Version History companion, `projects/forge/10-intent.history.md`.

## Unreleased — 3.x since 3.0

These changes are not yet approved; they cover intent versions 3.1 to
3.34, made between 2026-08-30 and 2026-09-05.

**Save and release are two commands.** THR.0220 — the cost of
rendering at every save — was closed by walkthrough on 2026-09-05, and
the forge gained its second door to git. `/save` is commit and push on
whatever branch is checked out, through `forge-save`, with no check
and no render: a commit message proposed and confirmed, the script
run, seconds. `/release` runs on `main` only and refuses elsewhere,
naming the branch it found: the full check with its walkthrough, the
README and release notes from the settled sources, the release commit
"release <intent version>" through `forge-save`, and at an approved
major the tag — the commit and the tag being `/save` run by `/release`
with the release message, not a second procedure; named without a
slug, `/release` asks which repository and never sweeps. It offers
`critique essence` once — the one lens that guards what a release
publishes, the drift of the chain — and runs no reviewer on its own;
neither reviewer runs at a save (POS.0400). Why two words: the
two-speed save had existed in practice for weeks — cosmetic changes
saved through `forge-save.ps1` from the shell, `/save` reserved for
changes that touched the README — and the renders at 5,700 words cost
seven to eight minutes and well over a hundred thousand tokens at
every save; with the renders at the release only, the README on
`main` is current at every release and stale in between only where
work happens on `main` itself, visibly in the `/forge` map, never
silently (POS.1100). Of the three candidates the thread had recorded,
stale-only regeneration at the save was rejected as REJ.0160 — it
saves perhaps a third of the engine's saves and nothing on projects,
whose README input, the ledger, moves at every operation, and it adds
a staleness state that `/save`, `/forge` and `/check` must all read
alike — and a fixed working branch with a forge switch that merges as
REJ.0170, the first step towards the wrapper of git the principal
does not want. The conformance check thereby belongs to the release,
not to the save (POS.0570): a light check fit for a save — ledger
bookkeeping, version and status agreement, the companion row — is a
kind of check, born with the kinds of THR.0290 after the THR.0270
trial and added to `/save` then, not built twice on today's
mechanism; until then broken bookkeeping may lie in git between
releases and is caught at the release, knowingly. These notes are
from now rendered by every `/release` of the engine, not by every
save (this recipe, 0.6).

**Tags and voluntary branches.** At every release of an approved
major from `main` the tag `v<major>` is part of the step, proposed by
`/release` and confirmed by word — a rule of the procedure, not a gate
in the script. On request any tag on anything: `/save -Tag` or
`/release -Tag`, on a branch as well, the name free — whatever git
accepts — Claude proposing `v<intent version>` when none is given and
passing it to `forge-save -Tag <name>`, since the script knows git and
nothing of the forge; the script pushes the tag with the commit and,
without an origin, keeps and reports it. Only the major's tag has a
fixed name, so that `/check` and the release notes can rely on it, and
the name alone tells the level: an integer is a released major,
anything else a snapshot. Branches are voluntary and belong to git
(POS.1110): whoever wants one gets it through `forge-branch <name>`,
which creates the branch or switches to it, `forge-branch main`
switching back, and never types git; merge, rebase and conflicts stay
git's, by hand or by merge request, and `forge-status` reports the
current branch. Nothing forces a branch — whoever does not use them
works on `main`, saves and now and then releases, and sees none of
this. The forge's only knowledge of a merge is that `/release` runs on
`main` after it and its full check finds what two branches broke; the
known hole — two parallel branches taking the same next free ID — is
left until it happens. The boundary against the wrapper of git: the
script does creation and switching, which only change where the next
commit lands, and nothing that rewrites history. Grounded in a
colleague's practice of working on a branch of a subject project in
his own forge instance and merging by merge request without ceremony;
the forge stays a single-user tool per instance, more people meaning
more instances and coordination by git (bearing on THR.0090). The
condition under which DEC.0090's overruled finding would have
returned — THR.0220 changing POS.0550 — fell with POS.1110, and
nothing returns.

**The first release, and its check.** The operating layer for the two
doors was built the same day the thread closed: `release.md` new,
`save.md` narrowed, `forge-save -Tag` and `forge-branch.ps1` new and
tested, CLAUDE.md, the templates and the genre files aligned, both
recipes bumped. The `/check-forge` of the first `/release` returned
ten findings, all accepted by walkthrough: `/release` ends by running
`/save` with the release message and tag instead of restating its
steps, and asks for the repository when no slug is given; five
positions and two threads say release where they said save (POS.0310,
POS.0930, POS.1070, THR.0210, THR.0270) — `/release` runs only the
README and release-notes renders, every other render is the
principal's `/render`, and `/save` runs none; the scripts' count was
dropped from POS.0550 and `forge-status` reports the branch; the
readme recipe (0.37) recast Saving and syncing to the two doors; and
CLAUDE.md was reduced to the two-doors sentence with `release.md` as
the owner of the procedure.

**Every project gets a README and release notes.** The engine's own
mechanism is generalised: every project has a README and, if it is a
thought project, release notes — both renders of the project's own
recipes (`recipes/readme.md`, `recipes/release-notes.md`, with
`output:` in the project root), exactly as the engine has them. The
recipe is what is iterated, the render is never edited by hand, and
every release of the project regenerates both after its check; the
ledger's Renders table carries them like any render. A library has a
README only — a catalogue of what it holds — since release notes are
distilled from an intent's Version History and decisions, which a
library does not have. Every project README closes with the fixed
sentence that reading it needs nothing and maintaining it needs Forge
of Thought, linked — the engine's own README excepted, being that
sentence's destination (POS.1000).

**Genre skeletons scaffolded from the start.** `readme` and
`release-notes` are genres of `/recipe`, with skeletons
`templates/recipe-readme.md` and `templates/recipe-release-notes.md`;
`/new-project` scaffolds them and `/check` expects them.

**An optional project icon.** A project may carry `logo.png` in its
root, supplied by the principal and picked up as the repository
avatar by hosts that do so. A project without an icon is complete,
and `/check` never reports its absence (POS.1010).

**Cross-repository dependencies registered in the ledger.** A project
writes down what it relies on outside its own repository: the ledger
carries a Dependencies table — path, library, used by, note — with one
row per document of another repository the project cites, typically a
library document referred to by path or a deck template named in a
recipe. Registration only, like sources; no version is pinned, by
design, because a library document is maintained by its owner and
cited as a moving target. `/check` verifies that every registered
path exists on disk, the `/forge` map names which libraries the
project needs, and `/ingest` registers the row when the principal
directs a project to a library document instead of copying it. The
position was raised when a document moved from a project into a
library and the project's reliance on it and on its deck template
became invisible (POS.1020).

**The forge's behaviour lives in the engine, never in the assistant's
private memory.** The assistant keeps a per-directory memory outside
the repository; whatever it learns there about how the forge should
work — a working method, a rule of a command, a convention — is
written into `CLAUDE.md`, the commands or the templates and removed
from memory, so that every instance behaves the same and a new user
meets the same forge as the principal. The audit before the first
fresh deployment found most of that memory to be engine rules already
written or engine rules missing, and the missing ones moved in: the
working method Step by step (one consent-needing action at a time,
the exact operation and its reason stated, a seen plan is not
consent), the walkthrough's rule that an accept recommendation carries
the concrete text the artefact would receive, and one research per
question in `/research`. Instance facts that had lived in memory —
the git identities — moved to `CLAUDE.local.md`. Memory is left with
what is personal to one principal only (POS.1030).

**A source has one form.** A file in `sources/` is either text or a
functional binary, never both by default. At `/ingest` every binary
file — isolated or inside a bundle — gets one question: convert to
Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and that extract
is the source — tracked, registered, indexed, immutable — while the
original is not copied into the project, or is gitignored where it
already lies in `sources/`. No: the binary is the source as a
functional thing — a deck template, a graphic, a logo — kept as is
with no extract. Text files get no question; keeping both is the
exception, on the principal's explicit word. The ledger's Sources
table records the form (`text | extract of <original> | binary`)
instead of an extract flag, and `/check` treats a binary without an
extract, or an extract without its original, as the normal case. The
reason: the repository carries what the forge works with — text — and
a binary nobody reads from git is weight without use. The convention
applies from now on: earlier extracts keep their `.extract.md` names,
and a binary already in git beside its extract leaves the index only
on the principal's word, never automatically. Raised by the day's
`/check`, where four PDFs sat in git beside the extracts that alone
are ever cited (POS.1040).

**First run is one command.** After cloning the engine, `/setup`
copies `templates/CLAUDE.local.md` to the root and fills it by
interview — principal, conversation language, git identities — and
creates `.claude/settings.local.json` with the session model set to
Fable without asking: the recommendation embodied as the default,
with one notice sentence naming the change path (`/model` or editing
the file). Existing files are reported, never overwritten. The
git-identities interview closes with one offer — the global identity
guard described below — and `/setup` still runs no git operation:
the user's git configuration file is the one thing it may edit
outside the engine, on his word. The command is named `/setup`, not
`/init`, over the collision with Claude Code's built-in command.
Prompted by a newcomer observed struggling through the manual
install steps (POS.1050).

**An existing project arrives through one command too.**
`/import-project <git-url>` brings an existing project in through the
scripts-only git door: `scripts/forge-clone.ps1` clones into
`projects/<repository name>`, with no slug parameter because the
directory falls out of the repository's name, refuses to overwrite,
and reports facts: the last commit, the origin, the commit identity
git resolves for the fresh clone, and whether a ledger with `kind:`
is present. The script carries no identity and sets the repository's
local commit identity only when given `-Name` and `-Email`; the
command layer passes them by default, proposing the matching identity
from the roster in `CLAUDE.local.md` by the URL's host and confirming
it on the principal's word — the clone runs bare only when the
principal says his own git configuration resolves the identity. A
clone left with no identity is caught by `forge-save`, which reports
and commits nothing (POS.1060).

**The chain drawn as a star, and an authorship boundary.** The
README's Quickstart was rebuilt as a common head — clone, install
Claude Code, `claude` from the root, `/setup` — plus two named paths,
starting a new project and bringing an existing one, with selecting
the project (`/forge <slug>`) visible as the first act of work. The
chain diagram was redrawn from a line into the star: solid what is
built today, dashed a fixed set of illustrative future layers —
business analysis, an RFP, an article with its translation render,
strategy, solution design, an implementation deck — visibly marked as
not existing yet. Raised on the way, the render concept gained its
authorship boundary: a chain artefact is composed by the principal, a
render is generated — an article the principal writes is a layer, its
translation a render (POS.0710 extended); the sentence was carried
into CLAUDE.md's chain section in the round that followed.

**The commit identity settles on the project.** POS.0950 was
rewritten twice in the span and ends where it began at 3.0: the
commit identity is a property of the project, not of the host. Mid
span the walkthrough of the day's check findings adopted a per-host
model — git conditional includes (`includeIf`) in the user's own
configuration resolving the identity by each repository's host, with
`/setup` generating `~/.gitconfig-<host>` files and appending the
include block. At 3.8 that model was dropped on the principal's
decision: the host is only a correlate of the identity and fails
exactly where one host serves two roles — a personal and a company
organisation on the same github.com — and writing `~/.gitconfig-<host>`
files reached beyond the engine's boundary. Instead the identity is
set locally in every repository at its creation or import, proposed
by the command layer from the identity roster in `CLAUDE.local.md` —
matched by the origin's host as an offer, never a rule — and set on
the principal's word. The one global guard, now `/setup`'s closing
offer, is `user.useConfigOnly = true` with no global
`user.name`/`user.email`, so that a commit in a repository without a
local identity fails aloud instead of silently taking a default;
where a global identity survives, the guard is defeated and `/setup`
says so, offering the removal only on the user's word. A user's own
configuration — per-host includes included — remains his business and
a legitimate way to resolve an identity; `forge-save`'s
effective-identity check stays, and the scripts are unchanged
(POS.0950 rewritten, POS.1050 narrowed, POS.1060 aligned). The first
`clarity` critique later rewrote the position to open with the
per-repository identity and no longer narrate its own history
(FND.0140), and named a project without a repository — local-only,
for sensitive work — as a legitimate shape that `/check` and
`forge-save` report as a fact, never a finding (POS.0940, POS.0960).

**One mechanism lives in one place.** A new position and a tenth
prime directive: whatever the forge already has a procedure for — a
command, a skill, a script, an agent — is invoked through that
procedure whenever its situation arises, never re-described ad hoc.
`/release` regenerates renders through `/render`, git is touched
through the scripts, reviews run through the reviewer agents; a
command that needs another's mechanism references it by path and adds
nothing of its own to how it runs, and the rules of a mechanism —
isolation, wrapping, provenance, what may be read — are written once,
in its own definition. Restating a procedure in a second place is a
defect: the two copies drift, and the copy without a rule silently
loses it. The position was raised by the principal after the README
of the day was rendered at a save by an ad-hoc subagent prompt
instead of `/render` and arrived unwrapped, missing the 72-column
rule, with a foreign provenance shape; the regeneration has been
routed through `/render` explicitly since (POS.1070).

**The operating layer swept for restatements.** The first sweep the
same day found fourteen restatements, every one with a rule missing
on one side, plus three observations — walked through, every verdict
the principal's, all accepted. Twelve commands, two agents and four
templates were aligned: `/check-forge` runs `/check` on the forge
project instead of copying it; `/challenge`, `/critique` and `/save`
cite the walkthrough instead of restating it; `/forge assignment` and
`/check` cite Requirement style; `/new-project` and `/spinoff` hand
the brief to `/forge brief` and the intent to `/forge intent`;
`/render` owns the definition of a stale render; `/save` leaves its
script's behaviour to the script's help. The shared behaviour of the
challenger personas got one owner, `templates/challenger.md`, carried
verbatim by every persona file with only its Lens section its own —
the principal's choice over a runtime include, because a persona file
stands alone like every skeleton and the copy is mechanically
checkable; the template sentence entered CLAUDE.md's reviewers
section. Two shapes that had no owner at all got a skeleton rather
than a second description: the bundle catalogue
(`templates/index-bundle.md`) and the library reduction of the ledger
(`templates/ledger.md`'s header). `/check-forge` carries the standing
rule from now on — a restated procedure, a persona file diverging
from its template, a direct operation where a script, command or
agent exists — scoped to the operating-layer files changed in the
save, the full sweep only on an explicit bare `/check-forge`, so that
the rule costs seconds, not minutes. The first isolated
`/check-forge` the same evening found nine more findings, all
accepted — among them the conversation language hard-coded as Czech
in thirteen commands and a template: POS.0060 now points at
`CLAUDE.local.md`, and the commands say "in the conversation
language".

**Checks in isolation, renders in parallel.** Prompted by a save that
had grown to five minutes, the context lever of one model for the
whole forge is extended to the conformance checks: `/check` and
`/check-forge` execute their own definition in an isolated subagent
that sees only the files, returning the report for the walkthrough in
the session, and a repository's README and release-notes renders are
launched in parallel — since 3.33 by `/release` — so that the working
conversation is spent on verdicts, not on reading (POS.0930
extended).

**The critic split into two lenses.** A user of the forge reported
that the critic hunts formalities and does not guard the drift
between the documents of the chain, and a reading of the agent
confirmed it: its mandate named one link in one word, the brief was
read but given no task, and formal checks filled four paragraphs of
its prompt. On the principal's decision the two reviewers now share
one shape (POS.0400 rewritten): the critic has lenses and produces
FND in `reviews/`, the challenger has personas and produces CHL in
`challenges/`; both are invoked by hand, both reports are immutable
and dated, both are settled by walkthrough, and each agent file
carries its shared behaviour verbatim from one skeleton —
`templates/critic.md` new as the mirror of `templates/challenger.md`
— with only its Lens section its own. The first two lenses, their
names chosen by the principal from several pairs (POS.0410
rewritten): `clarity` reads each artefact on its own — ambiguity,
contradiction, duplication, scope hygiene, Requirement style;
`essence` reads the chain — for every adjacent pair it distils the
downstream artefact's essence blind, then the upstream's, and reports
the difference of essences, not of texts: substance lost without a
trace, added without provenance, shifted in meaning, provenance that
does not hold. `critic-clarity.md` and `critic-essence.md` replace
`critic.md`, `templates/critique.md` is retired with the report shape
living in the skeleton, `/critique` is rewritten as the mirror of
`/challenge` (bare = roster), and `/check-forge` verifies lenses as
it verifies personas. Which of the reviewers run at a save or a
release was left to THR.0220 and settled with it: neither runs on
its own, and `/release` offers `critique essence` once.

**Both reviewers take a target.** At the principal's request
`/critique <lens>` and `/challenge <persona>` accept an optional
artefact named as `/forge` names it — `brief`, `brief-<name>`,
`intent`, `assignment`, later layers — and cover the whole chain
without one. `clarity` reads that artefact alone, `essence` reads it
against its parent (a transition addressed by its downstream
artefact, no arrow typed), a challenger the substance of that
artefact; the challenger's default moves from the intent to the whole
chain, each challenge naming the artefact it concerns (POS.0400,
POS.0410, POS.0420 extended).

**The first clarity critique, and one finding overruled.** The first
run of the `clarity` lens on the forge project returned ten findings,
walked through with every verdict the principal's. Nine were fixed:
among them THR.0220 gained the question which reviewers run at a save
or a release and the fact that a two-speed save already exists in the
principal's practice; the repository is named `forge-of-thought` and
`forge` kept for the project slug in the positions that had blurred
them; POS.0560 was folded into POS.1010, POS.1000 cites the render
positions it rests on, a library's contents are listed once, and the
first principal is called the engine's author, keeping "instance
fact" for `CLAUDE.local.md`. FND.0090 was overruled (DEC.0090): that
the scripts work on any branch while POS.0550 says "main only" is not
a contradiction but the normal relation of a rule to its tool, and
the manual tag at an approved major is a known gap settled in
THR.0220 together with the rest of the git ceremony, not ahead of it
— fixing it now would fix it twice.

**One item per message.** After a drift the principal named — the
interview of THR.0230 opened with six questions at once, and every
following message stacked the reflection of the last answer, a check
and further questions — the Walkthrough was sharpened (POS.0850
extended): Claude puts one item with its recommendation in front of
the principal and stops; the next message acknowledges the verdict in
a line and carries the next item, nothing else; a check of
understanding is an item of its own; an elicitation interview runs
the same way, one question at a time, a questionnaire being the table
of verdicts in another coat.

**A project's documents have a kind.** A new position (POS.1080)
sets out the taxonomy of a project's documents in one table, to be
read the same in the intent, in CLAUDE.md and in the README: five
groups — artefacts, records, state, rendering, resources — and
thirteen kinds, each with its meaning, who writes it, whether it is
versioned and how it behaves. "Document" is now the word for every
file of a project; "artefact" is reserved for the documents of the
chain — brief, intent, assignment and the later layers — which the
principal composes, the reviewers read and the renders are generated
from; the positions that had called an immutable review or source an
artefact now say document (POS.0060, POS.0160, POS.0320, POS.0550,
POS.0980, THR.0210). Records (history, decisions, reviews and
challenges), state (ledger, index), rendering (render) and resources
(source, research) carry no version; the recipe is versioned but
never approved. A functional binary is a source, so a library's
assets need no kind of their own, and a library carries no artefacts
and no records. The assignment is no longer described as "frozen": it
is rewritten freely between approvals like the intent, and what the
recipients hold is a version reached by a link into git — the word
described the handover, not the document. Decided 2026-09-04, when
the question where the Version History lives turned out to hang on
which kinds carry a version at all.

**The Version History leaves the document.** Opened at 3.14 as
THR.0260 — the table measured at 40 % of the intent (8,477 of 21,265
words, 72 rows) and held three times over: the row, the commit
message, the release notes — with a research note on placement whose
split by kind (the table kept in the head of the assignment and the
briefs) the principal rejected as two rules for one thing, the thread
is closed by POS.0310 rewritten: every versioned document keeps its
Version History in an append-only companion `<file>.history.md`
beside it, never in its body — the body is the current state, the
companion the record. One rule without exception: brief, intent,
assignment, every later artefact and the recipe alike. A brief that
arrives finished has one row; a brief born in the forge gains the
history it never had; the recipe, exempted at 1.15, gains one too
because the companion removes the reason for the exemption, a status
it still has none. The document's front-matter carries a
machine-written `last_change:` line summarising the newest row,
written by the same step that appends the row, so the two cannot
drift. The companion's row is the single primary; the commit message
`/save` drafts and the Unreleased head of these notes are derivations
by mechanism — a record rendered twice is not a procedure stated
twice. Every command and isolated agent that loads a document is
spared its history; a reviewer that needs the trajectory reads the
companion. A Version History table in the body of a document is a
`/check` finding, fixed by moving it into the companion — that is how
a project migrates, on the principal's word, project by project, each
saved by its own `/save`; a colleague's project meets the rule at its
next `/check` after `forge-pull`. Row 3.21 was the last written into
the intent itself: the operating layer — CLAUDE.md, the templates,
the `/forge` write steps, `/recipe`, `/save`, `/check`,
`/check-forge`, this recipe — followed, the forge project moved its
history into the companion, and on 2026-09-04 the three local
projects were migrated and saved, each by its own `/save`; these
notes read the log from the companion. Two words tidied in the same
round: POS.0550 states the scripts-only door to git without a count,
the number having gone stale twice, and the research's "11 % of a
brief" was struck as unverifiable, a brief carrying no table.

**The first save with the companion, and its findings.** The
`/check-forge` of the 3.21 save returned findings walked through at
3.22, every verdict the principal's: POS.0110 lists `last_change`
among the brief's header fields, CLAUDE.md aligned; POS.1070 names
the scripts without a count, as POS.0550 already does; THR.0210 no
longer reserves POS.1080, now taken by the taxonomy; this recipe
(0.4) and its template name the companion as the fine-grained log;
and `/check` and `/check-forge` report findings only — the checker's
informal "observation" is forbidden. One line was written into the
locked brief's front-matter on the principal's word — `last_change`,
immutability knowingly broken once for one metadata line, recorded
in the ledger. The same save brought the principal's remark that a
reader learns nothing from what is rendered — taken at first for a
remark about the Version History rows and opened as THR.0280, and
corrected two versions later into the thread on these notes below.

**Stale renders are the principal's business; one shape for every
index.** Two decisions taken during the migration of the three local
projects to the companion, when the checks listed every stale deck
and picture as findings — noise, since a render is regenerated only
on the principal's word. Only the README and the release notes have a
freshness rule, the next `/release` regenerating them; the staleness
of every other render is shown by the `/forge` map and never reported
by `/check` (POS.0570, POS.0810). And the two bundle indexes in the
field turned out to be a table and a prose catalogue of a third
shape, so the bundle index now has the same shape as the directory
index — one entry per file with What / Origin / Role / Use for, the
two bundle indexes rewritten: Role and Use for are what an index is
for, and a table does not carry them. The position is renamed
"Resources have an index" after the taxonomy (POS.0840). The
`/check-forge` walkthrough of the 3.23 save finished the alignment:
POS.0180 now says the same as POS.0840 — one entry per file in the
shape of the directory index, no table — and
`templates/index-bundle.md` is the full skeleton `/ingest` creates
the file from, header and opening paragraph its own, the entry
carried verbatim from `templates/index.md` as a reviewer agent
carries its skeleton, the principal's choice over a pointer-only
skeleton; and `/check` step 8 and `/save` step 2 were brought to
POS.0570 in fact, the 3.23 row having claimed step 8 done already.

**Threads opened for the forge's next shape.** Three further threads
were opened at the principal's direction, no decision taken. THR.0230:
a common engine beneath several frameworks — whatever every framework
needs alike (git through the scripts, the ledger, versioning, the ID
scheme, isolated agents, recipes and renders, resource indexes,
`/save`, `/check`, `/setup`) lifted out of the forge so that a new
framework is written as content only, the forge becoming the first
framework on it; a product framework and a project-management
framework named as the cases that draw the boundary, the agent
boundary drawn (mechanism the engine's, persona and critic content the
framework's), three paths by which the engine reaches a framework
recorded without choice, the second framework to exist in outline
before the engine is built; THR.0220's settlement is read as an
engine matter that carries over. THR.0240: the size of CLAUDE.md, 523
lines and growing, to be dealt with whatever becomes of THR.0230, the
effect measured by behaviour and never by line count. THR.0250: two
functions suggested to the principal, an expander and an essence
manager — the latter's detail gave the `essence` lens its method, the
former has a name only; parked.

**The shared reviewer skeleton as a preloaded skill, opened.**
THR.0270, at the principal's direction. POS.1070 chose at 3.10 the
verbatim copy over a runtime include, because a persona file stands
alone and the copy is mechanically checkable; on 2026-09-03 a fact
changed the weighing — Claude Code agents carry a `skills:` list in
their front-matter, and the whole body of each named
`.claude/skills/<name>/SKILL.md` is injected into the subagent's
system prompt at launch, verified in the documentation the same day:
an include with the behaviour of the copy and one source, seen in use
in a colleague's system that grew out of the forge, where one shared
contract skill carries the conduct, output classes and evidence rules
of every reviewer. Measured: about 100 of 171 lines of a critic lens
file and 90 of 131 of the challenger's are the shared part, the
critic skeleton existing three times and the challenger's twice, with
`/check-forge` comparing the copies at every release. Proposed: the
two skeletons move to `.claude/skills/`, every lens and persona file
keeps its front-matter and Lens section only, and `/check-forge`
replaces the copy comparison with a check that every skill named in
an agent's front-matter exists — a missing skill is skipped silently,
with a warning in the debug log only. Open before a decision: the
order in which skill and agent body land in the prompt, whether a
skeleton skill must be kept out of the main session's skill roster,
and the side fact that every subagent also receives the whole
CLAUDE.md — a cost that belongs to THR.0240.

**The guard rail parked.** THR.0210 — a standing rule that
`projects/forge` never carries the content of a subject project — is
parked at the principal's decision: the risk is small while he knows
of it, and a rule with its checks would add weight the forge does not
need now. The proposed solution is recorded for the day it is taken
up: a check item in `/check-forge` owning the rule, verified by
reading and never by a term list, plus one citing sentence under
Inputs in both reviewer skeletons; not a critic lens, and no sentence
in CLAUDE.md.

**Checks and research as lenses, and a user's private layer,
opened.** Two more threads at the principal's direction at the end of
the migration day, no decision taken. THR.0290: `/check` is today one
long command with eight numbered checks; the idea is to put it — and
`/research` alike — on the reviewer mechanism: one skeleton
(`templates/check.md`), one agent per kind of check (`check-<name>`),
bare `/check` listing the roster and recommending a fit, a named
check run by hand exactly as `/critique clarity` is. A new check is
then one file, written when the need appears. Since 3.33 the thread
owes two kinds to the two doors: a full check with sub-checks, which
`/release` runs, and a light check for `/save` — ledger bookkeeping,
version and status agreement, the companion row — which `/save` runs
without until it exists; the question which checks run at a save or a
release is thereby answered for the reviewers and the first two
kinds. Open: what the further kinds are — the public boundary of
THR.0210 among them — what `/research` gains from kinds, and whether
`/check-forge` survives as a kind or as a target; the order is fixed,
the THR.0270 trial first, then the kinds, so that no kind is built on
a skeleton about to change. THR.0300: whoever runs the forge may want
reviewers, checks or other agents of their own, for themselves only,
with no ambition of contributing them to the engine. They would need
a place the engine does not know and `forge-pull` never overwrites,
on the pattern of `CLAUDE.local.md` and `settings.local.json`, and
the rosters of `/critique`, `/challenge` and `/check` would list what
lies there beside the engine's own. Open: how a local agent takes the
shared skeleton, what happens when the engine renames or reshapes it,
and whether Claude Code's own user-level agents already serve.
Offered as possibly interesting, no priority.

**These notes must get better.** The principal's verdict of
2026-09-04: as rendered today the release notes are a story, and a
reader wants to see plainly what was added, what changed and what
disappeared. THR.0310 opens the question with no position on the
shape — a changelog format is not to be decided by fiat; a research
round on how release notes are done well comes first, then the
position, then the recipe (POS.0730, this recipe, the genre skeleton
and its `/recipe` file). THR.0280, opened earlier the same day as
"what a Version History row must say", was a misreading of the same
remark — the principal was speaking of the release notes throughout
— and is withdrawn into THR.0310; the ID stays used, its text gone.
Whether the row a release note is generated from must change too is
for the research to show.

**A foreign agent worn as a critic lens.** On 2026-09-05 the
principal, browsing the official plugin marketplace, installed
`plugin-dev` and had its `skill-reviewer` run isolated over the
operating layer `.claude/` as an exercise. The report was worth
keeping, so on his word it was recast into the critic's shape —
`reviews/2026-09-05-critique-harness.md`, FND.0190–0280, the lens
name `harness` his choice — rather than lost as conversation; the
run shows the critic's shape fits a foreign agent and is filed as the
first trial under THR.0290. Minutes later THR.0320 was opened at his
direction: the critic roster gets a lens `harness` that reviews the
operating layer — CLAUDE.md and the skills, commands and agents of
`.claude/` — against current Claude Code conventions, its knowledge
from the official plugins (`plugin-dev`, whose `skill-reviewer` and
`skill-development` carry the conventions for skills, commands and
agents; `claude-md-management`, whose `claude-md-improver` reads
CLAUDE.md), its output the classic critic's: a dated immutable report
in `reviews/`, FND in the ledger, settled by walkthrough. Open: how
`/critique harness` reaches the plugin — a mapping in `critique.md`
from the lens to the plugin agent with the skeleton's Output section
carried in the prompt, or an own `critic-harness` agent from the
skeleton with the plugin's skills preloaded, the `skills:` field
THR.0270 waits to verify; the plugin as an engine dependency, named
by `/setup` and CLAUDE.md, and what the lens does when the plugin is
absent; whether `claude-md-improver`'s rubric, written for codebases,
serves a constitution like the forge's CLAUDE.md beyond its
conciseness criterion; and the regression step every lens owes,
which the trial skipped. The first concrete kind of THR.0290; the
shape of the operating layer it reviews is the question of THR.0270
and THR.0240.

**The harness enforces the principal's word.** The harness critique
was walked through the same day, one item per message, every verdict
the principal's; six findings were fixed in the operating layer,
CLAUDE.md unchanged. Both reviewer skeletons and all three agents
carry `Edit` among their tools (FND.0200). Every command that writes,
scaffolds, commits or regenerates — `/save`, `/spinoff`, `/setup`,
`/new-project`, `/import-project`, `/ingest`, `/render` and the six
state and genre files behind `/forge` and `/recipe` — carries
`disable-model-invocation: true` in its front-matter, so that Claude
cannot start it on his own judgement: the principal invokes it by
slash, or asks in words and Claude follows the command's definition
read by path, as the dispatchers do (FND.0210, FND.0190); the state
files name their arguments in words, and each dispatcher says in one
sentence where a state file's arguments begin — the cheap variant,
chosen over relocating the files or the skills layout, both of which
belong to the round of THR.0270 and THR.0240. `/check` names its own
path to its subagent (FND.0240), `/render` carries the provenance
front-matter block in its subagent prompt and lets the subagent read
a previous render only when the recipe declares it among its inputs
(FND.0220; the absolute ban of the first fix was corrected the next
version, since the release-notes genre carries its released sections
over from the previous edition), and `$ARGUMENTS` reaches `/research`
and `/save` (FND.0230). Maps, reports and rosters — `/forge`,
`/ledger`, `/check`, `/check-forge`, `/critique`, `/challenge`,
`/research`, `/recipe` — stay model-invocable, since Claude is meant
to propose them. The guarantee of Step by step thereby rests on the
harness as well as on CLAUDE.md, and the descriptions of the guarded
commands leave the always-on context (POS.1090). FND.0250–0280 are
left open for the round of THR.0270 and THR.0240, where the layout of
the operating layer is decided once.

**The brief header gets an owner; the check of the harness save
settled.** The `/check-forge` of the 3.30 save returned findings
walked through at 3.31, every verdict the principal's.
`templates/brief.md` was created as the one owner of the brief's
header, cited by `/forge brief`, `/new-project` and CLAUDE.md in
place of three restatements — the rule of POS.1070 applied to a shape
that had lived in three copies. THR.0220 stated DEC.0090 beside the
fact it ruled on, so that the branch-aware scripts and POS.0550's
"main only" no longer read as a contradiction left standing. This
recipe (0.5) requires the intent's current vocabulary even where an
older history row uses a word since renamed, after "material index"
had resurfaced in the previous edition of this head. The write-once
sentence was dropped from the presentation and readme genre files,
and a stale ledger item on the renders was removed.

**The check comes before the render.** At 3.32 the save was
reordered at the principal's direction: the conformance check and
its walkthrough run first, the README and release-notes renders
after, from the settled sources (POS.0570, POS.1000). The order of
1.22 — render before check, so that `/check-forge` could verify the
render — had become a trap once the walkthrough entered the save: a
finding bumps the intent, and the freshly made render is stale again;
the saves of 2026-09-04 and 2026-09-05 both fell into it. A render
made from settled sources is current by construction, and a false
claim in it is a recipe defect, so `/check-forge` no longer checks
the README's currency; `/render` verifies its own output in its last
step. One version later the whole sequence — check, walkthrough,
renders — moved from `/save` into `/release`, where it now lives in
that order.

## 3.0 — 2026-08-30

Version 2 made the forge a workshop; version 3 sets it free. The
engine parted ways with the projects it serves and became a public
repository under an open licence, carrying no instance facts and no
content of anyone's projects, while each project lives in a
repository of its own. On the way the brief was redefined and born in
the forge for the first time, the whole forge settled on one model
with renders in isolation, the working methods got names, material
got an index and projects got a kind.

**The engine and the projects part ways.** The course set early in the
era — a public engine carrying no company-specific data, each user
responsible for their own project repositories — became a mechanism
and was then executed. The engine is a clone; the projects are nested
git repositories in a gitignored `projects/*`, with `projects/forge`
re-included. The engine does not know the projects: the scripts
recognise one by the presence of its `.git`, commit and push to its
own origin, and skip a directory without one; `git init` and the
remote are the user's one-off act; the engine is upgraded by
`forge-pull`, carries a git tag per approved major, and stamps no
engine version into projects. Submodules, subtree, a template
repository, copying the engine into projects and a plugin-only shape
were rejected on the research of the day — they model a dependency
this relation is not, or end in manifests, override layers and
migrations. A plugin remains a possible later distribution layer, its
cost (a `CLAUDE.md` split, commands rewritten to the repository root)
not worth paying yet (THR.0190). On 2026-08-30 the split was run to
its end along a runbook: the engine is public at a repository of its
own with a fresh one-commit history, the subject projects and the
library live in repositories of their own, and the former monorepo is
archived read-only with a notice naming the new homes and a
`pre-split` tag as its last complete state. The operating layer —
`CLAUDE.md`, `.gitignore`, the scripts, templates and commands — was
rebuilt to this intent the same day.

**No instance facts in the engine; identity per repository.** Who the
principal is and what language the conversation runs in move to a
gitignored `CLAUDE.local.md` at the engine root, the session model to
`.claude/settings.local.json`, the commit author to the user's git
configuration; the core names these things only as things that exist,
never by value, and the scripts carry no URL or identity. The commit
identity is set per repository, locally, as part of the one-off act
that creates it — never inherited from the global configuration by
default, since one machine serves hosts with different identities; a
repository whose identity is missing is reported by `forge-save` with
the command to set it, and nothing is committed until it is. `local/`
is dropped: it existed only to keep company material out of the
repository, which the gitignored `projects/*` now does, and deck
templates are named by path instead. The output language was
recognised on the way as an instance rule: English for every artefact
is the principal's own rule for the projects of this instance, a
project with Czech output is conceivable and the first such project
has been noted, and more than one output language is to be solved when
a project needs it (THR.0180).

**Publication and the public face.** The engine is the principal's to
publish, built outside any work assignment and on the company's git
only because it carried work information not yet separated. The
audience, in order: rollout in the company, at the same time a public
project around which a community may form, and a showcase of the
principal's work; the split also lets access be granted per project.
The boundary for the public forge project is nothing company-specific
by name, and before publication the project was gone through and
rewritten within it, immutable artefacts included — the locked brief
and both CTO challenges had a name, a host, an address, a template
file name and two sentences quoting a subject project's substance
removed, immutability knowingly broken once and recorded in the
ledger only. The slugs of the subject projects stay: that projects of
those names exist and travelled the chain is a process fact, not
content. A forbidden-term list was considered and dropped — a grep
catches names, not content. The public engine starts with a fresh git
history rather than one filtered by path (DEC.0080): the company lives
in the text — commit messages, every version of the forge intent, a
challenge, the research notes — so a filtered history would need text
filtering as well, work comparable to a fresh start with a residual
risk of a leak made public for good; "history lives in git" is not
voided but starts on the day of publication. The one true point of
the challenge, that the only complete record lives on the employer's
server, is accepted as it is, the company copy kept read-only while it
exists. The public face itself is settled (POS.0990): the repository
is named `forge-of-thought` — the bare word "forge" is overloaded on
every code host — under the licence CC BY 4.0, anyone free to use and
adapt the engine with credit to the author and a link to the
repository; the README names the author with a contact address as a
fixed text of its recipe, which is not an instance fact but who the
work is by, whoever runs an instance; the `LICENSE` file carries the
verbatim legal code.

**A guard rail for the boundary.** The rewrite before publication
found the leak surface where the challenge predicted it: the forge
project's own artefacts quoting the substance of subject projects — a
sentence of a subject intent in a CTO challenge, a deck's name in a
position. Wanted is a standing rule that `projects/forge` never
carries the content of a subject project, only process facts — that a
project exists, its versions, dates and counts — and a home for it in
`CLAUDE.md`, the reviewer prompts, `/check-forge` as a sweep, or all
three. Opened at approval for the next iteration (THR.0210).

**Projects have a kind.** A project is a `thought` — a chain from brief
to assignment — or a `library`: only `sources/` with its index, a
ledger and `research/`, prefix `lib-`, its own repository and therefore
its own visibility, a collection of documents used across projects
whose owner is also their author and may overwrite or version beside.
Nothing is redefined for it — `/ingest`, registration and the index
work as everywhere — and a citation of a library from another project
is a knowingly unguarded cross-repository dependency. A bare `/ingest`
sweep now reports changed sources with a question universally: a
breach in a thought project, the normal case in a library.

**Briefs redefined, and the first brief born in the forge.** A brief
is an intent that is composed and then locked: draft while written,
approved at the lock, immutable from the lock rather than from the
file's creation. Three origins are equally legitimate — it arrives
finished, is begun outside and finished with the forge, or is born in
the forge from the first word — with `/forge brief` as the door: the
principal moderates and says what is explored, Claude clarifies where
he is terse without adding content of its own and keeps asking
whether what exists already solves it, reaching for `/research` and
`/ingest` at his timing. Free-form means no *required* structure, not
no structure — headings, tables and use cases are legitimate, a brief
holds thoughts to be processed rather than decisions, changeable until
mined, and a summary ordered into a brief is stored as shown, never
re-narrated as prose. A project may carry more than one brief
(`00-brief-<name>.md`), each the birthplace of one whole of thinking
that would otherwise enter the intent as a batch of unproven
positions; the ledger's Briefs table tracks how far each has been
mined, and a whole that dies leaves its brief locked and one rejected
direction. Branch documents proper were considered and deferred as
heavy (THR.0170); the long-open thread on additional briefs closed.
`00-brief-public-engine.md` was the first brief composed inside the
forge, with three research notes on engine distribution beside it,
and the first brief challenged: seven CTO challenges before the lock,
six accepted into it, the seventh rejected in its remedy and accepted
in its risk (DEC.0080). Locked at 1.0 and mined at the principal's
direction, every verdict his — the whole cycle brief → challenge →
lock → mine run end to end for the first time.

**One model for the whole forge, and renders in isolation.** Every
command, state and reviewer runs on the session model, both agents
saying so explicitly (`model: inherit`); the `opus` pin on the CTO
challenger, set when opus was the strongest model, had silently come
to mean a weaker reviewer than the author, and reviewers may no longer
pin a model. Per-command pinning to a faster model was rejected:
routine commands are a small share of the work, their slowness comes
from carrying the whole conversation as context, and the pins would
add a convention to keep. The lever adopted instead is context:
`/render` generates in an isolated subagent that sees only the recipe
and its inputs — faster and cheaper on any model, the gain landing in
`/save`'s re-renders. A per-recipe model choice was tested and
deferred: a smaller model loosened pinned wording, dropped prescribed
elements and leaned on the previous render instead of the recipe —
the drift the delta-reporting position exists to prevent.

**Working methods named.** The ways a working conversation runs now
have names, so that commands and the README can refer to them and the
principal can invoke one in a word: Walkthrough, Propose never decide,
Elicitation interview, Draft early, Reflect back, Intent-first,
Recommend do not push. The Walkthrough is the one new position — any
list needing the principal's decision is worked one item at a time,
Claude's recommendation and reason first, "leave it open" a
legitimate verdict, everything written once at the round's end;
whatever produces a list ends by offering one. `/resolve` was retired
without alias, a per-verdict door never used.

**Material has an index.** Every `sources/` and `research/` directory
carries a freely rewritten `00-INDEX.md` — what a material is, where
it came from, its role, when to consult it — so that material need
not be re-read to be known about. The index tracks nothing and is no
automatic input of any command: a contradiction between the intent
and a material is not a finding. Bundles keep their own index and
appear as one entry above — two levels, never deeper. The ledger was
reduced to registration, and `/ingest`, `/research`, `/check` and
`/new-project` write, verify and scaffold the indexes.

**Decks become real PowerPoints; recipes composed by genre.**
`scripts/md2pptx.ps1` turns a Markdown deck render into a `.pptx`
through headless Claude Code with the official pptx skill — an LLM
conversion by design, deck definitions being free-form and carrying
instructions for the model; the generated file lands beside its
source render, tracked like any render output. `/recipe <genre>`
mirrors the `/forge` star: a guided interview composes a render
recipe from the genre's elicitation checklist and skeleton, the first
genre `presentation`. A render may cite another render as an input,
with provenance and staleness tracked.

**The README rebuilt as an onboarding pitch.** A bootstrap Quickstart,
a masthead leading with the forge's identity as an AI cognitive
extension of the principal, a challenge-headed opening section over
the failure modes the forge removes, a "What you get" list, sections
regrouped story → concepts → reference, a Working methods section so
that newcomers learn how the work feels, and at the end an
author-and-licence section. The forge dictates only the output
language; the conversation language is per-instance configuration
that never appears in outward-facing renders. Until a public exemplar
project exists the README carries a one-sentence placeholder.

**The forge runs beyond Windows.** `scripts/` is the only
platform-bound layer, kept in cross-platform PowerShell 7 with
nothing Windows-only, usage examples included, verified by a run on
Linux; the instance facts once hard-coded in the scripts left them
under the positions above. Replacing the set with POSIX `sh` under
Git Bash is still being weighed (THR.0150); a dual set and a Python
rewrite are excluded.

**Housekeeping of the door and the boundary.** A third script,
`forge-status.ps1`, reads repository state without changing anything,
so the scripts are the only door to git, reading included. The
enumerated ban on delivery-stage apparatus fell: what keeps an
assignment an assignment is the kind of content — it assigns, it does
not solve. These release notes gained an Unreleased head, regenerated
by every save that touches the core and recast as the new major's
section at approval — as here.

**The forge turned its reviewers on itself.** Two critique rounds of
the forge project, seven of eight findings fixed and one left open by
decision; the first CTO challenge of the forge intent returned six,
four accepted and two rejected with recorded reasons (DEC.0060,
DEC.0070). The round produced the scope positions: the forge is a
general tool for forging thoughts and ends where its owner is
satisfied, delivery deliberately outside its sight; reviewer isolation
is not independence, with independent challengers on a different
model family planned; regenerated renders pass under the principal's
eyes; and artefacts do not expire with the conventions they were
written to.

**Open by design:** THR.0090 (genuine multi-principal operation beyond
one instance per person via git), THR.0140 (whether the forge's output
one day feeds a delivery chain as grown layers or hands over to a
separate framework), THR.0150 (replacing the PowerShell scripts whole
with POSIX `sh`), THR.0170 (branch documents as a per-whole working
space before the merge), THR.0180 (more than one output language,
opened by the first project with Czech output), THR.0190 (a plugin as
a later distribution layer, taken up when `forge-pull` proves an
insufficient upgrade channel), THR.0200 (an exemplar project for the
README), THR.0210 (a standing guard rail so that `projects/forge`
never carries the content of a subject project).

## 2.0 — 2026-08-15

Version 1 was an engine that turned briefs into assignments. Version 2
is a workshop: the chain is worked by naming the state you want, what
the chain produces is communicated by generated renders rather than
hand-kept documents, and the adversarial pressure on the thinking has
grown teeth. The guiding aesthetic also shifted: an assignment is no
longer prized for being short, but for being complete and precise.

**The chain is worked by target state.** `/clarify` and `/draft` were
retired in favour of `/forge`: bare, it maps the project's state;
with a target (`/forge intent`, `/forge assignment`) it iterates that
artefact. Each state declares its own inputs in its own definition
file, so the chain can grow new layers — or branch — without new
conventions.

**Renders became a first-class concept.** Audience-specific outputs —
a pitch, an architecture picture, the repository README — are
generated from versioned recipes (`recipes/<recipe>.md`: inputs,
audience, instructions, template) by `/render <recipe>`, carry
provenance front-matter, and are never edited by hand: a recipe fixes
structure, never wording, and each rendering re-derives the words from
the current inputs. The README is itself a render and is regenerated
automatically by every `/save` that touches the core, so it can no
longer go stale. This file is a render too.

**The challenger grew into a panel.** `/challenge <persona>` selects a
lens — one isolated agent per persona, `cto` first — and may target
any chain artefact, best before the next layer is first derived from
it. Calibration was hardened from the principal's own pre-forge
challenger prompt: severity grading (dealbreaker | major | minor), a
wider epistemic scale, and an anti-fabrication discipline under which
a precise "I don't know" beats an invented figure.

**Sources serve, tooling converts.** `/ingest` was reduced to pure
registration — store, catalogue, nothing more; how and when a source
is used is the principal's call alone. Related files live as bundles
with a `00-INDEX.md` catalogue, and every text extract of a binary
source is produced by `scripts/doc2md.ps1` (markitdown) — ad-hoc
parsing is banned.

**Saving became a procedure.** The forge lives in a GitLab-backed
repository driven by `forge-save` / `forge-pull`; `/save` is the
recommended door: re-render the README, run the scope-routed
conformance check, settle findings with the principal, confirm the
commit message, then push. Advisory throughout — nothing blocks the
principal. Protection settled on Claude Code's permission system
after OS-level sandboxing proved unavailable on Windows.

**From short to complete.** The founding "short and airy" paradigm
was dropped in two steps: first the fixed page target (length is
never the defect), then the paradigm itself — an assignment now
carries the complete in-scope substance of the intent, as precisely
as it can be written; a silent omission is a defect, and leaving a
matter out is legitimate only as an explicit delegation. What keeps
an assignment an assignment is the kind of content, never the amount.

**Open by design:** THR.0090 (multi-principal use), THR.0110
(additional briefs during a project's life), THR.0120 (final form of
the delivery-stage exclusion under the completeness paradigm).

## 1.0 — 2026-08-02

The founding baseline. A fixed chain of versioned documents — verbatim
brief, working intent, distilled assignment — with decisions and a
ledger beside it; two independent reviewers blind to the working
conversation (document critic and substance challenger); stable global
IDs aligned with the group BRD standard; conversation in Czech,
artefacts in English; write once per iteration round; conformance
commands (`/check`, `/check-forge`) advisory and read-only. Version 1
deliberately ended at the assignment, with the growth path toward BRD
and solution architecture declared but not built.
