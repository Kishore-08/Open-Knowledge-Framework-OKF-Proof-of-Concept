---
id: python-text-i-o-https-docs-python-org-3-library-io-html-id1-link-to-dbdafd7f
type: concept
title: Text I/O[¶](https://docs.python.org/3/library/io.html#id1 "Link to this heading")
description: '*class* io.TextIOBase[¶](https://docs.python.org/3/library/io.html#io.TextIOBase
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Text I/O[¶](https://docs.python.org/3/library/io.html#id1 "Link to this heading")

*class* io.TextIOBase[¶](https://docs.python.org/3/library/io.html#io.TextIOBase "Link to this definition")
:   Base class for text streams. This class provides a character and line based
    interface to stream I/O. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").

    `TextIOBase` provides or overrides these data attributes and
    methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

    encoding[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.encoding "Link to this definition")
    :   The name of the encoding used to decode the stream’s bytes into
        strings, and to encode strings into bytes.

    errors[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.errors "Link to this definition")
    :   The error setting of the decoder or encoder.

    newlines[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.newlines "Link to this definition")
    :   A string, a tuple of strings, or `None`, indicating the newlines
        translated so far. Depending on the implementation and the initial
        constructor flags, this may not be available.

    buffer[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "Link to this definition")
    :   The underlying binary buffer (a [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
        or [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") instance) that `TextIOBase` deals with.
        This is not part of the `TextIOBase` API and may not exist
        in some implementations.

    detach()[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.detach "Link to this definition")
    :   Separate the underlying binary buffer from the `TextIOBase` and
        return it.

        After the underlying buffer has been detached, the `TextIOBase` is
        in an unusable state.

        Some `TextIOBase` implementations, like [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), may not
        have the concept of an underlying buffer and calling this method will
        raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").

        Added in version 3.1.

    read(*size=-1*, */*)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.read "Link to this definition")
    :   Read and return at most *size* characters from the stream as a single
        [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If *size* is negative or `None`, reads until EOF.

    readline(*size=-1*, */*)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "Link to this definition")
    :   Read until newline or EOF and return a single [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If the stream is
        already at EOF, an empty string is returned.

        If *size* is specified, at most *size* characters will be read.

    seek(*offset*, *whence=SEEK\_SET*, */*)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "Link to this definition")
    :   Change the stream position to the given *offset*. Behaviour depends on
        the *whence* parameter. The default value for *whence* is
        `SEEK_SET`.

        - `SEEK_SET` or `0`: seek from the start of the stream
          (the default); *offset* must either be a number returned by
          [`TextIOBase.tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell"), or zero. Any other *offset* value
          produces undefined behaviour.
        - `SEEK_CUR` or `1`: “seek” to the current position;
          *offset* must be zero, which is a no-operation (all other values
          are unsupported).
        - `SEEK_END` or `2`: seek to the end of the s