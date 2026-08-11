---
id: python-ranges-https-docs-python-org-3-library-stdtypes-html-ranges--5e0bc1d7
type: concept
title: Ranges[¶](https://docs.python.org/3/library/stdtypes.html#ranges "Link to this
  heading")
description: The [`range`](https://docs.python.org/3/library/stdtypes.html#range "range")
  type represents an immutable sequence of numbers and is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Ranges[¶](https://docs.python.org/3/library/stdtypes.html#ranges "Link to this heading")

The [`range`](https://docs.python.org/3/library/stdtypes.html#range "range") type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
loops.

*class* range(*stop*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#range "Link to this definition")

*class* range(*start*, *stop*, *step=1*, */*)
:   The arguments to the range constructor must be integers (either built-in
    [`int`](https://docs.python.org/3/library/functions.html#int "int") or any object that implements the [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") special
    method). If the *step* argument is omitted, it defaults to `1`.
    If the *start* argument is omitted, it defaults to `0`.
    If *step* is zero, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

    For a positive *step*, the contents of a range `r` are determined by the
    formula `r[i] = start + step*i` where `i >= 0` and
    `r[i] < stop`.

    For a negative *step*, the contents of the range are still determined by
    the formula `r[i] = start + step*i`, but the constraints are `i >= 0`
    and `r[i] > stop`.

    A range object will be empty if `r[0]` does not meet the value
    constraint. Ranges do support negative indices, but these are interpreted
    as indexing from the end of the sequence determined by the positive
    indices.

    Ranges containing absolute values larger than [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize") are
    permitted but some features (such as [`len()`](https://docs.python.org/3/library/functions.html#len "len")) may raise
    [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError").

    Range examples:

    ```
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(1, 11))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> list(range(0, 30, 5))
    [0, 5, 10, 15, 20, 25]
    >>> list(range(0, 10, 3))
    [0, 3, 6, 9]
    >>> list(range(0, -10, -1))
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> list(range(0))
    []
    >>> list(range(1, 0))
    []
    ```

    Ranges implement all of the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common) sequence operations
    except concatenation and repetition (due to the fact that range objects can
    only represent sequences that follow a strict pattern and repetition and
    concatenation will usually violate that pattern).

    start[¶](https://docs.python.org/3/library/stdtypes.html#range.start "Link to this definition")
    :   The value of the *start* parameter (or `0` if the parameter was
        not supplied)

    stop[¶](https://docs.python.org/3/library/stdtypes.html#range.stop "Link to this definition")
    :   The value of the *stop* parameter

    step[¶](https://docs.python.org/3/library/stdtypes.html#range.step "Link to this definition")
    :   The value of the *step* parameter (or `1` if the parameter was
        not supplied)

The advantage of the [`range`](https://docs.python.org/3/library/stdtypes.html#range "range") type over a regular [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or
[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") is that a `range` object will always take the same
(small) amount of memory, no matter the size of the range it represents (as it
only stores the `start`, `stop` and `step` values, calculating individual
items and subranges as needed).

Range objects implement the [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") ABC, and provide
features such as containment tests, element index lookup, sli