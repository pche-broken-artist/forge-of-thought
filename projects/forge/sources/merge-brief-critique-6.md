origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the brief `00-brief-collaboration.md` v0.7; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the brief `collaboration` 0.7

- Addressing the second tree. Both windows run from the engine's
  root with the same cwd, so `/save platform` or `/forge platform`
  cannot tell from the cwd which tree is meant. The solution the
  brief assumes implicitly but does not say: `<slug>@<branch>` is
  the slug for the commands (`/save platform@rework`), the bare slug
  is `projects/<slug>`, and forge-save without a slug visits both
  trees, which is desirable.
- The write step must not fetch. "The write step ... on a repository
  that is behind repeat it": the state "behind" needs a fetch; F2 has
  just driven the network out of the write so that an outage cannot
  spoil the round. Let the reflection read the state (where it makes
  the reservation) from the last `forge-status --remote`; the write
  step only repeats the known state, and an unknown or stale state
  never blocks.
- The steps of finishing by hand. "Resolve, add, commit with the
  message, continue": in a rebase, after the add comes
  `rebase --continue` without a commit; in a merge a commit without a
  continue; the sentence mixes the two. And since forge-save aborts
  a failed rebase today, the manual path begins with the principal's
  own `git pull --rebase`, not with continuing after `/save`.
- Five digits, two more sentences. New IDs stay four-digit as long
  as they fit (no zero padding, POS.0010 stays POS.0010); the fifth
  digit comes only beyond 9999. And every sorting of IDs in the
  scripts must be numeric by (prefix, number): as a string
  POS.10000 comes before POS.9990.
- M versus Order on A2. Order says "A2 first, then ... C1", M does
  the conversion only after the threads are cut. Not a
  contradiction (the conversion walks `threads/` too), just say it:
  the order in Order is the order of releases, the order in M the
  order of the steps of one run, and the conversion goes last over
  the threads already cut.
- The engine's second root. `../forge-of-thought@<branch>/` has in
  `projects/` only `projects/forge`; the subject projects are
  gitignored in the engine, so they are missing in the second tree.
  A property, not a defect; write it so that nobody wonders in the
  second window.
