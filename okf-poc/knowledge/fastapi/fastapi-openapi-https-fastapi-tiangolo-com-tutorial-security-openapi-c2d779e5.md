---
id: fastapi-openapi-https-fastapi-tiangolo-com-tutorial-security-openapi-c2d779e5
type: concept
title: OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/security/#openapi "Permanent
  link")
description: OpenAPI (previously known as Swagger) is the open specification for building
  APIs (now part of the Linux Foundation).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/security/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/security/#openapi "Permanent link")

OpenAPI (previously known as Swagger) is the open specification for building APIs (now part of the Linux Foundation).

**FastAPI** is based on **OpenAPI**.

That's what makes it possible to have multiple automatic interactive documentation interfaces, code generation, etc.

OpenAPI has a way to define multiple security "schemes".

By using them, you can take advantage of all these standard-based tools, including these interactive documentation systems.

OpenAPI defines the following security schemes:

- `apiKey`: an application specific key that can come from:
  - A query parameter.
  - A header.
  - A cookie.
- `http`: standard HTTP authentication systems, including:
  - `bearer`: a header `Authorization` with a value of `Bearer` plus a token. This is inherited from OAuth2.
  - HTTP Basic authentication.
  - HTTP Digest, etc.
- `oauth2`: all the OAuth2 ways to handle security (called "flows").
  - Several of these flows are appropriate for building an OAuth 2.0 authentication provider (like Google, Facebook, X (Twitter), GitHub, etc):
    - `implicit`
    - `clientCredentials`
    - `authorizationCode`
  - But there is one specific "flow" that can be perfectly used for handling authentication in the same application directly:
    - `password`: some next chapters will cover examples of this.
- `openIdConnect`: has a way to define how to discover OAuth2 authentication data automatically.
  - This automatic discovery is what is defined in the OpenID Connect specification.

Tip

Integrating other authentication/authorization providers like Google, Facebook, X (Twitter), GitHub, etc. is also possible and relatively easy.

The most complex problem is building an authentication/authorization provider like those, but **FastAPI** gives you the tools to do it easily, while doing the heavy lifting for you.