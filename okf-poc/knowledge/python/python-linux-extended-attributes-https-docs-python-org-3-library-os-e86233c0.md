---
id: python-linux-extended-attributes-https-docs-python-org-3-library-os-e86233c0
type: concept
title: Linux extended attributes[¶](https://docs.python.org/3/library/os.html#linux-extended-attributes
  "Link to this heading")
description: Added in version 3.3.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Linux extended attributes[¶](https://docs.python.org/3/library/os.html#linux-extended-attributes "Link to this heading")

Added in version 3.3.

These functions are all available on Linux only.

os.getxattr(*path*, *attribute*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/os.html#os.getxattr "Link to this definition")
:   Return the value of the extended filesystem attribute *attribute* for
    *path*. *attribute* can be bytes or str (directly or indirectly through the
    [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is str, it is encoded with the filesystem
    encoding.

    This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and
    [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.getxattr` with arguments `path`, `attribute`.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for *path* and *attribute*.

os.listxattr(*path=None*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/os.html#os.listxattr "Link to this definition")
:   Return a list of the extended filesystem attributes on *path*. The
    attributes in the list are represented as strings decoded with the filesystem
    encoding. If *path* is `None`, `listxattr()` will examine the current
    directory.

    This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and
    [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listxattr` with argument `path`.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.removexattr(*path*, *attribute*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/os.html#os.removexattr "Link to this definition")
:   Removes the extended filesystem attribute *attribute* from *path*.
    *attribute* should be bytes or str (directly or indirectly through the
    [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is a string, it is encoded
    with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler).

    This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and
    [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.removexattr` with arguments `path`, `attribute`.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for *path* and *attribute*.

os.setxattr(*path*, *attribute*, *value*, *flags=0*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/os.html#os.setxattr "Link to this definition")
:   Set the extended filesystem attribute *attribute* on *path* to *value*.
    *attribute* must be a bytes or str with no embedded NULs (directly or
    indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is a str,
    it is encoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler). *flags* may be
    [`XATTR_REPLACE`](https://docs.python.org/3/library/os.html#os.XATTR_REPLACE "os.XATTR_REPLACE") or [`XATTR_CREATE`](https://docs.python.org/3/library/os.html#os.XATTR_CREATE "os.XATTR_CREATE"). If `XATTR_REPLACE` is
    given and the attribute does not exist, `ENODATA` will be raised.
    If `XATTR_CREATE` is given and th