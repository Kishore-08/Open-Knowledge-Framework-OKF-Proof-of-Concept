---
id: python-handler-objects-https-docs-python-org-3-library-logging-html-025d6e6b
type: concept
title: Handler Objects[¶](https://docs.python.org/3/library/logging.html#handler-objects
  "Link to this heading")
description: Handlers have the following attributes and methods. Note that [`Handler`](https://docs.python.org/3/library/logging.html#logging.Handler
  "logging.Handler")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Handler Objects[¶](https://docs.python.org/3/library/logging.html#handler-objects "Link to this heading")

Handlers have the following attributes and methods. Note that [`Handler`](https://docs.python.org/3/library/logging.html#logging.Handler "logging.Handler")
is never instantiated directly; this class acts as a base for more useful
subclasses. However, the `__init__()` method in subclasses needs to call
[`Handler.__init__()`](https://docs.python.org/3/library/logging.html#logging.Handler.__init__ "logging.Handler.__init__").

*class* logging.Handler[¶](https://docs.python.org/3/library/logging.html#logging.Handler "Link to this definition")
:   \_\_init\_\_(*level=NOTSET*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.__init__ "Link to this definition")
    :   Initializes the `Handler` instance by setting its level, setting the list
        of filters to the empty list and creating a lock (using [`createLock()`](https://docs.python.org/3/library/logging.html#logging.Handler.createLock "logging.Handler.createLock")) for
        serializing access to an I/O mechanism.

    createLock()[¶](https://docs.python.org/3/library/logging.html#logging.Handler.createLock "Link to this definition")
    :   Initializes a thread lock which can be used to serialize access to underlying
        I/O functionality which may not be threadsafe.

    acquire()[¶](https://docs.python.org/3/library/logging.html#logging.Handler.acquire "Link to this definition")
    :   Acquires the thread lock created with [`createLock()`](https://docs.python.org/3/library/logging.html#logging.Handler.createLock "logging.Handler.createLock").

    release()[¶](https://docs.python.org/3/library/logging.html#logging.Handler.release "Link to this definition")
    :   Releases the thread lock acquired with [`acquire()`](https://docs.python.org/3/library/logging.html#logging.Handler.acquire "logging.Handler.acquire").

    setLevel(*level*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.setLevel "Link to this definition")
    :   Sets the threshold for this handler to *level*. Logging messages which are
        less severe than *level* will be ignored. When a handler is created, the
        level is set to [`NOTSET`](https://docs.python.org/3/library/logging.html#logging.NOTSET "logging.NOTSET") (which causes all messages to be
        processed).

        See [Logging Levels](https://docs.python.org/3/library/logging.html#levels) for a list of levels.

        Changed in version 3.2: The *level* parameter now accepts a string representation of the
        level such as ‘INFO’ as an alternative to the integer constants
        such as [`INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO").

    setFormatter(*fmt*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.setFormatter "Link to this definition")
    :   Sets the formatter for this handler to *fmt*.
        The *fmt* argument must be a [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") instance or `None`.

    addFilter(*filter*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.addFilter "Link to this definition")
    :   Adds the specified filter *filter* to this handler.

    removeFilter(*filter*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.removeFilter "Link to this definition")
    :   Removes the specified filter *filter* from this handler.

    filter(*record*)[¶](https://docs.python.org/3/library/logging.html#logging.Handler.filter "Link to this definition")
    :   Apply this handler’s filters to the record and return `True` if the
        record is to be processed. The filters are consulted in turn, until one of
        them returns a false value. If none of them return a false value, the record
        will be emitted. If one returns a false value, the handler will not emit the
        record.

    flush()[¶](https://docs.python