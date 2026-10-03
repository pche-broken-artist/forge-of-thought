---
project: forge
type: research
topic: how a person who is not a developer gets to the forge and through its first hour, and what Claude Code's surfaces and comparable frameworks offer to lower that threshold
date: 2026-10-03
derived_from: 00-brief-next-gen.md v0.1, section "The threshold of entry"
status: immutable
---

# The threshold of entry for a non-developer

## Question

How does a person who is not a developer get to a tool of this kind
and through its first hour, and what do Claude Code's surfaces and
comparable frameworks offer today to lower that threshold?

Out of scope, by the caller's word: company administration, data,
security and cost; the structure of documentation beyond the
first-run path.

## How to read this note

Every page was fetched on 2026-10-03. Three marks are used:

- **[verified]** read at the source named, on that date. Where the
  fetch tool returned the page text itself, the wording is the
  page's; where it returned a summary made by a small model, the
  mark is **[verified, summarised]** and the wording may be the
  summariser's, not the page's.
- **[secondary]** taken from a search-result snippet or a third
  party's account, the primary page not opened.
- **[synthesis]** this note's own reasoning from the above and from
  the forge's files; not stated by any source.

The Claude Code documentation pages (code.claude.com, claude.com/docs)
came back as full text. The GitHub READMEs, the support article on
Cowork, the Nielsen Norman pages and the documentation sites of the
other frameworks came back summarised. None of the documentation pages
shows a publication date of its own; they are living pages, so the
date of the fetch is the only date there is. Version numbers quoted
inside them (Claude Code v2.1.2xx, Claude Desktop 1.49585.0) show
they are current.

## Key findings

### 1. Claude Code's surfaces today

**The terminal CLI.** [verified]
https://code.claude.com/docs/en/setup and
https://code.claude.com/docs/en/overview

- Native installer, one line per platform; on Windows
  `irm https://claude.ai/install.ps1 | iex` from PowerShell, or a
  CMD variant, or `winget install Anthropic.ClaudeCode`. No
  administrator rights needed.
- Node.js is not needed: the native install is a binary, and even
  the npm package "downloads a native binary that doesn't use your
  Node.js at runtime".
- Git is not needed on Windows: "Native Windows | Requires: None;
  Git for Windows is optional". Without it "Claude Code runs shell
  commands via the PowerShell tool"; with it Claude Code uses Git
  Bash for its Bash tool and has the PowerShell tool alongside. The
  PowerShell meant is the one built into Windows; PowerShell 7 is
  named only as an alternative when no shell is found.
- An account: "Claude Code requires a Pro, Max, Team, Enterprise,
  or Console account. The free claude.ai plan does not include
  Claude Code access."
- A session starts by opening a terminal in the folder and running
  `claude`.
- `claude doctor` exists: it "prints read-only installation and
  settings diagnostics without starting a session".
- Anthropic itself treats the terminal as a barrier: there is a
  "Terminal guide for new users"
  (https://code.claude.com/docs/en/terminal-guide) that explains
  how to open a terminal and paste a command, and its first note
  reads "Don't want to use the terminal? The Claude Code desktop
  app lets you skip the terminal entirely." Its troubleshooting
  list is a record of where newcomers stumble on the install: the
  install directory missing from PATH, being in CMD instead of
  PowerShell, the 32-bit PowerShell, a TLS error on old Windows, no
  shell found. [verified]

**The desktop app (Mac, Windows; Linux in beta).** [verified]
https://code.claude.com/docs/en/desktop-quickstart and
https://code.claude.com/docs/en/desktop

- A downloaded installer, sign-in, the **Code** tab. "The desktop
  app includes Claude Code, so you don't need to install Node.js or
  the CLI to use the Code tab." A paid plan is required.
- A session starts by choosing an environment (Local, Cloud, SSH,
  on Windows a WSL distribution) and clicking **Select folder**. No
  terminal is involved.
- The configuration of a cloned repository works as in the
  terminal: "Desktop and CLI read the same configuration files";
  "CLAUDE.md and `CLAUDE.local.md` files in your project are used
  by both"; "Hooks and skills defined in settings apply to both";
  permission rules of `settings.json` "apply to Desktop sessions".
  Skills are run by typing `/` or through **+ > Slash commands**;
  plugins have a plugin browser.
- Git: needed only for sessions isolated in a worktree. "On
  Windows, Claude Desktop versions before 1.49585.0 asked for Git
  before starting any local session"; newer ones do not.
- Limits against the CLI: no scripting (`--print`), no agent teams,
  third-party providers only by a separate route, and built-in
  commands that open a terminal panel "behave differently", for
  example `/permissions` replies that it "isn't available in this
  environment". On Windows "the app inherits user and system
  environment variables but does not read PowerShell profiles".
- The app also holds the **Chat** and **Cowork** tabs.

**The web and the cloud sessions.** [verified]
https://code.claude.com/docs/en/web-quickstart,
https://code.claude.com/docs/en/claude-code-on-the-web and
https://code.claude.com/docs/en/cloud-environments

- Nothing to install; claude.ai/code in a browser, or the Code tab
  of the mobile app. Pro, Max and Team plans, Enterprise with the
  right seats.
- "You'll need a GitHub repository to get started." "To start a new
  project, create an empty repository on GitHub first." "Repository
  cloning and pull request creation require GitHub"; a repository
  on another host can be sent only as a bundle from the terminal
  and "the session can't push results back to that remote".
- Each session is a fresh clone in a virtual machine. What is
  committed carries over: the repository's `CLAUDE.md`,
  `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, and
  "in a session with one repository" the hooks and permission rules
  of `.claude/settings.json`. What does not: anything in the user's
  `~/.claude`, and "Plugins and marketplaces declared in your
  repo's `.claude/settings.json`". A session with several
  repositories "starts above the clones and doesn't read them" for
  settings and hooks.
- The machine carries Python 3, Node, git, gh and more; PowerShell
  and pandoc are not in the list of installed tools. A setup script
  can install more.
- Each task works on a branch of its own that is pushed for review;
  the modes offered are Auto, Accept edits and Plan, "Cloud
  sessions don't offer Manual".

**IDE extensions.** [verified]
https://code.claude.com/docs/en/overview. VS Code and Cursor by an
extension; JetBrains by a plugin that "requires the Claude Code
CLI, installed separately". An IDE is itself a developer's tool, so
this surface lowers nothing for an analyst. [synthesis]

**Mobile and Remote Control.** [verified]
https://code.claude.com/docs/en/remote-control. Remote Control
steers a session that runs on the user's machine from claude.ai or
the mobile app; it needs the session started locally first, a paid
plan, and on Team and Enterprise an owner's toggle. It is a
convenience after the threshold, not a way over it. [synthesis]

**Dev containers and Codespaces.** [verified]
https://code.claude.com/docs/en/devcontainer. A documented feature
installs Claude Code into any dev container, GitHub Codespaces
included; the page is written for "every engineer on your team" and
its prerequisites are VS Code, Docker and the Dev Containers
extension, or a Codespace. Sign-in is repeated after a rebuild
unless a volume is mounted.

**The claim that binds them.** [verified, vendor claim] "Each
surface connects to the same underlying Claude Code engine, so your
repo's CLAUDE.md files, settings, and MCP servers work across all
of them." The cloud pages above qualify this claim in detail.

### 2. Anthropic's products for knowledge workers

**Cowork.** [verified] https://claude.com/docs/cowork/overview:
"Cowork uses the same agentic architecture that powers Claude Code,
accessible within Claude Desktop without opening the terminal";
"Claude reads and writes local files". It "loads the ones
[connectors, skills, plugins] enabled for your claude.ai account,
synced at session start, and doesn't read the Claude Code CLI's
`~/.claude` directory on your machine".

**Plugins across chat, Cowork and Claude Code.** [verified]
https://claude.com/docs/plugins/overview and
https://claude.com/docs/plugins/platform-support

- One plugin folder installs everywhere, from **Customize >
  Plugins**: from the directory, from a Git repository added as a
  marketplace (GitHub, GitHub Enterprise, public GitLab and
  Bitbucket), or by uploading a zip. "Each plugin is saved to your
  account, so it's also available in Cowork and Claude Code without
  installing it again." On Team and Enterprise plans an owner can
  set a plugin to available, installed by default or required.
- What each surface loads, from the support table:

| Component | Chat | Cowork | Claude Code |
|---|---|---|---|
| Skills | loads | loads | loads |
| Commands | loads as a skill | loads, `/plugin-name:command` | loads |
| Agents | ignored | loads | loads |
| Hooks | ignored | loads | loads |
| Executables in a top-level `bin/` | can't be installed | can't be installed | loads |
| LSP servers, output styles, themes, `settings` | ignored | ignored | loads |

- Limits: 5,000 files and 200 MB per plugin, 25 marketplaces a
  user adds himself.

**Skills in the chat apps.** [verified, summarised]
https://code.claude.com/docs/en/skills. Skills uploaded to
claude.ai may use only the fields of the open Agent Skills
specification: "`name`, `description`, `license`, `compatibility`,
`metadata`, `allowed-tools`"; "Claude Code accepts every field".
Fields the forge's skills use today, `disable-model-invocation` and
`argument-hint`, are Claude Code's own. Whether a plugin's skill
keeps those fields inside Cowork the pages do not say. [not found]

**Could the forge be delivered there?** [synthesis, on the verified
facts above and on this project's research note
`2026-08-29-claude-code-packaging.md`, not re-verified today]

- Carries over to Cowork as a plugin: the skills, the commands, the
  reviewer agents, the per-prompt hook.
- Does not carry over, or is not documented to: an always-on
  instruction file (the earlier note found that a `CLAUDE.md` at a
  plugin root is not loaded; whether Cowork reads a `CLAUDE.md`
  from the selected folder is asserted by third-party tutorials
  only [secondary], and the support article speaks of "folder
  instructions" [verified, summarised]); the permission deny rules
  of `settings` (ignored outside Claude Code); the scripts as
  executables on PATH; prompts for plugin options ("Cowork doesn't
  prompt for values"); and the working arrangement in which Claude
  Code is started at the engine root above nested project
  repositories.
- The pages disagree on where a Cowork task runs: the overview says
  on the user's computer, the support article
  (https://support.claude.com/en/articles/13345190-get-started-with-cowork,
  [verified, summarised]) speaks of "an isolated environment on
  Anthropic's servers", and the support table speaks of "a Cowork
  session that runs on your computer" as one case. Whether git,
  PowerShell and pandoc are reachable from a Cowork task was not
  found.
- In plain chat the forge cannot live: no agents, no hooks, no
  files of a project.

### 3. How comparable frameworks get a user started

All from the projects' own pages, [verified, summarised] unless
marked.

| Framework | Prerequisites | Steps to the first result | Guided first run |
|---|---|---|---|
| GitHub Spec Kit | "Python 3.11+, uv, and a supported AI coding agent"; Git optional | `uv tool install specify-cli`; `specify init <project> --integration <agent>`; open the agent in the folder; run the `/speckit-*` skills one at a time | none found; `specify version` verifies the install |
| BMAD Method | Node.js, npm and Git for the skills CLI, uv and Python for setup; its first-change guide says "a macOS or Linux shell with Node.js 20.12+, Python 3" | `npx skills add bmad-code-org/BMAD-METHOD`, or in Claude Code `/plugin marketplace add bmad-code-org/bmad-plugins`; ask the `bmad` skill to run `bmad setup`; invoke `bmad-build` | `bmad setup`, `bmad status` ("check versions and see what to run next"), and asking `bmad` what to do next |
| OpenSpec | "Node.js 20.19.0 or higher" | `npm install -g @fission-ai/openspec@latest`; `openspec init` in the project; `/opsx:explore` or `/opsx:propose` | `/opsx:onboard`: "an interactive tutorial using your actual codebase", walks one whole cycle with narration, "takes 15-30 minutes" |
| Superpowers | Claude Code (or another harness) | `/plugin install superpowers@claude-plugins-official`; nothing more | none needed: "Because the skills trigger automatically, you don't need to do anything special" |
| Agent OS | not found | not found: the installation page shows no steps without a sign-up | not found |

Sources: https://github.com/github/spec-kit and
https://github.github.io/spec-kit/installation.html;
https://github.com/bmad-code-org/BMAD-METHOD and
https://docs.bmad-method.org/start/build-your-first-change/;
https://github.com/Fission-AI/OpenSpec and its `docs/commands.md`;
https://github.com/obra/superpowers;
https://github.com/buildermethods/agent-os and
https://buildermethods.com/agent-os/installation.

What this shows. [synthesis]

- Every one of them is two or three steps from nothing to the
  first working command, and none asks the user to clone a
  repository: the tool comes to the user's folder, not the user to
  the tool's.
- The cheapest entry is the marketplace install: one line inside a
  session already running. Two of the five now offer it, and the
  desktop app offers the same by clicking (finding 1).
- A guided first run exists in two shapes: a status command that
  says what to run next (BMAD), and a narrated walk through one
  whole cycle on real material (OpenSpec). No sample or playground
  project shipped with a tool was found in any of the five.
- All five address developers. None claims a non-developer
  audience, and their prerequisites (Node, Python, uv) are a
  developer's. Nothing in this field was found that is built for
  analysts.
- What newcomers stumble on: one open search surfaced a Spec Kit
  issue of `specify init` hanging on Windows PowerShell 5.1 and a
  request to initialise inside an existing project [secondary, the
  issues not opened]. A systematic reading of the issue trackers
  was not done; this part of the question stays thin.
- BMAD's "web bundles", which earlier versions offered for use in a
  chat app, were not found on its current pages. [not found]

### 4. Lowering the threshold in practice

- **Marketplace install instead of a clone.** [verified]
  https://code.claude.com/docs/en/discover-plugins. In the
  terminal `/plugin install <name>@<marketplace>`, or one command
  that adds the marketplace and installs; in the desktop app
  **+ > Plugins > Add plugin**; from the shell
  `claude plugin install`, fit for a setup script. A marketplace is
  a git repository on any host. Updates arrive automatically where
  auto-update is on, which for a third-party marketplace it is not
  by default. A plugin enabled at project scope in a committed
  `.claude/settings.json` is turned on for collaborators but each
  still installs it once.
- **A doctor.** Claude Code has `claude doctor` for itself
  [verified]; Spec Kit has `specify version`, BMAD `bmad status`
  [verified, summarised]. A check of a framework's own
  prerequisites before the first run is common practice in
  developer tooling [synthesis; no source measured its effect].
- **A guided first run on a small real example.** OpenSpec's
  `/opsx:onboard` is the one clear instance found (finding 3).
- **Hiding git.** [verified, summarised]
  https://github.com/Vinzent03/obsidian-git: the Obsidian Git
  plugin offers "Automatic commit-and-sync (commit, pull, and push)
  on a schedule", yet "Some Git services may require further setup
  for HTTPS/SSH authentication" and on mobile it is "very
  unstable". GitHub Desktop
  (https://docs.github.com/en/desktop/overview/about-github-desktop)
  is "a graphical user interface that simplifies commands" for
  "beginning and advanced users". Claude Code's own terminal guide
  tells the newcomer who installs Git for Windows: "You won't need
  to learn Git yourself." [verified] The pattern in all three: the
  daily commit and sync can be hidden well; the one-off acts
  (creating the remote, authenticating to the host) and the rare
  accidents (a conflict) are where the tool hands git back to the
  user. [synthesis]
- **Who creates the repository and the remote.** In the cloud route
  the user must: "create an empty repository on GitHub first"
  [verified]. No surveyed tool creates a remote for the user. A
  repository with no remote, or no repository at all, is the only
  route found that needs no git host. [synthesis]
- **Zero install.** The cloud session is it, at the price of a
  GitHub account, a GitHub repository and the limits of finding 1.
  A Codespace is a second route with a developer's prerequisites.
- **Removing interpreter prerequisites.** Claude Code needs neither
  Node nor git nor PowerShell 7 on Windows [verified]. Whatever a
  framework's own scripts need is therefore the whole of the added
  burden. [synthesis]

### 5. Research and practice on onboarding non-developers

This part of the evidence is the weakest; little of it is about
agentic tools.

- **Progressive disclosure.** [verified, summarised]
  https://www.nngroup.com/articles/progressive-disclosure/ (Nielsen,
  2006-12-03): "Initially, show users only a few of the most
  important options. Offer a larger set of specialized options upon
  request." Status: consensus in interface design for decades.
- **Training wheels.** [verified, summarised]
  https://www.nngroup.com/articles/training-wheels-user-interface/
  (Nielsen, 2006-12-04, reporting Carroll's studies of the 1980s):
  novices limited at first to a few features were "26% faster" and
  "21% faster" on tasks, learned more, and later did better on the
  advanced features too. Status: an old, replicated laboratory
  finding on a word processor; its transfer to a command-driven
  agent is this note's assumption, not a result.
- **Command lines and novices.** [secondary] A 1984 study in
  Communications of the ACM, "Building a user-derived interface",
  reported that the first version of a command interface recognised
  7 percent of the commands novices produced spontaneously and the
  final one 76 percent, after the system was adapted to what they
  typed. Its relevance: a model that understands plain requests
  removes much of the classic barrier of command syntax, so that
  what remains is the terminal around it. [synthesis]
- **Learning by a worked example.** No source on agentic tools was
  found. The practice is visible in OpenSpec's onboarding and in
  Anthropic's quickstarts, which all walk one small real task.
  Status: emerging practice, unmeasured.
- **Time to first value and where people give up.** Only marketing
  pages were found, with figures such as retention gains when value
  arrives within minutes; none names a study. [secondary, vendor
  and marketing claims, not to be relied on]. That shortening the
  path to the first useful result matters is consensus among
  practitioners; the numbers are not evidence.
- **The terminal as a barrier.** Anthropic's own documentation is
  the best evidence found: a guide for people who have never opened
  a terminal, and a desktop app presented as the way to skip it
  [verified]. Third-party guides "for non-coders" say that people
  give up at the terminal and that it is easier than feared
  [secondary, anecdote]. Anthropic's accounts of its own legal and
  marketing teams using Claude Code are vendor claims, seen in
  search results only [secondary]. Status: that the terminal is a
  barrier is consensus; how high it is with an agent inside it is
  contested and unmeasured.

## The forge's threshold today

Counted from `README.md` (Quickstart, Setup),
`.claude/skills/setup/SKILL.md`, `.claude/skills/new-project/SKILL.md`,
`.claude/settings.json` and CLAUDE.md, Persistence. [verified in the
files; the counting is synthesis]

**Prerequisites: four always, four for some functions, one for
saving to a host.**

1. A paid Claude plan.
2. git.
3. PowerShell 7 (`pwsh`). The per-prompt hook of
   `.claude/settings.json` calls `pwsh` at every prompt, so this is
   needed from the first message, not only for the scripts.
4. Claude Code.
5. For `/ingest` of binaries: Python 3 and markitdown.
6. For the plain Word and PowerPoint files: pandoc.
7. For `/publish`: the `document-skills` plugin, installed by two
   commands in a session.
8. For saving beyond the machine: an account on a git host, a
   repository created there by hand, and credentials that let git
   push.

Of these, Claude Code itself demands only the plan. Everything else
is the forge's own addition.

**Steps to the first useful result (the first question of
`/forge intent`): about eleven, nine of them before any thinking.**

1. Install git.
2. Install PowerShell 7.
3. Open a terminal.
4. Install Claude Code by a pasted command.
5. `git clone` the engine.
6. Change into the engine root and run `claude` ("always from the
   engine root").
7. Sign in through the browser.
8. `/setup`: an interview on language and principal, then the git
   hosts with a name and an e-mail for each, an offer to write
   `includeIf` stanzas and a guard into the global git
   configuration, and a notice on the model.
9. `/new-project <slug>`: kind, language, the brief pasted or
   dictated, the question whether it is finished.
10. Outside the session, since Claude is denied git:
    `git -C projects/<slug> init -b main`, then a remote created on
    a host and added by hand. May be skipped; the project is then
    "not under git" and `/save` has nothing to save it to.
11. `/forge intent`.

**What the person must already be able to do.** Open a terminal and
move between folders; know what a clone, a repository, a remote, a
commit identity and a push credential are; read and consent to an
edit of `~/.gitconfig`; type slash commands with arguments; keep to
one folder as the place Claude Code is started from. An analyst can
do the last two; the rest is a developer's knowledge.

## Options with trade-offs

**A. Keep the clone; add a doctor, a guided first run and a sample
project.**
For: no change of architecture; the forge's layout, CLAUDE.md, hook
and deny rules stay as they are; each piece has a precedent
(`claude doctor`, `bmad status`, `/opsx:onboard`). A bootstrap
script could check and name what is missing before the first
session. A sample project gives a worked example, which none of the
surveyed frameworks ships.
Against: every prerequisite and the clone remain; the doctor tells
the user what he lacks but he still installs it; steps 1 to 7 are
untouched unless combined with C.

**B. Deliver the engine as a plugin.**
For: the lowest entry found anywhere, one line or a few clicks, no
clone, no git for the install; versioned updates; one package
reaches Claude Code, the desktop app and Cowork; an organisation
can set it installed by default or required.
Against: a plugin does not load a CLAUDE.md, so the always-on core
needs another carrier (the earlier research note names three); the
deny rules in `settings` reach Claude Code only; `bin/` executables
make a plugin uninstallable in chat and Cowork; `projects/forge`
and the templates would need a new home; auto-update is off by
default for a third-party marketplace; cloud sessions do not load
plugins at all. This is the engine split under another name, not an
onboarding fix.

**C. Support the desktop app's Code tab as the default surface.**
For: removes the terminal, the pasted install command and the PATH
troubles; a normal installer; the engine folder is picked by
clicking; CLAUDE.md, CLAUDE.local.md, hooks, skills and permission
rules are documented to work as in the CLI; slash commands are
browsable from a menu, a form of progressive disclosure for free;
no change to the engine.
Against: the clone, git and PowerShell 7 remain, because the forge
needs them, not Claude Code; some built-in terminal commands behave
differently; the forge has not been run there, and the hook's
`pwsh` and the scripts' PATH under the app's inherited environment
are unverified; a Windows on ARM or Linux user has a narrower
route.

**D. A zero-install cloud route.**
For: a browser and a plan are the whole of the machine side.
Against: GitHub is mandatory, account and repository; the session
is one fresh clone, so the engine with its separate project
repositories inside does not map onto it; CLAUDE.local.md is
gitignored and so absent; PowerShell and pandoc are not on the
machine; work lands on a branch per task, not on `main`; the
permission mode Manual, on which step-by-step consent leans, is not
offered. It trades the terminal for GitHub and a different model of
work.

**E. Hide the creation of the project repository.**
For: removes step 10 and with it the one moment the user must type
git by hand; the daily side is hidden already behind `/save`.
Against: the forge's rule that initialising a repository and adding
a remote are the user's own act would change; creating a remote
needs a host, an account and a credential, which no surveyed tool
does for the user; a local repository without a remote is the only
part that can be hidden cheaply, and it protects history, not the
machine's loss.

## Relevance to this project

For the draft brief `00-brief-next-gen.md`, section "The threshold
of entry", and for the open question in its aim, who the target
user is.

**Recommendation.** Take C and A together first, the local half of
E with them, and leave B to the question of the engine's shape and
D aside.

1. Try the desktop app's Code tab on the engine as it stands, on a
   machine of a person who is not a developer, and write down what
   breaks. It is the only option that removes the terminal without
   touching the architecture, the vendor documents it as the route
   for exactly these people, and the test costs an afternoon. Until
   it is run, that the hook and the scripts behave there is this
   note's expectation, not a fact.
2. Treat the forge's own prerequisites as the real threshold. Claude
   Code on Windows asks for nothing but a plan; git, PowerShell 7,
   Python, markitdown and pandoc are all the forge's. PowerShell 7
   is needed at the first prompt only because of the hook. The
   planned rewrite of the scripts to Python would exchange one
   interpreter a Windows machine lacks for another it lacks, so it
   lowers nothing by itself; that is worth saying when POS.0830 is
   next touched.
3. Give the first hour a shape: a check of prerequisites that names
   what is missing and how to get it, a `/setup` that defers the git
   identity until the first save instead of opening with it, and one
   small worked project the newcomer walks through. The precedents
   are `claude doctor`, `bmad status` and `/opsx:onboard`; a shipped
   sample project would be the forge's own addition.
4. Let a project be born with a local repository on the user's
   word, through a script, and leave the remote for later. It
   removes the hand-typed git from the first hour and keeps "not
   under git" a property.
5. Decide the plugin with the brief's question of the shape of the
   whole, not here. As a means of entry it is the best there is; as
   a change it is the engine split, with the always-on core and the
   deny rules as its open problems. If Cowork is where analysts
   already are, the plugin is also the only way to them, and what
   would not carry over there is listed in finding 2.
6. Do not build on the cloud route now. It fits a repository of
   code worked task by task, not an engine with projects inside it
   and a conversation that waits for the principal's word.

**What stays uncertain.** Whether the forge runs in the desktop app
without change. What Cowork does with a CLAUDE.md in the selected
folder, where its tasks run, and whether a plugin's skills keep
Claude Code's own front-matter fields there. Agent OS's install
path. What the issue trackers of the surveyed frameworks say about
newcomers. Any measured result on non-developers and agentic tools:
none was found, and the old laboratory findings are applied here by
analogy. All product facts above are of 2026-10-03 and of a product
that changes weekly.
