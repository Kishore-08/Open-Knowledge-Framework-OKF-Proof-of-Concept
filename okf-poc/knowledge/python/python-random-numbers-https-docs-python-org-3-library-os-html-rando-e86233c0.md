---
id: python-random-numbers-https-docs-python-org-3-library-os-html-rando-e86233c0
type: concept
title: Random numbers[¶](https://docs.python.org/3/library/os.html#random-numbers
  "Link to this heading")
description: os.getrandom(*size*, *flags=0*)[¶](https://docs.python.org/3/library/os.html#os.getrandom
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Random numbers[¶](https://docs.python.org/3/library/os.html#random-numbers "Link to this heading")

os.getrandom(*size*, *flags=0*)[¶](https://docs.python.org/3/library/os.html#os.getrandom "Link to this definition")
:   Get up to *size* random bytes. The function can return less bytes than
    requested.

    These bytes can be used to seed user-space random number generators or for
    cryptographic purposes.

    `getrandom()` relies on entropy gathered from device drivers and other
    sources of environmental noise. Unnecessarily reading large quantities of
    data will have a negative impact on other users of the `/dev/random` and
    `/dev/urandom` devices.

    The flags argument is a bit mask that can contain zero or more of the
    following values ORed together: [`os.GRND_RANDOM`](https://docs.python.org/3/library/os.html#os.GRND_RANDOM "os.GRND_RANDOM") and
    [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK").

    See also the [Linux getrandom() manual page](https://man7.org/linux/man-pages/man2/getrandom.2.html).

    [Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.17.

    Added in version 3.6.

os.urandom(*size*, */*)[¶](https://docs.python.org/3/library/os.html#os.urandom "Link to this definition")
:   Return a bytestring of *size* random bytes suitable for cryptographic use.

    This function returns random bytes from an OS-specific randomness source. The
    returned data should be unpredictable enough for cryptographic applications,
    though its exact quality depends on the OS implementation.

    On Linux, if the `getrandom()` syscall is available, it is used in
    blocking mode: block until the system urandom entropy pool is initialized
    (128 bits of entropy are collected by the kernel). See the [**PEP 524**](https://peps.python.org/pep-0524/) for
    the rationale. On Linux, the [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom") function can be used to get
    random bytes in non-blocking mode (using the [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK") flag) or
    to poll until the system urandom entropy pool is initialized.

    On a Unix-like system, random bytes are read from the `/dev/urandom`
    device. If the `/dev/urandom` device is not available or not readable, the
    [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") exception is raised.

    On Windows, it will use `BCryptGenRandom()`.

    See also

    The [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.") module provides higher level functions. For an
    easy-to-use interface to the random number generator provided by your
    platform, please see [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom").

    Changed in version 3.5: On Linux 3.17 and newer, the `getrandom()` syscall is now used
    when available. On OpenBSD 5.6 and newer, the C `getentropy()`
    function is now used. These functions avoid the usage of an internal file
    descriptor.

    Changed in version 3.5.2: On Linux, if the `getrandom()` syscall blocks (the urandom entropy pool
    is not initialized yet), fall back on reading `/dev/urandom`.

    Changed in version 3.6: On Linux, `getrandom()` is now used in blocking mode to increase the
    security.

    Changed in version 3.11: On Windows, `BCryptGenRandom()` is used instead of `CryptGenRandom()`
    which is deprecated.

os.GRND\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "Link to this definition")
:   By default, when reading from `/dev/random`, [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom") blocks if
    no random bytes are available, and when reading fr