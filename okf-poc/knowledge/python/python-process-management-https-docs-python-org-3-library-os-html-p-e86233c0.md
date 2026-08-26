---
id: python-process-management-https-docs-python-org-3-library-os-html-p-e86233c0
type: concept
title: Process Management[¶](https://docs.python.org/3/library/os.html#process-management
  "Link to this heading")
description: These functions may be used to create and manage processes.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Process Management[¶](https://docs.python.org/3/library/os.html#process-management "Link to this heading")

These functions may be used to create and manage processes.

The various [`exec*`](https://docs.python.org/3/library/os.html#os.execl "os.execl") functions take a list of arguments for the new
program loaded into the process. In each case, the first of these arguments is
passed to the new program as its own name rather than as an argument a user may
have typed on a command line. For the C programmer, this is the `argv[0]`
passed to a program’s `main()`. For example, `os.execv('/bin/echo',
['foo', 'bar'])` will only print `bar` on standard output; `foo` will seem
to be ignored.

os.abort()[¶](https://docs.python.org/3/library/os.html#os.abort "Link to this definition")
:   Generate a `SIGABRT` signal to the current process. On Unix, the default
    behavior is to produce a core dump; on Windows, the process immediately returns
    an exit code of `3`. Be aware that calling this function will not call the
    Python signal handler registered for `SIGABRT` with
    [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal").

os.add\_dll\_directory(*path*)[¶](https://docs.python.org/3/library/os.html#os.add_dll_directory "Link to this definition")
:   Add a path to the DLL search path.

    This search path is used when resolving dependencies for imported
    extension modules (the module itself is resolved through
    [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")), and also by [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.").

    Remove the directory by calling **close()** on the returned object
    or using it in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.

    See the [Microsoft documentation](https://msdn.microsoft.com/44228cf2-6306-466c-8f16-f513cd3ba8b5)
    for more information about how DLLs are loaded.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.add_dll_directory` with argument `path`.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

    Added in version 3.8: Previous versions of CPython would resolve DLLs using the default
    behavior for the current process. This led to inconsistencies,
    such as only sometimes searching `PATH` or the current
    working directory, and OS functions such as `AddDllDirectory`
    having no effect.

    In 3.8, the two primary ways DLLs are loaded now explicitly
    override the process-wide behavior to ensure consistency. See the
    [porting notes](https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew) for information on
    updating libraries.

os.execl(*path*, *arg0*, *arg1*, *...*)[¶](https://docs.python.org/3/library/os.html#os.execl "Link to this definition")

os.execle(*path*, *arg0*, *arg1*, *...*, *env*)[¶](https://docs.python.org/3/library/os.html#os.execle "Link to this definition")

os.execlp(*file*, *arg0*, *arg1*, *...*)[¶](https://docs.python.org/3/library/os.html#os.execlp "Link to this definition")

os.execlpe(*file*, *arg0*, *arg1*, *...*, *env*)[¶](https://docs.python.org/3/library/os.html#os.execlpe "Link to this definition")

os.execv(*path*, *args*)[¶](https://docs.python.org/3/library/os.html#os.execv "Link to this definition")

os.execve(*path*, *args*, *env*)[¶](https://docs.python.org/3/library/os.html#os.execve "Link to this definition")

os.execvp(*file*, *args*)[¶](https://docs.python.org/3/library/os.html#os.execvp "Link to this definition")

os.execvpe(*file*, *args*, *env*)[¶](https://docs.python.org/3/library/os.html#os.execvpe "Link to this definition")
:   These functions all execute a new program, replacing the current process; they
    do not return. On Unix, the new executable is loaded into the current process,
    and will have the same process id as the caller. Err