---
id: python-command-line-interface-https-docs-python-org-3-library-sqlit-d14c7d1a
type: concept
title: Command-line interface[¶](https://docs.python.org/3/library/sqlite3.html#command-line-interface
  "Link to this heading")
description: The `sqlite3` module can be invoked as a script,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Command-line interface[¶](https://docs.python.org/3/library/sqlite3.html#command-line-interface "Link to this heading")

The `sqlite3` module can be invoked as a script,
using the interpreter’s [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) switch,
in order to provide a simple SQLite shell.
The argument signature is as follows:

```
python -m sqlite3 [-h] [-v] [filename] [sql]
```

Type `.quit` or CTRL-D to exit the shell.

-h, --help[¶](https://docs.python.org/3/library/sqlite3.html#cmdoption-python-m-sqlite3-h-v-filename-sql-h "Link to this definition")
:   Print CLI help.

-v, --version[¶](https://docs.python.org/3/library/sqlite3.html#cmdoption-python-m-sqlite3-h-v-filename-sql-v "Link to this definition")
:   Print underlying SQLite library version.

Added in version 3.12.

## How-to guides[¶](https://docs.python.org/3/library/sqlite3.html#how-to-guides "Link to this heading")