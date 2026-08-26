---
id: python-hints-for-further-verification-https-docs-python-org-3-libra-47076c99
type: concept
title: Hints for further verification[¶](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification
  "Link to this heading")
description: Even with `filter='data'`, *tarfile* is not suited for extracting untrusted
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Hints for further verification[¶](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification "Link to this heading")

Even with `filter='data'`, *tarfile* is not suited for extracting untrusted
files without prior inspection.
Among other issues, the pre-defined filters do not prevent denial-of-service
attacks. Users should do additional checks.

Here is an incomplete list of things to consider:

- Extract to a [`new temporary directory`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
  to prevent e.g. exploiting pre-existing links, and to make it easier to
  clean up after a failed extraction.
- Disallow symbolic links if you do not need the functionality.
- When working with untrusted data, use external (e.g. OS-level) limits on
  disk, memory and CPU usage.
- Check filenames against an allow-list of characters
  (to filter out control characters, confusables, foreign path separators,
  and so on).
- Check that filenames have expected extensions (discouraging files that
  execute when you “click on them”, or extension-less files like Windows
  special device names).
- Limit the number of extracted files, total size of extracted data,
  filename length (including symlink length), and size of individual files.
- Check for files that would be shadowed on case-insensitive filesystems.

Also note that:

- Tar files may contain multiple versions of the same file.
  Later ones are expected to overwrite any earlier ones.
  This feature is crucial to allow updating tape archives, but can be abused
  maliciously.
- *tarfile* does not protect against issues with “live” data,
  e.g. an attacker tinkering with the destination (or source) directory while
  extraction (or archiving) is in progress.