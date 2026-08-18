---
id: fastapi-run-it-https-fastapi-tiangolo-com-tutorial-testing-run-it-pe-459f3498
type: concept
title: Run it[¶](https://fastapi.tiangolo.com/tutorial/testing/#run-it "Permanent
  link")
description: After that, you just need to install `pytest`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/testing/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Run it[¶](https://fastapi.tiangolo.com/tutorial/testing/#run-it "Permanent link")

After that, you just need to install `pytest`.

Add it to your project:

```
$ uv add pytest

---> 100%
```

It will detect the files and tests automatically, execute them, and report the results back to you.

Run the tests with:

```
$ uv run pytest

================ test session starts ================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/user/code/superawesome-cli/app
plugins: forked-1.1.3, xdist-1.31.0, cov-2.8.1
collected 6 items

---> 100%

test_main.py <span style="color: green; white-space: pre;">......                            [100%]</span>

<span style="color: green;">================= 1 passed in 0.03s =================</span>
```