---
id: python-difflib-helpers-for-computing-deltas-https-docs-python-org-3-b041ceae
type: concept
title: '`difflib` — Helpers for computing deltas[¶](https://docs.python.org/3/library/di'
description: '**Source code:** [Lib/difflib.py](https://github.com/python/cpython/tree/3.14/Lib/difflib.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `difflib` — Helpers for computing deltas[¶](https://docs.python.org/3/library/difflib.html#module-difflib "Link to this heading")

**Source code:** [Lib/difflib.py](https://github.com/python/cpython/tree/3.14/Lib/difflib.py)

---

This module provides classes and functions for comparing sequences.
Most of them compare sequences of text lines (for example lists of strings,
or [file objects](https://docs.python.org/3/glossary.html#term-file-object)) and
produce *diffs* – reports on the differences.
Diffs can be produced in in various formats, including HTML and context
and unified diffs – formats produced by tools like
*[diff](https://manpages.debian.org/diff(1))* and *[git diff](https://manpages.debian.org/git-diff(1))*.

Comparisons are done using a matching algorithm implemented in
[`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") – a flexible class for comparing pairs of sequences
of any type, not just text, so long as the sequence elements are
[hashable](https://docs.python.org/3/glossary.html#term-hashable).