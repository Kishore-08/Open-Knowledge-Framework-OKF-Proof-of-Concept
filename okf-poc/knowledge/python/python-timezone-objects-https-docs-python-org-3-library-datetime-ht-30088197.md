---
id: python-timezone-objects-https-docs-python-org-3-library-datetime-ht-30088197
type: concept
title: '`timezone` objects[¶](https://docs.python.org/3/library/datetime.html#timezone-objects
  "Link to this heading")'
description: The [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone
  "datetime.timezone") class is a subclass of [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinf
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `timezone` objects[¶](https://docs.python.org/3/library/datetime.html#timezone-objects "Link to this heading")

The [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") class is a subclass of [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo"), each
instance of which represents a time zone defined by a fixed offset from
UTC.

Objects of this class cannot be used to represent time zone information in the
locations where different offsets are used in different days of the year or
where historical changes have been made to civil time.

*class* datetime.timezone(*offset*, *name=None*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone "Link to this definition")
:   The *offset* argument must be specified as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
    object representing the difference between the local time and UTC. It must
    be strictly between `-timedelta(hours=24)` and
    `timedelta(hours=24)`, otherwise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

    The *name* argument is optional. If specified it must be a string that
    will be used as the value returned by the [`datetime.tzname()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzname "datetime.datetime.tzname") method.

    Added in version 3.2.

    Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

timezone.utcoffset(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.utcoffset "Link to this definition")
:   Return the fixed value specified when the [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") instance is
    constructed.

    The *dt* argument is ignored. The return value is a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
    instance equal to the difference between the local time and UTC.

    Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

timezone.tzname(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.tzname "Link to this definition")
:   Return the fixed value specified when the [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") instance
    is constructed.

    If *name* is not provided in the constructor, the name returned by
    `tzname(dt)` is generated from the value of the `offset` as follows. If
    *offset* is `timedelta(0)`, the name is “UTC”, otherwise it is a string in
    the format `UTC±HH:MM`, where ± is the sign of `offset`, HH and MM are
    two digits of `offset.hours` and `offset.minutes` respectively.

    Changed in version 3.6: Name generated from `offset=timedelta(0)` is now plain `'UTC'`, not
    `'UTC+00:00'`.

timezone.dst(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.dst "Link to this definition")
:   Always returns `None`.

timezone.fromutc(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.fromutc "Link to this definition")
:   Return `dt + offset`. The *dt* argument must be an aware
    [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance, with `tzinfo` set to `self`.

Class attributes:

timezone.utc[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc "Link to this definition")
:   The UTC time zone, `timezone(timedelta(0))`.