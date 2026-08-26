---
id: python-hmac-keyed-hashing-for-message-authentication-https-docs-pyt-7a54556e
type: concept
title: '`hmac` — Keyed-Hashing for Message Authentication[¶](https://docs.python.org/3/l'
description: '**Source code:** [Lib/hmac.py](https://github.com/python/cpython/tree/3.14/Lib/hmac.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hmac.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `hmac` — Keyed-Hashing for Message Authentication[¶](https://docs.python.org/3/library/hmac.html#module-hmac "Link to this heading")

**Source code:** [Lib/hmac.py](https://github.com/python/cpython/tree/3.14/Lib/hmac.py)

---

This module implements the HMAC algorithm as described by [**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html).
The interface allows to use any hash function with a *fixed* digest size.
In particular, extendable output functions such as SHAKE-128 or SHAKE-256
cannot be used with HMAC.

hmac.new(*key*, *msg=None*, *digestmod*)[¶](https://docs.python.org/3/library/hmac.html#hmac.new "Link to this definition")
:   Return a new hmac object. *key* is a bytes or bytearray object giving the
    secret key. If *msg* is present, the method call `update(msg)` is made.
    *digestmod* is the digest name, digest constructor or module for the HMAC
    object to use. It may be any name suitable to [`hashlib.new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new").
    Despite its argument position, it is required.

    Changed in version 3.4: Parameter *key* can be a bytes or bytearray object.
    Parameter *msg* can be of any type supported by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.").
    Parameter *digestmod* can be the name of a hash algorithm.

    Changed in version 3.8: The *digestmod* argument is now required. Pass it as a keyword
    argument to avoid awkwardness when you do not have an initial *msg*.

hmac.digest(*key*, *msg*, *digest*)[¶](https://docs.python.org/3/library/hmac.html#hmac.digest "Link to this definition")
:   Return digest of *msg* for given secret *key* and *digest*. The
    function is equivalent to `HMAC(key, msg, digest).digest()`, but
    uses an optimized C or inline implementation, which is faster for messages
    that fit into memory. The parameters *key*, *msg*, and *digest* have
    the same meaning as in [`new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new").

    CPython implementation detail, the optimized C implementation is only used
    when *digest* is a string and name of a digest algorithm, which is
    supported by OpenSSL.

    Added in version 3.7.

*class* hmac.HMAC[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC "Link to this definition")
:   An HMAC object has the following methods:

HMAC.update(*msg*)[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.update "Link to this definition")
:   Update the hmac object with *msg*. Repeated calls are equivalent to a
    single call with the concatenation of all the arguments:
    `m.update(a); m.update(b)` is equivalent to `m.update(a + b)`.

    Changed in version 3.4: Parameter *msg* can be of any type supported by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.").

HMAC.digest()[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.digest "Link to this definition")
:   Return the digest of the bytes passed to the [`update()`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.update "hmac.HMAC.update") method so far.
    This bytes object will be the same length as the *digest\_size* of the digest
    given to the constructor. It may contain non-ASCII bytes, including NUL
    bytes.

    Warning

    When comparing the output of `digest()` to an externally supplied
    digest during a verification routine, it is recommended to use the
    [`compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest") function instead of the `==` operator
    to reduce the vulnerability to timing attacks.

HMAC.hexdigest()[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.hexdigest "Link to this definition")
:   Like [`digest()`](https://docs.python.org/3/library/hmac.html#hmac.digest "hmac.digest") except the digest is returned as a string twic