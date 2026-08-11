---
id: python-memory-views-https-docs-python-org-3-library-stdtypes-html-m-5e0bc1d7
type: concept
title: Memory Views[¶](https://docs.python.org/3/library/stdtypes.html#memory-views
  "Link to this heading")
description: '[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview
  "memoryview") objects allow Python code to access the internal data'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Memory Views[¶](https://docs.python.org/3/library/stdtypes.html#memory-views "Link to this heading")

[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") objects allow Python code to access the internal data
of an object that supports the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) without
copying.

*class* memoryview(*object*)[¶](https://docs.python.org/3/library/stdtypes.html#memoryview "Link to this definition")
:   > Create a `memoryview` that references *object*. *object* must
    > support the buffer protocol. Built-in objects that support the buffer
    > protocol include [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
    >
    > A `memoryview` has the notion of an *element*, which is the
    > atomic memory unit handled by the originating *object*. For many simple
    > types such as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"), an element is a single
    > byte, but other types such as [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array") may have bigger elements.
    >
    > `memoryview`s are [generic](https://docs.python.org/3/library/typing.html#generics) over the type of their
    > underlying data.
    >
    > `len(view)` is equal to the length of [`tolist`](https://docs.python.org/3/library/stdtypes.html#memoryview.tolist "memoryview.tolist"), which
    > is the nested list representation of the view. If `view.ndim = 1`,
    > this is equal to the number of elements in the view.
    >
    > Changed in version 3.12: If `view.ndim == 0`, `len(view)` now raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") instead of returning 1.
    >
    > The [`itemsize`](https://docs.python.org/3/library/stdtypes.html#memoryview.itemsize "memoryview.itemsize") attribute will give you the number of
    > bytes in a single element.
    >
    > A `memoryview` supports slicing and indexing to expose its data.
    > One-dimensional slicing will result in a subview:
    >
    > ```
    > >>> v = memoryview(b'abcefg')
    > >>> v[1]
    > 98
    > >>> v[-1]
    > 103
    > >>> v[1:4]
    > <memory at 0x7f3ddc9f4350>
    > >>> bytes(v[1:4])
    > b'bce'
    > ```
    >
    > If [`format`](https://docs.python.org/3/library/stdtypes.html#memoryview.format "memoryview.format") is one of the native format specifiers
    > from the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.") module, indexing with an integer or a tuple of
    > integers is also supported and returns a single *element* with
    > the correct type. One-dimensional memoryviews can be indexed
    > with an integer or a one-integer tuple. Multi-dimensional memoryviews
    > can be indexed with tuples of exactly *ndim* integers where *ndim* is
    > the number of dimensions. Zero-dimensional memoryviews can be indexed
    > with the empty tuple.
    >
    > Here is an example with a non-byte format:
    >
    > ```
    > >>> import array
    > >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
    > >>> m = memoryview(a)
    > >>> m[0]
    > -11111111
    > >>> m[-1]
    > 44444444
    > >>> m[::2].tolist()
    > [-11111111, -33333333]
    > ```
    >
    > If the underlying object is writable, the memoryview supports
    > one-dimensional slice assignment. Resizing is not allowed:
    >
    > ```
    > >>> data = bytearray(b'abcefg')
    > >>> v = memoryview(data)
    > >>> v.readonly
    > False
    > >>> v[0] = ord(b'z')
    > >>> data
    > bytearray(b'zbcefg')
    > >>> v[1:4] = b'123'
    > >>> data
    > bytearray(b'z123fg')
    > >>> v[2:3] = b'spam'
    > Traceback (most recent call last):
    >   File "<