---
date: 2026-11-01
project: forge
topic: what code of conduct a small one-author project on GitHub adopts
status: immutable
engine: claude
model: claude-fable-5-1
usage: —
run: tmp/research/2026-11-01-code-of-conduct-on-github/card-1
derived_from: the principal's word of 2026-11-01 (a quick research of one card, no plan file); web sources below
---

# A small project on GitHub adopts the Contributor Covenant, and the three neighbours do so unevenly

## In short

The Contributor Covenant is the standard text, and its steward, the
Organization for Ethical Source, now presents version 3.0 as the
latest, announced on 2025-07-28 and licensed CC BY-SA 4.0; it is a
rewrite with two editor notes to fill, the means of reporting and the
enforcement policy, and no e-mail placeholder [1][2][4]. The version a
reader assumes, 2.1 with `[INSERT CONTACT METHOD]`, is still served
on the standard's site but no longer the latest [3]. GitHub's wizard
offers the Contributor Covenant too, but the text it hands out is
version 2.0 [6], and GitHub's documentation looks for the file at
`.github/`, the root, then `docs/` [5]; Open Source Guides says root
`CODE_OF_CONDUCT`, linked from CONTRIBUTING or README [7]. The three
neighbours are not a model: spec-kit carries version 1.4 with a
generic organisational e-mail [8], BMAD-METHOD version 2.0 in
`.github/` with a Discord server as contact [11], OpenSpec none at all
[12][13]. The disconfirming query found no reliable source advising a
one-person project against a code of conduct; only forum opinion
surfaced in search results, none opened. The one unexpected thing:
the current standard text is share-alike (CC BY-SA 4.0), which a CC
BY 4.0 repository would carry as a file under another licence [1].

## Question

#### Card 1: what code of conduct a small project on GitHub adopts
- **Question:** what does a small open-source project of a single
  author on GitHub adopt today as its code of conduct: which standard
  text (the Contributor Covenant, in which current version), what is
  filled into it (the contact for reports, the scope), where the file
  stands, and how do frameworks comparable to the forge
  (github/spec-kit, Fission-AI/OpenSpec, bmad-code-org/BMAD-METHOD)
  adopt it; against the alternative of a short text of one's own.
- **Why it matters:** the code of conduct is to be adopted, not
  composed; the research must return the text to adopt and what to
  fill in.
- **What would answer it:** the standard's text and its version from
  the standard's own page, and the neighbours' files read at source.
- **Where to look:** contributor-covenant.org; GitHub's documentation
  on adding a code of conduct (what its wizard offers); the
  repositories of the three neighbours; Open Source Guides
  (opensource.guide).
- **Disconfirming query:** whether a code of conduct is advised
  against, or seen as empty, for a project of one person, and what
  projects that refused one say; expected: adopting the Contributor
  Covenant is the norm and GitHub's wizard offers it.
- **Stop rule:** the standard's text found at source with its version
  and the neighbours read; about ten openings.

The baseline the note must beat: what a reader already assumes, that
the Contributor Covenant is the standard, adopted as it is, with an
e-mail address filled in. The note beats it on three points: the
current version is 3.0, not 2.1; 3.0 asks for a means of reporting
and an enforcement policy, not an e-mail; and the version GitHub's
wizard inserts is neither.

## Key findings

F1. **The current Contributor Covenant is version 3.0, stewarded by
the Organization for Ethical Source and licensed CC BY-SA 4.0.**
[consensus; standard, read at the standard's own site] The standard's
site links "Latest Version" to `/version/3/0` [2]; the 3.0 page is
titled "Contributor Covenant 3.0 Code of Conduct" and closes with
"This Code of Conduct is adapted from the Contributor Covenant,
version 3.0, permanently available at
https://www.contributor-covenant.org/version/3/0/" and "Contributor
Covenant is stewarded by the Organization for Ethical Source and
licensed under CC BY-SA 4.0" [1]. The steward's announcement is dated
2025-07-28 and calls it "a major rewrite of the flagship code of
conduct" [4]. The 3.0 page itself carries no date beyond the site's
copyright year [1].

F2. **Version 3.0 has two things to fill in, marked `[NOTE`, and no
e-mail placeholder.** [single source; standard text] The Reporting
section reads "To report a possible violation, [NOTE: describe your
means of reporting here.]"; the enforcement section opens with a note
that its remedies "are suggestions based on best practices" and asks
the adopter, where a process of its own exists, to "edit this section
to describe your own policies"; the page says "You can find the
placeholders by searching the text for `[NOTE`" [1]. The sections are
Our Pledge, Encouraged Behaviors, Restricted Behaviors (with Other
Restrictions), Reporting an Issue, Addressing and Repairing Harm (a
ladder of Warning, Temporarily Limited Activities, Temporary
Suspension, Permanent Ban), Scope, Attribution [1]. The home page
describes a builder of four steps: choose a language from over 40
translations, provide the reporting details, describe the
enforcement policy or use the recommendations, download [2].

F3. **The scope of the standard text needs nothing filled in.**
[consensus across versions; standard text] 3.0: "This Code of Conduct
applies within all community spaces" and "also applies when an
individual is officially representing the community in public or
other spaces", with an official e-mail address, an official social
media account and an appointed representative at an event as the
examples [1]. 2.1 and 2.0 say the same with "in public spaces" [3][6].
No version read asks the adopter to name the spaces.

F4. **Version 2.1 is still served, with `[INSERT CONTACT METHOD]` in
its Enforcement section.** [consensus; standard text] The 2.1 page's
attribution reads "adapted from the Contributor Covenant, version
2.1, available at" the 2.1 URL; the placeholder stands in the
sentence beginning "Instances of abusive, harassing, or otherwise
unacceptable behavior may be reported to the community leaders
responsible for enforcement at" [3]. The 2.1 page names no licence in
its attribution [3]; what licence 2.1 carries was not verified here.
The 3.0 announcement does not say whether 2.1 is superseded or how to
upgrade [4].

F5. **GitHub's wizard offers the Contributor Covenant, but the text
it inserts is version 2.0.** [single source; vendor's own
documentation and API, primary] GitHub's documentation describes the
flow: Add file, Create new file, name it `CODE_OF_CONDUCT.md`, "Choose
a code of conduct template", pick one on the left, "complete the
fields to populate the selected code of conduct with the appropriate
information" on the right, review, commit; the page says GitHub
provides "templates for common codes of conduct" without naming them
or their versions [5]. GitHub's REST record of the template
`contributor_covenant`, name "Contributor Covenant", carries a body
whose attribution reads "adapted from the [Contributor
Covenant][homepage], version 2.0" with the 2.0 URL and the
placeholder `[INSERT CONTACT METHOD]` [6]. So the wizard's version
lags the standard by two releases as of 2026-11-01.

F6. **The file stands as `CODE_OF_CONDUCT.md` at the root, in
`.github/` or in `docs/`; GitHub takes the first found, in that
order.** [consensus; vendor documentation and practitioner guide]
GitHub checks `.github`, then the root, then `docs`, and "uses the
first file it finds" [5]. Open Source Guides says to put it in a file
named CODE_OF_CONDUCT in the project root and link it from the
CONTRIBUTING or README file [7]. The community profile marks "Code of
conduct" as added when the file is not empty and does not say the
project has none [5]; a text of one's own therefore counts, though
the REST profile's `code_of_conduct` key names only a recognised
template (F8 shows `contributor_covenant` for two neighbours).

F7. **Open Source Guides advises adopting early, deciding where it
applies, who enforces and how to report, and giving a private
reporting channel with a named recipient.** [consensus; practitioner
guide published by GitHub] "Try to establish a code of conduct as
early as possible"; it should say where it applies, to whom, what
happens after a violation and how to report one; it names the
Contributor Covenant as used by "over 40,000 open source projects",
beside the Django and Citizen codes; provide a private method such as
an e-mail address and say who receives reports, a maintainer, a group
or a working group, with an alternative channel where a report may
concern a recipient [7]. The standard's own site says "adopted by
thousands of communities, including 9 of the 10 largest open source
projects in the world" [2]; the two counts are of different kinds and
neither is dated.

F8. **The three neighbours adopt it unevenly: 1.4 with a generic
e-mail, 2.0 with a Discord server in `.github/`, and none.** [consensus
of primaries; the files and GitHub's profile records read at source]
- github/spec-kit: community profile 100 per cent, `code_of_conduct`
  key `contributor_covenant`, file `CODE_OF_CONDUCT.md` at the root
  [9]; the file's attribution says "adapted from the Contributor
  Covenant, version 1.4" and its contact sentence reads "Instances of
  abusive, harassing, or otherwise unacceptable behavior may be
  reported by contacting the project team at
  <opensource@github.com>", an organisation-wide address, not a
  project one [8]. Beyond attribution and contact the file was not
  compared with the 1.4 text at source.
- bmad-code-org/BMAD-METHOD: profile 87 per cent, key
  `contributor_covenant`, file at `.github/CODE_OF_CONDUCT.md` [10];
  attribution "version 2.0"; the contact sentence ends "at the
  official BMAD Discord server (<https://discord.com/invite/...>) - DM
  a moderator or flag a post"; no custom sections found [11].
- Fission-AI/OpenSpec: profile 75 per cent, `code_of_conduct` null and
  `code_of_conduct_file` null [12]; its CONTRIBUTING mentions no
  conduct, harassment or respect and names no contact beyond issue
  forms and a MAINTAINERS.md [13].
None of the three carries the current 3.0, and none fills in an
individual's e-mail: the contacts are an organisation address and a
chat server.

F9. **Attribution is a condition of adoption.** [consensus; vendor
documentation and standard] GitHub: when using a code of conduct
written by another person or organisation, "follow any attribution
guidelines from the source" [5]; the 3.0 text's attribution paragraph
with the permanent URL and the CC BY-SA 4.0 line is that guideline
[1].

## Unexpected

The card assumes one standard text adopted as it is; [1] shows that
3.0 is a template with an enforcement section the adopter is invited
to edit, so "adopted as it is" means keeping the suggested ladder and
filling one sentence of reporting. The 3.0 text is CC BY-SA 4.0 [1];
a repository published under CC BY 4.0 would hold one file under a
share-alike licence, which is lawful for a separate file but worth
one line in the repository's licensing, since the forge's whole is
said to be CC BY 4.0. This is the agent's own reading of the licence
line, not a source's.

GitHub's wizard and the neighbours lag the standard by one to three
versions [6][8][11]; the lag shows that adopting means picking a
version by hand from the standard's site, not trusting the wizard,
and that the version most readers have seen in the wild is not the
latest.

## Not found

- No reliable source advising a one-person project against a code of
  conduct, nor a project that refused one with reasons stated: the
  disconfirming search returned a 2022 forum thread and single
  projects' files, none opened, nothing citable (Search record).
- The licence of version 2.1: its page's attribution names none [3];
  not looked for elsewhere.
- A release date on the 3.0 page itself [1]; only the announcement
  carries one [4].
- Which fields GitHub's wizard asks for beyond the text: the
  documentation says "complete the fields" without naming them [5];
  the template body shows the one placeholder [6].
- The default branch of OpenSpec and BMAD was not confirmed; the
  profile records point at `main` for the files they list [10][12].

## Options

A. **Adopt Contributor Covenant 3.0 as it stands, filling the
reporting sentence and keeping the suggested enforcement ladder.**
Current, translatable, the steward's own recommendation [1][2][4].
Costs: a file under CC BY-SA 4.0 in a CC BY 4.0 repository (Unexpected);
the reporting sentence must name a private means, and a GitHub
profile offers no private message, so the sentence has to say what
the private channel is.

B. **Adopt 2.1 with `[INSERT CONTACT METHOD]` filled.** The text most
readers know, e-mail-shaped placeholder [3]; no longer the latest,
and its licence was not verified here (Not found).

C. **Use GitHub's wizard.** One click and the community profile
credit [5], but the text is 2.0 [6], two releases behind.

D. **A short text of one's own.** Counts in the community profile if
not empty [5], no share-alike licence, no attribution; against it,
every source read treats the standard as the norm [2][7] and the
one-author neighbours that have a file adopted the standard rather
than composing [8][11]; a text of one's own also carries no
translations and no enforcement ladder tested elsewhere.

E. **None, as OpenSpec does** [12]. Nothing read advises it; nothing
reliable read advises against it either (Not found).

## Relevance to this project

The agent's recommendation, its own: option A, the 3.0 text copied
from the standard's page word for word, as `CODE_OF_CONDUCT.md` at
the repository root beside README, CONTRIBUTING, RELEASE-NOTES and
LICENSE, where GitHub finds it second after `.github/` [5] and where
Open Source Guides puts it [7], linked from CONTRIBUTING and README
[7]. Two sentences to fill: the reporting note, pointing to the same
private contact CONTRIBUTING names, said as a means ("a private
message to the maintainer through ...") rather than an address,
since 3.0 asks for a means [1]; the enforcement note removed, keeping
the suggested ladder, which is what "adopted, not composed" means for
3.0. The attribution paragraph stays as the standard prints it [1][9].
Chosen against B because the standard's site no longer presents 2.1
as latest [2]; against C because the wizard's 2.0 is older still [6];
against D because every read source treats the standard as the norm
and a one-author project gains nothing by composing [2][7][8][11].

Fixed text, not a generated render, is the agent's inference: the
file is an adopted standard whose worth lies in being word for word
the standard's, with one filled sentence; a recipe would regenerate
text that must not vary, and the one variable, the contact, already
lives in CONTRIBUTING. If the contact is to stay in one place, the
reporting sentence can point at CONTRIBUTING rather than repeat it.
One line in the repository's licensing that this file is CC BY-SA 4.0
of the Organization for Ethical Source closes the licence point
(Unexpected).

Consult when: the code of conduct is adopted or its version bumped;
the private contact in CONTRIBUTING changes; the repository's
licensing is restated; a neighbour's conventions are compared again.

## Sources

Every page below was opened through a fetch that returns a model's
answer to a prompt over the page, with verbatim passages requested;
the quotes are as that fetch returned them, and each entry says
"summarised fetch" for that reason.

[1] Contributor Covenant 3.0 Code of Conduct. Organization for
Ethical Source. Undated (site footer © 2026).
https://www.contributor-covenant.org/version/3/0/code_of_conduct/
Primary (the standard's own text). Summarised fetch, whole page,
verbatim passages requested. Original.

[2] Contributor Covenant home page. Organization for Ethical Source.
Undated (footer © 2026). https://www.contributor-covenant.org/
Primary. Summarised fetch, whole page. Original.

[3] Contributor Covenant Code of Conduct, version 2.1. Organization
for Ethical Source. Undated.
https://www.contributor-covenant.org/version/2/1/code_of_conduct/
Primary. Summarised fetch, whole page. Original.

[4] Contributor Covenant 3.0 announcement. Organization for Ethical
Source (press release, no individual author). 2025-07-28, byline.
https://ethicalsource.dev/blog/contributor-covenant-3
Primary (the steward's own announcement). Summarised fetch, whole
page. Original.

[5] Adding a code of conduct to your project. GitHub Docs. Undated.
https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
Primary (vendor's documentation of its own product). Summarised
fetch, whole page. Original.

[6] GitHub REST API, code of conduct template `contributor_covenant`.
GitHub. Undated.
https://api.github.com/codes_of_conduct/contributor_covenant
Primary (the vendor's own template record with its body). Summarised
fetch, the key, name and body fields. Original.

[7] Your Code of Conduct. Open Source Guides (github/opensource.guide).
Undated. https://opensource.guide/code-of-conduct/
Secondary (practitioner guide). Summarised fetch, whole page.
Original.

[8] CODE_OF_CONDUCT.md of github/spec-kit, branch main. GitHub
(organisation). Undated.
https://raw.githubusercontent.com/github/spec-kit/main/CODE_OF_CONDUCT.md
Primary (the neighbour's file). Summarised fetch, whole file;
attribution and contact verbatim, the rest not compared with 1.4 at
source. Original.

[9] Community profile of github/spec-kit. GitHub REST API. Read
2026-11-01, undated record.
https://api.github.com/repos/github/spec-kit/community/profile
Primary. Summarised fetch, the files object. Original.

[10] Community profile of bmad-code-org/BMAD-METHOD. GitHub REST API.
Read 2026-11-01, undated record.
https://api.github.com/repos/bmad-code-org/BMAD-METHOD/community/profile
Primary. Summarised fetch, the files object. Original.

[11] .github/CODE_OF_CONDUCT.md of bmad-code-org/BMAD-METHOD, branch
main. Undated.
https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/.github/CODE_OF_CONDUCT.md
Primary (the neighbour's file). Summarised fetch, whole file.
Original.

[12] Community profile of Fission-AI/OpenSpec. GitHub REST API. Read
2026-11-01, undated record.
https://api.github.com/repos/Fission-AI/OpenSpec/community/profile
Primary. Summarised fetch, the files object. Original.

[13] CONTRIBUTING.md of Fission-AI/OpenSpec, branch main. Undated.
https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/CONTRIBUTING.md
Primary (the neighbour's file). Summarised fetch, whole file.
Original.

## Opened and not used

- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/CODE_OF_CONDUCT.md
  - 404; the absence confirmed through [12] instead.
- https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/CODE_OF_CONDUCT.md
  - 404; the file stands in `.github/`, found through [10], read as
  [11].

## Search record

Queries, in order: "Contributor Covenant current version"; "GitHub
docs adding a code of conduct to your project"; "code of conduct
pointless for single maintainer open source project" (the
disconfirming query); "opensource.guide code of conduct";
GitHub "Choose a code of conduct template" Contributor Covenant 2.1
Citizen Code of Conduct wizard.

Openings, fifteen: [1], [2], [5], [7], [8], OpenSpec root file (404),
BMAD root file (404), [12], [10], [9], [3], [4], [6], [11], [13].

The disconfirming query returned a 2022 forum thread in which one
commenter calls codes of conduct administrative noise on small
projects and another calls them overreaching, and a few one-author
projects' files that adopt a first-person text with a contact; none
of these was opened, so none is cited, and no reliable source against
a code of conduct for a one-person project was found. The search for
the wizard's templates returned only older enterprise snapshots of
GitHub's API, not opened; the live API record [6] was opened instead.

The run ended on the opening budget, at fifteen, with the stop rule's
first part also met: the standard's text was read at source with its
version, and all three neighbours were read at source. What remains
unopened is listed under Not found.
