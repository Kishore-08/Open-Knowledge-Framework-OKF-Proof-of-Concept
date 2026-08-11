---
id: python-pprint-data-pretty-printer-https-docs-python-org-3-library-p-cfd107b1
type: concept
title: '`pprint` — Data pretty printer[¶](https://docs.python.org/3/library/pprint.html#'
description: '**Source code:** [Lib/pprint.py](https://github.com/python/cpython/tree/3.14/Lib/pprint.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pprint.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `pprint` — Data pretty printer[¶](https://docs.python.org/3/library/pprint.html#module-pprint "Link to this heading")

**Source code:** [Lib/pprint.py](https://github.com/python/cpython/tree/3.14/Lib/pprint.py)

---

The `pprint` module provides a capability to “pretty-print” arbitrary
Python data structures in a form which can be used as input to the interpreter.
If the formatted structures include objects which are not fundamental Python
types, the representation may not be loadable. This may be the case if objects
such as files, sockets or classes are included, as well as many other
objects which are not representable as Python literals.

The formatted representation keeps objects on a single line if it can, and
breaks them onto multiple lines if they don’t fit within the allowed width,
adjustable by the *width* parameter defaulting to 80 characters.

Changed in version 3.9: Added support for pretty-printing [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace").

Changed in version 3.10: Added support for pretty-printing [`dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass").