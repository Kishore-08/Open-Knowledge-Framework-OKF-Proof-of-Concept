---
id: fastapi-using-testclient-https-fastapi-tiangolo-com-tutorial-testing-459f3498
type: concept
title: Using `TestClient`[¶](https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
  "Permanent link")
description: Note
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/testing/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Using `TestClient`[¶](https://fastapi.tiangolo.com/tutorial/testing/#using-testclient "Permanent link")

Note

To use `TestClient`, first install [`httpx`](https://www.python-httpx.org).

Add it to your project:

```
$ uv add httpx
```

Import `TestClient`.

Create a `TestClient` by passing your **FastAPI** application to it.

Create functions with a name that starts with `test_` (this is a standard `pytest` convention).

Use the `TestClient` object the same way as you do with `httpx`.

Write simple `assert` statements with the standard Python expressions that you need to check (again, standard `pytest`).

Python 3.10+

```
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

Tip

Notice that the testing functions are normal `def`, not `async def`.

And the calls to the client are also normal calls, not using `await`.

This allows you to use `pytest` directly without complications.

Technical Details

You could also use `from starlette.testclient import TestClient`.

**FastAPI** provides the same `starlette.testclient` as `fastapi.testclient` just as a convenience for you, the developer. But it comes directly from Starlette.

Tip

If you want to call `async` functions in your tests apart from sending requests to your FastAPI application (e.g. asynchronous database functions), have a look at the [Async Tests](https://fastapi.tiangolo.com/advanced/async-tests/) in the advanced tutorial.