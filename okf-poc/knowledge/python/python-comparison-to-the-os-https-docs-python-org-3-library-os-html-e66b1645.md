---
id: python-comparison-to-the-os-https-docs-python-org-3-library-os-html-e66b1645
type: concept
title: 'Comparison to the [`os`](https://docs.python.org/3/library/os.html#module-os
  "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path
  "os.path: Operations on pathnames.") modules[¶](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules
  "Link to this heading")'
description: pathlib implements path operations using [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath
  "pathlib.PurePath") and [`Path`](https://docs.python.org/3/library/pathlib.html#pa
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Comparison to the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules[¶](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules "Link to this heading")

pathlib implements path operations using [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") and [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
objects, and so it’s said to be *object-oriented*. On the other hand, the
[`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules supply functions that work with low-level
`str` and `bytes` objects, which is a more *procedural* approach. Some
users consider the object-oriented style to be more readable.

Many functions in [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") support `bytes` paths and
[paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd). These features aren’t
available in pathlib.

Python’s `str` and `bytes` types, and portions of the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and
[`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules, are written in C and are very speedy. pathlib is
written in pure Python and is often slower, but rarely slow enough to matter.

pathlib’s path normalization is slightly more opinionated and consistent than
[`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames."). For example, whereas [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") eliminates
“`..`” segments from a path, which may change its meaning if symlinks are
involved, [`Path.absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "pathlib.Path.absolute") preserves these segments for greater safety.

pathlib’s path normalization may render it unsuitable for some applications:

1. pathlib normalizes `Path("my_folder/")` to `Path("my_folder")`, which
   changes a path’s meaning when supplied to various operating system APIs and
   command-line utilities. Specifically, the absence of a trailing separator
   may allow the path to be resolved as either a file or directory, rather
   than a directory only.
2. pathlib normalizes `Path("./my_program")` to `Path("my_program")`,
   which changes a path’s meaning when used as an executable search path, such
   as in a shell or when spawning a child process. Specifically, the absence
   of a separator in the path may force it to be looked up in `PATH`
   rather than the current directory.

As a consequence of these differences, pathlib is not a drop-in replacement
for [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").