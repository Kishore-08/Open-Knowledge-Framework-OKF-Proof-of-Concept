---
id: python-streamhandler-https-docs-python-org-3-library-logging-handle-41e6f1c2
type: concept
title: StreamHandler[¶](https://docs.python.org/3/library/logging.handlers.html#streamhandler
  "Link to this heading")
description: The [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
  "logging.StreamHandler") class, located in the core [`logging`](https://docs.python.org/3/library/lo
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## StreamHandler[¶](https://docs.python.org/3/library/logging.handlers.html#streamhandler "Link to this heading")

The [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") class, located in the core [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package,
sends logging output to streams such as *sys.stdout*, *sys.stderr* or any
file-like object (or, more precisely, any object which supports `write()`
and `flush()` methods).

*class* logging.StreamHandler(*stream=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "Link to this definition")
:   Returns a new instance of the `StreamHandler` class. If *stream* is
    specified, the instance will use it for logging output; otherwise, *sys.stderr*
    will be used.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler.emit "Link to this definition")
    :   If a formatter is specified, it is used to format the record. The record
        is then written to the stream followed by [`terminator`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler.terminator "logging.StreamHandler.terminator"). If exception information
        is present, it is formatted using [`traceback.print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception") and
        appended to the stream.

    flush()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler.flush "Link to this definition")
    :   Flushes the stream by calling its `flush()` method. Note that the
        `close()` method is inherited from [`Handler`](https://docs.python.org/3/library/logging.html#logging.Handler "logging.Handler") and so
        does no output, so an explicit `flush()` call may be needed at times.

    setStream(*stream*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler.setStream "Link to this definition")
    :   Sets the instance’s stream to the specified value, if it is different.
        The old stream is flushed before the new stream is set.

        Parameters:
        :   **stream** – The stream that the handler should use.

        Returns:
        :   the old stream, if the stream was changed, or `None` if it wasn’t.

        Added in version 3.7.

    terminator[¶](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler.terminator "Link to this definition")
    :   String used as the terminator when writing a formatted record to a stream.
        Default value is `'\n'`.

        If you don’t want a newline termination, you can set the handler instance’s
        `terminator` attribute to the empty string.

        In earlier versions, the terminator was hardcoded as `'\n'`.

        Added in version 3.2.