# Commands

The commands of the forge, each with its arguments and its purpose in
a line; what a command does in full is its skill's
(`.claude/skills/<command>/SKILL.md`), and CLAUDE.md, Commands, names
this file and carries no table of its own.

| Command | Purpose |
|---|---|
| `/setup` | first run after cloning the engine: prepare the instance |
| `/new-project <slug>` | scaffold a project by kind: a thought project or a library |
| `/new-artefact <name>` | add a new kind of artefact to the forge |
| `/import-project <git-url>` | bring an existing project into `projects/` |
| `/forge [slug]` | the state map of a project |
| `/forge <state> [slug]` | iterate the target artefact through its definition |
| `/ingest [file] [slug] [--bundle name]` | store, register and index external input in sources/; bare = sweep sources/ |
| `/render <recipe> [slug]` | regenerate a render from its recipe |
| `/publish <recipe> [slug]` | make the designed file from a render, through a model |
| `/document [slug]` | generate the documentation of the engine or of a project into docs/ |
| `/recipe [genre] [slug]` | compose or iterate a render recipe by genre; bare = the genre roster |
| `/thread [text \| THR.NNNN] [slug]` | work the threads of a project: bare = the open threads, a text = the birth of a thread, an ID = that thread taken up |
| `/work [name] [slug]` | work a work product: its specification and its file; bare = the project's work products |
| `/critique [lens] [artefact] [slug]` | run a critic lens on the quality of the documents; bare = the lens roster |
| `/challenge [persona] [artefact] [slug]` | run a challenger persona against the substance; bare = the persona roster |
| `/research [--quick \| --deep [--engine <name>]] <topic> [slug]` | research a topic from a plan the principal confirms first, quick or deep; indexed |
| `/ledger [slug]` | state report from the ledger |
| `/history <ID> [slug]` | the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences |
| `/check [check] [slug]` | run a check on a project or on the engine; bare = the check roster |
| `/test [pytest arguments]` | run the engine's tests; the sum back, a red test as pytest printed it |
| `/save [slug] [-m "message"] [-F file] [--tag name] [--quick]` | save one repository, or every one with changes; `--quick` without the check |
| `/release [slug] [-m "message"] [--tag name] [--auto]` | release one repository from `main`; `--auto` runs through and stops only at a serious thing |
| `/pull [slug]` | look at the remote and, clean and behind, pull one repository or every one with an origin |
| `/end` | end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose |
| `/spinoff <project> <group> <slug>` | split a group into its own project |
| `/migrate [slug] [--comments \| --blocker]` | bring a project to the shape of a release that changed the shape of files; `--comments` replaces the skeletons' comments by the line that names the skeleton; `--blocker` brings a TBC's mark of blocking to the one wording |
| `/man [command \| method \| question]` | the forge's manual, read from its own definitions; a need in free words gets the way the forge has for it |
| `/manual …` | alias of `/man` |
