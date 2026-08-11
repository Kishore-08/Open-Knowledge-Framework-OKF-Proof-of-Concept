---
id: python-pure-paths-https-docs-python-org-3-library-pathlib-html-pure-e66b1645
type: concept
title: Pure paths[¶](https://docs.python.org/3/library/pathlib.html#pure-paths "Link
  to this heading")
description: Pure path objects provide path-handling operations which don’t actually
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Pure paths[¶](https://docs.python.org/3/library/pathlib.html#pure-paths "Link to this heading")

Pure path objects provide path-handling operations which don’t actually
access a filesystem. There are three ways to access these classes, which
we also call *flavours*:

*class* pathlib.PurePath(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "Link to this definition")
:   A generic class that represents the system’s path flavour (instantiating
    it creates either a [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath") or a [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath")):

    ```
    >>> PurePath('setup.py')      # Running on a Unix machine
    PurePosixPath('setup.py')
    ```

    Each element of *pathsegments* can be either a string representing a
    path segment, or an object implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface
    where the [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__") method returns a string,
    such as another path object:

    ```
    >>> PurePath('foo', 'some/path', 'bar')
    PurePosixPath('foo/some/path/bar')
    >>> PurePath(Path('foo'), Path('bar'))
    PurePosixPath('foo/bar')
    ```

    When *pathsegments* is empty, the current directory is assumed:

    ```
    >>> PurePath()
    PurePosixPath('.')
    ```

    If a segment is an absolute path, all previous segments are ignored
    (like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join")):

    ```
    >>> PurePath('/etc', '/usr', 'lib64')
    PurePosixPath('/usr/lib64')
    >>> PureWindowsPath('c:/Windows', 'd:bar')
    PureWindowsPath('d:bar')
    ```

    On Windows, the drive is not reset when a rooted relative path
    segment (e.g., `r'\foo'`) is encountered:

    ```
    >>> PureWindowsPath('c:/Windows', '/Program Files')
    PureWindowsPath('c:/Program Files')
    ```

    Spurious slashes and single dots are collapsed, but double dots (`'..'`)
    and leading double slashes (`'//'`) are not, since this would change the
    meaning of a path for various reasons (e.g. symbolic links, UNC paths):

    ```
    >>> PurePath('foo//bar')
    PurePosixPath('foo/bar')
    >>> PurePath('//foo/bar')
    PurePosixPath('//foo/bar')
    >>> PurePath('foo/./bar')
    PurePosixPath('foo/bar')
    >>> PurePath('foo/../bar')
    PurePosixPath('foo/../bar')
    ```

    (a naïve approach would make `PurePosixPath('foo/../bar')` equivalent
    to `PurePosixPath('bar')`, which is wrong if `foo` is a symbolic link
    to another directory)

    Pure path objects implement the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface, allowing them
    to be used anywhere the interface is accepted.

    Changed in version 3.6: Added support for the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface.

*class* pathlib.PurePosixPath(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "Link to this definition")
:   A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this path flavour represents non-Windows
    filesystem paths:

    ```
    >>> PurePosixPath('/etc/hosts')
    PurePosixPath('/etc/hosts')
    ```

    *pathsegments* is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

*class* pathlib.PureWindowsPath(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "Link to this definition")
:   A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this path flavour represents Windows