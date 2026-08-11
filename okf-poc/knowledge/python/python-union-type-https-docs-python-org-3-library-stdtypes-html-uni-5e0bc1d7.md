---
id: python-union-type-https-docs-python-org-3-library-stdtypes-html-uni-5e0bc1d7
type: concept
title: Union Type[¶](https://docs.python.org/3/library/stdtypes.html#union-type "Link
  to this heading")
description: A union object holds the value of the `|` (bitwise or) operation on
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Union Type[¶](https://docs.python.org/3/library/stdtypes.html#union-type "Link to this heading")

A union object holds the value of the `|` (bitwise or) operation on
multiple [type objects](https://docs.python.org/3/library/stdtypes.html#bltin-type-objects). These types are intended
primarily for [type annotations](https://docs.python.org/3/glossary.html#term-annotation). The union type expression
enables cleaner type hinting syntax compared to subscripting [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union").

X | Y | ...
:   Defines a union object which holds types *X*, *Y*, and so forth. `X | Y`
    means either X or Y. It is equivalent to `typing.Union[X, Y]`.
    For example, the following function expects an argument of type
    [`int`](https://docs.python.org/3/library/functions.html#int "int") or [`float`](https://docs.python.org/3/library/functions.html#float "float"):

    ```
    def square(number: int | float) -> int | float:
        return number ** 2
    ```

    Note

    The `|` operand cannot be used at runtime to define unions where one or
    more members is a forward reference. For example, `int | "Foo"`, where
    `"Foo"` is a reference to a class not yet defined, will fail at
    runtime. For unions which include forward references, present the
    whole expression as a string, e.g. `"int | Foo"`.

union\_object == other
:   Union objects can be tested for equality with other union objects. Details:

    - Unions of unions are flattened:

      ```
      (int | str) | float == int | str | float
      ```
    - Redundant types are removed:

      ```
      int | str | int == int | str
      ```
    - When comparing unions, the order is ignored:

      ```
      int | str == str | int
      ```
    - It creates instances of [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union"):

      ```
      int | str == typing.Union[int, str]
      type(int | str) is typing.Union
      ```
    - Optional types can be spelled as a union with `None`:

      ```
      str | None == typing.Optional[str]
      ```

isinstance(obj, union\_object)

issubclass(obj, union\_object)
:   Calls to [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") and [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") are also supported with a
    union object:

    ```
    >>> isinstance("", int | str)
    True
    ```

    However, [parameterized generics](https://docs.python.org/3/library/stdtypes.html#types-genericalias) in
    union objects cannot be checked:

    ```
    >>> isinstance(1, int | list[int])  # short-circuit evaluation
    True
    >>> isinstance([1], int | list[int])
    Traceback (most recent call last):
      ...
    TypeError: isinstance() argument 2 cannot be a parameterized generic
    ```

The user-exposed type for the union object can be accessed from
[`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union") and used for [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") checks:

```
>>> import typing
>>> isinstance(int | str, typing.Union)
True
>>> typing.Union()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot create 'typing.Union' instances
```

Note

The `__or__()` method for type objects was added to support the syntax
`X | Y`. If a metaclass implements `__or__()`, the Union may
override it:

```
>>> class M(type):
...     def __or__(self, other):
...         return "Hello"
...
>>> class C(metaclass=M):
...     pass
...
>>> C | int
'Hello'
>>> int | C
int | C
```

See also

[**PEP 604**](https://peps.python.org/pep-0604/) – PEP proposing the `X | Y` syntax and the Union type.

Added in version 3.10.

Changed in version 3.14: Union objects are now instances of [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Uni