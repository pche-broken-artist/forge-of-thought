---
description: End a session — what lives only in the conversation, what is unsaved, what a shutdown would lose
---

Close the session so that the user knows nothing is lost (POS.1500,
SOL.0180). This command writes nothing and runs nothing but the
status script; every remedy is an offer.

1. Say what lives only in this conversation: a round not written,
   verdicts carried, anything promised and not done. Offer the write
   (CLAUDE.md, Working methods, One write per round).
2. Run `python scripts/forge-status.py` (no remote) and name every
   repository with unsaved changes; offer `/save`.
3. Remake the project's ledger, `python scripts/forge-ledger.py <slug>`, and name
   stale renders as a fact from its Renders table (stale as `/render`
   step 5 defines it); no offer, the renders are the release's.
4. Close with one sentence: nothing lives only in this conversation
   and shutting the command line loses nothing; or the list of what
   it would lose.
