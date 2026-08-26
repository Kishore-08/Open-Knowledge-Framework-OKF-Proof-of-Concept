---
id: python-path-objects-https-docs-python-org-3-library-zipfile-html-pa-37e106d5
type: concept
title: Path objects[¶](https://docs.python.org/3/library/zipfile.html#path-objects
  "Link to this heading")
description: '*class* zipfile.Path(*root*, *at=''''*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Path objects[¶](https://docs.python.org/3/library/zipfile.html#path-objects "Link to this heading")

*class* zipfile.Path(*root*, *at=''*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path "Link to this definition")
:   Construct a Path object from a `root` zipfile (which may be a
    [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") instance or `file` suitable for passing to
    the `ZipFile` constructor).

    `at` specifies the location of this Path within the zipfile,
    e.g. ‘dir/file.txt’, ‘dir/’, or ‘’. Defaults to the empty string,
    indicating the root.

    Note

    The `Path` class does not sanitize filenames within the ZIP archive. Unlike
    the [`ZipFile.extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract") and [`ZipFile.extractall()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "zipfile.ZipFile.extractall") methods, it is the
    caller’s responsibility to validate or sanitize filenames to prevent path traversal
    vulnerabilities (for example, absolute paths or paths with “..” components). When handling
    untrusted archives, consider resolving filenames using [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath")
    and checking against the target directory with [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath").

Path objects expose the following features of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
objects:

Path objects are traversable using the `/` operator or `joinpath`.

Path.name[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.name "Link to this definition")
:   The final path component.

Path.open(*mode='r'*, *\**, *pwd*, *\*\**)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.open "Link to this definition")
:   Invoke [`ZipFile.open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open") on the current path.
    Allows opening for read or write, text or binary
    through supported modes: ‘r’, ‘w’, ‘rb’, ‘wb’.
    Positional and keyword arguments are passed through to
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") when opened as text and
    ignored otherwise.
    `pwd` is the `pwd` parameter to
    `ZipFile.open()`.

    Changed in version 3.9: Added support for text and binary modes for open. Default
    mode is now text.

    Changed in version 3.11.2: The `encoding` parameter can be supplied as a positional argument
    without causing a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). As it could in 3.9. Code needing to
    be compatible with unpatched 3.10 and 3.11 versions must pass all
    [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") arguments, `encoding` included, as keywords.

Path.iterdir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.iterdir "Link to this definition")
:   Enumerate the children of the current directory.

Path.is\_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_dir "Link to this definition")
:   Return `True` if the current context references a directory.

Path.is\_file()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_file "Link to this definition")
:   Return `True` if the current context references a file.

Path.is\_symlink()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_symlink "Link to this definition")
:   Return `True` if the current context references a symbolic link.

    Added in version 3.12.

    Changed in version 3.13: Previously, `is_symlink` would unconditionally return `False`.

Path.exists()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Pat