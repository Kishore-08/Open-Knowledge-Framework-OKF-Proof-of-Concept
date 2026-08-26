---
id: python-command-line-interface-https-docs-python-org-3-library-zipfi-37e106d5
type: concept
title: Command-line interface[¶](https://docs.python.org/3/library/zipfile.html#command-line-interface
  "Link to this heading")
description: The `zipfile` module provides a simple command-line interface to interact
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-line interface[¶](https://docs.python.org/3/library/zipfile.html#command-line-interface "Link to this heading")

The `zipfile` module provides a simple command-line interface to interact
with ZIP archives.

If you want to create a new ZIP archive, specify its name after the [`-c`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c)
option and then list the filename(s) that should be included:

```
$ python -m zipfile -c monty.zip spam.txt eggs.txt
```

Passing a directory is also acceptable:

```
$ python -m zipfile -c monty.zip life-of-brian_1979/
```

If you want to extract a ZIP archive into the specified directory, use
the [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e) option:

```
$ python -m zipfile -e monty.zip target-dir/
```

For a list of the files in a ZIP archive, use the [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l) option:

```
$ python -m zipfile -l monty.zip
```