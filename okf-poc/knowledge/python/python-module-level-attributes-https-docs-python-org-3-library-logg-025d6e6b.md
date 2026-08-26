---
id: python-module-level-attributes-https-docs-python-org-3-library-logg-025d6e6b
type: concept
title: Module-Level Attributes[¶](https://docs.python.org/3/library/logging.html#module-level-attributes
  "Link to this heading")
description: logging.lastResort[¶](https://docs.python.org/3/library/logging.html#logging.lastResort
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Module-Level Attributes[¶](https://docs.python.org/3/library/logging.html#module-level-attributes "Link to this heading")

logging.lastResort[¶](https://docs.python.org/3/library/logging.html#logging.lastResort "Link to this definition")
:   A “handler of last resort” is available through this attribute. This
    is a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") writing to `sys.stderr` with a level of
    `WARNING`, and is used to handle logging events in the absence of any
    logging configuration. The end result is to just print the message to
    `sys.stderr`. This replaces the earlier error message saying that
    “no handlers could be found for logger XYZ”. If you need the earlier
    behaviour for some reason, `lastResort` can be set to `None`.

    Added in version 3.2.

logging.raiseExceptions[¶](https://docs.python.org/3/library/logging.html#logging.raiseExceptions "Link to this definition")
:   Used to see if exceptions during handling should be propagated.

    Default: `True`.

    If `raiseExceptions` is `False`,
    exceptions get silently ignored. This is what is mostly wanted
    for a logging system - most users will not care about errors in
    the logging system, they are more interested in application errors.