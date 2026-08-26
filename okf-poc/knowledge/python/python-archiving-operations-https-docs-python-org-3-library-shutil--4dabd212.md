---
id: python-archiving-operations-https-docs-python-org-3-library-shutil--4dabd212
type: concept
title: Archiving operations[¶](https://docs.python.org/3/library/shutil.html#archiving-operations
  "Link to this heading")
description: Added in version 3.2.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Archiving operations[¶](https://docs.python.org/3/library/shutil.html#archiving-operations "Link to this heading")

Added in version 3.2.

Changed in version 3.5: Added support for the *xztar* format.

High-level utilities to create and read compressed and archived files are also
provided. They rely on the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") and [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.") modules.

shutil.make\_archive(*base\_name*, *format*[, *root\_dir*[, *base\_dir*[, *verbose*[, *dry\_run*[, *owner*[, *group*[, *logger*]]]]]]])[¶](https://docs.python.org/3/library/shutil.html#shutil.make_archive "Link to this definition")
:   Create an archive file (such as zip or tar) and return its name.

    *base\_name* is the name of the file to create, including the path, minus
    any format-specific extension.

    *format* is the archive format: one of
    “zip” (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available), “tar”, “gztar” (if the
    `zlib` module is available), “bztar” (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is
    available), “xztar” (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available), or “zstdtar”
    (if the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") module is available).

    *root\_dir* is a directory that will be the root directory of the
    archive, all paths in the archive will be relative to it; for example,
    we typically chdir into *root\_dir* before creating the archive.

    *base\_dir* is the directory where we start archiving from;
    i.e. *base\_dir* will be the common prefix of all files and
    directories in the archive. *base\_dir* must be given relative
    to *root\_dir*. See [Archiving example with base\_dir](https://docs.python.org/3/library/shutil.html#shutil-archiving-example-with-basedir) for how to
    use *base\_dir* and *root\_dir* together.

    *root\_dir* and *base\_dir* both default to the current directory.

    If *dry\_run* is true, no archive is created, but the operations that would be
    executed are logged to *logger*.

    *owner* and *group* are used when creating a tar archive. By default,
    uses the current owner and group.

    *logger* must be an object compatible with [**PEP 282**](https://peps.python.org/pep-0282/), usually an instance of
    [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger").

    The *verbose* argument is unused and deprecated.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.make_archive` with arguments `base_name`, `format`, `root_dir`, `base_dir`.

    Note

    This function is not thread-safe when custom archivers registered
    with [`register_archive_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "shutil.register_archive_format") do not support the *root\_dir*
    argument. In this case it
    temporarily changes the current working directory of the process
    to *root\_dir* to perform archiving.

    Changed in version 3.8: The modern pax (POSIX.1-2001) format is now used instead of
    the legacy GNU format for archives created with `format="tar"`.

    Changed in version 3.10.6: This function is now made thread-safe during creation of standard
    `.zip` and tar archives.

shutil.get\_archive\_formats()[¶](https://docs.python.org/3/library/shuti