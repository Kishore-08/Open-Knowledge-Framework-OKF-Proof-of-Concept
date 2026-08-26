---
id: python-copying-moving-and-deleting-https-docs-python-org-3-library--e66b1645
type: concept
title: Copying, moving and deleting[¶](https://docs.python.org/3/library/pathlib.html#copying-moving-and-deleting
  "Link to this heading")
description: Path.copy(*target*, *\**, *follow\_symlinks=True*, *preserve\_metadata=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Copying, moving and deleting[¶](https://docs.python.org/3/library/pathlib.html#copying-moving-and-deleting "Link to this heading")

Path.copy(*target*, *\**, *follow\_symlinks=True*, *preserve\_metadata=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy "Link to this definition")
:   Copy this file or directory tree to the given *target*, and return a new
    `Path` instance pointing to *target*.

    If the source is a file, the target will be replaced if it is an existing
    file. If the source is a symlink and *follow\_symlinks* is true (the
    default), the symlink’s target is copied. Otherwise, the symlink is
    recreated at the destination.

    If *preserve\_metadata* is false (the default), only directory structures
    and file data are guaranteed to be copied. Set *preserve\_metadata* to true
    to ensure that file and directory permissions, flags, last access and
    modification times, and extended attributes are copied where supported.
    This argument has no effect when copying files on Windows (where
    metadata is always preserved).

    Note

    Where supported by the operating system and file system, this method
    performs a lightweight copy, where data blocks are only copied when
    modified. This is known as copy-on-write.

    Added in version 3.14.

Path.copy\_into(*target\_dir*, *\**, *follow\_symlinks=True*, *preserve\_metadata=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy_into "Link to this definition")
:   Copy this file or directory tree into the given *target\_dir*, which should
    be an existing directory. Other arguments are handled identically to
    [`Path.copy()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.copy "pathlib.Path.copy"). Returns a new `Path` instance pointing to the
    copy.

    Added in version 3.14.

Path.rename(*target*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename "Link to this definition")
:   Rename this file or directory to the given *target*, and return a new
    `Path` instance pointing to *target*. On Unix, if *target* exists
    and is a file, it will be replaced silently if the user has permission.
    On Windows, if *target* exists, [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised.
    *target* can be either a string or another path object:

    ```
    >>> p = Path('foo')
    >>> p.open('w').write('some text')
    9
    >>> target = Path('bar')
    >>> p.rename(target)
    PosixPath('bar')
    >>> target.open().read()
    'some text'
    ```

    The target path may be absolute or relative. Relative paths are interpreted
    relative to the current working directory, *not* the directory of the
    `Path` object.

    It is implemented in terms of [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") and gives the same guarantees.

    Changed in version 3.8: Added return value, return the new `Path` instance.

Path.replace(*target*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace "Link to this definition")
:   Rename this file or directory to the given *target*, and return a new
    `Path` instance pointing to *target*. If *target* points to an
    existing file or empty directory, it will be unconditionally replaced.

    The target path may be absolute or relative. Relative paths are interpreted
    relative to the current working directory, *not* the directory of the
    `Path` object.

    Changed in version 3.8: Added return value, return the new `Path` instance.

Path.move(*target*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.move "Link to this definition")
:   Move this file or directory tree to the given *target*, and return a new
    `Path` instance pointing to *target*.

    If the *target* doesn’t exist it will be created. If both this path and the
    *target* are existing files, then the target is overwritt