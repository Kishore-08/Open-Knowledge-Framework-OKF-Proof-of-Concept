---
id: fastapi-check-the-docs-https-fastapi-tiangolo-com-tutorial-cookie-pa-b8bfc7ce
type: concept
title: Check the Docs[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#check-the-docs
  "Permanent link")
description: 'You can see the defined cookies in the docs UI at `/docs`:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cookie-param-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Check the Docs[¶](https://fastapi.tiangolo.com/tutorial/cookie-param-models/#check-the-docs "Permanent link")

You can see the defined cookies in the docs UI at `/docs`:

Note

Have in mind that, as **browsers handle cookies** in special ways and behind the scenes, they **don't** easily allow **JavaScript** to touch them.

If you go to the **API docs UI** at `/docs` you will be able to see the **documentation** for cookies for your *path operations*.

But even if you **fill the data** and click "Execute", because the docs UI works with **JavaScript**, the cookies won't be sent, and you will see an **error** message as if you didn't write any values.