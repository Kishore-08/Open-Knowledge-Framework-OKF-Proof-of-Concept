---
id: python-formatter-objects-https-docs-python-org-3-library-logging-ht-025d6e6b
type: concept
title: Formatter Objects[¶](https://docs.python.org/3/library/logging.html#formatter-objects
  "Link to this heading")
description: '*class* logging.Formatter(*fmt=None*, *datefmt=None*, *style=''%''*,
  *validate=True*, *\**, *defaults=None*)[¶](https://docs.python.org/3/library/logging.html#logging.Formatter
  "Link to this definition"'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Formatter Objects[¶](https://docs.python.org/3/library/logging.html#formatter-objects "Link to this heading")

*class* logging.Formatter(*fmt=None*, *datefmt=None*, *style='%'*, *validate=True*, *\**, *defaults=None*)[¶](https://docs.python.org/3/library/logging.html#logging.Formatter "Link to this definition")
:   Responsible for converting a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") to an output string
    to be interpreted by a human or external system.

    Parameters:
    :   - **fmt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – A format string in the given *style* for
          the logged output as a whole.
          The possible mapping keys are drawn from the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") object’s
          [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes).
          If not specified, `'%(message)s'` is used,
          which is just the logged message.
        - **datefmt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – A format string for the date/time portion of the logged output.
          If not specified, the default described in [`formatTime()`](https://docs.python.org/3/library/logging.html#logging.Formatter.formatTime "logging.Formatter.formatTime") is used.
        - **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – Can be one of `'%'`, `'{'` or `'$'` and determines
          how the format string will be merged with its data: using one of
          [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) (`%`), [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") (`{`)
          or [`string.Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") (`$`). This only applies to
          *fmt* (e.g. `'%(message)s'` versus `'{message}'`),
          not to the actual log messages passed to the logging methods.
          However, there are [other ways](https://docs.python.org/3/howto/logging-cookbook.html#formatting-styles)
          to use `{`- and `$`-formatting for log messages.
        - **validate** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True` (the default), incorrect or mismatched
          *fmt* and *style* will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"); for example,
          `logging.Formatter('%(asctime)s - %(message)s', style='{')`.
        - **defaults** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "dict")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "str")*,* *Any**]*) – A dictionary with default values to use in custom fields.
          For example,
          `logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})`

    Changed in version 3.2: Added the *style* parameter.

    Changed in version 3.8: Added the *validate* parameter.

    Changed in version 3.10: Added the *defaults* parameter.

    format(*record*)[¶](https://docs.python.org/3/library/logging.html#logging.Formatter.format "Link to this definition")
    :   The record’s attribute dictionary is used as the operand to a string
        formatting operation. Returns the resulting string. Before formatting the
        dictionary, a couple of preparatory steps are carried out. The *message*
        attribute of the record is computed using *msg* % *args*. If the
        formatting string contains `'(asctime)'`, [`formatTime()`](https://docs.python.org/3/library/logging.html#logging.Formatter.formatTime "logging.Formatter.formatTime") is called
        to format the event time. If there is exception information, it is
        formatted using [`formatException()`](https://docs.python.org/3/library/logging.html#logging.Formatter.formatExceptio