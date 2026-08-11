---
id: python-encodings-and-unicode-https-docs-python-org-3-library-codecs-6b1d6ecb
type: concept
title: Encodings and Unicode[¶](https://docs.python.org/3/library/codecs.html#encodings-and-unicode
  "Link to this heading")
description: Strings are stored internally as sequences of code points in
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Encodings and Unicode[¶](https://docs.python.org/3/library/codecs.html#encodings-and-unicode "Link to this heading")

Strings are stored internally as sequences of code points in
range `U+0000`–`U+10FFFF`. (See [**PEP 393**](https://peps.python.org/pep-0393/) for
more details about the implementation.)
Once a string object is used outside of CPU and memory, endianness
and how these arrays are stored as bytes become an issue. As with other
codecs, serialising a string into a sequence of bytes is known as *encoding*,
and recreating the string from the sequence of bytes is known as *decoding*.
There are a variety of different text serialisation codecs, which are
collectivity referred to as [text encodings](https://docs.python.org/3/glossary.html#term-text-encoding).

The simplest text encoding (called `'latin-1'` or `'iso-8859-1'`) maps
the code points 0–255 to the bytes `0x0`–`0xff`, which means that a string
object that contains code points above `U+00FF` can’t be encoded with this
codec. Doing so will raise a [`UnicodeEncodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "UnicodeEncodeError") that looks
like the following (although the details of the error message may differ):
`UnicodeEncodeError: 'latin-1' codec can't encode character '\u1234' in
position 3: ordinal not in range(256)`.

There’s another group of encodings (the so called charmap encodings) that choose
a different subset of all Unicode code points and how these code points are
mapped to the bytes `0x0`–`0xff`. To see how this is done simply open
e.g. `encodings/cp1252.py` (which is an encoding that is used primarily on
Windows). There’s a string constant with 256 characters that shows you which
character is mapped to which byte value.

All of these encodings can only encode 256 of the 1114112 code points
defined in Unicode. A simple and straightforward way that can store each Unicode
code point, is to store each code point as four consecutive bytes. There are two
possibilities: store the bytes in big endian or in little endian order. These
two encodings are called `UTF-32-BE` and `UTF-32-LE` respectively. Their
disadvantage is that if, for example, you use `UTF-32-BE` on a little endian
machine you will always have to swap bytes on encoding and decoding.
Python’s `UTF-16` and `UTF-32` codecs avoid this problem by using the
platform’s native byte order when no BOM is present.
Python follows prevailing platform
practice, so native-endian data round-trips without redundant byte swapping,
even though the Unicode Standard defaults to big-endian when the byte order is
unspecified. When these bytes are read by a CPU with a different endianness,
the bytes have to be swapped. To be able to detect the endianness of a
`UTF-16` or `UTF-32` byte sequence, a BOM (“Byte Order Mark”) is used.
This is the Unicode character `U+FEFF`. This character can be prepended to every
`UTF-16` or `UTF-32` byte sequence. The byte swapped version of this character
(`0xFFFE`) is an illegal character that may not appear in a Unicode text.
When the first character of a `UTF-16` or `UTF-32` byte sequence is
`U+FFFE`, the bytes have to be swapped on decoding.

Unfortunately the character `U+FEFF` had a second purpose as
a `ZERO WIDTH NO-BREAK SPACE`: a character that has no width and doesn’t allow
a word to be split. It can e.g. be used to give hints to a ligature algorithm.
With Unicode 4.0 using `U+FEFF` as a `ZERO WIDTH NO-BREAK SPACE` has been
deprecated (with `U+2060` (`WORD JOINER`) assuming this role). Nevertheless
Unicode software still must be able to handle `U+FEFF` in both roles: as a BOM
it’s a device to determine the storage layout of the encoded bytes, and vanishes
once the byte sequence has been decoded into a string; as a `ZERO WIDTH
NO-BREAK SPACE` it’s a normal character that will be decoded like any other.

There’s another encoding that is able to encode the full range of Unicode
characters: UTF-8. UTF-8 is an 8-bit encoding, which means there are