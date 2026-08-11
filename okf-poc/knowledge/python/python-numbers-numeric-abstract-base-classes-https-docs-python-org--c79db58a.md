---
id: python-numbers-numeric-abstract-base-classes-https-docs-python-org--c79db58a
type: concept
title: '`numbers` — Numeric abstract base classes[¶](https://docs.python.org/3/library/n'
description: '**Source code:** [Lib/numbers.py](https://github.com/python/cpython/tree/3.14/Lib/numbers.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/numbers.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `numbers` — Numeric abstract base classes[¶](https://docs.python.org/3/library/numbers.html#module-numbers "Link to this heading")

**Source code:** [Lib/numbers.py](https://github.com/python/cpython/tree/3.14/Lib/numbers.py)

---

The `numbers` module ([**PEP 3141**](https://peps.python.org/pep-3141/)) defines a hierarchy of numeric
[abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) which progressively define
more operations. None of the types defined in this module are intended to be instantiated.

*class* numbers.Number[¶](https://docs.python.org/3/library/numbers.html#numbers.Number "Link to this definition")
:   The root of the numeric hierarchy. If you just want to check if an argument
    *x* is a number, without caring what kind, use `isinstance(x, Number)`.