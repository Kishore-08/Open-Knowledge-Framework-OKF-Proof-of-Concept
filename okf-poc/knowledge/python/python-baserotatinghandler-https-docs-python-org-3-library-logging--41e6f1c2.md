---
id: python-baserotatinghandler-https-docs-python-org-3-library-logging--41e6f1c2
type: concept
title: BaseRotatingHandler[¶](https://docs.python.org/3/library/logging.handlers.html#baserotatinghandler
  "Link to this heading")
description: The [`BaseRotatingHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler
  "logging.handlers.BaseRotatingHandler") class, located in the `logging.handlers
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## BaseRotatingHandler[¶](https://docs.python.org/3/library/logging.handlers.html#baserotatinghandler "Link to this heading")

The [`BaseRotatingHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler "logging.handlers.BaseRotatingHandler") class, located in the `logging.handlers`
module, is the base class for the rotating file handlers,
[`RotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "logging.handlers.RotatingFileHandler") and [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler"). You should
not need to instantiate this class, but it has attributes and methods you may
need to override.

*class* logging.handlers.BaseRotatingHandler(*filename*, *mode*, *encoding=None*, *delay=False*, *errors=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler "Link to this definition")
:   The parameters are as for `FileHandler`. The attributes are:

    namer[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler.namer "Link to this definition")
    :   If this attribute is set to a callable, the [`rotation_filename()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler.rotation_filename "logging.handlers.BaseRotatingHandler.rotation_filename")
        method delegates to this callable. The parameters passed to the callable
        are those passed to `rotation_filename()`.

        Note

        The namer function is called quite a few times during rollover,
        so it should be as simple and as fast as possible. It should also
        return the same output every time for a given input, otherwise the
        rollover behaviour may not work as expected.

        It’s also worth noting that care should be taken when using a namer to
        preserve certain attributes in the filename which are used during rotation.
        For example, [`RotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "logging.handlers.RotatingFileHandler") expects to have a set of log files
        whose names contain successive integers, so that rotation works as expected,
        and [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler") deletes old log files (based on the
        `backupCount` parameter passed to the handler’s initializer) by determining
        the oldest files to delete. For this to happen, the filenames should be
        sortable using the date/time portion of the filename, and a namer needs to
        respect this. (If a namer is wanted that doesn’t respect this scheme, it will
        need to be used in a subclass of `TimedRotatingFileHandler` which
        overrides the [`getFilesToDelete()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler.getFilesToDelete "logging.handlers.TimedRotatingFileHandler.getFilesToDelete") method to
        fit in with the custom naming scheme.)

        Added in version 3.3.

    rotator[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler.rotator "Link to this definition")
    :   If this attribute is set to a callable, the [`rotate()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler.rotate "logging.handlers.BaseRotatingHandler.rotate") method
        delegates to this callable. The parameters passed to the callable are
        those passed to `rotate()`.

        Added in version 3.3.

    rotation\_filename(*default\_name*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BaseRotatingHandler.rotation_filename "Li