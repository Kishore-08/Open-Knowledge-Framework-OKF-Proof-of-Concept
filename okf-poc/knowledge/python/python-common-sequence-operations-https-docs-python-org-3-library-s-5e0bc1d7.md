---
id: python-common-sequence-operations-https-docs-python-org-3-library-s-5e0bc1d7
type: concept
title: Common Sequence Operations[¶](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
  "Link to this heading")
description: The operations in the following table are supported by most sequence
  types,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Common Sequence Operations[¶](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations "Link to this heading")

The operations in the following table are supported by most sequence types,
both mutable and immutable. The [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") ABC is
provided to make it easier to correctly implement these operations on
custom sequence types.

This table lists the sequence operations sorted in ascending priority. In the
table, *s* and *t* are sequences of the same type, *n*, *i*, *j* and *k* are
integers and *x* is an arbitrary object that meets any type and value
restrictions imposed by *s*.

The `in` and `not in` operations have the same priorities as the
comparison operations. The `+` (concatenation) and `*` (repetition)
operations have the same priority as the corresponding numeric operations. [[3]](https://docs.python.org/3/library/stdtypes.html#id14)

| Operation | Result | Notes |
| --- | --- | --- |
| `x in s` | `True` if an item of *s* is equal to *x*, else `False` | (1) |
| `x not in s` | `False` if an item of *s* is equal to *x*, else `True` | (1) |
| `s + t` | the concatenation of *s* and *t* | (6)(7) |
| `s * n` or `n * s` | equivalent to adding *s* to itself *n* times | (2)(7) |
| `s[i]` | *i*th item of *s*, origin 0 | (3)(8) |
| `s[i:j]` | slice of *s* from *i* to *j* | (3)(4) |
| `s[i:j:k]` | slice of *s* from *i* to *j* with step *k* | (3)(5) |
| `len(s)` | length of *s* |  |
| `min(s)` | smallest item of *s* |  |
| `max(s)` | largest item of *s* |  |

Sequences of the same type also support comparisons. In particular, tuples
and lists are compared lexicographically by comparing corresponding elements.
This means that to compare equal, every element must compare equal and the
two sequences must be of the same type and have the same length. (For full
details see [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) in the language reference.)

Forward and reversed iterators over mutable sequences access values using an
index. That index will continue to march forward (or backward) even if the
underlying sequence is mutated. The iterator terminates only when an
[`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") or a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") is encountered (or when the index
drops below zero).

Notes:

1. While the `in` and `not in` operations are used only for simple
   containment testing in the general case, some specialised sequences
   (such as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray")) also use
   them for subsequence testing:

   ```
   >>> "gg" in "eggs"
   True
   ```
2. Values of *n* less than `0` are treated as `0` (which yields an empty
   sequence of the same type as *s*). Note that items in the sequence *s*
   are not copied; they are referenced multiple times. This often haunts
   new Python programmers; consider:

   ```
   >>> lists = [[]] * 3
   >>> lists
   [[], [], []]
   >>> lists[0].append(3)
   >>> lists
   [[3], [3], [3]]
   ```

   What has happened is that `[[]]` is a one-element list containing an empty
   list, so all three elements of `[[]] * 3` are references to this single empty
   list. Modifying any of the elements of `lists` modifies this single list.
   You can create a list of different lists this way:

   ```
   >>> lists = [[] for i in range(3)]
   >>> lists[0].append(3)
   >>> lists[1].append(5)
   >>> lists[2].append(7)
   >>> lists
   [[3], [5], [7]]
   ```

   Further explanation is available in the FAQ entry
   [How do I create a multidimensional list?](https://docs.python.org/3/faq/programming.html#faq-multidimensiona