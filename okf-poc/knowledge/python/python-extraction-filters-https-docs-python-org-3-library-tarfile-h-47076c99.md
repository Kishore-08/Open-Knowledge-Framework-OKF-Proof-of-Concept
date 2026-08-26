---
id: python-extraction-filters-https-docs-python-org-3-library-tarfile-h-47076c99
type: concept
title: Extraction filters[¶](https://docs.python.org/3/library/tarfile.html#extraction-filters
  "Link to this heading")
description: Added in version 3.12.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Extraction filters[¶](https://docs.python.org/3/library/tarfile.html#extraction-filters "Link to this heading")

Added in version 3.12.

The *tar* format is designed to capture all details of a UNIX-like filesystem,
which makes it very powerful.
Unfortunately, the features make it easy to create tar files that have
unintended – and possibly malicious – effects when extracted.
For example, extracting a tar file can overwrite arbitrary files in various
ways (e.g. by using absolute paths, `..` path components, or symlinks that
affect later members).

In most cases, the full functionality is not needed.
Therefore, *tarfile* supports extraction filters: a mechanism to limit
functionality, and thus mitigate some of the security issues.

Warning

None of the available filters blocks *all* dangerous archive features.
Never extract archives from untrusted sources without prior inspection.
See also [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification).

See also

[**PEP 706**](https://peps.python.org/pep-0706/)
:   Contains further motivation and rationale behind the design.

The *filter* argument to [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
can be:

- the string `'fully_trusted'`: Honor all metadata as specified in the
  archive.
  Should be used if the user trusts the archive completely, or implements
  their own complex verification.
- the string `'tar'`: Honor most *tar*-specific features (i.e. features of
  UNIX-like filesystems), but block features that are very likely to be
  surprising or malicious. See [`tar_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "tarfile.tar_filter") for details.
- the string `'data'`: Ignore or block most features specific to UNIX-like
  filesystems. Intended for extracting cross-platform data archives.
  See [`data_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter") for details.
- `None` (default): Use [`TarFile.extraction_filter`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extraction_filter "tarfile.TarFile.extraction_filter").

  If that is also `None` (the default), the `'data'` filter will be used.

  > Changed in version 3.14: The default filter is set to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter").
  > Previously, the default was equivalent to
  > [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").
- A callable which will be called for each extracted member with a
  [TarInfo](https://docs.python.org/3/library/tarfile.html#tarinfo-objects) describing the member and the destination
  path to where the archive is extracted (i.e. the same path is used for all
  members):

  ```
  filter(member: TarInfo, path: str, /) -> TarInfo | None
  ```

  The callable is called just before each member is extracted, so it can
  take the current state of the disk into account.
  It can:

  - return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object which will be used instead of the metadata
    in the archive, or
  - return `None`, in which case the member will be skipped, or
  - raise an exception to abort the operation or skip the member,
    depending on [`errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel").
    Note that when extraction is aborted, [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") may leave
    the archive partially extracted. It does not attempt to clean up.