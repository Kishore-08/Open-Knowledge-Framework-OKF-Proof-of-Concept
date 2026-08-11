---
id: python-bytes-and-bytearray-operations-https-docs-python-org-3-libra-5e0bc1d7
type: concept
title: Bytes and Bytearray Operations[¶](https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray-operations
  "Link to this heading")
description: Both bytes and bytearray objects support the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common)
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Bytes and Bytearray Operations[¶](https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray-operations "Link to this heading")

Both bytes and bytearray objects support the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common)
sequence operations. They interoperate not just with operands of the same
type, but with any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object). Due to this flexibility, they can be
freely mixed in operations without causing errors. However, the return type
of the result may depend on the order of operands.

Note

The methods on bytes and bytearray objects don’t accept strings as their
arguments, just as the methods on strings don’t accept bytes as their
arguments. For example, you have to write:

```
a = "abc"
b = a.replace("a", "f")
```

and:

```
a = b"abc"
b = a.replace(b"a", b"f")
```

Some bytes and bytearray operations assume the use of ASCII compatible
binary formats, and hence should be avoided when working with arbitrary
binary data. These restrictions are covered below.

Note

Using these ASCII based operations to manipulate binary data that is not
stored in an ASCII based format may lead to data corruption.

The following methods on bytes and bytearray objects can be used with
arbitrary binary data.

bytes.count(*sub*[, *start*[, *end*]])[¶](https://docs.python.org/3/library/stdtypes.html#bytes.count "Link to this definition")

bytearray.count(*sub*[, *start*[, *end*]])[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.count "Link to this definition")
:   Return the number of non-overlapping occurrences of subsequence *sub* in
    the range [*start*, *end*]. Optional arguments *start* and *end* are
    interpreted as in slice notation.

    The subsequence to search for may be any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or an
    integer in the range 0 to 255.

    If *sub* is empty, returns the number of empty slices between characters
    which is the length of the bytes object plus one.

    Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.removeprefix(*prefix*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytes.removeprefix "Link to this definition")

bytearray.removeprefix(*prefix*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.removeprefix "Link to this definition")
:   If the binary data starts with the *prefix* string, return
    `bytes[len(prefix):]`. Otherwise, return a copy of the original
    binary data:

    ```
    >>> b'TestHook'.removeprefix(b'Test')
    b'Hook'
    >>> b'BaseTestCase'.removeprefix(b'Test')
    b'BaseTestCase'
    ```

    The *prefix* may be any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

    Note

    The bytearray version of this method does *not* operate in place -
    it always produces a new object, even if no changes were made.

    Added in version 3.9.

bytes.removesuffix(*suffix*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytes.removesuffix "Link to this definition")

bytearray.removesuffix(*suffix*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.removesuffix "Link to this definition")
:   If the binary data ends with the *suffix* string and that *suffix* is
    not empty, return `bytes[:-len(suffix)]`. Otherwise, return a copy of
    the original binary data:

    ```
    >>> b'MiscTests'.removesuffix(b'Tests')
    b'Misc'
    >>> b'TmpDirMixin'.removesuffix(b'Tests')
    b'TmpDirMixin'
    ```

    The *suffix* may be any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

    Note

    The bytearray version of this method does *not* operate in place -
    it always produces a new object, even if no changes were made.

    Added in version 3.9.

bytes.decode(*encoding='utf-8'*, *errors='strict'*)[¶](https://docs.python.org/3/library/stdtypes.ht