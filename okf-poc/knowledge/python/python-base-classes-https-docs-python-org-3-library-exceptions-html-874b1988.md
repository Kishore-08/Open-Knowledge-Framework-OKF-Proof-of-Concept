---
id: python-base-classes-https-docs-python-org-3-library-exceptions-html-874b1988
type: concept
title: Base classes[¶](https://docs.python.org/3/library/exceptions.html#base-classes
  "Link to this heading")
description: The following exceptions are used mostly as base classes for other exceptions.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/exceptions.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Base classes[¶](https://docs.python.org/3/library/exceptions.html#base-classes "Link to this heading")

The following exceptions are used mostly as base classes for other exceptions.

*exception* BaseException[¶](https://docs.python.org/3/library/exceptions.html#BaseException "Link to this definition")
:   The base class for all built-in exceptions. It is not meant to be directly
    inherited by user-defined classes (for that, use [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception")). If
    [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") is called on an instance of this class, the representation of
    the argument(s) to the instance are returned, or the empty string when
    there were no arguments.

    args[¶](https://docs.python.org/3/library/exceptions.html#BaseException.args "Link to this definition")
    :   The tuple of arguments given to the exception constructor. Some built-in
        exceptions (like [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")) expect a certain number of arguments and
        assign a special meaning to the elements of this tuple, while others are
        usually called only with a single string giving an error message.

    with\_traceback(*tb*)[¶](https://docs.python.org/3/library/exceptions.html#BaseException.with_traceback "Link to this definition")
    :   This method sets *tb* as the new traceback for the exception and returns
        the exception object. It was more commonly used before the exception
        chaining features of [**PEP 3134**](https://peps.python.org/pep-3134/) became available. The following example
        shows how we can convert an instance of `SomeException` into an
        instance of `OtherException` while preserving the traceback. Once
        raised, the current frame is pushed onto the traceback of the
        `OtherException`, as would have happened to the traceback of the
        original `SomeException` had we allowed it to propagate to the caller.

        ```
        try:
            ...
        except SomeException:
            tb = sys.exception().__traceback__
            raise OtherException(...).with_traceback(tb)
        ```

    \_\_traceback\_\_[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "Link to this definition")
    :   A writable field that holds the
        [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects) associated with this
        exception. See also: [The raise statement](https://docs.python.org/3/reference/simple_stmts.html#raise).

    add\_note(*note*)[¶](https://docs.python.org/3/library/exceptions.html#BaseException.add_note "Link to this definition")
    :   Add the string `note` to the exception’s notes which appear in the standard
        traceback after the exception string. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if `note`
        is not a string.

        Added in version 3.11.

    \_\_notes\_\_[¶](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "Link to this definition")
    :   A list of the notes of this exception, which were added with [`add_note()`](https://docs.python.org/3/library/exceptions.html#BaseException.add_note "BaseException.add_note").
        This attribute is created when `add_note()` is called.

        Added in version 3.11.

*exception* Exception[¶](https://docs.python.org/3/library/exceptions.html#Exception "Link to this definition")
:   All built-in, non-system-exiting exceptions are derived from this class. All
    user-defined exceptions should also be derived from this class.

*exception* ArithmeticError[¶](https://docs.python.org/3/library/exceptions.html#ArithmeticError "Link to this definition")
:   The base class for those built-in exceptions that are raised for various
    arithmetic errors: [`OverflowError`](https://docs.python.org/3/library/exc