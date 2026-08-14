---
id: fastapi-metadata-for-api-https-fastapi-tiangolo-com-tutorial-metadat-afa173ff
type: concept
title: Metadata for API[¶](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api
  "Permanent link")
description: 'You can set the following fields that are used in the OpenAPI specification
  and the automatic API docs UIs:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Metadata for API[¶](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api "Permanent link")

You can set the following fields that are used in the OpenAPI specification and the automatic API docs UIs:

| Parameter | Type | Description |
| --- | --- | --- |
| `title` | `str` | The title of the API. |
| `summary` | `str` | A short summary of the API. Available since OpenAPI 3.1.0, FastAPI 0.99.0. |
| `description` | `str` | A short description of the API. It can use Markdown. |
| `version` | `str` | The version of the API. This is the version of your own application, not of OpenAPI. For example `2.5.0`. |
| `terms_of_service` | `str` | A URL to the Terms of Service for the API. If provided, this has to be a URL. |
| `contact` | `dict` | The contact information for the exposed API. It can contain several fields. `contact` fields  | Parameter | Type | Description | | --- | --- | --- | | `name` | `str` | The identifying name of the contact person/organization. | | `url` | `str` | The URL pointing to the contact information. MUST be in the format of a URL. | | `email` | `str` | The email address of the contact person/organization. MUST be in the format of an email address. | |
| `license_info` | `dict` | The license information for the exposed API. It can contain several fields. `license_info` fields  | Parameter | Type | Description | | --- | --- | --- | | `name` | `str` | **REQUIRED** (if a `license_info` is set). The license name used for the API. | | `identifier` | `str` | An [SPDX](https://spdx.org/licenses/) license expression for the API. The `identifier` field is mutually exclusive of the `url` field. Available since OpenAPI 3.1.0, FastAPI 0.99.0. | | `url` | `str` | A URL to the license used for the API. MUST be in the format of a URL. | |

You can set them as follows:

Python 3.10+

```
from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.