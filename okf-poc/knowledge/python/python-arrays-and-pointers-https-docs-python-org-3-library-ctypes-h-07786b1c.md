---
id: python-arrays-and-pointers-https-docs-python-org-3-library-ctypes-h-07786b1c
type: concept
title: Arrays and pointers[¶](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers
  "Link to this heading")
description: '*class* ctypes.Array(*\*args*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Arrays and pointers[¶](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers "Link to this heading")

*class* ctypes.Array(*\*args*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array "Link to this definition")
:   Abstract base class for arrays.

    The recommended way to create concrete array types is by multiplying any
    `ctypes` data type with a non-negative integer. Alternatively, you can subclass
    this type and define [`_length_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "ctypes.Array._length_") and [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "ctypes.Array._type_") class variables.
    Array elements can be read and written using standard
    subscript and slice accesses; for slice reads, the resulting object is
    *not* itself an `Array`.

    Arrays are [generic](https://docs.python.org/3/library/typing.html#generics) over the type of their elements.

    \_length\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "Link to this definition")
    :   A positive integer specifying the number of elements in the array.
        Out-of-range subscripts result in an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError"). Will be
        returned by [`len()`](https://docs.python.org/3/library/functions.html#len "len").

    \_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "Link to this definition")
    :   Specifies the type of each element in the array.

    Array subclass constructors accept positional arguments, used to
    initialize the elements in order.

ctypes.ARRAY(*type*, *length*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ARRAY "Link to this definition")
:   Create an array.
    Equivalent to `type * length`, where *type* is a
    `ctypes` data type and *length* an integer.

    [Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated) since version 3.14: In favor of multiplication.

*class* ctypes.\_Pointer[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer "Link to this definition")
:   Private, abstract base class for pointers.

    Concrete pointer types are created by calling [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER") with the
    type that will be pointed to; this is done automatically by
    [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer").

    If a pointer points to an array, its elements can be read and
    written using standard subscript and slice accesses. Pointer objects
    have no size, so [`len()`](https://docs.python.org/3/library/functions.html#len "len") will raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). Negative
    subscripts will read from the memory *before* the pointer (as in C), and
    out-of-range subscripts will probably crash with an access violation (if
    you’re lucky).

    \_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer._type_ "Link to this definition")
    :   Specifies the type pointed to.

    contents[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer.contents "Link to this definition")
    :   Returns the object to which to pointer points. Assigning to this
        attribute changes the pointer to point to the assigned object.