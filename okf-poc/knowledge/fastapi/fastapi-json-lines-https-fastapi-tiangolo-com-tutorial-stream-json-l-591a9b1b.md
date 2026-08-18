---
id: fastapi-json-lines-https-fastapi-tiangolo-com-tutorial-stream-json-l-591a9b1b
type: concept
title: JSON Lines[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#json-lines
  "Permanent link")
description: In these cases, it's common to send "**JSON Lines**", which is a format
  where you send one JSON object per line.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/stream-json-lines/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## JSON Lines[¶](https://fastapi.tiangolo.com/tutorial/stream-json-lines/#json-lines "Permanent link")

In these cases, it's common to send "**JSON Lines**", which is a format where you send one JSON object per line.

A response would have a content type of `application/jsonl` (instead of `application/json`) and the body would be something like:

```
{"name": "Plumbus", "description": "A multi-purpose household device."}
{"name": "Portal Gun", "description": "A portal opening device."}
{"name": "Meeseeks Box", "description": "A box that summons a Meeseeks."}
```

It's very similar to a JSON array (equivalent of a Python list), but instead of being wrapped in `[]` and having `,` between the items, it has **one JSON object per line**, they are separated by a new line character.

Note

The important point is that your app will be able to produce each line in turn, while the client consumes the previous lines.

Technical Details

Because each JSON object will be separated by a new line, they can't contain literal new line characters in their content, but they can contain escaped new lines (`\n`), which is part of the JSON standard.

But normally you won't have to worry about it, it's done automatically, continue reading. 🤓