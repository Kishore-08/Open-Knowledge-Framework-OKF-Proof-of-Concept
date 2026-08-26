---
id: python-dest-https-docs-python-org-3-library-argparse-html-dest-link-49b35a18
type: concept
title: dest[¶](https://docs.python.org/3/library/argparse.html#dest "Link to this
  heading")
description: Most [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") actions add some value as an attribute of the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### dest[¶](https://docs.python.org/3/library/argparse.html#dest "Link to this heading")

Most [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") actions add some value as an attribute of the
object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). The name of this
attribute is determined by the `dest` keyword argument of
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). For positional argument actions,
`dest` is normally supplied as the first argument to
`add_argument()`:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('bar')
>>> parser.parse_args(['XXX'])
Namespace(bar='XXX')
```

For optional argument actions, the value of `dest` is normally inferred from
the option strings. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") generates the value of `dest` by
taking the first long option string and stripping away the initial `--`
string. If no long option strings were supplied, `dest` will be derived from
the first short option string by stripping the initial `-` character. Any
internal `-` characters will be converted to `_` characters to make sure
the string is a valid attribute name. The examples below illustrate this
behavior:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-f', '--foo-bar', '--foo')
>>> parser.add_argument('-x', '-y')
>>> parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')
```

`dest` allows a custom attribute name to be provided:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
```

Multiple arguments may share the same `dest`. By default, the value from the
last such argument given on the command line wins. Use `action='append'` to
collect values from all of them into a list instead. For conflicting *option
strings* rather than `dest` names, see [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler).