---
id: python-examples-https-docs-python-org-3-library-glob-html-examples--4ad45192
type: concept
title: Examples[¶](https://docs.python.org/3/library/glob.html#examples "Link to this
  heading")
description: 'Consider a directory containing the following files:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/glob.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples[¶](https://docs.python.org/3/library/glob.html#examples "Link to this heading")

Consider a directory containing the following files:
`1.gif`, `2.txt`, `card.gif` and a subdirectory `sub`
which contains only the file `3.txt`. [`glob()`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") will produce
the following results. Notice how any leading components of the path are
preserved.

```
>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']
```

If the directory contains files starting with `.` they won’t be matched by
default. For example, consider a directory containing `card.gif` and
`.card.gif`:

```
>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']
```

See also

The [`fnmatch`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching.") module offers shell-style filename (not path) expansion.

See also

The [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths") module offers high-level path objects.