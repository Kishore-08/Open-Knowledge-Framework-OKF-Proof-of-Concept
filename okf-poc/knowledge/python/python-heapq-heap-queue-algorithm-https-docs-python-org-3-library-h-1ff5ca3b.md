---
id: python-heapq-heap-queue-algorithm-https-docs-python-org-3-library-h-1ff5ca3b
type: concept
title: '`heapq` — Heap queue algorithm[¶](https://docs.python.org/3/library/heapq.html#m'
description: '**Source code:** [Lib/heapq.py](https://github.com/python/cpython/tree/3.14/Lib/heapq.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/heapq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `heapq` — Heap queue algorithm[¶](https://docs.python.org/3/library/heapq.html#module-heapq "Link to this heading")

**Source code:** [Lib/heapq.py](https://github.com/python/cpython/tree/3.14/Lib/heapq.py)

---

This module provides an implementation of the heap queue algorithm, also known
as the priority queue algorithm.

Min-heaps are binary trees for which every parent node has a value less than
or equal to any of its children.
We refer to this condition as the heap invariant.

For min-heaps, this implementation uses lists for which
`heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all *k* for which
the compared elements exist. Elements are counted from zero. The interesting
property of a min-heap is that its smallest element is always the root,
`heap[0]`.

Max-heaps satisfy the reverse invariant: every parent node has a value
*greater* than any of its children. These are implemented as lists for which
`maxheap[2*k+1] <= maxheap[k]` and `maxheap[2*k+2] <= maxheap[k]` for all
*k* for which the compared elements exist.
The root, `maxheap[0]`, contains the *largest* element;
`heap.sort(reverse=True)` maintains the max-heap invariant.

The `heapq` API differs from textbook heap algorithms in two aspects: (a)
We use zero-based indexing. This makes the relationship between the index for
a node and the indexes for its children slightly less obvious, but is more
suitable since Python uses zero-based indexing. (b) Textbooks often focus on
max-heaps, due to their suitability for in-place sorting. Our implementation
favors min-heaps as they better correspond to Python [`lists`](https://docs.python.org/3/library/stdtypes.html#list "list").

These two aspects make it possible to view the heap as a regular Python list
without surprises: `heap[0]` is the smallest item, and `heap.sort()`
maintains the heap invariant!

Like [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort"), this implementation uses only the `<` operator
for comparisons, for both min-heaps and max-heaps.

In the API below, and in this documentation, the unqualified term *heap*
generally refers to a min-heap.
The API for max-heaps is named using a `_max` suffix.

To create a heap, use a list initialized as `[]`, or transform an existing list
into a min-heap or max-heap using the [`heapify()`](https://docs.python.org/3/library/heapq.html#heapq.heapify "heapq.heapify") or [`heapify_max()`](https://docs.python.org/3/library/heapq.html#heapq.heapify_max "heapq.heapify_max")
functions, respectively.

The following functions are provided for min-heaps:

heapq.heapify(*x*)[¶](https://docs.python.org/3/library/heapq.html#heapq.heapify "Link to this definition")
:   Transform list *x* into a min-heap, in-place, in linear time.

heapq.heappush(*heap*, *item*)[¶](https://docs.python.org/3/library/heapq.html#heapq.heappush "Link to this definition")
:   Push the value *item* onto the *heap*, maintaining the min-heap invariant.

heapq.heappop(*heap*)[¶](https://docs.python.org/3/library/heapq.html#heapq.heappop "Link to this definition")
:   Pop and return the smallest item from the *heap*, maintaining the min-heap
    invariant. If the heap is empty, [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") is raised. To access the
    smallest item without popping it, use `heap[0]`.

heapq.heappushpop(*heap*, *item*)[¶](https://docs.python.org/3/library/heapq.html#heapq.heappushpop "Link to this definition")
:   Push *item* on the heap, then pop and return the smallest item from the
    *heap*. The combined action runs more efficiently than [`heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "heapq.heappush")
    followed by a separate call to [`heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "heapq.heappop").

heapq.heapreplace(*heap*, *item*)[¶](https://docs.python.org/3/library/heapq.html#heapq.heapreplace "Link to this definition")
:   Pop and return the smal