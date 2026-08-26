---
id: python-structure-union-layout-alignment-and-byte-order-https-docs-p-07786b1c
type: concept
title: Structure/union layout, alignment and byte order[¶](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order
  "Link to this heading")
description: By default, Structure and Union fields are laid out in the same way the
  C
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Structure/union layout, alignment and byte order[¶](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order "Link to this heading")

By default, Structure and Union fields are laid out in the same way the C
compiler does it. It is possible to override this behavior entirely by specifying a
[`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_") class attribute in the subclass definition; see
the attribute documentation for details.

It is possible to specify the maximum alignment for the fields and/or for the
structure itself by setting the class attributes [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")
and/or [`_align_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "ctypes.Structure._align_"), respectively.
See the attribute documentation for details.

`ctypes` uses the native byte order for Structures and Unions. To build
structures with non-native byte order, you can use one of the
[`BigEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "ctypes.BigEndianStructure"), [`LittleEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "ctypes.LittleEndianStructure"),
[`BigEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "ctypes.BigEndianUnion"), and [`LittleEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "ctypes.LittleEndianUnion") base classes. These
classes cannot contain pointer fields.