---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 879725c48b575464
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs-state.py
  - scripts/docs-check.py
  - templates/recipe-readme.md#Pinned facts (not rendered)
  - projects/forge/10-intent.md#POS.1450
---

# Change a documentation page

A documentation page is a generated file: the command `/document`
writes it from the files that own its matter, and the next run writes
it again. This page is for you, the extender, when a page says
something wrong or too little, when the shape of every page should
change, when pages should appear or disappear, or when the check
refuses a page. It shows where such a change is made so that the next
run keeps it instead of undoing it.

## When to use it

Use this page whenever you want the documentation to read differently
and are tempted to open a page under `docs/` and type into it. Do not.
A page is never edited by hand. Because the next run of `/document`
writes it again from its owners, a mend typed into the page is gone
at that run. Only a mend in the file that owns the matter survives,
and the page takes it at the next run. The run itself never touches a
page by hand either: what is wrong on a page is mended in the owning
file, and the page is regenerated.

The same holds for the map the pages are made from, `docs-map.md`
beside the owning project's ledger (the ledger is the project's state,
made from its documents by a script): the map is written anew by the
planner at every run, so a change typed into it is gone as well.

## What you do

### Find the owner

Every page opens with a front-matter. Its `inputs` list names every
file the page was made from, or the part of a file, written after
`#`: a section by its heading, or an item by its ID. Its `made` field
says whether the page mirrors those inputs or is derived from them.
The fields of the front-matter and of a page's entry in the map are
on the page [Documentation map](../reference/documentation-map.md).
The entry adds what the page is to say (`says`), the reasoning of a
derived page (`evidence`), the pages it may link (`links`) and what
it must not say (`must-not`). For the engine the map is
`projects/forge/docs-map.md` and the pages lie in `docs/` at the
engine root; for a project the map is `projects/<slug>/docs-map.md`
and the pages lie in `projects/<slug>/docs/`.

Where a change lands depends on what you want to change:

| What you want to change | Where the change is made |
|---|---|
| what one page says | the file the page's front-matter lists under `inputs` that owns the matter |
| a fact no file owns | the section `## Pinned facts (not rendered)` of the owning project's readme recipe, whose skeleton is `templates/recipe-readme.md` |
| the shape every page has, the outline of each kind | `.claude/agents/docs-writer.md` |
| what kind of content a page of each kind carries, the voice, the sentence, what must never reach a page | `.claude/skills/docs-contract/SKILL.md` |
| which pages exist, the sections, who reads them | the material of the target, and the planner's definition `.claude/agents/docs-planner.md` |
| what the check refuses | `scripts/docs-check.py` |

### To change what a page says

Mend the owning file and run `/document` for the engine, or
`/document <slug>` for a project. How the command is run is on the
page [Generate the documentation](../use/generate-the-documentation.md).
The run remakes only the pages whose inputs, entry or generating rule
changed. The state is computed, never judged: a page whose inputs did
not change is not regenerated, so a mend in one file reaches exactly
the pages that name that file, or that part of it, as an input.

A fact a page needs and no file owns is not typed into the page and
not invented by the run. The planner lists such a fact under
`## Unowned` in the map, with the page that needs it, and the writer
leaves it out. The home for it is the section
`## Pinned facts (not rendered)` of the project's readme recipe: one
bullet per fact. The README does not print that section. The
planner reads it as an owner. A bullet is dropped the day a file of
the project owns the fact.

### To change the shape of every page or what a kind carries

The writer's definition `.claude/agents/docs-writer.md` owns the
shape of a page and the outline of each kind. The documentation
contract `.claude/skills/docs-contract/SKILL.md` owns the kinds of a
page, the voice, the sentence and what must never reach a page. Both
are hashed with the inputs of every entry, as the generator of the
pages, with their whitespace normalised. So a change of a sentence in
either file regenerates every page made by the old rule. A re-wrap
of either file regenerates nothing. The planner's definition is not
hashed: its rules reach the pages through the entries it writes.

Claude Code, the harness in which Claude runs, loads an agent's
definition once per session (one conversation from its start to its
end). A change to `docs-writer.md` or `docs-planner.md` reaches the
agents only in a new session. If the run goes in the session that
changed one of them, it passes the changed rule to the agents in
their tasks and says so in its report. Start a new session before
the run when you want the change read from the file itself.

### To change which pages exist or who reads them

The map is not edited: the planner, a subagent (an agent that runs
apart from the conversation and reads everything from disk), writes
it from the target at every run. Which pages exist follows from the
material of the target and from the outline. A page appears when the
target has material for it: for the user, one page per job the thing
has a command or a procedure for; for the extender, one page per kind
of addition; one page per concept and per kind of artefact or part.
A page whose material is gone is marked `remove` by the planner and
deleted by the run. The readers, three in a fixed order, and the five
sections of the outline are set in the planner's definition and in a
position of the forge intent, `projects/forge/10-intent.md`, the
intent of the forge's own project. A change there is a change of the
forge like any other.

The planner keeps the path of every page that still has material, so
that page names stay stable across runs. It also receives the open
findings of the last documentation report that concern the map, so
that it brings those entries to their owners' wording instead of
carrying the old wording over.

### What the check refuses

The check `scripts/docs-check.py` verifies the pages against the map
and against the rules of a page, and prints every failure with its
file and line. It refuses:

- a map entry not in state `remove` without its page, and a page
  under the docs directory that the map does not name (the index
  `README.md` excepted);
- a relative link to a `.md` file that does not resolve;
- a long dash (em or en) in the prose of any page; a code span and a
  fenced block are exempt, since a literal is copied as its owner
  has it;
- a page that does not open with a front-matter;
- an instance fact: the values of `CLAUDE.local.md` at the engine
  root (every word of four letters or more in a value, looked for
  outside URLs), any e-mail address but a placeholder at `example.*`,
  any absolute path of a machine (a drive letter, a user's home
  directory), and every pattern given with `--fact`.

Exit code 0 means everything holds, 1 that something failed. The
check mends nothing. In a run, a page that fails is regenerated once
with the failure named in its task. A page that fails twice is
reported and left out of the documentation: deleted, its entry marked
`remove` in the map by hand, said aloud. It is never mended by hand.

The check carries no name, address or host of its own: the instance
facts it looks for are read from `CLAUDE.local.md` at run time. A
match is reported with its line. So a false hit, a common word that
happens to be a value, is seen, and the rule is adjusted, not the
page. Which addresses a page may carry is said by the entry's
`must-not`, which the planner writes. The check can be run alone,
from the engine root:

```
python scripts/docs-check.py projects/forge/docs-map.md docs
python scripts/docs-check.py projects/<slug>/docs-map.md projects/<slug>/docs
```

## What happens

After the mend in the owning file, one run of `/document` goes
through these steps; it asks nothing on the way.

1. The planner reads the target on disk and writes the map anew,
   taking the previous map as last committed to keep the page paths.
   You should now see the planner's counts of pages per section, its
   Unowned list and what did not fit.
2. The state script hashes every entry, its `state` line excepted,
   together with the content of its inputs and the generator, and
   compares the result with the `inputs-hash` the page at that path
   carries: `new` where no page exists, `regenerate` where the hash
   differs, `keep` where it is the same; a page no entry names is
   listed `remove`. You should now see the summary of states, with
   the page you mended for listed as `regenerate`.
3. The pages listed `remove` are deleted, and one writer per `new` or
   `regenerate` page makes its page from its task file alone, reading
   its inputs from disk. You should now see the number of pages said
   before the writers are launched, and then the writers' reports of
   what their inputs did not support.
4. The index is derived from the map, the check runs over the pages,
   the owning project's ledger is remade, and the run reports. You
   should now see the pages new, regenerated, kept and removed, and
   the check's result.

What the run could not place is filed as the run's own report: the
Unowned list and what did not fit, from the planner; a claim the map
asked for and no input carried, from the writers; and every place
where a writer wanted a reason and none is recorded, which the page
says is not recorded. The report is a check's report in `reviews/`,
named `YYYY-MM-DD-check-documentation.md` and completed by
`scripts/forge-report.py`, with one finding per matter: an unowned
fact and a disagreement of map and owner as medium, an unrecorded
reason as low. The ledger reads it as any check's report. The
findings are settled by walkthrough (the forge's way of putting
findings to the principal, the person whose thinking is forged, one
by one for a verdict), as the page
[Check conformance](../use/check-conformance.md) describes. A mend
lands in the owner, never on a page. A run that leaves nothing files
nothing.

## What you have afterwards

- The owning file changed, and every page that names it as an input
  written again, with today's date in `generated` and a new
  `inputs-hash`. Every other page as it was.
- The map with its `state` lines set by the script, the rest of it as
  the planner wrote it.
- Where the run could not place something, a report in `reviews/`
  whose findings wait for a walkthrough; the mend of each lands in an
  owner, and the next run takes it.
- A change of the forge like any other: the owning file is recorded
  and released as the page
  [Make a change to the forge](how-a-change-is-made.md) says.

## If something goes wrong

- The run is refused. `/document` runs on `main` only and refuses a
  repository behind or diverged from its origin.
- Your mend did not reach the page. Open the page's front-matter: if
  the file you changed is not among its `inputs`, the matter has
  another owner, or the page is derived from other evidence named in
  its entry. If you changed only the line breaks of the writer's
  definition or of the contract, nothing is regenerated, as intended.
  If you changed an agent's definition in the running session, the
  file itself is read in a new session.
- An input the map names and the disk does not have, a file or a
  part, is reported by the state script and hashed as missing; the
  page is regenerated and its writer reports the gap.
- A page fails the check. It is regenerated once with the failure
  named in its task; a page that fails twice is reported and left out,
  its entry marked `remove` by hand and said aloud. The mend is made
  in the owner that put the failing matter on the page, or in the
  check's rule where the hit is false.
- A page is regenerated and still lacks what you wanted. The writer
  leaves out what its inputs do not support and reports it; the fact
  needs an owner, and the readme recipe's pinned facts are the home
  for one that has none.

## A worked example

Suppose this page should say what the exit code of the check means,
and suppose the help header of `scripts/docs-check.py` did not say it
yet. The fix is traced from the page back to its owner and forward
to the next run.

1. You open the front-matter of
   `docs/extend/change-a-documentation-page.md`. Under `inputs` it
   lists `scripts/docs-check.py`: the help header of the check script
   owns what the check does. The page is `made: derived`, and its
   entry in `projects/forge/docs-map.md` names the script's docstring
   as the evidence for what the check looks for.
2. You do not type the sentence into the page. You add it to the
   header of `scripts/docs-check.py`, in the part that says what the
   script does.
3. In a new session, on `main`, you run `/document`. The planner
   writes the map anew and keeps this page's path. The state script
   hashes this page's entry with its inputs: the script's text
   changed, so the hash differs from the one in the front-matter and
   the page is `regenerate`. Every other page whose entry names
   `scripts/docs-check.py` is `regenerate` as well. Every page that
   does not name it is `keep`.
4. One writer per regenerated page reads its inputs from disk and
   writes the page with the new hash. The index is derived, the check
   runs and passes, the ledger is remade. The report says how many
   pages were regenerated and that the rest were kept; nothing is
   filed, since the run placed everything.
5. The change to `scripts/docs-check.py` is recorded and released as
   any change of the forge, as the page
   [Make a change to the forge](how-a-change-is-made.md) says.

Had you typed the sentence into the page instead, the next run that
wrote the page would have taken it from the header again, and the
sentence would be gone.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
- [Check conformance](../use/check-conformance.md): how a report's findings are settled by walkthrough.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
