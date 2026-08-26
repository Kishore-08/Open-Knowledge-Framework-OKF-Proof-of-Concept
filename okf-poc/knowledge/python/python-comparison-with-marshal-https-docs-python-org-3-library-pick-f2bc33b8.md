---
id: python-comparison-with-marshal-https-docs-python-org-3-library-pick-f2bc33b8
type: concept
title: Comparison with `marshal`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-marshal
  "Link to this heading")
description: 'Python has a more primitive serialization module called [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal
  "marshal: Convert Python objects to streams of bytes and back (with di'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Comparison with `marshal`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-marshal "Link to this heading")

Python has a more primitive serialization module called [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints)."), but in
general `pickle` should always be the preferred way to serialize Python
objects. `marshal` exists primarily to support Python’s `.pyc`
files.

The `pickle` module differs from [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") in several significant ways:

- [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") cannot be used to serialize user-defined classes and their
  instances. `pickle` can save and restore class instances transparently,
  however the class definition must be importable and live in the same module as
  when the object was pickled.
- The [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") serialization format is not guaranteed to be portable
  across Python versions. Because its primary job in life is to support
  `.pyc` files, the Python implementers reserve the right to change the
  serialization format in non-backwards compatible ways should the need arise.
  The `pickle` serialization format is guaranteed to be backwards compatible
  across Python releases provided a compatible pickle protocol is chosen and
  pickling and unpickling code deals with Python 2 to Python 3 type differences
  if your data is crossing that unique breaking change language boundary.