---
id: python-default-named-filters-https-docs-python-org-3-library-tarfil-47076c99
type: concept
title: Default named filters[¶](https://docs.python.org/3/library/tarfile.html#default-named-filters
  "Link to this heading")
description: The pre-defined, named filters are available as functions, so they can
  be
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Default named filters[¶](https://docs.python.org/3/library/tarfile.html#default-named-filters "Link to this heading")

The pre-defined, named filters are available as functions, so they can be
reused in custom filters:

tarfile.fully\_trusted\_filter(*member*, *path*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "Link to this definition")
:   Return *member* unchanged.

    This implements the `'fully_trusted'` filter.

tarfile.tar\_filter(*member*, *path*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "Link to this definition")
:   Implements the `'tar'` filter.

    - Strip leading slashes (`/` and [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep")) from filenames.
    - [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract files with absolute
      paths (in case the name is absolute
      even after stripping slashes, e.g. `C:/foo` on Windows).
      This raises [`AbsolutePathError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsolutePathError "tarfile.AbsolutePathError").
    - Normalize filenames ([`TarInfo.name`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "tarfile.TarInfo.name")) that contain `..` components
      using [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath").
      Note that this removes internal `..` components, which may change the
      meaning of the name if it traverses symbolic links.
    - [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract files whose absolute
      path (after following symlinks) would end up outside the destination.
      This raises [`OutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "tarfile.OutsideDestinationError").
    - Clear high mode bits (setuid, setgid, sticky) and group/other write bits
      ([`S_IWGRP`](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "stat.S_IWGRP") | [`S_IWOTH`](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "stat.S_IWOTH")).

    Return the modified `TarInfo` member.

    Changed in version 3.14.7 (unreleased): Filenames containing `..` components are now normalized.

tarfile.data\_filter(*member*, *path*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "Link to this definition")
:   Implements the `'data'` filter.
    In addition to what `tar_filter` does:

    - Normalize link targets ([`TarInfo.linkname`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.linkname "tarfile.TarInfo.linkname")) using
      [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath").
      Note that this removes internal `..` components, which may change the
      meaning of the link if the path in `TarInfo.linkname` traverses
      symbolic links.
    - [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract links (hard or soft)
      that link to absolute paths, or ones that link outside the destination.

      This raises [`AbsoluteLinkError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsoluteLinkError "tarfile.AbsoluteLinkError") or
      [`LinkOutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.LinkOutsideDestinationError "tarfile.LinkOutsideDestinationError").

      Note that such files are refused even on platforms that do not support
      symbolic links.
    - [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract device files
      (including pipes).
      This raises [`SpecialFileError`](https://docs.python.org/3/library/tarfile.html#tarfile.SpecialFileError "tarfile.SpecialFileError").
    - For regular files, including hard links:

      - Set the owner read and write permissions
        ([`S_IRUSR`](https://docs.python.org/3/library/