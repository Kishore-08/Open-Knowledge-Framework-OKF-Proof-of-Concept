---
id: python-data-compression-and-archiving-https-docs-python-org-3-libra-b4327d91
type: concept
title: Data Compression and Archiving[¶](https://docs.python.org/3/library/archiving.ht
description: The modules described in this chapter support data compression with the
  zlib,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/archiving.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# Data Compression and Archiving[¶](https://docs.python.org/3/library/archiving.html#data-compression-and-archiving "Link to this heading")

The modules described in this chapter support data compression with the zlib,
gzip, bzip2, lzma, and zstd algorithms, and the creation of ZIP- and tar-format
archives. See also [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations) provided by the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
module.

- [The `compression` package](https://docs.python.org/3/library/compression.html)
- [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
  - [Exceptions](https://docs.python.org/3/library/compression.zstd.html#exceptions)
  - [Reading and writing compressed files](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files)
  - [Compressing and decompressing data in memory](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
  - [Zstandard dictionaries](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries)
  - [Advanced parameter control](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control)
  - [Miscellaneous](https://docs.python.org/3/library/compression.zstd.html#miscellaneous)
  - [Examples](https://docs.python.org/3/library/compression.zstd.html#examples)
- [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
- [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
  - [Examples of usage](https://docs.python.org/3/library/gzip.html#examples-of-usage)
  - [Command-line interface](https://docs.python.org/3/library/gzip.html#command-line-interface)
    - [Command-line options](https://docs.python.org/3/library/gzip.html#command-line-options)
- [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
  - [(De)compression of files](https://docs.python.org/3/library/bz2.html#de-compression-of-files)
  - [Incremental (de)compression](https://docs.python.org/3/library/bz2.html#incremental-de-compression)
  - [One-shot (de)compression](https://docs.python.org/3/library/bz2.html#one-shot-de-compression)
  - [Examples of usage](https://docs.python.org/3/library/bz2.html#examples-of-usage)
- [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
  - [Reading and writing compressed files](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files)
  - [Compressing and decompressing data in memory](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory)
  - [Miscellaneous](https://docs.python.org/3/library/lzma.html#miscellaneous)
  - [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains)
  - [Constants](https://docs.python.org/3/library/lzma.html#constants)
  - [Examples](https://docs.python.org/3/library/lzma.html#examples)
- [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
  - [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects)
  - [Path objects](https://docs.python.org/3/library/zipfile.html#path-objects)
  - [PyZipFile objects](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects)
  - [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects)
  - [Command-line interface](https://docs.python.org/3/library/zipfile.html#command-line-interface)
    - [Command-line options](https://docs.python.org/3/library/zipfile.html#command-line-options)
  - [Decompression pitfalls](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls)
    - [From file itself](https://docs.python.org/3/library/zipfile.html#from-file-itself)