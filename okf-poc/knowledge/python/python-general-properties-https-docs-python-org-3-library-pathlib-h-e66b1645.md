---
id: python-general-properties-https-docs-python-org-3-library-pathlib-h-e66b1645
type: concept
title: General properties[¶](https://docs.python.org/3/library/pathlib.html#general-properties
  "Link to this heading")
description: Paths are immutable and [hashable](https://docs.python.org/3/glossary.html#term-hashable).
  Paths of a same flavour are comparable
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### General properties[¶](https://docs.python.org/3/library/pathlib.html#general-properties "Link to this heading")

Paths are immutable and [hashable](https://docs.python.org/3/glossary.html#term-hashable). Paths of a same flavour are comparable
and orderable. These properties respect the flavour’s case-folding
semantics:

```
>>> PurePosixPath('foo') == PurePosixPath('FOO')
False
>>> PureWindowsPath('foo') == PureWindowsPath('FOO')
True
>>> PureWindowsPath('FOO') in { PureWindowsPath('foo') }
True
>>> PureWindowsPath('C:') < PureWindowsPath('d:')
True
```

Paths of a different flavour compare unequal and cannot be ordered:

```
>>> PureWindowsPath('foo') == PurePosixPath('foo')
False
>>> PureWindowsPath('foo') < PurePosixPath('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPath'
```