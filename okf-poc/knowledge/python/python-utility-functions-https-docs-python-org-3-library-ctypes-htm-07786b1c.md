---
id: python-utility-functions-https-docs-python-org-3-library-ctypes-htm-07786b1c
type: concept
title: Utility functions[¶](https://docs.python.org/3/library/ctypes.html#utility-functions
  "Link to this heading")
description: ctypes.addressof(*obj*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.addressof
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Utility functions[¶](https://docs.python.org/3/library/ctypes.html#utility-functions "Link to this heading")

ctypes.addressof(*obj*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "Link to this definition")
:   Returns the address of the memory buffer as integer. *obj* must be an
    instance of a ctypes type.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.addressof` with argument `obj`.

ctypes.alignment(*obj\_or\_type*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.alignment "Link to this definition")
:   Returns the alignment requirements of a ctypes type. *obj\_or\_type* must be a
    ctypes type or instance.

ctypes.byref(*obj*[, *offset*])[¶](https://docs.python.org/3/library/ctypes.html#ctypes.byref "Link to this definition")
:   Returns a light-weight pointer to *obj*, which must be an instance of a
    ctypes type. *offset* defaults to zero, and must be an integer that will be
    added to the internal pointer value.

    `byref(obj, offset)` corresponds to this C code:

    ```
    (((char *)&obj) + offset)
    ```

    The returned object can only be used as a foreign function call parameter.
    It behaves similar to `pointer(obj)`, but the construction is a lot faster.

ctypes.CopyComPointer(*src*, *dst*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CopyComPointer "Link to this definition")
:   Copies a COM pointer from *src* to *dst* and returns the Windows specific
    `HRESULT` value.

    If *src* is not `NULL`, its `AddRef` method is called, incrementing the
    reference count.

    In contrast, the reference count of *dst* will not be decremented before
    assigning the new value. Unless *dst* is `NULL`, the caller is responsible
    for decrementing the reference count by calling its `Release` method when
    necessary.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows

    Added in version 3.14.

ctypes.cast(*obj*, *type*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.cast "Link to this definition")
:   This function is similar to the cast operator in C. It returns a new instance
    of *type* which points to the same memory block as *obj*. *type* must be a
    pointer type, and *obj* must be an object that can be interpreted as a
    pointer.

ctypes.create\_string\_buffer(*init*, *size=None*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "Link to this definition")

ctypes.create\_string\_buffer(*size*)
:   This function creates a mutable character buffer. The returned object is a
    ctypes array of [`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char").

    If *size* is given (and not `None`), it must be an [`int`](https://docs.python.org/3/library/functions.html#int "int").
    It specifies the size of the returned array.

    If the *init* argument is given, it must be [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). It is used
    to initialize the array items. Bytes not initialized this way are
    set to zero (NUL).

    If *size* is not given (or if it is `None`), the buffer is made one element
    larger than *init*, effectively adding a NUL terminator.

    If both arguments are given, *size* must not be less than `len(init)`.

    Warning

    If *size* is equal to `len(init)`, a NUL terminator is
    not added. Do not treat such a buffer as a C string.

    For example:

    ```
    >>> bytes(create_string_buffer(2))
    b'\x00\x00'
    >>> bytes(create_string_buffer(b'ab'))
    b'ab\x00'
    >>> bytes(create_string_buffer(b'ab', 2))
    b'ab'
    >>> bytes(create_string_buffer(b'ab', 4))
    b'ab\x00\x00'
    >>> bytes(create_string_buffer(b'abcdef', 2))
    Traceback (most recent call last):
       ...
    ValueError: byte string too long
    ```

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.create_string_buffer` with