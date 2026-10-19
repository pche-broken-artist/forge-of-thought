---
id: THR.0370
concerns: intent
origin: Claude's synthesis
status: open
---

Mermaid diagrams in Word. `scripts/md2docx.py`
(SOL.0440) converts a render to Word through pandoc and leaves
Mermaid blocks as code. Agreed in the walkthrough of 2026-09-12 but
not built: the route would be `mermaid-cli` rendering each block to
PNG through headless Chrome before pandoc runs (a pandoc Lua
filter), installed by the user one-off like markitdown and pandoc —
never by the script, never `npx` fetching at run time, no online
service. Open: whether to take the dependency at all, and global
versus repository-local installation. The LLM route (a sibling of
`md2pptx.ps1` on the `document-skills:docx` skill) was set aside on
2026-09-12: it would end at a picture too, with less determinism.
On 2026-09-27 the principal took that route for another purpose,
the design of the document: it is the `claude` engine of
`md2docx.py` behind `/publish` (POS.0590, SOL.0440). Mermaid in
the plain file stands as it was.
Word to PDF is the recipient's, never the forge's (SOL.0440).
Deferred 2026-09-12 by the principal — "needs more thought"; opened
as a thread 2026-09-14 from the ledger.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
