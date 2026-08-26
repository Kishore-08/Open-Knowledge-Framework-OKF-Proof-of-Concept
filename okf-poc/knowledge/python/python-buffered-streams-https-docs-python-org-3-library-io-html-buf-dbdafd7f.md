---
id: python-buffered-streams-https-docs-python-org-3-library-io-html-buf-dbdafd7f
type: concept
title: Buffered Streams[¶](https://docs.python.org/3/library/io.html#buffered-streams
  "Link to this heading")
description: Buffered I/O streams provide a higher-level interface to an I/O device
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Buffered Streams[¶](https://docs.python.org/3/library/io.html#buffered-streams "Link to this heading")

Buffered I/O streams provide a higher-level interface to an I/O device
than raw I/O does.

*class* io.BytesIO(*initial\_bytes=b''*)[¶](https://docs.python.org/3/library/io.html#io.BytesIO "Link to this definition")
:   A binary stream using an in-memory bytes buffer. It inherits from
    [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"). The buffer is discarded when the
    [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method is called.

    The optional argument *initial\_bytes* is a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) that
    contains initial data.

    `BytesIO` provides or overrides these methods in addition to those
    from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

    getbuffer()[¶](https://docs.python.org/3/library/io.html#io.BytesIO.getbuffer "Link to this definition")
    :   Return a readable and writable view over the contents of the buffer
        without copying them. Also, mutating the view will transparently
        update the contents of the buffer:

        ```
        >>> b = io.BytesIO(b"abcdef")
        >>> view = b.getbuffer()
        >>> view[2:4] = b"56"
        >>> b.getvalue()
        b'ab56ef'
        ```

        Note

        As long as the view exists, the `BytesIO` object cannot be
        resized or closed.

        Added in version 3.2.

    getvalue()[¶](https://docs.python.org/3/library/io.html#io.BytesIO.getvalue "Link to this definition")
    :   Return [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") containing the entire contents of the buffer.

    read1(*size=-1*, */*)[¶](https://docs.python.org/3/library/io.html#io.BytesIO.read1 "Link to this definition")
    :   In `BytesIO`, this is the same as [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read").

        Changed in version 3.7: The *size* argument is now optional.

    readinto1(*b*, */*)[¶](https://docs.python.org/3/library/io.html#io.BytesIO.readinto1 "Link to this definition")
    :   In `BytesIO`, this is the same as [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").

        Added in version 3.5.

*class* io.BufferedReader(*raw*, *buffer\_size=DEFAULT\_BUFFER\_SIZE*)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader "Link to this definition")
:   A buffered binary stream providing higher-level access to a readable, non
    seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from
    [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

    When reading data from this object, a larger amount of data may be
    requested from the underlying raw stream, and kept in an internal buffer.
    The buffered data can then be returned directly on subsequent reads.

    The constructor creates a `BufferedReader` for the given readable
    *raw* stream and *buffer\_size*. If *buffer\_size* is omitted,
    [`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE") is used.

    `BufferedReader` provides or overrides these methods in addition to
    those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

    peek(*size=0*, */*)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader.peek "Link to this definition")
    :   Return bytes from the stream without advancing the position. The number of