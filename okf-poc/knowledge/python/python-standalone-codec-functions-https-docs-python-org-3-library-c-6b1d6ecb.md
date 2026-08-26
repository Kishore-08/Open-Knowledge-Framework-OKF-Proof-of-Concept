---
id: python-standalone-codec-functions-https-docs-python-org-3-library-c-6b1d6ecb
type: concept
title: Standalone Codec Functions[¶](https://docs.python.org/3/library/codecs.html#standalone-codec-functions
  "Link to this heading")
description: The following functions provide encoding and decoding functionality similar
  to codecs,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Standalone Codec Functions[¶](https://docs.python.org/3/library/codecs.html#standalone-codec-functions "Link to this heading")

The following functions provide encoding and decoding functionality similar to codecs,
but are not available as named codecs through [`codecs.encode()`](https://docs.python.org/3/library/codecs.html#codecs.encode "codecs.encode") or [`codecs.decode()`](https://docs.python.org/3/library/codecs.html#codecs.decode "codecs.decode").
They are used internally (for example, by [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")) and behave similarly to the
`string_escape` codec that was removed in Python 3.

codecs.escape\_encode(*input*, *errors=None*)[¶](https://docs.python.org/3/library/codecs.html#codecs.codecs.escape_encode "Link to this definition")
:   Encode *input* using escape sequences. Similar to how [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") on bytes
    produces escaped byte values.

    *input* must be a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.

    Returns a tuple `(output, length)` where *output* is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
    object and *length* is the number of bytes consumed.

codecs.escape\_decode(*input*, *errors=None*)[¶](https://docs.python.org/3/library/codecs.html#codecs.codecs.escape_decode "Link to this definition")
:   Decode *input* from escape sequences back to the original bytes.

    *input* must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

    Returns a tuple `(output, length)` where *output* is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
    object and *length* is the number of bytes consumed.