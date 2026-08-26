---
id: python-conversion-table-https-docs-python-org-3-library-tomllib-htm-00f2bfaf
type: concept
title: Conversion Table[¶](https://docs.python.org/3/library/tomllib.html#conversion-table
  "Link to this heading")
description: '| TOML | Python |'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tomllib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Conversion Table[¶](https://docs.python.org/3/library/tomllib.html#conversion-table "Link to this heading")

| TOML | Python |
| --- | --- |
| TOML document | dict |
| string | str |
| integer | int |
| float | float (configurable with *parse\_float*) |
| boolean | bool |
| offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`) |
| local date-time | datetime.datetime (`tzinfo` attribute set to `None`) |
| local date | datetime.date |
| local time | datetime.time |
| array | list |
| table | dict |
| inline table | dict |
| array of tables | list of dicts |