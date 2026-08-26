---
id: python-logger-objects-https-docs-python-org-3-library-logging-html--025d6e6b
type: concept
title: Logger Objects[¶](https://docs.python.org/3/library/logging.html#logger-objects
  "Link to this heading")
description: Loggers have the following attributes and methods. Note that Loggers
  should
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Logger Objects[¶](https://docs.python.org/3/library/logging.html#logger-objects "Link to this heading")

Loggers have the following attributes and methods. Note that Loggers should
*NEVER* be instantiated directly, but always through the module-level function
`logging.getLogger(name)`. Multiple calls to [`getLogger()`](https://docs.python.org/3/library/logging.html#logging.getLogger "logging.getLogger") with the same
name will always return a reference to the same Logger object.

The `name` is potentially a period-separated hierarchical value, like
`foo.bar.baz` (though it could also be just plain `foo`, for example).
Loggers that are further down in the hierarchical list are children of loggers
higher up in the list. For example, given a logger with a name of `foo`,
loggers with names of `foo.bar`, `foo.bar.baz`, and `foo.bam` are all
descendants of `foo`. In addition, all loggers are descendants of the root
logger. The logger name hierarchy is analogous to the Python package hierarchy,
and identical to it if you organise your loggers on a per-module basis using
the recommended construction `logging.getLogger(__name__)`. That’s because
in a module, `__name__` is the module’s name in the Python package namespace.

*class* logging.Logger[¶](https://docs.python.org/3/library/logging.html#logging.Logger "Link to this definition")
:   name[¶](https://docs.python.org/3/library/logging.html#logging.Logger.name "Link to this definition")
    :   This is the logger’s name, and is the value that was passed to [`getLogger()`](https://docs.python.org/3/library/logging.html#logging.getLogger "logging.getLogger")
        to obtain the logger.

        Note

        This attribute should be treated as read-only.

    level[¶](https://docs.python.org/3/library/logging.html#logging.Logger.level "Link to this definition")
    :   The threshold of this logger, as set by the [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel") method.

        Note

        Do not set this attribute directly - always use [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel"),
        which has checks for the level passed to it.

    parent[¶](https://docs.python.org/3/library/logging.html#logging.Logger.parent "Link to this definition")
    :   The parent logger of this logger. It may change based on later instantiation
        of loggers which are higher up in the namespace hierarchy.

        Note

        This value should be treated as read-only.

    propagate[¶](https://docs.python.org/3/library/logging.html#logging.Logger.propagate "Link to this definition")
    :   If this attribute evaluates to true, events logged to this logger will be
        passed to the handlers of higher level (ancestor) loggers, in addition to
        any handlers attached to this logger. Messages are passed directly to the
        ancestor loggers’ handlers - neither the level nor filters of the ancestor
        loggers in question are considered.

        If this evaluates to false, logging messages are not passed to the handlers
        of ancestor loggers.

        Spelling it out with an example: If the propagate attribute of the logger named
        `A.B.C` evaluates to true, any event logged to `A.B.C` via a method call such as
        `logging.getLogger('A.B.C').error(...)` will [subject to passing that logger’s
        level and filter settings] be passed in turn to any handlers attached to loggers
        named `A.B`, `A` and the root logger, after first being passed to any handlers
        attached to `A.B.C`. If any logger in the chain `A.B.C`, `A.B`, `A` has its
        `propagate` attribute set to false, then that is the last logger whose handlers
        are offered the event to handle, and propagation stops at that point.

        The constructor sets this attribute to `True`.

        Note

        If you attach a handler to a logger *and* one