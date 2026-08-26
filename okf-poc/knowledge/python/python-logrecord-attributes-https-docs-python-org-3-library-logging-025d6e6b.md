---
id: python-logrecord-attributes-https-docs-python-org-3-library-logging-025d6e6b
type: concept
title: LogRecord attributes[¶](https://docs.python.org/3/library/logging.html#logrecord-attributes
  "Link to this heading")
description: The LogRecord has a number of attributes, most of which are derived from
  the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## LogRecord attributes[¶](https://docs.python.org/3/library/logging.html#logrecord-attributes "Link to this heading")

The LogRecord has a number of attributes, most of which are derived from the
parameters to the constructor. (Note that the names do not always correspond
exactly between the LogRecord constructor parameters and the LogRecord
attributes.) These attributes can be used to merge data from the record into
the format string. The following table lists (in alphabetical order) the
attribute names, their meanings and the corresponding placeholder in a %-style
format string.

If you are using {}-formatting ([`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format")), you can use
`{attrname}` as the placeholder in the format string. If you are using
$-formatting ([`string.Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template")), use the form `${attrname}`. In
both cases, of course, replace `attrname` with the actual attribute name
you want to use.

In the case of {}-formatting, you can specify formatting flags by placing them
after the attribute name, separated from it with a colon. For example: a
placeholder of `{msecs:03.0f}` would format a millisecond value of `4` as
`004`. Refer to the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") documentation for full details on
the options available to you.

| Attribute name | Format | Description |
| --- | --- | --- |
| args | You shouldn’t need to format this yourself. | The tuple of arguments merged into `msg` to produce `message`, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary). |
| asctime | `%(asctime)s` | Human-readable time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time). |
| created | `%(created)f` | Time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") was created (as returned by [`time.time_ns()`](https://docs.python.org/3/library/time.html#time.time_ns "time.time_ns") / 1e9). |
| exc\_info | You shouldn’t need to format this yourself. | Exception tuple (à la `sys.exc_info`) or, if no exception has occurred, `None`. |
| exc\_text | You shouldn’t need to format this yourself. | Exception information formatted as a string. This is set when [`Formatter.format()`](https://docs.python.org/3/library/logging.html#logging.Formatter.format "logging.Formatter.format") is invoked, or `None` if no exception has occurred. |
| filename | `%(filename)s` | Filename portion of `pathname`. |
| funcName | `%(funcName)s` | Name of function containing the logging call. |
| levelname | `%(levelname)s` | Text logging level for the message (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`). |
| levelno | `%(levelno)s` | Numeric logging level for the message ([`DEBUG`](https://docs.python.org/3/library/logging.html#logging.DEBUG "logging.DEBUG"), [`INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO"), [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING"), [`ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR"), [`CRITICAL`](https://docs.python.org/3/library/logging.html#logging.CRITICAL "logging.CRITICAL")). |
| lineno | `%(lineno)d` | Source line number where the logging call was issued (if available). |
| message | `%(message)s` | The logged message, computed as `msg % args`. This is set when [`Formatter.format()`](https://docs.python.org/3/library/logging.html#logging.Formatter.format "logging.Formatter.format") is invoked. |
| module | `%(module)s` | Module (name portion of `filename`). |
| msecs | `%(msecs)d` | Millisecond portion of the time when the [`LogRecord`]