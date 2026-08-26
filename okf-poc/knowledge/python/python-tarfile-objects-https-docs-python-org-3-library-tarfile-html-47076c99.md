---
id: python-tarfile-objects-https-docs-python-org-3-library-tarfile-html-47076c99
type: concept
title: TarFile Objects[¶](https://docs.python.org/3/library/tarfile.html#tarfile-objects
  "Link to this heading")
description: The [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile
  "tarfile.TarFile") object provides an interface to a tar archive. A tar
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## TarFile Objects[¶](https://docs.python.org/3/library/tarfile.html#tarfile-objects "Link to this heading")

The [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object provides an interface to a tar archive. A tar
archive is a sequence of blocks. An archive member (a stored file) is made up of
a header block followed by data blocks. It is possible to store a file in a tar
archive several times. Each archive member is represented by a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
object, see [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects) for details.

A [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object can be used as a context manager in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
statement. It will automatically be closed when the block is completed. Please
note that in the event of an exception an archive opened for writing will not
be finalized; only the internally used file object will be closed. See the
[Examples](https://docs.python.org/3/library/tarfile.html#tar-examples) section for a use case.

Added in version 3.2: Added support for the context management protocol.

*class* tarfile.TarFile(*name=None*, *mode='r'*, *fileobj=None*, *format=DEFAULT\_FORMAT*, *tarinfo=TarInfo*, *dereference=False*, *ignore\_zeros=False*, *encoding=ENCODING*, *errors='surrogateescape'*, *pax\_headers=None*, *debug=0*, *errorlevel=1*, *stream=False*)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "Link to this definition")
:   All following arguments are optional and can be accessed as instance attributes
    as well.

    *name* is the pathname of the archive. *name* may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
    It can be omitted if *fileobj* is given.
    In this case, the file object’s `name` attribute is used if it exists.

    *mode* is either `'r'` to read from an existing archive, `'a'` to append
    data to an existing file, `'w'` to create a new file overwriting an existing
    one, or `'x'` to create a new file only if it does not already exist.

    If *fileobj* is given, it is used for reading or writing data. If it can be
    determined, *mode* is overridden by *fileobj*’s mode. *fileobj* will be used
    from position 0.

    Note

    *fileobj* is not closed, when `TarFile` is closed.

    *format* controls the archive format for writing. It must be one of the constants
    [`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT"), [`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT") or [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") that are
    defined at module level. When reading, format will be automatically detected, even
    if different formats are present in a single archive.

    The *tarinfo* argument can be used to replace the default [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") class
    with a different one.

    If *dereference* is [`False`](https://docs.python.org/3/library/constants.html#False "False"), add symbolic and hard links to the archive. If it
    is [`True`](https://docs.python.org/3/library/constants.html#True "True"), add the content of the target files to the archive. This has no
    effect on systems that do not support symbolic links.

    If *ignore\_zeros* is [`False`](https://docs.python.org/3/library/constants.html#False "False"), treat an empty block as the end of the archive.
    If it is [`True`](https://docs.python.org/3/library/constants.html#True "True"), skip empty (and invalid) blocks and try to get as many members
    as possible. This is only useful for reading concatenated or damaged archives.

    *debug