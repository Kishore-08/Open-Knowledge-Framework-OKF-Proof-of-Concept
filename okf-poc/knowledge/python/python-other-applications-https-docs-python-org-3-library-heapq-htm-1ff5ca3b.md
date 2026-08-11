---
id: python-other-applications-https-docs-python-org-3-library-heapq-htm-1ff5ca3b
type: concept
title: Other Applications[¶](https://docs.python.org/3/library/heapq.html#other-applications
  "Link to this heading")
description: '[Medians](https://en.wikipedia.org/wiki/Median) are a measure of'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/heapq.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Other Applications[¶](https://docs.python.org/3/library/heapq.html#other-applications "Link to this heading")

[Medians](https://en.wikipedia.org/wiki/Median) are a measure of
central tendency for a set of numbers. In distributions skewed by
outliers, the median provides a more stable estimate than an average
(arithmetic mean). A running median is an [online algorithm](https://en.wikipedia.org/wiki/Online_algorithm) that updates
continuously as new data arrives.

A running median can be efficiently implemented by balancing two heaps,
a max-heap for values at or below the midpoint and a min-heap for values
above the midpoint. When the two heaps have the same size, the new
median is the average of the tops of the two heaps; otherwise, the
median is at the top of the larger heap:

```
def running_median(iterable):
    "Yields the cumulative median of values seen so far."

    lo = []  # max-heap
    hi = []  # min-heap (same size as or one smaller than lo)

    for x in iterable:
        if len(lo) == len(hi):
            heappush_max(lo, heappushpop(hi, x))
            yield lo[0]
        else:
            heappush(hi, heappushpop_max(lo, x))
            yield (lo[0] + hi[0]) / 2
```

For example:

```
>>> list(running_median([5.0, 9.0, 4.0, 12.0, 8.0, 9.0]))
[5.0, 7.0, 5.0, 7.0, 8.0, 8.5]
```