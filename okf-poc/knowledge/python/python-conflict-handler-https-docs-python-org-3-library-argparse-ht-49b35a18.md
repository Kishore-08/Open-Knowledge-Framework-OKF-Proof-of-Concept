---
id: python-conflict-handler-https-docs-python-org-3-library-argparse-ht-49b35a18
type: concept
title: conflict\_handler[¶](https://docs.python.org/3/library/argparse.html#conflict-handler
  "Link to this heading")
description: '[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") objects do not allow two actions with the same option'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### conflict\_handler[¶](https://docs.python.org/3/library/argparse.html#conflict-handler "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects do not allow two actions with the same option
string. By default, `ArgumentParser` objects raise an exception if an
attempt is made to create an argument with an option string that is already in
use:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```

Sometimes (e.g. when using [parents](https://docs.python.org/3/library/argparse.html#parents)) it may be useful to simply override any
older arguments with the same option string. To get this behavior, the value
`'resolve'` can be supplied to the `conflict_handler=` argument of
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):

```
>>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
>>> parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

options:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
```

Note that [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects only remove an action if all of its
option strings are overridden. So, in the example above, the old `-f/--foo`
action is retained as the `-f` action, because only the `--foo` option
string was overridden.