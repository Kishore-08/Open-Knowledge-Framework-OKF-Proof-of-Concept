---
id: python-default-values-https-docs-python-org-3-library-optparse-html-f59a6996
type: concept
title: Default values[¶](https://docs.python.org/3/library/optparse.html#default-values
  "Link to this heading")
description: All of the above examples involve setting some variable (the “destination”)
  when
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Default values[¶](https://docs.python.org/3/library/optparse.html#default-values "Link to this heading")

All of the above examples involve setting some variable (the “destination”) when
certain command-line options are seen. What happens if those options are never
seen? Since we didn’t supply any defaults, they are all set to `None`. This
is usually fine, but sometimes you want more control. `optparse` lets you
supply a default value for each destination, which is assigned before the
command line is parsed.

First, consider the verbose/quiet example. If we want `optparse` to set
`verbose` to `True` unless `-q` is seen, then we can do this:

```
parser.add_option("-v", action="store_true", dest="verbose", default=True)
parser.add_option("-q", action="store_false", dest="verbose")
```

Since default values apply to the *destination* rather than to any particular
option, and these two options happen to have the same destination, this is
exactly equivalent:

```
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose", default=True)
```

Consider this:

```
parser.add_option("-v", action="store_true", dest="verbose", default=False)
parser.add_option("-q", action="store_false", dest="verbose", default=True)
```

Again, the default value for `verbose` will be `True`: the last default
value supplied for any particular destination is the one that counts.

A clearer way to specify default values is the `set_defaults()` method of
OptionParser, which you can call at any time before calling
[`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"):

```
parser.set_defaults(verbose=True)
parser.add_option(...)
(options, args) = parser.parse_args()
```

As before, the last value specified for a given option destination is the one
that counts. For clarity, try to use one method or the other of setting default
values, not both.