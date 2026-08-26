---
id: python-callback-example-3-check-option-order-generalized-https-docs-f59a6996
type: concept
title: 'Callback example 3: check option order (generalized)[¶](https://docs.python.org/3/library/optparse.html#callback-example-3-check-option-order-generalized
  "Link to this heading")'
description: If you want to reuse this callback for several similar options (set a
  flag, but
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Callback example 3: check option order (generalized)[¶](https://docs.python.org/3/library/optparse.html#callback-example-3-check-option-order-generalized "Link to this heading")

If you want to reuse this callback for several similar options (set a flag, but
blow up if `-b` has already been seen), it needs a bit of work: the error
message and the flag that it sets must be generalized.

```
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use %s after -b" % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("-a", action="callback", callback=check_order, dest='a')
parser.add_option("-b", action="store_true", dest="b")
parser.add_option("-c", action="callback", callback=check_order, dest='c')
```