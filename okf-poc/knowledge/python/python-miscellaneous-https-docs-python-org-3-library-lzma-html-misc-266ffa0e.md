---
id: python-miscellaneous-https-docs-python-org-3-library-lzma-html-misc-266ffa0e
type: concept
title: Miscellaneous[¶](https://docs.python.org/3/library/lzma.html#miscellaneous
  "Link to this heading")
description: lzma.is\_check\_supported(*check*)[¶](https://docs.python.org/3/library/lzma.html#lzma.is_check_supported
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Miscellaneous[¶](https://docs.python.org/3/library/lzma.html#miscellaneous "Link to this heading")

lzma.is\_check\_supported(*check*)[¶](https://docs.python.org/3/library/lzma.html#lzma.is_check_supported "Link to this definition")
:   Return `True` if the given integrity check is supported on this system.

    [`CHECK_NONE`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "lzma.CHECK_NONE") and [`CHECK_CRC32`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "lzma.CHECK_CRC32") are always supported.
    [`CHECK_CRC64`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "lzma.CHECK_CRC64") and [`CHECK_SHA256`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "lzma.CHECK_SHA256") may be unavailable if you are
    using a version of **liblzma** that was compiled with a limited
    feature set.