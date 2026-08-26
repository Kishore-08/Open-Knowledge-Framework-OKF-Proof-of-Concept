---
id: python-the-dircmp-https-docs-python-org-3-library-filecmp-html-file-78408fbb
type: concept
title: The [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp
  "filecmp.dircmp") class[¶](https://docs.python.org/3/library/filecmp.html#the-dircmp-class
  "Link to this heading")
description: '*class* filecmp.dircmp(*a*, *b*, *ignore=None*, *hide=None*, *\**, *shallow=True*)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/filecmp.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## The [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp") class[¶](https://docs.python.org/3/library/filecmp.html#the-dircmp-class "Link to this heading")

*class* filecmp.dircmp(*a*, *b*, *ignore=None*, *hide=None*, *\**, *shallow=True*)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "Link to this definition")
:   Construct a new directory comparison object, to compare the directories *a*
    and *b*. *ignore* is a list of names to ignore, and defaults to
    [`filecmp.DEFAULT_IGNORES`](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "filecmp.DEFAULT_IGNORES"). *hide* is a list of names to hide, and
    defaults to `[os.curdir, os.pardir]`.

    The `dircmp` class compares files by doing *shallow* comparisons
    as described for [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp") by default using the *shallow*
    parameter.

    Changed in version 3.13: Added the *shallow* parameter.

    The `dircmp` class provides the following methods:

    report()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report "Link to this definition")
    :   Print (to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")) a comparison between *a* and *b*.

    report\_partial\_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_partial_closure "Link to this definition")
    :   Print a comparison between *a* and *b* and common immediate
        subdirectories.

    report\_full\_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_full_closure "Link to this definition")
    :   Print a comparison between *a* and *b* and common subdirectories
        (recursively).

    The `dircmp` class offers a number of interesting attributes that may be
    used to get various bits of information about the directory trees being
    compared.

    Note that via [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") hooks, all attributes are computed lazily,
    so there is no speed penalty if only those attributes which are lightweight
    to compute are used.

    left[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left "Link to this definition")
    :   The directory *a*.

    right[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right "Link to this definition")
    :   The directory *b*.

    left\_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_list "Link to this definition")
    :   Files and subdirectories in *a*, filtered by *hide* and *ignore*.

    right\_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_list "Link to this definition")
    :   Files and subdirectories in *b*, filtered by *hide* and *ignore*.

    common[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common "Link to this definition")
    :   Files and subdirectories in both *a* and *b*.

    left\_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_only "Link to this definition")
    :   Files and subdirectories only in *a*.

    right\_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_only "Link to this definition")
    :   Files and subdirectories only in *b*.

    common\_dirs[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_dirs "Link to this definition")
    :   Subdirectories in both *a* and *b*.

    common\_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_files "Link to this definition")
    :   Files in both *a* and *b*.

    common\_funny[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_funny "Link to this definition")
    :   Names in both *a* and *b*, such that the type differs between the
        directories, or names for which [`os.stat()`](https://docs.python.org/3