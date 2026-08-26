---
id: python-standard-interpreter-types-https-docs-python-org-3-library-t-3209cdc1
type: concept
title: Standard Interpreter Types[¶](https://docs.python.org/3/library/types.html#standard-interpreter-types
  "Link to this heading")
description: This module provides names for many of the types that are required to
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/types.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Standard Interpreter Types[¶](https://docs.python.org/3/library/types.html#standard-interpreter-types "Link to this heading")

This module provides names for many of the types that are required to
implement a Python interpreter. It deliberately avoids including some of
the types that arise only incidentally during processing such as the
`listiterator` type.

Typical use of these names is for [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") or
[`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") checks.

If you instantiate any of these types, note that signatures may vary between Python versions.

Standard names are defined for the following types:

*class* types.NoneType[¶](https://docs.python.org/3/library/types.html#types.NoneType "Link to this definition")
:   The type of [`None`](https://docs.python.org/3/library/constants.html#None "None").

    Added in version 3.10.

*class* types.FunctionType[¶](https://docs.python.org/3/library/types.html#types.FunctionType "Link to this definition")

*class* types.LambdaType[¶](https://docs.python.org/3/library/types.html#types.LambdaType "Link to this definition")
:   The type of user-defined functions and functions created by
    [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) expressions.

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `function.__new__` with argument `code`.

    The audit event only occurs for direct instantiation of function objects,
    and is not raised for normal compilation.

*class* types.GeneratorType[¶](https://docs.python.org/3/library/types.html#types.GeneratorType "Link to this definition")
:   The type of [generator](https://docs.python.org/3/glossary.html#term-generator)-iterator objects, created by
    generator functions.

*class* types.CoroutineType[¶](https://docs.python.org/3/library/types.html#types.CoroutineType "Link to this definition")
:   The type of [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) objects, created by
    [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions.

    Added in version 3.5.

*class* types.AsyncGeneratorType[¶](https://docs.python.org/3/library/types.html#types.AsyncGeneratorType "Link to this definition")
:   The type of [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)-iterator objects, created by
    asynchronous generator functions.

    Added in version 3.6.

*class* types.CodeType(*\*\*kwargs*)[¶](https://docs.python.org/3/library/types.html#types.CodeType "Link to this definition")
:   The type of [code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) such as returned by [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile").

    Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `code.__new__` with arguments `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags`.

    Note that the audited arguments may not match the names or positions
    required by the initializer. The audit event only occurs for direct
    instantiation of code objects, and is not raised for normal compilation.

*class* types.CellType[¶](https://docs.python.org/3/library/types.html#types.CellType "Link to this definition")
:   The type for cell objects: such objects are used as containers for
    a function’s [closure variables](https://docs.python.org/3/glossary.html#term-closure-variable).

    Added in version 3.8.

*class* types.MethodType[¶](https://docs.python.org/3/library/types.html#types.MethodType "Link to this definition")
:   The type of methods of user-defined class instances.

*class* types.BuiltinFunctionType[¶](https://docs.python.org/3/library/types.html#types.BuiltinFunctionType "Link to this definition")

*class* types.BuiltinMethodType[¶](h