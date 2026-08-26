---
id: python-file-hashing-https-docs-python-org-3-library-hashlib-html-fi-4a693406
type: concept
title: File hashing[¶](https://docs.python.org/3/library/hashlib.html#file-hashing
  "Link to this heading")
description: The hashlib module provides a helper function for efficient hashing of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## File hashing[¶](https://docs.python.org/3/library/hashlib.html#file-hashing "Link to this heading")

The hashlib module provides a helper function for efficient hashing of
a file or file-like object.

hashlib.file\_digest(*fileobj*, *digest*, */*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.file_digest "Link to this definition")
:   Return a digest object that has been updated with contents of file object.

    *fileobj* must be a file-like object opened for reading in binary mode.
    It accepts file objects from builtin [`open()`](https://docs.python.org/3/library/functions.html#open "open"), [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
    instances, SocketIO objects from [`socket.socket.makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile"), and
    similar. *fileobj* must be opened in blocking mode, otherwise a
    [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") may be raised.

    The function may bypass Python’s I/O and use the file descriptor
    from [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") directly. *fileobj* must be assumed to be
    in an unknown state after this function returns or raises. It is up to
    the caller to close *fileobj*.

    *digest* must either be a hash algorithm name as a *str*, a hash
    constructor, or a callable that returns a hash object.

    Example:

    ```
    >>> import io, hashlib, hmac
    >>> with open("library/hashlib.rst", "rb") as f:
    ...     digest = hashlib.file_digest(f, "sha256")
    ...
    >>> digest.hexdigest()
    '...'
    ```

    ```
    >>> buf = io.BytesIO(b"somedata")
    >>> mac1 = hmac.HMAC(b"key", digestmod=hashlib.sha512)
    >>> digest = hashlib.file_digest(buf, lambda: mac1)
    ```

    ```
    >>> digest is mac1
    True
    >>> mac2 = hmac.HMAC(b"key", b"somedata", digestmod=hashlib.sha512)
    >>> mac1.digest() == mac2.digest()
    True
    ```

    Added in version 3.11.

    Changed in version 3.14: Now raises a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") if the file is opened in non-blocking
    mode. Previously, spurious null bytes were added to the digest.