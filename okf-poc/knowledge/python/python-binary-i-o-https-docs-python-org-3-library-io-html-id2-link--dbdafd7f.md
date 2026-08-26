---
id: python-binary-i-o-https-docs-python-org-3-library-io-html-id2-link--dbdafd7f
type: concept
title: Binary I/O[¶](https://docs.python.org/3/library/io.html#id2 "Link to this heading")
description: By reading and writing only large chunks of data even when the user asks
  for a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Binary I/O[¶](https://docs.python.org/3/library/io.html#id2 "Link to this heading")

By reading and writing only large chunks of data even when the user asks for a
single byte, buffered I/O hides any inefficiency in calling and executing the
operating system’s unbuffered I/O routines. The gain depends on the OS and the
kind of I/O which is performed. For example, on some modern OSes such as Linux,
unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however,
is that buffered I/O offers predictable performance regardless of the platform
and the backing device. Therefore, it is almost always preferable to use
buffered I/O rather than unbuffered I/O for binary data.