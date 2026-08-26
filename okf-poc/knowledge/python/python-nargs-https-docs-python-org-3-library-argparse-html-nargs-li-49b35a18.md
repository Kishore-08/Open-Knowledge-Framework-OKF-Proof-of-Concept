---
id: python-nargs-https-docs-python-org-3-library-argparse-html-nargs-li-49b35a18
type: concept
title: nargs[¶](https://docs.python.org/3/library/argparse.html#nargs "Link to this
  heading")
description: '[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") objects usually associate a single command-line argument
  with a'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### nargs[¶](https://docs.python.org/3/library/argparse.html#nargs "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects usually associate a single command-line argument with a
single action to be taken. The `nargs` keyword argument associates a
different number of command-line arguments with a single action.
See also [Specifying ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments). The supported values are:

- `N` (an integer). `N` arguments from the command line will be gathered
  together into a list. For example:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs=2)
  >>> parser.add_argument('bar', nargs=1)
  >>> parser.parse_args('c --foo a b'.split())
  Namespace(bar=['c'], foo=['a', 'b'])
  ```

  Note that `nargs=1` produces a list of one item. This is different from
  the default, in which the item is produced by itself.

- `'?'`. One argument will be consumed from the command line if possible, and
  produced as a single item. If no command-line argument is present, the value from
  [default](https://docs.python.org/3/library/argparse.html#default) will be produced. Note that for optional arguments, there is an
  additional case - the option string is present but not followed by a
  command-line argument. In this case the value from [const](https://docs.python.org/3/library/argparse.html#const) will be produced. Some
  examples to illustrate this:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs='?', const='c', default='d')
  >>> parser.add_argument('bar', nargs='?', default='d')
  >>> parser.parse_args(['XX', '--foo', 'YY'])
  Namespace(bar='XX', foo='YY')
  >>> parser.parse_args(['XX', '--foo'])
  Namespace(bar='XX', foo='c')
  >>> parser.parse_args([])
  Namespace(bar='d', foo='d')
  ```

  One of the more common uses of `nargs='?'` is to allow optional input and
  output files:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('infile', nargs='?')
  >>> parser.add_argument('outfile', nargs='?')
  >>> parser.parse_args(['input.txt', 'output.txt'])
  Namespace(infile='input.txt', outfile='output.txt')
  >>> parser.parse_args(['input.txt'])
  Namespace(infile='input.txt', outfile=None)
  >>> parser.parse_args([])
  Namespace(infile=None, outfile=None)
  ```

- `'*'`. All command-line arguments present are gathered into a list. Note that
  it generally doesn’t make much sense to have more than one positional argument
  with `nargs='*'`, but multiple optional arguments with `nargs='*'` is
  possible. For example:

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs='*')
  >>> parser.add_argument('--bar', nargs='*')
  >>> parser.add_argument('baz', nargs='*')
  >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
  Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
  ```

- `'+'`. Just like `'*'`, all command-line arguments present are gathered into a
  list. Additionally, an error message will be generated if there wasn’t at
  least one command-line argument present. For example:

  ```
  >>> parser = argparse.ArgumentParser(prog='PROG')
  >>> parser.add_argument('foo', nargs='+')
  >>> parser.parse_args(['a', 'b'])
  Namespace(foo=['a', 'b'])
  >>> parser.parse_args([])
  usage: PROG [-h] foo [foo ...]
  PROG: error: the following arguments are required: foo
  ```

If the `nargs` keyword argument is not provided, the number of arguments consumed
is determined by the [action](https://docs.python.org/3/library/argparse.html#action). Generally this means a single command-line argument
will be consumed and a single item (not a list) will be produced.
Actions that do not consume command-line arguments (e.g.
`'store_const'`) set `nargs=0`.