---
id: python-ordereddict-https-docs-python-org-3-library-collections-html-4b36d233
type: concept
title: '[`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict
  "collections.OrderedDict") Examples and Recipes[¶](https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
  "Link to this heading")'
description: It is straightforward to create an ordered dictionary variant
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") Examples and Recipes[¶](https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes "Link to this heading")

It is straightforward to create an ordered dictionary variant
that remembers the order the keys were *last* inserted.
If a new entry overwrites an existing entry, the
original insertion position is changed and moved to the end:

```
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
```

An [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") would also be useful for implementing
variants of [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache"):

```
from collections import OrderedDict
from time import monotonic

class TimeBoundedLRU:
    "LRU Cache that invalidates and refreshes old entries."

    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()      # { args : (timestamp, result)}
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if monotonic() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = monotonic(), result
        if len(self.cache) > self.maxsize:
            self.cache.popitem(last=False)
        return result
```

```
class MultiHitLRUCache:
    """ LRU cache that defers caching a result until
        it has been requested multiple times.

        To avoid flushing the LRU cache with one-time requests,
        we don't cache until a request has been made more than once.

    """

    def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
        self.requests = OrderedDict()   # { uncached_key : request_count }
        self.cache = OrderedDict()      # { cached_key : function_result }
        self.func = func
        self.maxrequests = maxrequests  # max number of uncached requests
        self.maxsize = maxsize          # max number of stored return values
        self.cache_after = cache_after

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            return self.cache[args]
        result = self.func(*args)
        self.requests[args] = self.requests.get(args, 0) + 1
        if self.requests[args] <= self.cache_after:
            self.requests.move_to_end(args)
            if len(self.requests) > self.maxrequests:
                self.requests.popitem(last=False)
        else:
            self.requests.pop(args, None)
            self.cache[args] = result
            if len(self.cache) > self.maxsize:
                self.cache.popitem(last=False)
        return result
```