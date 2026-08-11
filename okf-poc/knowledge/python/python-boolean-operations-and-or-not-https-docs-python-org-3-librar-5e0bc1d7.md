---
id: python-boolean-operations-and-or-not-https-docs-python-org-3-librar-5e0bc1d7
type: concept
title: Boolean Operations — `and`, `or`, `not`[¶](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
  "Link to this heading")
description: 'These are the Boolean operations, ordered by ascending priority:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Boolean Operations — `and`, `or`, `not`[¶](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not "Link to this heading")

These are the Boolean operations, ordered by ascending priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x or y` | if *x* is true, then *x*, else *y* | (1) |
| `x and y` | if *x* is false, then *x*, else *y* | (2) |
| `not x` | if *x* is false, then `True`, else `False` | (3) |

Notes:

1. This is a short-circuit operator, so it only evaluates the second
   argument if the first one is false.
2. This is a short-circuit operator, so it only evaluates the second
   argument if the first one is true.
3. `not` has a lower priority than non-Boolean operators, so `not a == b` is
   interpreted as `not (a == b)`, and `a == not b` is a syntax error.