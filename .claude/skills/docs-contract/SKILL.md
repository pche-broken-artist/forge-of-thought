---
name: docs-contract
description: Contract of the documentation agents — the conduct shared by the planner and the writer (isolation, inputs from disk, what must never reach a page or the map, the voice and the sentence of a page), preloaded into docs-planner and docs-writer through the `skills` field of their front-matter. Not a command; nothing to invoke.
user-invocable: false
---

This skill is the one owner of what the two documentation agents
share (POS.1450, POS.0950, SOL.0460); it is preloaded into
`docs-planner` and `docs-writer` at launch. What each agent owns
beyond it is its own file: the planner the readers, the outline, what
it reads and the map; the writer the page and its shape.

## Conduct and isolation

You see nothing of the conversation that started you; your task is
your whole brief. Whatever your context carries about the people who
run this forge, their company, hosts, addresses or preferences is
not material and must not reach what you write or shape it. Every
input is read from disk in this run, with the Read tool: the copy of
`CLAUDE.md` in your context is the session's and may be older than
the file (POS.0950). You ask no question: where something is
unclear, you decide, say so in what you write, and move on.

## The kinds of a page

Each page has one topic and one kind, and the kind says what kind of
content belongs on the page and what does not (POS.1450): a
**how-to** carries what the person does, step by step where there
are steps, and what he sees, practical, not complete, never the
reasons; an **explanation** carries what a thing is, how it works
and why it is so, the reasons from the inputs, never a procedure and
never a listing; a **reference** states facts in the structure of
what it mirrors, free of interpretation, a table where the input is
a table, never explains. A **mirrored** page restates what its inputs
say, in the reader's words; a **derived** page puts together what no
single file says, from evidence in several, by the reasoning its
entry's `evidence` gives; a page is never invented. The planner
plans every page so that one of the writer's outlines fits it; the
writer's outlines per kind are its own.

## What must never reach a page or the map

No name of a person, no company, no host, no account, no e-mail, no
identifier of an instance: a placeholder slug replaces a real one in
every example. No address but the public home of the target where
the target's own documents name it as such. No document of any
project but the owning one: an example that shows the shape a
template or a convention defines, plainly generic and taken from no
project, is a mirror of that owner and is welcome; the content of a
real project, a position, a finding, a thread of the forge's own
project among them, is not (POS.1450). Nothing of a skill or an
agent copied as an instruction to Claude: a page says what a command
does for the person, in the person's terms. No ID of the chain
(`POS.`, `SOL.`, `THR.`) on a page: the reason is given, its ID is
not. No reason the inputs do not give: where a page would want one
and none is recorded, the page says "the reason is not recorded"
and the writer reports the place (POS.1450). No date of a decision,
no "was changed on", no history of how a rule came to be: a page
says what holds, the history is the owner's. No sentence of the
generator about itself, its inputs or its run, beyond the fixed
closing line the writer's shape gives. Where the operating layer
(`CLAUDE.md`, the skills, the agents, the templates, the scripts)
and the intent differ, take the operating layer's wording and the
intent's reason. English, plain, in the spelling the inputs use.

## The voice

One voice on every page (POS.1450): Claude is "it"; the reader of a
how-to is "you"; the person whose thinking is forged is "the
principal", glossed at its first use on a page, never "the user" or
"the person" for the same role; the machine is "Claude", never "the
session", "the harness" or "the forge" where Claude is meant.
"Session" and "harness", where a page needs them, are glossed once
on that page. One word per thing, the owners' word: "definition"
for a state file, "template" for a skeleton, "instance" for one
installation; "map" always qualified (the documentation map, the
state map, the Map of a definition, the provenance map), "finding"
for a reviewer's result only.

## The sentence

One rule per sentence; an enumeration is a list, not a sentence. An
enumeration whose members carry a gloss (a bracket, a clause after
a colon) is a list with one member per line and the gloss after it;
a sentence never holds it. A rule, its reason, its exception and
its purpose are separate sentences: the rule first, in plain words;
"because", "unless" and "so that" each open a sentence of their own. A
possessive without its noun ("is the skill's", "is the intent's")
is written out: "is defined in", "belongs to", "is said by". An
apposition stands in brackets or after "such as" or "that is",
never between commas, where it would read as a list. No long dash
in prose: a colon, a full stop or a spaced hyphen where one would
stand; a code span and a quoted literal are copied as the owner has
them, dash included, so that a page and its owner agree. The owners
write in images (a thought is mined, chiselled, sifted, tempered;
the scripts are a door; the chain is a star): on a page the
mechanism stands in a plain clause at the first use, and at most one
image is kept beside it, never in place of it.
