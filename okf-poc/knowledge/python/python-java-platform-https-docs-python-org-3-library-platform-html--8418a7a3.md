---
id: python-java-platform-https-docs-python-org-3-library-platform-html--8418a7a3
type: concept
title: Java platform[¶](https://docs.python.org/3/library/platform.html#java-platform
  "Link to this heading")
description: platform.java\_ver(*release=''*, *vendor=''*, *vminfo=('', '', '')*,
  *osinfo=('', '', '')*)[¶](https://docs.python.org/3/library/platform.html#platform.java_ver
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Java platform[¶](https://docs.python.org/3/library/platform.html#java-platform "Link to this heading")

platform.java\_ver(*release=''*, *vendor=''*, *vminfo=('', '', '')*, *osinfo=('', '', '')*)[¶](https://docs.python.org/3/library/platform.html#platform.java_ver "Link to this definition")
:   Version interface for Jython.

    Returns a tuple `(release, vendor, vminfo, osinfo)` with *vminfo* being a
    tuple `(vm_name, vm_release, vm_vendor)` and *osinfo* being a tuple
    `(os_name, os_version, os_arch)`. Values which cannot be determined are set to
    the defaults given as parameters (which all default to `''`).

    Deprecated since version 3.13, will be removed in version 3.15: It was largely untested, had a confusing API,
    and was only useful for Jython support.