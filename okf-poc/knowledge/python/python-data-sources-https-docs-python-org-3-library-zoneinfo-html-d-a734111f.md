---
id: python-data-sources-https-docs-python-org-3-library-zoneinfo-html-d-a734111f
type: concept
title: Data sources[¶](https://docs.python.org/3/library/zoneinfo.html#data-sources
  "Link to this heading")
description: The `zoneinfo` module does not directly provide time zone data, and instead
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Data sources[¶](https://docs.python.org/3/library/zoneinfo.html#data-sources "Link to this heading")

The `zoneinfo` module does not directly provide time zone data, and instead
pulls time zone information from the system time zone database or the
first-party PyPI package [tzdata](https://pypi.org/project/tzdata/), if available. Some systems, including
notably Windows systems, do not have an IANA database available, and so for
projects targeting cross-platform compatibility that require time zone data, it
is recommended to declare a dependency on tzdata. If neither system data nor
tzdata are available, all calls to [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") will raise
[`ZoneInfoNotFoundError`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "zoneinfo.ZoneInfoNotFoundError").