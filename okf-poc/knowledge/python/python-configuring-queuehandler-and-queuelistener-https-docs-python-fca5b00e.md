---
id: python-configuring-queuehandler-and-queuelistener-https-docs-python-fca5b00e
type: concept
title: Configuring QueueHandler and QueueListener[¶](https://docs.python.org/3/library/logging.config.html#configuring-queuehandler-and-queuelistener
  "Link to this heading")
description: If you want to configure a [`QueueHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler
  "logging.handlers.QueueHandler"), noting that this
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Configuring QueueHandler and QueueListener[¶](https://docs.python.org/3/library/logging.config.html#configuring-queuehandler-and-queuelistener "Link to this heading")

If you want to configure a [`QueueHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler "logging.handlers.QueueHandler"), noting that this
is normally used in conjunction with a [`QueueListener`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueListener "logging.handlers.QueueListener"), you
can configure both together. After the configuration, the `QueueListener` instance
will be available as the [`listener`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler.listener "logging.handlers.QueueHandler.listener") attribute of
the created handler, and that in turn will be available to you using
[`getHandlerByName()`](https://docs.python.org/3/library/logging.html#logging.getHandlerByName "logging.getHandlerByName") and passing the name you have used for the
`QueueHandler` in your configuration. The dictionary schema for configuring the pair
is shown in the example YAML snippet below.

```
handlers:
  qhand:
    class: logging.handlers.QueueHandler
    queue: my.module.queue_factory
    listener: my.package.CustomListener
    handlers:
      - hand_name_1
      - hand_name_2
      ...
```

The `queue` and `listener` keys are optional.

If the `queue` key is present, the corresponding value can be one of the following:

- An object implementing the [`Queue.put_nowait`](https://docs.python.org/3/library/queue.html#queue.Queue.put_nowait "queue.Queue.put_nowait")
  and [`Queue.get`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") public API. For instance, this may be
  an actual instance of [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") or a subclass thereof, or a proxy
  obtained by [`multiprocessing.managers.SyncManager.Queue()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Queue "multiprocessing.managers.SyncManager.Queue").

  This is of course only possible if you are constructing or modifying
  the configuration dictionary in code.
- A string that resolves to a callable which, when called with no arguments, returns
  the queue instance to use. That callable could be a [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") subclass
  or a function which returns a suitable queue instance,
  such as `my.module.queue_factory()`.
- A dict with a `'()'` key which is constructed in the usual way as discussed in
  [User-defined objects](https://docs.python.org/3/library/logging.config.html#logging-config-dict-userdef). The result of this construction should be a
  [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") instance.

If the `queue` key is absent, a standard unbounded [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") instance is
created and used.

If the `listener` key is present, the corresponding value can be one of the following:

- A subclass of [`logging.handlers.QueueListener`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueListener "logging.handlers.QueueListener"). This is of course only
  possible if you are constructing or modifying the configuration dictionary in
  code.
- A string which resolves to a class which is a subclass of `QueueListener`, such as
  `'my.package.CustomListener'`.
- A dict with a `'()'` key which is constructed in the usual way as discussed in
  [User-defined objects](https://docs.python.org/3/library/logging.config.html#logging-config-dict-userdef). The result of this construction should be a
  callable with the same signature as the `QueueListener` initializer.

If the `listener` key is absent, [`logging.handlers.QueueListener`](https://docs.python.org/3/library/loggi