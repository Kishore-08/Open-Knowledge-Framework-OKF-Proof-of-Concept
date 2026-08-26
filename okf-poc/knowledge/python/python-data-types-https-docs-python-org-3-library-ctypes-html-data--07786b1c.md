---
id: python-data-types-https-docs-python-org-3-library-ctypes-html-data--07786b1c
type: concept
title: Data types[¶](https://docs.python.org/3/library/ctypes.html#data-types "Link
  to this heading")
description: '*class* ctypes.\_CData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Data types[¶](https://docs.python.org/3/library/ctypes.html#data-types "Link to this heading")

*class* ctypes.\_CData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData "Link to this definition")
:   This non-public class is the common base class of all ctypes data types.
    Among other things, all ctypes type instances contain a memory block that
    hold C compatible data; the address of the memory block is returned by the
    [`addressof()`](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "ctypes.addressof") helper function. Another instance variable is exposed as
    [`_objects`](https://docs.python.org/3/library/ctypes.html#ctypes._CData._objects "ctypes._CData._objects"); this contains other Python objects that need to be kept
    alive in case the memory block contains pointers.

    Common methods of ctypes data types, these are all class methods (to be
    exact, they are methods of the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)):

    from\_buffer(*source*[, *offset*])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer "Link to this definition")
    :   This method returns a ctypes instance that shares the buffer of the
        *source* object. The *source* object must support the writeable buffer
        interface. The optional *offset* parameter specifies an offset into the
        source buffer in bytes; the default is zero. If the source buffer is not
        large enough a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

        Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

    from\_buffer\_copy(*source*[, *offset*])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer_copy "Link to this definition")
    :   This method creates a ctypes instance, copying the buffer from the
        *source* object buffer which must be readable. The optional *offset*
        parameter specifies an offset into the source buffer in bytes; the default
        is zero. If the source buffer is not large enough a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is
        raised.

        Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

    from\_address(*address*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address "Link to this definition")
    :   This method returns a ctypes type instance using the memory specified by
        *address* which must be an integer.

        This method, and others that indirectly call this method, raises an
        [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ctypes.cdata` with argument
        `address`.

    from\_param(*obj*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "Link to this definition")
    :   This method adapts *obj* to a ctypes type. It is called with the actual
        object used in a foreign function call when the type is present in the
        foreign function’s [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") tuple;
        it must return an object that can be used as a function call parameter.

        All ctypes data types have a default implementation of this classmethod
        that normally returns *obj* if that is an instance of the type. Some
        types accept other objects as well.

    in\_dll(*library*, *name*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "Link to this definition")
    :   This method returns a ctypes type instance exported by a shared
        library. *name* is the name of the symbol that exports the data, *library*
        is the loaded shared library.

    Common class variables of ctypes data