---
id: python-clock-id-constants-https-docs-python-org-3-library-time-html-90883e54
type: concept
title: Clock ID Constants[¶](https://docs.python.org/3/library/time.html#clock-id-constants
  "Link to this heading")
description: These constants are used as parameters for [`clock_getres()`](https://docs.python.org/3/library/time.html#time.clock_getres
  "time.clock_getres") and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/time.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Clock ID Constants[¶](https://docs.python.org/3/library/time.html#clock-id-constants "Link to this heading")

These constants are used as parameters for [`clock_getres()`](https://docs.python.org/3/library/time.html#time.clock_getres "time.clock_getres") and
[`clock_gettime()`](https://docs.python.org/3/library/time.html#time.clock_gettime "time.clock_gettime").

time.CLOCK\_BOOTTIME[¶](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "Link to this definition")
:   Identical to [`CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC"), except it also includes any time that
    the system is suspended.

    This allows applications to get a suspend-aware monotonic clock without
    having to deal with the complications of [`CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME"), which may
    have discontinuities if the time is changed using `settimeofday()` or
    similar.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.39.

    Added in version 3.7.

time.CLOCK\_HIGHRES[¶](https://docs.python.org/3/library/time.html#time.CLOCK_HIGHRES "Link to this definition")
:   The Solaris OS has a `CLOCK_HIGHRES` timer that attempts to use an optimal
    hardware source, and may give close to nanosecond resolution.
    `CLOCK_HIGHRES` is the nonadjustable, high-resolution clock.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Solaris.

    Added in version 3.3.

time.CLOCK\_MONOTONIC[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "Link to this definition")
:   Clock that cannot be set and represents monotonic time since some unspecified
    starting point.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

    Added in version 3.3.

time.CLOCK\_MONOTONIC\_RAW[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW "Link to this definition")
:   Similar to [`CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC"), but provides access to a raw
    hardware-based time that is not subject to NTP adjustments.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.28, macOS >= 10.12.

    Added in version 3.3.

time.CLOCK\_MONOTONIC\_RAW\_APPROX[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW_APPROX "Link to this definition")
:   Similar to [`CLOCK_MONOTONIC_RAW`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW "time.CLOCK_MONOTONIC_RAW"), but reads a value cached by
    the system at context switch and hence has less accuracy.

    [Availability](https://docs.python.org/3/library/intro.html#availability): macOS >= 10.12.

    Added in version 3.13.

time.CLOCK\_PROCESS\_CPUTIME\_ID[¶](https://docs.python.org/3/library/time.html#time.CLOCK_PROCESS_CPUTIME_ID "Link to this definition")
:   High-resolution per-process timer from the CPU.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

    Added in version 3.3.

time.CLOCK\_PROF[¶](https://docs.python.org/3/library/time.html#time.CLOCK_PROF "Link to this definition")
:   High-resolution per-process timer from the CPU.

    [Availability](https://docs.python.org/3/library/intro.html#availability): FreeBSD, NetBSD >= 7, OpenBSD.

    Added in version 3.7.

time.CLOCK\_TAI[¶](https://docs.python.org/3/library/time.html#time.CLOCK_TAI "Link to this definition")
:   [International Atomic Time](https://www.nist.gov/pml/time-and-frequency-division/how-utcnist-related-coordinated-universal-time-utc-international)

    The system must have a current leap second table in order for this to give
    the correct answer. PTP or NTP software can maintain a leap second table.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Linux.

    Added in vers