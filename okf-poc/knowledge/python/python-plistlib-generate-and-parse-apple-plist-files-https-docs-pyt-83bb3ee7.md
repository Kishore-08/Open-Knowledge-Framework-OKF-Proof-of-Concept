---
id: python-plistlib-generate-and-parse-apple-plist-files-https-docs-pyt-83bb3ee7
type: concept
title: '`plistlib` — Generate and parse Apple `.plist` files[¶](https://docs.python.org/'
description: '**Source code:** [Lib/plistlib.py](https://github.com/python/cpython/tree/3.14/Lib/plistlib.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/plistlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `plistlib` — Generate and parse Apple `.plist` files[¶](https://docs.python.org/3/library/plistlib.html#module-plistlib "Link to this heading")

**Source code:** [Lib/plistlib.py](https://github.com/python/cpython/tree/3.14/Lib/plistlib.py)

---

This module provides an interface for reading and writing the “property list”
files used by Apple, primarily on macOS and iOS. This module supports both binary
and XML plist files.

The property list (`.plist`) file format is a simple serialization supporting
basic object types, like dictionaries, lists, numbers and strings. Usually the
top level object is a dictionary.

To write out and to parse a plist file, use the [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump") and
[`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load") functions.

To work with plist data in bytes or string objects, use [`dumps()`](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "plistlib.dumps")
and [`loads()`](https://docs.python.org/3/library/plistlib.html#plistlib.loads "plistlib.loads").

Values can be strings, integers, floats, booleans, tuples, lists, dictionaries
(but only with string keys), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray")
or [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects.

Changed in version 3.4: New API, old API deprecated. Support for binary format plists added.

Changed in version 3.8: Support added for reading and writing [`UID`](https://docs.python.org/3/library/plistlib.html#plistlib.UID "plistlib.UID") tokens in binary plists as used
by NSKeyedArchiver and NSKeyedUnarchiver.

Changed in version 3.9: Old API removed.

See also

[PList manual page](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/)
:   Apple’s documentation of the file format.

This module defines the following functions:

plistlib.load(*fp*, *\**, *fmt=None*, *dict\_type=dict*, *aware\_datetime=False*)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.load "Link to this definition")
:   Read a plist file. *fp* should be a readable and binary file object.
    Return the unpacked root object (which usually is a
    dictionary).

    The *fmt* is the format of the file and the following values are valid:

    - [`None`](https://docs.python.org/3/library/constants.html#None "None"): Autodetect the file format
    - [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML"): XML file format
    - [`FMT_BINARY`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_BINARY "plistlib.FMT_BINARY"): Binary plist format

    The *dict\_type* is the type used for dictionaries that are read from the
    plist file.

    When *aware\_datetime* is true, fields with type `datetime.datetime` will
    be created as [aware object](https://docs.python.org/3/library/datetime.html#datetime-naive-aware), with
    `tzinfo` as [`datetime.UTC`](https://docs.python.org/3/library/datetime.html#datetime.UTC "datetime.UTC").

    XML data for the [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML") format is parsed using the Expat parser
    from [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") – see its documentation for possible
    exceptions on ill-formed XML. Unknown elements will simply be ignored
    by the plist parser.

    The parser raises [`InvalidFileException`](https://docs.python.org/3/library/plistlib.html#plistlib.InvalidFileException "plistlib.InvalidFileException") when the file cannot be parsed.

    Added in version 3.4.

    Changed in version 3.13: The keyword-only parameter *aware\_datetime* has been