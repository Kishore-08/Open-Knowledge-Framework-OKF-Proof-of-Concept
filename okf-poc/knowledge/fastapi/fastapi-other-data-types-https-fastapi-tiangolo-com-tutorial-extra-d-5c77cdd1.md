---
id: fastapi-other-data-types-https-fastapi-tiangolo-com-tutorial-extra-d-5c77cdd1
type: concept
title: Other data types[¶](https://fastapi.tiangolo.com/tutorial/extra-data-types/#other-data-types
  "Permanent link")
description: 'Here are some of the additional data types you can use:'
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/extra-data-types/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Other data types[¶](https://fastapi.tiangolo.com/tutorial/extra-data-types/#other-data-types "Permanent link")

Here are some of the additional data types you can use:

- `UUID`:
  - A standard "Universally Unique Identifier", common as an ID in many databases and systems.
  - In requests and responses will be represented as a `str`.
- `datetime.datetime`:
  - A Python `datetime.datetime`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `2008-09-15T15:53:00+05:00`.
- `datetime.date`:
  - Python `datetime.date`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `2008-09-15`.
- `datetime.time`:
  - A Python `datetime.time`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `14:23:55.003`.
- `datetime.timedelta`:
  - A Python `datetime.timedelta`.
  - In requests and responses will be represented as a `float` of total seconds.
  - Pydantic also allows representing it as an "ISO 8601 time diff encoding", [see the docs for more info](https://pydantic.dev/docs/validation/latest/concepts/serialization/#custom-serializers).
- `frozenset`:
  - In requests and responses, treated the same as a `set`:
    - In requests, a list will be read, eliminating duplicates and converting it to a `set`.
    - In responses, the `set` will be converted to a `list`.
    - The generated schema will specify that the `set` values are unique (using JSON Schema's `uniqueItems`).
- `bytes`:
  - Standard Python `bytes`.
  - In requests and responses will be treated as `str`.
  - The generated schema will specify that it's a `str` with `binary` "format".
- `Decimal`:
  - Standard Python `Decimal`.
  - In requests and responses, handled the same as a `float`.
- You can check all the valid Pydantic data types here: [Pydantic data types](https://pydantic.dev/docs/validation/latest/concepts/types/).