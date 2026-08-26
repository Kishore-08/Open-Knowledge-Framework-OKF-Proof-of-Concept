---
id: python-accessing-individual-parts-https-docs-python-org-3-library-p-e66b1645
type: concept
title: Accessing individual parts[¶](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts
  "Link to this heading")
description: To access the individual “parts” (components) of a path, use the following
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Accessing individual parts[¶](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts "Link to this heading")

To access the individual “parts” (components) of a path, use the following
property:

PurePath.parts[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parts "Link to this definition")
:   A tuple giving access to the path’s various components:

    ```
    >>> p = PurePath('/usr/bin/python3')
    >>> p.parts
    ('/', 'usr', 'bin', 'python3')

    >>> p = PureWindowsPath('c:/Program Files/PSF')
    >>> p.parts
    ('c:\\', 'Program Files', 'PSF')
    ```

    (note how the drive and local root are regrouped in a single part)