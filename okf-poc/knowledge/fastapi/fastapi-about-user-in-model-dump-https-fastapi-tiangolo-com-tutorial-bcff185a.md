---
id: fastapi-about-user-in-model-dump-https-fastapi-tiangolo-com-tutorial-bcff185a
type: concept
title: About `**user_in.model_dump()`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#about-user-in-model-dump
  "Permanent link")
description: '`user_in` is a Pydantic model of class `UserIn`.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### About `**user_in.model_dump()`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#about-user-in-model-dump "Permanent link")

#### Pydantic's `.model_dump()`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#pydantics-model-dump "Permanent link")

`user_in` is a Pydantic model of class `UserIn`.

Pydantic models have a `.model_dump()` method that returns a `dict` with the model's data.

So, if we create a Pydantic object `user_in` like:

```
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
```

and then we call:

```
user_dict = user_in.model_dump()
```

we now have a `dict` with the data in the variable `user_dict` (it's a `dict` instead of a Pydantic model object).

And if we call:

```
print(user_dict)
```

we would get a Python `dict` with:

```
{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}
```

#### Unpacking a `dict`[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#unpacking-a-dict "Permanent link")

If we take a `dict` like `user_dict` and pass it to a function (or class) with `**user_dict`, Python will "unpack" it. It will pass the keys and values of the `user_dict` directly as key-value arguments.

So, continuing with the `user_dict` from above, writing:

```
UserInDB(**user_dict)
```

would result in something equivalent to:

```
UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
```

Or more exactly, using `user_dict` directly, with whatever contents it might have in the future:

```
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
```

#### A Pydantic model from the contents of another[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#a-pydantic-model-from-the-contents-of-another "Permanent link")

As in the example above we got `user_dict` from `user_in.model_dump()`, this code:

```
user_dict = user_in.model_dump()
UserInDB(**user_dict)
```

would be equivalent to:

```
UserInDB(**user_in.model_dump())
```

...because `user_in.model_dump()` is a `dict`, and then we make Python "unpack" it by passing it to `UserInDB` prefixed with `**`.

So, we get a Pydantic model from the data in another Pydantic model.

#### Unpacking a `dict` and extra keywords[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#unpacking-a-dict-and-extra-keywords "Permanent link")

And then adding the extra keyword argument `hashed_password=hashed_password`, like in:

```
UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
```

...ends up being like:

```
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = hashed_password,
)
```

Warning

The supporting additional functions `fake_password_hasher` and `fake_save_user` are just to demo a possible flow of the data, but they of course are not providing any real security.