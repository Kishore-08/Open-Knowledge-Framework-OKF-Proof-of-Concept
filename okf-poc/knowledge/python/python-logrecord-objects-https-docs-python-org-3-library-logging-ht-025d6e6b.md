---
id: python-logrecord-objects-https-docs-python-org-3-library-logging-ht-025d6e6b
type: concept
title: LogRecord Objects[¶](https://docs.python.org/3/library/logging.html#logrecord-objects
  "Link to this heading")
description: '[`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord
  "logging.LogRecord") instances are created automatically by the [`Logger`](https://docs.python.org/3/library/logging.html'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## LogRecord Objects[¶](https://docs.python.org/3/library/logging.html#logrecord-objects "Link to this heading")

[`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") instances are created automatically by the [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger")
every time something is logged, and can be created manually via
[`makeLogRecord()`](https://docs.python.org/3/library/logging.html#logging.makeLogRecord "logging.makeLogRecord") (for example, from a pickled event received over the
wire).

*class* logging.LogRecord(*name*, *level*, *pathname*, *lineno*, *msg*, *args*, *exc\_info*, *func=None*, *sinfo=None*)[¶](https://docs.python.org/3/library/logging.html#logging.LogRecord "Link to this definition")
:   Contains all the information pertinent to the event being logged.

    The primary information is passed in *msg* and *args*,
    which are combined using `msg % args` to create
    the `message` attribute of the record.

    Parameters:
    :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the logger used to log the event
          represented by this `LogRecord`.
          Note that the logger name in the `LogRecord`
          will always have this value,
          even though it may be emitted by a handler
          attached to a different (ancestor) logger.
        - **level** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The [numeric level](https://docs.python.org/3/library/logging.html#levels) of the logging event
          (such as `10` for `DEBUG`, `20` for `INFO`, etc).
          Note that this is converted to *two* attributes of the LogRecord:
          `levelno` for the numeric value
          and `levelname` for the corresponding level name.
        - **pathname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – The full string path of the source file
          where the logging call was made.
        - **lineno** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The line number in the source file
          where the logging call was made.
        - **msg** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")) – The event description message,
          which can be a %-format string with placeholders for variable data,
          or an arbitrary object (see [Using arbitrary objects as messages](https://docs.python.org/3/howto/logging.html#arbitrary-object-messages)).
        - **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "dict")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "str")*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")*]*) – Variable data to merge into the *msg* argument
          to obtain the event description.
        - **exc\_info** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "tuple")*[*[*type*](https://docs.python.org/3/library/functions.html#type "type")*[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException")*]**,* *BaseException**,* [*types.TracebackType*](https://docs.python.org/3/library/types.html#types.TracebackType "types.TracebackType")*]* *|* *None*) – An exception tuple with the current exception information,
          as returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"),
          or `None` if no exception information is available.
        - **func** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str") *|* *None*) – The name of the function or method
          from which the logging call was invoked.
        - **sinfo** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str") *|* *None*) – A text string representing stack information
          from the base of the s