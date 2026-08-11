---
id: python-exceptions-and-warnings-https-docs-python-org-3-library-zone-a734111f
type: concept
title: Exceptions and warnings[¶](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings
  "Link to this heading")
description: '*exception* zoneinfo.ZoneInfoNotFoundError[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Exceptions and warnings[¶](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings "Link to this heading")

*exception* zoneinfo.ZoneInfoNotFoundError[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "Link to this definition")
:   Raised when construction of a [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") object fails because the
    specified key could not be found on the system. This is a subclass of
    [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError").

*exception* zoneinfo.InvalidTZPathWarning[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.InvalidTZPathWarning "Link to this definition")
:   Raised when [`PYTHONTZPATH`](https://docs.python.org/3/library/zoneinfo.html#envvar-PYTHONTZPATH) contains an invalid component that will
    be filtered out, such as a relative path.