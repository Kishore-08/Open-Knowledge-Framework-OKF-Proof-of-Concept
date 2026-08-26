---
id: python-zipfile-work-with-zip-archives-https-docs-python-org-3-libra-37e106d5
type: concept
title: '`zipfile` — Work with ZIP archives[¶](https://docs.python.org/3/library/zipfile.'
description: '**Source code:** [Lib/zipfile/](https://github.com/python/cpython/tree/3.14/Lib/zipfile/)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `zipfile` — Work with ZIP archives[¶](https://docs.python.org/3/library/zipfile.html#module-zipfile "Link to this heading")

**Source code:** [Lib/zipfile/](https://github.com/python/cpython/tree/3.14/Lib/zipfile/)

---

The ZIP file format is a common archive and compression standard. This module
provides tools to create, read, write, append, and list a ZIP file. Any
advanced use of this module will require an understanding of the format, as
defined in [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT).

This module does not handle multipart ZIP files.
It can handle ZIP files that use the ZIP64 extensions
(that is ZIP files that are more than 4 GiB in size). It supports
decryption of encrypted files in ZIP archives, but it cannot
create an encrypted file. Decryption is extremely slow as it is
implemented in native Python rather than C.

Handling compressed archives requires [optional modules](https://docs.python.org/3/glossary.html#term-optional-module)
such as [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), and [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.").
If any of them are missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

The module defines the following items:

*exception* zipfile.BadZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "Link to this definition")
:   The error raised for bad ZIP files.

    Added in version 3.2.

*exception* zipfile.BadZipfile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipfile "Link to this definition")
:   Alias of [`BadZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "zipfile.BadZipFile"), for compatibility with older Python versions.

    Deprecated since version 3.2.

*exception* zipfile.LargeZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.LargeZipFile "Link to this definition")
:   The error raised when a ZIP file would require ZIP64 functionality but that has
    not been enabled.

*class* zipfile.ZipFile
:   The class for reading and writing ZIP files. See section
    [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects) for constructor details.

*class* zipfile.Path
:   Class that implements a subset of the interface provided by
    [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path"), including the full
    [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") interface.

    Added in version 3.8.

*class* zipfile.PyZipFile
:   Class for creating ZIP archives containing Python libraries.

*class* zipfile.ZipInfo(*filename='NoName'*, *date\_time=(1980, 1, 1, 0, 0, 0)*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "Link to this definition")
:   Class used to represent information about a member of an archive. Instances
    of this class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo") and [`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist")
    methods of [`ZipFile`](https://docs.p