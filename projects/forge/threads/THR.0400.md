---
id: THR.0400
concerns: intent
origin: the principal
status: open
---

A gate in front of the tools. On 2026-09-20 Claude
read git state directly, past the scripts, twice, and on a bare yes
to one change wrote its consequences as well — with the rules fully
in context and the session in an automatic permission mode, so that
nothing stopped it. The principal's three rules of that day: where
the forge has a script, the script is used; a command of Claude's
own, beyond plain reading, is explained and approved first;
nothing is written, run or changed that was not agreed and
approved. Done the same day, as the soft half: the per-prompt hook
prints the three rules beside its two walkthrough lines
(POS.1170). Open, the hard half: a `PreToolUse` hook,
`scripts/hook-gate.py` in Claude's proposal, that reads each
command and each write before it runs and answers deny (raw `git`,
raw `pandoc` or `markitdown`, with the script to use instead),
allow (plain reading; writes to the session's scratch and to
memory) or ask (a state-changing forge script, any other command
of Claude's own, a write into the repository). Known before it is
built: telling reading from acting, and `git` as a command from
the word in a string, is a heuristic, so what is unsure asks; the
price is a dialog per write, an isolated render included; whether
"ask" holds in an automatic permission mode, and whether the hook
leaves the principal's own `!` commands alone, is to be tried, not
assumed. Whether writes are gated file by file or left to the
reminder is undecided. Deferred by the principal until the forge
has been shown to the group (THR.0390): the script needs tuning
and there is no time for it now; that condition fell when THR.0390
closed on 2026-09-26, and nothing is scheduled in its place.
Claude's reading of 2026-09-26,
offered once: the "deny raw `git`" part of the hard half is done
by the deny list of POS.1200, so what the gate still owes is
`pandoc`, `markitdown` and the ask on writes.
A silent refusal of a save, 2026-09-26, the first save since the
deny list was added: `./scripts/forge-save.ps1 forge -m <message>`
was refused by the permission layer with no dialog and no reason
given, the script never starting. Six probes settled what did it. A
one-line command carrying `git ` inside quotes runs; a two-line one
runs; a here-string carrying the word runs; the message's exact
sentence printed by `Write-Output` runs; the save whose here-string
carried that sentence was refused; the same save with that one
sentence reworded went through (commit 6cfd6f2). So no pattern
matched a word. What was refused was the pair of a state-changing
call and a text saying that raw git is denied to Claude — a
judgement of content and intent, so the automatic permission mode's
classifier and not the deny list; POS.1200 is not at fault.
Research of the same day adds that no rule could have been more
precise anyway: a rule cannot target a tool's primary content field,
and `Bash(command:…)` is ignored with a startup warning. Two
remedies were weighed and neither taken: `-MessageFile` on
`forge-save.ps1`, so that no prose rides on the command line (the
principal: a file is not a good solution); and dropping the prose
statement of the ban to leave only the deny rule, his own proposal,
against which stands that the trigger was the commit message and not
the rule's prose, and for which stands that the ban is today written
three times (the deny list, CLAUDE.md, the hook) — whether the
classifier reads the hook's line as well is not verifiable from
here. Left as it is on his word of 2026-09-26 and watched. What the
incident adds to this thread's own case: the refusal explained
nothing, where a gate of the forge's own would have named the rule
and the script to use instead. The loop to expect: the forge's
commit messages describe the forge's rules, git among them, so the
pair will recur.
The sweep of THR.0210 — names
from `CLAUDE.local.md` searched in what is about to be saved — is
a neighbour of this gate and stays that thread's. Opened
2026-09-20 (Claude's proposal, the principal's rules).
State 2026-10-21: the hard half built for git, as `scripts/hook-git.py`
(POS.1200), narrower than the gate proposed here: it reads git alone,
answers allow or deny and never ask, and names the script to use where
it denies. Still open: `pandoc` and `markitdown`, and the ask on writes.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
