---
description: Run a challenger persona against the substance of any chain artefact — bare = persona roster
argument-hint: [persona] [artefact] [project-slug]
---

Challenger personas live as `.claude/agents/challenger-<persona>.md` —
one isolated agent per persona, each defined by the blind spots it
exists to find. Currently: `cto`. Adding a persona means adding an
agent file; this command does not change. New personas are created only
by the principal's decision, and only where their blind spots genuinely
differ — personas that would say the same things in different words are
noise.

Shared invariants, whatever the persona: an isolated context that never
sees the working conversation; substance only, never document quality
(that is the critic's job); three to seven sharp challenges, each with
a severity (dealbreaker | major | minor, ordered by it — a fatal flaw
is never buried among cosmetics), a falsifiable "what would change my
mind" and an epistemic status (consensus | active debate | emerging
practice | my judgement); no fabrication — a precise "I don't know"
beats an invented figure, and anything reconstructed from memory is
flagged; output `challenges/YYYY-MM-DD-challenge-<persona>.md`
(immutable) plus CHL entries in the ledger, continuing the global CHL
sequence.

**Bare `/challenge` — the roster.** List the available personas (scan
`.claude/agents/challenger-*.md`) and recommend which fits the
project's subject. A recommendation, never a gate.

**`/challenge <persona> [artefact] [slug]` — run it.** The target may
be any artefact of the chain — `intent` (the default), `assignment`,
one day `brd` or deeper layers. Invoke the `challenger-<persona>`
subagent on the project (infer it from context; if ambiguous, ask),
naming the target artefact. Pass only the project path and the target —
no summary of the conversation, no defence of the principal's
reasoning. Its isolation and its ignorance of our discussion are
the point. The challenger reads the whole chain above the target for
context; what it challenges is the substance of the target.

Best used **before the next layer is first derived from the target** —
for the intent, before the first `/forge assignment` — while an
accepted challenge is still cheap to absorb, and again after any major
shift of direction. Running it on a near-final artefact is late but
not useless.

When it returns:
1. Verify the challenge file exists and the ledger Challenges table is
   updated; fix bookkeeping only, never the challenges themselves.
2. Present it to the principal in Czech: the overall read first, then each
   challenge compressed to two or three sentences. Do not editorialise and
   do not defend earlier drafting choices — if you disagree with a
   challenge, say so plainly and separately, marked as your own view.
3. Answer the challenger's open questions where the answers exist in our
   conversation but not in the documents, and flag those to the principal:
   they usually mean something true is missing from the intent.
4. Offer a **walkthrough** of the challenges (CLAUDE.md, Working
   methods): one at a time in order of severity, your recommendation
   with a one-sentence reason first, then the principal's verdict —
   **accept** (feeds into `/forge intent`; an accepted challenge must
   change the intent), **reject** (a DEC with his one-line reason;
   the challenger respects it in future runs), **park** (stays open)
   or **obsolete** (note what made it moot). Verdicts are carried in
   the conversation and written once at the end: states in the ledger,
   DEC records, the intent iteration. Never delete challenges; states
   only. If he declines the walkthrough, the challenges wait.

A rejected challenge is a normal, healthy outcome. So is a challenge that
survives three rounds unresolved — park it and move on.
