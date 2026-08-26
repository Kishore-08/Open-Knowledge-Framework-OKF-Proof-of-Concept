---
id: python-windows-platform-https-docs-python-org-3-library-platform-ht-8418a7a3
type: concept
title: Windows platform[¶](https://docs.python.org/3/library/platform.html#windows-platform
  "Link to this heading")
description: platform.win32\_ver(*release=''*, *version=''*, *csd=''*, *ptype=''*)[¶](https://docs.python.org/3/library/platform.html#platform.win32_ver
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Windows platform[¶](https://docs.python.org/3/library/platform.html#windows-platform "Link to this heading")

platform.win32\_ver(*release=''*, *version=''*, *csd=''*, *ptype=''*)[¶](https://docs.python.org/3/library/platform.html#platform.win32_ver "Link to this definition")
:   Get additional version information from the Windows Registry and return a tuple
    `(release, version, csd, ptype)` referring to OS release, version number,
    CSD level (service pack) and OS type (multi/single processor). Values which
    cannot be determined are set to the defaults given as parameters (which all
    default to an empty string).

    As a hint: *ptype* is `'Uniprocessor Free'` on single processor NT machines
    and `'Multiprocessor Free'` on multi processor machines. The `'Free'` refers
    to the OS version being free of debugging code. It could also state `'Checked'`
    which means the OS version uses debugging code, i.e. code that checks arguments,
    ranges, etc.

platform.win32\_edition()[¶](https://docs.python.org/3/library/platform.html#platform.win32_edition "Link to this definition")
:   Returns a string representing the current Windows edition, or `None` if the
    value cannot be determined. Possible values include but are not limited to
    `'Enterprise'`, `'IoTUAP'`, `'ServerStandard'`, and `'nanoserver'`.

    Added in version 3.8.

platform.win32\_is\_iot()[¶](https://docs.python.org/3/library/platform.html#platform.win32_is_iot "Link to this definition")
:   Return `True` if the Windows edition returned by [`win32_edition()`](https://docs.python.org/3/library/platform.html#platform.win32_edition "platform.win32_edition")
    is recognized as an IoT edition.

    Added in version 3.8.