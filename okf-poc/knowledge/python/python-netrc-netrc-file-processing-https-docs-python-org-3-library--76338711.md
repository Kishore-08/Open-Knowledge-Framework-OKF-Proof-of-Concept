---
id: python-netrc-netrc-file-processing-https-docs-python-org-3-library--76338711
type: concept
title: '`netrc` — netrc file processing[¶](https://docs.python.org/3/library/netrc.html#'
description: '**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.14/Lib/netrc.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/netrc.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `netrc` — netrc file processing[¶](https://docs.python.org/3/library/netrc.html#module-netrc "Link to this heading")

**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.14/Lib/netrc.py)

---

The [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc") class parses and encapsulates the netrc file format used by
the Unix **ftp** program and other FTP clients.

*class* netrc.netrc([*file*])[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc "Link to this definition")
:   A `netrc` instance or subclass instance encapsulates data from a netrc
    file. The initialization argument, if present, specifies the file to parse. If
    no argument is given, the file `.netrc` in the user’s home directory –
    as determined by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") – will be read. Otherwise,
    a [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") exception will be raised.
    Parse errors will raise [`NetrcParseError`](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "netrc.NetrcParseError") with diagnostic
    information including the file name, line number, and terminating token.

    If no argument is specified on a POSIX system, the presence of passwords in
    the `.netrc` file will raise a [`NetrcParseError`](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "netrc.NetrcParseError") if the file
    ownership or permissions are insecure (owned by a user other than the user
    running the process, or accessible for read or write by any other user).
    This implements security behavior equivalent to that of ftp and other
    programs that use `.netrc`. Such security checks are not available
    on platforms that do not support [`os.getuid()`](https://docs.python.org/3/library/os.html#os.getuid "os.getuid").

    Changed in version 3.4: Added the POSIX permission check.

    Changed in version 3.7: [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") is used to find the location of the
    `.netrc` file when *file* is not passed as argument.

    Changed in version 3.10: `netrc` try UTF-8 encoding before using locale specific
    encoding.
    The entry in the netrc file no longer needs to contain all tokens. The missing
    tokens’ value default to an empty string. All the tokens and their values now
    can contain arbitrary characters, like whitespace and non-ASCII characters.
    If the login name is anonymous, it won’t trigger the security check.

*exception* netrc.NetrcParseError[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "Link to this definition")
:   Exception raised by the [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc") class when syntactical errors are
    encountered in source text. Instances of this exception provide three
    interesting attributes:

    msg[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.msg "Link to this definition")
    :   Textual explanation of the error.

    filename[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.filename "Link to this definition")
    :   The name of the source file.

    lineno[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.lineno "Link to this definition")
    :   The line number on which the error was found.