---
id: python-filetype-objects-https-docs-python-org-3-library-argparse-ht-49b35a18
type: concept
title: FileType objects[¶](https://docs.python.org/3/library/argparse.html#filetype-objects
  "Link to this heading")
description: '*class* argparse.FileType(*mode=''r''*, *bufsize=-1*, *encoding=None*,
  *errors=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.FileType
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### FileType objects[¶](https://docs.python.org/3/library/argparse.html#filetype-objects "Link to this heading")

*class* argparse.FileType(*mode='r'*, *bufsize=-1*, *encoding=None*, *errors=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.FileType "Link to this definition")
:   The `FileType` factory creates objects that can be passed to the type
    argument of [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). Arguments that have
    `FileType` objects as their type will open command-line arguments as
    files with the requested modes, buffer sizes, encodings and error handling
    (see the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function for more details):

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
    >>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
    >>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
    Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)
    ```

    FileType objects understand the pseudo-argument `'-'` and automatically
    convert this into [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") for readable `FileType` objects and
    [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") for writable `FileType` objects:

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('infile', type=argparse.FileType('r'))
    >>> parser.parse_args(['-'])
    Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)
    ```

    Note

    If one argument uses *FileType* and then a subsequent argument fails,
    an error is reported but the file is not automatically closed.
    This can also clobber the output files.
    In this case, it would be better to wait until after the parser has
    run and then use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)-statement to manage the files.

    Changed in version 3.4: Added the *encoding* and *errors* parameters.

    Deprecated since version 3.14.