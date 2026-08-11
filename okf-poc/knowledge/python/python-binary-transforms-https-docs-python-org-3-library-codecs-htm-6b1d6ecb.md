---
id: python-binary-transforms-https-docs-python-org-3-library-codecs-htm-6b1d6ecb
type: concept
title: Binary Transforms[¶](https://docs.python.org/3/library/codecs.html#binary-transforms
  "Link to this heading")
description: 'The following codecs provide binary transforms: [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Binary Transforms[¶](https://docs.python.org/3/library/codecs.html#binary-transforms "Link to this heading")

The following codecs provide binary transforms: [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") mappings. They are not supported by [`bytes.decode()`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "bytes.decode")
(which only produces [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") output).

| Codec | Aliases | Meaning | Encoder / decoder |
| --- | --- | --- | --- |
| base64\_codec [[1]](https://docs.python.org/3/library/codecs.html#b64) | base64, base\_64 | Convert the operand to multiline MIME base64 (the result always includes a trailing `'\n'`).  Changed in version 3.4: accepts any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) as input for encoding and decoding | [`base64.encodebytes()`](https://docs.python.org/3/library/base64.html#base64.encodebytes "base64.encodebytes") / [`base64.decodebytes()`](https://docs.python.org/3/library/base64.html#base64.decodebytes "base64.decodebytes") |
| bz2\_codec | bz2 | Compress the operand using bz2. | [`bz2.compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") / [`bz2.decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") |
| hex\_codec | hex | Convert the operand to hexadecimal representation, with two digits per byte. | [`binascii.b2a_hex()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "binascii.b2a_hex") / [`binascii.a2b_hex()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_hex "binascii.a2b_hex") |
| quopri\_codec | quopri, quotedprintable, quoted\_printable | Convert the operand to MIME quoted printable. | [`quopri.encode()`](https://docs.python.org/3/library/quopri.html#quopri.encode "quopri.encode") with `quotetabs=True` / [`quopri.decode()`](https://docs.python.org/3/library/quopri.html#quopri.decode "quopri.decode") |
| uu\_codec | uu | Convert the operand using uuencode. |  |
| zlib\_codec | zip, zlib | Compress the operand using gzip. | [`zlib.compress()`](https://docs.python.org/3/library/zlib.html#zlib.compress "zlib.compress") / [`zlib.decompress()`](https://docs.python.org/3/library/zlib.html#zlib.decompress "zlib.decompress") |

Added in version 3.2: Restoration of the binary transforms.

Changed in version 3.4: Restoration of the aliases for the binary transforms.