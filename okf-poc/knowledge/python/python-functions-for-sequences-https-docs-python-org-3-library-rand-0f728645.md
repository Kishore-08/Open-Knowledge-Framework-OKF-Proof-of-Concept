---
id: python-functions-for-sequences-https-docs-python-org-3-library-rand-0f728645
type: concept
title: Functions for sequences[¶](https://docs.python.org/3/library/random.html#functions-for-sequences
  "Link to this heading")
description: random.choice(*seq*)[¶](https://docs.python.org/3/library/random.html#random.choice
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Functions for sequences[¶](https://docs.python.org/3/library/random.html#functions-for-sequences "Link to this heading")

random.choice(*seq*)[¶](https://docs.python.org/3/library/random.html#random.choice "Link to this definition")
:   Return a random element from the non-empty sequence *seq*. If *seq* is empty,
    raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError").

random.choices(*population*, *weights=None*, *\**, *cum\_weights=None*, *k=1*)[¶](https://docs.python.org/3/library/random.html#random.choices "Link to this definition")
:   Return a *k* sized list of elements chosen from the *population* with replacement.
    If the *population* is empty, raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError").

    If a *weights* sequence is specified, selections are made according to the
    relative weights. Alternatively, if a *cum\_weights* sequence is given, the
    selections are made according to the cumulative weights (perhaps computed
    using [`itertools.accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate")). For example, the relative weights
    `[10, 5, 30, 5]` are equivalent to the cumulative weights
    `[10, 15, 45, 50]`. Internally, the relative weights are converted to
    cumulative weights before making selections, so supplying the cumulative
    weights saves work.

    If neither *weights* nor *cum\_weights* are specified, selections are made
    with equal probability. If a weights sequence is supplied, it must be
    the same length as the *population* sequence. It is a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError")
    to specify both *weights* and *cum\_weights*.

    The *weights* or *cum\_weights* can use any numeric type that interoperates
    with the [`float`](https://docs.python.org/3/library/functions.html#float "float") values returned by [`random()`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") (that includes
    integers, floats, and fractions but excludes decimals). Weights are assumed
    to be non-negative and finite. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if all
    weights are zero.

    For a given seed, the `choices()` function with equal weighting
    typically produces a different sequence than repeated calls to
    [`choice()`](https://docs.python.org/3/library/random.html#random.choice "random.choice"). The algorithm used by `choices()` uses floating-point
    arithmetic for internal consistency and speed. The algorithm used
    by `choice()` defaults to integer arithmetic with repeated selections
    to avoid small biases from round-off error.

    Added in version 3.6.

    Changed in version 3.9: Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if all weights are zero.

random.shuffle(*x*)[¶](https://docs.python.org/3/library/random.html#random.shuffle "Link to this definition")
:   Shuffle the sequence *x* in place.

    To shuffle an immutable sequence and return a new shuffled list, use
    `sample(x, k=len(x))` instead.

    Note that even for small `len(x)`, the total number of permutations of *x*
    can quickly grow larger than the period of most random number generators.
    This implies that most permutations of a long sequence can never be
    generated. For example, a sequence of length 2080 is the largest that
    can fit within the period of the Mersenne Twister random number generator.

    Changed in version 3.11: Removed the optional parameter *random*.

random.sample(*population*, *k*, *\**, *counts=None*)[¶](https://docs.python.org/3/library/random.html#random.sample "Link to this definition")
:   Return a *k* length list of unique elements chosen from the population
    sequen