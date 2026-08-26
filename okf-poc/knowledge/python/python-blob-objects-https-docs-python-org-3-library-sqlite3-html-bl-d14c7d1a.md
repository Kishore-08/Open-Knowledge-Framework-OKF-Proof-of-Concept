---
id: python-blob-objects-https-docs-python-org-3-library-sqlite3-html-bl-d14c7d1a
type: concept
title: Blob objects[¶](https://docs.python.org/3/library/sqlite3.html#blob-objects
  "Link to this heading")
description: '*class* sqlite3.Blob[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Blob objects[¶](https://docs.python.org/3/library/sqlite3.html#blob-objects "Link to this heading")

*class* sqlite3.Blob[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "Link to this definition")
:   Added in version 3.11.

    A `Blob` instance is a [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object)
    that can read and write data in an SQLite BLOB.
    Call [`len(blob)`](https://docs.python.org/3/library/functions.html#len "len") to get the size (number of bytes) of the blob.
    Use indices and [slices](https://docs.python.org/3/glossary.html#term-slice) for direct access to the blob data.

    Use the `Blob` as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) to ensure that the blob
    handle is closed after use.

    ```
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE test(blob_col blob)")
    con.execute("INSERT INTO test(blob_col) VALUES(zeroblob(13))")

    # Write to our blob, using two write operations:
    with con.blobopen("test", "blob_col", 1) as blob:
        blob.write(b"hello, ")
        blob.write(b"world.")
        # Modify the first and last bytes of our blob
        blob[0] = ord("H")
        blob[-1] = ord("!")

    # Read the contents of our blob
    with con.blobopen("test", "blob_col", 1) as blob:
        greeting = blob.read()

    print(greeting)  # outputs "b'Hello, world!'"
    con.close()
    ```

    close()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.close "Link to this definition")
    :   Close the blob.

        The blob will be unusable from this point onward. An
        [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error") (or subclass) exception will be raised if any
        further operation is attempted with the blob.

    read(*length=-1*, */*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.read "Link to this definition")
    :   Read *length* bytes of data from the blob at the current offset position.
        If the end of the blob is reached, the data up to
        EOF will be returned. When *length* is not
        specified, or is negative, `read()` will read until the end of
        the blob.

    write(*data*, */*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.write "Link to this definition")
    :   Write *data* to the blob at the current offset. This function cannot
        change the blob length. Writing beyond the end of the blob will raise
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

    tell()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.tell "Link to this definition")
    :   Return the current access position of the blob.

    seek(*offset*, *origin=os.SEEK\_SET*, */*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob.seek "Link to this definition")
    :   Set the current access position of the blob to *offset*. The *origin*
        argument defaults to [`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET") (absolute blob positioning).
        Other values for *origin* are [`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR") (seek relative to the
        current position) and [`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END") (seek relative to the blob’s
        end).