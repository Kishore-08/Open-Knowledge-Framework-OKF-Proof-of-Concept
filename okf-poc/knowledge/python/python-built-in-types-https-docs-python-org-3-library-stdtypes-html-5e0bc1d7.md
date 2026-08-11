---
id: python-built-in-types-https-docs-python-org-3-library-stdtypes-html-5e0bc1d7
type: concept
title: Built-in Types[¶](https://docs.python.org/3/library/stdtypes.html#built-in-types
description: The following sections describe the standard types that are built into
  the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# Built-in Types[¶](https://docs.python.org/3/library/stdtypes.html#built-in-types "Link to this heading")

The following sections describe the standard types that are built into the
interpreter.

The principal built-in types are numerics, sequences, mappings, classes,
instances and exceptions.

Some collection classes are mutable. The methods that add, subtract, or
rearrange their members in place, and don’t return a specific item, never return
the collection instance itself but `None`.

Some operations are supported by several object types; in particular,
practically all objects can be compared for equality, tested for truth
value, and converted to a string (with the [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") function or the
slightly different [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") function). The latter function is implicitly
used when an object is written by the [`print()`](https://docs.python.org/3/library/functions.html#print "print") function.