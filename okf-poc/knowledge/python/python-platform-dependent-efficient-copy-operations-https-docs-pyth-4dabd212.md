---
id: python-platform-dependent-efficient-copy-operations-https-docs-pyth-4dabd212
type: concept
title: Platform-dependent efficient copy operations[¶](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations
  "Link to this heading")
description: Starting from Python 3.8, all functions involving a file copy
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Platform-dependent efficient copy operations[¶](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations "Link to this heading")

Starting from Python 3.8, all functions involving a file copy
([`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile"), [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"), [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"),
[`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), and [`move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move")) may use
platform-specific “fast-copy” syscalls in order to copy the file more
efficiently (see [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671)).
“fast-copy” means that the copying operation occurs within the kernel, avoiding
the use of userspace buffers in Python as in “`outfd.write(infd.read())`”.

On macOS [fcopyfile](http://www.manpagez.com/man/3/copyfile/) is used to copy the file content (not metadata).

On Linux [`os.copy_file_range()`](https://docs.python.org/3/library/os.html#os.copy_file_range "os.copy_file_range") or [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") is used.

On Solaris [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") is used.

On Windows [`shutil.copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") uses a bigger default buffer size (1 MiB
instead of 64 KiB) and a [`memoryview()`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview")-based variant of
[`shutil.copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj") is used.

If the fast-copy operation fails and no data was written in the destination
file then shutil will silently fall back to less efficient
[`copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj") function internally.

Changed in version 3.8.

Changed in version 3.14: Solaris now uses [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile").

Changed in version 3.14: Copy-on-write or server-side copy may be used internally via
[`os.copy_file_range()`](https://docs.python.org/3/library/os.html#os.copy_file_range "os.copy_file_range") on supported Linux filesystems.