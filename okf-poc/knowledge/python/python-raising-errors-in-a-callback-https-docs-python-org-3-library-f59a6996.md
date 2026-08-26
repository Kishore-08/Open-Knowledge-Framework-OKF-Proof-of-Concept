---
id: python-raising-errors-in-a-callback-https-docs-python-org-3-library-f59a6996
type: concept
title: Raising errors in a callback[¶](https://docs.python.org/3/library/optparse.html#raising-errors-in-a-callback
  "Link to this heading")
description: The callback function should raise [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError
  "optparse.OptionValueError") if there are any
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Raising errors in a callback[¶](https://docs.python.org/3/library/optparse.html#raising-errors-in-a-callback "Link to this heading")

The callback function should raise [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if there are any
problems with the option or its argument(s). `optparse` catches this and
terminates the program, printing the error message you supply to stderr. Your
message should be clear, concise, accurate, and mention the option at fault.
Otherwise, the user will have a hard time figuring out what they did wrong.