---
id: python-i-o-base-classes-https-docs-python-org-3-library-io-html-i-o-dbdafd7f
type: concept
title: I/O Base Classes[¶](https://docs.python.org/3/library/io.html#i-o-base-classes
  "Link to this heading")
description: '*class* io.IOBase[¶](https://docs.python.org/3/library/io.html#io.IOBase
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### I/O Base Classes[¶](https://docs.python.org/3/library/io.html#i-o-base-classes "Link to this heading")

*class* io.IOBase[¶](https://docs.python.org/3/library/io.html#io.IOBase "Link to this definition")
:   The abstract base class for all I/O classes.

    This class provides empty abstract implementations for many methods
    that derived classes can override selectively; the default
    implementations represent a file that cannot be read, written or
    seeked.

    Even though `IOBase` does not declare `read()`
    or `write()` because their signatures will vary, implementations and
    clients should consider those methods part of the interface. Also,
    implementations may raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation"))
    when operations they do not support are called.

    The basic type used for binary data read from or written to a file is
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Other [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) are
    accepted as method arguments too. Text I/O classes work with [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") data.

    Note that calling any method (even inquiries) on a closed stream is
    undefined. Implementations may raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in this case.

    `IOBase` (and its subclasses) supports the iterator protocol, meaning
    that an `IOBase` object can be iterated over yielding the lines in a
    stream. Lines are defined slightly differently depending on whether the
    stream is a binary stream (yielding bytes), or a text stream (yielding
    character strings). See [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") below.

    `IOBase` is also a context manager and therefore supports the
    [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, *file* is closed after the
    `with` statement’s suite is finished—even if an exception occurs:

    ```
    with open('spam.txt', 'w') as file:
        file.write('Spam and eggs!')
    ```

    `IOBase` provides these data attributes and methods:

    close()[¶](https://docs.python.org/3/library/io.html#io.IOBase.close "Link to this definition")
    :   Flush and close this stream. This method has no effect if the file is
        already closed. Once the file is closed, any operation on the file
        (e.g. reading or writing) will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

        As a convenience, it is allowed to call this method more than once;
        only the first call, however, will have an effect.

    closed[¶](https://docs.python.org/3/library/io.html#io.IOBase.closed "Link to this definition")
    :   `True` if the stream is closed.

    fileno()[¶](https://docs.python.org/3/library/io.html#io.IOBase.fileno "Link to this definition")
    :   Return the underlying file descriptor (an integer) of the stream if it
        exists. An [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if the IO object does not use a file
        descriptor.

    flush()[¶](https://docs.python.org/3/library/io.html#io.IOBase.flush "Link to this definition")
    :   Flush the write buffers of the stream if applicable. This does nothing
        for read-only and non-blocking streams.

    isatty()[¶](https://docs.python.org/3/library/io.html#io.IOBase.isatty "Link to this definition")
    :   Return `True` if the stream is interactive (i.e., connected to
        a terminal/tty device).

    readable()[¶](https://docs.python.org/3/library/io.html#io.IOBase.readable "Link to this definition")
    :   Return `Tru