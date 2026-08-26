---
id: python-finding-all-adverbs-https-docs-python-org-3-library-re-html--02d619bb
type: concept
title: Finding all Adverbs[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs
  "Link to this heading")
description: '[`findall()`](https://docs.python.org/3/library/re.html#re.findall "re.findall")
  matches *all* occurrences of a pattern, not just the first'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Finding all Adverbs[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs "Link to this heading")

[`findall()`](https://docs.python.org/3/library/re.html#re.findall "re.findall") matches *all* occurrences of a pattern, not just the first
one as [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") does. For example, if a writer wanted to
find all of the adverbs in some text, they might use `findall()` in
the following manner:

```
>>> text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly\b", text)
['carefully', 'quickly']
```