---
id: python-argument-default-https-docs-python-org-3-library-argparse-ht-49b35a18
type: concept
title: argument\_default[¶](https://docs.python.org/3/library/argparse.html#argument-default
  "Link to this heading")
description: Generally, argument defaults are specified either by passing a default
  to
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### argument\_default[¶](https://docs.python.org/3/library/argparse.html#argument-default "Link to this heading")

Generally, argument defaults are specified either by passing a default to
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") or by calling the
[`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults") methods with a specific set of name-value
pairs. Sometimes however, it may be useful to specify a single parser-wide
default for arguments. This can be accomplished by passing the
`argument_default=` keyword argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). For example,
to globally suppress attribute creation on [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
calls, we supply `argument_default=SUPPRESS`:

```
>>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar', nargs='?')
>>> parser.parse_args(['--foo', '1', 'BAR'])
Namespace(bar='BAR', foo='1')
>>> parser.parse_args([])
Namespace()
```