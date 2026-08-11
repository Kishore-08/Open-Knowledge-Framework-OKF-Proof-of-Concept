---
id: python-finalizer-objects-https-docs-python-org-3-library-weakref-ht-356c48ce
type: concept
title: Finalizer Objects[¶](https://docs.python.org/3/library/weakref.html#finalizer-objects
  "Link to this heading")
description: The main benefit of using [`finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize
  "weakref.finalize") is that it makes it simple
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/weakref.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Finalizer Objects[¶](https://docs.python.org/3/library/weakref.html#finalizer-objects "Link to this heading")

The main benefit of using [`finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize "weakref.finalize") is that it makes it simple
to register a callback without needing to preserve the returned finalizer
object. For instance

```
>>> import weakref
>>> class Object:
...     pass
...
>>> kenny = Object()
>>> weakref.finalize(kenny, print, "You killed Kenny!")
<finalize object at ...; for 'Object' at ...>
>>> del kenny
You killed Kenny!
```

The finalizer can be called directly as well. However the finalizer
will invoke the callback at most once.

```
>>> def callback(x, y, z):
...     print("CALLBACK")
...     return x + y + z
...
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> assert f.alive
>>> assert f() == 6
CALLBACK
>>> assert not f.alive
>>> f()                     # callback not called because finalizer dead
>>> del obj                 # callback not called because finalizer dead
```

You can unregister a finalizer using its [`detach()`](https://docs.python.org/3/library/weakref.html#weakref.finalize.detach "weakref.finalize.detach")
method. This kills the finalizer and returns the arguments passed to
the constructor when it was created.

```
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> f.detach()
(<...Object object ...>, <function callback ...>, (1, 2), {'z': 3})
>>> newobj, func, args, kwargs = _
>>> assert not f.alive
>>> assert newobj is obj
>>> assert func(*args, **kwargs) == 6
CALLBACK
```

Unless you set the [`atexit`](https://docs.python.org/3/library/weakref.html#weakref.finalize.atexit "weakref.finalize.atexit") attribute to
[`False`](https://docs.python.org/3/library/constants.html#False "False"), a finalizer will be called when the program exits if it
is still alive. For instance

```
>>> obj = Object()
>>> weakref.finalize(obj, print, "obj dead or exiting")
<finalize object at ...; for 'Object' at ...>
>>> exit()
obj dead or exiting
```