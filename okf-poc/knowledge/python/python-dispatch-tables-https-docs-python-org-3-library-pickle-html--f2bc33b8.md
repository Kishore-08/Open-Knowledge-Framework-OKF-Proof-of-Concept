---
id: python-dispatch-tables-https-docs-python-org-3-library-pickle-html--f2bc33b8
type: concept
title: Dispatch Tables[¶](https://docs.python.org/3/library/pickle.html#dispatch-tables
  "Link to this heading")
description: If one wants to customize pickling of some classes without disturbing
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Dispatch Tables[¶](https://docs.python.org/3/library/pickle.html#dispatch-tables "Link to this heading")

If one wants to customize pickling of some classes without disturbing
any other code which depends on pickling, then one can create a
pickler with a private dispatch table.

The global dispatch table managed by the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module is
available as `copyreg.dispatch_table`. Therefore, one may
choose to use a modified copy of `copyreg.dispatch_table` as a
private dispatch table.

For example

```
f = io.BytesIO()
p = pickle.Pickler(f)
p.dispatch_table = copyreg.dispatch_table.copy()
p.dispatch_table[SomeClass] = reduce_SomeClass
```

creates an instance of [`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") with a private dispatch
table which handles the `SomeClass` class specially. Alternatively,
the code

```
class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[SomeClass] = reduce_SomeClass
f = io.BytesIO()
p = MyPickler(f)
```

does the same but all instances of `MyPickler` will by default
share the private dispatch table. On the other hand, the code

```
copyreg.pickle(SomeClass, reduce_SomeClass)
f = io.BytesIO()
p = pickle.Pickler(f)
```

modifies the global dispatch table shared by all users of the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module.