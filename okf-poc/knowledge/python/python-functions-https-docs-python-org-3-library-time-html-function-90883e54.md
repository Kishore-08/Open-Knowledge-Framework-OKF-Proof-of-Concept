---
id: python-functions-https-docs-python-org-3-library-time-html-function-90883e54
type: concept
title: Functions[¶](https://docs.python.org/3/library/time.html#functions "Link to
  this heading")
description: time.asctime([*time\_tuple*])[¶](https://docs.python.org/3/library/time.html#time.asctime
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/time.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Functions[¶](https://docs.python.org/3/library/time.html#functions "Link to this heading")

time.asctime([*time\_tuple*])[¶](https://docs.python.org/3/library/time.html#time.asctime "Link to this definition")
:   Convert a tuple or [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") representing a time as returned by
    [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime") or [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime") to a string of the following
    form: `'Sun Jun 20 23:21:05 1993'`. The day field is two characters long
    and is space padded if the day is a single digit,
    for example: `'Wed Jun  9 04:26:40 1993'`.

    If *time\_tuple* is not provided,
    the current time as returned by [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime") is used.
    Locale information is not used by `asctime()`.

    Note

    Unlike the C function of the same name, `asctime()` does not add a
    trailing newline.

time.pthread\_getcpuclockid(*thread\_id*, */*)[¶](https://docs.python.org/3/library/time.html#time.pthread_getcpuclockid "Link to this definition")
:   Return the *clk\_id* of the thread-specific CPU-time clock for the specified *thread\_id*.

    Use [`threading.get_ident()`](https://docs.python.org/3/library/threading.html#threading.get_ident "threading.get_ident") or the [`ident`](https://docs.python.org/3/library/threading.html#threading.Thread.ident "threading.Thread.ident")
    attribute of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") objects to get a suitable value
    for *thread\_id*.

    Warning

    Passing an invalid or expired *thread\_id* may result in
    undefined behavior, such as segmentation fault.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix

    See the man page for *[pthread\_getcpuclockid(3)](https://manpages.debian.org/pthread_getcpuclockid(3))* for
    further information.

    Added in version 3.7.

time.clock\_getres(*clk\_id*, */*)[¶](https://docs.python.org/3/library/time.html#time.clock_getres "Link to this definition")
:   Return the resolution (precision) of the specified clock *clk\_id*. Refer to
    [Clock ID Constants](https://docs.python.org/3/library/time.html#time-clock-id-constants) for a list of accepted values for *clk\_id*.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

    Added in version 3.3.

time.clock\_gettime(*clk\_id*, */*) → [float](https://docs.python.org/3/library/functions.html#float "float")[¶](https://docs.python.org/3/library/time.html#time.clock_gettime "Link to this definition")
:   Return the time of the specified clock *clk\_id*. Refer to
    [Clock ID Constants](https://docs.python.org/3/library/time.html#time-clock-id-constants) for a list of accepted values for *clk\_id*.

    Use [`clock_gettime_ns()`](https://docs.python.org/3/library/time.html#time.clock_gettime_ns "time.clock_gettime_ns") to avoid the precision loss caused by the
    [`float`](https://docs.python.org/3/library/functions.html#float "float") type.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

    Added in version 3.3.

time.clock\_gettime\_ns(*clk\_id*, */*) → [int](https://docs.python.org/3/library/functions.html#int "int")[¶](https://docs.python.org/3/library/time.html#time.clock_gettime_ns "Link to this definition")
:   Similar to [`clock_gettime()`](https://docs.python.org/3/library/time.html#time.clock_gettime "time.clock_gettime") but return time as nanoseconds.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

    Added in version 3.7.

time.clock\_settime(*clk\_id*, *time: [float](https://docs.python.org/3/library/functions.html#float "float")*, */*)[¶](https://docs.python.org/3/library/time.html#time