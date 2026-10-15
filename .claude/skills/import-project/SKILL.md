---
description: Bring an existing project into projects/ — clone through scripts/forge-clone.py, which reports the commit identity git resolves
argument-hint: "<git-url>"
disable-model-invocation: true
---

Bring the project at `$0` into the forge (POS.1060). Git is done by
`scripts/forge-clone.py` only (CLAUDE.md, Persistence).

1. Require the URL. The target directory is
   `projects/<repository name>` — the name falls out of the URL (no
   slug parameter); if the directory already exists, stop and report.
2. On the principal's word run `python scripts/forge-clone.py <url>`. The
   commit identity is git's, resolved per host from his own
   configuration (CLAUDE.md, Persistence); the script sets none and
   reports the one the clone resolves.
3. Relay the script's facts: the last commit, the origin, the
   identity git resolves, and whether the project carries a ledger
   with a `kind:` header (its absence: `templates/ledger.md`, header).
   When git resolves no identity, say in plain words what that means
   and what to do: git has no name and e-mail to sign commits on this
   host — the login that cloned the repository is a different thing —
   and `forge-save` commits nothing until git resolves one. The usual
   causes: no per-host rule in the user's git configuration, or a rule
   whose identity file git cannot find from this place (a `~` path, or
   a file beside a global file, under a HOME that differs by place).
   The two ways out, both the user's and outside the engine: the
   identity step of `/setup` with absolute paths, or a local identity
   in the repository (`git -C projects/<name> config user.name` and
   `user.email`). The forge writes none.
4. Finish by recommending `/forge <slug>` as the first act of work:
   the engine does not track the project and cannot guess it, so the
   project is selected by naming it.

Nothing is written into the imported project by this command.
