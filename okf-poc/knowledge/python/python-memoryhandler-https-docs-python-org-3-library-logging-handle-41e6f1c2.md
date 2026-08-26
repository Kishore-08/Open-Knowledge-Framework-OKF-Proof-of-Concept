---
id: python-memoryhandler-https-docs-python-org-3-library-logging-handle-41e6f1c2
type: concept
title: MemoryHandler[¶](https://docs.python.org/3/library/logging.handlers.html#memoryhandler
  "Link to this heading")
description: The [`MemoryHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler
  "logging.handlers.MemoryHandler") class, located in the `logging.handlers` module,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## MemoryHandler[¶](https://docs.python.org/3/library/logging.handlers.html#memoryhandler "Link to this heading")

The [`MemoryHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler "logging.handlers.MemoryHandler") class, located in the `logging.handlers` module,
supports buffering of logging records in memory, periodically flushing them to a
*target* handler. Flushing occurs whenever the buffer is full, or when an
event of a certain severity or greater is seen.

[`MemoryHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler "logging.handlers.MemoryHandler") is a subclass of the more general
[`BufferingHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler "logging.handlers.BufferingHandler"), which is an abstract class. This buffers logging
records in memory. Whenever each record is added to the buffer, a check is made
by calling `shouldFlush()` to see if the buffer should be flushed. If it
should, then `flush()` is expected to do the flushing.

*class* logging.handlers.BufferingHandler(*capacity*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler "Link to this definition")
:   Initializes the handler with a buffer of the specified capacity. Here,
    *capacity* means the number of logging records buffered.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler.emit "Link to this definition")
    :   Append the record to the buffer. If [`shouldFlush()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler.shouldFlush "logging.handlers.BufferingHandler.shouldFlush") returns true,
        call [`flush()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler.flush "logging.handlers.BufferingHandler.flush") to process the buffer.

    flush()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler.flush "Link to this definition")
    :   For a `BufferingHandler` instance, flushing means that it sets the
        buffer to an empty list. This method can be overwritten to implement more useful
        flushing behavior.

    shouldFlush(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.BufferingHandler.shouldFlush "Link to this definition")
    :   Return `True` if the buffer is up to capacity. This method can be
        overridden to implement custom flushing strategies.

*class* logging.handlers.MemoryHandler(*capacity*, *flushLevel=ERROR*, *target=None*, *flushOnClose=True*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler "Link to this definition")
:   Returns a new instance of the `MemoryHandler` class. The instance is
    initialized with a buffer size of *capacity* (number of records buffered).
    If *flushLevel* is not specified, `ERROR` is used. If no *target* is
    specified, the target will need to be set using [`setTarget()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler.setTarget "logging.handlers.MemoryHandler.setTarget") before this
    handler does anything useful. If *flushOnClose* is specified as `False`,
    then the buffer is *not* flushed when the handler is closed. If not specified
    or specified as `True`, the previous behaviour of flushing the buffer will
    occur when the handler is closed.

    Changed in version 3.6: The *flushOnClose* parameter was added.

    close()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler.close "Link to this definition")
    :   Calls [`flush()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler.flush "logging.handlers.MemoryHandler.flush"), sets the target to `None` and clears the
        buffer.

    flush()[¶](https://docs.python.org/3/librar