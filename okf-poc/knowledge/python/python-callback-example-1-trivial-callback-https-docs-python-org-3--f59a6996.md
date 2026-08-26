---
id: python-callback-example-1-trivial-callback-https-docs-python-org-3--f59a6996
type: concept
title: 'Callback example 1: trivial callback[¶](https://docs.python.org/3/library/optparse.html#callback-example-1-trivial-callback
  "Link to this heading")'
description: Here’s an example of a callback option that takes no arguments, and simply
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Callback example 1: trivial callback[¶](https://docs.python.org/3/library/optparse.html#callback-example-1-trivial-callback "Link to this heading")

Here’s an example of a callback option that takes no arguments, and simply
records that the option was seen:

```
def record_foo_seen(option, opt_str, value, parser):
    parser.values.saw_foo = True

parser.add_option("--foo", action="callback", callback=record_foo_seen)
```

Of course, you could do that with the `"store_true"` action.