---
id: python-os-exceptions-https-docs-python-org-3-library-exceptions-htm-874b1988
type: concept
title: OS exceptions[¶](https://docs.python.org/3/library/exceptions.html#os-exceptions
  "Link to this heading")
description: The following exceptions are subclasses of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError
  "OSError"), they get raised
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/exceptions.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### OS exceptions[¶](https://docs.python.org/3/library/exceptions.html#os-exceptions "Link to this heading")

The following exceptions are subclasses of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), they get raised
depending on the system error code.

*exception* BlockingIOError[¶](https://docs.python.org/3/library/exceptions.html#BlockingIOError "Link to this definition")
:   Raised when an operation would block on an object (e.g. socket) set
    for non-blocking operation.
    Corresponds to `errno` [`EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN"), [`EALREADY`](https://docs.python.org/3/library/errno.html#errno.EALREADY "errno.EALREADY"),
    [`EWOULDBLOCK`](https://docs.python.org/3/library/errno.html#errno.EWOULDBLOCK "errno.EWOULDBLOCK") and [`EINPROGRESS`](https://docs.python.org/3/library/errno.html#errno.EINPROGRESS "errno.EINPROGRESS").

    In addition to those of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), `BlockingIOError` can have
    one more attribute:

    characters\_written[¶](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "Link to this definition")
    :   An integer containing the number of **bytes** written to the stream
        before it blocked. This attribute is available when using the
        buffered I/O classes from the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") module.

*exception* ChildProcessError[¶](https://docs.python.org/3/library/exceptions.html#ChildProcessError "Link to this definition")
:   Raised when an operation on a child process failed.
    Corresponds to `errno` [`ECHILD`](https://docs.python.org/3/library/errno.html#errno.ECHILD "errno.ECHILD").

*exception* ConnectionError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionError "Link to this definition")
:   A base class for connection-related issues.

    Subclasses are [`BrokenPipeError`](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "BrokenPipeError"), [`ConnectionAbortedError`](https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError "ConnectionAbortedError"),
    [`ConnectionRefusedError`](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError "ConnectionRefusedError") and [`ConnectionResetError`](https://docs.python.org/3/library/exceptions.html#ConnectionResetError "ConnectionResetError").

*exception* BrokenPipeError[¶](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "Link to this definition")
:   A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when trying to write on a
    pipe while the other end has been closed, or trying to write on a socket
    which has been shutdown for writing.
    Corresponds to `errno` [`EPIPE`](https://docs.python.org/3/library/errno.html#errno.EPIPE "errno.EPIPE") and [`ESHUTDOWN`](https://docs.python.org/3/library/errno.html#errno.ESHUTDOWN "errno.ESHUTDOWN").

*exception* ConnectionAbortedError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError "Link to this definition")
:   A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when a connection attempt
    is aborted by the peer.
    Corresponds to `errno` [`ECONNABORTED`](https://docs.python.org/3/library/errno.html#errno.ECONNABORTED "errno.ECONNABORTED").

*exception* ConnectionRefusedError[¶](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError "Link to this definition")
:   A subclass of [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError"), raised when a connection attempt
    is refused by the peer.
    Corresponds to `errno` [`ECONNREFUSED`](https://docs.python.org/3/library/errno.html#errno.ECONNREFUSED