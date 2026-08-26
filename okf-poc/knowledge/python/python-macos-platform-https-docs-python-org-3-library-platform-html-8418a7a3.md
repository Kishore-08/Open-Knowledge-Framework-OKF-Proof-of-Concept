---
id: python-macos-platform-https-docs-python-org-3-library-platform-html-8418a7a3
type: concept
title: macOS platform[¶](https://docs.python.org/3/library/platform.html#macos-platform
  "Link to this heading")
description: platform.mac\_ver(*release=''*, *versioninfo=('', '', '')*, *machine=''*)[¶](https://docs.python.org/3/library/platform.html#platform.mac_ver
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## macOS platform[¶](https://docs.python.org/3/library/platform.html#macos-platform "Link to this heading")

platform.mac\_ver(*release=''*, *versioninfo=('', '', '')*, *machine=''*)[¶](https://docs.python.org/3/library/platform.html#platform.mac_ver "Link to this definition")
:   Get macOS version information and return it as tuple `(release, versioninfo,
    machine)` with *versioninfo* being a tuple `(version, dev_stage,
    non_release_version)`.

    Entries which cannot be determined are set to `''`. All tuple entries are
    strings.