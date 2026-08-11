---
id: python-junk-heuristic-https-docs-python-org-3-library-difflib-html--b041ceae
type: concept
title: Junk heuristic[¶](https://docs.python.org/3/library/difflib.html#junk-heuristic
  "Link to this heading")
description: '`difflib` uses a *junk* heuristic: some items are deemed to be'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Junk heuristic[¶](https://docs.python.org/3/library/difflib.html#junk-heuristic "Link to this heading")

`difflib` uses a *junk* heuristic: some items are deemed to be
*junk*, and ignored when searching for similarities.
Ideally, these are uninteresting or common items, such as blank lines
or whitespace.

This heuristic can speed the algorithm up (because it reduces the number of
possible combinations) and it can produce results that are more understandable
for humans (typically breaking on whitespace).
But it can also cause pathological cases:

- Inappropriately chosen junk items can cause an unexpectedly **large** (but
  still correct) result.
- The default heuristic is **asymmetric**: only the second sequence is
  inspected when determining what is considered junk, so comparing A to B can
  give different results than comparing B to A and reversing the result.

By default, if the second input sequence is at least 200 items long, items
that account for more than 1% it are considered *junk*.

Depending on your data, you should consider turning this heuristic off
(setting [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher")’s *autojunk* argument to to `False`)
or tuning it (using the *isjunk* argument, perhaps to one of the
[predefined functions](https://docs.python.org/3/library/difflib.html#difflib-isjunk-functions)).