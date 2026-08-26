---
id: python-byte-order-size-and-alignment-https-docs-python-org-3-librar-16930738
type: concept
title: Byte Order, Size, and Alignment[¶](https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
  "Link to this heading")
description: By default, C types are represented in the machine’s native format and
  byte
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Byte Order, Size, and Alignment[¶](https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment "Link to this heading")

By default, C types are represented in the machine’s native format and byte
order, and properly aligned by skipping pad bytes if necessary (according to the
rules used by the C compiler).
This behavior is chosen so
that the bytes of a packed struct correspond exactly to the memory layout
of the corresponding C struct.
Whether to use native byte ordering
and padding or standard formats depends on the application.

Alternatively, the first character of the format string can be used to indicate
the byte order, size and alignment of the packed data, according to the
following table:

| Character | Byte order | Size | Alignment |
| --- | --- | --- | --- |
| `@` | native | native | native |
| `=` | native | standard | none |
| `<` | little-endian | standard | none |
| `>` | big-endian | standard | none |
| `!` | network (= big-endian) | standard | none |

If the first character is not one of these, `'@'` is assumed.

Note

The number 1023 (`0x3ff` in hexadecimal) has the following byte representations:

- `03 ff` in big-endian (`>`)
- `ff 03` in little-endian (`<`)

Python example:

```
>>> import struct
>>> struct.pack('>h', 1023)
b'\x03\xff'
>>> struct.pack('<h', 1023)
b'\xff\x03'
```

Native byte order is big-endian or little-endian, depending on the
host system. For example, Intel x86, AMD64 (x86-64), and Apple M1 are
little-endian; IBM z and many legacy architectures are big-endian.
Use [`sys.byteorder`](https://docs.python.org/3/library/sys.html#sys.byteorder "sys.byteorder") to check the endianness of your system.

Native size and alignment are determined using the C compiler’s
`sizeof` expression. This is always combined with native byte order.

Standard size depends only on the format character; see the table in
the [Format Characters](https://docs.python.org/3/library/struct.html#format-characters) section.

Note the difference between `'@'` and `'='`: both use native byte order, but
the size and alignment of the latter is standardized.

The form `'!'` represents the network byte order which is always big-endian
as defined in [IETF RFC 1700](https://datatracker.ietf.org/doc/html/rfc1700).

There is no way to indicate non-native byte order (force byte-swapping); use the
appropriate choice of `'<'` or `'>'`.

Notes:

1. Padding is only automatically added between successive structure members.
   No padding is added at the beginning or the end of the encoded struct.
2. No padding is added when using non-native size and alignment, e.g.
   with ‘<’, ‘>’, ‘=’, and ‘!’.
3. To align the end of a structure to the alignment requirement of a
   particular type, end the format with the code for that type with a repeat
   count of zero. See [Examples](https://docs.python.org/3/library/struct.html#struct-examples).