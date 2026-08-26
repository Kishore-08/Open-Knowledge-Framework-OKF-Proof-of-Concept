---
id: python-text-i-o-https-docs-python-org-3-library-io-html-text-i-o-li-dbdafd7f
type: concept
title: Text I/O[¶](https://docs.python.org/3/library/io.html#text-i-o "Link to this
  heading")
description: Text I/O expects and produces [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") objects. This means that whenever
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Text I/O[¶](https://docs.python.org/3/library/io.html#text-i-o "Link to this heading")

Text I/O expects and produces [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects. This means that whenever
the backing store is natively made of bytes (such as in the case of a file),
encoding and decoding of data is made transparently as well as optional
translation of platform-specific newline characters.

The easiest way to create a text stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open"), optionally
specifying an encoding:

```
f = open("myfile.txt", "r", encoding="utf-8")
```

In-memory text streams are also available as [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") objects:

```
f = io.StringIO("some initial text data")
```

Note

When working with a non-blocking stream, be aware that read operations on text I/O objects
might raise a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") if the stream cannot perform the operation
immediately.

The text stream API is described in detail in the documentation of
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").