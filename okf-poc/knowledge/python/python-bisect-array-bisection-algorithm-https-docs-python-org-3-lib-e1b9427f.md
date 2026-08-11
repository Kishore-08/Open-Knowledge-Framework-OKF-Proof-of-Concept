---
id: python-bisect-array-bisection-algorithm-https-docs-python-org-3-lib-e1b9427f
type: concept
title: '`bisect` — Array bisection algorithm[¶](https://docs.python.org/3/library/bisect'
description: '**Source code:** [Lib/bisect.py](https://github.com/python/cpython/tree/3.14/Lib/bisect.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bisect.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `bisect` — Array bisection algorithm[¶](https://docs.python.org/3/library/bisect.html#module-bisect "Link to this heading")

**Source code:** [Lib/bisect.py](https://github.com/python/cpython/tree/3.14/Lib/bisect.py)

---

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over
linear searches or frequent resorting.

The module is called `bisect` because it uses a basic bisection
algorithm to do its work. Unlike other bisection tools that search for a
specific value, the functions in this module are designed to locate an
insertion point. Accordingly, the functions never call an [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
method to determine whether a value has been found. Instead, the
functions only call the [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__") method and will return an insertion
point between values in an array.

Note

The functions in this module are not thread-safe. If multiple threads
concurrently use `bisect` functions on the same sequence, this
may result in undefined behaviour. Likewise, if the provided sequence
is mutated by a different thread while a `bisect` function
is operating on it, the result is undefined. For example, using
[`insort_left()`](https://docs.python.org/3/library/bisect.html#bisect.insort_left "bisect.insort_left") on the same list from multiple threads
may result in the list becoming unsorted.

The following functions are provided:

bisect.bisect\_left(*a*, *x*, *lo=0*, *hi=len(a)*, *\**, *key=None*)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "Link to this definition")
:   Locate the insertion point for *x* in *a* to maintain sorted order.
    The parameters *lo* and *hi* may be used to specify a subset of the list
    which should be considered; by default the entire list is used. If *x* is
    already present in *a*, the insertion point will be before (to the left of)
    any existing entries. The return value is suitable for use as the first
    parameter to `list.insert()` assuming that *a* is already sorted.

    The returned insertion point *ip* partitions the array *a* into two
    slices such that `all(elem < x for elem in a[lo : ip])` is true for the
    left slice and `all(elem >= x for elem in a[ip : hi])` is true for the
    right slice.

    *key* specifies a [key function](https://docs.python.org/3/glossary.html#term-key-function) of one argument that is used to
    extract a comparison key from each element in the array. To support
    searching complex records, the key function is not applied to the *x* value.

    If *key* is `None`, the elements are compared directly and
    no key function is called.

    Changed in version 3.10: Added the *key* parameter.

bisect.bisect\_right(*a*, *x*, *lo=0*, *hi=len(a)*, *\**, *key=None*)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect_right "Link to this definition")

bisect.bisect(*a*, *x*, *lo=0*, *hi=len(a)*, *\**, *key=None*)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect "Link to this definition")
:   Similar to [`bisect_left()`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "bisect.bisect_left"), but returns an insertion point which comes
    after (to the right of) any existing entries of *x* in *a*.

    The returned insertion point *ip* partitions the array *a* into two slices
    such that `all(elem <= x for elem in a[lo : ip])` is true for the left slice and
    `all(elem > x for elem in a[ip : hi])` is true for the right slice.

    Changed in version 3.10: Added the *key* parameter.

bisect.insort\_left(*a*, *x*, *lo=0*, *hi=len(a)*, *\**, *key=None*)[¶](https://docs.python.org/3/library/bisect.html#bisect.insort_left "Link to this definition")
:   Insert *x* in *a* in sorted order.

    T