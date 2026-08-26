---
id: python-concrete-exceptions-https-docs-python-org-3-library-exceptio-874b1988
type: concept
title: Concrete exceptions[¶](https://docs.python.org/3/library/exceptions.html#concrete-exceptions
  "Link to this heading")
description: The following exceptions are the exceptions that are usually raised.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/exceptions.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Concrete exceptions[¶](https://docs.python.org/3/library/exceptions.html#concrete-exceptions "Link to this heading")

The following exceptions are the exceptions that are usually raised.

*exception* AssertionError[¶](https://docs.python.org/3/library/exceptions.html#AssertionError "Link to this definition")
:   Raised when an [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement fails.

*exception* AttributeError[¶](https://docs.python.org/3/library/exceptions.html#AttributeError "Link to this definition")
:   Raised when an attribute reference (see [Attribute references](https://docs.python.org/3/reference/expressions.html#attribute-references)) or
    assignment fails. (When an object does not support attribute references or
    attribute assignments at all, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.)

    The optional *name* and *obj* keyword-only arguments
    set the corresponding attributes:

    name[¶](https://docs.python.org/3/library/exceptions.html#AttributeError.name "Link to this definition")
    :   The name of the attribute that was attempted to be accessed.

    obj[¶](https://docs.python.org/3/library/exceptions.html#AttributeError.obj "Link to this definition")
    :   The object that was accessed for the named attribute.

    Changed in version 3.10: Added the [`name`](https://docs.python.org/3/library/exceptions.html#AttributeError.name "AttributeError.name") and [`obj`](https://docs.python.org/3/library/exceptions.html#AttributeError.obj "AttributeError.obj") attributes.

*exception* EOFError[¶](https://docs.python.org/3/library/exceptions.html#EOFError "Link to this definition")
:   Raised when the [`input()`](https://docs.python.org/3/library/functions.html#input "input") function hits an end-of-file condition (EOF)
    without reading any data. (Note: the [`io.TextIOBase.read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read") and
    [`io.IOBase.readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") methods return an empty string when they hit EOF.)

*exception* FloatingPointError[¶](https://docs.python.org/3/library/exceptions.html#FloatingPointError "Link to this definition")
:   Not currently used.

*exception* GeneratorExit[¶](https://docs.python.org/3/library/exceptions.html#GeneratorExit "Link to this definition")
:   Raised when a [generator](https://docs.python.org/3/glossary.html#term-generator) or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) is closed;
    see [`generator.close()`](https://docs.python.org/3/reference/expressions.html#generator.close "generator.close") and [`coroutine.close()`](https://docs.python.org/3/reference/datamodel.html#coroutine.close "coroutine.close"). It
    directly inherits from [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") instead of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") since
    it is technically not an error.

*exception* ImportError[¶](https://docs.python.org/3/library/exceptions.html#ImportError "Link to this definition")
:   Raised when the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement has troubles trying to
    load a module. Also raised when the “from list” in `from ... import`
    has a name that cannot be found.

    The optional *name* and *path* keyword-only arguments
    set the corresponding attributes:

    name[¶](https://docs.python.org/3/library/exceptions.html#ImportError.name "Link to this definition")
    :   The name of the module that was attempted to be imported.

    path[¶](https://docs.python.org/3/library/exceptions.html#ImportError.path "Link to this definition")
    :   The path to any file which triggered the exception.

    Changed in version 3.3: Added the [`name`](https://docs.python.org/3/library/exceptions.