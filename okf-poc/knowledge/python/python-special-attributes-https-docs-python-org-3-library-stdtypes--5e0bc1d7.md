---
id: python-special-attributes-https-docs-python-org-3-library-stdtypes--5e0bc1d7
type: concept
title: Special Attributes[¶](https://docs.python.org/3/library/stdtypes.html#special-attributes
  "Link to this heading")
description: The implementation adds a few special read-only attributes to several
  object
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Special Attributes[¶](https://docs.python.org/3/library/stdtypes.html#special-attributes "Link to this heading")

The implementation adds a few special read-only attributes to several object
types, where they are relevant. Some of these are not reported by the
[`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") built-in function.

definition.\_\_name\_\_[¶](https://docs.python.org/3/library/stdtypes.html#definition.__name__ "Link to this definition")
:   The name of the class, function, method, descriptor, or
    generator instance.

definition.\_\_qualname\_\_[¶](https://docs.python.org/3/library/stdtypes.html#definition.__qualname__ "Link to this definition")
:   The [qualified name](https://docs.python.org/3/glossary.html#term-qualified-name) of the class, function, method, descriptor,
    or generator instance.

    Added in version 3.3.

definition.\_\_module\_\_[¶](https://docs.python.org/3/library/stdtypes.html#definition.__module__ "Link to this definition")
:   The name of the module in which a class or function was defined.

definition.\_\_doc\_\_[¶](https://docs.python.org/3/library/stdtypes.html#definition.__doc__ "Link to this definition")
:   The documentation string of a class or function, or `None` if undefined.

definition.\_\_type\_params\_\_[¶](https://docs.python.org/3/library/stdtypes.html#definition.__type_params__ "Link to this definition")
:   The [type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params) of generic classes, functions,
    and [type aliases](https://docs.python.org/3/library/typing.html#type-aliases). For classes and functions that
    are not generic, this will be an empty tuple.

    Added in version 3.12.