---
id: python-permissions-and-ownership-https-docs-python-org-3-library-pa-e66b1645
type: concept
title: Permissions and ownership[¶](https://docs.python.org/3/library/pathlib.html#permissions-and-ownership
  "Link to this heading")
description: Path.owner(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Permissions and ownership[¶](https://docs.python.org/3/library/pathlib.html#permissions-and-ownership "Link to this heading")

Path.owner(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner "Link to this definition")
:   Return the name of the user owning the file. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised
    if the file’s user identifier (UID) isn’t found in the system database.

    This method normally follows symlinks; to get the owner of the symlink, add
    the argument `follow_symlinks=False`.

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") if the [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends).") module is not
    available. In earlier versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised.

    Changed in version 3.13: The *follow\_symlinks* parameter was added.

Path.group(*\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.group "Link to this definition")
:   Return the name of the group owning the file. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised
    if the file’s group identifier (GID) isn’t found in the system database.

    This method normally follows symlinks; to get the group of the symlink, add
    the argument `follow_symlinks=False`.

    Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") if the [`grp`](https://docs.python.org/3/library/grp.html#module-grp "grp: The group database (getgrnam() and friends).") module is not
    available. In earlier versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised.

    Changed in version 3.13: The *follow\_symlinks* parameter was added.

Path.chmod(*mode*, *\**, *follow\_symlinks=True*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod "Link to this definition")
:   Change the file mode and permissions, like [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod").

    This method normally follows symlinks. Some Unix flavours support changing
    permissions on the symlink itself; on these platforms you may add the
    argument `follow_symlinks=False`, or use [`lchmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lchmod "pathlib.Path.lchmod").

    ```
    >>> p = Path('setup.py')
    >>> p.stat().st_mode
    33277
    >>> p.chmod(0o444)
    >>> p.stat().st_mode
    33060
    ```

    Changed in version 3.10: The *follow\_symlinks* parameter was added.

Path.lchmod(*mode*)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lchmod "Link to this definition")
:   Like [`Path.chmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod "pathlib.Path.chmod") but, if the path points to a symbolic link, the
    symbolic link’s mode is changed rather than its target’s.