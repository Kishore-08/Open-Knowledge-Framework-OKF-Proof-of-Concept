---
id: python-credits-https-docs-python-org-3-library-hashlib-html-credits-4a693406
type: concept
title: Credits[¶](https://docs.python.org/3/library/hashlib.html#credits "Link to
  this heading")
description: '[BLAKE2](https://www.blake2.net) was designed by *Jean-Philippe Aumasson*,
  *Samuel Neves*, *Zooko'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Credits[¶](https://docs.python.org/3/library/hashlib.html#credits "Link to this heading")

[BLAKE2](https://www.blake2.net) was designed by *Jean-Philippe Aumasson*, *Samuel Neves*, *Zooko
Wilcox-O’Hearn*, and *Christian Winnerlein* based on [SHA-3](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) finalist [BLAKE](https://web.archive.org/web/20200918190133/https://131002.net/blake/)
created by *Jean-Philippe Aumasson*, *Luca Henzen*, *Willi Meier*, and
*Raphael C.-W. Phan*.

It uses core algorithm from [ChaCha](https://cr.yp.to/chacha.html) cipher designed by *Daniel J. Bernstein*.

The stdlib implementation is based on [pyblake2](https://pythonhosted.org/pyblake2/) module. It was written by
*Dmitry Chestnykh* based on C implementation written by *Samuel Neves*. The
documentation was copied from [pyblake2](https://pythonhosted.org/pyblake2/) and written by *Dmitry Chestnykh*.

The C code was partly rewritten for Python by *Christian Heimes*.

The following public domain dedication applies for both C hash function
implementation, extension code, and this documentation:

> To the extent possible under law, the author(s) have dedicated all copyright
> and related and neighboring rights to this software to the public domain
> worldwide. This software is distributed without any warranty.
>
> You should have received a copy of the CC0 Public Domain Dedication along
> with this software. If not, see
> <https://creativecommons.org/publicdomain/zero/1.0/>.

The following people have helped with development or contributed their changes
to the project and the public domain according to the Creative Commons Public
Domain Dedication 1.0 Universal:

- *Alexandr Sokolovskiy*

See also

Module [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication (HMAC) implementation")
:   A module to generate message authentication codes using hashes.

Module [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
:   Another way to encode binary hashes for non-binary environments.

<https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf>
:   The FIPS 180-4 publication on Secure Hash Algorithms.

<https://csrc.nist.gov/pubs/fips/202/final>
:   The FIPS 202 publication on the SHA-3 Standard.

<https://www.blake2.net/>
:   Official BLAKE2 website.

<https://en.wikipedia.org/wiki/Cryptographic_hash_function>
:   Wikipedia article with information on which algorithms have known issues
    and what that means regarding their use.

<https://www.ietf.org/rfc/rfc8018.txt>
:   PKCS #5: Password-Based Cryptography Specification Version 2.1

<https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf>
:   NIST Recommendation for Password-Based Key Derivation.