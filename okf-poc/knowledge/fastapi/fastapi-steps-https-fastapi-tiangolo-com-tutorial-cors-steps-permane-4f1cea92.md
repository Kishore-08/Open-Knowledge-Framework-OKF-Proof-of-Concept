---
id: fastapi-steps-https-fastapi-tiangolo-com-tutorial-cors-steps-permane-4f1cea92
type: concept
title: Steps[¶](https://fastapi.tiangolo.com/tutorial/cors/#steps "Permanent link")
description: So, let's say you have a frontend running in your browser at `http://localhost:8080`,
  and its JavaScript is trying to communicate with a backend running at `http://localhost`
  (because we don't specify
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/cors/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Steps[¶](https://fastapi.tiangolo.com/tutorial/cors/#steps "Permanent link")

So, let's say you have a frontend running in your browser at `http://localhost:8080`, and its JavaScript is trying to communicate with a backend running at `http://localhost` (because we don't specify a port, the browser will assume the default port `80`).

Then, the browser will send an HTTP `OPTIONS` request to the `:80`-backend, and if the backend sends the appropriate headers authorizing the communication from this different origin (`http://localhost:8080`) then the `:8080`-browser will let the JavaScript in the frontend send its request to the `:80`-backend.

To achieve this, the `:80`-backend must have a list of "allowed origins".

In this case, the list would have to include `http://localhost:8080` for the `:8080`-frontend to work correctly.