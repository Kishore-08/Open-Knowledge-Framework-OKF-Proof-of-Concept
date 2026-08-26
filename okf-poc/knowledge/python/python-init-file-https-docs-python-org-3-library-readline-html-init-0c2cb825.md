---
id: python-init-file-https-docs-python-org-3-library-readline-html-init-0c2cb825
type: concept
title: Init file[¶](https://docs.python.org/3/library/readline.html#init-file "Link
  to this heading")
description: 'The following functions relate to the init file and user configuration:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Init file[¶](https://docs.python.org/3/library/readline.html#init-file "Link to this heading")

The following functions relate to the init file and user configuration:

readline.parse\_and\_bind(*string*)[¶](https://docs.python.org/3/library/readline.html#readline.parse_and_bind "Link to this definition")
:   Execute the init line provided in the *string* argument. This calls
    `rl_parse_and_bind()` in the underlying library.

readline.read\_init\_file([*filename*])[¶](https://docs.python.org/3/library/readline.html#readline.read_init_file "Link to this definition")
:   Execute a readline initialization file. The default filename is the last filename
    used. This calls `rl_read_init_file()` in the underlying library.
    It raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name
    if given, and `"<readline_init_file>"` otherwise, regardless of
    which file the library resolves.

    Changed in version 3.14: The auditing event was added.