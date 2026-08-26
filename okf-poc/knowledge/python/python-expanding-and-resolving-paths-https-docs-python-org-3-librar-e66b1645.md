---
id: python-expanding-and-resolving-paths-https-docs-python-org-3-librar-e66b1645
type: concept
title: Expanding and resolving paths[¶](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths
  "Link to this heading")
description: '*classmethod* Path.home()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Expanding and resolving paths[¶](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths "Link to this heading")

*classmethod* Path.home()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home "Link to this definition")
:   Return a new path object representing the user’s home directory (as
    returned by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") with `~` construct). If the home
    directory can’t be resolved, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.

    ```
    >>> Path.home()
    PosixPath('/home/antoine')
    ```

    Added in version 3.5.

Path.expanduser()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "Link to this definition")
:   Return a new path with expanded `~` and `~user` constructs,
    as returned by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser"). If a home directory can’t be
    resolved, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.

    ```
    >>> p = PosixPath('~/films/Monty Python')
    >>> p.expanduser()
    PosixPath('/home/eric/films/Monty Python')
    ```

    Added in version 3.5.

*classmethod* Path.cwd()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd "Link to this definition")
:   Return a new path object representing the current directory (as returned
    by [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd "os.getcwd")):

    ```
    >>> Path.cwd()
    PosixPath('/home/antoine/pathlib')
    ```

Path.absolute()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "Link to this definition")
:   Make the path absolute, without normalization or resolving symlinks.
    Returns a new path object:

    ```
    >>> p = Path('tests')
    >>> p
    PosixPath('tests')
    >>> p.absolute()
    PosixPath('/home/antoine/pathlib/tests')
    ```

Path.resolve(*strict=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve "Link to this definition")
:   Make the path absolute, resolving any symlinks. A new path object is
    returned:

    ```
    >>> p = Path()
    >>> p
    PosixPath('.')
    >>> p.resolve()
    PosixPath('/home/antoine/pathlib')
    ```

    “`..`” components are also eliminated (this is the only method to do so):

    ```
    >>> p = Path('docs/../setup.py')
    >>> p.resolve()
    PosixPath('/home/antoine/pathlib/setup.py')
    ```

    If a path doesn’t exist or a symlink loop is encountered, and *strict* is
    `True`, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised. If *strict* is `False`, the path is
    resolved as far as possible and any remainder is appended without checking
    whether it exists.

    Changed in version 3.6: The *strict* parameter was added (pre-3.6 behavior is strict).

    Changed in version 3.13: Symlink loops are treated like other errors: [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised in
    strict mode, and no exception is raised in non-strict mode. In previous
    versions, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised no matter the value of *strict*.

Path.readlink()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.readlink "Link to this definition")
:   Return the path to which the symbolic link points (as returned by
    [`os.readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink")):

    ```
    >>> p = Path('mylink')
    >>> p.symlink_to('setup.py')
    >>> p.readlink()
    PosixPath('setup.py')
    ```

    Added in version 3.9.

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "