---
id: python-filter-errors-https-docs-python-org-3-library-tarfile-html-f-47076c99
type: concept
title: Filter errors[¶](https://docs.python.org/3/library/tarfile.html#filter-errors
  "Link to this heading")
description: When a filter refuses to extract a file, it will raise an appropriate
  exception,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Filter errors[¶](https://docs.python.org/3/library/tarfile.html#filter-errors "Link to this heading")

When a filter refuses to extract a file, it will raise an appropriate exception,
a subclass of [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError").
This will abort the extraction if [`TarFile.errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel") is 1 or more.
With `errorlevel=0` the error will be logged and the member will be skipped,
but extraction will continue.