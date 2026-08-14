---
id: fastapi-metadata-for-tags-https-fastapi-tiangolo-com-tutorial-metada-afa173ff
type: concept
title: Metadata for tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags
  "Permanent link")
description: You can also add additional metadata for the different tags used to group
  your path operations with the parameter `openapi_tags`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/metadata/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Metadata for tags[¶](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags "Permanent link")

You can also add additional metadata for the different tags used to group your path operations with the parameter `openapi_tags`.

It takes a list containing one dictionary for each tag.

Each dictionary can contain:

- `name` (**required**): a `str` with the same tag name you use in the `tags` parameter in your *path operations* and `APIRouter`s.
- `description`: a `str` with a short description for the tag. It can have Markdown and will be shown in the docs UI.
- `externalDocs`: a `dict` describing external documentation with:
  - `description`: a `str` with a short description for the external docs.
  - `url` (**required**): a `str` with the URL for the external documentation.