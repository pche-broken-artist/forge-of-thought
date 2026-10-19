---
project: <slug>
kind: thought            # thought | library (POS.0960)
language: en             # language of the chain's artefacts (ISO 639-1);
                         # CLAUDE.md, prime directive 6
---

<!-- The project file (POS.1590): written once at the creation of a
project, by /new-project or by the migration, never by a round;
merged as text; read wherever the kind and the language of a project
are needed. A fixture project carries `fixture: true` (SOL.0830).
A project without this file is of the shape before the migration;
the one remedy is `/migrate` (scripts/forge-migrate.py): a command
reports the shape as a fact, a check as one finding with that fix,
and nothing else of the new shape is raised against it. This
comment is the one owner of that rule. -->
