---
id: python-tarinfo-objects-https-docs-python-org-3-library-tarfile-html-47076c99
type: concept
title: TarInfo Objects[¶](https://docs.python.org/3/library/tarfile.html#tarinfo-objects
  "Link to this heading")
description: A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo
  "tarfile.TarInfo") object represents one member in a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.Tar
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## TarInfo Objects[¶](https://docs.python.org/3/library/tarfile.html#tarinfo-objects "Link to this heading")

A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object represents one member in a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile"). Aside
from storing all required attributes of a file (like file type, size, time,
permissions, owner etc.), it provides some useful methods to determine its type.
It does *not* contain the file’s data itself.

[`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") objects are returned by [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")’s methods
[`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember"), [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") and
[`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo").

Modifying the objects returned by [`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember") or
[`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") will affect all subsequent
operations on the archive.
For cases where this is unwanted, you can use [`copy.copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") or
call the [`replace()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.replace "tarfile.TarInfo.replace") method to create a modified copy in one step.

Several attributes can be set to `None` to indicate that a piece of metadata
is unused or unknown.
Different [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") methods handle `None` differently:

- The [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") methods will
  ignore the corresponding metadata, leaving it set to a default.
- [`addfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "tarfile.TarFile.addfile") will fail.
- [`list()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "tarfile.TarFile.list") will print a placeholder string.

*class* tarfile.TarInfo(*name=''*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "Link to this definition")
:   Create a `TarInfo` object.

*classmethod* TarInfo.frombuf(*buf*, *encoding*, *errors*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.frombuf "Link to this definition")
:   Create and return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object from string buffer *buf*.

    Raises [`HeaderError`](https://docs.python.org/3/library/tarfile.html#tarfile.HeaderError "tarfile.HeaderError") if the buffer is invalid.

*classmethod* TarInfo.fromtarfile(*tarfile*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.fromtarfile "Link to this definition")
:   Read the next member from the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object *tarfile* and return it as
    a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object.

TarInfo.tobuf(*format=DEFAULT\_FORMAT*, *encoding=ENCODING*, *errors='surrogateescape'*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.tobuf "Link to this definition")
:   Create a string buffer from a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object. For information on