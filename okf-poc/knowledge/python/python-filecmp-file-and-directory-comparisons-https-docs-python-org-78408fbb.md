---
id: python-filecmp-file-and-directory-comparisons-https-docs-python-org-78408fbb
type: concept
title: '`filecmp` — File and Directory Comparisons[¶](https://docs.python.org/3/library/'
description: '**Source code:** [Lib/filecmp.py](https://github.com/python/cpython/tree/3.14/Lib/filecmp.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/filecmp.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `filecmp` — File and Directory Comparisons[¶](https://docs.python.org/3/library/filecmp.html#module-filecmp "Link to this heading")

**Source code:** [Lib/filecmp.py](https://github.com/python/cpython/tree/3.14/Lib/filecmp.py)

---

The `filecmp` module defines functions to compare files and directories,
with various optional time/correctness trade-offs. For comparing files,
see also the [`difflib`](https://docs.python.org/3/library/difflib.html#module-difflib "difflib: Helpers for computing differences between objects.") module.

The `filecmp` module defines the following functions:

filecmp.cmp(*f1*, *f2*, *shallow=True*)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "Link to this definition")
:   Compare the files named *f1* and *f2*, returning `True` if they seem equal,
    `False` otherwise.

    If *shallow* is true and the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") signatures (file type, size, and
    modification time) of both files are identical, the files are taken to be
    equal.

    Otherwise, the files are treated as different if their sizes or contents differ.

    Note that no external programs are called from this function, giving it
    portability and efficiency.

    This function uses a cache for past comparisons and the results,
    with cache entries invalidated if the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") information for the
    file changes. The entire cache may be cleared using [`clear_cache()`](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "filecmp.clear_cache").

filecmp.cmpfiles(*a*, *b*, *common*, *shallow=True*)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmpfiles "Link to this definition")
:   Compare the files in the two directories *a* and *b* whose names are
    given by *common*.

    Returns three lists of file names: *match*, *mismatch*,
    *errors*. *match* contains the list of files that match, *mismatch* contains
    the names of those that don’t, and *errors* lists the names of files which
    could not be compared. Files are listed in *errors* if they don’t exist in
    one of the directories, the user lacks permission to read them or if the
    comparison could not be done for some other reason.

    The *shallow* parameter has the same meaning and default value as for
    [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp").

    For example, `cmpfiles('a', 'b', ['c', 'd/e'])` will compare `a/c` with
    `b/c` and `a/d/e` with `b/d/e`. `'c'` and `'d/e'` will each be in
    one of the three returned lists.

filecmp.clear\_cache()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "Link to this definition")
:   Clear the filecmp cache. This may be useful if a file is compared so quickly
    after it is modified that it is within the mtime resolution of
    the underlying filesystem.

    Added in version 3.4.