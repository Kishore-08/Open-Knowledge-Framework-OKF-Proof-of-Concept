---
id: python-built-in-constants-https-docs-python-org-3-library-constants-a8c4ec5e
type: concept
title: Built-in Constants[¶](https://docs.python.org/3/library/constants.html#built-in-
description: 'A small number of constants live in the built-in namespace. They are:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/constants.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# Built-in Constants[¶](https://docs.python.org/3/library/constants.html#built-in-constants "Link to this heading")

A small number of constants live in the built-in namespace. They are:

False[¶](https://docs.python.org/3/library/constants.html#False "Link to this definition")
:   The false value of the [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") type. Assignments to `False`
    are illegal and raise a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError").

True[¶](https://docs.python.org/3/library/constants.html#True "Link to this definition")
:   The true value of the [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") type. Assignments to `True`
    are illegal and raise a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError").

None[¶](https://docs.python.org/3/library/constants.html#None "Link to this definition")
:   An object frequently used to represent the absence of a value, as when
    default arguments are not passed to a function. Assignments to `None`
    are illegal and raise a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError").
    `None` is the sole instance of the [`NoneType`](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType") type.

NotImplemented[¶](https://docs.python.org/3/library/constants.html#NotImplemented "Link to this definition")
:   A special value which should be returned by the binary special methods
    (e.g. [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"), [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__"), [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__"), [`__rsub__()`](https://docs.python.org/3/reference/datamodel.html#object.__rsub__ "object.__rsub__"),
    etc.) to indicate that the operation is not implemented with respect to
    the other type; may be returned by the in-place binary special methods
    (e.g. [`__imul__()`](https://docs.python.org/3/reference/datamodel.html#object.__imul__ "object.__imul__"), [`__iand__()`](https://docs.python.org/3/reference/datamodel.html#object.__iand__ "object.__iand__"), etc.) for the same purpose.
    It should not be evaluated in a boolean context.
    `NotImplemented` is the sole instance of the [`types.NotImplementedType`](https://docs.python.org/3/library/types.html#types.NotImplementedType "types.NotImplementedType") type.

    Note

    When a binary (or in-place) method returns `NotImplemented` the
    interpreter will try the reflected operation on the other type (or some
    other fallback, depending on the operator). If all attempts return
    `NotImplemented`, the interpreter will raise an appropriate exception.
    Incorrectly returning `NotImplemented` will result in a misleading
    error message or the `NotImplemented` value being returned to Python code.

    See [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations) for examples.

    Caution

    `NotImplemented` and `NotImplementedError` are not
    interchangeable. This constant should only be used as described
    above; see [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") for details on correct usage
    of the exception.

    Changed in version 3.9: Evaluating `NotImplemented` in a boolean context was deprecated.

    Changed in version 3.14: Evaluating `NotImplemented` in a boolean context now raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
    It previously evaluated to [`True`](https://docs.python.org/3/library/constants.html#True "True") and emitted a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarnin