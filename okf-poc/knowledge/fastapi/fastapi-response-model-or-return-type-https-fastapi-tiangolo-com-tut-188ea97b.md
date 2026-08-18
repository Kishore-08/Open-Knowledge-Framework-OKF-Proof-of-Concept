---
id: fastapi-response-model-or-return-type-https-fastapi-tiangolo-com-tut-188ea97b
type: concept
title: '`response_model` or Return Type[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-or-return-type
  "Permanent link")'
description: In this case, because the two models are different, if we annotated the
  function return type as `UserOut`, the editor and tools would complain that we are
  returning an invalid type, as those are diffe
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/response-model/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `response_model` or Return Type[¶](https://fastapi.tiangolo.com/tutorial/response-model/#response-model-or-return-type "Permanent link")

In this case, because the two models are different, if we annotated the function return type as `UserOut`, the editor and tools would complain that we are returning an invalid type, as those are different classes.

That's why in this example we have to declare it in the `response_model` parameter.

...but continue reading below to see how to overcome that.