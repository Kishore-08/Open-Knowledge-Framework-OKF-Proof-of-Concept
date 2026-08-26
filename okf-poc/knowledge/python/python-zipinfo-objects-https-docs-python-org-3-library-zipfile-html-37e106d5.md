---
id: python-zipinfo-objects-https-docs-python-org-3-library-zipfile-html-37e106d5
type: concept
title: ZipInfo objects[¶](https://docs.python.org/3/library/zipfile.html#zipinfo-objects
  "Link to this heading")
description: Instances of the [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo
  "zipfile.ZipInfo") class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zi
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## ZipInfo objects[¶](https://docs.python.org/3/library/zipfile.html#zipinfo-objects "Link to this heading")

Instances of the [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo") and
[`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist") methods of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") objects. Each object stores
information about a single member of the ZIP archive.

There is one classmethod to make a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance for a filesystem
file:

*classmethod* ZipInfo.from\_file(*filename*, *arcname=None*, *\**, *strict\_timestamps=True*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.from_file "Link to this definition")
:   Construct a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance for a file on the filesystem, in
    preparation for adding it to a zip file.

    *filename* should be the path to a file or directory on the filesystem.

    If *arcname* is specified, it is used as the name within the archive.
    If *arcname* is not specified, the name will be the same as *filename*, but
    with any drive letter and leading path separators removed.

    The *strict\_timestamps* argument, when set to `False`, allows to
    zip files older than 1980-01-01 at the cost of setting the
    timestamp to 1980-01-01.
    Similar behavior occurs with files newer than 2107-12-31,
    the timestamp is also set to the limit.

    Added in version 3.6.

    Changed in version 3.6.2: The *filename* parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

    Changed in version 3.8: Added the *strict\_timestamps* keyword-only parameter.

Instances have the following methods and attributes:

ZipInfo.is\_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.is_dir "Link to this definition")
:   Return `True` if this archive member is a directory.

    This uses the entry’s name: directories should always end with `/`.

    Added in version 3.6.

ZipInfo.filename[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.filename "Link to this definition")
:   Name of the file in the archive.

ZipInfo.date\_time[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.date_time "Link to this definition")
:   The time and date of the last modification to the archive member. This is a
    tuple of six values representing the “last [modified] file time” and “last [modified] file date”
    fields from the ZIP file’s central directory.

    The tuple contains:

    | Index | Value |
    | --- | --- |
    | `0` | Year (>= 1980) |
    | `1` | Month (one-based) |
    | `2` | Day of month (one-based) |
    | `3` | Hours (zero-based) |
    | `4` | Minutes (zero-based) |
    | `5` | Seconds (zero-based) |

    Note

    The ZIP format supports multiple timestamp fields in different locations
    (central directory, extra fields for NTFS/UNIX systems, etc.). This attribute
    specifically returns the timestamp from the central directory. The central
    directory timestamp format in ZIP files does not support timestamps before
    1980. While some extra field formats (such as UNIX timestamps) can represent
    earlier dates, this attribute only returns the central directory timestamp.

    The central directory timestamp is interpreted as representing local
    time, rather than UTC time, to match the behavior of other zip tools.

ZipInfo.compress\_type[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.compress_type "Link to this definition")
:   Type of compression for the archive member.

ZipInfo.comment[¶](https://