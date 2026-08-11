---
id: python-standard-formats-https-docs-python-org-3-library-struct-html-16930738
type: concept
title: Standard Formats[¶](https://docs.python.org/3/library/struct.html#standard-formats
  "Link to this heading")
description: When exchanging data beyond your process such as networking or storage,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Standard Formats[¶](https://docs.python.org/3/library/struct.html#standard-formats "Link to this heading")

When exchanging data beyond your process such as networking or storage,
be precise. Specify the exact byte order, size, and alignment. Do
not assume they match the native order of a particular machine.
For example, network byte order is big-endian, while many popular CPUs
are little-endian. By defining this explicitly, the user need not
care about the specifics of the platform their code is running on.
The first character should typically be `<` or `>`
(or `!`). Padding is the responsibility of the programmer. The
zero-repeat format character won’t work. Instead, the user must
explicitly add `'x'` pad bytes where needed. Revisiting the
examples from the previous section, we have:

```
>>> calcsize('<qh6xq')
24
>>> pack('<qh6xq', 1, 2, 3) == pack('@lhl', 1, 2, 3)
True
>>> calcsize('@llh')
18
>>> pack('@llh', 1, 2, 3) == pack('<qqh', 1, 2, 3)
True
>>> calcsize('<qqh6x')
24
>>> calcsize('@llh0l')
24
>>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
True
```

The above results (executed on a 64-bit machine) aren’t guaranteed to
match when executed on different machines. For example, the examples
below were executed on a 32-bit machine:

```
>>> calcsize('<qqh6x')
24
>>> calcsize('@llh0l')
12
>>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
False
```