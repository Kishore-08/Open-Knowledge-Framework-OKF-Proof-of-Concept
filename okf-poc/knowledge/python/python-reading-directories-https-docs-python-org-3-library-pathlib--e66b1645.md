---
id: python-reading-directories-https-docs-python-org-3-library-pathlib--e66b1645
type: concept
title: Reading directories[¶](https://docs.python.org/3/library/pathlib.html#reading-directories
  "Link to this heading")
description: Path.iterdir()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Reading directories[¶](https://docs.python.org/3/library/pathlib.html#reading-directories "Link to this heading")

Path.iterdir()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir "Link to this definition")
:   When the path points to a directory, yield path objects of the directory
    contents:

    ```
    >>> p = Path('docs')
    >>> for child in p.iterdir(): child
    ...
    PosixPath('docs/conf.py')
    PosixPath('docs/_templates')
    PosixPath('docs/make.bat')
    PosixPath('docs/index.rst')
    PosixPath('docs/_build')
    PosixPath('docs/_static')
    PosixPath('docs/Makefile')
    ```

    The children are yielded in arbitrary order, and the special entries
    `'.'` and `'..'` are not included. If a file is removed from or added
    to the directory after creating the iterator, it is unspecified whether
    a path object for that file is included.

    If the path is not a directory or otherwise inaccessible, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is
    raised.

Path.glob(*pattern*, *\**, *case\_sensitive=None*, *recurse\_symlinks=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "Link to this definition")
:   Glob the given relative *pattern* in the directory represented by this path,
    yielding all matching files (of any kind):

    ```
    >>> sorted(Path('.').glob('*.py'))
    [PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
    >>> sorted(Path('.').glob('*/*.py'))
    [PosixPath('docs/conf.py')]
    >>> sorted(Path('.').glob('**/*.py'))
    [PosixPath('build/lib/pathlib.py'),
     PosixPath('docs/conf.py'),
     PosixPath('pathlib.py'),
     PosixPath('setup.py'),
     PosixPath('test_pathlib.py')]
    ```

    Note

    The paths are returned in no particular order.
    If you need a specific order, sort the results.

    See also

    [Pattern language](https://docs.python.org/3/library/pathlib.html#pathlib-pattern-language) documentation.

    By default, or when the *case\_sensitive* keyword-only argument is set to
    `None`, this method matches paths using platform-specific casing rules:
    typically, case-sensitive on POSIX, and case-insensitive on Windows.
    Set *case\_sensitive* to `True` or `False` to override this behaviour.

    By default, or when the *recurse\_symlinks* keyword-only argument is set to
    `False`, this method follows symlinks except when expanding “`**`”
    wildcards. Set *recurse\_symlinks* to `True` to always follow symlinks.

    Note

    Any [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exceptions raised from scanning the filesystem are
    suppressed. This includes [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError") when accessing
    directories without read permission.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `pathlib.Path.glob` with arguments `self`, `pattern`.

    Changed in version 3.12: The *case\_sensitive* parameter was added.

    Changed in version 3.13: The *recurse\_symlinks* parameter was added.

    Changed in version 3.13: The *pattern* parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

    Changed in version 3.13: Any [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exceptions raised from scanning the filesystem are
    suppressed. In previous versions, such exceptions are suppressed in many
    cases, but not all.

Path.rglob(*pattern*, *\**, *case\_sensitive=None*, *recurse\_symlinks=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "Link to this definition")
:   Glob the given relative *pattern* recursively. This is like calling
    [`Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") with “`**/`” added in front of the *pattern*.

    Not