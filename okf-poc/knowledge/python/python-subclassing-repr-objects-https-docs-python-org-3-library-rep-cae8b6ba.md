---
id: python-subclassing-repr-objects-https-docs-python-org-3-library-rep-cae8b6ba
type: concept
title: Subclassing Repr Objects[¶](https://docs.python.org/3/library/reprlib.html#subclassing-repr-objects
  "Link to this heading")
description: The use of dynamic dispatching by [`Repr.repr1()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr1
  "reprlib.Repr.repr1") allows subclasses of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/reprlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Subclassing Repr Objects[¶](https://docs.python.org/3/library/reprlib.html#subclassing-repr-objects "Link to this heading")

The use of dynamic dispatching by [`Repr.repr1()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr1 "reprlib.Repr.repr1") allows subclasses of
[`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr") to add support for additional built-in object types or to modify
the handling of types already supported. This example shows how special support
for file objects could be added:

```
import reprlib
import sys

class MyRepr(reprlib.Repr):

    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)

aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'
```

```
<stdin>
```