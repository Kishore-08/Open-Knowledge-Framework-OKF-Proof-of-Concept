---
id: python-recommended-configuration-https-docs-python-org-3-library-st-5e0bc1d7
type: concept
title: Recommended configuration[¶](https://docs.python.org/3/library/stdtypes.html#recommended-configuration
  "Link to this heading")
description: The default [`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits
  "sys.int_info.default_max_str_digits") is expected to be
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Recommended configuration[¶](https://docs.python.org/3/library/stdtypes.html#recommended-configuration "Link to this heading")

The default [`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits") is expected to be
reasonable for most applications. If your application requires a different
limit, set it from your main entry point using Python version agnostic code as
these APIs were added in security patch releases in versions before 3.12.

Example:

```
>>> import sys
>>> if hasattr(sys, "set_int_max_str_digits"):
...     upper_bound = 68000
...     lower_bound = 4004
...     current_limit = sys.get_int_max_str_digits()
...     if current_limit == 0 or current_limit > upper_bound:
...         sys.set_int_max_str_digits(upper_bound)
...     elif current_limit < lower_bound:
...         sys.set_int_max_str_digits(lower_bound)
```

If you need to disable it entirely, set it to `0`.

Footnotes