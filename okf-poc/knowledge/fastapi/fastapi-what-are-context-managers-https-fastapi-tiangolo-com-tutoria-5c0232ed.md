---
id: fastapi-what-are-context-managers-https-fastapi-tiangolo-com-tutoria-5c0232ed
type: concept
title: What are "Context Managers"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#what-are-context-managers
  "Permanent link")
description: '"Context Managers" are any of those Python objects that you can use
  in a `with` statement.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### What are "Context Managers"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#what-are-context-managers "Permanent link")

"Context Managers" are any of those Python objects that you can use in a `with` statement.

For example, [you can use `with` to read a file](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files):

```
with open("./somefile.txt") as f:
    contents = f.read()
    print(contents)
```

Underneath, the `open("./somefile.txt")` creates an object that is called a "Context Manager".

When the `with` block finishes, it makes sure to close the file, even if there were exceptions.

When you create a dependency with `yield`, **FastAPI** will internally create a context manager for it, and combine it with some other related tools.