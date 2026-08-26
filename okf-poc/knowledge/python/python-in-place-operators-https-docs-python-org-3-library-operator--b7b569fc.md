---
id: python-in-place-operators-https-docs-python-org-3-library-operator--b7b569fc
type: concept
title: In-place Operators[¶](https://docs.python.org/3/library/operator.html#in-place-operators
  "Link to this heading")
description: Many operations have an “in-place” version. Listed below are functions
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/operator.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## In-place Operators[¶](https://docs.python.org/3/library/operator.html#in-place-operators "Link to this heading")

Many operations have an “in-place” version. Listed below are functions
providing a more primitive access to in-place operators than the usual syntax
does; for example, the [statement](https://docs.python.org/3/glossary.html#term-statement) `x += y` is equivalent to
`x = operator.iadd(x, y)`. Another way to put it is to say that
`z = operator.iadd(x, y)` is equivalent to the compound statement
`z = x; z += y`.

In those examples, note that when an in-place method is called, the computation
and assignment are performed in two separate steps. The in-place functions
listed below only do the first step, calling the in-place method. The second
step, assignment, is not handled.

For immutable targets such as strings, numbers, and tuples, the updated
value is computed, but not assigned back to the input variable:

```
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'
```

For mutable targets such as lists and dictionaries, the in-place method
will perform the update, so no subsequent assignment is necessary:

```
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

operator.iadd(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.iadd "Link to this definition")

operator.\_\_iadd\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__iadd__ "Link to this definition")
:   `a = iadd(a, b)` is equivalent to `a += b`.

operator.iand(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.iand "Link to this definition")

operator.\_\_iand\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__iand__ "Link to this definition")
:   `a = iand(a, b)` is equivalent to `a &= b`.

operator.iconcat(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.iconcat "Link to this definition")

operator.\_\_iconcat\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__iconcat__ "Link to this definition")
:   `a = iconcat(a, b)` is equivalent to `a += b` for *a* and *b* sequences.

operator.ifloordiv(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.ifloordiv "Link to this definition")

operator.\_\_ifloordiv\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__ifloordiv__ "Link to this definition")
:   `a = ifloordiv(a, b)` is equivalent to `a //= b`.

operator.ilshift(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.ilshift "Link to this definition")

operator.\_\_ilshift\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__ilshift__ "Link to this definition")
:   `a = ilshift(a, b)` is equivalent to `a <<= b`.

operator.imod(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.imod "Link to this definition")

operator.\_\_imod\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__imod__ "Link to this definition")
:   `a = imod(a, b)` is equivalent to `a %= b`.

operator.imul(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.imul "Link to this definition")

operator.\_\_imul\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__imul__ "Link to this definition")
:   `a = imul(a, b)` is equivalent to `a *= b`.

operator.imatmul(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.imatmul "Link to this definition")

operator.\_\_imatmul\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__imatmul__ "Link to this definition")
:   `a = imatmul(a, b)` is equivalent to `a @= b`.

    Added in version 3.5.

operator.ior(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.ior "Link to this definition")

operator.\_\_ior\_\_(*a*, *b*)[¶](https://docs.python