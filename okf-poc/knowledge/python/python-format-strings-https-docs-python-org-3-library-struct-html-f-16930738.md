---
id: python-format-strings-https-docs-python-org-3-library-struct-html-f-16930738
type: concept
title: Format Strings[¶](https://docs.python.org/3/library/struct.html#format-strings
  "Link to this heading")
description: Format strings describe the data layout when
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Format Strings[¶](https://docs.python.org/3/library/struct.html#format-strings "Link to this heading")

Format strings describe the data layout when
packing and unpacking data. They are built up from [format characters](https://docs.python.org/3/library/struct.html#format-characters),
which specify the type of data being packed/unpacked. In addition,
special characters control the [byte order, size and alignment](https://docs.python.org/3/library/struct.html#struct-alignment).
Each format string consists of an optional prefix character which
describes the overall properties of the data and one or more format
characters which describe the actual data values and padding.