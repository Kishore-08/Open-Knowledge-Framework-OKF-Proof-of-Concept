---
id: python-loggeradapter-objects-https-docs-python-org-3-library-loggin-025d6e6b
type: concept
title: LoggerAdapter Objects[¶](https://docs.python.org/3/library/logging.html#loggeradapter-objects
  "Link to this heading")
description: '[`LoggerAdapter`](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter
  "logging.LoggerAdapter") instances are used to conveniently pass contextual'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## LoggerAdapter Objects[¶](https://docs.python.org/3/library/logging.html#loggeradapter-objects "Link to this heading")

[`LoggerAdapter`](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter "logging.LoggerAdapter") instances are used to conveniently pass contextual
information into logging calls. For a usage example, see the section on
[adding contextual information to your logging output](https://docs.python.org/3/howto/logging-cookbook.html#context-info).

*class* logging.LoggerAdapter(*logger*, *extra=None*, *merge\_extra=False*)[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter "Link to this definition")
:   Returns an instance of `LoggerAdapter` initialized with an
    underlying [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") instance, an optional dict-like object (*extra*),
    and an optional boolean (*merge\_extra*) indicating whether or not
    the *extra* argument of individual log calls should be merged with
    the `LoggerAdapter` extra.
    The default behavior is to ignore the *extra* argument of individual log
    calls and only use the one of the `LoggerAdapter` instance

    process(*msg*, *kwargs*)[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter.process "Link to this definition")
    :   Modifies the message and/or keyword arguments passed to a logging call in
        order to insert contextual information. This implementation takes the object
        passed as *extra* to the constructor and adds it to *kwargs* using key
        ‘extra’. The return value is a (*msg*, *kwargs*) tuple which has the
        (possibly modified) versions of the arguments passed in.

    manager[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter.manager "Link to this definition")
    :   Delegates to the underlying `manager` on *logger*.

    \_log[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter._log "Link to this definition")
    :   Delegates to the underlying `_log()` method on *logger*.

    In addition to the above, `LoggerAdapter` supports the following
    methods of [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger"): [`debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug"), [`info()`](https://docs.python.org/3/library/logging.html#logging.Logger.info "logging.Logger.info"),
    [`warning()`](https://docs.python.org/3/library/logging.html#logging.Logger.warning "logging.Logger.warning"), [`error()`](https://docs.python.org/3/library/logging.html#logging.Logger.error "logging.Logger.error"), [`exception()`](https://docs.python.org/3/library/logging.html#logging.Logger.exception "logging.Logger.exception"),
    [`critical()`](https://docs.python.org/3/library/logging.html#logging.Logger.critical "logging.Logger.critical"), [`log()`](https://docs.python.org/3/library/logging.html#logging.Logger.log "logging.Logger.log"), [`isEnabledFor()`](https://docs.python.org/3/library/logging.html#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"),
    [`getEffectiveLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"), [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel") and
    [`hasHandlers()`](https://docs.python.org/3/library/logging.html#logging.Logger.hasHandlers "logging.Logger.hasHandlers"). These methods have the same signatures as their
    counterparts in `Logger`, so you can use the two types of instances
    interchangeably.

    Changed in version 3.2: The [`isEnabledFor()`](https://docs.python.org/3/library/logging.html#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"), [`getEffectiveLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"),
    [`setLevel()`](https://docs.p