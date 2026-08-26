---
id: python-constants-https-docs-python-org-3-library-decimal-html-const-2d6abe7b
type: concept
title: Constants[¶](https://docs.python.org/3/library/decimal.html#constants "Link
  to this heading")
description: The constants in this section are only relevant for the C module. They
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants[¶](https://docs.python.org/3/library/decimal.html#constants "Link to this heading")

The constants in this section are only relevant for the C module. They
are also included in the pure Python version for compatibility.

|  | 32-bit | 64-bit |
| --- | --- | --- |
| decimal.MAX\_PREC[¶](https://docs.python.org/3/library/decimal.html#decimal.MAX_PREC "Link to this definition") | `425000000` | `999999999999999999` |
| decimal.MAX\_EMAX[¶](https://docs.python.org/3/library/decimal.html#decimal.MAX_EMAX "Link to this definition") | `425000000` | `999999999999999999` |
| decimal.MIN\_EMIN[¶](https://docs.python.org/3/library/decimal.html#decimal.MIN_EMIN "Link to this definition") | `-425000000` | `-999999999999999999` |
| decimal.MIN\_ETINY[¶](https://docs.python.org/3/library/decimal.html#decimal.MIN_ETINY "Link to this definition") | `-849999999` | `-1999999999999999997` |
| decimal.IEEE\_CONTEXT\_MAX\_BITS[¶](https://docs.python.org/3/library/decimal.html#decimal.IEEE_CONTEXT_MAX_BITS "Link to this definition") | `256` | `512` |

decimal.HAVE\_THREADS[¶](https://docs.python.org/3/library/decimal.html#decimal.HAVE_THREADS "Link to this definition")
:   The value is `True`. Deprecated, because Python now always has threads.

    Deprecated since version 3.9.

decimal.HAVE\_CONTEXTVAR[¶](https://docs.python.org/3/library/decimal.html#decimal.HAVE_CONTEXTVAR "Link to this definition")
:   The default value is `True`. If Python is [`configured using
    the --without-decimal-contextvar option`](https://docs.python.org/3/using/configure.html#cmdoption-without-decimal-contextvar),
    the C version uses a thread-local rather than a coroutine-local context and the value
    is `False`. This is slightly faster in some nested context scenarios.

    Added in version 3.8.3.