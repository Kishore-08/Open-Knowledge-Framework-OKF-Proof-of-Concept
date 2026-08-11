---
id: python-functions-for-integers-https-docs-python-org-3-library-rando-0f728645
type: concept
title: Functions for integers[¶](https://docs.python.org/3/library/random.html#functions-for-integers
  "Link to this heading")
description: random.randrange(*stop*)[¶](https://docs.python.org/3/library/random.html#random.randrange
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Functions for integers[¶](https://docs.python.org/3/library/random.html#functions-for-integers "Link to this heading")

random.randrange(*stop*)[¶](https://docs.python.org/3/library/random.html#random.randrange "Link to this definition")

random.randrange(*start*, *stop*[, *step*])
:   Return a randomly selected element from `range(start, stop, step)`.

    This is roughly equivalent to `choice(range(start, stop, step))` but
    supports arbitrarily large ranges and is optimized for common cases.

    The positional argument pattern matches the [`range()`](https://docs.python.org/3/library/stdtypes.html#range "range") function.

    Keyword arguments should not be used because they can be interpreted
    in unexpected ways. For example `randrange(start=100)` is interpreted
    as `randrange(0, 100, 1)`.

    Changed in version 3.2: `randrange()` is more sophisticated about producing equally distributed
    values. Formerly it used a style like `int(random()*n)` which could produce
    slightly uneven distributions.

    Changed in version 3.12: Automatic conversion of non-integer types is no longer supported.
    Calls such as `randrange(10.0)` and `randrange(Fraction(10, 1))`
    now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

random.randint(*a*, *b*)[¶](https://docs.python.org/3/library/random.html#random.randint "Link to this definition")
:   Return a random integer *N* such that `a <= N <= b`. Alias for
    `randrange(a, b+1)`.

random.getrandbits(*k*)[¶](https://docs.python.org/3/library/random.html#random.getrandbits "Link to this definition")
:   Returns a non-negative Python integer with *k* random bits. This method
    is supplied with the Mersenne Twister generator and some other generators
    may also provide it as an optional part of the API. When available,
    `getrandbits()` enables [`randrange()`](https://docs.python.org/3/library/random.html#random.randrange "random.randrange") to handle arbitrarily large
    ranges.

    Changed in version 3.9: This method now accepts zero for *k*.