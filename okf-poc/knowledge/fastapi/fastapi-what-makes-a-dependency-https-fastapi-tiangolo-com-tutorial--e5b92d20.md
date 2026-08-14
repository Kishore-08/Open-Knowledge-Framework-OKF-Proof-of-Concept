---
id: fastapi-what-makes-a-dependency-https-fastapi-tiangolo-com-tutorial--e5b92d20
type: concept
title: What makes a dependency[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#what-makes-a-dependency
  "Permanent link")
description: Up to now you have seen dependencies declared as functions.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## What makes a dependency[¶](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#what-makes-a-dependency "Permanent link")

Up to now you have seen dependencies declared as functions.

But that's not the only way to declare dependencies (although it would probably be the more common).

The key factor is that a dependency should be a "callable".

A "**callable**" in Python is anything that Python can "call" like a function.

So, if you have an object `something` (that might *not* be a function) and you can "call" it (execute it) like:

```
something()
```

or

```
something(some_argument, some_keyword_argument="foo")
```

then it is a "callable".