---
id: python-custom-reduction-for-types-functions-and-other-objects-https-f2bc33b8
type: concept
title: Custom Reduction for Types, Functions, and Other Objects[¶](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects
  "Link to this heading")
description: Added in version 3.8.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Custom Reduction for Types, Functions, and Other Objects[¶](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects "Link to this heading")

Added in version 3.8.

Sometimes, [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") may not be flexible enough.
In particular we may want to customize pickling based on another criterion
than the object’s type, or we may want to customize the pickling of
functions and classes.

For those cases, it is possible to subclass from the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") class and
implement a [`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") method. This method can return an
arbitrary reduction tuple (see [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__")). It can alternatively return
[`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") to fallback to the traditional behavior.

If both the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") and
[`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") are defined, then
`reducer_override()` method takes priority.

Note

For performance reasons, [`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") may not be
called for the following objects: `None`, `True`, `False`, and
exact instances of [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"),
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list")
and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").

Here is a simple example where we allow pickling and reconstructing
a given class:

```
import io
import pickle

class MyClass:
    my_attribute = 1

class MyPickler(pickle.Pickler):
    def reducer_override(self, obj):
        """Custom reducer for MyClass."""
        if getattr(obj, "__name__", None) == "MyClass":
            return type, (obj.__name__, obj.__bases__,
                          {'my_attribute': obj.my_attribute})
        else:
            # For any other object, fallback to usual reduction
            return NotImplemented

f = io.BytesIO()
p = MyPickler(f)
p.dump(MyClass)

del MyClass

unpickled_class = pickle.loads(f.getvalue())

assert isinstance(unpickled_class, type)
assert unpickled_class.__name__ == "MyClass"
assert unpickled_class.my_attribute == 1
```