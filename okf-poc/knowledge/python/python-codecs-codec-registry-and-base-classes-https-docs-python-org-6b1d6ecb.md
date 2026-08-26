---
id: python-codecs-codec-registry-and-base-classes-https-docs-python-org-6b1d6ecb
type: concept
title: '`codecs` — Codec registry and base classes[¶](https://docs.python.org/3/library/'
description: '**Source code:** [Lib/codecs.py](https://github.com/python/cpython/tree/3.14/Lib/codecs.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `codecs` — Codec registry and base classes[¶](https://docs.python.org/3/library/codecs.html#module-codecs "Link to this heading")

**Source code:** [Lib/codecs.py](https://github.com/python/cpython/tree/3.14/Lib/codecs.py)

---

This module defines base classes for standard Python codecs (encoders and
decoders) and provides access to the internal Python codec registry, which
manages the codec and error handling lookup process. Most standard codecs
are [text encodings](https://docs.python.org/3/glossary.html#term-text-encoding), which encode text to bytes (and
decode bytes to text), but there are also codecs provided that encode text to
text, and bytes to bytes. Custom codecs may encode and decode between arbitrary
types, but some module features are restricted to be used specifically with
text encodings or with codecs that encode to
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

The module defines the following functions for encoding and decoding with
any codec:

codecs.encode(*obj*, *encoding='utf-8'*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.encode "Link to this definition")
:   Encodes *obj* using the codec registered for *encoding*.

    *Errors* may be given to set the desired error handling scheme. The
    default error handler is `'strict'` meaning that encoding errors raise
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as
    [`UnicodeEncodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")). Refer to [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes) for more
    information on codec error handling.

codecs.decode(*obj*, *encoding='utf-8'*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.decode "Link to this definition")
:   Decodes *obj* using the codec registered for *encoding*.

    *Errors* may be given to set the desired error handling scheme. The
    default error handler is `'strict'` meaning that decoding errors raise
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as
    [`UnicodeDecodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")). Refer to [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes) for more
    information on codec error handling.

codecs.charmap\_build(*string*)[¶](https://docs.python.org/3/library/codecs.html#codecs.charmap_build "Link to this definition")
:   Return a mapping suitable for encoding with a custom single-byte encoding.
    Given a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") *string* of up to 256 characters representing a
    decoding table, returns either a compact internal mapping object
    `EncodingMap` or a [`dictionary`](https://docs.python.org/3/library/stdtypes.html#dict "dict") mapping character ordinals
    to byte values. Raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") on invalid input.

The full details for each codec can also be looked up directly:

codecs.lookup(*encoding*, */*)[¶](https://docs.python.org/3/library/codecs.html#codecs.lookup "Link to this definition")
:   Looks up the codec info in the Python codec registry and returns a
    [`CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object as defined below.

    Encodings are first looked up in the registry’s cache. If not found, the list of
    registered search functions is scanned. If no [`CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object is
    found, a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") is raised. Otherwise, the `CodecInfo` object
    is stored in the c