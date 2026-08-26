---
id: python-functools-higher-order-functions-and-operations-on-callable--1cd9df78
type: concept
title: '`functools` — Higher-order functions and operations on callable objects[¶](https'
description: '**Source code:** [Lib/functools.py](https://github.com/python/cpython/tree/3.14/Lib/functools.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/functools.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `functools` — Higher-order functions and operations on callable objects[¶](https://docs.python.org/3/library/functools.html#module-functools "Link to this heading")

**Source code:** [Lib/functools.py](https://github.com/python/cpython/tree/3.14/Lib/functools.py)

---

The `functools` module is for higher-order functions: functions that act on
or return other functions. In general, any callable object can be treated as a
function for the purposes of this module.

The `functools` module defines the following functions:

@functools.cache(*user\_function*)[¶](https://docs.python.org/3/library/functools.html#functools.cache "Link to this definition")
:   Simple lightweight unbounded function cache. Sometimes called
    [“memoize”](https://en.wikipedia.org/wiki/Memoization).

    Returns the same as `lru_cache(maxsize=None)`, creating a thin
    wrapper around a dictionary lookup for the function arguments. Because it
    never needs to evict old values, this is smaller and faster than
    [`@lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache") with a size limit.

    For example:

    ```
    @cache
    def factorial(n):
        return n * factorial(n-1) if n else 1

    >>> factorial(10)   # no previously cached result, makes 11 recursive calls
    3628800
    >>> factorial(5)    # no new calls, just returns the cached result
    120
    >>> factorial(12)   # two new recursive calls, factorial(10) is cached
    479001600
    ```

    The cache is threadsafe so that the wrapped function can be used in
    multiple threads. This means that the underlying data structure will
    remain coherent during concurrent updates.

    It is possible for the wrapped function to be called more than once if
    another thread makes an additional call before the initial call has been
    completed and cached.

    Added in version 3.9.

@functools.cached\_property(*func*)[¶](https://docs.python.org/3/library/functools.html#functools.cached_property "Link to this definition")
:   Transform a method of a class into a property whose value is computed once
    and then cached as a normal attribute for the life of the instance. Similar
    to [`@property`](https://docs.python.org/3/library/functions.html#property "property"), with the addition of caching. Useful for expensive
    computed properties of instances that are otherwise effectively immutable.

    Example:

    ```
    class DataSet:

        def __init__(self, sequence_of_numbers):
            self._data = tuple(sequence_of_numbers)

        @cached_property
        def stdev(self):
            return statistics.stdev(self._data)
    ```

    The mechanics of [`@cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property "functools.cached_property") are somewhat different from
    [`@property`](https://docs.python.org/3/library/functions.html#property "property"). A regular property blocks attribute writes unless a
    setter is defined. In contrast, a *cached\_property* allows writes.

    The *cached\_property* decorator only runs on lookups and only when an
    attribute of the same name doesn’t exist. When it does run, the
    *cached\_property* writes to the attribute with the same name. Subsequent
    attribute reads and writes take precedence over the *cached\_property*
    method and it works like a normal attribute.

    The cached value can be cleared by deleting the attribute. This
    allows the *cached\_property* method to run again.

    The *cached\_property* does not prevent a possible race condition in
    multi-threaded usage. The getter function could run more than once on the
    same instance, with the latest run setting the cached value. If the cached
    property is idempotent or otherwise not harmful to run more than once on an
    instance, this is fine. If synchronization is needed, implement the necessary
    locking inside the decorated getter function or around the cached pro