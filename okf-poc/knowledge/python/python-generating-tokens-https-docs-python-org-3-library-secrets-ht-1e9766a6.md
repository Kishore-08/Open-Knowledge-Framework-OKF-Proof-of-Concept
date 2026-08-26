---
id: python-generating-tokens-https-docs-python-org-3-library-secrets-ht-1e9766a6
type: concept
title: Generating tokens[¶](https://docs.python.org/3/library/secrets.html#generating-tokens
  "Link to this heading")
description: The `secrets` module provides functions for generating secure
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Generating tokens[¶](https://docs.python.org/3/library/secrets.html#generating-tokens "Link to this heading")

The `secrets` module provides functions for generating secure
tokens, suitable for applications such as password resets,
hard-to-guess URLs, and similar.

secrets.token\_bytes(*nbytes=None*)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_bytes "Link to this definition")
:   Return a random byte string containing *nbytes* number of bytes.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_bytes(16)
    b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'
    ```

secrets.token\_hex(*nbytes=None*)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_hex "Link to this definition")
:   Return a random text string, in hexadecimal. The string has *nbytes*
    random bytes, each byte converted to two hex digits.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_hex(16)
    'f9bf78b9a18ce6d46a0cd2b0b86df9da'
    ```

secrets.token\_urlsafe(*nbytes=None*)[¶](https://docs.python.org/3/library/secrets.html#secrets.token_urlsafe "Link to this definition")
:   Return a random URL-safe text string, containing *nbytes* random
    bytes. The text is Base64 encoded, so on average each byte results
    in approximately 1.3 characters.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_urlsafe(16)
    'Drmhze6EPcv0fN_81Bj-nA'
    ```