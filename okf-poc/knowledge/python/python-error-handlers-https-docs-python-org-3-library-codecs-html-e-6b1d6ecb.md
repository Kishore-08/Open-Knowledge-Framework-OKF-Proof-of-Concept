---
id: python-error-handlers-https-docs-python-org-3-library-codecs-html-e-6b1d6ecb
type: concept
title: Error Handlers[¶](https://docs.python.org/3/library/codecs.html#error-handlers
  "Link to this heading")
description: To simplify and standardize error handling, codecs may implement different
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Error Handlers[¶](https://docs.python.org/3/library/codecs.html#error-handlers "Link to this heading")

To simplify and standardize error handling, codecs may implement different
error handling schemes by accepting the *errors* string argument:

```
>>> 'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
>>> 'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'
```

The following error handlers can be used with all Python
[Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings) codecs:

| Value | Meaning |
| --- | --- |
| `'strict'` | Raise [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError") (or a subclass), this is the default. Implemented in [`strict_errors()`](https://docs.python.org/3/library/codecs.html#codecs.strict_errors "codecs.strict_errors"). |
| `'ignore'` | Ignore the malformed data and continue without further notice. Implemented in [`ignore_errors()`](https://docs.python.org/3/library/codecs.html#codecs.ignore_errors "codecs.ignore_errors"). |
| `'replace'` | Replace with a replacement marker. On encoding, use `?` (ASCII character). On decoding, use `�` (U+FFFD, the official REPLACEMENT CHARACTER). Implemented in [`replace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.replace_errors "codecs.replace_errors"). |
| `'backslashreplace'` | Replace with backslashed escape sequences. On encoding, use hexadecimal form of Unicode code point with formats `\xhh` `\uxxxx` `\Uxxxxxxxx`. On decoding, use hexadecimal form of byte value with format `\xhh`. Implemented in [`backslashreplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.backslashreplace_errors "codecs.backslashreplace_errors"). |
| `'surrogateescape'` | On decoding, replace byte with individual surrogate code ranging from `U+DC80` to `U+DCFF`. This code will then be turned back into the same byte when the `'surrogateescape'` error handler is used when encoding the data. (See [**PEP 383**](https://peps.python.org/pep-0383/) for more.) |

The following error handlers are only applicable to encoding (within
[text encodings](https://docs.python.org/3/glossary.html#term-text-encoding)):

| Value | Meaning |
| --- | --- |
| `'xmlcharrefreplace'` | Replace with XML/HTML numeric character reference, which is a decimal form of Unicode code point with format `&#num;`. Implemented in [`xmlcharrefreplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.xmlcharrefreplace_errors "codecs.xmlcharrefreplace_errors"). |
| `'namereplace'` | Replace with `\N{...}` escape sequences, what appears in the braces is the Name property from Unicode Character Database. Implemented in [`namereplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.namereplace_errors "codecs.namereplace_errors"). |

In addition, the following error handler is specific to the given codecs:

| Value | Codecs | Meaning |
| --- | --- | --- |
| `'surrogatepass'` | utf-8, utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le | Allow encoding and decoding surrogate code point (`U+D800` - `U+DFFF`) as normal code point. Otherwise these codecs treat the presence of surrogate code point in [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") as an error. |

Added in version 3.1: The `'surrogateescape'` and `'surrogatepass'` error handlers.

Changed in version 3.4: The `'surrogatepass'` error handler now works with utf-16\* and utf-32\*
codecs.

Added in version 3.5: The `'namereplace'` error handler.

Changed in version 3.5: The `'backslashreplace'` error handler now works with decoding and
translating.

The set of allowed values can be extended by registering a new named error
handler:

codecs.register\_error(*name*, *error\_handler*, */*)[¶](https://docs.python.org/3/library/codecs.html#codecs.register_error "Link to this definition")
:   Register the error handling function *error