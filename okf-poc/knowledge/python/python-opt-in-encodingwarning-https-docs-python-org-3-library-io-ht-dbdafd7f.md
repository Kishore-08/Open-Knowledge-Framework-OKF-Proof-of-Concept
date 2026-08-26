---
id: python-opt-in-encodingwarning-https-docs-python-org-3-library-io-ht-dbdafd7f
type: concept
title: Opt-in EncodingWarning[¶](https://docs.python.org/3/library/io.html#opt-in-encodingwarning
  "Link to this heading")
description: 'Added in version 3.10: See [**PEP 597**](https://peps.python.org/pep-0597/)
  for more details.'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Opt-in EncodingWarning[¶](https://docs.python.org/3/library/io.html#opt-in-encodingwarning "Link to this heading")

Added in version 3.10: See [**PEP 597**](https://peps.python.org/pep-0597/) for more details.

To find where the default locale encoding is used, you can enable
the [`-X warn_default_encoding`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option or set the
[`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) environment variable, which will
emit an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") when the default encoding is used.

If you are providing an API that uses [`open()`](https://docs.python.org/3/library/functions.html#open "open") or
[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and passes `encoding=None` as a parameter, you
can use [`text_encoding()`](https://docs.python.org/3/library/io.html#io.text_encoding "io.text_encoding") so that callers of the API will emit an
[`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if they don’t pass an `encoding`. However,
please consider using UTF-8 by default (i.e. `encoding="utf-8"`) for
new APIs.