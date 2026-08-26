---
id: python-concrete-paths-https-docs-python-org-3-library-pathlib-html--e66b1645
type: concept
title: Concrete paths[¶](https://docs.python.org/3/library/pathlib.html#concrete-paths
  "Link to this heading")
description: Concrete paths are subclasses of the pure path classes. In addition to
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Concrete paths[¶](https://docs.python.org/3/library/pathlib.html#concrete-paths "Link to this heading")

Concrete paths are subclasses of the pure path classes. In addition to
operations provided by the latter, they also provide methods to do system
calls on path objects. There are three ways to instantiate concrete paths:

*class* pathlib.Path(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path "Link to this definition")
:   A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this class represents concrete paths of
    the system’s path flavour (instantiating it creates either a
    [`PosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "pathlib.PosixPath") or a [`WindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath "pathlib.WindowsPath")):

    ```
    >>> Path('setup.py')
    PosixPath('setup.py')
    ```

    *pathsegments* is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

*class* pathlib.PosixPath(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "Link to this definition")
:   A subclass of [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") and [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath"), this class
    represents concrete non-Windows filesystem paths:

    ```
    >>> PosixPath('/etc/hosts')
    PosixPath('/etc/hosts')
    ```

    *pathsegments* is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") on Windows. In previous versions,
    [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised instead.

*class* pathlib.WindowsPath(*\*pathsegments*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath "Link to this definition")
:   A subclass of [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") and [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath"), this class
    represents concrete Windows filesystem paths:

    ```
    >>> WindowsPath('c:/', 'Users', 'Ximénez')
    WindowsPath('c:/Users/Ximénez')
    ```

    *pathsegments* is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") on non-Windows platforms. In previous
    versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised instead.

You can only instantiate the class flavour that corresponds to your system
(allowing system calls on non-compatible path flavours could lead to
bugs or failures in your application):

```
>>> import os
>>> os.name
'posix'
>>> Path('setup.py')
PosixPath('setup.py')
>>> PosixPath('setup.py')
PosixPath('setup.py')
>>> WindowsPath('setup.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 798, in __new__
    % (cls.__name__,))
UnsupportedOperation: cannot instantiate 'WindowsPath' on your system
```

Some concrete path methods can raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if a system call fails
(for example because the path doesn’t exist).