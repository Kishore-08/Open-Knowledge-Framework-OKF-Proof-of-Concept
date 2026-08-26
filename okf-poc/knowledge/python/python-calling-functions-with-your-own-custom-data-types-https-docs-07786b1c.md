---
id: python-calling-functions-with-your-own-custom-data-types-https-docs-07786b1c
type: concept
title: Calling functions with your own custom data types[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types
  "Link to this heading")
description: You can also customize `ctypes` argument conversion to allow instances
  of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Calling functions with your own custom data types[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types "Link to this heading")

You can also customize `ctypes` argument conversion to allow instances of
your own classes be used as function arguments. `ctypes` looks for an
`_as_parameter_` attribute and uses this as the function argument. The
attribute must be an integer, string, bytes, a `ctypes` instance, or an
object with an `_as_parameter_` attribute:

```
>>> class Bottles:
...     def __init__(self, number):
...         self._as_parameter_ = number
...
>>> bottles = Bottles(42)
>>> printf(b"%d bottles of beer\n", bottles)
42 bottles of beer
19
>>>
```

If you don’t want to store the instance’s data in the `_as_parameter_`
instance variable, you could define a [`@property`](https://docs.python.org/3/library/functions.html#property "property") which makes the
attribute available on request.