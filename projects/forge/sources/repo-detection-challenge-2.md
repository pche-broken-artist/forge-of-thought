origin: pasted into the conversation by the principal on 2026-10-22; written in Czech by Gemini in a session outside the forge, in a conversation the principal ran on his tasks, as the answer to his question whether the proposal for THR.0730 (a project inside a larger repository) could be simplified by one limiting condition at the start; translated into English at registration on the principal's word, the wording kept as close as the translation allows, the proposed English wordings of the items kept as they were
date: 2026-10-22

# The simplification: a guard condition

## The principle of radical simplification (guard condition)

A project has only two possible states for the forge:

- It is a repository of its own: `git rev-parse --show-toplevel`
  equals exactly the project's path `projects/<slug>`. Then the full
  git logic is used (the checks clean and main, commit, tag,
  `--undo`).
- It is not a repository of its own: the path differs (it is a
  directory without git, or in a subdirectory of another's git).
  Then the forge understands the project purely as an ordinary
  directory on disk (a plain directory). The forge does not call,
  examine or handle the git layer at all.

## What happens with another's git? (the answer to your question)

If the user puts the project into a subdirectory of another's
repository:

The original, complex proposal: the forge found out through `git
ls-files` whether the other git tracked `ledger.md`, advised the user
the command `git rm --cached` and steered its behaviour by the state
of the other's index.

The simplified proposal (guard): the forge ignores the other's git
completely. The write goes directly to disk into the directory. If
the user keeps the project in another's git, it is his business: the
forge does not touch his git, does not find out what it tracked and
does not order him to `git rm`. The other git sees the file as
changed on disk, exactly as if any other text editor had changed it.

If we want to be extremely careful, the script only prints a
one-sentence notice when it detects another's top level: "Project is
inside an external git repository at <path>. Forge treats it as a
non-git directory and will not perform any git operations."

## What falls away and gets simpler thanks to this

- No querying of another's index (`git ls-files`): all the logic of
  detecting whether another's git tracks `ledger.md` falls away.
- The end of the complex `--layout inside` in the fixture: two states
  suffice in `fixture.py`, with git and without git. No need to
  generate and test artificial outer repositories for the fixture.
- Simplification of the specification (POS, SOL): the paragraph on
  the exceptions of the migration in another's git and the
  instruction to the user to `git rm --cached` fall away.

## How the simplified wording in the proposal would look

POS.0550 (Persistence): every user project is likewise a repository
of its own where its owner wants one, with whatever remote and
visibility he gives it (POS.0940). Of its own means that git names
the project's directory as the top of its repository: the one
question the scripts ask, never the presence of a `.git`. Any project
whose top lies elsewhere or is missing is treated purely as a project
outside git: the scripts write directly to disk without git
operations. A project outside git comes in by hand, a copy or a link
into `projects/`, and the forge knows it from then on.

SOL.0510 (the git scripts): every project that is a repository of its
own: git names its directory as the top (`rev-parse
--show-toplevel`). Where the top lies above the project or is
missing, git operations are completely skipped and the project is
treated as a plain directory outside git.

SOL.0800 (the migration): refuses an unclean repository, behind
origin or not on main only where the project is a repository of its
own. A project outside git gets none of these: `--apply` writes
directly to disk and tells the user to rely on their manual backup;
`--undo` is disabled.

This approach fully solves issue #3, takes a fraction of the code and
eliminates all the "cleverness" that could break in the future on an
edge case.
