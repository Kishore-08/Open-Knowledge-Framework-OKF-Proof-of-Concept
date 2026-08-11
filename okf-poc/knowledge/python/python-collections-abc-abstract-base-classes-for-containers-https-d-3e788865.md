---
id: python-collections-abc-abstract-base-classes-for-containers-https-d-3e788865
type: concept
title: '`collections.abc` — Abstract Base Classes for Containers[¶](https://docs.python.'
description: 'Added in version 3.3: Formerly, this module was part of the [`collections`](https://docs.python.org/3/library/collections.html#module-collections
  "collections: Container datatypes") module.'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.abc.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `collections.abc` — Abstract Base Classes for Containers[¶](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "Link to this heading")

Added in version 3.3: Formerly, this module was part of the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.

**Source code:** [Lib/\_collections\_abc.py](https://github.com/python/cpython/tree/3.14/Lib/_collections_abc.py)

---

This module provides [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) that
can be used to test whether a class provides a particular interface; for
example, whether it is [hashable](https://docs.python.org/3/glossary.html#term-hashable) or whether it is a [mapping](https://docs.python.org/3/glossary.html#term-mapping).

An [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") or [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") test for an interface works in one
of three ways.

1. A newly written class can inherit directly from one of the
   abstract base classes. The class must supply the required abstract
   methods. The remaining mixin methods come from inheritance and can be
   overridden if desired. Other methods may be added as needed:

   ```
   class C(Sequence):                      # Direct inheritance
       def __init__(self): ...             # Extra method not required by the ABC
       def __getitem__(self, index):  ...  # Required abstract method
       def __len__(self):  ...             # Required abstract method
       def count(self, value): ...         # Optionally override a mixin method
   ```

   ```
   >>> issubclass(C, Sequence)
   True
   >>> isinstance(C(), Sequence)
   True
   ```
2. Existing classes and built-in classes can be registered as “virtual
   subclasses” of the ABCs. Those classes should define the full API
   including all of the abstract methods and all of the mixin methods.
   This lets users rely on [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") or [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") tests
   to determine whether the full interface is supported. The exception to
   this rule is for methods that are automatically inferred from the rest
   of the API:

   ```
   class D:                                 # No inheritance
       def __init__(self): ...              # Extra method not required by the ABC
       def __getitem__(self, index):  ...   # Abstract method
       def __len__(self):  ...              # Abstract method
       def count(self, value): ...          # Mixin method
       def index(self, value): ...          # Mixin method

   Sequence.register(D)                     # Register instead of inherit
   ```

   ```
   >>> issubclass(D, Sequence)
   True
   >>> isinstance(D(), Sequence)
   True
   ```

   In this example, class `D` does not need to define
   `__contains__`, `__iter__`, and `__reversed__` because the
   [in-operator](https://docs.python.org/3/reference/expressions.html#comparisons), the [iteration](https://docs.python.org/3/glossary.html#term-iterable)
   logic, and the [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "reversed") function automatically fall back to
   using `__getitem__` and `__len__`.
3. Some simple interfaces are directly recognizable by the presence of
   the required methods (unless those methods have been set to [`None`](https://docs.python.org/3/library/constants.html#None "None")):

   ```
   class E:
       def __iter__(self): ...
       def __next__(self): ...
   ```

   ```
   >>> issubclass(E, Iterable)
   True
   >>> isinstance(E(), Iterable)
   True
   ```

   Complex interfaces do not support this last technique because an
   interface is more than just the presence of method names. Interfaces
   specify semantics and relation