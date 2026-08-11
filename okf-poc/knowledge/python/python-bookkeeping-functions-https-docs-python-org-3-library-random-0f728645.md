---
id: python-bookkeeping-functions-https-docs-python-org-3-library-random-0f728645
type: concept
title: Bookkeeping functions[¶](https://docs.python.org/3/library/random.html#bookkeeping-functions
  "Link to this heading")
description: random.seed(*a=None*, *version=2*)[¶](https://docs.python.org/3/library/random.html#random.seed
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Bookkeeping functions[¶](https://docs.python.org/3/library/random.html#bookkeeping-functions "Link to this heading")

random.seed(*a=None*, *version=2*)[¶](https://docs.python.org/3/library/random.html#random.seed "Link to this definition")
:   Initialize the random number generator.

    If *a* is omitted or `None`, the current system time is used. If
    randomness sources are provided by the operating system, they are used
    instead of the system time (see the [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") function for details
    on availability).

    If *a* is an int, its absolute value is used directly.

    With version 2 (the default), a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray")
    object gets converted to an [`int`](https://docs.python.org/3/library/functions.html#int "int") and all of its bits are used.

    With version 1 (provided for reproducing random sequences from older versions
    of Python), the algorithm for [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") generates a
    narrower range of seeds.

    Changed in version 3.2: Moved to the version 2 scheme which uses all of the bits in a string seed.

    Changed in version 3.11: The *seed* must be one of the following types:
    `None`, [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

random.getstate()[¶](https://docs.python.org/3/library/random.html#random.getstate "Link to this definition")
:   Return an object capturing the current internal state of the generator. This
    object can be passed to [`setstate()`](https://docs.python.org/3/library/random.html#random.setstate "random.setstate") to restore the state.

random.setstate(*state*)[¶](https://docs.python.org/3/library/random.html#random.setstate "Link to this definition")
:   *state* should have been obtained from a previous call to [`getstate()`](https://docs.python.org/3/library/random.html#random.getstate "random.getstate"), and
    `setstate()` restores the internal state of the generator to what it was at
    the time `getstate()` was called.