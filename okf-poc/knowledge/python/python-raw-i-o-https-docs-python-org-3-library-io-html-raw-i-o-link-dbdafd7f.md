---
id: python-raw-i-o-https-docs-python-org-3-library-io-html-raw-i-o-link-dbdafd7f
type: concept
title: Raw I/O[¶](https://docs.python.org/3/library/io.html#raw-i-o "Link to this
  heading")
description: Raw I/O (also called *unbuffered I/O*) is generally used as a low-level
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Raw I/O[¶](https://docs.python.org/3/library/io.html#raw-i-o "Link to this heading")

Raw I/O (also called *unbuffered I/O*) is generally used as a low-level
building-block for binary and text streams; it is rarely useful to directly
manipulate a raw stream from user code. Nevertheless, you can create a raw
stream by opening a file in binary mode with buffering disabled:

```
f = open("myfile.jpg", "rb", buffering=0)
```

The raw stream API is described in detail in the docs of [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase").

Warning

Raw I/O is a low-level interface and methods generally must have their return
values checked and be explicitly retried to ensure an operation completes.
For instance [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write") returns the number of bytes written
which may be less than the number of bytes provided (a partial write).
High-level I/O objects like [Binary I/O](https://docs.python.org/3/library/io.html#binary-io) and [Text I/O](https://docs.python.org/3/library/io.html#text-io) implement
retry behavior.