---
id: python-callback-example-4-check-arbitrary-condition-https-docs-pyth-f59a6996
type: concept
title: 'Callback example 4: check arbitrary condition[¶](https://docs.python.org/3/library/optparse.html#callback-example-4-check-arbitrary-condition
  "Link to this heading")'
description: Of course, you could put any condition in there—you’re not limited to
  checking
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Callback example 4: check arbitrary condition[¶](https://docs.python.org/3/library/optparse.html#callback-example-4-check-arbitrary-condition "Link to this heading")

Of course, you could put any condition in there—you’re not limited to checking
the values of already-defined options. For example, if you have options that
should not be called when the moon is full, all you have to do is this:

```
def check_moon(option, opt_str, value, parser):
    if is_moon_full():
        raise OptionValueError("%s option invalid when moon is full"
                               % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("--foo",
                  action="callback", callback=check_moon, dest="foo")
```

(The definition of `is_moon_full()` is left as an exercise for the reader.)