---
id: python-thread-safety-for-list-objects-https-docs-python-org-3-libra-185db8ec
type: concept
title: Thread safety for list objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects
  "Link to this heading")
description: Reading a single element from a [`list`](https://docs.python.org/3/library/stdtypes.html#list
  "list") is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Thread safety for list objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects "Link to this heading")

Reading a single element from a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") is
[atomic](https://docs.python.org/3/glossary.html#term-atomic-operation):

```
lst[i]   # list.__getitem__
```

The following methods traverse the list and use [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
reads of each item to perform their function. That means that they may
return results affected by concurrent modifications:

```
item in lst
lst.index(item)
lst.count(item)
```

All of the above operations avoid acquiring [per-object locks](https://docs.python.org/3/glossary.html#term-per-object-lock). They do not block concurrent modifications. Other
operations that hold a lock will not block these from observing intermediate
states.

All other operations from here on block using the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock).

Writing a single item via `lst[i] = x` is safe to call from multiple
threads and will not corrupt the list.

The following operations return new objects and appear
[atomic](https://docs.python.org/3/glossary.html#term-atomic-operation) to other threads:

```
lst1 + lst2    # concatenates two lists into a new list
x * lst        # repeats lst x times into a new list
lst.copy()     # returns a shallow copy of the list
```

The following methods that only operate on a single element with no shifting
required are [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation):

```
lst.append(x)  # append to the end of the list, no shifting required
lst.pop()      # pop element from the end of the list, no shifting required
```

The [`clear()`](https://docs.python.org/3/library/stdtypes.html#list.clear "list.clear") method is also [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).
Other threads cannot observe elements being removed.

The [`sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort") method is not [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).
Other threads cannot observe intermediate states during sorting, but the
list appears empty for the duration of the sort.

The following operations may allow [lock-free](https://docs.python.org/3/glossary.html#term-lock-free) operations to observe
intermediate states since they modify multiple elements in place:

```
lst.insert(idx, item)  # shifts elements
lst.pop(idx)           # idx not at the end of the list, shifts elements
lst *= x               # copies elements in place
```

The [`remove()`](https://docs.python.org/3/library/stdtypes.html#list.remove "list.remove") method may allow concurrent modifications since
element comparison may execute arbitrary Python code (via
[`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")).

[`extend()`](https://docs.python.org/3/library/stdtypes.html#list.extend "list.extend") is safe to call from multiple threads. However, its
guarantees depend on the iterable passed to it. If it is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), a
[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") or a
[dictionary view object](https://docs.python.org/3/library/stdtypes.html#dict-views) (but not their subclasses), the
`extend` operation is safe from concurrent modifications to the iterable.
Otherwise, an iterator is created which can be concurrently modified by
another thread. The same applies to inplace concatenation of a list with
other iterables when using `lst += iterable`.

Similarly, assigning to a list slice with `lst[i:j]