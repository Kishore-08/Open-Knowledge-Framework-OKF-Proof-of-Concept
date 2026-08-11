---
id: python-methods-https-docs-python-org-3-library-stdtypes-html-method-5e0bc1d7
type: concept
title: Methods[¶](https://docs.python.org/3/library/stdtypes.html#methods "Link to
  this heading")
description: Methods are functions that are called using the attribute notation.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Methods[¶](https://docs.python.org/3/library/stdtypes.html#methods "Link to this heading")

Methods are functions that are called using the attribute notation.
There are two flavors: [built-in methods](https://docs.python.org/3/reference/datamodel.html#builtin-methods)
(such as [`append()`](https://docs.python.org/3/library/stdtypes.html#list.append "list.append") on lists)
and [class instance method](https://docs.python.org/3/reference/datamodel.html#instance-methods).
Built-in methods are described with the types that support them.

If you access a method (a function defined in a class namespace) through an
instance, you get a special object: a *bound method* (also called
[instance method](https://docs.python.org/3/reference/datamodel.html#instance-methods)) object. When called, it will add
the `self` argument
to the argument list. Bound methods have two special read-only attributes:
[`m.__self__`](https://docs.python.org/3/reference/datamodel.html#method.__self__ "method.__self__") is the object on which the method
operates, and [`m.__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__") is
the function implementing the method. Calling `m(arg-1, arg-2, ..., arg-n)`
is completely equivalent to calling `m.__func__(m.__self__, arg-1, arg-2, ...,
arg-n)`.

Like [function objects](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs), bound method objects support
getting arbitrary
attributes. However, since method attributes are actually stored on the
underlying function object ([`method.__func__`](https://docs.python.org/3/reference/datamodel.html#method.__func__ "method.__func__")), setting method attributes on
bound methods is disallowed. Attempting to set an attribute on a method
results in an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") being raised. In order to set a method
attribute, you need to explicitly set it on the underlying function object:

```
>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'method' object has no attribute 'whoami'
>>> c.method.__func__.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'
```

See [Instance methods](https://docs.python.org/3/reference/datamodel.html#instance-methods) for more information.