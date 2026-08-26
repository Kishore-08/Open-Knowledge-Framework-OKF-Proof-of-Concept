---
id: python-overview-https-docs-python-org-3-library-io-html-overview-li-dbdafd7f
type: concept
title: Overview[¶](https://docs.python.org/3/library/io.html#overview "Link to this
  heading")
description: The `io` module provides Python’s main facilities for dealing with various
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Overview[¶](https://docs.python.org/3/library/io.html#overview "Link to this heading")

The `io` module provides Python’s main facilities for dealing with various
types of I/O. There are three main types of I/O: *text I/O*, *binary I/O*
and *raw I/O*. These are generic categories, and various backing stores can
be used for each of them. A concrete object belonging to any of these
categories is called a [file object](https://docs.python.org/3/glossary.html#term-file-object). Other common terms are *stream*
and *file-like object*.

Independent of its category, each concrete stream object will also have
various capabilities: it can be read-only, write-only, or read-write. It can
also allow arbitrary random access (seeking forwards or backwards to any
location), or only sequential access (for example in the case of a socket or
pipe).

All streams are careful about the type of data you give to them. For example
giving a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object to the `write()` method of a binary stream
will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). So will giving a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object to the
`write()` method of a text stream.

Changed in version 3.3: Operations that used to raise [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") now raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), since
`IOError` is now an alias of `OSError`.