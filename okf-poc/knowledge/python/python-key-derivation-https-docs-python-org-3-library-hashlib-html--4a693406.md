---
id: python-key-derivation-https-docs-python-org-3-library-hashlib-html--4a693406
type: concept
title: Key derivation[¶](https://docs.python.org/3/library/hashlib.html#key-derivation
  "Link to this heading")
description: Key derivation and key stretching algorithms are designed for secure
  password
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Key derivation[¶](https://docs.python.org/3/library/hashlib.html#key-derivation "Link to this heading")

Key derivation and key stretching algorithms are designed for secure password
hashing. Naive algorithms such as `sha1(password)` are not resistant against
brute-force attacks. A good password hashing function must be tunable, slow, and
include a [salt](https://en.wikipedia.org/wiki/Salt_%28cryptography%29).

hashlib.pbkdf2\_hmac(*hash\_name*, *password*, *salt*, *iterations*, *dklen=None*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac "Link to this definition")
:   The function provides PKCS#5 password-based key derivation function 2. It
    uses HMAC as pseudorandom function.

    The string *hash\_name* is the desired name of the hash digest algorithm for
    HMAC, e.g. ‘sha1’ or ‘sha256’. *password* and *salt* are interpreted as
    buffers of bytes. Applications and libraries should limit *password* to
    a sensible length (e.g. 1024). *salt* should be about 16 or more bytes from
    a proper source, e.g. [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom").

    The number of *iterations* should be chosen based on the hash algorithm and
    computing power. As of 2022, hundreds of thousands of iterations of SHA-256
    are suggested. For rationale as to why and how to choose what is best for
    your application, read *Appendix A.2.2* of [NIST-SP-800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf). The answers
    on the [stackexchange pbkdf2 iterations question](https://security.stackexchange.com/questions/3959/recommended-of-iterations-when-using-pbkdf2-sha256/) explain in detail.

    *dklen* is the length of the derived key in bytes. If *dklen* is `None` then the
    digest size of the hash algorithm *hash\_name* is used, e.g. 64 for SHA-512.

    ```
    >>> from hashlib import pbkdf2_hmac
    >>> our_app_iters = 500_000  # Application specific, read above.
    >>> dk = pbkdf2_hmac('sha256', b'password', b'bad salt' * 2, our_app_iters)
    >>> dk.hex()
    '15530bba69924174860db778f2c6f8104d3aaf9d26241840c8c4a641c8d000a9'
    ```

    Function only available when Python is compiled with OpenSSL.

    Added in version 3.4.

    Changed in version 3.12: Function now only available when Python is built with OpenSSL. The slow
    pure Python implementation has been removed.

hashlib.scrypt(*password*, *\**, *salt*, *n*, *r*, *p*, *maxmem=0*, *dklen=64*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt "Link to this definition")
:   The function provides scrypt password-based key derivation function as
    defined in [**RFC 7914**](https://datatracker.ietf.org/doc/html/rfc7914.html).

    *password* and *salt* must be [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object). Applications and libraries should limit *password*
    to a sensible length (e.g. 1024). *salt* should be about 16 or more
    bytes from a proper source, e.g. [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom").

    *n* is the CPU/Memory cost factor, *r* the block size, *p* parallelization
    factor and *maxmem* limits memory (OpenSSL 1.1.0 defaults to 32 MiB).
    *dklen* is the length of the derived key in bytes.

    Added in version 3.6.