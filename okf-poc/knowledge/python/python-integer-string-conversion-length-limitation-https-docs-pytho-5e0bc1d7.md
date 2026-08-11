---
id: python-integer-string-conversion-length-limitation-https-docs-pytho-5e0bc1d7
type: concept
title: Integer string conversion length limitation[¶](https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation
  "Link to this heading")
description: CPython has a global limit for converting between [`int`](https://docs.python.org/3/library/functions.html#int
  "int") and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Integer string conversion length limitation[¶](https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation "Link to this heading")

CPython has a global limit for converting between [`int`](https://docs.python.org/3/library/functions.html#int "int") and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")
to mitigate denial of service attacks. This limit *only* applies to decimal or
other non-power-of-two number bases. Hexadecimal, octal, and binary conversions
are unlimited. The limit can be configured.

The [`int`](https://docs.python.org/3/library/functions.html#int "int") type in CPython is an arbitrary length number stored in binary
form (commonly known as a “bignum”). There exists no algorithm that can convert
a string to a binary integer or a binary integer to a string in linear time,
*unless* the base is a power of 2. Even the best known algorithms for base 10
have sub-quadratic complexity. Converting a large value such as `int('1' *
500_000)` can take over a second on a fast CPU.

Limiting conversion size offers a practical way to avoid [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735).

The limit is applied to the number of digit characters in the input or output
string when a non-linear conversion algorithm would be involved. Underscores
and the sign are not counted towards the limit.

When an operation would exceed the limit, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:

```
>>> import sys
>>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
>>> _ = int('2' * 5432)
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
>>> i = int('2' * 4300)
>>> len(str(i))
4300
>>> i_squared = i*i
>>> len(str(i_squared))
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> len(hex(i_squared))
7144
>>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.
```

The default limit is 4300 digits as provided in
[`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info").
The lowest limit that can be configured is 640 digits as provided in
`sys.int_info.str_digits_check_threshold`.

Verification:

```
>>> import sys
>>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
>>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
>>> msg = int('578966293710682886880994035146873798396722250538762761564'
...           '9252925514383915483333812743580549779436104706260696366600'
...           '571186405732').to_bytes(53, 'big')
...
```

Added in version 3.11.