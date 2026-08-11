---
id: python-zoneinfo-iana-time-zone-support-https-docs-python-org-3-libr-a734111f
type: concept
title: '`zoneinfo` — IANA time zone support[¶](https://docs.python.org/3/library/zoneinf'
description: Added in version 3.9.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `zoneinfo` — IANA time zone support[¶](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "Link to this heading")

Added in version 3.9.

**Source code:** [Lib/zoneinfo](https://github.com/python/cpython/tree/3.14/Lib/zoneinfo)

---

The `zoneinfo` module provides a concrete time zone implementation to
support the IANA time zone database as originally specified in [**PEP 615**](https://peps.python.org/pep-0615/). By
default, `zoneinfo` uses the system’s time zone data if available; if no
system time zone data is available, the library will fall back to using the
first-party [tzdata](https://pypi.org/project/tzdata/) package available on PyPI.

See also

Module: [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
:   Provides the [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
    types with which the [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") class is designed to be used.

Package [tzdata](https://pypi.org/project/tzdata/)
:   First-party package maintained by the CPython core developers to supply
    time zone data via PyPI.

[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.