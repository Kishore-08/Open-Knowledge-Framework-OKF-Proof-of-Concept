---
id: python-supported-tar-formats-https-docs-python-org-3-library-tarfil-47076c99
type: concept
title: Supported tar formats[¶](https://docs.python.org/3/library/tarfile.html#supported-tar-formats
  "Link to this heading")
description: 'There are three tar formats that can be created with the `tarfile` module:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Supported tar formats[¶](https://docs.python.org/3/library/tarfile.html#supported-tar-formats "Link to this heading")

There are three tar formats that can be created with the `tarfile` module:

- The POSIX.1-1988 ustar format ([`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT")). It supports filenames
  up to a length of at best 256 characters and linknames up to 100 characters.
  The maximum file size is 8 GiB. This is an old and limited but widely
  supported format.
- The GNU tar format ([`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")). It supports long filenames and
  linknames, files bigger than 8 GiB and sparse files. It is the de facto
  standard on GNU/Linux systems. `tarfile` fully supports the GNU tar
  extensions for long names, sparse file support is read-only.
- The POSIX.1-2001 pax format ([`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")). It is the most flexible
  format with virtually no limits. It supports long filenames and linknames, large
  files and stores pathnames in a portable way. Modern tar implementations,
  including GNU tar, bsdtar/libarchive and star, fully support extended *pax*
  features; some old or unmaintained libraries may not, but should treat
  *pax* archives as if they were in the universally supported *ustar* format.
  It is the current default format for new archives.

  It extends the existing *ustar* format with extra headers for information
  that cannot be stored otherwise. There are two flavours of pax headers:
  Extended headers only affect the subsequent file header, global
  headers are valid for the complete archive and affect all following files.
  All the data in a pax header is encoded in *UTF-8* for portability reasons.

There are some more variants of the tar format which can be read, but not
created:

- The ancient V7 format. This is the first tar format from Unix Seventh Edition,
  storing only regular files and directories. Names must not be longer than 100
  characters, there is no user/group name information. Some archives have
  miscalculated header checksums in case of fields with non-ASCII characters.
- The SunOS tar extended format. This format is a variant of the POSIX.1-2001
  pax format, but is not compatible.