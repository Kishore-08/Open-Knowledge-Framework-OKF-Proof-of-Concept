---
id: python-text-i-o-https-docs-python-org-3-library-io-html-id3-link-to-dbdafd7f
type: concept
title: Text I/O[¶](https://docs.python.org/3/library/io.html#id3 "Link to this heading")
description: Text I/O over a binary storage (such as a file) is significantly slower
  than
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Text I/O[¶](https://docs.python.org/3/library/io.html#id3 "Link to this heading")

Text I/O over a binary storage (such as a file) is significantly slower than
binary I/O over the same storage, because it requires conversions between
unicode and binary data using a character codec. This can become noticeable
handling huge amounts of text data like large log files. Also,
[`tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell") and [`seek()`](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "io.TextIOBase.seek") are both quite slow
due to the reconstruction algorithm used.

[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), however, is a native in-memory unicode container and will
exhibit similar speed to [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO").