---
id: python-fundamental-data-types-https-docs-python-org-3-library-ctype-07786b1c
type: concept
title: Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2
  "Link to this heading")
description: '*class* ctypes.\_SimpleCData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2 "Link to this heading")

*class* ctypes.\_SimpleCData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData "Link to this definition")
:   This non-public class is the base class of all fundamental ctypes data
    types. It is mentioned here because it contains the common attributes of the
    fundamental ctypes data types. `_SimpleCData` is a subclass of
    [`_CData`](https://docs.python.org/3/library/ctypes.html#ctypes._CData "ctypes._CData"), so it inherits their methods and attributes. ctypes data
    types that are not and do not contain pointers can now be pickled.

    Instances have a single attribute:

    value[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData.value "Link to this definition")
    :   This attribute contains the actual value of the instance. For integer and
        pointer types, it is an integer, for character types, it is a single
        character bytes object or string, for character pointer types it is a
        Python bytes object or string.

        When the `value` attribute is retrieved from a ctypes instance, usually
        a new object is returned each time. `ctypes` does *not* implement
        original object return, always a new object is constructed. The same is
        true for all other ctypes object instances.

    Each subclass has a class attribute:

    \_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "Link to this definition")
    :   Class attribute that contains an internal type code, as a
        single-character string.
        See [Fundamental data types](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types) for a summary.

        Types marked \* in the summary may be (or always are) aliases of a
        different `_SimpleCData` subclass, and will not necessarily
        use the listed type code.
        For example, if the platform’s long, long long
        and time\_t C types are the same, then [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long"),
        [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong") and [`c_time_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "ctypes.c_time_t") all refer to a single class,
        `c_long`, whose [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_") code is `'l'`.
        The `'L'` code will be unused.

        See also

        The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") and [struct](https://docs.python.org/3/library/struct.html#format-characters) modules,
        as well as third-party modules like [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__),
        use similar – but slightly different – type codes.

Fundamental data types, when returned as foreign function call results, or, for
example, by retrieving structure field members or array items, are transparently
converted to native Python types. In other words, if a foreign function has a
[`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype") of [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p"), you will always receive a Python bytes
object, *not* a `c_char_p` instance.

Subclasses of fundamental data types do *not* inherit this behavior. So, if a
foreign functions `restype` is a subclass of [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p"), you will
receive an instance of this subclass from the function call. Of course, you can
get the value of the pointer by accessing the `value` attribute.

These are the fundamental ctypes data types: