---
id: python-file-object-creation-https-docs-python-org-3-library-os-html-e86233c0
type: concept
title: File Object Creation[¶](https://docs.python.org/3/library/os.html#file-object-creation
  "Link to this heading")
description: These functions create new [file objects](https://docs.python.org/3/glossary.html#term-file-object).
  (See also
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## File Object Creation[¶](https://docs.python.org/3/library/os.html#file-object-creation "Link to this heading")

These functions create new [file objects](https://docs.python.org/3/glossary.html#term-file-object). (See also
[`open()`](https://docs.python.org/3/library/os.html#os.open "os.open") for opening file descriptors.)

os.fdopen(*fd*, *\*args*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/os.html#os.fdopen "Link to this definition")
:   Return an open file object connected to the file descriptor *fd*. This is an
    alias of the [`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function and accepts the same arguments.
    The only difference is that the first argument of `fdopen()` must always
    be an integer.