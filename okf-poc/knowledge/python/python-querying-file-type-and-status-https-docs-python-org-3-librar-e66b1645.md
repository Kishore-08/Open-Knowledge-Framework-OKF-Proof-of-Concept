---
id: python-querying-file-type-and-status-https-docs-python-org-3-librar-e66b1645
type: concept
title: Querying file type and status[¶](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status
  "Link to this heading")
description: 'Changed in version 3.8: [`exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists
  "pathlib.Path.exists"), [`is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Querying file type and status[¶](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status "Link to this heading")

Changed in version 3.8: [`exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "pathlib.Path.exists"), [`is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir"), [`is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file"),
[`is_mount()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_mount "pathlib.Path.is_mount"), [`is_symlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink "pathlib.Path.is_symlink"),
[`is_block_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_block_device "pathlib.Path.is_block_device"), [`is_char_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_char_device "pathlib.Path.is_char_device"),
[`is_fifo()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_fifo "pathlib.Path.is_fifo"), [`is_socket()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_socket "pathlib.Path.is_socket") now return `False`
instead of raising an exception for paths that contain characters
unrepresentable at the OS level.

Changed in version 3.14: The methods given above now return `False` instead of raising any
[`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception from the operating system. In previous versions,
some kinds of `OSError` exception are raised, and others suppressed.
The new behaviour is consistent with [`os.path.exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists "os.path.exists"),
[`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir"), etc. Use [`stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to retrieve the file
status without suppressing exceptions.

Path.stat(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "Link to this definition")
:   Return an [`os.stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object containing information about this path, like [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat").
    The result is looked up at each call to this method.

    This method normally follows symlinks; to stat a symlink add the argument
    `follow_symlinks=False`, or use [`lstat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "pathlib.Path.lstat").

    ```
    >>> p = Path('setup.py')
    >>> p.stat().st_size
    956
    >>> p.stat().st_mtime
    1327883547.852554
    ```

    Changed in version 3.10: The *follow\_symlinks* parameter was added.

Path.lstat()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "Link to this definition")
:   Like [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") but, if the path points to a symbolic link, return
    the symbolic link’s information rather than its target’s.

Path.exists(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "Link to this definition")
:   Return `True` if the path points to an existing file or directory.
    `False` will be returned if the path is invalid, inaccessible or missing.
    Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

    This method normally follows symlinks; to check if a symlink exists, add
    the argument `follow_symlinks=False`.

    ```
    >>> Path('.').exists()
    True
    >>> Path('setup.py').exists()
    True
    >>> Path('/etc').exists()
    True
    >>> Path('nonexistentfile').exists()
    False
    ```

    Changed in version 3.12: The *follow\_symlinks* parameter was added