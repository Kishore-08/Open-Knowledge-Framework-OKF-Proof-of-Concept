---
id: python-creating-hash-objects-https-docs-python-org-3-library-hashli-4a693406
type: concept
title: Creating hash objects[¶](https://docs.python.org/3/library/hashlib.html#creating-hash-objects
  "Link to this heading")
description: 'New hash objects are created by calling constructor functions:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Creating hash objects[¶](https://docs.python.org/3/library/hashlib.html#creating-hash-objects "Link to this heading")

New hash objects are created by calling constructor functions:

hashlib.blake2b(*data=b''*, *\**, *digest\_size=64*, *key=b''*, *salt=b''*, *person=b''*, *fanout=1*, *depth=1*, *leaf\_size=0*, *node\_offset=0*, *node\_depth=0*, *inner\_size=0*, *last\_node=False*, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.blake2b "Link to this definition")

hashlib.blake2s(*data=b''*, *\**, *digest\_size=32*, *key=b''*, *salt=b''*, *person=b''*, *fanout=1*, *depth=1*, *leaf\_size=0*, *node\_offset=0*, *node\_depth=0*, *inner\_size=0*, *last\_node=False*, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.blake2s "Link to this definition")

These functions return the corresponding hash objects for calculating
BLAKE2b or BLAKE2s. They optionally take these general parameters:

- *data*: initial chunk of data to hash, which must be
  [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object). It can be passed only as positional argument.
- *digest\_size*: size of output digest in bytes.
- *key*: key for keyed hashing (up to 64 bytes for BLAKE2b, up to 32 bytes for
  BLAKE2s).
- *salt*: salt for randomized hashing (up to 16 bytes for BLAKE2b, up to 8
  bytes for BLAKE2s).
- *person*: personalization string (up to 16 bytes for BLAKE2b, up to 8 bytes
  for BLAKE2s).

The following table shows limits for general parameters (in bytes):

| Hash | digest\_size | len(key) | len(salt) | len(person) |
| --- | --- | --- | --- | --- |
| BLAKE2b | 64 | 64 | 16 | 16 |
| BLAKE2s | 32 | 32 | 8 | 8 |

Note

BLAKE2 specification defines constant lengths for salt and personalization
parameters, however, for convenience, this implementation accepts byte
strings of any size up to the specified length. If the length of the
parameter is less than specified, it is padded with zeros, thus, for
example, `b'salt'` and `b'salt\x00'` is the same value. (This is not
the case for *key*.)

These sizes are available as module [constants](https://docs.python.org/3/library/hashlib.html#constants) described below.

Constructor functions also accept the following tree hashing parameters:

- *fanout*: fanout (0 to 255, 0 if unlimited, 1 in sequential mode).
- *depth*: maximal depth of tree (1 to 255, 255 if unlimited, 1 in
  sequential mode).
- *leaf\_size*: maximal byte length of leaf (0 to `2**32-1`, 0 if unlimited or in
  sequential mode).
- *node\_offset*: node offset (0 to `2**64-1` for BLAKE2b, 0 to `2**48-1` for
  BLAKE2s, 0 for the first, leftmost, leaf, or in sequential mode).
- *node\_depth*: node depth (0 to 255, 0 for leaves, or in sequential mode).
- *inner\_size*: inner digest size (0 to 64 for BLAKE2b, 0 to 32 for
  BLAKE2s, 0 in sequential mode).
- *last\_node*: boolean indicating whether the processed node is the last
  one (`False` for sequential mode).

![Explanation of tree mode parameters.](https://docs.python.org/3/_images/hashlib-blake2-tree.png)

See section 2.10 in [BLAKE2 specification](https://www.blake2.net/blake2_20130129.pdf) for comprehensive review of tree
hashing.