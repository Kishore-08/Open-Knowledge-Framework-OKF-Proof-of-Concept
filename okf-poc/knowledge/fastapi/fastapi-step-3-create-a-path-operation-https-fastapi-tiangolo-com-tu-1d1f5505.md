---
id: fastapi-step-3-create-a-path-operation-https-fastapi-tiangolo-com-tu-1d1f5505
type: concept
title: 'Step 3: create a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation
  "Permanent link")'
description: '"Path" here refers to the last part of the URL starting from the first
  `/`.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Step 3: create a *path operation*[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation "Permanent link")

#### Path[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#path "Permanent link")

"Path" here refers to the last part of the URL starting from the first `/`.

So, in a URL like:

```
https://example.com/items/foo
```

...the path would be:

```
/items/foo
```

Note

A "path" is also commonly called an "endpoint" or a "route".

While building an API, the "path" is the main way to separate "concerns" and "resources".

#### Operation[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#operation "Permanent link")

"Operation" here refers to one of the HTTP "methods".

One of:

- `POST`
- `GET`
- `PUT`
- `DELETE`

...and the more exotic ones:

- `OPTIONS`
- `HEAD`
- `PATCH`
- `TRACE`

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

---

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

- `POST`: to create data.
- `GET`: to read data.
- `PUT`: to update data.
- `DELETE`: to delete data.

So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "**operations**" too.

#### Define a *path operation decorator*[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

The `@app.get("/")` tells **FastAPI** that the function right below is in charge of handling requests that go to:

- the path `/`
- using a `get` operation

`@decorator` Info

That `@something` syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells **FastAPI** that the function below corresponds to the **path** `/` with an **operation** `get`.

It is the "**path operation decorator**".

You can also use the other operations:

- `@app.post()`
- `@app.put()`
- `@app.delete()`

And the more exotic ones:

- `@app.options()`
- `@app.head()`
- `@app.patch()`
- `@app.trace()`

Tip

You are free to use each operation (HTTP method) as you wish.

**FastAPI** doesn't enforce any specific meaning.

The information here is presented as a guideline, not a requirement.

For example, when using GraphQL you normally perform all the actions using only `POST` operations.