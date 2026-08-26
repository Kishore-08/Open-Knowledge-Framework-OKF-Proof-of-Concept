---
id: python-thread-safety-without-the-gil-https-docs-python-org-3-librar-07786b1c
type: concept
title: Thread safety without the GIL[¶](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil
  "Link to this heading")
description: From Python 3.13 onward, the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
  can be disabled on the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build).
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Thread safety without the GIL[¶](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil "Link to this heading")

From Python 3.13 onward, the [GIL](https://docs.python.org/3/glossary.html#term-GIL) can be disabled on the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build).
In ctypes, reads and writes to a single object concurrently is safe, but not across multiple objects:

> ```
> >>> number = c_int(42)
> >>> pointer_a = pointer(number)
> >>> pointer_b = pointer(number)
> ```

In the above, it’s only safe for one object to read and write to the address at once if the GIL is disabled.
So, `pointer_a` can be shared and written to across multiple threads, but only if `pointer_b`
is not also attempting to do the same. If this is an issue, consider using a [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock")
to synchronize access to memory:

> ```
> >>> import threading
> >>> lock = threading.Lock()
> >>> # Thread 1
> >>> with lock:
> ...    pointer_a.contents = 24
> >>> # Thread 2
> >>> with lock:
> ...    pointer_b.contents = 42
> ```