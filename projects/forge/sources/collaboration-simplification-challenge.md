origin: pasted into the conversation by the principal on 2026-10-23; written in Czech by Gemini in a session outside the forge, in a conversation the principal ran on his tasks, answering his briefing on the cutover of the brief `collaboration` after its first release (the deferred releases, DEC.0250, THR.0710, the two options of its section 6); translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-23

# The collaboration cutover: the moloch and how to simplify it

Your intuition is entirely right. You walked into the classic trap of
over-engineering.

The reason is simple: after the conflict of 17 October a reaction
arose that tried to write, in Python, a complete git client of its
own and a deterministic merge engine (custom merge drivers, versions
with `+`, blocks of IDs by the thousand, special worktree
arrangements and so on).

The meaning of Forge of Thought lies in the considered chaining of
thoughts and in the AI architecture, not in reinventing git.

Here is an analysis of what happened, what to throw away, and how to
simplify collaboration to the absolute minimum.

## 1. Analysis: what worked and what is the "moloch"

### A. What was a huge win (release 1, done)

What you did in release 1 solved 90 % of all real conflicts:

1. The ledger out of git (`.gitignore` plus generation at run time):
   the main culprit of every conflict was killed.
2. Clean headers: removing the dynamic fields `date` and
   `last_change` from the artefacts' headers abolished the guaranteed
   conflict at every round of work.
3. One file per thread (`threads/THR.NNNN.md`): two people working
   on different topics never meet in git at all.
4. Unique names of reports: no overwriting of the same files.

### B. What the designed "moloch" is (releases 2 to 4, option A)

The plan for releases 2 to 4 wanted to solve the remaining 10 % of
cases with extremely complex machinery:

- A custom merge driver (`forge-records` in Python): the registration
  of a script of your own in the user's global `.gitconfig`, which
  was to analyse and merge the risky files (histories, decisions).
  Risk: brittle, does not work in CI/CD, does not work for an
  external contributor on GitHub without setup.
- Complex logic of versions on branches (`v1+2`): computing the
  state of versions at run time.
- The allocation of blocks of 1000 IDs per author (release 4): manual
  reservation of IDs (author A has 1000 to 1999, author B 2000 to
  2999, for example).
- The conversion of the text to one sentence per line (release 3): a
  destructive change of the formatting of every document in the
  repository.

## 2. The view of simplification: what collaboration "without the moloch" looks like

Instead of writing a git engine of our own we use what Claude, an
LLM, is best at: it is an intelligent being that can read text and
resolve conflicts directly.

### 1. Merging histories (`.history.md`) and records: native git `merge=union`

- Instead of writing a Python merge driver it is enough to put a rule
  into `.gitattributes` for `.history.md` and `decisions.md`:
  `*.history.md merge=union`
- At a merge git simply joins the lines of both branches one under
  the other (append-only).
- If a small awkwardness in the order of lines arises,
  `forge-ledger.py` breaks nothing when it reads the ledger, and
  Claude can repair it organically at the next task. No hand-written
  Python driver is needed.

### 2. Duplicate IDs: "fix on read" instead of blocks of 1000 IDs

- No blocking of IDs by the thousand. People and Claude generate IDs
  normally, sequentially (POS.0100, POS.0101, ...).
- What if two people create the same `POS.0105` in parallel?
  1. Git merges the branches.
  2. `forge-ledger.py` already detects duplicate IDs when it reads
     and reports them as a finding.
  3. Claude, when `/forge` runs, sees the finding of the duplicate
     and fixes the conflict in one simple step (renumbering the
     newer ID).

### 3. Conflicts in text (the artefacts): the LLM as an intelligent conflict resolver

- When a conflict in text arises (two people changed the same
  position of the intent, say), git writes the standard markers into
  the file:

```markdown
<<<<<<< HEAD
POS.0100: The original thought A
=======
POS.0100: The original thought B from the colleague
>>>>>>> branch
```

- Quick resolution: Claude has the right to read these markers.
  Instead of a complex interactive guide `/merge` in Python, Claude
  gets the instruction: "There is a conflict in intent.md. Read both
  variants, propose a merge of the thoughts and write the result."
- The user only confirms (consent): "Yes, this makes sense." Then
  `forge-save`.

### 4. Branches and worktrees

- No special system for managing directories of the kind
  `projects/<slug>@<branch>` is needed.
- Work on several branches is standard git: `git checkout -b
  new-thought`, or a standard git worktree if an advanced user wants
  one. The forge treats it as any other git project.

## 3. Comparison: what is cancelled and what stays

| Area | The original complex plan (releases 2 to 4) | The simplified proposal (pragmatic) |
|---|---|---|
| Merging histories | A custom Python driver `forge-records` registered in `.gitconfig` | Native `.gitattributes` with `merge=union` |
| Allocation of IDs | Blocks of 1000 IDs per author by `ids.md` | Sequential IDs; duplicates detected by `forge-ledger.py` and fixed by the LLM |
| Conflicts in text | A Python script `/merge` with an interactive walkthrough | A standard git conflict; the LLM reads `<<<<<<<` and proposes the merge |
| Versioning on branches | Complex arithmetic of branches and `+` flags in headers | Standard versioning on `main` at approval or release |
| Formatting of text | Conversion of the whole repository to one sentence per line | Cancelled. Ordinary Markdown stays. |

## 4. Answers to the questions of the briefing

1. Is the deferral (DEC.0250) right? Yes, absolutely. It turned out
   that release 1 removed 90 % of the real problems. Inventing heavy
   machinery for hypothetical multi-author scenarios without real
   pressure was a mistake.
2. Which option of section 6 is better (A or B)? Unambiguously an
   extended version of option B (simplified). Write no further
   scripts of the `/merge` kind and no driver of your own. Extend
   Claude's ability to work with git (under the safety hook), and let
   the LLM resolve conflicts in text as any human developer does.
3. Is the designed machinery proportionate? It is not. It reacted to
   two conflicts of one person (caused by `ledger.md` and the
   headers). Those causes are already removed in release 1. Building
   custom merge drivers for that is disproportionate.
4. Which of the limitations will hurt first? None of them will hurt
   you in ordinary practice. If a second author comes, he will most
   often make a pull request on GitHub. GitHub shows a conflict in
   text in the same way and the team's integrator resolves it in the
   PR. Handing out blocks of 1000 IDs to a PR contributor is
   unusable.

## The recommended next step

1. Leave release 1 as it is (it is excellent, it works and it cleared
   the battlefield).
2. Officially cancel the planned releases 2, 3 and 4, or replace them
   by a single principle:
   "The forge does not stand in for git. Records are merged through
   `merge=union`. A conflict in text or a duplicate ID is resolved by
   Claude with perspective, within the ordinary dialogue at
   `forge-pull` / `forge-save`."
3. Put the energy into developing the thought chains themselves, the
   agents and the analytics; that is where the real value of the
   forge lies.
