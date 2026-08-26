---
id: python-functions-https-docs-python-org-3-library-zoneinfo-html-func-a734111f
type: concept
title: Functions[¶](https://docs.python.org/3/library/zoneinfo.html#functions "Link
  to this heading")
description: zoneinfo.available\_timezones()[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Functions[¶](https://docs.python.org/3/library/zoneinfo.html#functions "Link to this heading")

zoneinfo.available\_timezones()[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones "Link to this definition")
:   Get a set containing all the valid keys for IANA time zones available
    anywhere on the time zone path. This is recalculated on every call to the
    function.

    This function only includes canonical zone names and does not include
    “special” zones such as those under the `posix/` and `right/`
    directories, or the `posixrules` zone.

    Caution

    This function may open a large number of files, as the best way to
    determine if a file on the time zone path is a valid time zone is to
    read the “magic string” at the beginning.

    Note

    These values are not designed to be exposed to end-users; for user
    facing elements, applications should use something like CLDR (the
    Unicode Common Locale Data Repository) to get more user-friendly
    strings. See also the cautionary note on [`ZoneInfo.key`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key "zoneinfo.ZoneInfo.key").

zoneinfo.reset\_tzpath(*to=None*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "Link to this definition")
:   Sets or resets the time zone search path ([`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH")) for the module.
    When called with no arguments, `TZPATH` is set to the default value.

    Calling `reset_tzpath` will not invalidate the [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") cache,
    and so calls to the primary `ZoneInfo` constructor will only use the new
    `TZPATH` in the case of a cache miss.

    The `to` parameter must be a [sequence](https://docs.python.org/3/glossary.html#term-sequence) of strings or
    [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") and not a string, all of which must be absolute paths.
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if something other than an absolute path
    is passed.