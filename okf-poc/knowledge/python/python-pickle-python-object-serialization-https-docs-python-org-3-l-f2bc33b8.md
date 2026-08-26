---
id: python-pickle-python-object-serialization-https-docs-python-org-3-l-f2bc33b8
type: concept
title: '`pickle` — Python object serialization[¶](https://docs.python.org/3/library/pick'
description: '**Source code:** [Lib/pickle.py](https://github.com/python/cpython/tree/3.14/Lib/pickle.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `pickle` — Python object serialization[¶](https://docs.python.org/3/library/pickle.html#module-pickle "Link to this heading")

**Source code:** [Lib/pickle.py](https://github.com/python/cpython/tree/3.14/Lib/pickle.py)

---

The `pickle` module implements binary protocols for serializing and
de-serializing a Python object structure. *“Pickling”* is the process
whereby a Python object hierarchy is converted into a byte stream, and
*“unpickling”* is the inverse operation, whereby a byte stream
(from a [binary file](https://docs.python.org/3/glossary.html#term-binary-file) or [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)) is converted
back into an object hierarchy. Pickling (and unpickling) is alternatively
known as “serialization”, “marshalling,” [[1]](https://docs.python.org/3/library/pickle.html#id7) or “flattening”; however, to
avoid confusion, the terms used here are “pickling” and “unpickling”.

Warning

The `pickle` module **is not secure**. Only unpickle data you trust.

It is possible to construct malicious pickle data which will **execute
arbitrary code during unpickling**. Never unpickle data that could have come
from an untrusted source, or that could have been tampered with.

Consider signing data with [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication (HMAC) implementation") if you need to ensure that it has not
been tampered with.

Safer serialization formats such as [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.") may be more appropriate if
you are processing untrusted data. See [Comparison with json](https://docs.python.org/3/library/pickle.html#comparison-with-json).

## Relationship to other Python modules[¶](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules "Link to this heading")