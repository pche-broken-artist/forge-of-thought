origin: pasted into the conversation by the principal on 2026-10-22; written in Czech by Gemini in a session outside the forge, in a conversation the principal ran on his tasks, as a challenge of the proposal of 2026-10-22 for THR.0730 (a project inside a larger repository) as Claude reflected it before the write; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-22

# Challenge of the proposal for a project inside a larger repository

The proposed solution is architecturally and philosophically very
clean. Against the previous direction of 21 October (when the forge
was to manage a project inside another's repository and handle
relative paths), today's decision of 22 October fundamentally
simplifies the boundary of responsibility: the forge never writes
into another's git repository and treats such a project as not under
git.

Below is a detailed analysis and a critical opposition (challenge) of
the parts of the proposal from the view of edge cases, safety,
testing and consistency.

## 1. The scope of the protection against writing: only ledger.md, or the other files too?

Weak point of the proposal: POS.0550 and SOL.0680/0800 say that the
forge asks the outer repository one thing only: whether it tracks
`ledger.md` (`git ls-files ledger.md`).

Risk: what if the outer git repository tracks other files inside the
project directory (e.g. `docs/architecture.md`, `POS.md` or other
artefacts) but `ledger.md` is missing from the index? If a forge
script modifies these documents, it writes into versioned files of
another's git, which breaks the basic principle "the forge does not
write into another's git".

Recommendation: examine whether `git ls-files` should be run either
on every file to be written, before its change, or over the whole
project directory before the first write (`git ls-files
projects/<slug>`). If the outer git tracks anything inside the
project, the forge refuses the operation. If the intention is to
watch strictly and only `ledger.md`, the SOL should explicitly defend
why.

## 2. Shortcomings of the migration of projects not under git (no `--undo`, the danger of an incomplete write)

Weak point of the proposal: POS.1740 and SOL.0800 say that for
projects not under git the refusals of the git checks do not apply
and `--undo` is refused. The user is told to take a manual backup
before `--apply`.

Risk of a non-atomic migration: with a project under git, steps B, C
and D are covered by a git commit or tag or by a revert. If the
migration script fails midway on a project not under git (e.g. a
disk write error in step C), the project stays in a half-done or
damaged state. `--undo` returns an error and the user has to restore
from the backup by hand.

Recommendation: make sure the migration script writes atomically on
projects not under git (e.g. writing to temporary files and renaming
only after success), or validates all steps in memory before the
first physical write to disk. In the CLI output before `--apply` on a
project not under git, stress an explicit warning about the manual
backup.

## 3. Detection of the top-level repository and symlinks (`rev-parse --show-toplevel`)

Weak point of the proposal: SOL.0510 says canonical paths are
compared (resolved paths compared) between the project directory
`projects/<slug>` and the output of `git rev-parse --show-toplevel`.

Detail to check in the code: `os.path.realpath` (or
`pathlib.Path.resolve()`) must be applied to both paths before the
comparison.

Symlink scenario A: the user creates a symlink `projects/my-proj ->
/external/repo/subfolder`. `rev-parse` returns `/external/repo`.
`realpath(projects/my-proj)` is `/external/repo/subfolder`. The paths
differ, so the project is correctly judged as outside a repository of
its own.

Symlink scenario B: the user creates a symlink `projects/my-proj ->
/external/repo` (the root of the repository itself). The realpaths of
both are equal, so it is judged a repository of its own.

Recommendation: make sure the tests in `fixture.py` also cover the
case where the directory in `projects/` is a symlink to a
subdirectory of another's repository.

## 4. Testing in `fixture.py` (SOL.0830): a missing negative test case

Weak point of the proposal: SOL.0830 introduces the switch `--layout
none | inside`. The tests verify the migration and the ledger in
these layouts.

Missing test: the proposal does not describe testing the refusal of
the write when `ledger.md` in the layout `inside` is tracked by the
outer repository.

Recommendation: add an explicit negative test to the test set: create
the fixture `inside`, run `git add ledger.md` in the outer temporary
repository in `tmp/` and verify that both migrate and the ledger
script fail with the exactly defined error message recommending `git
rm --cached ledger.md`.

## 5. Wording and unambiguity in the import-project skill

Weak point of the proposal: "A project that is not a repository, or
lies in another's, is not imported: it is copied or linked into
`projects/` by hand and the forge knows it from `/forge` on
(POS.0550)."

Ambiguity: what if the user copies or links by hand a directory that
IS a repository of its own (e.g. links an external git repository
into `projects/my-repo`)? By the first part of the sentence, "A
project that is not a repository...", such a project should be
imported, but by the second part it was brought in by hand.

Recommendation: change the text in the skill to a wholly unambiguous
wording: "A project that is not a repository of its own (or lies
inside another repository) cannot be imported via this skill. It must
be copied or linked into `projects/<slug>` manually..."

## 6. Performance and behaviour of `docs-state.py`

Weak point of the proposal: SOL.0510 says the walk up the parent
directories looking for `.git` in `docs-state.py` is replaced by the
same detection logic through `forge_repos`.

Impact: if `docs-state.py` walks dozens of projects and starts a new
subprocess `git rev-parse --show-toplevel` for each, there may be a
slight slowdown when rendering the state of the documentation.

Recommendation: create a helper function in the python module
`forge_repos` (e.g. `get_project_git_status(project_path)`) that
encapsulates running `rev-parse` and `ls-files` efficiently and with
a clear interface for the other scripts.

## Summary of the recommended changes to the proposal before approval

- POS.0550 / SOL.0510: consider or specify whether the non-tracking
  concerns `ledger.md` exclusively or any file the forge writes in
  that project.
- SOL.0830: add a negative test for the case where the outer
  repository tracks `ledger.md` (verification of the error message
  and the refusal).
- Skill import-project: slightly reword the last sentence to remove
  the small unclarity about repositories of their own linked by hand.
- Scripts: create in `forge_repos` one method with the comparison
  through `os.path.realpath`, which migrate, ledger and
  `docs-state.py` draw on.
