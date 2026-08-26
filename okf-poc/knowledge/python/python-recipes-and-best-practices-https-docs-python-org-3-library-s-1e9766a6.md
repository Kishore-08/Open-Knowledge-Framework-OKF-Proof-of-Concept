---
id: python-recipes-and-best-practices-https-docs-python-org-3-library-s-1e9766a6
type: concept
title: Recipes and best practices[¶](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
  "Link to this heading")
description: This section shows recipes and best practices for using `secrets`
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Recipes and best practices[¶](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices "Link to this heading")

This section shows recipes and best practices for using `secrets`
to manage a basic level of security.

Generate an eight-character alphanumeric password:

```
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
```

Note

Applications should not
[**store passwords in a recoverable format**](https://cwe.mitre.org/data/definitions/257.html),
whether plain text or encrypted. They should be salted and hashed
using a cryptographically strong one-way (irreversible) hash function.

Generate a ten-character alphanumeric password with at least one
lowercase character, at least one uppercase character, and at least
three digits:

```
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
```

Generate an [XKCD-style passphrase](https://xkcd.com/936/):

```
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))
```

Generate a hard-to-guess temporary URL containing a security token
suitable for password recovery applications:

```
import secrets
url = 'https://example.com/reset=' + secrets.token_urlsafe()
```