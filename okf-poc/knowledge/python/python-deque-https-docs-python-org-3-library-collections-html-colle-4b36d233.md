---
id: python-deque-https-docs-python-org-3-library-collections-html-colle-4b36d233
type: concept
title: '[`deque`](https://docs.python.org/3/library/collections.html#collections.deque
  "collections.deque") Recipes[¶](https://docs.python.org/3/library/collections.html#deque-recipes
  "Link to this heading")'
description: This section shows various approaches to working with deques.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") Recipes[¶](https://docs.python.org/3/library/collections.html#deque-recipes "Link to this heading")

This section shows various approaches to working with deques.

Bounded length deques provide functionality similar to the `tail` filter
in Unix:

```
def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)
```

Another approach to using deques is to maintain a sequence of recently
added elements by appending to the right and popping to the left:

```
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
```

A [round-robin scheduler](https://en.wikipedia.org/wiki/Round-robin_scheduling) can be implemented with
input iterators stored in a [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque"). Values are yielded from the active
iterator in position zero. If that iterator is exhausted, it can be removed
with [`popleft()`](https://docs.python.org/3/library/collections.html#collections.deque.popleft "collections.deque.popleft"); otherwise, it can be cycled back to the end with
the [`rotate()`](https://docs.python.org/3/library/collections.html#collections.deque.rotate "collections.deque.rotate") method:

```
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()
```

The [`rotate()`](https://docs.python.org/3/library/collections.html#collections.deque.rotate "collections.deque.rotate") method provides a way to implement [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") slicing and
deletion. For example, a pure Python implementation of `del d[n]` relies on
the `rotate()` method to position elements to be popped:

```
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
```

To implement [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") slicing, use a similar approach applying
[`rotate()`](https://docs.python.org/3/library/collections.html#collections.deque.rotate "collections.deque.rotate") to bring a target element to the left side of the deque. Remove
old entries with [`popleft()`](https://docs.python.org/3/library/collections.html#collections.deque.popleft "collections.deque.popleft"), add new entries with [`extend()`](https://docs.python.org/3/library/collections.html#collections.deque.extend "collections.deque.extend"), and then
reverse the rotation.
With minor variations on that approach, it is easy to implement Forth style
stack manipulations such as `dup`, `drop`, `swap`, `over`, `pick`,
`rot`, and `roll`.