---
id: python-files-and-directories-https-docs-python-org-3-library-os-htm-e86233c0
type: concept
title: Files and Directories[¶](https://docs.python.org/3/library/os.html#files-and-directories
  "Link to this heading")
description: On some Unix platforms, many of these functions support one or more of
  these
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Files and Directories[¶](https://docs.python.org/3/library/os.html#files-and-directories "Link to this heading")

On some Unix platforms, many of these functions support one or more of these
features:

- **specifying a file descriptor:**
  Normally the *path* argument provided to functions in the `os` module
  must be a string specifying a file path. However, some functions now
  alternatively accept an open file descriptor for their *path* argument.
  The function will then operate on the file referred to by the descriptor.
  For POSIX systems, Python will call the variant of the function prefixed
  with `f` (e.g. call `fchdir` instead of `chdir`).

  You can check whether or not *path* can be specified as a file descriptor
  for a particular function on your platform using [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd").
  If this functionality is unavailable, using it will raise a
  [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

  If the function also supports *dir\_fd* or *follow\_symlinks* arguments, it’s
  an error to specify one of those when supplying *path* as a file descriptor.

- **paths relative to directory descriptors:** If *dir\_fd* is not `None`, it
  should be a file descriptor referring to a directory, and the path to operate
  on should be relative; path will then be relative to that directory. If the
  path is absolute, *dir\_fd* is ignored. For POSIX systems, Python will call
  the variant of the function with an `at` suffix and possibly prefixed with
  `f` (e.g. call `faccessat` instead of `access`).

  You can check whether or not *dir\_fd* is supported for a particular function
  on your platform using [`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd "os.supports_dir_fd"). If it’s unavailable,
  using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

- **not following symlinks:** If *follow\_symlinks* is
  `False`, and the last element of the path to operate on is a symbolic link,
  the function will operate on the symbolic link itself rather than the file
  pointed to by the link. For POSIX systems, Python will call the `l...`
  variant of the function.

  You can check whether or not *follow\_symlinks* is supported for a particular
  function on your platform using [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks").
  If it’s unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

os.access(*path*, *mode*, *\**, *dir\_fd=None*, *effective\_ids=False*, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/os.html#os.access "Link to this definition")
:   Use the real uid/gid to test for access to *path*. Note that most operations
    will use the effective uid/gid, therefore this routine can be used in a
    suid/sgid environment to test if the invoking user has the specified access to
    *path*. *mode* should be [`F_OK`](https://docs.python.org/3/library/os.html#os.F_OK "os.F_OK") to test the existence of *path*, or it
    can be the inclusive OR of one or more of [`R_OK`](https://docs.python.org/3/library/os.html#os.R_OK "os.R_OK"), [`W_OK`](https://docs.python.org/3/library/os.html#os.W_OK "os.W_OK"), and
    [`X_OK`](https://docs.python.org/3/library/os.html#os.X_OK "os.X_OK") to test permissions. Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if access is allowed,
    [`False`](https://docs.python.org/3/library/constants.html#False "False") if not. See the Unix man page *[access(2)](https://manpages.debian.org/access(2))* for more
    information.

    This function can support specifying [paths relative to directory
    descriptors](https://docs