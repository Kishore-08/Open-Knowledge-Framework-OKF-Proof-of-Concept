---
id: python-globals-https-docs-python-org-3-library-zoneinfo-html-global-a734111f
type: concept
title: Globals[¶](https://docs.python.org/3/library/zoneinfo.html#globals "Link to
  this heading")
description: zoneinfo.TZPATH[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Globals[¶](https://docs.python.org/3/library/zoneinfo.html#globals "Link to this heading")

zoneinfo.TZPATH[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "Link to this definition")
:   A read-only sequence representing the time zone search path – when
    constructing a `ZoneInfo` from a key, the key is joined to each entry in
    the `TZPATH`, and the first file found is used.

    `TZPATH` may contain only absolute paths, never relative paths,
    regardless of how it is configured.

    The object that `zoneinfo.TZPATH` points to may change in response to a
    call to [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath"), so it is recommended to use
    `zoneinfo.TZPATH` rather than importing `TZPATH` from `zoneinfo` or
    assigning a long-lived variable to `zoneinfo.TZPATH`.

    For more information on configuring the time zone search path, see
    [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-configuration).