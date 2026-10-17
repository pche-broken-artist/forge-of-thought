origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of Claude's proposal for the solution design pass over the brief `collaboration` (the proposal of 2026-10-17, solution design 0.17 to 0.18); translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the solution design pass over the brief `collaboration`

The shape of the pass is right: unbuilt parts as a specification
with "Not built; the N-th release" is the one choice under which the
builder has something to read; TBC.0030 is the model for a mechanism
nobody has designed yet, not for one designed and not built. The
four releases agree with the brief part by part. What I would fix
before the write of 0.18:

## 1. The names of reports: the first report of a day on two branches collides (a fix for the intent too)

E, POS.1720 and SOL.0810 give the suffix of time and hash only to the
second report of the day, "instead of `-2`". But two branches each
make their first report that day, both `2026-10-16-check-light.md`,
with different content, and at the merge that is a conflict "added
on both sides". Since `/save` runs the light check on every branch,
it is a certain conflict in way 4 on every day two people save. The
value "two branches do not make the same name" therefore does not
hold. The fix: every report carries the suffix HHMM and four hex
characters, the first too; the legibility of the name suffers a
little, and there is no other uniqueness across branches without
knowing the other branch. Existing names stay (immutable). It is a
change of POS.1720, not only of the design.

## 2. SOL.0680: what the script reads

The list of eight kinds has neither the threads (Waiting is empty
without them) nor `project.md` (the ledger header's kind, language).
It reads, then: the project file, the artefacts' headers, the
histories, the decisions, the indexes, reviews and challenges, the
provenance of recipes and renders, the published companions, the
work specifications, the threads, the archive. Eleven, not eight;
the count does not matter, the threads do.

## 3. CLAUDE.md and the documentation are missing from "Where"

The brief's "Where it lands" named the sections of CLAUDE.md
explicitly (Ledger, Versioning & status, Persistence, Document
kinds, the ID table with the THR row). In the design CLAUDE.md
appears only in 0670, 0710 and 0790. It belongs also in 0680
(Ledger: "single source of truth, freely rewritten, keep it current
after every operation" ceases to hold), 0700 and 0760 (Versioning:
the header fields, `landed`, `+`), 0720 (the THR row "lives in
threads.md"), 0730 and 0740 (Persistence). And the documentation:
the pages are renders, but the map is authored;
about/persistence-in-git, reference/ledger,
reference/document-kinds, about/versioning-and-history,
use/work-on-a-branch, use/save-your-work, use/pull-from-the-remote
get regenerated, and the driver, the migration and the branches need
new entries of the map. One sentence in 0460 or in 0530 (the run of
`/document` as part of the release), so that it does not fall out.

## 4. SOL.0690: the shape of a verdict in a DEC

The script derives rejected | parked | obsolete from the decisions,
so a DEC must carry a fixed shape ("FND.NNNN parked until <x>"), or
it does not parse. `templates/decisions.md` is missing from the
Where of 0690.

## 5. Smaller

- SOL.0770, the engine's second root: the gitignored instance files
  (`CLAUDE.local.md`, `tmp/`) are not in a worktree; without
  `CLAUDE.local.md` the second window knows neither the principal
  nor the conversation language. `forge-branch --worktree` copies
  them; say so.
- SOL.0710, Where: the 72-column rule is carried also by
  `.claude/skills/render/SKILL.md` and
  `templates/recipe-screenplay.md` (verified by grep earlier), not
  only by CLAUDE.md.
- SOL.0740, Choice: "the engine's scripts have the same path for
  every clone on one machine" does not hold, two clones have two
  paths; correctly "one registration per machine points at the
  primary clone of the engine, forge-status reports the difference
  of version", which 0750 already says.
- SOL.0720, Where: `/end` saves an unfinished conversation into its
  thread, now into the thread's file; `.claude/skills/end/SKILL.md`
  is missing.
- The provenance `v<base>+N` of a research and a critique: 0400
  covers the renders; the `derived_from` of a research and of a
  critique has no owner among the changes (0300 speaks only of the
  `closed` record).
- A project's README recipe has the ledger as an input today; after
  0680 the input is the script's output. One sentence in
  `templates/recipe-readme.md` or in 0400.
- "Not built" and drift: the forge's own FND.1440 says nobody keeps
  the design true against what realises it. For unbuilt parts it is
  doubly so: let `/release` walk in its walkthrough the parts marked
  "Not built; the N-th release" for the N being released and turn
  them over, else it stays written there after the building. It
  belongs in 0530.
