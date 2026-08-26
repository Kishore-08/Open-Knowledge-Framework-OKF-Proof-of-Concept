---
id: python-constructors-https-docs-python-org-3-library-hashlib-html-co-4a693406
type: concept
title: Constructors[¶](https://docs.python.org/3/library/hashlib.html#constructors
  "Link to this heading")
description: hashlib.new(*name*, [*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.new
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constructors[¶](https://docs.python.org/3/library/hashlib.html#constructors "Link to this heading")

hashlib.new(*name*, [*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.new "Link to this definition")
:   Is a generic constructor that takes the string *name* of the desired
    algorithm as its first parameter. It also exists to allow access to the
    above listed hashes as well as any other algorithms that your OpenSSL
    library may offer.

Using [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new") with an algorithm name:

```
>>> h = hashlib.new('sha256')
>>> h.update(b"Nobody inspects the spammish repetition")
>>> h.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
```

hashlib.md5([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "Link to this definition")

hashlib.sha1([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha1 "Link to this definition")

hashlib.sha224([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha224 "Link to this definition")

hashlib.sha256([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "Link to this definition")

hashlib.sha384([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha384 "Link to this definition")

hashlib.sha512([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha512 "Link to this definition")

hashlib.sha3\_224([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_224 "Link to this definition")

hashlib.sha3\_256([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_256 "Link to this definition")

hashlib.sha3\_384([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_384 "Link to this definition")

hashlib.sha3\_512([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_512 "Link to this definition")

Named constructors such as these are faster than passing an algorithm name to
[`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new").