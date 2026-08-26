---
id: python-helper-functions-https-docs-python-org-3-library-string-temp-465b2467
type: concept
title: Helper functions[¶](https://docs.python.org/3/library/string.templatelib.html#helper-functions
  "Link to this heading")
description: string.templatelib.convert(*obj*, */*, *conversion*)[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.convert
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.templatelib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Helper functions[¶](https://docs.python.org/3/library/string.templatelib.html#helper-functions "Link to this heading")

string.templatelib.convert(*obj*, */*, *conversion*)[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.convert "Link to this definition")
:   Applies formatted string literal [conversion](https://docs.python.org/3/library/string.html#formatstrings-conversion)
    semantics to the given object *obj*.
    This is frequently useful for custom template string processing logic.

    Three conversion flags are currently supported:

    - `'s'` which calls [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") on the value (like `!s`),
    - `'r'` which calls [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") (like `!r`), and
    - `'a'` which calls [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii") (like `!a`).

    If the conversion flag is `None`, *obj* is returned unchanged.