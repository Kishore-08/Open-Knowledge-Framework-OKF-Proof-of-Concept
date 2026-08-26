---
id: python-color-https-docs-python-org-3-library-argparse-html-color-li-49b35a18
type: concept
title: color[¶](https://docs.python.org/3/library/argparse.html#color "Link to this
  heading")
description: By default, the help message is printed in color using [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code).
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### color[¶](https://docs.python.org/3/library/argparse.html#color "Link to this heading")

By default, the help message is printed in color using [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code).
If you want plain text help messages, you can disable this [in your local
environment](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color), or in the argument parser itself
by setting `color` to `False`:

```
>>> parser = argparse.ArgumentParser(description='Process some integers.',
...                                  color=False)
>>> parser.add_argument('--action', choices=['sum', 'max'])
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.parse_args(['--help'])
```

Note that when `color=True`, colored output depends on both environment
variables and terminal capabilities. However, if `color=False`, colored
output is always disabled, even if environment variables like `FORCE_COLOR`
are set.

Note

Error messages will include color codes when redirecting stderr to a
file. To avoid this, set the [`NO_COLOR`](https://no-color.org/) or [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS)
environment variable (for example,
`NO_COLOR=1 python script.py 2> errors.txt`).

Added in version 3.14.