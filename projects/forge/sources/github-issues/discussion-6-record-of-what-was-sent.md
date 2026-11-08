# GitHub discussion #6: A record of what was sent out, pinned to the exact version

Source: https://github.com/pche-broken-artist/forge-of-thought/discussions/6  
Author: martinkosina  
Opened: 2026-11-02  
Category: Ideas  
State at download: open, 0 comments, downloaded 2026-11-08

What I would want. A project-level record of what the principal sent out of the forge: which file, made from what, to whom, by which channel, and when. Each entry would be pinned to the commit that holds the file, so the exact content sent can always be recovered.

Why. A render is overwritten by the next /render, and its earlier content lives only in git history. After a few iterations of a response to stakeholders, I need to know which exact version went out and when. Today I would have to remember a commit hash or set a tag by hand. Neither says where the file went, and tags do not read as a log.

A possible shape. Offered as a sketch only, since the convention is yours to decide:
- sent.md in the project root, append-only, kind records: no version, no history companion, no ledger row.
- One line per sending: - YYYY-MM-DD | <file sent> | <made from: recipe and inputs at their versions, or the artefact's version> | commit <hash> | to: <recipient> | via: <channel> | <handle>
- Written by Claude only on the principal's word that something was sent, never inferred from a render or a publish.
- Born at the first sending, not scaffolded by /new-project.

Open questions for you.
- Should a sending also set a tag on the commit?
- Does an entry belong in the ledger, for example to flag that a render sent out has since gone stale?
