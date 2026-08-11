---
id: python-code-objects-https-docs-python-org-3-library-stdtypes-html-c-5e0bc1d7
type: concept
title: Code Objects[¶](https://docs.python.org/3/library/stdtypes.html#code-objects
  "Link to this heading")
description: Code objects are used by the implementation to represent “pseudo-compiled”
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Code Objects[¶](https://docs.python.org/3/library/stdtypes.html#code-objects "Link to this heading")

Code objects are used by the implementation to represent “pseudo-compiled”
executable Python code such as a function body. They differ from function
objects because they don’t contain a reference to their global execution
environment. Code objects are returned by the built-in [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") function
and can be extracted from function objects through their
[`__code__`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__") attribute. See also the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module.

Accessing [`__code__`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__") raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
`object.__getattr__` with arguments `obj` and `"__code__"`.

A code object can be executed or evaluated by passing it (instead of a source
string) to the [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") or [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") built-in functions.

See [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types) for more information.