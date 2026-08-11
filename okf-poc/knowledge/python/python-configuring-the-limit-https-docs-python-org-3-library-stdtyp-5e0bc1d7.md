---
id: python-configuring-the-limit-https-docs-python-org-3-library-stdtyp-5e0bc1d7
type: concept
title: Configuring the limit[¶](https://docs.python.org/3/library/stdtypes.html#configuring-the-limit
  "Link to this heading")
description: Before Python starts up you can use an environment variable or an interpreter
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Configuring the limit[¶](https://docs.python.org/3/library/stdtypes.html#configuring-the-limit "Link to this heading")

Before Python starts up you can use an environment variable or an interpreter
command line flag to configure the limit:

- [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), e.g.
  `PYTHONINTMAXSTRDIGITS=640 python3` to set the limit to 640 or
  `PYTHONINTMAXSTRDIGITS=0 python3` to disable the limitation.
- [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X), e.g.
  `python3 -X int_max_str_digits=640`
- [`sys.flags.int_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.flags.int_max_str_digits "sys.flags.int_max_str_digits") contains the value of
  [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) or [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X).
  If both the env var and the `-X` option are set, the `-X` option takes
  precedence. A value of *-1* indicates that both were unset, thus a value of
  [`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits") was used during initialization.

From code, you can inspect the current limit and set a new one using these
[`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") APIs:

- [`sys.get_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits") and [`sys.set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits") are
  a getter and setter for the interpreter-wide limit. Subinterpreters have
  their own limit.

Information about the default and minimum can be found in [`sys.int_info`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info"):

- [`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info") is the compiled-in
  default limit.
- [`sys.int_info.str_digits_check_threshold`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info") is the lowest
  accepted value for the limit (other than 0 which disables it).

Added in version 3.11.

Caution

Setting a low limit *can* lead to problems. While rare, code exists that
contains integer constants in decimal in their source that exceed the
minimum threshold. A consequence of setting the limit is that Python source
code containing decimal integer literals longer than the limit will
encounter an error during parsing, usually at startup time or import time or
even at installation time - anytime an up to date `.pyc` does not already
exist for the code. A workaround for source that contains such large
constants is to convert them to `0x` hexadecimal form as it has no limit.

Test your application thoroughly if you use a low limit. Ensure your tests
run with the limit set early via the environment or flag so that it applies
during startup and even during any installation step that may invoke Python
to precompile `.py` sources to `.pyc` files.