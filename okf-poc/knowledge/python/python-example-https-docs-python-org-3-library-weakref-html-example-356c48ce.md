---
id: python-example-https-docs-python-org-3-library-weakref-html-example-356c48ce
type: concept
title: Example[¶](https://docs.python.org/3/library/weakref.html#example "Link to
  this heading")
description: This simple example shows how an application can use object IDs to retrieve
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/weakref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Example[¶](https://docs.python.org/3/library/weakref.html#example "Link to this heading")

This simple example shows how an application can use object IDs to retrieve
objects that it has seen before. The IDs of the objects can then be used in
other data structures without forcing the objects to remain alive, but the
objects can still be retrieved by ID if they do.

```
import weakref

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]
```