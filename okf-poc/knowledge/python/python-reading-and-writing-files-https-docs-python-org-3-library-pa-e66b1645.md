---
id: python-reading-and-writing-files-https-docs-python-org-3-library-pa-e66b1645
type: concept
title: Reading and writing files[¶](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files
  "Link to this heading")
description: Path.open(*mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*,
  *newline=None*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Reading and writing files[¶](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files "Link to this heading")

Path.open(*mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "Link to this definition")
:   Open the file pointed to by the path, like the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open")
    function does:

    ```
    >>> p = Path('setup.py')
    >>> with p.open() as f:
    ...     f.readline()
    ...
    '#!/usr/bin/env python3\n'
    ```

Path.read\_text(*encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text "Link to this definition")
:   Return the decoded contents of the pointed-to file as a string:

    ```
    >>> p = Path('my_text_file')
    >>> p.write_text('Text file contents')
    18
    >>> p.read_text()
    'Text file contents'
    ```

    The file is opened and then closed. The optional parameters have the same
    meaning as in [`open()`](https://docs.python.org/3/library/functions.html#open "open").

    Added in version 3.5.

    Changed in version 3.13: The *newline* parameter was added.

Path.read\_bytes()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes "Link to this definition")
:   Return the binary contents of the pointed-to file as a bytes object:

    ```
    >>> p = Path('my_binary_file')
    >>> p.write_bytes(b'Binary file contents')
    20
    >>> p.read_bytes()
    b'Binary file contents'
    ```

    Added in version 3.5.

Path.write\_text(*data*, *encoding=None*, *errors=None*, *newline=None*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text "Link to this definition")
:   Open the file pointed to in text mode, write *data* to it, and close the
    file:

    ```
    >>> p = Path('my_text_file')
    >>> p.write_text('Text file contents')
    18
    >>> p.read_text()
    'Text file contents'
    ```

    An existing file of the same name is overwritten. The optional parameters
    have the same meaning as in [`open()`](https://docs.python.org/3/library/functions.html#open "open").

    Added in version 3.5.

    Changed in version 3.10: The *newline* parameter was added.

Path.write\_bytes(*data*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "Link to this definition")
:   Open the file pointed to in bytes mode, write *data* to it, and close the
    file:

    ```
    >>> p = Path('my_binary_file')
    >>> p.write_bytes(b'Binary file contents')
    20
    >>> p.read_bytes()
    b'Binary file contents'
    ```

    An existing file of the same name is overwritten.

    Added in version 3.5.