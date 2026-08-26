---
id: python-queuehandler-https-docs-python-org-3-library-logging-handler-41e6f1c2
type: concept
title: QueueHandler[¶](https://docs.python.org/3/library/logging.handlers.html#queuehandler
  "Link to this heading")
description: Added in version 3.2.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## QueueHandler[¶](https://docs.python.org/3/library/logging.handlers.html#queuehandler "Link to this heading")

Added in version 3.2.

The [`QueueHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler "logging.handlers.QueueHandler") class, located in the `logging.handlers` module,
supports sending logging messages to a queue, such as those implemented in the
[`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.") or [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") modules.

Along with the [`QueueListener`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueListener "logging.handlers.QueueListener") class, [`QueueHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler "logging.handlers.QueueHandler") can be used
to let handlers do their work on a separate thread from the one which does the
logging. This is important in web applications and also other service
applications where threads servicing clients need to respond as quickly as
possible, while any potentially slow operations (such as sending an email via
[`SMTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler "logging.handlers.SMTPHandler")) are done on a separate thread.

*class* logging.handlers.QueueHandler(*queue*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler "Link to this definition")
:   Returns a new instance of the `QueueHandler` class. The instance is
    initialized with the queue to send messages to. The *queue* can be any
    queue-like object; it’s used as-is by the [`enqueue()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler.enqueue "logging.handlers.QueueHandler.enqueue") method, which
    needs to know how to send messages to it. The queue is not *required* to
    have the task tracking API, which means that you can use
    [`SimpleQueue`](https://docs.python.org/3/library/queue.html#queue.SimpleQueue "queue.SimpleQueue") instances for *queue*.

    Note

    If you are using [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism."), you should avoid using
    [`SimpleQueue`](https://docs.python.org/3/library/queue.html#queue.SimpleQueue "queue.SimpleQueue") and instead use [`multiprocessing.Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue").

    Warning

    The [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") module uses an internal logger created and
    accessed via [`get_logger()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_logger "multiprocessing.get_logger").
    [`multiprocessing.Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue") will log `DEBUG` level messages upon
    items being queued. If those log messages are processed by a
    `QueueHandler` using the same `multiprocessing.Queue` instance,
    it will cause a deadlock or infinite recursion.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler.emit "Link to this definition")
    :   Enqueues the result of preparing the LogRecord. Should an exception
        occur (e.g. because a bounded queue has filled up), the
        [`handleError()`](https://docs.python.org/3/library/logging.html#logging.Handler.handleError "logging.Handler.handleError") method is called to handle the
        error. This can result in the record silently being dropped (if
        [`logging.raiseExceptions`](https://docs.python.org/3/library/logging.html#logging.rai