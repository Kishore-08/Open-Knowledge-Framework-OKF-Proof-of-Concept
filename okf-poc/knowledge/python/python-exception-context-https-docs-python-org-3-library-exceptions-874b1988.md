---
id: python-exception-context-https-docs-python-org-3-library-exceptions-874b1988
type: concept
title: Exception context[¶](https://docs.python.org/3/library/exceptions.html#exception-context
  "Link to this heading")
description: Three attributes on exception objects provide information about the context
  in
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/exceptions.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Exception context[¶](https://docs.python.org/3/library/exceptions.html#exception-context "Link to this heading")

Three attributes on exception objects provide information about the context in
which the exception was raised:

BaseException.\_\_context\_\_[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "Link to this definition")

BaseException.\_\_cause\_\_[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "Link to this definition")

BaseException.\_\_suppress\_context\_\_[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__suppress_context__ "Link to this definition")
:   When raising a new exception while another exception
    is already being handled, the new exception’s
    `__context__` attribute is automatically set to the handled
    exception. An exception may be handled when an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) or
    [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause, or a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, is used.

    This implicit exception context can be
    supplemented with an explicit cause by using `from` with
    [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise):

    ```
    raise new_exc from original_exc
    ```

    The expression following [`from`](https://docs.python.org/3/reference/simple_stmts.html#raise) must be an exception or `None`. It
    will be set as `__cause__` on the raised exception. Setting
    `__cause__` also implicitly sets the `__suppress_context__`
    attribute to `True`, so that using `raise new_exc from None`
    effectively replaces the old exception with the new one for display
    purposes (e.g. converting [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") to [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError")), while
    leaving the old exception available in `__context__` for introspection
    when debugging.

    The default traceback display code shows these chained exceptions in
    addition to the traceback for the exception itself. An explicitly chained
    exception in `__cause__` is always shown when present. An implicitly
    chained exception in `__context__` is shown only if `__cause__`
    is [`None`](https://docs.python.org/3/library/constants.html#None "None") and `__suppress_context__` is false.

    In either case, the exception itself is always shown after any chained
    exceptions so that the final line of the traceback always shows the last
    exception that was raised.