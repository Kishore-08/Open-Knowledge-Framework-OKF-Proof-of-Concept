---
id: python-watchedfilehandler-https-docs-python-org-3-library-logging-h-41e6f1c2
type: concept
title: WatchedFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#watchedfilehandler
  "Link to this heading")
description: The [`WatchedFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler
  "logging.handlers.WatchedFileHandler") class, located in the `logging.handlers`
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## WatchedFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#watchedfilehandler "Link to this heading")

The [`WatchedFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler "logging.handlers.WatchedFileHandler") class, located in the `logging.handlers`
module, is a `FileHandler` which watches the file it is logging to. If
the file changes, it is closed and reopened using the file name.

A file change can happen because of usage of programs such as *newsyslog* and
*logrotate* which perform log file rotation. This handler, intended for use
under Unix/Linux, watches the file to see if it has changed since the last emit.
(A file is deemed to have changed if its device or inode have changed.) If the
file has changed, the old file stream is closed, and the file opened to get a
new stream.

This handler is not appropriate for use under Windows, because under Windows
open log files cannot be moved or renamed - logging opens the files with
exclusive locks - and so there is no need for such a handler. Furthermore,
*ST\_INO* is not supported under Windows; [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") always returns zero
for this value.

*class* logging.handlers.WatchedFileHandler(*filename*, *mode='a'*, *encoding=None*, *delay=False*, *errors=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler "Link to this definition")
:   Returns a new instance of the `WatchedFileHandler` class. The specified
    file is opened and used as the stream for logging. If *mode* is not specified,
    `'a'` is used. If *encoding* is not `None`, it is used to open the file
    with that encoding. If *delay* is true, then file opening is deferred until the
    first call to [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.emit "logging.handlers.WatchedFileHandler.emit"). By default, the file grows indefinitely. If
    *errors* is provided, it determines how encoding errors are handled.

    Changed in version 3.6: As well as string values, [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects are also accepted
    for the *filename* argument.

    Changed in version 3.9: The *errors* parameter was added.

    reopenIfNeeded()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.reopenIfNeeded "Link to this definition")
    :   Checks to see if the file has changed. If it has, the existing stream is
        flushed and closed and the file opened again, typically as a precursor to
        outputting the record to the file.

        Added in version 3.6.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.emit "Link to this definition")
    :   Outputs the record to the file, but first calls [`reopenIfNeeded()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.reopenIfNeeded "logging.handlers.WatchedFileHandler.reopenIfNeeded") to
        reopen the file if it has changed.