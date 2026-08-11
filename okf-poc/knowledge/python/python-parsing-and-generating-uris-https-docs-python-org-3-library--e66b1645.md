---
id: python-parsing-and-generating-uris-https-docs-python-org-3-library--e66b1645
type: concept
title: Parsing and generating URIs[¶](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris
  "Link to this heading")
description: Concrete path objects can be created from, and represented as, ‘file’
  URIs
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Parsing and generating URIs[¶](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris "Link to this heading")

Concrete path objects can be created from, and represented as, ‘file’ URIs
conforming to [**RFC 8089**](https://datatracker.ietf.org/doc/html/rfc8089.html).

Note

File URIs are not portable across machines with different
[filesystem encodings](https://docs.python.org/3/library/os.html#filesystem-encoding).

*classmethod* Path.from\_uri(*uri*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.from_uri "Link to this definition")
:   Return a new path object from parsing a ‘file’ URI. For example:

    ```
    >>> p = Path.from_uri('file:///etc/hosts')
    PosixPath('/etc/hosts')
    ```

    On Windows, DOS device and UNC paths may be parsed from URIs:

    ```
    >>> p = Path.from_uri('file:///c:/windows')
    WindowsPath('c:/windows')
    >>> p = Path.from_uri('file://server/share')
    WindowsPath('//server/share')
    ```

    Several variant forms are supported:

    ```
    >>> p = Path.from_uri('file:////server/share')
    WindowsPath('//server/share')
    >>> p = Path.from_uri('file://///server/share')
    WindowsPath('//server/share')
    >>> p = Path.from_uri('file:c:/windows')
    WindowsPath('c:/windows')
    >>> p = Path.from_uri('file:/c|/windows')
    WindowsPath('c:/windows')
    ```

    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the URI does not start with `file:`, or
    the parsed path isn’t absolute.

    Added in version 3.13.

    Changed in version 3.14: The URL authority is discarded if it matches the local hostname.
    Otherwise, if the authority isn’t empty or `localhost`, then on
    Windows a UNC path is returned (as before), and on other platforms a
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

Path.as\_uri()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.as_uri "Link to this definition")
:   Represent the path as a ‘file’ URI. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if
    the path isn’t absolute.

    ```
    >>> p = PosixPath('/etc/passwd')
    >>> p.as_uri()
    'file:///etc/passwd'
    >>> p = WindowsPath('c:/Windows')
    >>> p.as_uri()
    'file:///c:/Windows'
    ```

    Deprecated since version 3.14, will be removed in version 3.19: Calling this method from [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") rather than [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") is
    possible but deprecated. The method’s use of [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") makes
    it strictly impure.