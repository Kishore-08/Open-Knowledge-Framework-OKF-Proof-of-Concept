---
id: python-the-ellipsis-object-https-docs-python-org-3-library-stdtypes-5e0bc1d7
type: concept
title: The Ellipsis Object[¶](https://docs.python.org/3/library/stdtypes.html#the-ellipsis-object
  "Link to this heading")
description: This object is commonly used to indicate that something is omitted.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### The Ellipsis Object[¶](https://docs.python.org/3/library/stdtypes.html#the-ellipsis-object "Link to this heading")

This object is commonly used to indicate that something is omitted.
It supports no special operations. There is exactly one ellipsis object, named
[`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "Ellipsis") (a built-in name). `type(Ellipsis)()` produces the
`Ellipsis` singleton.

It is written as `Ellipsis` or `...`.

In typical use, `...` as the `Ellipsis` object appears in a few different
places, for instance:

- In type annotations, such as [callable arguments](https://docs.python.org/3/library/typing.html#annotating-callables)
  or [tuple elements](https://docs.python.org/3/library/typing.html#annotating-tuples).
- As the body of a function instead of a [pass statement](https://docs.python.org/3/tutorial/controlflow.html#tut-pass).
- In third-party libraries, such as [Numpy’s slicing and striding](https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding).

Python also uses three dots in ways that are not `Ellipsis` objects, for instance:

- Doctest’s [`ELLIPSIS`](https://docs.python.org/3/library/doctest.html#doctest.ELLIPSIS "doctest.ELLIPSIS"), as a pattern for missing content.
- The default Python prompt of the [interactive](https://docs.python.org/3/glossary.html#term-interactive) shell when partial input is incomplete.

Lastly, the Python documentation often uses three dots in conventional English
usage to mean omitted content, even in code examples that also use them as the
`Ellipsis`.