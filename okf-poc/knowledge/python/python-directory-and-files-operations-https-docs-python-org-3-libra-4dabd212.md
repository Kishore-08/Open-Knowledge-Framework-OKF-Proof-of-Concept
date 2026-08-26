---
id: python-directory-and-files-operations-https-docs-python-org-3-libra-4dabd212
type: concept
title: Directory and files operations[¶](https://docs.python.org/3/library/shutil.html#directory-and-files-operations
  "Link to this heading")
description: shutil.copyfileobj(*fsrc*, *fdst*[, *length*])[¶](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Directory and files operations[¶](https://docs.python.org/3/library/shutil.html#directory-and-files-operations "Link to this heading")

shutil.copyfileobj(*fsrc*, *fdst*[, *length*])[¶](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "Link to this definition")
:   Copy the contents of the [file-like object](https://docs.python.org/3/glossary.html#term-file-object) *fsrc* to the file-like object *fdst*.
    The integer *length*, if given, is the buffer size. In particular, a negative
    *length* value means to copy the data without looping over the source data in
    chunks; by default the data is read in chunks to avoid uncontrolled memory
    consumption. Note that if the current file position of the *fsrc* object is not
    0, only the contents from the current file position to the end of the file will
    be copied.

    `copyfileobj()` will *not* guarantee that the destination stream has
    been flushed on completion of the copy. If you want to read from the
    destination at the completion of the copy operation (for example, reading
    the contents of a temporary file that has been copied from a HTTP stream),
    you must ensure that you have called [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush") or
    [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") on the file-like object before attempting to read
    the destination file.

shutil.copyfile(*src*, *dst*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/shutil.html#shutil.copyfile "Link to this definition")
:   Copy the contents (no metadata) of the file named *src* to a file named
    *dst* and return *dst* in the most efficient way possible.
    *src* and *dst* are [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) or path names given as strings.

    *dst* must be the complete target file name; look at [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy")
    for a copy that accepts a target directory path. If *src* and *dst*
    specify the same file, [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError") is raised.

    The destination location must be writable; otherwise, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")
    exception will be raised. If *dst* already exists, it will be replaced.
    Special files such as character or block devices and pipes cannot be
    copied with this function.

    If *follow\_symlinks* is false and *src* is a symbolic link,
    a new symbolic link will be created instead of copying the
    file *src* points to.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.

    Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised instead of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
    Added *follow\_symlinks* argument.
    Now returns *dst*.

    Changed in version 3.4: Raise [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError") instead of [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error"). Since the former is
    a subclass of the latter, this change is backward compatible.

    Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to
    copy the file more efficiently. See
    [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.

*exception* shutil.SpecialFileError[¶](https://docs.python.org/3/library/shutil.html#shutil.SpecialFileError "Link to this definition")
:   This exception is raised when [`copyfile()`](https://docs.python.org/3/library/shutil.ht