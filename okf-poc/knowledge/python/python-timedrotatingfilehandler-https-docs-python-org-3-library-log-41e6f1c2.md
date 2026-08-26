---
id: python-timedrotatingfilehandler-https-docs-python-org-3-library-log-41e6f1c2
type: concept
title: TimedRotatingFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
  "Link to this heading")
description: The [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
  "logging.handlers.TimedRotatingFileHandler") class, located in the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## TimedRotatingFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler "Link to this heading")

The [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler") class, located in the
`logging.handlers` module, supports rotation of disk log files at certain
timed intervals.

*class* logging.handlers.TimedRotatingFileHandler(*filename*, *when='h'*, *interval=1*, *backupCount=0*, *encoding=None*, *delay=False*, *utc=False*, *atTime=None*, *errors=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "Link to this definition")
:   Returns a new instance of the `TimedRotatingFileHandler` class. The
    specified file is opened and used as the stream for logging. On rotating it also
    sets the filename suffix. Rotating happens based on the product of *when* and
    *interval*.

    You can use the *when* to specify the type of *interval*. The list of possible
    values is below. Note that they are not case sensitive.

    | Value | Type of interval | If/how *atTime* is used |
    | --- | --- | --- |
    | `'S'` | Seconds | Ignored |
    | `'M'` | Minutes | Ignored |
    | `'H'` | Hours | Ignored |
    | `'D'` | Days | Ignored |
    | `'W0'-'W6'` | Weekday (0=Monday) | Used to compute initial rollover time |
    | `'midnight'` | Roll over at midnight, if *atTime* not specified, else at time *atTime* | Used to compute initial rollover time |

    When using weekday-based rotation, specify ‘W0’ for Monday, ‘W1’ for
    Tuesday, and so on up to ‘W6’ for Sunday. In this case, the value passed for
    *interval* isn’t used.

    The system will save old log files by appending extensions to the filename.
    The extensions are date-and-time based, using the strftime format
    `%Y-%m-%d_%H-%M-%S` or a leading portion thereof, depending on the
    rollover interval.

    When computing the next rollover time for the first time (when the handler
    is created), the last modification time of an existing log file, or else
    the current time, is used to compute when the next rotation will occur.

    If the *utc* argument is true, times in UTC will be used; otherwise
    local time is used.

    If *backupCount* is nonzero, at most *backupCount* files
    will be kept, and if more would be created when rollover occurs, the oldest
    one is deleted. The deletion logic uses the interval to determine which
    files to delete, so changing the interval may leave old files lying around.

    If *delay* is true, then file opening is deferred until the first call to
    [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler.emit "logging.handlers.TimedRotatingFileHandler.emit").

    If *atTime* is not `None`, it must be a `datetime.time` instance which
    specifies the time of day when rollover occurs, for the cases where rollover
    is set to happen “at midnight” or “on a particular weekday”. Note that in
    these cases, the *atTime* value is effectively used to compute the *initial*
    rollover, and subsequent rollovers would be calculated via the normal
    interval calculation.

    If *errors* is specified, it’s used to determine how encoding errors are
    handled.

    Note

    Calculation of the initial rollover time is done when the handler
    is initialised. Calculation of subsequent rollover times is done only
    when rollover occurs, and rollover occurs only when emitting output. If
    this is not kept in mind, it might lead to some confusion. For example,
    if an interval of “every minute” is set, that does not mean you will
    always see log files with times (in the filename) separated by a minute;
    if, during application execution, logging output is generated more
    frequently than once a minute, *then* you can expect to see log files
    with times separate