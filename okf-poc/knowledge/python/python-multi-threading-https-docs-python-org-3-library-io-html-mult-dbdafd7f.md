---
id: python-multi-threading-https-docs-python-org-3-library-io-html-mult-dbdafd7f
type: concept
title: Multi-threading[¶](https://docs.python.org/3/library/io.html#multi-threading
  "Link to this heading")
description: '[`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO")
  objects are thread-safe to the extent that the operating system'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Multi-threading[¶](https://docs.python.org/3/library/io.html#multi-threading "Link to this heading")

[`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") objects are thread-safe to the extent that the operating system
calls (such as *[read(2)](https://manpages.debian.org/read(2))* under Unix) they wrap are thread-safe too.

Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair"))
protect their internal structures using a lock; it is therefore safe to call
them from multiple threads at once.

[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") objects are not thread-safe.