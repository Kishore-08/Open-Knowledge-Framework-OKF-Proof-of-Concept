---
id: python-native-formats-https-docs-python-org-3-library-struct-html-n-16930738
type: concept
title: Native Formats[¶](https://docs.python.org/3/library/struct.html#native-formats
  "Link to this heading")
description: When constructing format strings which mimic native layouts, the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Native Formats[¶](https://docs.python.org/3/library/struct.html#native-formats "Link to this heading")

When constructing format strings which mimic native layouts, the
compiler and machine architecture determine byte ordering and padding.
In such cases, the `@` format character should be used to specify
native byte ordering and data sizes. Internal pad bytes are normally inserted
automatically. It is possible that a zero-repeat format code will be
needed at the end of a format string to round up to the correct
byte boundary for proper alignment of consecutive chunks of data.

Consider these two simple examples (on a 64-bit, little-endian
machine):

```
>>> calcsize('@lhl')
24
>>> calcsize('@llh')
18
```

Data is not padded to an 8-byte boundary at the end of the second
format string without the use of extra padding. A zero-repeat format
code solves that problem:

```
>>> calcsize('@llh0l')
24
```

The `'x'` format code can be used to specify the repeat, but for
native formats it is better to use a zero-repeat format like `'0l'`.

By default, native byte ordering and alignment is used, but it is
better to be explicit and use the `'@'` prefix character.