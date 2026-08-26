---
id: python-text-encoding-https-docs-python-org-3-library-io-html-text-e-dbdafd7f
type: concept
title: Text Encoding[¶](https://docs.python.org/3/library/io.html#text-encoding "Link
  to this heading")
description: The default encoding of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper
  "io.TextIOWrapper") and [`open()`](https://docs.python.org/3/library/functions.html#open
  "open") is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Text Encoding[¶](https://docs.python.org/3/library/io.html#text-encoding "Link to this heading")

The default encoding of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and [`open()`](https://docs.python.org/3/library/functions.html#open "open") is
locale-specific ([`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")).

However, many developers forget to specify the encoding when opening text files
encoded in UTF-8 (e.g. JSON, TOML, Markdown, etc…) since most Unix
platforms use UTF-8 locale by default. This causes bugs because the locale
encoding is not UTF-8 for most Windows users. For example:

```
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()
```

Accordingly, it is highly recommended that you specify the encoding
explicitly when opening text files. If you want to use UTF-8, pass
`encoding="utf-8"`. To use the current locale encoding,
`encoding="locale"` is supported since Python 3.10.

See also

[Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
:   Python UTF-8 Mode can be used to change the default encoding to
    UTF-8 from locale-specific encoding.

[**PEP 686**](https://peps.python.org/pep-0686/)
:   Python 3.15 will make [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) default.