---
id: python-calling-variadic-functions-https-docs-python-org-3-library-c-07786b1c
type: concept
title: Calling variadic functions[¶](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions
  "Link to this heading")
description: On a lot of platforms calling variadic functions through ctypes is exactly
  the same
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Calling variadic functions[¶](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions "Link to this heading")

On a lot of platforms calling variadic functions through ctypes is exactly the same
as calling functions with a fixed number of parameters. On some platforms, and in
particular ARM64 for Apple Platforms, the calling convention for variadic functions
is different than that for regular functions.

On those platforms it is required to specify the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
attribute for the regular, non-variadic, function arguments:

```
libc.printf.argtypes = [ctypes.c_char_p]
```

Because specifying the attribute does not inhibit portability it is advised to always
specify [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") for all variadic functions.