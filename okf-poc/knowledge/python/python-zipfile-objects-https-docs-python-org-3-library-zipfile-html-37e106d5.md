---
id: python-zipfile-objects-https-docs-python-org-3-library-zipfile-html-37e106d5
type: concept
title: ZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#zipfile-objects
  "Link to this heading")
description: '*class* zipfile.ZipFile(*file*, *mode=''r''*, *compression=ZIP\_STORED*,
  *allowZip64=True*, *compresslevel=None*, *\**, *strict\_timestamps=True*, *metadata\_encoding=None*)[¶](https://docs.python.org/3'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## ZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#zipfile-objects "Link to this heading")

*class* zipfile.ZipFile(*file*, *mode='r'*, *compression=ZIP\_STORED*, *allowZip64=True*, *compresslevel=None*, *\**, *strict\_timestamps=True*, *metadata\_encoding=None*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "Link to this definition")
:   Open a ZIP file, where *file* can be a path to a file (a string), a
    file-like object or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

    The *mode* parameter should be `'r'` to read an existing
    file, `'w'` to truncate and write a new file, `'a'` to append to an
    existing file, or `'x'` to exclusively create and write a new file.
    If *mode* is `'x'` and *file* refers to an existing file,
    a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised.
    If *mode* is `'a'` and *file* refers to an existing ZIP
    file, then additional files are added to it. If *file* does not refer to a
    ZIP file, then a new ZIP archive is appended to the file. This is meant for
    adding a ZIP archive to another file (such as `python.exe`). If
    *mode* is `'a'` and the file does not exist at all, it is created.
    If *mode* is `'r'` or `'a'`, the file should be seekable.

    *compression* is the ZIP compression method to use when writing the archive,
    and should be [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED"), [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED"),
    [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2"), [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA"), or [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD");
    unrecognized values will cause [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") to be raised. If
    `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or
    `ZIP_ZSTANDARD` is specified but the corresponding module
    ([`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), or [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")) is not
    available, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. The default is `ZIP_STORED`.

    If *allowZip64* is `True` (the default) zipfile will create ZIP files that
    use the ZIP64 extensions when the zipfile is larger than 4 GiB. If it is
    `false` `zipfile` will raise an exception when the ZIP file would
    require ZIP64 extensions.

    The *compresslevel* parameter controls the compression level to use when
    writing files to the archive.
    When using [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED") or [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA") it has no effect.
    When using [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED") integers `0` through `9` are accepted
    (see [`zlib`](https://docs.python.org/3/library/zlib.html#zlib.compressobj "zlib.compressobj") for more information).
    When using [`ZIP_BZIP2`](https://docs.pyt