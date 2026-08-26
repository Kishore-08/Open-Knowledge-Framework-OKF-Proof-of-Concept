---
id: python-tarfile-read-and-write-tar-archive-files-https-docs-python-o-47076c99
type: concept
title: '`tarfile` — Read and write tar archive files[¶](https://docs.python.org/3/librar'
description: '**Source code:** [Lib/tarfile.py](https://github.com/python/cpython/tree/3.14/Lib/tarfile.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `tarfile` — Read and write tar archive files[¶](https://docs.python.org/3/library/tarfile.html#module-tarfile "Link to this heading")

**Source code:** [Lib/tarfile.py](https://github.com/python/cpython/tree/3.14/Lib/tarfile.py)

---

The `tarfile` module makes it possible to read and write tar
archives, including those using gzip, bz2 and lzma compression.
Use the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") module to read or write `.zip` files, or the
higher-level functions in [shutil](https://docs.python.org/3/library/shutil.html#archiving-operations).

Some facts and figures:

- reads and writes [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library."), and
  [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compressed archives if the respective modules are available.

  If any of these [optional modules](https://docs.python.org/3/glossary.html#term-optional-module) are missing from
  your copy of CPython, look for documentation from your distributor (that is,
  whoever provided Python to you).
  If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
- read/write support for the POSIX.1-1988 (ustar) format.
- read/write support for the GNU tar format including *longname* and *longlink*
  extensions, read-only support for all variants of the *sparse* extension
  including restoration of sparse files.
- read/write support for the POSIX.1-2001 (pax) format.
- handles directories, regular files, hardlinks, symbolic links, fifos,
  character devices and block devices and is able to acquire and restore file
  information like timestamp, access permissions and owner.

Changed in version 3.3: Added support for [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compression.

Changed in version 3.12: Archives are extracted using a [filter](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter),
which makes it possible to either limit surprising/dangerous features,
or to acknowledge that they are expected and the archive is fully trusted.

Changed in version 3.14: Set the default extraction filter to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter"),
which disallows some dangerous features such as links to absolute paths
or paths outside of the destination. Previously, the filter strategy
was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").

Changed in version 3.14: Added support for Zstandard compression using [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.").

tarfile.open(*name=None*, *mode='r'*, *fileobj=None*, *bufsize=10240*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.open "Link to this definition")
:   Return a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object for the pathname *name*. For detailed
    information on `TarFile` objects and the keyword arguments that are
    allowed, see [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects).

    *mode* has to be a string of the form