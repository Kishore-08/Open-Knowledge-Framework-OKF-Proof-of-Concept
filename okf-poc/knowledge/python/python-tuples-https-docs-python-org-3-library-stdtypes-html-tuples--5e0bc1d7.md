---
id: python-tuples-https-docs-python-org-3-library-stdtypes-html-tuples--5e0bc1d7
type: concept
title: Tuples[¶](https://docs.python.org/3/library/stdtypes.html#tuples "Link to this
  heading")
description: Tuples are immutable sequences, typically used to store collections of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Tuples[¶](https://docs.python.org/3/library/stdtypes.html#tuples "Link to this heading")

Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate")
built-in). Tuples are also used for cases where an immutable sequence of
homogeneous data is needed (such as allowing storage in a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") instance).

*class* tuple(*iterable=()*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#tuple "Link to this definition")
:   Tuples may be constructed in a number of ways:

    - Using a pair of parentheses to denote the empty tuple: `()`
    - Using a trailing comma for a singleton tuple: `a,` or `(a,)`
    - Separating items with commas: `a, b, c` or `(a, b, c)`
    - Using the [`tuple()`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") built-in: `tuple()` or `tuple(iterable)`

    The constructor builds a tuple whose items are the same and in the same
    order as *iterable*’s items. *iterable* may be either a sequence, a
    container that supports iteration, or an iterator object. If *iterable*
    is already a tuple, it is returned unchanged. For example,
    `tuple('abc')` returns `('a', 'b', 'c')` and
    `tuple( [1, 2, 3] )` returns `(1, 2, 3)`.
    If no argument is given, the constructor creates a new empty tuple, `()`.

    Note that it is actually the comma which makes a tuple, not the parentheses.
    The parentheses are optional, except in the empty tuple case, or
    when they are needed to avoid syntactic ambiguity. For example,
    `f(a, b, c)` is a function call with three arguments, while
    `f((a, b, c))` is a function call with a 3-tuple as the sole argument.

    Tuples implement all of the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common) sequence
    operations.

    Tuples are [generic](https://docs.python.org/3/library/typing.html#generics) over the types of their contents.
    For more information, refer to
    [the typing documentation on annotating tuples](https://docs.python.org/3/library/typing.html#annotating-tuples).

For heterogeneous collections of data where access by name is clearer than
access by index, [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") may be a more appropriate
choice than a simple tuple object.