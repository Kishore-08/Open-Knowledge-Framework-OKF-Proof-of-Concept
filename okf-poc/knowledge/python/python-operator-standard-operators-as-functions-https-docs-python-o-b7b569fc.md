---
id: python-operator-standard-operators-as-functions-https-docs-python-o-b7b569fc
type: concept
title: '`operator` — Standard operators as functions[¶](https://docs.python.org/3/librar'
description: '**Source code:** [Lib/operator.py](https://github.com/python/cpython/tree/3.14/Lib/operator.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/operator.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `operator` — Standard operators as functions[¶](https://docs.python.org/3/library/operator.html#module-operator "Link to this heading")

**Source code:** [Lib/operator.py](https://github.com/python/cpython/tree/3.14/Lib/operator.py)

---

The `operator` module exports a set of efficient functions corresponding to
the intrinsic operators of Python. For example, `operator.add(x, y)` is
equivalent to the expression `x+y`. Many function names are those used for
special methods, without the double underscores. For backward compatibility,
many of these have a variant with the double underscores kept. The variants
without the double underscores are preferred for clarity.

The functions fall into categories that perform object comparisons, logical
operations, mathematical operations and sequence operations.

The object comparison functions are useful for all objects, and are named after
the rich comparison operators they support:

operator.lt(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.lt "Link to this definition")

operator.le(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.le "Link to this definition")

operator.eq(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.eq "Link to this definition")

operator.ne(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.ne "Link to this definition")

operator.ge(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.ge "Link to this definition")

operator.gt(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.gt "Link to this definition")

operator.\_\_lt\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__lt__ "Link to this definition")

operator.\_\_le\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__le__ "Link to this definition")

operator.\_\_eq\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__eq__ "Link to this definition")

operator.\_\_ne\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__ne__ "Link to this definition")

operator.\_\_ge\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__ge__ "Link to this definition")

operator.\_\_gt\_\_(*a*, *b*)[¶](https://docs.python.org/3/library/operator.html#operator.__gt__ "Link to this definition")
:   Perform “rich comparisons” between *a* and *b*. Specifically, `lt(a, b)` is
    equivalent to `a < b`, `le(a, b)` is equivalent to `a <= b`, `eq(a,
    b)` is equivalent to `a == b`, `ne(a, b)` is equivalent to `a != b`,
    `gt(a, b)` is equivalent to `a > b` and `ge(a, b)` is equivalent to `a
    >= b`. Note that these functions can return any value, which may
    or may not be interpretable as a Boolean value. See
    [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) for more information about rich comparisons.

The logical operations are also generally applicable to all objects, and support
truth tests, identity tests, and boolean operations:

operator.not\_(*obj*)[¶](https://docs.python.org/3/library/operator.html#operator.not_ "Link to this definition")

operator.\_\_not\_\_(*obj*)[¶](https://docs.python.org/3/library/operator.html#operator.__not__ "Link to this definition")
:   Return the outcome of [`not`](https://docs.python.org/3/reference/expressions.html#not) *obj*. (Note that there is no
    `__not__()` method for object instances; only the interpreter core defines
    this operation. The result is affected by the [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__") and
    [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") methods.)

operator.truth(*obj*)[¶](https://docs.python.org/3/library/operator.html#operator.truth "Link to this definition")
:   Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if *obj* is true, and [`False`](https://