---
description: Run a challenger persona against the substance of any chain artefact — bare = persona roster
argument-hint: "[persona] [artefact] [project-slug]"
---

Challenger personas live as `.claude/agents/challenger-<persona>.md` —
one isolated agent per persona, each defined by the blind spots it
exists to find, said in its `description`; the roster is the scan of
those files. Adding a persona means adding an agent file from
`templates/challenger.md`; this command does not change (who creates
a persona, and when: CLAUDE.md, Isolated reviewers).

Shared behaviour: the contract skill named in each persona file's
front-matter (CLAUDE.md, Isolated reviewers). This command only
chooses the persona, passes the target and verifies the bookkeeping.

**Bare `/challenge` — the roster.** List the available personas (scan
`.claude/agents/challenger-*.md`) and recommend which fits the
project's subject. A recommendation, never a gate.

**`/challenge <persona> [artefact] [slug]` — run it.** The target is
an artefact named as `/forge` names it (CLAUDE.md, Isolated
reviewers); how it narrows the run is the contract's and the persona
file's. Invoke the `challenger-<persona>`
subagent on the project (infer it from context; if ambiguous, ask),
naming the target artefact. Pass only the project path and the target,
nothing else (CLAUDE.md, Isolated reviewers).

Best used **before the next layer is first derived from the target** —
for the intent, before the first `/forge assignment` — while an
accepted challenge is still cheap to absorb, and again after any major
shift of direction. Running it on a near-final artefact is late but
not useless.

When it returns:
1. Verify the challenge file exists and the ledger Challenges table is
   updated; fix bookkeeping only, never the challenges themselves.
2. Present it to the principal: the overall
   read first, then each
   challenge compressed to two or three sentences. Do not editorialise and
   do not defend earlier drafting choices — if you disagree with a
   challenge, say so plainly and separately, marked as your own view.
3. Answer the challenger's open questions where the answers exist in our
   conversation but not in the documents, and flag those to the principal:
   they usually mean something true is missing from the intent.
4. End by offering a **walkthrough** of the challenges
   (`.claude/skills/walkthrough/SKILL.md`, the one owner of its
   shape and of the verdict words). What `accept` writes here: it
   feeds into `/forge intent`, state `accepted`; an accepted
   challenge must change the intent (CLAUDE.md, Isolated reviewers).
   The other verdicts are the walkthrough's. If he declines the
   walkthrough, the challenges wait.

A rejected challenge is a normal, healthy outcome. So is a challenge that
survives three rounds unresolved — park it and move on.
