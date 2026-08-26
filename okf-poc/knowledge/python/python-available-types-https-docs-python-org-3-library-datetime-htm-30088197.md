---
id: python-available-types-https-docs-python-org-3-library-datetime-htm-30088197
type: concept
title: Available types[¶](https://docs.python.org/3/library/datetime.html#available-types
  "Link to this heading")
description: '*class* datetime.date'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Available types[¶](https://docs.python.org/3/library/datetime.html#available-types "Link to this heading")

*class* datetime.date
:   An idealized naive date, assuming the current Gregorian calendar always was, and
    always will be, in effect. Attributes: [`year`](https://docs.python.org/3/library/datetime.html#datetime.date.year "datetime.date.year"), [`month`](https://docs.python.org/3/library/datetime.html#datetime.date.month "datetime.date.month"), and
    [`day`](https://docs.python.org/3/library/datetime.html#datetime.date.day "datetime.date.day").

*class* datetime.time
:   An idealized time, independent of any particular day, assuming that every day
    has exactly 24\*60\*60 seconds. (There is no notion of “leap seconds” here.)
    Attributes: [`hour`](https://docs.python.org/3/library/datetime.html#datetime.time.hour "datetime.time.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.time.minute "datetime.time.minute"), [`second`](https://docs.python.org/3/library/datetime.html#datetime.time.second "datetime.time.second"), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond"),
    and [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo").

*class* datetime.datetime
:   A combination of a date and a time. Attributes: [`year`](https://docs.python.org/3/library/datetime.html#datetime.datetime.year "datetime.datetime.year"), [`month`](https://docs.python.org/3/library/datetime.html#datetime.datetime.month "datetime.datetime.month"),
    [`day`](https://docs.python.org/3/library/datetime.html#datetime.datetime.day "datetime.datetime.day"), [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "datetime.datetime.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute "datetime.datetime.minute"), [`second`](https://docs.python.org/3/library/datetime.html#datetime.datetime.second "datetime.datetime.second"), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond"),
    and [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo").

*class* datetime.timedelta
:   A duration expressing the difference between two [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
    or [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") instances to microsecond resolution.

*class* datetime.tzinfo
:   An abstract base class for time zone information objects. These are used by the
    [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") classes to provide a customizable notion of
    time adjustment (for example, to account for time zone and/or daylight saving
    time).

*class* datetime.timezone
:   A class that implements the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") abstract base class as a
    fixed offset from the UTC.

    Added in version 3.2.

Objects of these types are immutable.

Subclass relationships:

![timedelta, tzinfo, time, and date inherit from object; timezone inherits from tzinfo; and datetime inherits from date.](https://docs.python.org/3/_images/datetime-inheritance.svg)