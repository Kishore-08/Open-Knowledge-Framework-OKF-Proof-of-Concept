---
id: python-deprecated-https-docs-python-org-3-library-argparse-html-dep-49b35a18
type: concept
title: deprecated[¶](https://docs.python.org/3/library/argparse.html#deprecated "Link
  to this heading")
description: During a project’s lifetime, some arguments may need to be removed from
  the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### deprecated[¶](https://docs.python.org/3/library/argparse.html#deprecated "Link to this heading")

During a project’s lifetime, some arguments may need to be removed from the
command line. Before removing them, you should inform
your users that the arguments are deprecated and will be removed.
The `deprecated` keyword argument of
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), which defaults to `False`,
specifies if the argument is deprecated and will be removed
in the future.
For arguments, if `deprecated` is `True`, then a warning will be
printed to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") when the argument is used:

```
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='snake.py')
>>> parser.add_argument('--legs', default=0, type=int, deprecated=True)
>>> parser.parse_args([])
Namespace(legs=0)
>>> parser.parse_args(['--legs', '4'])
snake.py: warning: option '--legs' is deprecated
Namespace(legs=4)
```

Added in version 3.13.