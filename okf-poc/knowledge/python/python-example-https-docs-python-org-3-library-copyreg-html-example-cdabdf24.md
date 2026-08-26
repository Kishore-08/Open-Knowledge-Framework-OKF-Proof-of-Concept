---
id: python-example-https-docs-python-org-3-library-copyreg-html-example-cdabdf24
type: concept
title: Example[¶](https://docs.python.org/3/library/copyreg.html#example "Link to
  this heading")
description: The example below would like to show how to register a pickle function
  and how
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/copyreg.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Example[¶](https://docs.python.org/3/library/copyreg.html#example "Link to this heading")

The example below would like to show how to register a pickle function and how
it will be used:

```
>>> import copyreg, copy, pickle
>>> class C:
...     def __init__(self, a):
...         self.a = a
...
>>> def pickle_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
>>> copyreg.pickle(C, pickle_c)
>>> c = C(1)
>>> d = copy.copy(c)
pickling a C instance...
>>> p = pickle.dumps(c)
pickling a C instance...
```