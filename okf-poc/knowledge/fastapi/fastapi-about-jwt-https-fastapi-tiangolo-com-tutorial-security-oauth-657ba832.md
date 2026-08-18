---
id: fastapi-about-jwt-https-fastapi-tiangolo-com-tutorial-security-oauth-657ba832
type: concept
title: About JWT[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt
  "Permanent link")
description: JWT means "JSON Web Tokens".
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## About JWT[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt "Permanent link")

JWT means "JSON Web Tokens".

It's a standard to codify a JSON object in a long dense string without spaces. It looks like this:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

It is not encrypted, so, anyone could recover the information from the contents.

But it's signed. So, when you receive a token that you issued, you can verify that it was you who issued it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.

If you want to play with JWT tokens and see how they work, check [https://jwt.io](https://jwt.io/).