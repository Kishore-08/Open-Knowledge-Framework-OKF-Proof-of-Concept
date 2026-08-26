---
id: python-unnamed-sections-https-docs-python-org-3-library-configparse-caa28eb2
type: concept
title: Unnamed Sections[¶](https://docs.python.org/3/library/configparser.html#unnamed-sections
  "Link to this heading")
description: The name of the first section (or unique) may be omitted and values
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Unnamed Sections[¶](https://docs.python.org/3/library/configparser.html#unnamed-sections "Link to this heading")

The name of the first section (or unique) may be omitted and values
retrieved by the [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION") attribute.

```
>>> config = """
... option = value
...
... [  Section 2  ]
... another = val
... """
>>> unnamed = configparser.ConfigParser(allow_unnamed_section=True)
>>> unnamed.read_string(config)
>>> unnamed.get(configparser.UNNAMED_SECTION, 'option')
'value'
```