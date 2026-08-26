---
id: python-mutable-sequence-types-https-docs-python-org-3-library-stdty-5e0bc1d7
type: concept
title: Mutable Sequence Types[¶](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
  "Link to this heading")
description: The operations in the following table are defined on mutable sequence
  types.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Mutable Sequence Types[¶](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types "Link to this heading")

The operations in the following table are defined on mutable sequence types.
The [`collections.abc.MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") ABC is provided to make it
easier to correctly implement these operations on custom sequence types.

In the table *s* is an instance of a mutable sequence type, *t* is any
iterable object and *x* is an arbitrary object that meets any type
and value restrictions imposed by *s* (for example, [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") only
accepts integers that meet the value restriction `0 <= x <= 255`).

| Operation | Result | Notes |
| --- | --- | --- |
| `s[i] = x` | item *i* of *s* is replaced by *x* |  |
| `del s[i]` | removes item *i* of *s* |  |
| `s[i:j] = t` | slice of *s* from *i* to *j* is replaced by the contents of the iterable *t* |  |
| `del s[i:j]` | removes the elements of `s[i:j]` from the list (same as `s[i:j] = []`) |  |
| `s[i:j:k] = t` | the elements of `s[i:j:k]` are replaced by those of *t* | (1) |
| `del s[i:j:k]` | removes the elements of `s[i:j:k]` from the list |  |
| `s += t` | extends *s* with the contents of *t* (for the most part the same as `s[len(s):len(s)] = t`) |  |
| `s *= n` | updates *s* with its contents repeated *n* times | (2) |

Notes:

1. If *k* is not equal to `1`, *t* must have the same length as the slice it is replacing.
2. The value *n* is an integer, or an object implementing
   [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__"). Zero and negative values of *n* clear
   the sequence. Items in the sequence are not copied; they are referenced
   multiple times, as explained for `s * n` under [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common).

Mutable Sequence Methods

Mutable sequence types also support the following methods:

sequence.append(*value*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#sequence.append "Link to this definition")
:   Append *value* to the end of the sequence.
    This is equivalent to writing `seq[len(seq):len(seq)] = [value]`.

sequence.clear()[¶](https://docs.python.org/3/library/stdtypes.html#sequence.clear "Link to this definition")
:   Added in version 3.3.

    Remove all items from *sequence*.
    This is equivalent to writing `del sequence[:]`.

sequence.copy()[¶](https://docs.python.org/3/library/stdtypes.html#sequence.copy "Link to this definition")
:   Added in version 3.3.

    Create a shallow copy of *sequence*.
    This is equivalent to writing `sequence[:]`.

    Hint

    The `copy()` method is not part of the
    [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC"),
    but most concrete mutable sequence types provide it.

sequence.extend(*iterable*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#sequence.extend "Link to this definition")
:   Extend *sequence* with the contents of *iterable*.
    For the most part, this is the same as writing
    `seq[len(seq):len(seq)] = iterable`.

sequence.insert(*index*, *value*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#sequence.insert "Link to this definition")
:   Insert *value* into *sequence* at the given *index*.
    This is equivalent to writing `sequence[index:index] = [value]`.

sequence.pop(*index=-1*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#sequence.pop "Link to this definition")
:   Retrieve the item at *index* and also remove it from *sequence*.
    By default, the last item in *sequence* is removed and returned.

sequence.remove(*value*, */*)[¶](https://docs.python.org/3/library/stdtypes.h