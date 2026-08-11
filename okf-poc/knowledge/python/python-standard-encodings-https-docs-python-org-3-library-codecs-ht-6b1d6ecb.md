---
id: python-standard-encodings-https-docs-python-org-3-library-codecs-ht-6b1d6ecb
type: concept
title: Standard Encodings[¶](https://docs.python.org/3/library/codecs.html#standard-encodings
  "Link to this heading")
description: Python comes with a number of codecs built-in, either implemented as
  C functions
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Standard Encodings[¶](https://docs.python.org/3/library/codecs.html#standard-encodings "Link to this heading")

Python comes with a number of codecs built-in, either implemented as C functions
or with dictionaries as mapping tables. The following table lists the codecs by
name, together with a few common aliases, and the languages for which the
encoding is likely used. Neither the list of aliases nor the list of languages
is meant to be exhaustive. Notice that spelling alternatives that only differ in
case or use a hyphen instead of an underscore are also valid aliases
because they are equivalent when normalized by
[`normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding"). For example, `'utf-8'` is a valid
alias for the `'utf_8'` codec.

Note

The below table lists the most common aliases, for a complete list
refer to the source [aliases.py](https://github.com/python/cpython/tree/3.14/Lib/encodings/aliases.py) file.

On Windows, `cpXXX` codecs are available for all code pages.
But only codecs listed in the following table are guarantead to exist on
other platforms.

**CPython implementation detail:** Some common encodings can bypass the codecs lookup machinery to
improve performance. These optimization opportunities are only
recognized by CPython for a limited set of (case insensitive)
aliases: utf-8, utf8, latin-1, latin1, iso-8859-1, iso8859-1, mbcs
(Windows only), ascii, us-ascii, utf-16, utf16, utf-32, utf32, and
the same using underscores instead of dashes. Using alternative
aliases for these encodings may result in slower execution.

Changed in version 3.6: Optimization opportunity recognized for us-ascii.

Many of the character sets support the same languages. They vary in individual
characters (e.g. whether the EURO SIGN is supported or not), and in the
assignment of characters to code positions. For the European languages in
particular, the following variants typically exist:

- an ISO 8859 codeset
- a Microsoft Windows code page, which is typically derived from an 8859 codeset,
  but replaces control characters with additional graphic characters
- an IBM EBCDIC code page
- an IBM PC code page, which is ASCII compatible

| Codec | Aliases | Languages |
| --- | --- | --- |
| ascii | 646, us-ascii | English |
| big5 | big5-tw, csbig5 | Traditional Chinese |
| big5hkscs | big5-hkscs, hkscs | Traditional Chinese |
| cp037 | IBM037, IBM039 | English |
| cp273 | 273, IBM273, csIBM273 | German  Added in version 3.4. |
| cp424 | EBCDIC-CP-HE, IBM424 | Hebrew |
| cp437 | 437, IBM437 | English |
| cp500 | EBCDIC-CP-BE, EBCDIC-CP-CH, IBM500 | Western Europe |
| cp720 |  | Arabic |
| cp737 |  | Greek |
| cp775 | IBM775 | Baltic languages |
| cp850 | 850, IBM850 | Western Europe |
| cp852 | 852, IBM852 | Central and Eastern Europe |
| cp855 | 855, IBM855 | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| cp856 |  | Hebrew |
| cp857 | 857, IBM857 | Turkish |
| cp858 | 858, IBM00858 | Western Europe |
| cp860 | 860, IBM860 | Portuguese |
| cp861 | 861, CP-IS, IBM861 | Icelandic |
| cp862 | 862, IBM862 | Hebrew |
| cp863 | 863, IBM863 | Canadian |
| cp864 | IBM864 | Arabic |
| cp865 | 865, IBM865 | Danish, Norwegian |
| cp866 | 866, IBM866 | Russian |
| cp869 | 869, CP-GR, IBM869 | Greek |
| cp874 |  | Thai |
| cp875 |  | Greek |
| cp932 | 932, ms932, mskanji, ms-kanji, windows-31j | Japanese |
| cp949 | 949, ms949, uhc | Korean |
| cp950 | 950, ms950 | Traditional Chinese |
| cp1006 |  | Urdu |
| cp1026 | ibm1026 | Turkish |
| cp1125 | 1125, ibm1125, cp866u, ruscii | Ukrainian  Added in version 3.4. |
| cp1140 | IBM01140 | Western Europe |
| cp1250 | windows-1250 | Central and Eastern Europe |
| cp1251 | windows-1251 | Belarusian, Bulgarian, Macedonian, Russian, Serbian |
| cp1252 | windows-1252 | Western Europe |
| cp1253 | windows-1253 | Greek |
| cp1254 | windows-1254 | Turkish |
| cp1255 | windows-1255 | Hebrew |
| cp1256 | windows-1256 | Arabic