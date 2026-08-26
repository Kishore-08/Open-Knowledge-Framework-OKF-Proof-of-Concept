---
id: python-file-descriptor-operations-https-docs-python-org-3-library-o-e86233c0
type: concept
title: File Descriptor Operations[¶](https://docs.python.org/3/library/os.html#file-descriptor-operations
  "Link to this heading")
description: These functions operate on I/O streams referenced using file descriptors.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## File Descriptor Operations[¶](https://docs.python.org/3/library/os.html#file-descriptor-operations "Link to this heading")

These functions operate on I/O streams referenced using file descriptors.

File descriptors are small integers corresponding to a file that has been opened
by the current process. For example, standard input is usually file descriptor
0, standard output is 1, and standard error is 2. Further files opened by a
process will then be assigned 3, 4, 5, and so forth. The name “file descriptor”
is slightly deceptive; on Unix platforms, sockets and pipes are also referenced
by file descriptors.

The [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method can be used to obtain the file descriptor
associated with a [file object](https://docs.python.org/3/glossary.html#term-file-object) when required. Note that using the file
descriptor directly will bypass the file object methods, ignoring aspects such
as internal buffering of data.

os.close(*fd*)[¶](https://docs.python.org/3/library/os.html#os.close "Link to this definition")
:   Close file descriptor *fd*.

    Note

    This function is intended for low-level I/O and must be applied to a file
    descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe"). To close a “file
    object” returned by the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open") or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or
    [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen"), use its [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method.

os.closerange(*fd\_low*, *fd\_high*, */*)[¶](https://docs.python.org/3/library/os.html#os.closerange "Link to this definition")
:   Close all file descriptors from *fd\_low* (inclusive) to *fd\_high* (exclusive),
    ignoring errors. Equivalent to (but much faster than):

    ```
    for fd in range(fd_low, fd_high):
        try:
            os.close(fd)
        except OSError:
            pass
    ```

os.copy\_file\_range(*src*, *dst*, *count*, *offset\_src=None*, *offset\_dst=None*)[¶](https://docs.python.org/3/library/os.html#os.copy_file_range "Link to this definition")
:   Copy *count* bytes from file descriptor *src*, starting from offset
    *offset\_src*, to file descriptor *dst*, starting from offset *offset\_dst*.
    If *offset\_src* is `None`, then *src* is read from the current position;
    respectively for *offset\_dst*.

    In Linux kernel older than 5.3, the files pointed to by *src* and *dst*
    must reside in the same filesystem, otherwise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is
    raised with [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") set to [`errno.EXDEV`](https://docs.python.org/3/library/errno.html#errno.EXDEV "errno.EXDEV").

    This copy is done without the additional cost of transferring data
    from the kernel to user space and then back into the kernel. Additionally,
    some filesystems could implement extra optimizations, such as the use of
    reflinks (i.e., two or more inodes that share pointers to the same
    copy-on-write disk blocks; supported file systems include btrfs and XFS)
    and server-side copy (in the case of NFS).

    The function copies bytes between two file descriptors. Text options, like
    the encoding and the line ending, are ignored.

    The return value is the amount of bytes copied. This could be less than the
    amount requested.

    Note

    On Linux, `os.copy_file_range()` should not be used for copying a
    range of a pseudo file from a special filesystem like procfs and sysfs.
    It will always copy no bytes and return 0 as if the file was empty
    because of a known Linux kernel