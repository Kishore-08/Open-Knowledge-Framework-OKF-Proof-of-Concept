---
id: python-integration-with-the-warnings-module-https-docs-python-org-3-025d6e6b
type: concept
title: Integration with the warnings module[¶](https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module
  "Link to this heading")
description: The [`captureWarnings()`](https://docs.python.org/3/library/logging.html#logging.captureWarnings
  "logging.captureWarnings") function can be used to integrate `logging`
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Integration with the warnings module[¶](https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module "Link to this heading")

The [`captureWarnings()`](https://docs.python.org/3/library/logging.html#logging.captureWarnings "logging.captureWarnings") function can be used to integrate `logging`
with the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module.

logging.captureWarnings(*capture*)[¶](https://docs.python.org/3/library/logging.html#logging.captureWarnings "Link to this definition")
:   This function is used to turn the capture of warnings by logging on and
    off.

    If *capture* is `True`, warnings issued by the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module will
    be redirected to the logging system. Specifically, a warning will be
    formatted using [`warnings.formatwarning()`](https://docs.python.org/3/library/warnings.html#warnings.formatwarning "warnings.formatwarning") and the resulting string
    logged to a logger named `'py.warnings'` with a severity of [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING").

    If *capture* is `False`, the redirection of warnings to the logging system
    will stop, and warnings will be redirected to their original destinations
    (i.e. those in effect before `captureWarnings(True)` was called).

See also

Module [`logging.config`](https://docs.python.org/3/library/logging.config.html#module-logging.config "logging.config: Configuration of the logging module.")
:   Configuration API for the logging module.

Module [`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.")
:   Useful handlers included with the logging module.

[**PEP 282**](https://peps.python.org/pep-0282/) - A Logging System
:   The proposal which described this feature for inclusion in the Python standard
    library.

[Original Python logging package](https://old.red-dove.com/python_logging.html)
:   This is the original source for the `logging` package. The version of the
    package available from this site is suitable for use with Python 1.5.2, 2.1.x
    and 2.2.x, which do not include the `logging` package in the standard
    library.