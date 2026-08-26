---
id: python-bit-fields-in-structures-and-unions-https-docs-python-org-3--07786b1c
type: concept
title: Bit fields in structures and unions[¶](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions
  "Link to this heading")
description: It is possible to create structures and unions containing bit fields.
  Bit fields
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Bit fields in structures and unions[¶](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions "Link to this heading")

It is possible to create structures and unions containing bit fields. Bit fields
are only possible for integer fields, the bit width is specified as the third
item in the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") tuples:

```
>>> class Int(Structure):
...     _fields_ = [("first_16", c_int, 16),
...                 ("second_16", c_int, 16)]
...
>>> print(Int.first_16)
<ctypes.CField 'first_16' type=c_int, ofs=0, bit_size=16, bit_offset=0>
>>> print(Int.second_16)
<ctypes.CField 'second_16' type=c_int, ofs=0, bit_size=16, bit_offset=16>
```

It is important to note that bit field allocation and layout in memory are not
defined as a C standard; their implementation is compiler-specific.
By default, Python will attempt to match the behavior of a “native” compiler
for the current platform.
See the [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_") attribute for details on the default
behavior and how to change it.