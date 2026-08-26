---
id: python-pickling-class-instances-https-docs-python-org-3-library-pic-f2bc33b8
type: concept
title: Pickling Class Instances[¶](https://docs.python.org/3/library/pickle.html#pickling-class-instances
  "Link to this heading")
description: In this section, we describe the general mechanisms available to you
  to define,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Pickling Class Instances[¶](https://docs.python.org/3/library/pickle.html#pickling-class-instances "Link to this heading")

In this section, we describe the general mechanisms available to you to define,
customize, and control how class instances are pickled and unpickled.

In most cases, no additional code is needed to make instances picklable. By
default, pickle will retrieve the class and the attributes of an instance via
introspection. When a class instance is unpickled, its [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method
is usually *not* invoked. The default behaviour first creates an uninitialized
instance and then restores the saved attributes. The following code shows an
implementation of this behaviour:

```
def save(obj):
    return (obj.__class__, obj.__dict__)

def restore(cls, attributes):
    obj = cls.__new__(cls)
    obj.__dict__.update(attributes)
    return obj
```

Classes can alter the default behaviour by providing one or several special
methods:

object.\_\_getnewargs\_ex\_\_()[¶](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "Link to this definition")
:   In protocols 2 and newer, classes that implement the
    `__getnewargs_ex__()` method can dictate the values passed to the
    [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method upon unpickling. The method must return a pair
    `(args, kwargs)` where *args* is a tuple of positional arguments
    and *kwargs* a dictionary of named arguments for constructing the
    object. Those will be passed to the `__new__()` method upon
    unpickling.

    You should implement this method if the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method of your
    class requires keyword-only arguments. Otherwise, it is recommended for
    compatibility to implement [`__getnewargs__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "object.__getnewargs__").

    Changed in version 3.6: `__getnewargs_ex__()` is now used in protocols 2 and 3.

object.\_\_getnewargs\_\_()[¶](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "Link to this definition")
:   This method serves a similar purpose as [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__"), but
    supports only positional arguments. It must return a tuple of arguments
    `args` which will be passed to the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method upon unpickling.

    `__getnewargs__()` will not be called if [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__") is
    defined.

    Changed in version 3.6: Before Python 3.6, `__getnewargs__()` was called instead of
    [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__") in protocols 2 and 3.

object.\_\_getstate\_\_()[¶](https://docs.python.org/3/library/pickle.html#object.__getstate__ "Link to this definition")
:   Classes can further influence how their instances are pickled by overriding
    the method `__getstate__()`. It is called and the returned object
    is pickled as the contents for the instance, instead of a default state.
    There are several cases:

    - For a class that has no instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") and no
      [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__"), the default state is `None`.
    - For a class that has an instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") and no
      [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__