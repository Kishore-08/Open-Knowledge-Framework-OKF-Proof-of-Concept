---
id: python-beyond-sys-argv-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: Beyond `sys.argv`[¶](https://docs.python.org/3/library/argparse.html#beyond-sys-argv
  "Link to this heading")
description: Sometimes it may be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") parse arguments other than those
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Beyond `sys.argv`[¶](https://docs.python.org/3/library/argparse.html#beyond-sys-argv "Link to this heading")

Sometimes it may be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") parse arguments other than those
of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv"). This can be accomplished by passing a list of strings to
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). This is useful for testing at the
interactive prompt:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument(
...     'integers', metavar='int', type=int, choices=range(10),
...     nargs='+', help='an integer in the range 0..9')
>>> parser.add_argument(
...     '--sum', dest='accumulate', action='store_const', const=sum,
...     default=max, help='sum the integers (default: find the max)')
>>> parser.parse_args(['1', '2', '3', '4'])
Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
>>> parser.parse_args(['1', '2', '3', '4', '--sum'])
Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])
```