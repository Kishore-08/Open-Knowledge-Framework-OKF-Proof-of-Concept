---
id: python-glob-unix-style-pathname-pattern-expansion-https-docs-python-4ad45192
type: concept
title: '`glob` — Unix style pathname pattern expansion[¶](https://docs.python.org/3/libr'
description: '**Source code:** [Lib/glob.py](https://github.com/python/cpython/tree/3.14/Lib/glob.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/glob.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `glob` — Unix style pathname pattern expansion[¶](https://docs.python.org/3/library/glob.html#module-glob "Link to this heading")

**Source code:** [Lib/glob.py](https://github.com/python/cpython/tree/3.14/Lib/glob.py)

---

The `glob` module finds pathnames
using pattern matching rules similar to the Unix shell.
No tilde expansion is done, but `*`, `?`, and character
ranges expressed with `[]` will be correctly matched. This is done by using
the [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") and [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch") functions in concert, and
not by actually invoking a subshell.

Note

The pathnames are returned in no particular order. If you need a specific
order, sort the results.

By default, files beginning with a dot (`.`) can only be matched by
patterns that also start with a dot,
unlike [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch") or [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob").
For tilde and shell variable expansion, use [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") and
[`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars").

For a literal match, wrap the meta-characters in brackets.
For example, `'[?]'` matches the character `'?'`.

The `glob` module defines the following functions:

glob.glob(*pathname*, *\**, *root\_dir=None*, *dir\_fd=None*, *recursive=False*, *include\_hidden=False*)[¶](https://docs.python.org/3/library/glob.html#glob.glob "Link to this definition")
:   Return a possibly empty list of path names that match *pathname*, which must be
    a string containing a path specification. *pathname* can be either absolute
    (like `/usr/src/Python-1.5/Makefile`) or relative (like
    `../../Tools/*/*.gif`), and can contain shell-style wildcards. Broken
    symlinks are included in the results (as in the shell). Whether or not the
    results are sorted depends on the file system. If a file that satisfies
    conditions is removed or added during the call of this function, whether
    a path name for that file will be included is unspecified.

    If *root\_dir* is not `None`, it should be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
    specifying the root directory for searching. It has the same effect on
    `glob()` as changing the current directory before calling it. If
    *pathname* is relative, the result will contain paths relative to
    *root\_dir*.

    This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) with the *dir\_fd* parameter.

    If *recursive* is true, the pattern “`**`” will match any files and zero or
    more directories, subdirectories and symbolic links to directories. If the
    pattern is followed by an [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep") or [`os.altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep") then files will not
    match.

    If *include\_hidden* is true, wildcards can match path segments that
    begin with a dot (`.`).

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob` with arguments `pathname`, `recursive`.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

    Note

    Using the “`**`” pattern in large directory trees may consume
    an inordinate amount of time.

    Note

    This function may return duplicate path names if *pathname*
    contains multiple “`**`” patterns and *recursive* is true.

    Note

    Any [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSErro