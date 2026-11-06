---
description: Compose or iterate the recipe that renders a project's user stories as the export the instance hands over — one heading per story, its parts on lines of their own, pasted into a wiki or a tracker such as Confluence or Jira
---

Genre: user-stories-export. Skeleton:
`templates/recipe-user-stories-export.md`. Output: the default,
`renders/user-stories-export.md`. Thought projects that have
`35-user-stories.md` (`.claude/skills/forge/states/user-stories.md`);
the export is a render and never the artefact.

The shape of the export is the skeleton's and follows the pattern
in `projects/forge/sources/example-user-stories-v2.md`: no table,
since a Markdown table cannot break a line inside a cell and a paste
into a wiki or a tracker runs a story into one paragraph; a recipe
keeps the shape and changes only what the elicitation below opens.

Role: interviewer, lightly — this genre has few degrees of freedom.
Elicit:
1. **The input.** `35-user-stories.md` by default; a work product in
   `work/` where the stories were made from a source.
2. **The section heading and the purpose line.** The skeleton holds
   placeholders for the second heading and the sentence under it;
   they are filled with the words of the export the instance hands
   over, as the principal gives them, in the render's language.

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2); the labels of a story stay in
English whatever the language.
