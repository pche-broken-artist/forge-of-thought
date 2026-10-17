origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a second review, of Claude's proposal for mending the six challenges of the architect (intent 5.16, solution design 0.19); translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Second review: the mending of the architect's challenges

## 1. `/merge` and the following `/save`: the rebase drops the merge commit and the conflicts return

`git pull --rebase` (what forge-save does) drops merge commits by
default and linearises: the branch's commits are replayed onto
origin/main one by one. The resolution of the conflicts from the
walkthrough lives only in the merge commit, so if someone pushed to
main between `/merge` and `/save`, the rebase meets the same
conflicts again, forge-save aborts and the person is back at manual
git, exactly what POS.1760 removes. Two cheap fixes, both into
SOL.0820 and SOL.0740:

- `/merge` refuses a repository behind or diverged, as `/release`
  does (POS.1710); the window narrows to the minutes between the
  merge and the save.
- `rerere.enabled true` set by `/setup`, not offered: rerere records
  the resolution at the commit of the merge and resolves the same
  hunks by itself at the replay. For this flow it is a load-bearing
  mechanism, not a convenience. (`pull.rebase merges` would keep the
  merge commit, but the conflict would be resolved again all the
  same; rerere is the part that holds it.)

## 2. Additions

- A fetch before the merge. The contributor's branch exists on the
  origin, not locally; `/merge <branch>` first runs `git fetch
  origin` and merges `origin/<branch>`, or `git merge feature` fails
  on an unknown name. Allow a fast-forward (then there is nothing to
  name in the message; `landed` covers it at the next `/save`).
- Blocks above the used numbers. When `ids.md` is introduced, used
  numbers exist outside any block (THR up to 0680, POS up to 1550);
  the integrator assigns from the highest used number upward, and
  the overlap check reports a block containing a used number too,
  not only a block against a block.
- The numbering of the TBCs: the tests were TBC.0040, the conversion
  script TBC.0050; "TBC.0050 widened by three preliminary tests" in
  0.19 looks like a mix-up.
