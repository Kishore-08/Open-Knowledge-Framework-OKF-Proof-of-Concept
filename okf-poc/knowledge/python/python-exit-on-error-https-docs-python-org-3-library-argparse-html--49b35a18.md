---
id: python-exit-on-error-https-docs-python-org-3-library-argparse-html--49b35a18
type: concept
title: exit\_on\_error[¶](https://docs.python.org/3/library/argparse.html#exit-on-error
  "Link to this heading")
description: Normally, when you pass an invalid argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "argparse.ArgumentParser.parse_args")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### exit\_on\_error[¶](https://docs.python.org/3/library/argparse.html#exit-on-error "Link to this heading")

Normally, when you pass an invalid argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"), it will print a *message* to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and exit with a status
code of 2.

If the user would like to catch errors manually, the feature can be enabled by setting
`exit_on_error` to `False`:

```
>>> parser = argparse.ArgumentParser(exit_on_error=False)
>>> parser.add_argument('--integers', type=int)
_StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
>>> try:
...     parser.parse_args('--integers a'.split())
... except argparse.ArgumentError:
...     print('Catching an argumentError')
...
Catching an argumentError
```

Added in version 3.9.