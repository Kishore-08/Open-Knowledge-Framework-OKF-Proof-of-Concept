---
id: python-binary-i-o-https-docs-python-org-3-library-io-html-binary-i--dbdafd7f
type: concept
title: Binary I/O[¶](https://docs.python.org/3/library/io.html#binary-i-o "Link to
  this heading")
description: Binary I/O (also called *buffered I/O*) expects
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Binary I/O[¶](https://docs.python.org/3/library/io.html#binary-i-o "Link to this heading")

Binary I/O (also called *buffered I/O*) expects
[bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) and produces [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
objects. No encoding, decoding, or newline translation is performed. This
category of streams can be used for all kinds of non-text data, and also when
manual control over the handling of text data is desired.

The easiest way to create a binary stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open") with `'b'` in
the mode string:

```
f = open("myfile.jpg", "rb")
```

In-memory binary streams are also available as [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") objects:

```
f = io.BytesIO(b"some initial binary data: \x00\x01")
```

The binary stream API is described in detail in the docs of
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

Other library modules may provide additional ways to create text or binary
streams. See [`socket.socket.makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile") for example.