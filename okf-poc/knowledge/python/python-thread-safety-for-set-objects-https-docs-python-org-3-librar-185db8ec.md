---
id: python-thread-safety-for-set-objects-https-docs-python-org-3-librar-185db8ec
type: concept
title: Thread safety for set objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-set-objects
  "Link to this heading")
description: The [`len()`](https://docs.python.org/3/library/functions.html#len "len")
  function is lock-free and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Thread safety for set objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-set-objects "Link to this heading")

The [`len()`](https://docs.python.org/3/library/functions.html#len "len") function is lock-free and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).

The following read operation is lock-free. It does not block concurrent
modifications and may observe intermediate states from operations that
hold the per-object lock:

```
elem in s    # set.__contains__
```

This operation may compare elements using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"), which can
execute arbitrary Python code. During such comparisons, the set may be
modified by another thread. For built-in types like [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
[`int`](https://docs.python.org/3/library/functions.html#int "int"), and [`float`](https://docs.python.org/3/library/functions.html#float "float"), `__eq__()` does not release the
underlying lock during comparisons and this is not a concern.

All other operations from here on hold the per-object lock.

Adding or removing a single element is safe to call from multiple threads
and will not corrupt the set:

```
s.add(elem)      # add element
s.remove(elem)   # remove element, raise if missing
s.discard(elem)  # remove element if present
s.pop()          # remove and return arbitrary element
```

These operations also compare elements, so the same [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
considerations as above apply.

The [`copy()`](https://docs.python.org/3/library/stdtypes.html#set.copy "set.copy") method returns a new object and holds the per-object lock
for the duration so that it is always atomic.

The [`clear()`](https://docs.python.org/3/library/stdtypes.html#set.clear "set.clear") method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations only accept [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")
as operands and always lock both objects:

```
s |= other                   # other must be set/frozenset
s &= other                   # other must be set/frozenset
s -= other                   # other must be set/frozenset
s ^= other                   # other must be set/frozenset
s & other                    # other must be set/frozenset
s | other                    # other must be set/frozenset
s - other                    # other must be set/frozenset
s ^ other                    # other must be set/frozenset
```

[`set.update()`](https://docs.python.org/3/library/stdtypes.html#set.update "set.update"), [`set.union()`](https://docs.python.org/3/library/stdtypes.html#set.union "set.union"), [`set.intersection()`](https://docs.python.org/3/library/stdtypes.html#set.intersection "set.intersection") and
[`set.difference()`](https://docs.python.org/3/library/stdtypes.html#set.difference "set.difference") can take multiple iterables as arguments. They all
iterate through all the passed iterables and do the following:

> - [`set.update()`](https://docs.python.org/3/library/stdtypes.html#set.update "set.update") and [`set.union()`](https://docs.python.org/3/library/stdtypes.html#set.union "set.union") lock both objects only when
>   :   the other operand is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), or [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").
> - [`set.intersection()`](https://docs.python.org/3/library/stdtypes.html#set.intersection "set.intersection") and [`set.difference()`](https://docs.python.org/3/library/stdtypes.html#set.difference "set.difference") always try to lock
>   :   all objects.

[`set.symmetric_difference()