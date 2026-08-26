---
id: python-action-https-docs-python-org-3-library-argparse-html-action--49b35a18
type: concept
title: action[¶](https://docs.python.org/3/library/argparse.html#action "Link to this
  heading")
description: '[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") objects associate command-line arguments with actions.
  These'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### action[¶](https://docs.python.org/3/library/argparse.html#action "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects associate command-line arguments with actions. These
actions can do just about anything with the command-line arguments associated with
them, though most actions simply add an attribute to the object returned by
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). The `action` keyword argument specifies
how the command-line arguments should be handled. The supplied actions are:

- `'store'` - This just stores the argument’s value. This is the default
  action.
- `'store_const'` - This stores the value specified by the [const](https://docs.python.org/3/library/argparse.html#const) keyword
  argument; note that the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument defaults to `None`. The
  `'store_const'` action is most commonly used with optional arguments that
  specify some sort of flag. For example:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='store_const', const=42)
  >>> parser.parse_args(['--foo'])
  Namespace(foo=42)
  ```
- `'store_true'` and `'store_false'` - These are special cases of
  `'store_const'` that respectively store the values `True` and `False`
  with default values of `False` and
  `True`:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='store_true')
  >>> parser.add_argument('--bar', action='store_false')
  >>> parser.add_argument('--baz', action='store_false')
  >>> parser.parse_args('--foo --bar'.split())
  Namespace(foo=True, bar=False, baz=True)
  ```
- `'append'` - This appends each argument value to a list.
  It is useful for allowing an option to be specified multiple times.
  If the default value is a non-empty list, the parsed value will start
  with the default list’s elements and any values from the command line
  will be appended after those default values. Example usage:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='append', default=['0'])
  >>> parser.parse_args('--foo 1 --foo 2'.split())
  Namespace(foo=['0', '1', '2'])
  ```
- `'append_const'` - This appends the value specified by
  the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument to a list; note that the [const](https://docs.python.org/3/library/argparse.html#const) keyword
  argument defaults to `None`. The `'append_const'` action is typically
  useful when multiple arguments need to store constants to the same list. For
  example:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--str', dest='types', action='append_const', const=str)
  >>> parser.add_argument('--int', dest='types', action='append_const', const=int)
  >>> parser.parse_args('--str --int'.split())
  Namespace(types=[<class 'str'>, <class 'int'>])
  ```
- `'extend'` - This appends each item from a multi-value
  argument to a list.
  The `'extend'` action is typically used with the [nargs](https://docs.python.org/3/library/argparse.html#nargs) keyword argument
  value `'+'` or `'*'`.
  Note that when [nargs](https://docs.python.org/3/library/argparse.html#nargs) is `None` (the default) or `'?'`, each
  character of the argument string will be appended to the list.
  Example usage:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
  >>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
  Namespace(foo=['f1', 'f2', 'f3', 'f4'])
  ```

  Added in version 3.8.
- `'count'` - This counts the number of times an argument occurs. For
  example, this is useful for increasing verbosity levels:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--verbose', '-v',