---
id: python-thread-safety-for-memoryview-objects-https-docs-python-org-3-185db8ec
type: concept
title: Thread safety for memoryview objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-memoryview-objects
  "Link to this heading")
description: '[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview
  "memoryview") objects provide access to the internal data of an'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Thread safety for memoryview objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-memoryview-objects "Link to this heading")

[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") objects provide access to the internal data of an
underlying object without copying. Thread safety depends on both the
memoryview itself and the underlying buffer exporter.

The memoryview implementation uses atomic operations to track its own
exports in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build). Creating and
releasing a memoryview are thread-safe. Attribute access (e.g.,
[`shape`](https://docs.python.org/3/library/stdtypes.html#memoryview.shape "memoryview.shape"), [`format`](https://docs.python.org/3/library/stdtypes.html#memoryview.format "memoryview.format")) reads fields that
are immutable for the lifetime of the memoryview, so concurrent reads
are safe as long as the memoryview has not been released.

However, the actual data accessed through the memoryview is owned by the
underlying object. Concurrent access to this data is only safe if the
underlying object supports it:

- For immutable objects like [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), concurrent reads through
  multiple memoryviews are safe.
- For mutable objects like [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"), reading and writing the
  same memory region from multiple threads without external
  synchronization is not safe and may result in data corruption.
  Note that even read-only memoryviews of mutable objects do not
  prevent data races if the underlying object is modified from
  another thread.

```
# NOT safe: concurrent writes to the same buffer
data = bytearray(1000)
view = memoryview(data)
# Thread 1: view[0:500] = b'x' * 500
# Thread 2: view[0:500] = b'y' * 500
```

```
# Safe: use a lock for concurrent access
import threading
lock = threading.Lock()
data = bytearray(1000)
view = memoryview(data)

with lock:
    view[0:500] = b'x' * 500
```

Resizing or reallocating the underlying object (such as calling
[`bytearray.resize()`](https://docs.python.org/3/library/stdtypes.html#bytearray.resize "bytearray.resize")) while a memoryview is exported raises
[`BufferError`](https://docs.python.org/3/library/exceptions.html#BufferError "BufferError"). This is enforced regardless of threading.