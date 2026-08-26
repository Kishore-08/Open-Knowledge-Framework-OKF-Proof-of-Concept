---
id: python-ios-platform-https-docs-python-org-3-library-platform-html-i-8418a7a3
type: concept
title: iOS platform[¶](https://docs.python.org/3/library/platform.html#ios-platform
  "Link to this heading")
description: platform.ios\_ver(*system=''*, *release=''*, *model=''*, *is\_simulator=False*)[¶](https://docs.python.org/3/library/platform.html#platform.ios_ver
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## iOS platform[¶](https://docs.python.org/3/library/platform.html#ios-platform "Link to this heading")

platform.ios\_ver(*system=''*, *release=''*, *model=''*, *is\_simulator=False*)[¶](https://docs.python.org/3/library/platform.html#platform.ios_ver "Link to this definition")
:   Get iOS version information and return it as a
    [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") with the following attributes:

    - `system` is the OS name; either `'iOS'` or `'iPadOS'`.
    - `release` is the iOS version number as a string (e.g., `'17.2'`).
    - `model` is the device model identifier; this will be a string like
      `'iPhone13,2'` for a physical device, or `'iPhone'` on a simulator.
    - `is_simulator` is a boolean describing if the app is running on a
      simulator or a physical device.

    Entries which cannot be determined are set to the defaults given as
    parameters.