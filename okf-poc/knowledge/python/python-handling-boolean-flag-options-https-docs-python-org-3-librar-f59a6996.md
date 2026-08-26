---
id: python-handling-boolean-flag-options-https-docs-python-org-3-librar-f59a6996
type: concept
title: Handling boolean (flag) options[¶](https://docs.python.org/3/library/optparse.html#handling-boolean-flag-options
  "Link to this heading")
description: Flag options—set a variable to true or false when a particular option
  is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Handling boolean (flag) options[¶](https://docs.python.org/3/library/optparse.html#handling-boolean-flag-options "Link to this heading")

Flag options—set a variable to true or false when a particular option is
seen—are quite common. `optparse` supports them with two separate actions,
`store_true` and `store_false`. For example, you might have a `verbose`
flag that is turned on with `-v` and off with `-q`:

```
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose")
```

Here we have two different options with the same destination, which is perfectly
OK. (It just means you have to be a bit careful when setting default
values—see below.)

When `optparse` encounters `-v` on the command line, it sets
`options.verbose` to `True`; when it encounters `-q`,
`options.verbose` is set to `False`.