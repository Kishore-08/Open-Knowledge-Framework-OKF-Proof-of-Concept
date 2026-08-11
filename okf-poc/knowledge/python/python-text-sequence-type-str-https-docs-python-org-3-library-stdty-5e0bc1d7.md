---
id: python-text-sequence-type-str-https-docs-python-org-3-library-stdty-5e0bc1d7
type: concept
title: Text Sequence Type — [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str")[¶](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
  "Link to this heading")
description: Textual data in Python is handled with [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") objects, or *strings*.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Text Sequence Type — [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")[¶](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "Link to this heading")

Textual data in Python is handled with [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects, or *strings*.
Strings are immutable
[sequences](https://docs.python.org/3/library/stdtypes.html#typesseq) of Unicode code points. String literals are
written in a variety of ways:

- Single quotes: `'allows embedded "double" quotes'`
- Double quotes: `"allows embedded 'single' quotes"`
- Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`

Triple quoted strings may span multiple lines - all associated whitespace will
be included in the string literal.

String literals that are part of a single expression and have only whitespace
between them will be implicitly converted to a single string literal. That
is, `("spam " "eggs") == "spam eggs"`.

See [String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings) for more about the various forms of string literal,
including supported [escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences), and the `r` (“raw”) prefix that
disables most escape sequence processing.

Strings may also be created from other objects using the [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")
constructor.

Since there is no separate “character” type, indexing a string produces
strings of length 1. That is, for a non-empty string *s*, `s[0] == s[0:1]`.

There is also no mutable string type, but [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join "str.join") or
[`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") can be used to efficiently construct strings from
multiple fragments.

Changed in version 3.3: For backwards compatibility with the Python 2 series, the `u` prefix is
once again permitted on string literals. It has no effect on the meaning
of string literals and cannot be combined with the `r` prefix.

*class* str(*\**, *encoding='utf-8'*, *errors='strict'*)[¶](https://docs.python.org/3/library/stdtypes.html#str "Link to this definition")

*class* str(*object*)

*class* str(*object*, *encoding*, *errors='strict'*)

*class* str(*object*, *\**, *errors*)
:   Return a [string](https://docs.python.org/3/library/stdtypes.html#textseq) version of *object*. If *object* is not
    provided, returns the empty string. Otherwise, the behavior of `str()`
    depends on whether *encoding* or *errors* is given, as follows.

    If neither *encoding* nor *errors* is given, `str(object)` returns
    [`type(object).__str__(object)`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__"),
    which is the “informal” or nicely
    printable string representation of *object*. For string objects, this is
    the string itself. If *object* does not have a `__str__()`
    method, then [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") falls back to returning
    [`repr(object)`](https://docs.python.org/3/library/functions.html#repr "repr").

    If at least one of *encoding* or *errors* is given, *object* should be a
    [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) (e.g. [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray")). In
    this case, if *object* is a `bytes` (or `bytearray`) object,
    then `str(bytes, encoding, errors)` is equivalent to
    [`bytes.decode(encoding, errors)`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "bytes.decode"). Otherwise, the bytes
    object underlying the buffer object is obtained before calling
    `bytes.decode()`. See [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3/library/stdtypes.html#b