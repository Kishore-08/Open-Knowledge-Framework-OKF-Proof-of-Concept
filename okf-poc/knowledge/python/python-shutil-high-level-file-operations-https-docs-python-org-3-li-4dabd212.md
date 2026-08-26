---
id: python-shutil-high-level-file-operations-https-docs-python-org-3-li-4dabd212
type: concept
title: '`shutil` — High-level file operations[¶](https://docs.python.org/3/library/shuti'
description: '**Source code:** [Lib/shutil.py](https://github.com/python/cpython/tree/3.14/Lib/shutil.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `shutil` — High-level file operations[¶](https://docs.python.org/3/library/shutil.html#module-shutil "Link to this heading")

**Source code:** [Lib/shutil.py](https://github.com/python/cpython/tree/3.14/Lib/shutil.py)

---

The `shutil` module offers a number of high-level operations on files and
collections of files. In particular, functions are provided which support file
copying and removal. For operations on individual files, see also the
[`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module.

Warning

Even the higher-level file copying functions ([`shutil.copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"),
[`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2")) cannot copy all file metadata.

On POSIX platforms, this means that file owner and group are lost as well
as ACLs. On Mac OS, the resource fork and other metadata are not used.
This means that resources will be lost and file type and creator codes will
not be correct. On Windows, file owners, ACLs and alternate data streams
are not copied.