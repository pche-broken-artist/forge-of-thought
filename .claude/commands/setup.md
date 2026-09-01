---
description: First run after cloning the engine — fill CLAUDE.local.md by interview, set the session model (Fable); never overwrites, never touches git
---

Prepare this instance of the forge (POS.1050). Run after cloning the
engine, before any other work. Two files, nothing else; the command
never touches git.

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
