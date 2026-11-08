# projects/

Every project of this instance lives here as a directory of its own,
`projects/<slug>/`, and is a git repository of its own, which the
engine does not track: nothing under this directory but this file
enters the engine's repository (CLAUDE.md, Persistence). A new project
is scaffolded by `/new-project <slug>`, an existing one brought in by
`/import-project <git-url>`. The forge's own project, the thinking
behind the engine, is one of them: `/import-project
https://github.com/pche-broken-artist/forge.git` clones it into
`projects/forge`; a user of the engine never needs it (POS.1980).
