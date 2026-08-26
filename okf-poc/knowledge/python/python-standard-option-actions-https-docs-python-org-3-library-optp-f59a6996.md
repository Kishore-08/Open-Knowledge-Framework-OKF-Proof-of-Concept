---
id: python-standard-option-actions-https-docs-python-org-3-library-optp-f59a6996
type: concept
title: Standard option actions[¶](https://docs.python.org/3/library/optparse.html#standard-option-actions
  "Link to this heading")
description: The various option actions all have slightly different requirements and
  effects.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Standard option actions[¶](https://docs.python.org/3/library/optparse.html#standard-option-actions "Link to this heading")

The various option actions all have slightly different requirements and effects.
Most actions have several relevant option attributes which you may specify to
guide `optparse`’s behaviour; a few have required attributes, which you
must specify for any option using that action.

- `"store"` [relevant: [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"),
  [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices")]

  The option must be followed by an argument, which is converted to a value
  according to [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and stored in [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"). If
  [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") > 1, multiple arguments will be consumed from the
  command line; all will be converted according to `type` and
  stored to `dest` as a tuple. See the
  [Standard option types](https://docs.python.org/3/library/optparse.html#optparse-standard-option-types) section.

  If [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices") is supplied (a list or tuple of strings), the type
  defaults to `"choice"`.

  If [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") is not supplied, it defaults to `"string"`.

  If [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") is not supplied, `optparse` derives a destination
  from the first long option string (e.g., `--foo-bar` implies
  `foo_bar`). If there are no long option strings, `optparse` derives a
  destination from the first short option string (e.g., `-f` implies `f`).

  Example:

  ```
  parser.add_option("-f")
  parser.add_option("-p", type="float", nargs=3, dest="point")
  ```

  As it parses the command line

  ```
  -f foo.txt -p 1 -3.5 4 -fbar.txt
  ```

  `optparse` will set

  ```
  options.f = "foo.txt"
  options.point = (1.0, -3.5, 4.0)
  options.f = "bar.txt"
  ```
- `"store_const"` [required: [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const"); relevant:
  [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]

  The value [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const") is stored in [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").

  Example:

  ```
  parser.add_option("-q", "--quiet",
                    action="store_const", const=0, dest="verbose")
  parser.add_option("-v", "--verbose",
                    action="store_const", const=1, dest="verbose")
  parser.add_option("--noisy",
                    action="store_const", const=2, dest="verbose")
  ```

  If `--noisy` is seen, `optparse` will set

  ```
  options.verbose = 2
  ```
- `"store_true"` [relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]

  A special case of `"store_const"` that stores `True` to
  [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").
- `"store_false"` [relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]

  Like `"store_true"`, but stores `False`.

  Example:

  ```
  parser.add_option("--clobber", action="s