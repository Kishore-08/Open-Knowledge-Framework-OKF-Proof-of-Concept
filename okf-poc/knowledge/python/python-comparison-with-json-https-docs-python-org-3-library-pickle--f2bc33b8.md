---
id: python-comparison-with-json-https-docs-python-org-3-library-pickle--f2bc33b8
type: concept
title: Comparison with `json`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-json
  "Link to this heading")
description: There are fundamental differences between the pickle protocols and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Comparison with `json`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-json "Link to this heading")

There are fundamental differences between the pickle protocols and
[JSON (JavaScript Object Notation)](https://json.org):

- JSON is a text serialization format (it outputs unicode text, although
  most of the time it is then encoded to `utf-8`), while pickle is
  a binary serialization format;
- JSON is human-readable, while pickle is not;
- JSON is interoperable and widely used outside of the Python ecosystem,
  while pickle is Python-specific;
- JSON, by default, can only represent a subset of the Python built-in
  types, and no custom classes; pickle can represent an extremely large
  number of Python types (many of them automatically, by clever usage
  of Python’s introspection facilities; complex cases can be tackled by
  implementing [specific object APIs](https://docs.python.org/3/library/pickle.html#pickle-inst));
- Unlike pickle, deserializing untrusted JSON does not in itself create an
  arbitrary code execution vulnerability.

See also

The [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.") module: a standard library module allowing JSON
serialization and deserialization.