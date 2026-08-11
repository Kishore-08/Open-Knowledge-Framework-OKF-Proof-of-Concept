---
id: python-context-manager-types-https-docs-python-org-3-library-stdtyp-5e0bc1d7
type: concept
title: Context Manager Types[¶](https://docs.python.org/3/library/stdtypes.html#context-manager-types
  "Link to this heading")
description: Python’s [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
  statement supports the concept of a runtime context
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Context Manager Types[¶](https://docs.python.org/3/library/stdtypes.html#context-manager-types "Link to this heading")

Python’s [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement supports the concept of a runtime context
defined by a context manager. This is implemented using a pair of methods
that allow user-defined classes to define a runtime context that is entered
before the statement body is executed and exited when the statement ends:

contextmanager.\_\_enter\_\_()[¶](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "Link to this definition")
:   Enter the runtime context and return either this object or another object
    related to the runtime context. The value returned by this method is bound to
    the identifier in the `as` clause of [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statements using
    this context manager.

    An example of a context manager that returns itself is a [file object](https://docs.python.org/3/glossary.html#term-file-object).
    File objects return themselves from \_\_enter\_\_() to allow [`open()`](https://docs.python.org/3/library/functions.html#open "open") to be
    used as the context expression in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.

    An example of a context manager that returns a related object is the one
    returned by [`decimal.localcontext()`](https://docs.python.org/3/library/decimal.html#decimal.localcontext "decimal.localcontext"). These managers set the active
    decimal context to a copy of the original decimal context and then return the
    copy. This allows changes to be made to the current decimal context in the body
    of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement without affecting code outside the
    `with` statement.

contextmanager.\_\_exit\_\_(*exc\_type*, *exc\_val*, *exc\_tb*)[¶](https://docs.python.org/3/library/stdtypes.html#contextmanager.__exit__ "Link to this definition")
:   Exit the runtime context and return a Boolean flag indicating if any exception
    that occurred should be suppressed. If an exception occurred while executing the
    body of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, the arguments contain the exception type,
    value and traceback information. Otherwise, all three arguments are `None`.

    Returning a true value from this method will cause the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement
    to suppress the exception and continue execution with the statement immediately
    following the `with` statement. Otherwise the exception continues
    propagating after this method has finished executing.

    If this method raises an exception while handling an earlier exception from the
    [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) block, the new exception is raised, and the original exception
    is stored in its [`__context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "BaseException.__context__") attribute.

    The exception passed in should never be reraised explicitly - instead, this
    method should return a false value to indicate that the method completed
    successfully and does not want to suppress the raised exception. This allows
    context management code to easily detect whether or not an [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
    method has actually failed.

Python defines several context managers to support easy thread synchronisation,
prompt closure of files or other objects, and simpler manipulation of the active
decimal arithmetic context. The specific types are not treated specially beyond
their implementation of the context management protocol. See the
[`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "c