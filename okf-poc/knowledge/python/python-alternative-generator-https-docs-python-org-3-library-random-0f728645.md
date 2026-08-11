---
id: python-alternative-generator-https-docs-python-org-3-library-random-0f728645
type: concept
title: Alternative Generator[¶](https://docs.python.org/3/library/random.html#alternative-generator
  "Link to this heading")
description: '*class* random.Random([*seed*])[¶](https://docs.python.org/3/library/random.html#random.Random
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Alternative Generator[¶](https://docs.python.org/3/library/random.html#alternative-generator "Link to this heading")

*class* random.Random([*seed*])[¶](https://docs.python.org/3/library/random.html#random.Random "Link to this definition")
:   Class that implements the default pseudo-random number generator used by the
    `random` module.

    Changed in version 3.11: Formerly the *seed* could be any hashable object. Now it is limited to:
    `None`, [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"),
    [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

    Subclasses of `Random` should override the following methods if they
    wish to make use of a different basic generator:

    seed(*a=None*, *version=2*)[¶](https://docs.python.org/3/library/random.html#random.Random.seed "Link to this definition")
    :   Override this method in subclasses to customise the `seed()`
        behaviour of `Random` instances.

    getstate()[¶](https://docs.python.org/3/library/random.html#random.Random.getstate "Link to this definition")
    :   Override this method in subclasses to customise the `getstate()`
        behaviour of `Random` instances.

    setstate(*state*)[¶](https://docs.python.org/3/library/random.html#random.Random.setstate "Link to this definition")
    :   Override this method in subclasses to customise the `setstate()`
        behaviour of `Random` instances.

    random()[¶](https://docs.python.org/3/library/random.html#random.Random.random "Link to this definition")
    :   Override this method in subclasses to customise the `random()`
        behaviour of `Random` instances.

    Optionally, a custom generator subclass can also supply the following method:

    getrandbits(*k*)[¶](https://docs.python.org/3/library/random.html#random.Random.getrandbits "Link to this definition")
    :   Override this method in subclasses to customise the
        `getrandbits()` behaviour of `Random` instances.

    randbytes(*n*)[¶](https://docs.python.org/3/library/random.html#random.Random.randbytes "Link to this definition")
    :   Override this method in subclasses to customise the
        `randbytes()` behaviour of `Random` instances.

*class* random.SystemRandom([*seed*])[¶](https://docs.python.org/3/library/random.html#random.SystemRandom "Link to this definition")
:   Class that uses the [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") function for generating random numbers
    from sources provided by the operating system. Not available on all systems.
    Does not rely on software state, and sequences are not reproducible. Accordingly,
    the [`seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed") method has no effect and is ignored.
    The [`getstate()`](https://docs.python.org/3/library/random.html#random.getstate "random.getstate") and [`setstate()`](https://docs.python.org/3/library/random.html#random.setstate "random.setstate") methods raise
    [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if called.