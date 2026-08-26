---
id: python-prog-https-docs-python-org-3-library-argparse-html-prog-link-49b35a18
type: concept
title: prog[¶](https://docs.python.org/3/library/argparse.html#prog "Link to this
  heading")
description: By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") calculates the name of the program
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### prog[¶](https://docs.python.org/3/library/argparse.html#prog "Link to this heading")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") calculates the name of the program
to display in help messages depending on the way the Python interpreter was run:

- The [`base name`](https://docs.python.org/3/library/os.path.html#os.path.basename "os.path.basename") of `sys.argv[0]` if a file was
  passed as argument.
- The Python interpreter name followed by `sys.argv[0]` if a directory or
  a zipfile was passed as argument.
- The Python interpreter name followed by `-m` followed by the
  module or package name if the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) option was used.

This default is almost always desirable because it will make the help messages
match the string that was used to invoke the program on the command line.
However, to change this default behavior, another value can be supplied using
the `prog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):

```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.print_help()
usage: myprogram [-h]

options:
 -h, --help  show this help message and exit
```

Note that the program name, whether determined from `sys.argv[0]`,
from the `__main__` module attributes or from the
`prog=` argument, is available to help messages using the `%(prog)s` format
specifier.

```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.add_argument('--foo', help='foo of the %(prog)s program')
>>> parser.print_help()
usage: myprogram [-h] [--foo FOO]

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
```

Changed in version 3.14: The default `prog` value now reflects how `__main__` was actually executed,
rather than always being `os.path.basename(sys.argv[0])`.