---
id: python-linux-platforms-https-docs-python-org-3-library-platform-htm-8418a7a3
type: concept
title: Linux platforms[¶](https://docs.python.org/3/library/platform.html#linux-platforms
  "Link to this heading")
description: platform.freedesktop\_os\_release()[¶](https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Linux platforms[¶](https://docs.python.org/3/library/platform.html#linux-platforms "Link to this heading")

platform.freedesktop\_os\_release()[¶](https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release "Link to this definition")
:   Get operating system identification from `os-release` file and return
    it as a dict. The `os-release` file is a [freedesktop.org standard](https://www.freedesktop.org/software/systemd/man/os-release.html) and
    is available in most Linux distributions. A noticeable exception is
    Android and Android-based distributions.

    Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") or subclass when neither `/etc/os-release` nor
    `/usr/lib/os-release` can be read.

    On success, the function returns a dictionary where keys and values are
    strings. Values have their special characters like `"` and `$`
    unquoted. The fields `NAME`, `ID`, and `PRETTY_NAME` are always
    defined according to the standard. All other fields are optional. Vendors
    may include additional fields.

    Note that fields like `NAME`, `VERSION`, and `VARIANT` are strings
    suitable for presentation to users. Programs should use fields like
    `ID`, `ID_LIKE`, `VERSION_ID`, or `VARIANT_ID` to identify
    Linux distributions.

    Example:

    ```
    def get_like_distro():
        info = platform.freedesktop_os_release()
        ids = [info["ID"]]
        if "ID_LIKE" in info:
            # ids are space separated and ordered by precedence
            ids.extend(info["ID_LIKE"].split())
        return ids
    ```

    Added in version 3.10.