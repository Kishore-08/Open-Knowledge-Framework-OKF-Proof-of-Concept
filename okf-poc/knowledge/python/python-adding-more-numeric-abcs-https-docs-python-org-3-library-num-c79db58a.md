---
id: python-adding-more-numeric-abcs-https-docs-python-org-3-library-num-c79db58a
type: concept
title: Adding More Numeric ABCs[¶](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs
  "Link to this heading")
description: There are, of course, more possible ABCs for numbers, and this would
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/numbers.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Adding More Numeric ABCs[¶](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs "Link to this heading")

There are, of course, more possible ABCs for numbers, and this would
be a poor hierarchy if it precluded the possibility of adding
those. You can add `MyFoo` between [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex") and
[`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real") with:

```
class MyFoo(Complex): ...
MyFoo.register(Real)
```