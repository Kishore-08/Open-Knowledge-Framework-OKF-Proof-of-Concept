---
id: python-additional-utility-classes-and-functions-https-docs-python-o-3209cdc1
type: concept
title: Additional Utility Classes and Functions[¶](https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions
  "Link to this heading")
description: '*class* types.SimpleNamespace[¶](https://docs.python.org/3/library/types.html#types.SimpleNamespace
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/types.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Additional Utility Classes and Functions[¶](https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions "Link to this heading")

*class* types.SimpleNamespace[¶](https://docs.python.org/3/library/types.html#types.SimpleNamespace "Link to this definition")
:   A simple [`object`](https://docs.python.org/3/library/functions.html#object "object") subclass that provides attribute access to its
    namespace, as well as a meaningful repr.

    Unlike [`object`](https://docs.python.org/3/library/functions.html#object "object"), with `SimpleNamespace` you can add and remove
    attributes.

    `SimpleNamespace` objects may be initialized
    in the same way as [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"): either with keyword arguments,
    with a single positional argument, or with both.
    When initialized with keyword arguments,
    those are directly added to the underlying namespace.
    Alternatively, when initialized with a positional argument,
    the underlying namespace will be updated with key-value pairs
    from that argument (either a mapping object or
    an [iterable](https://docs.python.org/3/glossary.html#term-iterable) object producing key-value pairs).
    All such keys must be strings.

    The type is roughly equivalent to the following code:

    ```
    class SimpleNamespace:
        def __init__(self, mapping_or_iterable=(), /, **kwargs):
            self.__dict__.update(mapping_or_iterable)
            self.__dict__.update(kwargs)

        def __repr__(self):
            items = (f"{k}={v!r}" for k, v in self.__dict__.items())
            return "{}({})".format(type(self).__name__, ", ".join(items))

        def __eq__(self, other):
            if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
               return self.__dict__ == other.__dict__
            return NotImplemented
    ```

    `SimpleNamespace` may be useful as a replacement for `class NS: pass`.
    However, for a structured record type use [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
    instead.

    `SimpleNamespace` objects are supported by [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace").

    Added in version 3.3.

    Changed in version 3.9: Attribute order in the repr changed from alphabetical to insertion (like
    `dict`).

    Changed in version 3.13: Added support for an optional positional argument.

types.DynamicClassAttribute(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)[¶](https://docs.python.org/3/library/types.html#types.DynamicClassAttribute "Link to this definition")
:   Route attribute access on a class to \_\_getattr\_\_.

    This is a descriptor, used to define attributes that act differently when
    accessed through an instance and through a class. Instance access remains
    normal, but access to an attribute through a class will be routed to the
    class’s \_\_getattr\_\_ method; this is done by raising AttributeError.

    This allows one to have properties active on an instance, and have virtual
    attributes on the class with the same name (see [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") for an example).

    Added in version 3.4.