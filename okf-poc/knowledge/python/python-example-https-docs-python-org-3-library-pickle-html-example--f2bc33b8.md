---
id: python-example-https-docs-python-org-3-library-pickle-html-example--f2bc33b8
type: concept
title: Example[¶](https://docs.python.org/3/library/pickle.html#example "Link to this
  heading")
description: Here is a trivial example where we implement a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray
  "bytearray") subclass
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Example[¶](https://docs.python.org/3/library/pickle.html#example "Link to this heading")

Here is a trivial example where we implement a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") subclass
able to participate in out-of-band buffer pickling:

```
class ZeroCopyByteArray(bytearray):

    def __reduce_ex__(self, protocol):
        if protocol >= 5:
            return type(self)._reconstruct, (PickleBuffer(self),), None
        else:
            # PickleBuffer is forbidden with pickle protocols <= 4.
            return type(self)._reconstruct, (bytearray(self),)

    @classmethod
    def _reconstruct(cls, obj):
        with memoryview(obj) as m:
            # Get a handle over the original buffer object
            obj = m.obj
            if type(obj) is cls:
                # Original buffer object is a ZeroCopyByteArray, return it
                # as-is.
                return obj
            else:
                return cls(obj)
```

The reconstructor (the `_reconstruct` class method) returns the buffer’s
providing object if it has the right type. This is an easy way to simulate
zero-copy behaviour on this toy example.

On the consumer side, we can pickle those objects the usual way, which
when unserialized will give us a copy of the original object:

```
b = ZeroCopyByteArray(b"abc")
data = pickle.dumps(b, protocol=5)
new_b = pickle.loads(data)
print(b == new_b)  # True
print(b is new_b)  # False: a copy was made
```

But if we pass a *buffer\_callback* and then give back the accumulated
buffers when unserializing, we are able to get back the original object:

```
b = ZeroCopyByteArray(b"abc")
buffers = []
data = pickle.dumps(b, protocol=5, buffer_callback=buffers.append)
new_b = pickle.loads(data, buffers=buffers)
print(b == new_b)  # True
print(b is new_b)  # True: no copy was made
```

This example is limited by the fact that [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") allocates its
own memory: you cannot create a `bytearray` instance that is backed
by another object’s memory. However, third-party datatypes such as NumPy
arrays do not have this limitation, and allow use of zero-copy pickling
(or making as few copies as possible) when transferring between distinct
processes or systems.

See also

[**PEP 574**](https://peps.python.org/pep-0574/) – Pickle protocol 5 with out-of-band data