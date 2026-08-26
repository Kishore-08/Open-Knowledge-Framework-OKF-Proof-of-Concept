---
id: python-logging-levels-https-docs-python-org-3-library-logging-html--025d6e6b
type: concept
title: Logging Levels[¶](https://docs.python.org/3/library/logging.html#logging-levels
  "Link to this heading")
description: The numeric values of logging levels are given in the following table.
  These are
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Logging Levels[¶](https://docs.python.org/3/library/logging.html#logging-levels "Link to this heading")

The numeric values of logging levels are given in the following table. These are
primarily of interest if you want to define your own levels, and need them to
have specific values relative to the predefined levels. If you define a level
with the same numeric value, it overwrites the predefined value; the predefined
name is lost.

| Level | Numeric value | What it means / When to use it |
| --- | --- | --- |
| logging.NOTSET[¶](https://docs.python.org/3/library/logging.html#logging.NOTSET "Link to this definition") | 0 | When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to `NOTSET`, then all events are logged. When set on a handler, all events are handled. |
| logging.DEBUG[¶](https://docs.python.org/3/library/logging.html#logging.DEBUG "Link to this definition") | 10 | Detailed information, typically only of interest to a developer trying to diagnose a problem. |
| logging.INFO[¶](https://docs.python.org/3/library/logging.html#logging.INFO "Link to this definition") | 20 | Confirmation that things are working as expected. |
| logging.WARNING[¶](https://docs.python.org/3/library/logging.html#logging.WARNING "Link to this definition") | 30 | An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| logging.ERROR[¶](https://docs.python.org/3/library/logging.html#logging.ERROR "Link to this definition") | 40 | Due to a more serious problem, the software has not been able to perform some function. |
| logging.CRITICAL[¶](https://docs.python.org/3/library/logging.html#logging.CRITICAL "Link to this definition") | 50 | A serious error, indicating that the program itself may be unable to continue running. |