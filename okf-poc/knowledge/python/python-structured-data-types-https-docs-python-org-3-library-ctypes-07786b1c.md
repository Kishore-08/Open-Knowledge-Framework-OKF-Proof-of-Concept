---
id: python-structured-data-types-https-docs-python-org-3-library-ctypes-07786b1c
type: concept
title: Structured data types[¶](https://docs.python.org/3/library/ctypes.html#structured-data-types
  "Link to this heading")
description: '*class* ctypes.Union(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Union
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Structured data types[¶](https://docs.python.org/3/library/ctypes.html#structured-data-types "Link to this heading")

*class* ctypes.Union(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Union "Link to this definition")
:   Abstract base class for unions in native byte order.

    Unions share common attributes and behavior with structures;
    see [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure") documentation for details.

*class* ctypes.BigEndianUnion(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "Link to this definition")
:   Abstract base class for unions in *big endian* byte order.

    Added in version 3.11.

*class* ctypes.LittleEndianUnion(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "Link to this definition")
:   Abstract base class for unions in *little endian* byte order.

    Added in version 3.11.

*class* ctypes.BigEndianStructure(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "Link to this definition")
:   Abstract base class for structures in *big endian* byte order.

*class* ctypes.LittleEndianStructure(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "Link to this definition")
:   Abstract base class for structures in *little endian* byte order.

Structures and unions with non-native byte order cannot contain pointer type
fields, or any other data types containing pointer type fields.

*class* ctypes.Structure(*\*args*, *\*\*kw*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "Link to this definition")
:   Abstract base class for structures in *native* byte order.

    Concrete structure and union types must be created by subclassing one of these
    types, and at least define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") class variable. `ctypes` will
    create [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s which allow reading and writing the fields by direct
    attribute accesses. These are the

    \_fields\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "Link to this definition")
    :   A sequence defining the structure fields. The items must be 2-tuples or
        3-tuples. The first item is the name of the field, the second item
        specifies the type of the field; it can be any ctypes data type.

        For integer type fields like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int"), a third optional item can be
        given. It must be a small positive integer defining the bit width of the
        field.

        Field names must be unique within one structure or union. This is not
        checked, only one field can be accessed when names are repeated.

        It is possible to define the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") class variable *after* the
        class statement that defines the Structure subclass, this allows creating
        data types that directly or indirectly reference themselves:

        ```
        class List(Structure):
            pass
        List._fields_ = [("pnext", POINTER(List)),
                         ...
                        ]
        ```

        The `_fields_` class variable can only be set once.
        Later assignments will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").

        Additionally, the `_fields_` class variable must be defined before
        the structure or union type is first used: an instance or subclass is
        created, [`sizeof()`](https://docs.python.org/3/library/ctypes.html#ctypes.sizeof "ctypes.sizeof") is called on it, and so on.
        Later assign