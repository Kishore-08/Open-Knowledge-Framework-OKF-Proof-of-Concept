---
id: python-mapping-operators-to-functions-https-docs-python-org-3-libra-b7b569fc
type: concept
title: Mapping Operators to Functions[¶](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
  "Link to this heading")
description: This table shows how abstract operations correspond to operator symbols
  in the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/operator.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Mapping Operators to Functions[¶](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions "Link to this heading")

This table shows how abstract operations correspond to operator symbols in the
Python syntax and the functions in the `operator` module.

| Operation | Syntax | Function |
| --- | --- | --- |
| Addition | `a + b` | `add(a, b)` |
| Concatenation | `seq1 + seq2` | `concat(seq1, seq2)` |
| Containment Test | `obj in seq` | `contains(seq, obj)` |
| Division | `a / b` | `truediv(a, b)` |
| Division | `a // b` | `floordiv(a, b)` |
| Bitwise And, or Intersection | `a & b` | `and_(a, b)` |
| Bitwise Exclusive Or, or Symmetric Difference | `a ^ b` | `xor(a, b)` |
| Bitwise Inversion, or Complement | `~ a` | `invert(a)` |
| Bitwise Or, or Union | `a | b` | `or_(a, b)` |
| Exponentiation | `a ** b` | `pow(a, b)` |
| Identity | `a is b` | `is_(a, b)` |
| Identity | `a is not b` | `is_not(a, b)` |
| Identity | `a is None` | `is_none(a)` |
| Identity | `a is not None` | `is_not_none(a)` |
| Indexed Assignment | `obj[k] = v` | `setitem(obj, k, v)` |
| Indexed Deletion | `del obj[k]` | `delitem(obj, k)` |
| Indexing | `obj[k]` | `getitem(obj, k)` |
| Left Shift | `a << b` | `lshift(a, b)` |
| Modulo | `a % b` | `mod(a, b)` |
| Multiplication | `a * b` | `mul(a, b)` |
| Matrix Multiplication | `a @ b` | `matmul(a, b)` |
| Negation (Arithmetic) | `- a` | `neg(a)` |
| Negation (Logical) | `not a` | `not_(a)` |
| Positive | `+ a` | `pos(a)` |
| Right Shift | `a >> b` | `rshift(a, b)` |
| Slice Assignment | `seq[i:j] = values` | `setitem(seq, slice(i, j), values)` |
| Slice Deletion | `del seq[i:j]` | `delitem(seq, slice(i, j))` |
| Slicing | `seq[i:j]` | `getitem(seq, slice(i, j))` |
| String Formatting | `s % obj` | `mod(s, obj)` |
| Subtraction | `a - b` | `sub(a, b)` |
| Truth Test | `obj` | `truth(obj)` |
| Ordering | `a < b` | `lt(a, b)` |
| Ordering | `a <= b` | `le(a, b)` |
| Equality | `a == b` | `eq(a, b)` |
| Difference | `a != b` | `ne(a, b)` |
| Ordering | `a >= b` | `ge(a, b)` |
| Ordering | `a > b` | `gt(a, b)` |