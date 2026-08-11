---
id: python-performance-notes-https-docs-python-org-3-library-bisect-htm-e1b9427f
type: concept
title: Performance Notes[¶](https://docs.python.org/3/library/bisect.html#performance-notes
  "Link to this heading")
description: When writing time sensitive code using *bisect()* and *insort()*, keep
  these
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bisect.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Performance Notes[¶](https://docs.python.org/3/library/bisect.html#performance-notes "Link to this heading")

When writing time sensitive code using *bisect()* and *insort()*, keep these
thoughts in mind:

- Bisection is effective for searching ranges of values.
  For locating specific values, dictionaries are more performant.
- The *insort()* functions are *O*(*n*) because the logarithmic search step
  is dominated by the linear time insertion step.
- The search functions are stateless and discard key function results after
  they are used. Consequently, if the search functions are used in a loop,
  the key function may be called again and again on the same array elements.
  If the key function isn’t fast, consider wrapping it with
  [`@functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache "functools.cache") to avoid duplicate computations. Alternatively,
  consider searching an array of precomputed keys to locate the insertion
  point (as shown in the examples section below).

See also

- [Sorted Collections](https://grantjenks.com/docs/sortedcollections/) is a high performance
  module that uses *bisect* to managed sorted collections of data.
- The [SortedCollection recipe](https://code.activestate.com/recipes/577197-sortedcollection/) uses
  bisect to build a full-featured collection class with straight-forward search
  methods and support for a key-function. The keys are precomputed to save
  unnecessary calls to the key function during searches.