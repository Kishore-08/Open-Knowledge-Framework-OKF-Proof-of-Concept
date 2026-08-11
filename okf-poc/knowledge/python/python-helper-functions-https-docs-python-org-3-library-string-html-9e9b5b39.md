---
id: python-helper-functions-https-docs-python-org-3-library-string-html-9e9b5b39
type: concept
title: Helper functions[¶](https://docs.python.org/3/library/string.html#helper-functions
  "Link to this heading")
description: string.capwords(*s*, *sep=None*)[¶](https://docs.python.org/3/library/string.html#string.capwords
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Helper functions[¶](https://docs.python.org/3/library/string.html#helper-functions "Link to this heading")

string.capwords(*s*, *sep=None*)[¶](https://docs.python.org/3/library/string.html#string.capwords "Link to this definition")
:   Split the argument into words using [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split "str.split"), capitalize each word
    using [`str.capitalize()`](https://docs.python.org/3/library/stdtypes.html#str.capitalize "str.capitalize"), and join the capitalized words using
    [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join "str.join"). If the optional second argument *sep* is absent
    or `None`, runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise *sep* is used to
    split and join the words.