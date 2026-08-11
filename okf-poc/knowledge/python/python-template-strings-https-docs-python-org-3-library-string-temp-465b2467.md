---
id: python-template-strings-https-docs-python-org-3-library-string-temp-465b2467
type: concept
title: Template strings[¶](https://docs.python.org/3/library/string.templatelib.html#template-strings
  "Link to this heading")
description: Added in version 3.14.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.templatelib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Template strings[¶](https://docs.python.org/3/library/string.templatelib.html#template-strings "Link to this heading")

Added in version 3.14.

Template strings are a mechanism for custom string processing.
They have the full flexibility of Python’s [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings),
but return a [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template") instance that gives access
to the static and interpolated (in curly brackets) parts of a string
*before* they are combined.

To write a t-string, use a `'t'` prefix instead of an `'f'`, like so:

```
>>> pi = 3.14
>>> t't-strings are new in Python {pi!s}!'
Template(
   strings=('t-strings are new in Python ', '!'),
   interpolations=(Interpolation(3.14, 'pi', 's', ''),)
)
```