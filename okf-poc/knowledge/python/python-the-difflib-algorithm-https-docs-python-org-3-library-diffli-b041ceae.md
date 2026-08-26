---
id: python-the-difflib-algorithm-https-docs-python-org-3-library-diffli-b041ceae
type: concept
title: The `difflib` algorithm[¶](https://docs.python.org/3/library/difflib.html#the-difflib-algorithm
  "Link to this heading")
description: The algorithm used in [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
  "difflib.SequenceMatcher") predates, and is a little
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## The `difflib` algorithm[¶](https://docs.python.org/3/library/difflib.html#the-difflib-algorithm "Link to this heading")

The algorithm used in [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") predates, and is a little
fancier than, an algorithm published in the late 1980s by Ratcliff and
Obershelp under the hyperbolic name “gestalt pattern matching.”
The idea is to find the longest contiguous subsequence common to both inputs,
then recursively handle the pieces of the sequences to the left and to the
right of the matching subsequence.

See also

[Pattern Matching: The Gestalt Approach](https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8807/8807c/8807c.htm)
:   Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener. This
    was published in Dr. Dobb’s Journal in July, 1988.

As an extension to the Ratcliff and Obershelp algorithm, `difflib`
searches for the longest *junk-free* contiguous subsequence.
See the [Junk heuristic](https://docs.python.org/3/library/difflib.html#difflib-junk) section for details.

**CPython implementation detail:** Timing

The basic Ratcliff-Obershelp algorithm is cubic time in the worst
case and quadratic time in the expected case.
`difflib`’s algorithm is quadratic time for the worst case and has
expected-case behavior dependent in a complicated way on how many elements
the sequences have in common;
best case time is linear.