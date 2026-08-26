---
id: python-default-https-docs-python-org-3-library-argparse-html-defaul-49b35a18
type: concept
title: default[¶](https://docs.python.org/3/library/argparse.html#default "Link to
  this heading")
description: All optional arguments and some positional arguments may be omitted at
  the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### default[¶](https://docs.python.org/3/library/argparse.html#default "Link to this heading")

All optional arguments and some positional arguments may be omitted at the
command line. The `default` keyword argument of
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), whose value defaults to `None`,
specifies what value should be used if the command-line argument is not present.
For optional arguments, the `default` value is used when the option string
was not present at the command line:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args(['--foo', '2'])
Namespace(foo='2')
>>> parser.parse_args([])
Namespace(foo=42)
```

If the target namespace already has an attribute set, the action *default*
will not overwrite it:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args([], namespace=argparse.Namespace(foo=101))
Namespace(foo=101)
```

If the `default` value is a string, the parser parses the value as if it
were a command-line argument. In particular, the parser applies any [type](https://docs.python.org/3/library/argparse.html#type)
conversion argument, if provided, before setting the attribute on the
[`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") return value. Otherwise, the parser uses the value as is:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--length', default='10', type=int)
>>> parser.add_argument('--width', default=10.5, type=int)
>>> parser.parse_args()
Namespace(length=10, width=10.5)
```

For positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs) equal to `?` or `*`, the `default` value
is used when no command-line argument was present:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', nargs='?', default=42)
>>> parser.parse_args(['a'])
Namespace(foo='a')
>>> parser.parse_args([])
Namespace(foo=42)
```

Because `nargs='*'` gathers any supplied values into a list, an absent
positional argument yields an empty list (`[]`). Only a non-`None`
*default* overrides this (so `default=None` still gives `[]`).

For [required](https://docs.python.org/3/library/argparse.html#required) arguments, the `default` value is ignored. For example, this
applies to positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs) values other than `?` or `*`,
or optional arguments marked as `required=True`.

Providing `default=argparse.SUPPRESS` causes no attribute to be added if the
command-line argument was not present:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=argparse.SUPPRESS)
>>> parser.parse_args([])
Namespace()
>>> parser.parse_args(['--foo', '1'])
Namespace(foo='1')
```