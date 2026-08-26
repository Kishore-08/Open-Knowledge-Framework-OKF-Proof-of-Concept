---
id: python-callback-example-2-check-option-order-https-docs-python-org--f59a6996
type: concept
title: 'Callback example 2: check option order[¶](https://docs.python.org/3/library/optparse.html#callback-example-2-check-option-order
  "Link to this heading")'
description: 'Here’s a slightly more interesting example: record the fact that `-a`
  is'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Callback example 2: check option order[¶](https://docs.python.org/3/library/optparse.html#callback-example-2-check-option-order "Link to this heading")

Here’s a slightly more interesting example: record the fact that `-a` is
seen, but blow up if it comes after `-b` in the command-line.

```
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use -a after -b")
    parser.values.a = 1
...
parser.add_option("-a", action="callback", callback=check_order)
parser.add_option("-b", action="store_true", dest="b")
```