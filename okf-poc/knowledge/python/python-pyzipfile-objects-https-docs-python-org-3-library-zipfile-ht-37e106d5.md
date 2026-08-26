---
id: python-pyzipfile-objects-https-docs-python-org-3-library-zipfile-ht-37e106d5
type: concept
title: PyZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects
  "Link to this heading")
description: The [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile
  "zipfile.PyZipFile") constructor takes the same parameters as the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## PyZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects "Link to this heading")

The [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "zipfile.PyZipFile") constructor takes the same parameters as the
[`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") constructor, and one additional parameter, *optimize*.

*class* zipfile.PyZipFile(*file*, *mode='r'*, *compression=ZIP\_STORED*, *allowZip64=True*, *optimize=-1*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "Link to this definition")
:   Changed in version 3.2: Added the *optimize* parameter.

    Changed in version 3.4: ZIP64 extensions are enabled by default.

    Instances have one method in addition to those of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") objects:

    writepy(*pathname*, *basename=''*, *filterfunc=None*)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile.writepy "Link to this definition")
    :   Search for files `*.py` and add the corresponding file to the
        archive.

        If the *optimize* parameter to `PyZipFile` was not given or `-1`,
        the corresponding file is a `*.pyc` file, compiling if necessary.

        If the *optimize* parameter to `PyZipFile` was `0`, `1` or
        `2`, only files with that optimization level (see [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile")) are
        added to the archive, compiling if necessary.

        If *pathname* is a file, the filename must end with `.py`, and
        just the (corresponding `*.pyc`) file is added at the top level
        (no path information). If *pathname* is a file that does not end with
        `.py`, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") will be raised. If it is a directory,
        and the directory is not a package directory, then all the files
        `*.pyc` are added at the top level. If the directory is a
        package directory, then all `*.pyc` are added under the package
        name as a file path, and if any subdirectories are package directories,
        all of these are added recursively in sorted order.

        *basename* is intended for internal use only.

        *filterfunc*, if given, must be a function taking a single string
        argument. It will be passed each path (including each individual full
        file path) before it is added to the archive. If *filterfunc* returns a
        false value, the path will not be added, and if it is a directory its
        contents will be ignored. For example, if our test files are all either
        in `test` directories or start with the string `test_`, we can use a
        *filterfunc* to exclude them:

        ```
        >>> zf = PyZipFile('myprog.zip')
        >>> def notests(s):
        ...     fn = os.path.basename(s)
        ...     return (not (fn == 'test' or fn.startswith('test_')))
        ...
        >>> zf.writepy('myprog', filterfunc=notests)
        ```

        The `writepy()` method makes archives with file names like
        this:

        ```
        string.pyc                   # Top level name
        test/__init__.pyc            # Package directory
        test/testall.pyc             # Module test.testall
        test/bogus/__init__.pyc      # Subpackage directory
        test/bogus/myfile.pyc        # Submodule test.bogus.myfile
        ```

        Changed in version 3.4: Added the *filterfunc* parameter.

        Changed in version 3.6.2: The *pathname* parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

        Changed in version 3.7: Recursion sorts directory entries.