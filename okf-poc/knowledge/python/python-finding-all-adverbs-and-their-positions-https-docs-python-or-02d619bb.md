---
id: python-finding-all-adverbs-and-their-positions-https-docs-python-or-02d619bb
type: concept
title: Finding all Adverbs and their Positions[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs-and-their-positions
  "Link to this heading")
description: If one wants more information about all matches of a pattern than the
  matched
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Finding all Adverbs and their Positions[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs-and-their-positions "Link to this heading")

If one wants more information about all matches of a pattern than the matched
text, [`finditer()`](https://docs.python.org/3/library/re.html#re.finditer "re.finditer") is useful as it provides [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match") objects
instead of strings. Continuing with the previous example, if a writer wanted
to find all of the adverbs *and their positions* in some text, they would use
`finditer()` in the following manner:

```
>>> text = "He was carefully disguised but captured quickly by police."
>>> for m in re.finditer(r"\w+ly\b", text):
...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
07-16: carefully
40-47: quickly
```