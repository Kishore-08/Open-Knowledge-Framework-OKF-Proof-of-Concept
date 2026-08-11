---
id: python-exception-groups-https-docs-python-org-3-library-exceptions--874b1988
type: concept
title: Exception groups[¶](https://docs.python.org/3/library/exceptions.html#exception-groups
  "Link to this heading")
description: The following are used when it is necessary to raise multiple unrelated
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/exceptions.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Exception groups[¶](https://docs.python.org/3/library/exceptions.html#exception-groups "Link to this heading")

The following are used when it is necessary to raise multiple unrelated
exceptions. They are part of the exception hierarchy so they can be
handled with [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) like all other exceptions. In addition,
they are recognised by [`except*`](https://docs.python.org/3/reference/compound_stmts.html#except-star), which matches
their subgroups based on the types of the contained exceptions.

*exception* ExceptionGroup(*msg*, *excs*)[¶](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "Link to this definition")

*exception* BaseExceptionGroup(*msg*, *excs*)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "Link to this definition")
:   Both of these exception types wrap the exceptions in the sequence `excs`.
    The `msg` parameter must be a string. The difference between the two
    classes is that `BaseExceptionGroup` extends [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") and
    it can wrap any exception, while [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup") extends [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception")
    and it can only wrap subclasses of `Exception`. This design is so that
    `except Exception` catches an `ExceptionGroup` but not
    `BaseExceptionGroup`.

    The `BaseExceptionGroup` constructor returns an [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup")
    rather than a `BaseExceptionGroup` if all contained exceptions are
    [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") instances, so it can be used to make the selection
    automatic. The `ExceptionGroup` constructor, on the other hand,
    raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if any contained exception is not an
    `Exception` subclass.

    Exception groups are [generic](https://docs.python.org/3/library/typing.html#generics) over the type of their
    contained exceptions.

    **CPython implementation detail:** The `excs` parameter may be any sequence, but lists and tuples are
    specifically processed more efficiently here. For optimal performance,
    pass a tuple as `excs`.

    message[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.message "Link to this definition")
    :   The `msg` argument to the constructor. This is a read-only attribute.

    exceptions[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.exceptions "Link to this definition")
    :   A tuple of the exceptions in the `excs` sequence given to the
        constructor. This is a read-only attribute.

    subgroup(*condition*)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.subgroup "Link to this definition")
    :   Returns an exception group that contains only the exceptions from the
        current group that match *condition*, or `None` if the result is empty.

        The condition can be an exception type or tuple of exception types, in which
        case each exception is checked for a match using the same check that is used
        in an `except` clause. The condition can also be a callable (other than
        a type object) that accepts an exception as its single argument and returns
        true for the exceptions that should be in the subgroup.

        The nesting structure of the current exception is preserved in the result,
        as are the values of its [`message`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.message "BaseExceptionGroup.message"),
        [`__traceback__`](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "BaseException.__traceba