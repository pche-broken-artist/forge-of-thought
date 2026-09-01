---
description: First run after cloning the engine — fill CLAUDE.local.md by interview, set the session model (Fable), offer the per-host git identity configuration; never overwrites, runs no git operation
---

Prepare this instance of the forge (POS.1050). Run after cloning the
engine, before any other work. Two files in the engine — plus, on the
user's word, the git identity configuration outside it; the command
runs no git operation.

The conversation language is not configured yet on a true first run:
speak whatever language the user speaks to you.

1. **`CLAUDE.local.md`** at the engine root.
   - If it already exists: report briefly what it holds and do not
     touch it.
   - Otherwise copy `templates/CLAUDE.local.md` to the root and fill
     it by elicitation interview, one question at a time:
     - **Principal** — name and role (whose thinking is being forged);
     - **Conversation language** — the language the working
       conversation runs in (artefacts are always English, briefs
       verbatim);
     - **Git identities** — name and e-mail per git host the user
       will push to (e.g. github.com, a company host). May be left
       empty and added later; say so.
   - Keep the template's format; the file is gitignored and never
     committed.
   - Close the git-identities part with an offer (POS.1050,
     POS.0950): generate one `~/.gitconfig-<host>` file per identity
     (`[user]` name and email) and the matching
     `includeIf "hasconfig:remote.*.url:…"` block (both the https
     and the ssh URL form per host), and on the user's word write
     the files and append the block to the END of `~/.gitconfig` —
     read it first, never overwrite existing content; appended last,
     a matching host overrides a global `[user]` default. Declined:
     print the contents for the user to apply by hand. This is the
     one write outside the engine; it is a configuration text file,
     not a git operation. Requires git ≥ 2.36 — say so.
2. **`.claude/settings.local.json`**.
   - If it already exists: report the model it names and do not touch
     it.
   - Otherwise create it with `{ "model": "fable" }` and tell the
     user in one sentence: the session is set to Fable — the
     strongest available model, which the whole forge including the
     blind reviewers runs on — and it can be changed at any time with
     `/model` or by editing this file. A notice, not a question.
3. Finish by pointing at the next step from the Quickstart: start a
   new project with `/new-project <slug>`, or bring an existing one
   with `/import-project <git-url>`.
