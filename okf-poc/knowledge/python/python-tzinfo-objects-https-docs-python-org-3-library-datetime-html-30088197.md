---
id: python-tzinfo-objects-https-docs-python-org-3-library-datetime-html-30088197
type: concept
title: '`tzinfo` objects[¶](https://docs.python.org/3/library/datetime.html#tzinfo-objects
  "Link to this heading")'
description: '*class* datetime.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `tzinfo` objects[¶](https://docs.python.org/3/library/datetime.html#tzinfo-objects "Link to this heading")

*class* datetime.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "Link to this definition")
:   This is an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class), meaning that this class should not be
    instantiated directly. Define a subclass of `tzinfo` to capture
    information about a particular time zone.

    An instance of (a concrete subclass of) `tzinfo` can be passed to the
    constructors for [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects. The latter objects
    view their attributes as being in local time, and the `tzinfo` object
    supports methods revealing offset of local time from UTC, the name of the time
    zone, and DST offset, all relative to a date or time object passed to them.

    You need to derive a concrete subclass, and (at least)
    supply implementations of the standard `tzinfo` methods needed by the
    [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") methods you use. The `datetime` module provides
    [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone"), a simple concrete subclass of `tzinfo` which can
    represent time zones with fixed offset from UTC such as UTC itself or North
    American EST and EDT.

    Special requirement for pickling: A `tzinfo` subclass must have an
    [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method that can be called with no arguments,
    otherwise it can be
    pickled but possibly not unpickled again. This is a technical requirement that
    may be relaxed in the future.

    A concrete subclass of `tzinfo` may need to implement the following
    methods. Exactly which methods are needed depends on the uses made of aware
    `datetime` objects. If in doubt, simply implement all of them.

tzinfo.utcoffset(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.utcoffset "Link to this definition")
:   Return offset of local time from UTC, as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object that is
    positive east of UTC. If local time is west of UTC, this should be negative.

    This represents the *total* offset from UTC; for example, if a
    [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") object represents both time zone and DST adjustments,
    `utcoffset()` should return their sum. If the UTC offset isn’t known,
    return `None`. Else the value returned must be a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object
    strictly between `-timedelta(hours=24)` and `timedelta(hours=24)`
    (the magnitude of the offset must be less than one day). Most implementations
    of `utcoffset()` will probably look like one of these two:

    ```
    return CONSTANT                 # fixed-offset class
    return CONSTANT + self.dst(dt)  # daylight-aware class
    ```

    If `utcoffset()` does not return `None`, [`dst()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.dst "datetime.tzinfo.dst") should not return
    `None` either.

    The default implementation of `utcoffset()` raises
    [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

    Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

tzinfo.dst(*dt*)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.dst "Link to this definition")
:   Return the daylight saving time (DST) adjustment, as a [`timedelta`](https://doc