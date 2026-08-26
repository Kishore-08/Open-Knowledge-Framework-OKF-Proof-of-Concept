---
id: python-creating-files-and-directories-https-docs-python-org-3-libra-e66b1645
type: concept
title: Creating files and directories[¶](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories
  "Link to this heading")
description: Path.touch(*mode=0o666*, *exist\_ok=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.touch
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Creating files and directories[¶](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories "Link to this heading")

Path.touch(*mode=0o666*, *exist\_ok=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.touch "Link to this definition")
:   Create a file at this given path. If *mode* is given, it is combined
    with the process’s `umask` value to determine the file mode and access
    flags. If the file already exists, the function succeeds when *exist\_ok*
    is true (and its modification time is updated to the current time),
    otherwise [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is raised.

    See also

    The [`open()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "pathlib.Path.open"), [`write_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text "pathlib.Path.write_text") and
    [`write_bytes()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "pathlib.Path.write_bytes") methods are often used to create files.

Path.mkdir(*mode=0o777*, *parents=False*, *exist\_ok=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir "Link to this definition")
:   Create a new directory at this given path. If *mode* is given, it is
    combined with the process’s `umask` value to determine the file mode
    and access flags. If the path already exists, [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError")
    is raised.

    If *parents* is true, any missing parents of this path are created
    as needed; they are created with the default permissions without taking
    *mode* into account (mimicking the POSIX `mkdir -p` command).

    If *parents* is false (the default), a missing parent raises
    [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError").

    If *exist\_ok* is false (the default), [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is
    raised if the target directory already exists.

    If *exist\_ok* is true, [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will not be raised unless the given
    path already exists in the file system and is not a directory (same
    behavior as the POSIX `mkdir -p` command).

    Changed in version 3.5: The *exist\_ok* parameter was added.

Path.symlink\_to(*target*, *target\_is\_directory=False*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to "Link to this definition")
:   Make this path a symbolic link pointing to *target*.

    On Windows, a symlink represents either a file or a directory, and does not
    morph to the target dynamically. If the target is present, the type of the
    symlink will be created to match. Otherwise, the symlink will be created
    as a directory if *target\_is\_directory* is true or a file symlink (the
    default) otherwise. On non-Windows platforms, *target\_is\_directory* is ignored.

    ```
    >>> p = Path('mylink')
    >>> p.symlink_to('setup.py')
    >>> p.resolve()
    PosixPath('/home/antoine/pathlib/setup.py')
    >>> p.stat().st_size
    956
    >>> p.lstat().st_size
    8
    ```

    Note

    The order of arguments (link, target) is the reverse
    of [`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink")’s.

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") if [`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink") is not
    available. In previous versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised.

Path.hardlink\_to(*target*)[¶](https://doc