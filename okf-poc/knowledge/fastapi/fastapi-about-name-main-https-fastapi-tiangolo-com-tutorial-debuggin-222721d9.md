---
id: fastapi-about-name-main-https-fastapi-tiangolo-com-tutorial-debuggin-222721d9
type: concept
title: About `__name__ == "__main__"`[¶](https://fastapi.tiangolo.com/tutorial/debugging/#about-name-main
  "Permanent link")
description: 'The main purpose of the `__name__ == "__main__"` is to have some code
  that is executed when your file is called with:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/debugging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### About `__name__ == "__main__"`[¶](https://fastapi.tiangolo.com/tutorial/debugging/#about-name-main "Permanent link")

The main purpose of the `__name__ == "__main__"` is to have some code that is executed when your file is called with:

```
$ uv run python myapp.py
```

but is not called when another file imports it, like in:

```
from myapp import app
```

#### More details[¶](https://fastapi.tiangolo.com/tutorial/debugging/#more-details "Permanent link")

Let's say your file is named `myapp.py`.

If you run it with:

```
$ uv run python myapp.py
```

then the internal variable `__name__` in your file, created automatically by Python, will have as value the string `"__main__"`.

So, the section:

```
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

will run.

---

This won't happen if you import that module (file).

So, if you have another file `importer.py` with:

```
from myapp import app

# Some more code
```

in that case, the automatically created variable `__name__` inside of `myapp.py` will not have the value `"__main__"`.

So, the line:

```
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

will not be executed.

Note

For more information, check [the official Python docs](https://docs.python.org/3/library/__main__.html).