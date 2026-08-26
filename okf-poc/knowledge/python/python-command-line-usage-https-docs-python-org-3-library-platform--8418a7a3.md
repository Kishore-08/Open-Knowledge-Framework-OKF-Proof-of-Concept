---
id: python-command-line-usage-https-docs-python-org-3-library-platform--8418a7a3
type: concept
title: Command-line usage[¶](https://docs.python.org/3/library/platform.html#command-line-usage
  "Link to this heading")
description: '`platform` can also be invoked directly using the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-line usage[¶](https://docs.python.org/3/library/platform.html#command-line-usage "Link to this heading")

`platform` can also be invoked directly using the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
switch of the interpreter:

```
python -m platform [--terse] [--nonaliased] [{nonaliased,terse} ...]
```

The following options are accepted:

--terse[¶](https://docs.python.org/3/library/platform.html#cmdoption-platform-terse "Link to this definition")
:   Print terse information about the platform. This is equivalent to
    calling [`platform.platform()`](https://docs.python.org/3/library/platform.html#platform.platform "platform.platform") with the *terse* argument set to `True`.

--nonaliased[¶](https://docs.python.org/3/library/platform.html#cmdoption-platform-nonaliased "Link to this definition")
:   Print platform information without system/OS name aliasing. This is
    equivalent to calling [`platform.platform()`](https://docs.python.org/3/library/platform.html#platform.platform "platform.platform") with the *aliased* argument
    set to `True`.

You can also pass one or more positional arguments (`terse`, `nonaliased`)
to explicitly control the output format. These behave similarly to their
corresponding options.