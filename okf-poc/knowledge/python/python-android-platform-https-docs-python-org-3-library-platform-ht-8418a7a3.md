---
id: python-android-platform-https-docs-python-org-3-library-platform-ht-8418a7a3
type: concept
title: Android platform[¶](https://docs.python.org/3/library/platform.html#android-platform
  "Link to this heading")
description: platform.android\_ver(*release=''*, *api\_level=0*, *manufacturer=''*,
  *model=''*, *device=''*, *is\_emulator=False*)[¶](https://docs.python.org/3/library/platform.html#platform.android_ver
  "Link to t
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Android platform[¶](https://docs.python.org/3/library/platform.html#android-platform "Link to this heading")

platform.android\_ver(*release=''*, *api\_level=0*, *manufacturer=''*, *model=''*, *device=''*, *is\_emulator=False*)[¶](https://docs.python.org/3/library/platform.html#platform.android_ver "Link to this definition")
:   Get Android device information. Returns a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
    with the following attributes. Values which cannot be determined are set to
    the defaults given as parameters.

    - `release` - Android version, as a string (e.g. `"14"`).
    - `api_level` - API level of the running device, as an integer (e.g. `34`
      for Android 14). To get the API level which Python was built against, see
      [`sys.getandroidapilevel()`](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "sys.getandroidapilevel").
    - `manufacturer` - [Manufacturer name](https://developer.android.com/reference/android/os/Build#MANUFACTURER).
    - `model` - [Model name](https://developer.android.com/reference/android/os/Build#MODEL) –
      typically the marketing name or model number.
    - `device` - [Device name](https://developer.android.com/reference/android/os/Build#DEVICE) –
      typically the model number or a codename.
    - `is_emulator` - `True` if the device is an emulator; `False` if it’s
      a physical device.

    Google maintains a [list of known model and device names](https://storage.googleapis.com/play_public/supported_devices.html).

    Added in version 3.13.