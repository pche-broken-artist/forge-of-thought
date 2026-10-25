---
date: 2026-10-25
project: forge
topic: a Markdown deck shown in the browser from a GitHub repository, and whether a Marp-class tool fits the forge
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-25-a-markdown-deck-in-the-browser-from-github/deck-in-the-browser
derived_from: the principal's word of 2026-10-25 (a quick research: how a deck of the forge is shown on GitHub without a download, and whether Marp or a tool of its class would serve the forge); the card as confirmed in the conversation, no plan file (quick research, one card, one engine); .claude/skills/research/SKILL.md; no known notes named; web sources below
---

# A deck in a GitHub repository is shown in the browser as a PDF in the file viewer or as a static HTML deck under GitHub Pages, and pandoc already writes that HTML deck from the Markdown it writes `.pptx` from

## In short

GitHub's own file viewer renders PDF (links inside it ignored),
images, Markdown and a short list of other kinds; its documentation
names no Office format, so a `.pptx` in a repository has no
documented browser form of its own [1]. GitHub Pages serves static
HTML, CSS and JavaScript [3], which gives two more forms: a PDF put
under Pages, and an HTML deck under Pages. Pandoc, which the
pipeline already has, writes an HTML deck (reveal.js, Slidy, S5,
DZSlides, Slideous) from the same Markdown and with the same
`::: notes` speaker notes it writes `.pptx` from; a single
`--self-contained` file is one option away [6]. The Marp class
(Marp, Slidev, Quarto) brings the same forms: a static HTML deck, a
PDF, images per slide, and a `.pptx`; but Marp's and Slidev's
`.pptx` is pre-rendered images of slides by design, their editable
variants experimental or image-free only at a cost, and every form
but HTML needs a Chromium-class browser in the pipeline
[4][5][9]. The disconfirming query found no GitHub statement that
`.pptx` is rendered and no Marp statement that its `.pptx` is
editable shapes by default; it strengthened the expectation rather
than overturned it. Confidence: high on what each vendor documents,
moderate on the loss comparison where a vendor is silent (fonts,
links in HTML decks), and GitHub's silence on `.pptx` is absence
of a statement, not a statement of absence.

## Question

#### Card 1: a Markdown deck shown in the browser from a GitHub repository, and whether a Marp-class tool fits the forge
- **Question:** How is a slide deck, kept in a GitHub repository, shown to a visitor in the browser without downloading a file, in which forms (a `.pptx` or `.pdf` rendered by GitHub's own file viewer, a PDF under GitHub Pages, an HTML deck under GitHub Pages, a deck image per slide), with what each form loses (animation, notes, fonts, search, links) and what it needs in the pipeline; and whether a Markdown-to-slides tool of the Marp class (Marp, reveal.js, Slidev, Quarto revealjs, pandoc's own HTML slide writers) adds a form the forge lacks against the pipeline it has today: a Markdown render, `pandoc` to `.pptx` through a `.potx` template, a model for the designed file, and a browser player of timed terminal events served from `docs/videos/` on GitHub Pages.
- **Why it matters:** two decks of the forge (an introduction for analysts, an executive pitch) exist only as `.pptx`; the principal wants to decide whether they get a browser form, by which mechanism, and whether a new tool earns its place beside pandoc and the existing player.
- **What would answer it:** the documented behaviour of each mechanism, from the vendor's own documentation and GitHub's documentation (primary); a comparison that names what each form drops.
- **Where to look:** GitHub Docs (rendering of `.pdf` and Office files in the file viewer, GitHub Pages limits), Marp's documentation (Marp CLI, outputs `html`, `pdf`, `pptx`, themes, GitHub Action), reveal.js and Slidev documentation, pandoc's manual (slide output formats, `--to revealjs`, `--to pptx` from one source), Quarto's revealjs documentation; the known item that must turn up: pandoc already writes HTML slide decks from the same Markdown it writes `.pptx` from.
- **Disconfirming query:** "GitHub does not render pptx" / "pptx preview GitHub removed", and "Marp pptx export limitations editable text": expected is that GitHub previews `.pdf` but shows `.pptx` only as a download, and that Marp's `.pptx` is images of slides, not editable shapes; the query is written to find the opposite.
- **Stop rule:** nothing new from a differently-worded query and every form above has a primary source; about ten to fifteen openings.

The baseline the note must beat: the pipeline already turns a
Markdown render into `.pptx` through pandoc and a `.potx` template,
and already serves a static page with one JavaScript file per
recording from `docs/videos/` on GitHub Pages. A new tool earns its
place only if it yields a browser form that pandoc plus Pages
cannot, or yields it at a clearly lower cost in the pipeline.

## Key findings

F1. **GitHub's file viewer renders PDF, with links inside the PDF
ignored; its documentation lists no Office format.** [consensus
for the documented list; vendor documentation] The GitHub Docs
page on non-code files says "GitHub supports rendering of PDF
documents" and "Currently, links within PDFs are ignored" (section
Rendering PDF documents). The kinds it lists as rendered are
images (PNG, JPG, GIF, PSD, SVG), STL, CSV and TSV, PDF, prose
formats through github/markup, GeoJSON and TopoJSON, Jupyter
notebooks and Mermaid files; `.pptx`, `.docx` and "Office" occur
nowhere on the page [1]. That `.pptx` is therefore offered as a
download only is this agent's inference from the list, not a
statement GitHub makes; a search of docs.github.com and
github.blog for a rendered `.pptx` preview returned nothing of the
kind (Search record).

F2. **GitHub Pages serves static files, so a PDF or an HTML deck
put under it is shown by the visitor's browser with no download
step; the limits are 1 GB per site, a soft 100 GB per month and a
soft 10 builds per hour.** [consensus; vendor documentation]
Pages "is a static site hosting service" that "takes HTML, CSS,
and JavaScript files straight from a repository on GitHub" [3];
"Published GitHub Pages sites may be no larger than 1 GB", "a
*soft* bandwidth limit of 100 GB per month", "a *soft* limit of 10
builds per hour", the build limit lifted for a custom Actions
workflow, and Pages is not to be used "as a free web-hosting
service to run your online business" [2]. How a PDF under Pages
behaves (inline viewer or download, whether its links work) is the
visitor's browser's, not GitHub's; no GitHub source says anything
about it and the note does not claim it.

F3. **Pandoc writes an HTML + JavaScript deck from the same
Markdown it writes `.pptx` from; speaker notes carry to reveal.js,
pptx and beamer alike.** [consensus; vendor documentation; the
card's known item, found] The manual's Slide shows section opens
"You can use pandoc to produce an HTML + JavaScript slide
presentation that can be viewed via a web browser", names S5,
DZSlides, Slidy, Slideous and reveal.js, and gives one source file
for `pandoc -t revealjs -s habits.txt -o habits.html`, `pandoc -t
beamer habits.txt -o habits.pdf` and `pandoc habits.txt -o
habits.pptx`. "Speaker notes are supported in reveal.js,
PowerPoint (pptx), and beamer output" through a `::: notes` div;
`--slide-level` governs the split for all slide formats;
background images go to "self-contained reveal.js slide shows,
beamer slide shows, and pptx slide shows" [6]. The reveal.js
output links JS and CSS at the relative path `reveal.js`,
changeable with the `revealjs-url` variable, or bundled into one
file with `--self-contained` [6]; the manual's option list warns
that with embedded resources "some advanced features (e.g. zoom or
speaker notes) may not work" [6]. So the HTML form is already in
the pipeline's tool, at the price of hosting the reveal.js files
(or pointing `revealjs-url` at a copy) under Pages.

F4. **The pptx writer of pandoc uses seven named layouts from the
reference document; a `.potx`-based reference is the documented
way to style it.** [consensus; vendor documentation] The pptx
writer picks from "Title Slide, Section Header, Two Content,
Comparison, Content with Caption, Blank, and Title and Content",
taken from the default reference doc "unless an alternative
reference doc is specified using `--reference-doc`"; "For each
name, the first layout found with that name will be used" [6].
This is the mechanism the pipeline already uses; nothing in the
Marp class replaces it.

F5. **A reveal.js deck runs from static files with no build; a PDF
of it is made in Chrome through `?print-pdf` or with DeckTape, and
notes and fragments have documented print switches.** [consensus;
vendor documentation] "There's no need to go through a build
process or install any dependencies"; only "external Markdown"
is named as needing a local web server [8]. Export to PDF goes
"via a special print stylesheet", "only been confirmed to work in
Google Chrome and Chromium"; `showNotes: true` prints notes on
the slide or `"separate-page"` after it; each fragment step
prints as its own page unless `pdfSeparateFragments: false` [7].
The page says nothing about animations in the PDF; that auto-
animate and transitions are lost on paper is this agent's
inference from what a static page is.

F6. **Marp CLI's `.pptx` is pre-rendered images by design; the
editable variant is experimental, needs LibreOffice and drops
notes; PDF, PPTX and images all need a Chromium-class browser
installed.** [consensus across the vendor's README and the
maintainer's own FAQ; vendor documentation] "A converted PPTX
usually consists of pre-rendered background images"; "A created
PPTX includes rendered Marp slide pages and the support of Marpit
presenter notes"; "The experimental `--pptx-editable` option
requires installing both of the browser and LibreOffice Impress",
"may throw an error or output the incomplete result", "results in
lower slide reproducibility", and "presenter notes are not
supported" [4]. The maintainer's FAQ discussion of 23 March 2021
says the PPTX consists of "pre-rendered slide images" and that a
"pre-rendered image is nearly perfect" for design fidelity [5].
To "convert slide deck into PDF, PPTX, and image(s)" one of
Chrome, Edge or Firefox must be installed [4]. Marp's PDF can
carry notes as annotations and outlines/bookmarks (`--pdf-notes`,
`--pdf-outlines`); `--images png|jpeg` yields one file per slide
"like `slide-deck.001.png`"; `--notes` writes the notes to a text
file [4]. Whether Marp's HTML output is one self-contained file is
not stated in the README as read (Not found).

F7. **Slidev's PPTX is images too ("the text will not be
selectable"), with notes carried; its browser form is a static
SPA built with `slidev build` and deployed to Pages through
Actions with a base path.** [consensus; vendor documentation]
"all the slides in the PPTX file will be exported as images, so
the text will not be selectable"; "Presenter notes will be
conveyed into the PPTX file on a per-slide basis"; a
`pptx-editable` format rebuilds native shapes; PDF, PPTX and PNG
need `playwright-chromium`; the default export is "one page per
slide with clicks animations disabled" unless `--with-clicks` [9].
The build output goes to `dist`, served by "any other static
server"; the Pages workflow builds with `--base
/${{github.event.repository.name}}/` [10]. Slidev is a Node and
Vue toolchain, the heaviest of the class in the pipeline.

F8. **Quarto names reveal.js "the most capable format by far"
against pptx and beamer, with one syntax for all three.**
[vendor claim; vendor documentation] "The most capable format by
far is `revealjs`", recommended unless Office or LaTeX output is
required, with "the basic syntax for presentations that applies to
all formats" [11]; speaker notes go in a `.notes` div, with
`incremental` and `. . .` pauses [12]. Quarto wraps pandoc; it
adds a toolchain, not a form.

F9. **A deck image per slide is the one form every viewer shows
and every tool of the class makes, and it loses the most.**
[consensus; vendor documentation, with the loss list partly this
agent's] GitHub renders PNG and JPG in the file viewer [1]; Marp
`--images` [4] and Slidev PNG export [9] make one image per slide,
each needing a Chromium-class browser in the pipeline. What goes:
selectable and searchable text, links, notes and any animation,
by the nature of an image; the vendors do not spell this out.

Comparison of the forms, from the findings above:

| Form | Needs in the pipeline | Documented loss |
|---|---|---|
| `.pptx` in the GitHub file viewer | nothing new | no documented render at all [1]; download only (inference) |
| `.pdf` in the GitHub file viewer | a PDF writer (pandoc beamer needs LaTeX; Marp/Slidev/reveal.js need Chromium) | links ignored [1]; animation gone; notes only if the writer prints them [4][7] |
| PDF under GitHub Pages | the same PDF writer plus a Pages source | whatever the visitor's browser does with a PDF; no GitHub source |
| HTML deck under GitHub Pages | pandoc `-t revealjs` plus the reveal.js files under Pages, or `--self-contained` [6]; or Marp `html`, or Slidev `build` | self-contained output may lose zoom or speaker notes [6]; external Markdown needs a server [8] |
| image per slide | Chromium in the pipeline [4][9] | text, search, links, notes, animation |

## Unexpected

The card frames Marp-class tools as a possible new form. The
sources show the opposite ordering: the HTML form comes free with
pandoc [6], while the Marp class costs a Chromium-class browser
for everything but HTML [4][9] and delivers a `.pptx` that is
images [4][5][9], weaker than the `.potx`-templated `.pptx` the
pipeline has. The one thing the class adds over pandoc is a
designed theme system for the HTML deck (Marp themes, Slidev's
Vue components), which is a question of look, not of form. Lead,
not conclusion: the Marp author's own starter deploys only
`public/index.html` and an Open Graph image to Pages through an
Actions workflow `.github/workflows/github-pages.yml` [13]; if a
Marp look is ever wanted, that is the smallest shape of it.

A second lead: pandoc's manual warns that `--embed-resources`
output may lose "zoom or speaker notes" [6]. If the forge hosts a
reveal.js deck under Pages, hosting the reveal.js directory beside
it, or pointing `revealjs-url` at it, keeps notes; a single-file
deck is the convenience, not the default. Unverified in a run.

## Not found

- No GitHub statement, positive or negative, on how a `.pptx` file
  is shown in the file viewer; searched docs.github.com and
  github.blog (Search record). The documented list of rendered
  kinds [1] is the only evidence, and it is silence.
- No source on how a PDF under GitHub Pages behaves in the
  visitor's browser (inline viewer, link handling); this is the
  browser's, and no vendor page read says it.
- Whether Marp CLI's HTML output is one self-contained file; the
  README as read does not say [4].
- Font behaviour per form (embedding in PDF, web fonts in an HTML
  deck under Pages, substitution in `.pptx`): no vendor page read
  states it; the card's "fonts" column stays unanswered here.
- A GitHub Action published by marp-team itself: the Marp CLI
  README has no such reference [4]; the official starter uses a
  plain workflow with npm [13]. Community actions exist (seen in
  search results, not opened).
- The pandoc version the manual read documents: the page does not
  carry it in the parts read [6].

## Options

1. **PDF only, in the repository.** `pandoc -t beamer` (needs
   LaTeX) or a browser-made PDF from an HTML deck [7]; GitHub
   renders it in place [1]. Cheapest to host, loses links in the
   viewer [1] and all motion; notes only if printed [7].
2. **HTML deck under Pages through pandoc.** `-t revealjs` from the
   same Markdown render that makes the `.pptx` [6], the reveal.js
   files committed under `docs/` beside the existing player, one
   Pages source already in use. Keeps notes, fragments, links and
   search; adds no tool. Costs a reveal.js copy in the repository
   and a second output per deck recipe. This agent's recommended
   option.
3. **HTML deck under Pages through Marp or Slidev.** A designed
   look out of the box, at the price of Node (and Chromium for any
   non-HTML output) in the pipeline and a second slide dialect
   beside pandoc's [4][9][10]; their `.pptx` does not replace the
   templated one [4][5][9].
4. **Images per slide in the repository.** Needs Chromium [4][9];
   shows anywhere [1]; loses text, links, notes and search. Fit for
   a thumbnail or a social preview, not for a deck.

## Relevance to this project

The browser form the forge lacks is an HTML deck under GitHub
Pages, and the tool that makes it is the one the forge already
runs: pandoc's reveal.js writer takes the same Markdown render and
the same `::: notes` as the `.pptx` writer [6], and the Pages
source that serves `docs/videos/` serves a deck directory just as
well [3]. That is the recommendation, chosen against Marp or
Slidev because they add a toolchain and a Chromium dependency
[4][9] while their `.pptx` is images [4][5][9], weaker than the
`.potx` output the pipeline has; and against PDF-only because
the GitHub viewer drops links [1] and a PDF drops notes and motion
unless printed in [7]. What the recommendation rests on is vendor
documentation throughout; what it does not rest on is any run, so
the self-contained versus hosted reveal.js choice [6] and the
behaviour of fonts (Not found) are to be tried, not assumed. This
agent's own inferences, marked as such above: that `.pptx` in the
GitHub viewer is download only (from GitHub's silence [1]), and
that images and PDFs lose animation (from what they are).

Consult when: a deck recipe gains a browser output; a `.pptx` is
proposed as the thing a visitor opens from the repository; someone
proposes Marp, Slidev or Quarto for the forge; a PDF of a deck is
to be put in the repository or under Pages; a theme for the HTML
deck is wanted and the Marp look is on the table.

## Sources

1. Working with non-code files. GitHub Docs (GitHub, Inc.).
   Undated (no date on page). https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files
   Kind: primary. Read: partially, the rendering sections (PDF,
   images, 3D, CSV, prose, maps, Jupyter, Mermaid) through a
   summarising fetch. Original.
2. GitHub Pages limits. GitHub Docs (GitHub, Inc.). Undated.
   https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
   Kind: primary. Read: in full through a summarising fetch.
   Original.
3. What is GitHub Pages? GitHub Docs (GitHub, Inc.). Undated.
   https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
   Kind: primary. Read: partially, the definition paragraph,
   through a summarising fetch. Original.
4. marp-team/marp-cli README. Marp team (GitHub repository).
   Undated; the README shows only a version placeholder
   "v4.x.x". https://github.com/marp-team/marp-cli
   Kind: primary (vendor documentation). Read: partially, in two
   summarising fetches: the sections on outputs, browser
   requirement, PPTX and `--pptx-editable`, PDF notes and
   outlines, images, `--notes`, server and watch. Original.
5. [Frequently Asked] Exported PPTX cannot re-edit. yhatt
   (maintainer), marp-team GitHub Discussions #82. Dated 23 March
   2021 by the page's byline. https://github.com/orgs/marp-team/discussions/82
   Kind: primary (maintainer's statement). Read: in full through a
   summarising fetch. Original.
6. Pandoc User's Guide, section Slide shows and the options list.
   John MacFarlane (pandoc.org). Undated on page; version not
   read. https://pandoc.org/MANUAL.html
   Kind: primary (vendor documentation). Read: partially, in two
   summarising fetches: the options list (first 100,000
   characters) and the Slide shows section with its subsections
   (from offset 230,000). Original.
7. PDF Export. reveal.js documentation (Hakim El Hattab /
   Slides). Undated. https://revealjs.com/pdf-export/
   Kind: primary. Read: in full through a summarising fetch.
   Original.
8. Installation. reveal.js documentation. Undated.
   https://revealjs.com/installation/
   Kind: primary. Read: in full through a summarising fetch.
   Original.
9. Exporting. Slidev documentation (Slidev / Anthony Fu).
   Undated. https://sli.dev/guide/exporting
   Kind: primary. Read: in full through a summarising fetch.
   Original.
10. Hosting. Slidev documentation. Undated.
    https://sli.dev/guide/hosting
    Kind: primary. Read: partially, the build and GitHub Pages
    sections, through a summarising fetch. Original.
11. Presentations. Quarto documentation (Posit). Undated.
    https://quarto.org/docs/presentations/
    Kind: primary. Read: in full through a summarising fetch.
    Original.
12. Revealjs. Quarto documentation (Posit). Undated.
    https://quarto.org/docs/presentations/revealjs/
    Kind: primary. Read: partially, the speaker notes and
    incremental content sections, through a summarising fetch.
    Original.
13. yhatt/marp-cli-example README. yhatt (author of Marp), GitHub
    repository. Undated. https://github.com/yhatt/marp-cli-example
    Kind: primary (the tool author's own starter). Read: in full
    through a summarising fetch. Original.
14. Pandoc manual, chunked HTML, "10 Slide shows".
    https://pandoc.org/chunkedhtml-demo/10-slide-shows.html
    Not opened: HTTP 404 on fetch; the section was read in [6]
    instead. Never cited for content.

Every reading above was through WebFetch, which returns a
summarised extraction of the page; quotes are as the extraction
returned them and are short.

## Opened and not used

- Quarto Revealjs [12]: opened for the "most capable" sentence,
  which stands on the overview page [11] instead; its notes and
  fragments content is cited once only.
- No other opened page was left out.

## Search record

Queries, in order: GitHub docs rendering PDF files in repository
viewer; Marp CLI pptx export editable text limitations; pandoc
slide shows revealjs pptx same markdown source; GitHub does not
render pptx preview download only (disconfirming, first form);
Marp GitHub Actions deploy slides GitHub Pages marp-cli-action;
github.com community discussion render pptx docx preview in
repository file viewer; GitHub changelog preview Office documents
pptx docx in repositories rendered (disconfirming, second form);
pptx PowerPoint files rendered preview repository, limited to
docs.github.com and github.blog (disconfirming, third form); Marp
pptx export limitations editable text, limited to marp.app and
github.com (disconfirming, Marp half).

Disconfirming result: the three GitHub-side forms returned no
GitHub page stating that `.pptx` is rendered or that a preview
was removed; the only GitHub pages returned were the non-code
files page [1], which lists no Office format, an attachments page
(not opened) and pull-request changelog entries about image,
Markdown and SVG rich diffs. The Marp half returned the
maintainer's FAQ [5] and issues about the editable export
failing, none claiming editable shapes by default. The expectation
held on both halves; the GitHub half holds by silence.

Openings: 14, of which 13 succeeded and one returned 404 [14];
two pages were read in two passes each ([4], [6]). The run ended
on both parts of the stop rule at once: every form of the card
has a primary source, and the last two queries, worded
differently and restricted to the vendors' own domains, returned
nothing not already opened. The opening budget was reached at the
same point.

## Attached notes

None.
