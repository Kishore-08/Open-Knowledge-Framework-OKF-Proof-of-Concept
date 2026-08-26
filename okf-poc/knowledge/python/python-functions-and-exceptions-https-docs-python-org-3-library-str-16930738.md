---
id: python-functions-and-exceptions-https-docs-python-org-3-library-str-16930738
type: concept
title: Functions and Exceptions[¶](https://docs.python.org/3/library/struct.html#functions-and-exceptions
  "Link to this heading")
description: 'The module defines the following exception and functions:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Functions and Exceptions[¶](https://docs.python.org/3/library/struct.html#functions-and-exceptions "Link to this heading")

The module defines the following exception and functions:

*exception* struct.error[¶](https://docs.python.org/3/library/struct.html#struct.error "Link to this definition")
:   Exception raised on various occasions; argument is a string describing what
    is wrong.

struct.pack(*format*, *v1*, *v2*, *...*)[¶](https://docs.python.org/3/library/struct.html#struct.pack "Link to this definition")
:   Return a bytes object containing the values *v1*, *v2*, … packed according
    to the format string *format*. The arguments must match the values required by
    the format exactly.

struct.pack\_into(*format*, *buffer*, *offset*, *v1*, *v2*, *...*)[¶](https://docs.python.org/3/library/struct.html#struct.pack_into "Link to this definition")
:   Pack the values *v1*, *v2*, … according to the format string *format* and
    write the packed bytes into the writable buffer *buffer* starting at
    position *offset*. Note that *offset* is a required argument.
    A negative *offset* counts from the end of *buffer*.

struct.unpack(*format*, *buffer*)[¶](https://docs.python.org/3/library/struct.html#struct.unpack "Link to this definition")
:   Unpack from the buffer *buffer* (presumably packed by `pack(format, ...)`)
    according to the format string *format*. The result is a tuple even if it
    contains exactly one item. The buffer’s size in bytes must match the
    size required by the format, as reflected by [`calcsize()`](https://docs.python.org/3/library/struct.html#struct.calcsize "struct.calcsize").

struct.unpack\_from(*format*, */*, *buffer*, *offset=0*)[¶](https://docs.python.org/3/library/struct.html#struct.unpack_from "Link to this definition")
:   Unpack from *buffer* starting at position *offset*, according to the format
    string *format*. The result is a tuple even if it contains exactly one
    item. The buffer’s size in bytes, starting at position *offset*, must be at
    least the size required by the format, as reflected by [`calcsize()`](https://docs.python.org/3/library/struct.html#struct.calcsize "struct.calcsize").
    A negative *offset* counts from the end of *buffer*.

struct.iter\_unpack(*format*, *buffer*)[¶](https://docs.python.org/3/library/struct.html#struct.iter_unpack "Link to this definition")
:   Iteratively unpack from the buffer *buffer* according to the format
    string *format*. This function returns an iterator which will read
    equally sized chunks from the buffer until all its contents have been
    consumed. The buffer’s size in bytes must be a multiple of the size
    required by the format, as reflected by [`calcsize()`](https://docs.python.org/3/library/struct.html#struct.calcsize "struct.calcsize").

    Each iteration yields a tuple as specified by the format string.

    Added in version 3.4.

struct.calcsize(*format*)[¶](https://docs.python.org/3/library/struct.html#struct.calcsize "Link to this definition")
:   Return the size of the struct (and hence of the bytes object produced by
    `pack(format, ...)`) corresponding to the format string *format*.