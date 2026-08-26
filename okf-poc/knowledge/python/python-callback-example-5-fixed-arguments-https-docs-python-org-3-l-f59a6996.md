---
id: python-callback-example-5-fixed-arguments-https-docs-python-org-3-l-f59a6996
type: concept
title: 'Callback example 5: fixed arguments[¶](https://docs.python.org/3/library/optparse.html#callback-example-5-fixed-arguments
  "Link to this heading")'
description: Things get slightly more interesting when you define callback options
  that take
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Callback example 5: fixed arguments[¶](https://docs.python.org/3/library/optparse.html#callback-example-5-fixed-arguments "Link to this heading")

Things get slightly more interesting when you define callback options that take
a fixed number of arguments. Specifying that a callback option takes arguments
is similar to defining a `"store"` or `"append"` option: if you define
[`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), then the option takes one argument that must be
convertible to that type; if you further define [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), then the
option takes `nargs` arguments.

Here’s an example that just emulates the standard `"store"` action:

```
def store_value(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value)
...
parser.add_option("--foo",
                  action="callback", callback=store_value,
                  type="int", nargs=3, dest="foo")
```

Note that `optparse` takes care of consuming 3 arguments and converting
them to integers for you; all you have to do is store them. (Or whatever;
obviously you don’t need a callback for this example.)