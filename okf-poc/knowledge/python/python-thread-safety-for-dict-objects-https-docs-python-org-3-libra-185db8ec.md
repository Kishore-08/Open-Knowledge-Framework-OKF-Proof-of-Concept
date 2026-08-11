---
id: python-thread-safety-for-dict-objects-https-docs-python-org-3-libra-185db8ec
type: concept
title: Thread safety for dict objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-dict-objects
  "Link to this heading")
description: Creating a dictionary with the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict
  "dict") constructor is atomic when the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Thread safety for dict objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-dict-objects "Link to this heading")

Creating a dictionary with the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") constructor is atomic when the
argument to it is a `dict` or a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). When using the
[`dict.fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys "dict.fromkeys") method, dictionary creation is atomic when the
argument is a `dict`, `tuple`, [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or
[`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset").

The following operations and functions are [lock-free](https://docs.python.org/3/glossary.html#term-lock-free) and
[atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).

```
d[key]       # dict.__getitem__
d.get(key)   # dict.get
key in d     # dict.__contains__
len(d)       # dict.__len__
```

All other operations from here on hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock).

Writing or removing a single item is safe to call from multiple threads
and will not corrupt the dictionary:

```
d[key] = value        # write
del d[key]            # delete
d.pop(key)            # remove and return
d.popitem()           # remove and return last item
d.setdefault(key, v)  # insert if missing
```

These operations may compare keys using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"), which can
execute arbitrary Python code. During such comparisons, the dictionary may
be modified by another thread. For built-in types like [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
[`int`](https://docs.python.org/3/library/functions.html#int "int"), and [`float`](https://docs.python.org/3/library/functions.html#float "float"), that implement `__eq__()` in C,
the underlying lock is not released during comparisons and this is not a
concern.

The following operations return new objects and hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
for the duration of the operation:

```
d.copy()      # returns a shallow copy of the dictionary
d | other     # merges two dicts into a new dict
d.keys()      # returns a new dict_keys view object
d.values()    # returns a new dict_values view object
d.items()     # returns a new dict_items view object
```

The [`clear()`](https://docs.python.org/3/library/stdtypes.html#dict.clear "dict.clear") method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations lock both dictionaries. For [`update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update")
and `|=`, this applies only when the other operand is a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")
that uses the standard dict iterator (but not subclasses that override
iteration). For equality comparison, this applies to `dict` and
its subclasses:

```
d.update(other_dict)  # both locked when other_dict is a dict
d |= other_dict       # both locked when other_dict is a dict
d == other_dict       # both locked for dict and subclasses
```

All comparison operations also compare values using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"),
so for non-built-in types the lock may be released during comparison.

[`fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys "dict.fromkeys") locks both the new dictionary and the iterable
when the iterable is exactly a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), or
[`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") (not subclasses):

```
dict.fromkeys(a_dict)