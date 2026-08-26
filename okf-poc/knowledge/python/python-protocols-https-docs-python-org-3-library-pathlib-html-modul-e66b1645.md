---
id: python-protocols-https-docs-python-org-3-library-pathlib-html-modul-e66b1645
type: concept
title: Protocols[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib.types
  "Link to this heading")
description: The `pathlib.types` module provides types for static type checking.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Protocols[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib.types "Link to this heading")

The `pathlib.types` module provides types for static type checking.

Added in version 3.14.

*class* pathlib.types.PathInfo[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo "Link to this definition")
:   A [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol") describing the
    [`Path.info`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.info "pathlib.Path.info") attribute. Implementations may
    return cached results from their methods.

    exists(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.exists "Link to this definition")
    :   Return `True` if the path is an existing file or directory, or any
        other kind of file; return `False` if the path doesn’t exist.

        If *follow\_symlinks* is `False`, return `True` for symlinks without
        checking if their targets exist.

    is\_dir(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_dir "Link to this definition")
    :   Return `True` if the path is a directory, or a symbolic link pointing
        to a directory; return `False` if the path is (or points to) any other
        kind of file, or if it doesn’t exist.

        If *follow\_symlinks* is `False`, return `True` only if the path
        is a directory (without following symlinks); return `False` if the
        path is any other kind of file, or if it doesn’t exist.

    is\_file(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_file "Link to this definition")
    :   Return `True` if the path is a file, or a symbolic link pointing to
        a file; return `False` if the path is (or points to) a directory or
        other non-file, or if it doesn’t exist.

        If *follow\_symlinks* is `False`, return `True` only if the path
        is a file (without following symlinks); return `False` if the path
        is a directory or other non-file, or if it doesn’t exist.

    is\_symlink()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_symlink "Link to this definition")
    :   Return `True` if the path is a symbolic link (even if broken); return
        `False` if the path is a directory or any kind of file, or if it
        doesn’t exist.