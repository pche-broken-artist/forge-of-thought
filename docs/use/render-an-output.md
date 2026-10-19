---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 14f10e8f83a9d91a
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
---

# Render an output

This page shows how to regenerate a render, and its plain file, with
`/render`. A render is an output made for one audience from the
documents of a project, such as a README or a deck. It is written for
the principal (the person whose thinking is forged) who wants the
output made again after the documents or the recipe changed.

## When to use it

Use it when a render is out of date, or when you have changed its
recipe (the file that says how the render is made) and want to see the
result. A render is never edited by hand and is never a source of
truth. Why that is so is on [Renders and
recipes](../about/renders-and-recipes.md).

Claude does not regenerate a render on its own judgement. It reports a
stale render and offers. A render is regenerated only on this command
or by `/release`.

## The command

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/` directory,
for example `readme`. `[slug]` names the project; leave it out and
Claude infers the project from the conversation, or asks if it is
ambiguous.

## What happens

1. Claude reads `recipes/<recipe>.md`. If the recipe does not exist,
   it offers to compose one and stops. You should now see either the
   recipe read, or the offer to compose it.

2. Claude reads the inputs the recipe declares, each from disk at its
   current version. Where an input is the ledger (the file that holds a
   project's state), Claude first makes it with its script, so the
   render reads a current file. You should now see the inputs read
   from disk.

3. Claude generates the Markdown in isolation. A subagent (a separate
   Claude run that never sees your conversation) reads the recipe and
   its inputs alone and writes the file. Nothing said in the
   conversation reaches the render. You should now see the render
   written.

4. The file lands in `renders/<recipe>.md`, or at the recipe's
   `output:` path where the recipe names one. An existing file is
   overwritten, because its history lives in git. The render opens with
   provenance front-matter that records what it was made from; its
   shape is on [Render provenance](../reference/render-provenance.md).
   You should now see the file with its provenance at the top.

5. Where the recipe declares `languages:`, the first language is the
   primary render and is written first. Each other language is then
   written as a file of its own, `renders/<recipe>.<lang>.md`, scene
   for scene and line for line, and its provenance names the primary
   render it was made from. Nothing is re-cut. You should now see one
   file per language.

6. Back in the session (the working conversation with Claude), the
   written file is scanned mechanically for facts of the instance, with
   `python scripts/docs-check.py --file <render>`. A hit is said aloud
   and you judge it. An instance fact is regenerated out, never edited
   by hand. A public fixed text of the recipe, or a fact of the
   engine's own history, stands. You should now see either no hit or
   the hits named for your judgement.

7. Claude verifies that the file exists and that its provenance is
   correct. The ledger's Renders table reads that provenance, so
   nobody writes a row. A translation cites the primary render. Claude
   remakes the ledger and reports what was rendered from what. You
   should now see the report.

8. Where the recipe has a `## Format` section, the plain file is made
   beside the render:
   - a `.docx` or `.pptx` through pandoc, from the reference document
     and page size the section names;
   - for a screenplay, the video or the player file through
     `scripts/md2video.py`, with the format, the pace and the date the
     section names, at the render or at the recipe's `output:`.

   Where a needed tool is missing, Claude says so aloud, the render
   stands and the plain file is not made. A recipe without the section
   ends at the Markdown. You should now see the plain file beside the
   render. The screenplay's formats are on [Make a teaching video from a
   recipe](make-a-video-from-a-recipe.md).

9. Where a published file of the recipe exists, Claude tells you that
   it is now older than its render. It remakes nothing. You should now
   see that line.

## What you have afterwards

- The Markdown render, in `renders/` or at the recipe's `output:`,
  with provenance at its top.
- One file per language, where the recipe declares languages.
- The plain file beside the render, where the recipe names a format
  and the tool was present.
- The ledger's Renders table reading the new provenance.

The designed file, the one made through a model, is not made here. It
is made on its own command: [Publish a designed
file](publish-a-designed-file.md).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it and makes
  nothing.
- The scan names an instance fact: you judge it, and the render is
  regenerated, not edited by hand.
- A tool for the plain file is missing (pandoc, or the tools the video
  needs): the render stands, the plain file is not made and Claude says
  so. Install the tool and run the command again.

For any term of the forge on this page, see the
[Glossary](../reference/glossary.md).

## A worked example

You have changed the recipe `readme` of a project `my-project` and
want the README again.

```
/render readme my-project
```

Claude reads `recipes/readme.md`, reads its inputs from disk, and has a
subagent write the README to the recipe's `output:` path, with
provenance at the top. It scans the file for instance facts and finds
none, verifies the provenance and remakes the ledger. The recipe has no
`## Format` section, so it ends at the Markdown. No published file
exists, so nothing is said about one. You see the report of what was
rendered from what.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
