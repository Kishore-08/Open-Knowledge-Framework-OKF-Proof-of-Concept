---
id: python-module-level-functions-https-docs-python-org-3-library-loggi-025d6e6b
type: concept
title: Module-Level Functions[¶](https://docs.python.org/3/library/logging.html#module-level-functions
  "Link to this heading")
description: In addition to the classes described above, there are a number of module-level
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Module-Level Functions[¶](https://docs.python.org/3/library/logging.html#module-level-functions "Link to this heading")

In addition to the classes described above, there are a number of module-level
functions.

logging.getLogger(*name=None*)[¶](https://docs.python.org/3/library/logging.html#logging.getLogger "Link to this definition")
:   Return a logger with the specified name or, if name is `None`, return the
    root logger of the hierarchy. If specified, the name is typically a
    dot-separated hierarchical name like *‘a’*, *‘a.b’* or *‘a.b.c.d’*. Choice
    of these names is entirely up to the developer who is using logging, though
    it is recommended that `__name__` be used unless you have a specific
    reason for not doing that, as mentioned in [Logger Objects](https://docs.python.org/3/library/logging.html#logger).

    All calls to this function with a given name return the same logger instance.
    This means that logger instances never need to be passed between different parts
    of an application.

logging.getLoggerClass()[¶](https://docs.python.org/3/library/logging.html#logging.getLoggerClass "Link to this definition")
:   Return either the standard [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") class, or the last class passed to
    [`setLoggerClass()`](https://docs.python.org/3/library/logging.html#logging.setLoggerClass "logging.setLoggerClass"). This function may be called from within a new class
    definition, to ensure that installing a customized `Logger` class will
    not undo customizations already applied by other code. For example:

    ```
    class MyLogger(logging.getLoggerClass()):
        # ... override behaviour here
    ```

logging.getLogRecordFactory()[¶](https://docs.python.org/3/library/logging.html#logging.getLogRecordFactory "Link to this definition")
:   Return a callable which is used to create a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord").

    Added in version 3.2: This function has been provided, along with [`setLogRecordFactory()`](https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory "logging.setLogRecordFactory"),
    to allow developers more control over how the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord")
    representing a logging event is constructed.

    See [`setLogRecordFactory()`](https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory "logging.setLogRecordFactory") for more information about the how the
    factory is called.

logging.debug(*msg*, *\*args*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/logging.html#logging.debug "Link to this definition")
:   This is a convenience function that calls [`Logger.debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug"), on the root
    logger. The handling of the arguments is in every way identical
    to what is described in that method.

    The only difference is that if the root logger has no handlers, then
    [`basicConfig()`](https://docs.python.org/3/library/logging.html#logging.basicConfig "logging.basicConfig") is called, prior to calling `debug` on the root logger.

    For very short scripts or quick demonstrations of `logging` facilities,
    `debug` and the other module-level functions may be convenient. However,
    most programs will want to carefully and explicitly control the logging
    configuration, and should therefore prefer creating a module-level logger and
    calling [`Logger.debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug") (or other level-specific methods) on it, as
    described at the beginning of this documentation.

logging.info(*msg*, *\*args*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/logging.html#logging.info "Link to this definition")
:   Logs a message with level [`INFO`](https