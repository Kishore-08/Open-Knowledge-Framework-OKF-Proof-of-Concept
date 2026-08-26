---
id: python-command-line-usage-https-docs-python-org-3-library-random-ht-0f728645
type: concept
title: Command-line usage[¶](https://docs.python.org/3/library/random.html#command-line-usage
  "Link to this heading")
description: Added in version 3.13.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-line usage[¶](https://docs.python.org/3/library/random.html#command-line-usage "Link to this heading")

Added in version 3.13.

The `random` module can be executed from the command line.

```
python -m random [-h] [-c CHOICE [CHOICE ...] | -i N | -f N] [input ...]
```

The following options are accepted:

-h, --help[¶](https://docs.python.org/3/library/random.html#cmdoption-random-h "Link to this definition")
:   Show the help message and exit.

-c CHOICE [CHOICE ...][¶](https://docs.python.org/3/library/random.html#cmdoption-random-c "Link to this definition")

--choice CHOICE [CHOICE ...][¶](https://docs.python.org/3/library/random.html#cmdoption-random-choice "Link to this definition")
:   Print a random choice, using [`choice()`](https://docs.python.org/3/library/random.html#random.choice "random.choice").

-i <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-i "Link to this definition")

--integer <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-integer "Link to this definition")
:   Print a random integer between 1 and N inclusive, using [`randint()`](https://docs.python.org/3/library/random.html#random.randint "random.randint").

-f <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-f "Link to this definition")

--float <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-float "Link to this definition")
:   Print a random floating-point number between 0 and N inclusive,
    using [`uniform()`](https://docs.python.org/3/library/random.html#random.uniform "random.uniform").

If no options are given, the output depends on the input:

- String or multiple: same as [`--choice`](https://docs.python.org/3/library/random.html#cmdoption-random-choice).
- Integer: same as [`--integer`](https://docs.python.org/3/library/random.html#cmdoption-random-integer).
- Float: same as [`--float`](https://docs.python.org/3/library/random.html#cmdoption-random-float).