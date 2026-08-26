---
id: python-unicode-issues-https-docs-python-org-3-library-tarfile-html--47076c99
type: concept
title: Unicode issues[¶](https://docs.python.org/3/library/tarfile.html#unicode-issues
  "Link to this heading")
description: The tar format was originally conceived to make backups on tape drives
  with the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Unicode issues[¶](https://docs.python.org/3/library/tarfile.html#unicode-issues "Link to this heading")

The tar format was originally conceived to make backups on tape drives with the
main focus on preserving file system information. Nowadays tar archives are
commonly used for file distribution and exchanging archives over networks. One
problem of the original format (which is the basis of all other formats) is
that there is no concept of supporting different character encodings. For
example, an ordinary tar archive created on a *UTF-8* system cannot be read
correctly on a *Latin-1* system if it contains non-*ASCII* characters. Textual
metadata (like filenames, linknames, user/group names) will appear damaged.
Unfortunately, there is no way to autodetect the encoding of an archive. The
pax format was designed to solve this problem. It stores non-ASCII metadata
using the universal character encoding *UTF-8*.

The details of character conversion in `tarfile` are controlled by the
*encoding* and *errors* keyword arguments of the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") class.

*encoding* defines the character encoding to use for the metadata in the
archive. The default value is [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") or `'ascii'`
as a fallback. Depending on whether the archive is read or written, the
metadata must be either decoded or encoded. If *encoding* is not set
appropriately, this conversion may fail.

The *errors* argument defines how characters are treated that cannot be
converted. Possible values are listed in section [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers).
The default scheme is `'surrogateescape'` which Python also uses for its
file system calls, see [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#os-filenames).

For [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") archives (the default), *encoding* is generally not needed
because all the metadata is stored using *UTF-8*. *encoding* is only used in
the rare cases when binary pax headers are decoded or when strings with
surrogate characters are stored.