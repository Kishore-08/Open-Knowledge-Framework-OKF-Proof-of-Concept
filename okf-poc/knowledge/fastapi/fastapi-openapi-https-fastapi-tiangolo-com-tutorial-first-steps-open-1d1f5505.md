---
id: fastapi-openapi-https-fastapi-tiangolo-com-tutorial-first-steps-open-1d1f5505
type: concept
title: OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi "Permanent
  link")
description: '**FastAPI** generates a "schema" with all your API using the **OpenAPI**
  standard for defining APIs.'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/first-steps/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

### OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi "Permanent link")

**FastAPI** generates a "schema" with all your API using the **OpenAPI** standard for defining APIs.

#### "Schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#schema "Permanent link")

A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

#### API "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema "Permanent link")

In this case, [OpenAPI](https://github.com/OAI/OpenAPI-Specification) is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc.

#### Data "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#data-schema "Permanent link")

The term "schema" might also refer to the shape of some data, like a JSON content.

In that case, it would mean the JSON attributes, and data types they have, etc.

#### OpenAPI and JSON Schema[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema "Permanent link")

OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using **JSON Schema**, the standard for JSON data schemas.

#### Check the `openapi.json`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#check-the-openapi-json "Permanent link")

If you are curious about what the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

You can see it directly at: <http://127.0.0.1:8000/openapi.json>.

It will show a JSON starting with something like:

```
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
```

#### What is OpenAPI for[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#what-is-openapi-for "Permanent link")

The OpenAPI schema is what powers the two interactive documentation systems included.

And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with **FastAPI**.

You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.