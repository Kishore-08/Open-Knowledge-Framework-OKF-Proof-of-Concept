---
id: python-option-callbacks-https-docs-python-org-3-library-optparse-ht-f59a6996
type: concept
title: Option Callbacks[¶](https://docs.python.org/3/library/optparse.html#option-callbacks
  "Link to this heading")
description: When `optparse`’s built-in actions and types aren’t quite enough for
  your
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Option Callbacks[¶](https://docs.python.org/3/library/optparse.html#option-callbacks "Link to this heading")

When `optparse`’s built-in actions and types aren’t quite enough for your
needs, you have two choices: extend `optparse` or define a callback option.
Extending `optparse` is more general, but overkill for a lot of simple
cases. Quite often a simple callback is all you need.

There are two steps to defining a callback option:

- define the option itself using the `"callback"` action
- write the callback; this is a function (or method) that takes at least four
  arguments, as described below