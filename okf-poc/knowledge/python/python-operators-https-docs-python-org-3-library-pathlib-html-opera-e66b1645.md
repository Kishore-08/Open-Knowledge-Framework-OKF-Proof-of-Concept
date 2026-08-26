---
id: python-operators-https-docs-python-org-3-library-pathlib-html-opera-e66b1645
type: concept
title: Operators[¶](https://docs.python.org/3/library/pathlib.html#operators "Link
  to this heading")
description: The slash operator helps create child paths, like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join
  "os.path.join").
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Operators[¶](https://docs.python.org/3/library/pathlib.html#operators "Link to this heading")

The slash operator helps create child paths, like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join").
If the argument is an absolute path, the previous path is ignored.
On Windows, the drive is not reset when the argument is a rooted
relative path (e.g., `r'\foo'`):

```
>>> p = PurePath('/etc')
>>> p
PurePosixPath('/etc')
>>> p / 'init.d' / 'apache2'
PurePosixPath('/etc/init.d/apache2')
>>> q = PurePath('bin')
>>> '/usr' / q
PurePosixPath('/usr/bin')
>>> p / '/an_absolute_path'
PurePosixPath('/an_absolute_path')
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')
```

A path object can be used anywhere an object implementing [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
is accepted:

```
>>> import os
>>> p = PurePath('/etc')
>>> os.fspath(p)
'/etc'
```

The string representation of a path is the raw filesystem path itself
(in native form, e.g. with backslashes under Windows), which you can
pass to any function taking a file path as a string:

```
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program Files')
>>> str(p)
'c:\\Program Files'
```

Similarly, calling [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") on a path gives the raw filesystem path as a
bytes object, as encoded by [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode"):

```
>>> bytes(p)
b'/etc'
```

Note

Calling [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") is only recommended under Unix. Under Windows,
the unicode form is the canonical representation of filesystem paths.