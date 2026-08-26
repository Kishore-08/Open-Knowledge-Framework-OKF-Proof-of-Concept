---
id: python-command-line-interface-https-docs-python-org-3-library-tarfi-47076c99
type: concept
title: Command-Line Interface[¶](https://docs.python.org/3/library/tarfile.html#command-line-interface
  "Link to this heading")
description: Added in version 3.4.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-Line Interface[¶](https://docs.python.org/3/library/tarfile.html#command-line-interface "Link to this heading")

Added in version 3.4.

The `tarfile` module provides a simple command-line interface to interact
with tar archives.

If you want to create a new tar archive, specify its name after the [`-c`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c)
option and then list the filename(s) that should be included:

```
$ python -m tarfile -c monty.tar  spam.txt eggs.txt
```

Passing a directory is also acceptable:

```
$ python -m tarfile -c monty.tar life-of-brian_1979/
```

If you want to extract a tar archive into the current directory, use
the [`-e`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e) option:

```
$ python -m tarfile -e monty.tar
```

You can also extract a tar archive into a different directory by passing the
directory’s name:

```
$ python -m tarfile -e monty.tar  other-dir/
```

For a list of the files in a tar archive, use the [`-l`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l) option:

```
$ python -m tarfile -l monty.tar
```