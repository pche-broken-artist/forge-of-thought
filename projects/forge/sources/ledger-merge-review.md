origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge, from a read-only look at the repository at v5.9; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Why the ledger merges badly, and what to do about it

I looked into the repository (v5.9, `projects/forge/ledger.md`, 464
lines, `templates/ledger.md`, `docs/about/persistence-in-git.md`).
The problem is not so much git as the shape of the file.
Concretely:

**Why it merges badly**

1. `updated: 2026-10-16` in the header changes at every operation.
   Two branches always change it, so a conflict is guaranteed even
   when the tables were not touched.
2. The `Note` cells are paragraphs on one line (sometimes 400+
   characters). Git merges line by line, so any change of a line on
   both sides is a conflict of the whole line, and the merge tool
   does not show you which word differs. The forge's own rule "the
   ledger cites and never copies" is not kept here in practice.
3. The Findings and Challenges tables grow at the end. Two people
   add a row at the same place, git sees two hunks at the same
   position, conflict (the classic "adjacent append"). The same
   holds for `threads.md`, `decisions.md` and `*.history.md`; they
   are append-only onto the same tail.
4. "Ledger is freely rewritten" means that Claude may, while
   rewriting, reorder or reword lines that did not change in
   substance. That generates diff noise and false conflicts.
5. The documentation itself admits: "One hole is known and left
   until it happens: two parallel branches taking the same next
   free ID." With two people it happens at once, and the ledger
   then holds two different `FIND.0123`.

**What git has for it**

Git has nothing that understands Markdown tables. It has two things
that help, though:

- `merge=union` in `.gitattributes`: a built-in driver that on a
  conflict takes both sides without markers. For append-only files
  (`decisions.md`, `threads.md`, `*.history.md`) it is nearly the
  right answer. For the ledger it is dangerous: the same line
  changed on both sides ends up as two lines, that is a duplicate
  record, and the order is not deterministic.
- A custom merge driver: `ledger.md merge=forge-ledger` in
  `.gitattributes` and
  `git config merge.forge-ledger.driver "python scripts/forge-merge-ledger.py %O %A %B"`.
  The script receives base, ours and theirs, parses the tables by
  primary key (File, ID, Render, Path), performs a three-way merge
  row by row: a change on one side only is taken, the same change
  on both sides is idempotent, a different change of the same row
  is a conflict on that row only, `updated` = max. It looks like 150
  to 200 lines of Python and fits your doctrine "scripts are the
  only door". The driver is registered per clone (`.git/config`, not
  versioned), so `/setup`, which already writes git config, must
  write it. It applies to rebase too, hence to `/save`. It does not
  apply to a merge through the GitHub web UI.
- `git rerere` on top, so that a conflict resolved once is not
  resolved again at a rebase.

**What is worth changing in the ledger itself** (no architecture,
ten minutes)

- Drop `updated`, or derive it from git
  (`git log -1 --format=%cs -- ledger.md`).
- Shorten the notes to a citation of the ID; the substance belongs
  in the thread or the decision. That is exactly what your rule
  says.
- Stable ordering of rows by key, so that an insert does not
  reshuffle the table.
- Forbid Claude to rewrite a row that did not change in substance
  (in the SKILL.md of `/ledger`).

**A ledger made differently**

If two people on one project are to be the normal case, then a
hand-rewritten single file as the single source of truth is the
wrong primitive, and no merge driver fixes that for good. The
better model is event sourcing: every operation *appends* one line
to `ledger.log.md` (or JSONL), e.g.
`2026-10-16 FIND.0120 resolved assignment=1.3`, and `ledger.md` is
*rendered* from it by a script, the same way the README is rendered
from its recipe. An append-only log with `merge=union` merges
without conflict, provided the events are idempotent and carry a
timestamp (last-write-wins per key). The ledger thereby becomes
what your docs say about renders: "overwritten at every run, never
a source of truth". A large part of the tables is in any case
derivable already today: Renders mirrors the renders' front-matter,
Findings and Challenges arise from `reviews/` and `challenges/`,
Documents from the artefacts' front-matter, Sources from
`sources/00-INDEX.md`. Not derivable are only the state transitions
(resolved/rejected with a DEC), Mined and Waiting on principal, and
those are exactly the log.

That is an intervention into the doctrine "single source of truth",
but it does not really change it, it only moves the truth from the
render into the log.

**ID collisions**: the cheapest is lazy allocation. On a branch an
item receives a provisional ID (`FIND.tmp-<short hash>`), the final
number is assigned by `/release` on `main`, where the sequence is
linear. The alternative is a block of IDs per branch (`forge-branch`
reserves a hundred numbers), but that leads to gaps and is not much
simpler.

What I would do, in this order: the format changes now, the merge
driver as the short-term solution, the log and the rendered ledger
as the direction, if you seriously want multi-user. If you like, I
will write the merge driver as `scripts/forge-merge-ledger.py`
against the current shape of the tables.
