---
id: fastapi-testing-file-https-fastapi-tiangolo-com-tutorial-testing-tes-459f3498
type: concept
title: Testing file[¶](https://fastapi.tiangolo.com/tutorial/testing/#testing-file
  "Permanent link")
description: 'Then you could have a file `test_main.py` with your tests. It could
  live on the same Python package (the same directory with a `__init__.py` file):'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/testing/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Testing file[¶](https://fastapi.tiangolo.com/tutorial/testing/#testing-file "Permanent link")

Then you could have a file `test_main.py` with your tests. It could live on the same Python package (the same directory with a `__init__.py` file):

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

Because this file is in the same package, you can use relative imports to import the object `app` from the `main` module (`main.py`):

Python 3.10+

```
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

...and have the code for the tests just like before.