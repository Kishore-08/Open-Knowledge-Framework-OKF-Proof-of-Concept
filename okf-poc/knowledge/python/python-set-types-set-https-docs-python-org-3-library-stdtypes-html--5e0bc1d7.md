---
id: python-set-types-set-https-docs-python-org-3-library-stdtypes-html--5e0bc1d7
type: concept
title: Set Types — [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"),
  [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")[¶](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
  "Link to this heading")
description: A *set* object is an unordered collection of distinct [hashable](https://docs.python.org/3/glossary.html#term-hashable)
  objects.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Set Types — [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")[¶](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset "Link to this heading")

A *set* object is an unordered collection of distinct [hashable](https://docs.python.org/3/glossary.html#term-hashable) objects.
Common uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference.
(For other containers see the built-in [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"),
and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") classes, and the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.)

Like other collections, sets support `x in set`, `len(set)`, and `for x in
set`. Being an unordered collection, sets do not record element position or
order of insertion. Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior.

There are currently two built-in set types, [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset").
The `set` type is mutable — the contents can be changed using methods
like [`add()`](https://docs.python.org/3/library/stdtypes.html#set.add "set.add") and [`remove()`](https://docs.python.org/3/library/stdtypes.html#set.remove "set.remove").
Since it is mutable, it has no hash value and cannot be used as
either a dictionary key or as an element of another set.
The `frozenset` type is immutable and [hashable](https://docs.python.org/3/glossary.html#term-hashable) —
its contents cannot be altered after it is created;
it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list
of elements within braces, for example: `{'jack', 'sjoerd'}`, in addition to the
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set") constructor.

The constructors for both classes work the same:

*class* set(*iterable=()*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#set "Link to this definition")

*class* frozenset(*iterable=()*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#frozenset "Link to this definition")
:   Return a new set or frozenset object whose elements are taken from
    *iterable*. The elements of a set must be [hashable](https://docs.python.org/3/glossary.html#term-hashable). To
    represent sets of sets, the inner sets must be `frozenset`
    objects. If *iterable* is not specified, a new empty set is
    returned.

Sets can be created by several means:

- Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`
- Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`
- Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`

Instances of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") provide the following
operations:

len(s)
:   Return the number of elements in set *s* (cardinality of *s*).

x in s
:   Test *x* for membership in *s*.

x not in s
:   Test *x* for non-membership in *s*.

frozenset.isdisjoint(*other*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#frozenset.isdisjoint "Link to this definition")

set.isdisjoint(*other*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#set.isdisjoint "Link to this definition")
:   Return `True` if the set has no elements in common with *other*. Sets are
    disjoint if and only if their intersection is the empty set.

frozenset.issubset(*other*, */*)[¶](https://do