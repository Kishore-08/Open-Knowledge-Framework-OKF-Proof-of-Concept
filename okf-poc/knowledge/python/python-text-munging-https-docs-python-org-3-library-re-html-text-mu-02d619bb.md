---
id: python-text-munging-https-docs-python-org-3-library-re-html-text-mu-02d619bb
type: concept
title: Text Munging[¶](https://docs.python.org/3/library/re.html#text-munging "Link
  to this heading")
description: '[`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub")
  replaces every occurrence of a pattern with a string or the'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Text Munging[¶](https://docs.python.org/3/library/re.html#text-munging "Link to this heading")

[`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub") replaces every occurrence of a pattern with a string or the
result of a function. This example demonstrates using `sub()` with
a function to “munge” text, or randomize the order of all the characters
in each word of a sentence except for the first and last characters:

```
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
...
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
```