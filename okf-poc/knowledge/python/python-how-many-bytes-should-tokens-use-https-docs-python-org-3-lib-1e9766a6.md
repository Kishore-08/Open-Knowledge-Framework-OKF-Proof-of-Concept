---
id: python-how-many-bytes-should-tokens-use-https-docs-python-org-3-lib-1e9766a6
type: concept
title: How many bytes should tokens use?[¶](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use
  "Link to this heading")
description: To be secure against
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How many bytes should tokens use?[¶](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use "Link to this heading")

To be secure against
[brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack),
tokens need to have sufficient randomness. Unfortunately, what is
considered sufficient will necessarily increase as computers get more
powerful and able to make more guesses in a shorter period. As of 2015,
it is believed that 32 bytes (256 bits) of randomness is sufficient for
the typical use-case expected for the `secrets` module.

For those who want to manage their own token length, you can explicitly
specify how much randomness is used for tokens by giving an [`int`](https://docs.python.org/3/library/functions.html#int "int")
argument to the various `token_*` functions. That argument is taken
as the number of bytes of randomness to use.

Otherwise, if no argument is provided, or if the argument is `None`,
the `token_*` functions use [`DEFAULT_ENTROPY`](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY") instead.

secrets.DEFAULT\_ENTROPY[¶](https://docs.python.org/3/library/secrets.html#secrets.DEFAULT_ENTROPY "Link to this definition")
:   Default number of bytes of randomness used by the `token_*` functions.

    The exact value is subject to change at any time, including during
    maintenance releases.