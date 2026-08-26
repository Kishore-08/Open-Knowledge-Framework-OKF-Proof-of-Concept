---
id: python-immutable-sequence-types-https-docs-python-org-3-library-std-5e0bc1d7
type: concept
title: Immutable Sequence Types[¶](https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types
  "Link to this heading")
description: The only operation that immutable sequence types generally implement
  that is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Immutable Sequence Types[¶](https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types "Link to this heading")

The only operation that immutable sequence types generally implement that is
not also implemented by mutable sequence types is support for the [`hash()`](https://docs.python.org/3/library/functions.html#hash "hash")
built-in.

This support allows immutable sequences, such as [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") instances, to
be used as [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") keys and stored in [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")
instances.

Attempting to hash an immutable sequence that contains unhashable values will
result in [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").