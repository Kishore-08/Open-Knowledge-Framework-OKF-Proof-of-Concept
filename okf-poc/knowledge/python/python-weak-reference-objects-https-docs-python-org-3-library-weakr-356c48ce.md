---
id: python-weak-reference-objects-https-docs-python-org-3-library-weakr-356c48ce
type: concept
title: Weak Reference Objects[¶](https://docs.python.org/3/library/weakref.html#weak-reference-objects
  "Link to this heading")
description: Weak reference objects have no methods and no attributes besides
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/weakref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Weak Reference Objects[¶](https://docs.python.org/3/library/weakref.html#weak-reference-objects "Link to this heading")

Weak reference objects have no methods and no attributes besides
[`ref.__callback__`](https://docs.python.org/3/library/weakref.html#weakref.ref.__callback__ "weakref.ref.__callback__"). A weak reference object allows the referent to be
obtained, if it still exists, by calling it:

```
>>> import weakref
>>> class Object:
...     pass
...
>>> o = Object()
>>> r = weakref.ref(o)
>>> o2 = r()
>>> o is o2
True
```

If the referent no longer exists, calling the reference object returns
[`None`](https://docs.python.org/3/library/constants.html#None "None"):

```
>>> del o, o2
>>> print(r())
None
```

Testing that a weak reference object is still live should be done using the
expression `ref() is not None`. Normally, application code that needs to use
a reference object should follow this pattern:

```
# r is a weak reference object
o = r()
if o is None:
    # referent has been garbage collected
    print("Object has been deallocated; can't frobnicate.")
else:
    print("Object is still live!")
    o.do_something_useful()
```

Using a separate test for “liveness” creates race conditions in threaded
applications; another thread can cause a weak reference to become invalidated
before the weak reference is called; the idiom shown above is safe in threaded
applications as well as single-threaded applications.

Specialized versions of [`ref`](https://docs.python.org/3/library/weakref.html#weakref.ref "weakref.ref") objects can be created through subclassing.
This is used in the implementation of the [`WeakValueDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary "weakref.WeakValueDictionary") to reduce
the memory overhead for each entry in the mapping. This may be most useful to
associate additional information with a reference, but could also be used to
insert additional processing on calls to retrieve the referent.

This example shows how a subclass of [`ref`](https://docs.python.org/3/library/weakref.html#weakref.ref "weakref.ref") can be used to store
additional information about an object and affect the value that’s returned when
the referent is accessed:

```
import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, /, **annotations):
        super().__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super().__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob
```