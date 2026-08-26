---
id: python-class-hierarchy-https-docs-python-org-3-library-io-html-clas-dbdafd7f
type: concept
title: Class hierarchy[¶](https://docs.python.org/3/library/io.html#class-hierarchy
  "Link to this heading")
description: The implementation of I/O streams is organized as a hierarchy of classes.
  First
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Class hierarchy[¶](https://docs.python.org/3/library/io.html#class-hierarchy "Link to this heading")

The implementation of I/O streams is organized as a hierarchy of classes. First
[abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) (ABCs), which are used to
specify the various categories of streams, then concrete classes providing the
standard stream implementations.

Note

The abstract base classes also provide default implementations of some
methods in order to help implementation of concrete stream classes. For
example, [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") provides unoptimized implementations of
`readinto()` and `readline()`.

At the top of the I/O hierarchy is the abstract base class [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are allowed
to raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation") if they do not support a given operation.

The [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with the reading
and writing of bytes to a stream. [`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") subclasses `RawIOBase`
to provide an interface to files in the machine’s file system.

The [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with
buffering on a raw binary stream ([`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")). Its subclasses,
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"), and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair")
buffer raw binary streams that are writable, readable, and both readable and writable,
respectively. [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") provides a buffered interface to seekable streams.
Another `BufferedIOBase` subclass, [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), is a stream of
in-memory bytes.

The [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with
streams whose bytes represent text, and handles encoding and decoding to and
from strings. [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"), which extends `TextIOBase`, is a buffered text
interface to a buffered raw stream ([`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")). Finally,
[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") is an in-memory stream for text.

Argument names are not part of the specification, and only the arguments of
[`open()`](https://docs.python.org/3/library/functions.html#open "open") are intended to be used as keyword arguments.

The following table summarizes the ABCs provided by the `io` module:

| ABC | Inherits | Stub Methods | Mixin Methods and Properties |
| --- | --- | --- | --- |
| [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") |  | `fileno`, `seek`, and `truncate` | `close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable`, and `writelines` |