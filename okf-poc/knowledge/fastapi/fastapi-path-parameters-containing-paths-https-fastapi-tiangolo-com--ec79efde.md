---
id: fastapi-path-parameters-containing-paths-https-fastapi-tiangolo-com--ec79efde
type: concept
title: Path parameters containing paths[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths
  "Permanent link")
description: Let's say you have a *path operation* with a path `/files/{file_path}`.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/path-params/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Path parameters containing paths[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths "Permanent link")

Let's say you have a *path operation* with a path `/files/{file_path}`.

But you need `file_path` itself to contain a *path*, like `home/johndoe/myfile.txt`.

So, the URL for that file would be something like: `/files/home/johndoe/myfile.txt`.