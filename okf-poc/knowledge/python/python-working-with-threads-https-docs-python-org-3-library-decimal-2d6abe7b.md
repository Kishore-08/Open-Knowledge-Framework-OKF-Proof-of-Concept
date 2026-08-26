---
id: python-working-with-threads-https-docs-python-org-3-library-decimal-2d6abe7b
type: concept
title: Working with threads[¶](https://docs.python.org/3/library/decimal.html#working-with-threads
  "Link to this heading")
description: The [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext
  "decimal.getcontext") function accesses a different [`Context`](https://docs.python.org/3/library/decimal.html#de
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Working with threads[¶](https://docs.python.org/3/library/decimal.html#working-with-threads "Link to this heading")

The [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") function accesses a different [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") object for
each thread. Having separate thread contexts means that threads may make
changes (such as `getcontext().prec=10`) without interfering with other threads.

Likewise, the [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") function automatically assigns its target to
the current thread.

If [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") has not been called before [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext"), then
`getcontext()` will automatically create a new context for use in the
current thread. New context objects have default values set from the
[`decimal.DefaultContext`](https://docs.python.org/3/library/decimal.html#decimal.DefaultContext "decimal.DefaultContext") object.

The [`sys.flags.thread_inherit_context`](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "sys.flags.thread_inherit_context") flag affects the context for
new threads. If the flag is false, new threads will start with an empty
context. In this case, [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") will create a new context object
when called and use the default values from *DefaultContext*. If the flag
is true, new threads will start with a copy of context from the caller of
[`threading.Thread.start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start").

To control the defaults so that each thread will use the same values throughout
the application, directly modify the *DefaultContext* object. This should be
done *before* any threads are started so that there won’t be a race condition
between threads calling [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext"). For example:

```
# Set applicationwide defaults for all threads about to be launched
DefaultContext.prec = 12
DefaultContext.rounding = ROUND_DOWN
DefaultContext.traps = ExtendedContext.traps.copy()
DefaultContext.traps[InvalidOperation] = 1
setcontext(DefaultContext)

# Afterwards, the threads can be started
t1.start()
t2.start()
t3.start()
 . . .
```