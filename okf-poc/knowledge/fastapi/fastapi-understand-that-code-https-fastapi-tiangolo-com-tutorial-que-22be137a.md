---
id: fastapi-understand-that-code-https-fastapi-tiangolo-com-tutorial-que-22be137a
type: concept
title: Understand that Code[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#understand-that-code
  "Permanent link")
description: The important point is just using **`AfterValidator` with a function
  inside `Annotated`**. Feel free to skip this part. 🤸
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### Understand that Code[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#understand-that-code "Permanent link")

The important point is just using **`AfterValidator` with a function inside `Annotated`**. Feel free to skip this part. 🤸

---

But if you're curious about this specific code example and you're still entertained, here are some extra details.

#### String with `value.startswith()`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#string-with-value-startswith "Permanent link")

Did you notice? A string using `value.startswith()` can take a tuple, and it will check each value in the tuple:

Python 3.10+

```
# Code above omitted 👆

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

# Code below omitted 👇
```

👀 Full file preview

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

#### A Random Item[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#a-random-item "Permanent link")

With `data.items()` we get an iterable object with tuples containing the key and value for each dictionary item.

We convert this iterable object into a proper `list` with `list(data.items())`.

Then with `random.choice()` we can get a **random value** from the list, so, we get a tuple with `(id, name)`. It will be something like `("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy")`.

Then we **assign those two values** of the tuple to the variables `id` and `name`.

So, if the user didn't provide an item ID, they will still receive a random suggestion.

...we do all this in a **single simple line**. 🤯 Don't you love Python? 🐍

Python 3.10+

```
# Code above omitted 👆

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

👀 Full file preview

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```