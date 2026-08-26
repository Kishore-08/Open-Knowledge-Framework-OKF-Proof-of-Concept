---
id: python-text-encodings-https-docs-python-org-3-library-codecs-html-t-6b1d6ecb
type: concept
title: Text Encodings[¶](https://docs.python.org/3/library/codecs.html#text-encodings
  "Link to this heading")
description: The following codecs provide [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
  encoding and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Text Encodings[¶](https://docs.python.org/3/library/codecs.html#text-encodings "Link to this heading")

The following codecs provide [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") encoding and
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) to `str` decoding, similar to the Unicode text
encodings.

| Codec | Aliases | Meaning |
| --- | --- | --- |
| idna |  | Implement [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html), see also [`encodings.idna`](https://docs.python.org/3/library/codecs.html#module-encodings.idna "encodings.idna: Internationalized Domain Names implementation"). Only `errors='strict'` is supported. |
| mbcs | ansi, dbcs | Windows only: Encode the operand according to the ANSI codepage (CP\_ACP). |
| oem |  | Windows only: Encode the operand according to the OEM codepage (CP\_OEMCP).  Added in version 3.6. |
| palmos |  | Encoding of PalmOS 3.5. |
| punycode |  | Implement [**RFC 3492**](https://datatracker.ietf.org/doc/html/rfc3492.html). Stateful codecs are not supported.  Warning  The decoding and encoding algorithms scale poorly, so limit the length of untrusted input. |
| raw\_unicode\_escape |  | Latin-1 encoding with `\uXXXX` and `\UXXXXXXXX` for other code points. Existing backslashes are not escaped in any way. It is used in the Python pickle protocol. |
| undefined |  | This Codec should only be used for testing purposes.  Raise an exception for all conversions, even empty strings. The error handler is ignored. |
| unicode\_escape |  | Encoding suitable as the contents of a Unicode literal in ASCII-encoded Python source code, except that quotes are not escaped. Decode from Latin-1 source code. Beware that Python source code actually uses UTF-8 by default. |

Changed in version 3.8: “unicode\_internal” codec is removed.