---
id: python-timer-file-descriptors-https-docs-python-org-3-library-os-ht-e86233c0
type: concept
title: Timer File Descriptors[¶](https://docs.python.org/3/library/os.html#timer-file-descriptors
  "Link to this heading")
description: Added in version 3.13.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Timer File Descriptors[¶](https://docs.python.org/3/library/os.html#timer-file-descriptors "Link to this heading")

Added in version 3.13.

These functions provide support for Linux’s *timer file descriptor* API.
Naturally, they are all only available on Linux.

os.timerfd\_create(*clockid*, */*, *\**, *flags=0*)[¶](https://docs.python.org/3/library/os.html#os.timerfd_create "Link to this definition")
:   Create and return a timer file descriptor (*timerfd*).

    The file descriptor returned by `timerfd_create()` supports:

    - [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
    - [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
    - [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")

    The file descriptor’s [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") method can be called with a buffer size
    of 8. If the timer has already expired one or more times, `read()`
    returns the number of expirations with the host’s endianness, which may be
    converted to an [`int`](https://docs.python.org/3/library/functions.html#int "int") by `int.from_bytes(x, byteorder=sys.byteorder)`.

    [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select") and [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll") can be used to wait until
    timer expires and the file descriptor is readable.

    *clockid* must be a valid [clock ID](https://docs.python.org/3/library/time.html#time-clock-id-constants),
    as defined in the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module:

    - [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
    - [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
    - [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME") (Since Linux 3.15 for timerfd\_create)

    If *clockid* is [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME"), a settable system-wide
    real-time clock is used. If system clock is changed, timer setting need
    to be updated. To cancel timer when system clock is changed, see
    [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET").

    If *clockid* is [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC"), a non-settable monotonically
    increasing clock is used. Even if the system clock is changed, the timer
    setting will not be affected.

    If *clockid* is [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME"), same as [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
    except it includes any time that the system is suspended.

    The file descriptor’s behaviour can be modified by specifying a *flags* value.
    Any of the following variables may be used, combined using bitwise OR
    (the `|` operator):

    - [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
    - [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")

    If [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK") is not set as a flag, [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") blocks until
    the timer expires. If it is set as a flag, `read()` doesn’t block, but
    If there hasn’t been an expiration since the last call to read,
    `read()` raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") with `errno`