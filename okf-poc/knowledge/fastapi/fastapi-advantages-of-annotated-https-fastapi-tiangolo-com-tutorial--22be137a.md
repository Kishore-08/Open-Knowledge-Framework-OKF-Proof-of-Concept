---
id: fastapi-advantages-of-annotated-https-fastapi-tiangolo-com-tutorial--22be137a
type: concept
title: Advantages of `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#advantages-of-annotated
  "Permanent link")
description: '**Using `Annotated` is recommended** instead of the default value in
  function parameters, it is **better** for multiple reasons. 🤓'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Advantages of `Annotated`[¶](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#advantages-of-annotated "Permanent link")

**Using `Annotated` is recommended** instead of the default value in function parameters, it is **better** for multiple reasons. 🤓

The **default** value of the **function parameter** is the **actual default** value, that's more intuitive with Python in general. 😌

You could **call** that same function in **other places** without FastAPI, and it would **work as expected**. If there's a **required** parameter (without a default value), your **editor** will let you know with an error, **Python** will also complain if you run it without passing the required parameter.

When you don't use `Annotated` and instead use the **(old) default value style**, if you call that function without FastAPI in **other places**, you have to **remember** to pass the arguments to the function for it to work correctly, otherwise the values will be different from what you expect (e.g. `QueryInfo` or something similar instead of `str`). And your editor won't complain, and Python won't complain running that function, only when the operations inside error out.

Because `Annotated` can have more than one metadata annotation, you could now even use the same function with other tools, like [Typer](https://typer.tiangolo.com/). 🚀