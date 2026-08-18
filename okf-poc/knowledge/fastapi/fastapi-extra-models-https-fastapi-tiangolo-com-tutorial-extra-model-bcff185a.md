---
id: fastapi-extra-models-https-fastapi-tiangolo-com-tutorial-extra-model-bcff185a
type: concept
title: Extra Models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#extra-models
description: Continuing with the previous example, it will be common to have more
  than one related model.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-models/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Extra Models[¶](https://fastapi.tiangolo.com/tutorial/extra-models/#extra-models "Permanent link")

Continuing with the previous example, it will be common to have more than one related model.

This is especially the case for user models, because:

- The **input model** needs to be able to have a password.
- The **output model** should not have a password.
- The **database model** would probably need to have a hashed password.

Danger

Never store user's plaintext passwords. Always store a "secure hash" that you can then verify.

If you don't know, you will learn what a "password hash" is in the [security chapters](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#password-hashing).