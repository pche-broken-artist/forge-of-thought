---
project: forge
type: research
topic: how concurrent work of several people on structured text files in git is solved elsewhere, for the collision points the forge's own note names (identifiers, append-only logs, shared state files, version numbers, silent collisions, the workflow, a save that meets a conflict)
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1, section "Several people on one project"; research/2026-10-03-what-a-write-touches-and-where-two-authors-collide.md (the inside half of the question, its options A to H)
status: immutable
---

# Concurrent work on structured text in git

## Question

How is concurrent work of several people on structured text files
in git solved elsewhere, for exactly the collision points the
internal note names: an identifier taken without an allocator, an
append-only log and a shared state file that every write touches,
a version number bumped on two branches, collisions git merges in
silence, and a script-driven save that meets a conflict?

The inside half is answered in
`2026-10-03-what-a-write-touches-and-where-two-authors-collide.md`
and is not repeated; its options A to H are tested here against
what the world does.

## How it was read

Surveyed on 2026-10-03, at the projects' own documentation where
it could be reached. Three marks:

- **[V]** wording returned as a quotation from the page itself.
  Pages were read through a fetch tool that condenses them, so a
  [V] quotation is as that tool returned it.
- **[S]** taken from a search summary, a secondary page, or
  general knowledge of a tool not fetched for this note.
- **[Y]** the author's own synthesis.

Status per finding: consensus / emerging / contested. Where a
source was looked for and not found, that is said.

## Answer in one paragraph

The world has no way to keep a sequential, human-chosen number
safe between two branches, and has stopped trying: it either gives
the number at the one place where the branches meet (the pull
request, the editor, the tracking issue), or it stops using a
sequence (a timestamp, a hash, a random suffix), or it keeps the
sequence and adds a guard that turns the silent collision into a
loud one. Shared files that every change appends to are replaced by
one small file per change, compiled at release; `merge=union` is
the documented shortcut and is known to hurt. State that can be
computed from other files is regenerated after a merge, never
merged by hand. Versions are given at release, not at edit. And
no tool that commits on a user's behalf resolves a content
conflict for him: the good ones keep his work safe, say plainly
what happened, and offer one way through. [Y, from the findings
below]

## Key findings

### A. Identifiers without a central allocator

1. **"Highest number in my copy plus one" is the naive scheme, and
   it collides.** [V, adr-tools, `src/adr-new`] The reference tool
   for decision records computes the new number as the highest
   numeric prefix in the local directory plus one. [S, search
   summary of a published ADR validation skill] The failure is
   described as "ADR numbers are chosen at branch time but only
   claimed at merge time, so two in-flight ADR PRs can pick the
   same number and both land", with a case that "went unnoticed
   for a week"; the remedy given there is a guard script that
   reports duplicate numbers before the second merge. [S, npm page
   of log4brains] Another ADR tool lists among its features that
   it needs "no required file numbering schema", to avoid merge
   trouble. This is the forge's scheme and the forge's hole.
   Status: consensus that it fails.
2. **The number is given where the branches meet.** [V, Rust RFCs
   README] "Copy `0000-template.md` to `text/0000-my-feature.md`
   ... Don't assign an RFC number yet; This is going to be the PR
   number and we'll rename the file accordingly". [V, Kubernetes
   enhancements, keps/README] "KEPs are now prefixed with their
   associated tracking issue number. This gives both the KEP a
   unique identifier and provides an easy breadcrumb". [V, PEP 1]
   The author takes "the next available PEP number not used by a
   published or in-PR PEP", and the editors assign the final
   number. In all three the allocator is the hosting platform's
   own counter or a human editor: one place, reached before or at
   the merge. The price: the item has a placeholder until it is
   numbered, the numbers have gaps, and the scheme needs a platform
   or a person in that role. Status: consensus for documents that
   pass through a pull request.
3. **Migrations: three answers to two files with the same number.**
   - Django keeps the number and takes identity from elsewhere.
     [V, Django 6.1, Migrations] "you and another developer have
     both committed a migration to the same app at the same time,
     resulting in two migrations with the same number. Don't
     worry - the numbers are just there for developers' reference,
     Django just cares that each migration has a different name.
     Migrations specify which other migrations they depend on ...
     so it's possible to detect when there's two new migrations
     for the same app that aren't ordered." The tool then offers
     to linearize them. The collision is found because every
     record names its parent.
   - Alembic drops the number. [V, Alembic, Working with Branches]
     Revisions carry a generated identifier and a `down_revision`;
     two revisions with one parent are "a branch", and an upgrade
     then stops with "Multiple head revisions are present"; "An
     Alembic merge is a migration file that joins two or more
     'head' files together."
   - Rails replaced the sequence with time. [V, Rails 8.1 guide]
     The file name "contains a UTC timestamp identifying the
     migration". [S] The change from sequential numbers was made
     for teams working in parallel; the guide as fetched does not
     say so.
   Status: consensus, each within its community.
4. **Requirements tools assume one allocation at a time, or check
   afterwards.** [V, Doorstop, Creation] One YAML file per item;
   `doorstop add` continues the numbering, and a number or a name
   may be given by hand. The page says nothing of two people
   adding at once; a search for Doorstop's handling of parallel
   branches found nothing [S, not found; an allocation server is
   said to exist in the tool, not verified]. [V, StrictDoc user
   guide] The human UID is free in form and optional; beside it
   stands a second identifier, the MID, which "increases the
   portability of requirements data. Even when UID naming
   conventions change or nodes are relocated, the MID continues to
   uniquely identify the original node". [V, Sphinx-Needs,
   configuration] An ID not given by hand is generated from the
   need's type and a hash of its title, with the warning that "The
   user needs to ensure the uniqueness of the given title"; a
   warning type `needs.duplicate_id` exists. [S] That a duplicate
   stops the build in these tools was not verified at source.
   Status: no consensus on allocation; consensus that uniqueness
   is checked by a tool, not trusted.
5. **Identifiers that cannot collide: random or hashed, with a
   short form for people.** [V, Beads, Hash IDs] "Traditional
   sequential IDs (`#1`, `#2`, `#3`) break when: Multiple agents
   create issues simultaneously, Different branches have
   independent numbering, Forks diverge and later merge"; IDs are
   generated from the title, the creation time and a random salt,
   and look like `bd-a1b2`; children are numbered under the
   parent, `bd-a3f8e9.1`. [S, search summary of its release
   notes] The tool began with sequential IDs and left them
   because agents on parallel branches minted the same next
   number. The page also names a cost: an abbreviated ID once
   matched the wrong issue in silence, so one command demands the
   full ID. [V, git-bug, data model] The identifier is a hash of
   the first operation, "displayed truncated to a 7 characters
   string to a human user", and any unambiguous prefix is
   accepted. [V, ULID spec] 26 characters, a time part and 80
   random bits, "Lexicographically sortable". [V, reno, Usage] A
   note's file name is a slug with a random suffix, as in
   `slug-goes-here-95915aaedd3c48d8.yaml`. Status: consensus where
   many writers or agents create records in parallel; the price is
   always the same, an ID that says nothing of order or group and
   is harder to say aloud.
6. **Author prefixes, reserved ranges.** No project was found that
   documents a prefix per author or a range of numbers per author
   for items in git. [S, not found] It is the known technique of
   distributed databases, not of document repositories. An ID
   that carries its author also stops being true when the item
   changes hands. [Y] Status: no precedent found.
7. **A guard file that makes the collision loud.** [V,
   django-linear-migrations] The tool records the name of the
   newest migration in a one-line `max_migration.txt` per app;
   "These files will then cause a merge conflicts in your source
   control tool ... in the case of migrations being developed in
   parallel", and "The first merged migration for an app will
   prevent the second from being merged, without addressing the
   conflict"; a command then renames the later migration and
   repairs its parent. [V, Atlas, migration directory integrity]
   The same idea with a checksum file: without it "no such
   conflict happens because migrations are typically described in
   a separate file for each migration"; with it "two branches that
   each add a migration conflict". The scheme keeps sequential
   numbers and gives up nothing but a conflict at the right
   moment: the second author renumbers before his work lands, when
   nothing yet cites his number. Status: consensus in the
   migration world; no use for document IDs was found.

### B. Append-only logs and changelogs under concurrent appends

8. **One shared changelog does not survive many writers; the
   answer is one file per change.** [V, GitLab, 2018-07-03] "we'd
   constantly see merge conflicts in the changelog when multiple
   merge requests attempted to add an entry to the list." The
   first remedy, empty placeholders with each author picking "a
   random spot in the list", only delayed the conflicts. The
   remedy kept: one YAML file per entry in an `unreleased`
   directory, compiled into the changelog at release and then
   deleted. [V, GitLab development docs] Today the entry is a
   `Changelog:` trailer in the commit message, and the file is
   generated from the commits. [V, towncrier 26.9.0] Fragments in
   place of "one single file which developers all write to and
   produce merge conflicts"; a fragment is named by its issue and
   type, or starts with `+` when it has none; the build removes
   the fragments and appends the compiled news. [V, reno, design]
   "We want to avoid merge issues when shepherding in a lot of
   release-note-worthy changes". [V, Kubernetes contributor
   guide] The note is written in the pull request's description
   and collected at release; no file is edited at all. Status:
   consensus.
9. **`merge=union` is documented with a warning and has a record of
   harm.** [V, gitattributes, git 2.56.0] union will "take lines
   from both versions, instead of leaving conflict markers. This
   tends to leave the added lines in the resulting file in random
   order and the user should verify the result. Do not use this if
   you do not understand the implications." [V, an open-source
   project's issue, discussed 2023-02-23] With `CHANGELOG.md
   merge=union`, an entry of an open merge request was merged
   under the section just released "whereas it is supposed to stay
   under `## Unreleased`. Every open merge request thus requires a
   manual change", and "entries are duplicated"; reverting the
   strategy was among the remedies weighed. [S] Union also keeps
   a line one side deleted, and whether the hosting platform's
   merge button honours the attribute differs by platform; neither
   was verified at source. Status: contested; used, and known to
   hurt wherever position or deletion carries meaning.
10. **A custom merge driver is not carried by the repository.** [V,
    gitattributes] "The definition of a merge driver is done in
    the `.git/config` file, not in the `gitattributes` file". Every
    clone must be configured, and a hosting platform's merge does
    not run it [S for the platform]. [V, npm docs, v6] npm offers
    such a driver for its lock file, installed per machine. Status:
    consensus that it works locally and is fragile as a team
    mechanism.
11. **Newest-first or oldest-first makes no difference.** Both put
    every author's insertion at one position; GitLab's attempt to
    spread insertions over random positions failed (finding 8).
    [Y] The earlier note `2026-09-29-change-record-file-format.md`
    (option e) set aside one file per record because the forge had
    one writer; with several writers that reason is gone.

### C. Shared state files

12. **A file that can be computed is regenerated, never merged by
    hand.** [V, npm docs, v6] Lock file conflicts "can be resolved
    by manually fixing any `package.json` conflicts, and then
    running `npm install [--package-lock-only]` again. npm will
    automatically resolve any conflicts for you". [V, Cargo FAQ]
    "The lockfile can also be a source of merge conflicts"; reset
    your side, fix the other conflicts, "and then run some cargo
    command ... which should re-update the lockfile". [V, Rails
    8.1 guide] "Merge conflicts can occur in your schema file when
    two branches modify schema. To resolve these conflicts run
    `bin/rails db:migrate` to regenerate the schema file." The
    pattern in all three: the derived file is still committed, its
    conflict is expected, and the resolution is a command, not a
    judgement. Status: consensus.
13. **Further along the same line, the state is not stored at
    all.** reno reads notes and releases from the git history and
    tags (finding 15); GitLab's changelog and Kubernetes' release
    notes are compiled from commits and pull requests (finding 8).
    Status: consensus for release bookkeeping.
14. **One file per record is how tools built on git avoid a shared
    table.** Doorstop (an item), reno and towncrier (a note),
    migrations (a step), ADRs (a decision). Two new files with
    different names never conflict; that is also why their
    collisions are silent and need finding 7 or section E. [Y]
    Tools that go beyond files keep an operation log merged by
    rule: [V, git-bug] concurrent edits are joined into a graph
    and ordered by a logical clock, with no conflict shown to the
    user, at the price that the data are git objects and no longer
    files a person reads. CRDT formats for prose in git were not
    surveyed at source. Status: consensus for one file per record;
    emerging for operation logs.

### D. Version numbers on two branches

15. **The version is given at release, by a tool, from what was
    merged.** [V, semantic-release] It "uses the commit messages to
    determine the consumer impact of changes" and "automatically
    determines the next semantic version number", which "removes
    the immediate connection between human emotions and version
    numbers". [V, Changesets] A contributor adds a statement of
    intent with his change; "The version command is run when a
    release is ready", and it "consumes all changesets, and updates
    to the most appropriate semver version". [V, reno, Usage]
    "Notes are output in the order they are found when scanning the
    git history", with releases read from tags; the page warns that
    a note edited on a later branch then shows under the later
    release. [S] Tools that derive a package version from the
    newest tag and the distance from it exist; the page was not
    reached. Status: consensus in software. No source was found on
    versioned prose documents edited on two branches; applying the
    pattern to them is [Y].

### E. Detecting silent collisions

16. **Checks run at the meeting point, against the merged result.**
    [V, GitHub, merge queue] The queue ensures that "the pull
    request's changes pass all required status checks when applied
    to the latest version of the target branch and any pull
    requests already in the queue"; a request that fails "will be
    removed from the queue". This is the mechanism for exactly the
    case of two branches that are each correct and wrong together.
    [V, pre-commit] Hooks run at commit for "identifying simple
    issues before submission to code review", and the same checks
    can run in CI. A hook on one clone cannot see the other clone,
    so it does not find a duplicate across branches; only a check
    after the merge, or on the merge candidate, can. [Y] Status:
    consensus.

### F. The workflow level

17. **Short branches, small changes, one owner per branch.** [V,
    trunkbaseddevelopment.com] A branch "should only last a couple
    of days", and "the developer count should stay at one (or two
    if pair-programming)". The practice does not remove collisions;
    it shortens the time in which a number or a version is taken
    blind. Status: consensus.
18. **Ownership routes review; it does not prevent concurrent
    edits.** [V, GitHub, code owners] "Code owners are
    automatically requested for review when someone opens a pull
    request that modifies code that they own." Status: consensus.
19. **Locking is chosen where merging is impossible.** [V, Git LFS,
    File Locking] "Concurrent edits in Git repositories will lead
    to merge conflicts, which are very difficult to resolve in
    large binary files"; lockable files are made read-only until
    locked, and the lock lives on the server. The page itself
    warns that few servers implement it fully. Teams lock binaries
    and merge text; no source was found that recommends locking
    Markdown. [Y for the last sentence] Status: consensus for
    binaries.

### G. A save made on the user's behalf that meets a conflict

20. **No tool surveyed resolves a content conflict for the user.**
    What differs is what is left in his hands.
    - [V, Flux image automation] A controller that commits on its
      own retries "with an exponential backoff, until it
      succeeds", and can push to a separate branch for review. It
      can afford to: its change is computed afresh on each run
      from the current state, so there is nothing to merge.
    - [V, GitBook, Git Sync troubleshooting] A failed sync shows
      "an unexpected error", and the way through is to make a
      small new change, which makes the whole content be exported
      or imported again.
    - [S, search summary; the plugin's pages reached did not cover
      it] A notes plugin that commits and syncs on a timer opens,
      on a conflicted pull, an overview page listing the
      conflicted files with the usual markers, and offers a
      command to mark them resolved.
    - [V, Jujutsu, Conflicts] "if you rebase a commit and it
      results in a conflict, the conflict will be recorded in the
      rebased commit and the rebase operation will succeed"; this
      "Allows you to postpone conflict resolution until you're
      ready for it", and the way through is always the same:
      "check out the conflicted commit, resolve conflicts, and
      amend".
    - [V, Claude Code, Common workflows] Parallel sessions are
      kept apart by a worktree and a branch each, "without the
      edits colliding"; the page says nothing of how the branches
      are joined.
    Status: consensus on the limits (sync before the work, keep
    the local work safe, say where the conflict is, one command to
    go on); emerging for conflicts recorded as state.

## Options with trade-offs

### The internal note's options against the outside

| Option | Outside precedent | What the outside says |
|---|---|---|
| A. one writer at a time | file locking (19) | chosen for files that cannot be merged, and enforced by a server; as a bare convention for text, no precedent found |
| B. make the stop survivable | every tool of finding 20 | the minimum everywhere; none goes further than keeping the work safe and showing one way through; removes no silent collision |
| C. make appends merge (`merge=union`) | exists (9) | known to hurt: order lost, entries land in the wrong section, duplicates; the field left it for one file per change (8) |
| D1. block or suffix per author | none found (6) | no precedent in document repositories |
| D2. allocation from the remote before the write | the editor or the platform as allocator (2) | precedent only where a central counter exists; a fetch before the write narrows the window and does not close it |
| D3. ID given at the merge | Rust RFCs, KEPs, PEPs (2) | consensus; needs one meeting point and a placeholder until then |
| E. state derived, not stored | lock files, schema file, compiled changelogs (12, 13) | consensus, in two strengths: regenerate after a merge, or do not store |
| F. divide by topic | one file per record (14), short branches (17) | consensus as a way to make textual conflicts rare; makes ID collisions silent rather than rarer |
| G. meet in another system | release notes in the pull request, KEP tracking issue (2, 8) | precedent for bookkeeping that lives on the platform; none surveyed for the thinking itself |
| H. record, pin or tolerate the engine version | [S] lock files and migration tables record the tool or schema level they were written by | not surveyed at source here; outside this note's question |

### Options the internal note did not list

**I. A guard that makes the ID collision loud (finding 7).** One
small file holding the last ID given per prefix (and the current
version per document), rewritten by every write that takes an ID.
Two branches that each took an ID then always conflict in that
file, at the save, before anything cites the later ID; the second
author renumbers his new items and goes on. Keeps the ID scheme
whole. Costs one more file in every write, a conflict on purpose
at every parallel allocation, and a defined renumbering step for
items not yet handed over. It must be the one file never given to
`merge=union`, and it is itself state that could be derived, so it
sits against E unless it is declared the exception. Precedent:
migrations only.

**J. A duplicate-ID and dangling-reference check at the meeting
(findings 1, 4, 16).** Uniqueness said in words and verified after
every merge or pull, before the push. Finds; does not prevent. The
cheapest of all, and the precondition of every other option: a
scheme that cannot collide still wants the check.

**K. Two identifiers: a stable one nobody reads and a human one
that may change (findings 4, 5).** StrictDoc's MID beside its UID,
a hash with a short prefix in git-bug and Beads. A duplicate human
ID is then repairable, because citations that matter follow the
stable one. For the forge it would mean that `PREFIX.NNNN` stops
being the identity, which is the opposite of "global and stable,
never renumbered".

**L. A non-sequential human ID (finding 5).** A short hash or a
time-based ID in place of the number. Cannot collide in practice,
needs no allocator and no guard. Loses numbering in tens, groups
by hundreds, order, and ease of saying an ID aloud; abbreviations
have been seen to hit the wrong record.

**M. One file per change for the log, compiled or simply listed
(finding 8).** A record file per round or per change, named so
that two authors never share a name. Ends the conflict in the
history at its root. The directory grows with every round, and the
companion stops being one file handed over with its document; the
earlier format note weighed this as its option (e).

**N. The version given at the merge into `main`, not at the edit
(finding 15).** A branch carries its changes without a number;
the number, `last_change` and the log's version label are written
when the round lands. Ends the silent double bump. Changes what
"a round is one version" means while the round is unmerged, and
needs someone or something in the role of the release tool.

**O. Regenerate instead of resolve (finding 12).** For every file
or field that is derived (`last_change`, the ledger's derivable
tables, the indexes, the renders), the answer to a conflict is
declared to be a regeneration, and the save's way through a
conflict runs it. Weaker than E (the files stay), and enough to
turn most of the frequent conflicts into no decision at all.

**P. Review by merge request with the checks on the candidate
(finding 16).** The second author's work is checked against the
first's before it lands. Needs a hosting platform with pipelines
and somebody to run a model-driven check there; the forge's checks
are agents, not scripts.

### What is known to fail

- Sequential numbers taken locally with no guard (finding 1).
- `merge=union` on a file whose order or sections carry meaning
  (finding 9).
- Spreading insertions over positions to dodge conflicts (finding
  8).
- A merge driver as a team mechanism without per-clone setup
  (finding 10).
- A hook on one clone as a guard against the other clone (finding
  16).

## Relevance to this project

All of this is the author's reading [Y] of the findings against
the internal note.

**What the outside confirms.** The internal note's ranking holds:
the duplicate ID is the collision every surveyed community met
first, and none solved it by care. Its estimate that the ledger
makes nearly every pair of saves conflict matches what drove
GitLab, towncrier and reno to fragments.

**What the outside corrects.**

- Option C should be read as a warning, not an option, for the
  history log and the ledger: git's own manual warns against it,
  and it would remove the one moment a duplicate ID is seen, as
  the internal note already suspected.
- Option D's first variant (a block or suffix per author) has no
  precedent; its third (the ID at the merge) is the consensus, but
  only where a platform counter or an editor exists, which the
  forge, with a script as its only door to git, does not have.
- Option E is not a reversal of "single source of truth" in the
  outside's weaker form: lock files stay committed and stay
  authoritative for their readers; only their conflicts are
  settled by regeneration (option O).
- The dead end at the save is not solved anywhere by resolving for
  the user. What is solved is the three things around it: syncing
  before the work, never losing the local work, and one stated way
  through.

**Recommendation**, offered once:

1. **Detection first (J).** Say in words that an ID is unique in a
   project and have it verified at every meeting of two lines of
   work. It is the one measure every scheme needs, and the only
   one that costs no convention.
2. **For IDs, the guard file (I) before any change of scheme.** It
   is the single outside pattern that keeps `PREFIX.NNNN` in tens,
   stable and readable, and still makes the collision impossible
   to miss, at the moment when renumbering is still harmless. A
   hash ID (L) is what the world uses when writers are many and
   truly parallel; by the brief's own estimate of few collisions
   it would cost more in readability than it saves. Number at the
   merge (D3) fits only if the project decides that work meets
   through merge requests on a platform.
3. **For the ledger, the indexes and `last_change`, regeneration
   (O) rather than a new structure.** It is the lock-file practice,
   it needs no reversal of a position, and it removes the most
   frequent stop. The Waiting section has no source to regenerate
   from and stays a true conflict.
4. **For the history log, leave the file as it is until two
   people really write the same document in the same days;** then
   fragments (M), not union (C).
5. **For the version, decide in words what a number means on an
   unmerged branch (N)** before building anything: the outside's
   answer is that it has none yet.
6. **For the save, the minimum of finding 20:** fetch and say
   ahead or behind before a round, keep the commit, name the
   conflicted files, and give one defined way on. Whether that way
   is inside the forge or is "git, by hand" is the forge's
   boundary to draw (POS.1110); the outside draws it at
   regenerating what is derived and showing the rest.

Nothing in this note changes any convention. The positions it
would touch are POS.1110 (the boundary to git and the known hole)
and the ID scheme of `CLAUDE.md`, through `/forge intent`.

## What stays uncertain

- Doorstop, StrictDoc and Sphinx-Needs were read for how an ID is
  made, not for what they do at a duplicate; that a duplicate
  stops their build is unverified. A source on Doorstop under
  parallel branches was not found.
- The behaviour of the notes plugin at a conflict and the history
  of Beads' and Rails' change away from sequential numbers come
  from search summaries.
- Whether hosting platforms honour `merge=union` and custom
  drivers in their own merge button was not verified.
- No source was found on versioned prose documents (as opposed to
  software releases) edited on two branches; finding 15 is carried
  over by analogy.
- CRDT formats and structure-aware merge tools for Markdown were
  not surveyed at source.
- The engine-version dimension (option H) was outside this
  question.

## Sources

All fetched 2026-10-03 unless marked.

- Django 6.1, *Migrations*,
  https://docs.djangoproject.com/en/stable/topics/migrations/
- Alembic, *Working with Branches*,
  https://alembic.sqlalchemy.org/en/latest/branches.html
- Rails 8.1 guide, *Active Record Migrations*,
  https://guides.rubyonrails.org/active_record_migrations.html
- PEP 1, *PEP Purpose and Guidelines*,
  https://peps.python.org/pep-0001/
- Rust RFCs, README,
  https://github.com/rust-lang/rfcs/blob/master/README.md
- Kubernetes enhancements, keps/README,
  https://github.com/kubernetes/enhancements/blob/master/keps/README.md
- adr-tools, `src/adr-new`,
  https://github.com/npryce/adr-tools/blob/master/src/adr-new
- log4brains, https://npmjs.com/package/log4brains (through a
  search summary)
- django-linear-migrations,
  https://github.com/adamchainz/django-linear-migrations
- Atlas, *Migration Directory Integrity*,
  https://atlasgo.io/concepts/migration-directory-integrity
- Doorstop, *Creation*,
  https://doorstop.readthedocs.io/en/latest/cli/creation.html
- StrictDoc, *User Guide*,
  https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide.html
- Sphinx-Needs, *Configuration*,
  https://sphinx-needs.readthedocs.io/en/latest/configuration.html
- Beads, *Hash IDs*,
  https://beads.gascity.com/core-concepts/hash-ids; its release
  history through a search summary
- git-bug, *Data model*,
  https://github.com/git-bug/git-bug/blob/master/doc/design/data-model.md
- ULID specification, https://github.com/ulid/spec
- OpenStack reno, *Design Constraints* and *Usage*,
  https://docs.openstack.org/reno/latest/user/design.html,
  https://docs.openstack.org/reno/latest/user/usage.html
- towncrier 26.9.0, https://towncrier.readthedocs.io/en/stable/
  and its tutorial,
  https://towncrier.readthedocs.io/en/stable/tutorial.html
- GitLab, *How we solved GitLab's CHANGELOG conflict crisis*
  (2018-07-03),
  https://about.gitlab.com/blog/solving-gitlabs-changelog-conflict-crisis/
- GitLab development docs, *Changelog entries*,
  https://docs.gitlab.com/development/changelog/
- Kubernetes contributor guide, *Release notes*,
  https://github.com/kubernetes/community/blob/master/contributors/guide/release-notes.md
- Changesets, *Intro to using changesets*,
  https://github.com/changesets/changesets/blob/main/docs/intro-to-using-changesets.md
- git 2.56.0, *gitattributes*,
  https://git-scm.com/docs/gitattributes
- quantify-scheduler, issue 406, on `merge=union` for the
  changelog (discussed 2023-02-23),
  https://gitlab.com/quantify-os/quantify-scheduler/-/issues/406
- npm CLI v6, *package-locks*, section "Resolving lockfile
  conflicts",
  https://docs.npmjs.com/cli/v6/configuring-npm/package-locks
- Cargo, *Frequently Asked Questions*,
  https://doc.rust-lang.org/cargo/faq.html
- semantic-release, https://semantic-release.gitbook.io/semantic-release/
- GitHub Docs, *Managing a merge queue*,
  https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- GitHub Docs, *About code owners*,
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- pre-commit, https://pre-commit.com/
- Trunk Based Development, *Short-Lived Feature Branches*,
  https://trunkbaseddevelopment.com/short-lived-feature-branches/
- Git LFS wiki, *File Locking*,
  https://github.com/git-lfs/git-lfs/wiki/File-Locking
- Flux, *Image Update Automations*,
  https://fluxcd.io/flux/components/image/imageupdateautomations/
- GitBook, *Git Sync, Troubleshooting*,
  https://gitbook.com/docs/docs-as-code/git-sync/troubleshooting
- Jujutsu, *Conflicts*, https://docs.jj-vcs.dev/latest/conflicts/
- Claude Code, *Common workflows*,
  https://code.claude.com/docs/en/common-workflows
- Obsidian Git plugin documentation,
  https://publish.obsidian.md/git-doc/ (pages reached did not
  cover conflicts; behaviour from a search summary)
