---
date: 2026-10-17
project: forge
topic: git merge drivers and their limits
status: immutable
derived_from: the principal's word of 2026-10-17 (does git have something for joining files); research/2026-10-17-mergeable-shared-records-in-git.md; 10-intent.md v5.12 (POS.1110, POS.1490); web sources
---

# git merge drivers and their limits

## Question

What does git itself offer for merging one file automatically - the
attributes, the built-in drivers, the contract of a custom driver -
where does each apply and where does none of it reach, so that the
forge knows what it may promise when it puts a driver on its record
files? Companion of
`2026-10-17-mergeable-shared-records-in-git.md`, which says what
the field does with that machinery.

## Key findings

**F1. The `merge` attribute chooses a driver per path.** [verified,
git documentation] `.gitattributes` maps paths to a driver: `text`
(the usual three-way merge with conflict markers), `binary` (keep
ours, leave the path conflicted), `union` (three-way merge that
takes lines from both sides instead of markers), or the name of a
custom driver. The attribute "affects how three versions of a file
are merged when a file-level merge is necessary during git merge,
and other commands such as git revert and git cherry-pick". The
documentation does not name `git rebase`; rebase replays commits
through the same merge machinery, so a driver runs there too, a
mechanical inference confirmed by the field's use of drivers under
`pull --rebase` but not by a sentence in the manual - to be tested
on a throwaway clone before the forge relies on it (THR.0650 has
such a test pending).

**F2. The custom driver's contract is small.** [verified, git
documentation] In the config, `merge.<name>.driver` is a command
line with placeholders: `%O` the ancestor's version, `%A` ours,
`%B` theirs, as temporary files; `%L` the conflict-marker size; `%P`
the path the result will be stored at; `%S`, `%X`, `%Y` the labels.
The driver overwrites the file at `%A` with the result and exits 0
for a clean merge, non-zero for a conflict, above 128 for a crash
(then the merge fails rather than conflicts). `merge.<name>.recursive`
names the driver for the inner merges of criss-cross ancestors,
`binary` being the usual choice. A Python script of the forge fits
this contract without a dependency.

**F3. A driver runs only when the three-way merge would conflict in
that file, and only on the clone that merges.** [verified, GitLab
docs and git behaviour] "A custom merge driver is invoked only in
the case of a non-trivial merge conflict" (GitLab, Git attributes):
a file changed on one side only is taken as it is, a file changed
on both sides in different places is merged by the text driver's
hunks first. The practical consequence for the forge: a driver is
a safety net under the cases that would otherwise stop the user,
not a rewrite of every merge.

**F4. The driver definition is not shared.** [verified] The
repository carries `.gitattributes` with the name; the command
behind the name lives in `.git/config` or the user's `~/.gitconfig`,
which git never transports. Every clone must register it: the field
does so from an install hook (derived-merge's `postinstall`) or a
setup command (Weave's `weave setup`, mergiraf's registration). In
the forge that is `/setup`'s and `/new-project`'s to do, and
`forge-clone`'s at an import; a clone where the step was skipped
falls back to the text driver and shows the conflict as today -
degraded, never wrong.

**F5. `union` is positional, and that is why it loses lines.**
[verified on reports] The union driver is the text driver with
conflicts resolved by taking both hunks; at a seam where both sides
appended after the same last line, the shared context is emitted
once and an edge line can vanish; a line edited on both sides is
kept twice; the order of the added lines is undefined. git's own
manual says "the user should verify the result". For a file whose
lines are records with an identity, the right semantics is a set
union - deduplicate by the record, order by a key - which git has
only for notes (`git notes merge --strategy=cat_sort_uniq`) and
which a custom driver can implement in a few lines: read the three
versions as sets of records, result = ours ∪ theirs minus what
either side removed from the base, sorted by the record's key
(date, version), exit 0. A record changed on both sides into two
different wordings is the one case left to the user, reported as a
conflict with both wordings.

**F6. Hosting platforms merge without drivers.** [verified] GitLab:
custom merge drivers are "not supported on GitLab.com", on
self-managed instances only an administrator can define them, and
`merge=union` is not honoured when a merge request is merged (issues
17325 and 18830 open). Bitbucket: the same, two open tickets.
GitHub: the web merge is not documented to honour attributes'
drivers, and field reports say it does not. Consequence: a merge
request whose files would conflict stays unmergeable on the server
until someone merges locally; a driver helps in exactly that local
merge and in the rebase of `/save`. The forge should say this
plainly where it offers the driver and not promise a conflict-free
merge request.

**F7. Validate what a driver writes.** [consensus in the field]
The lockfile drivers that survived validate their result
(`npm ls`) and fail loudly when it does not hold; the generated-
block driver regenerates rather than merges. A forge driver for a
record file should run the file's own check after writing
(the history's shape, the ledger's generation) and exit non-zero
when it fails, so that a bad merge never exits 0 - the failure the
`union` reports all share.

## Options with trade-offs

| Option | Trade-off |
|---|---|
| no driver, conflicts by hand (today) | nothing to install; every parallel branch stops at the ledger and the histories |
| `merge=union` on the record files | one line, no script; loses lines silently, undefined order, zero exit on damage - rejected |
| a forge driver, set-union for record logs, regenerate for derived files | one Python script in `scripts/`, registered per clone by `/setup`; the merge the user ordered completes where it would have stopped; nothing on the server; must validate its output |
| an external driver (mergiraf, Weave, cfgmerge) | no Markdown-table or bullet-log support verified; a dependency beyond Python and git, which the forge's portability rule avoids |

## Relevance to this project

The forge may promise exactly this: when the user merges or `/save`
rebases on his clone, a conflict in a history log, in `decisions.md`
or in an index is settled as a set union of records, a conflict in
the ledger is settled by regenerating it, and a record changed on
both sides is shown to him; a merge request on GitLab or GitHub
does not benefit and says so. The driver is one script, registered
by `/setup` and `/new-project`, named in each project's
`.gitattributes` (scaffolded from a template), and tested on the
throwaway clone THR.0650 already asks for. POS.1110 and REJ.0170
stand: merge logic stays git's; the forge only tells git how its own
record files merge, as every lockfile tool does.

## Sources

- git, gitattributes documentation: https://git-scm.com/docs/gitattributes
- git, `git notes merge` strategy `cat_sort_uniq`, commit a6a09095: https://git.lorimer.id.au/gitweb.git/diff/a6a09095a08339afc8468d053ff978ed4662a1d5
- GitLab, Git attributes (custom merge drivers): https://docs.gitlab.com/user/project/repository/files/git_attributes
- GitLab issue 17325, support `merge=union` in merge requests: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/17325
- GitLab issue 18830, use gitattributes custom merge driver in MRs: https://gitlab.com/gitlab-org/gitlab/-/issues/18830
- Bitbucket BCLOUD-20234, BSERV-19161: https://jira.atlassian.com/browse/BCLOUD-20234 , https://jira.atlassian.com/browse/BSERV-19161
- Graphite, git merge driver guide: https://graphite.dev/guides/git-merge-driver
- Julian Burr, custom git merge drivers: https://www.julianburr.de/til/custom-git-merge-drivers
- derived-merge (registration from `postinstall`): https://github.com/ShawezA/derived-merge
- Weave (`weave setup`): https://raw.githubusercontent.com/Ataraxy-Labs/weave/main/README.md
- mergiraf: https://terminaltrove.com/mergiraf/
- cfgmerge: https://github.com/jaysyrk/cfgmerge
- git-json-merge: https://github.com/jonatanpedersen/git-json-merge
- boneskull/package-lock-merge-driver (validation): https://github.com/boneskull/package-lock-merge-driver
- `merge=union` failure reports: https://github.com/btclib-org/.github/issues/1582 , https://github.com/btclib-org/btclib-node/issues/1460 , https://github.com/choiceoh/stkernel/pull/1222 , https://github.com/dsifry/metareview/pull/211
