---
id: python-itertools-recipes-https-docs-python-org-3-library-itertools--4a9248d3
type: concept
title: Itertools Recipes[¶](https://docs.python.org/3/library/itertools.html#itertools-recipes
  "Link to this heading")
description: This section shows recipes for creating an extended toolset using the
  existing
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/itertools.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Itertools Recipes[¶](https://docs.python.org/3/library/itertools.html#itertools-recipes "Link to this heading")

This section shows recipes for creating an extended toolset using the existing
itertools as building blocks.

The primary purpose of the itertools recipes is educational. The recipes show
various ways of thinking about individual tools — for example, that
`chain.from_iterable` is related to the concept of flattening. The recipes
also give ideas about ways that the tools can be combined — for example, how
`starmap()` and `repeat()` can work together. The recipes also show patterns
for using itertools with the [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.") and [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") modules as
well as with the built-in itertools such as `map()`, `filter()`,
`reversed()`, and `enumerate()`.

A secondary purpose of the recipes is to serve as an incubator. The
`accumulate()`, `compress()`, and `pairwise()` itertools started out as
recipes. Currently, the `sliding_window()`, `derangements()`, and `sieve()`
recipes are being tested to see whether they prove their worth.

Substantially all of these recipes and many, many others can be installed from
the [more-itertools](https://pypi.org/project/more-itertools/) project found
on the Python Package Index:

```
python -m pip install more-itertools
```

Many of the recipes offer the same high performance as the underlying toolset.
Superior memory performance is kept by processing elements one at a time rather
than bringing the whole iterable into memory all at once. Code volume is kept
small by linking the tools together in a [functional style](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf). High speed
is retained by preferring “vectorized” building blocks over the use of for-loops
and [generators](https://docs.python.org/3/glossary.html#term-generator) which incur interpreter overhead.

```
from itertools import (accumulate, batched, chain, combinations, compress,
     count, cycle, filterfalse, groupby, islice, permutations, product,
     repeat, starmap, tee, zip_longest)
from collections import Counter, deque
from contextlib import suppress
from functools import reduce
from heapq import heappush, heappushpop, heappush_max, heappushpop_max
from math import comb, isqrt, prod, sumprod
from operator import getitem, is_not, itemgetter, mul, neg, truediv


# ==== Basic one liners ====

def take(n, iterable):
    "Return first n items of the iterable as a list."
    return list(islice(iterable, n))

def prepend(value, iterable):
    "Prepend a single value in front of an iterable."
    # prepend(1, [2, 3, 4]) → 1 2 3 4
    return chain([value], iterable)

def repeatfunc(function, times=None, *args):
    "Repeat calls to a function with specified arguments."
    if times is None:
        return starmap(function, repeat(args))
    return starmap(function, repeat(args, times))

def flatten(list_of_lists):
    "Flatten one level of nesting."
    return chain.from_iterable(list_of_lists)

def ncycles(iterable, n):
    "Returns the sequence elements n times."
    return chain.from_iterable(repeat(tuple(iterable), n))

def loops(n):
    "Loop n times. Like range(n) but without creating integers."
    # for _ in loops(100): ...
    return repeat(None, n)

def tail(n, iterable):
    "Return an iterator over the last n items."
    # tail(3, 'ABCDEFG') → E F G
    return iter(deque(iterable, maxlen=n))

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)

def nth(iterable, n, default=None):
    "Returns the nth item or a default value."
    return next(islice(iterable, n, N