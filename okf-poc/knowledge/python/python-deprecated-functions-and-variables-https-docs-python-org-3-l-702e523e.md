---
id: python-deprecated-functions-and-variables-https-docs-python-org-3-l-702e523e
type: concept
title: Deprecated functions and variables[¶](https://docs.python.org/3/library/tempfile.html#deprecated-functions-and-variables
  "Link to this heading")
description: A historical way to create temporary files was to first generate a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tempfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Deprecated functions and variables[¶](https://docs.python.org/3/library/tempfile.html#deprecated-functions-and-variables "Link to this heading")

A historical way to create temporary files was to first generate a
file name with the [`mktemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mktemp "tempfile.mktemp") function and then create a file
using this name. Unfortunately this is not secure, because a different
process may create a file with this name in the time between the call
to `mktemp()` and the subsequent attempt to create the file by the
first process. The solution is to combine the two steps and create the
file immediately. This approach is used by [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp") and the
other functions described above.

tempfile.mktemp(*suffix=''*, *prefix='tmp'*, *dir=None*)[¶](https://docs.python.org/3/library/tempfile.html#tempfile.mktemp "Link to this definition")
:   Deprecated since version 2.3: Use [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp") instead.

    Return an absolute pathname of a file that did not exist at the time the
    call is made. The *prefix*, *suffix*, and *dir* arguments are similar
    to those of [`mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp"), except that bytes file names, `suffix=None`
    and `prefix=None` are not supported.

    Warning

    Use of this function may introduce a security hole in your program. By
    the time you get around to doing anything with the file name it returns,
    someone else may have beaten you to the punch. `mktemp()` usage can
    be replaced easily with [`NamedTemporaryFile()`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile "tempfile.NamedTemporaryFile"), passing it the
    `delete=False` parameter:

    ```
    >>> f = NamedTemporaryFile(delete=False)
    >>> f.name
    '/tmp/tmptjujjt'
    >>> f.write(b"Hello World!\n")
    13
    >>> f.close()
    >>> os.unlink(f.name)
    >>> os.path.exists(f.name)
    False
    ```