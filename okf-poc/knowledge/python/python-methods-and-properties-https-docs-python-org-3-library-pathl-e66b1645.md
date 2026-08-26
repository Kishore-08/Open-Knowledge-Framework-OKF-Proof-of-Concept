---
id: python-methods-and-properties-https-docs-python-org-3-library-pathl-e66b1645
type: concept
title: Methods and properties[¶](https://docs.python.org/3/library/pathlib.html#methods-and-properties
  "Link to this heading")
description: 'Pure paths provide the following methods and properties:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Methods and properties[¶](https://docs.python.org/3/library/pathlib.html#methods-and-properties "Link to this heading")

Pure paths provide the following methods and properties:

PurePath.parser[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parser "Link to this definition")
:   The implementation of the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") module used for low-level path
    parsing and joining: either `posixpath` or `ntpath`.

    Added in version 3.13.

PurePath.drive[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.drive "Link to this definition")
:   A string representing the drive letter or name, if any:

    ```
    >>> PureWindowsPath('c:/Program Files/').drive
    'c:'
    >>> PureWindowsPath('/Program Files/').drive
    ''
    >>> PurePosixPath('/etc').drive
    ''
    ```

    UNC shares are also considered drives:

    ```
    >>> PureWindowsPath('//host/share/foo.txt').drive
    '\\\\host\\share'
    ```

PurePath.root[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.root "Link to this definition")
:   A string representing the (local or global) root, if any:

    ```
    >>> PureWindowsPath('c:/Program Files/').root
    '\\'
    >>> PureWindowsPath('c:Program Files/').root
    ''
    >>> PurePosixPath('/etc').root
    '/'
    ```

    UNC shares always have a root:

    ```
    >>> PureWindowsPath('//host/share').root
    '\\'
    ```

    If the path starts with more than two successive slashes,
    [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath") collapses them:

    ```
    >>> PurePosixPath('//etc').root
    '//'
    >>> PurePosixPath('///etc').root
    '/'
    >>> PurePosixPath('////etc').root
    '/'
    ```

    Note

    This behavior conforms to *The Open Group Base Specifications Issue 6*,
    paragraph [4.11 Pathname Resolution](https://pubs.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap04.html#tag_04_11):

    *“A pathname that begins with two successive slashes may be interpreted in
    an implementation-defined manner, although more than two leading slashes
    shall be treated as a single slash.”*

PurePath.anchor[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.anchor "Link to this definition")
:   The concatenation of the drive and root:

    ```
    >>> PureWindowsPath('c:/Program Files/').anchor
    'c:\\'
    >>> PureWindowsPath('c:Program Files/').anchor
    'c:'
    >>> PurePosixPath('/etc').anchor
    '/'
    >>> PureWindowsPath('//host/share').anchor
    '\\\\host\\share\\'
    ```

PurePath.parents[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents "Link to this definition")
:   An immutable sequence providing access to the logical ancestors of
    the path:

    ```
    >>> p = PureWindowsPath('c:/foo/bar/setup.py')
    >>> p.parents[0]
    PureWindowsPath('c:/foo/bar')
    >>> p.parents[1]
    PureWindowsPath('c:/foo')
    >>> p.parents[2]
    PureWindowsPath('c:/')
    ```

    Changed in version 3.10: The parents sequence now supports [slices](https://docs.python.org/3/glossary.html#term-slice) and negative index values.

PurePath.parent[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent "Link to this definition")
:   The logical parent of the path:

    ```
    >>> p = PurePosixPath('/a/b/c/d')
    >>> p.parent
    PurePosixPath('/a/b/c')
    ```

    You cannot go past an anchor, or empty path:

    ```
    >>> p = PurePosixPath('/')
    >>> p.parent
    PurePosixPath('/')
    >>> p = PurePosixPath('.')
    >>> p.parent
    PurePosixPath('.')
    ```

    Note

    This is a purely lexical operation, hence the following behaviour:

    ```
    >>> p = PurePosixPath('foo/..')
    >>> p.parent
    PurePosixPath('foo')
    ```

    If you want to walk an arbitrary filesystem path upwards, it is
    recommended to first call