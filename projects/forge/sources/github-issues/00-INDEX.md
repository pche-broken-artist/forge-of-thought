---
bundle: github-issues
project: forge
date: 2026-10-21
origin: the issues of the engine's GitHub repository, downloaded with their comments through the GitHub API
---

# Index — bundle `github-issues`

<!-- Catalogue of one bundle (sources/<slug>/): the rules are
CLAUDE.md's (Document chain, External inputs). This skeleton is the one owner of the
bundle index (POS.1070): the header and the opening paragraph are its
own, the per-file entry is the sources entry of templates/index.md,
cited and not copied. The opening paragraph says whether the bundle
arrived whole or grows (POS.0180). -->

The issues visitors open on the engine's GitHub repository, one file
per issue with the comments it carried when it was downloaded. A
growing bundle: a new issue is added as its own file and entry when
the principal ingests it, each file immutable from its registration
(POS.0180).

### `issue-3-repo-detection.md`
- **What:** GitHub issue #3, "Repository detection tests for `<path>/.git` instead of asking git": the scripts test `projects/<slug>/.git` and assume the project directory is the top of its repository, so a project that is a subdirectory of a larger repository (reached through a symlink in the reporter's case) is reported as "not under git" by every script, the ledger's `tracked` guard included; nine sites listed with lines on `main` at `c0b0f3c`; a helper `repo_root` asking `git rev-parse --show-toplevel` proposed, with the project directory and its repository kept apart. With the principal's reply of 2026-10-21: accepted for work, intent first; the engine-root exclusion of the helper holds only while the engine is the top of its own repository; `.gitignore` and `.gitattributes` may stay in the project directory.
- **Origin:** https://github.com/pche-broken-artist/forge-of-thought/issues/3, opened by a contributor on 2026-10-21; downloaded with its one comment on 2026-10-21.
- **Date:** 2026-10-21, from the content
- **Form:** text
- **Role:** the report from which the thread on a project inside a larger repository was opened; the author's layout, the nine sites and his proposed helper, with the principal's reply of 2026-10-21.
- **Use for:** the layout that fails today and why; the list of detection sites in the scripts; the proposed helper and the two remarks on it.
