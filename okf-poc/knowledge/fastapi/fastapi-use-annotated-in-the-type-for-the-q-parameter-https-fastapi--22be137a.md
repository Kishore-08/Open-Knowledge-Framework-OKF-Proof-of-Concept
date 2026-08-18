---
id: fastapi-use-annotated-in-the-type-for-the-q-parameter-https-fastapi--22be137a
type: concept
title: Use `Annotated` in the type for the `q` parameter[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#use-annotated-in-the-type-for-the-q-parameter
  "Permanent link")
description: Remember I told you before that `Annotated` can be used to add metadata
  to your parameters in the [Python Types Intro](https://fastapi.tiangolo.com/python-types/#type-hints-with-metadata-annotations)?
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Use `Annotated` in the type for the `q` parameter[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#use-annotated-in-the-type-for-the-q-parameter "Permanent link")

Remember I told you before that `Annotated` can be used to add metadata to your parameters in the [Python Types Intro](https://fastapi.tiangolo.com/python-types/#type-hints-with-metadata-annotations)?

Now it's the time to use it with FastAPI. 🚀

We had this type annotation:

```
q: str | None = None
```

What we will do is wrap that with `Annotated`, so it becomes:

```
q: Annotated[str | None] = None
```

Both of those versions mean the same thing, `q` is a parameter that can be a `str` or `None`, and by default, it is `None`.

Now let's jump to the fun stuff. 🎉