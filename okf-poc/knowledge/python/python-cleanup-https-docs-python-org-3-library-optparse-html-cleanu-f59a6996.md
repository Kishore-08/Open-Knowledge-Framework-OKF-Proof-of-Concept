---
id: python-cleanup-https-docs-python-org-3-library-optparse-html-cleanu-f59a6996
type: concept
title: Cleanup[¶](https://docs.python.org/3/library/optparse.html#cleanup "Link to
  this heading")
description: OptionParser instances have several cyclic references. This should not
  be a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Cleanup[¶](https://docs.python.org/3/library/optparse.html#cleanup "Link to this heading")

OptionParser instances have several cyclic references. This should not be a
problem for Python’s garbage collector, but you may wish to break the cyclic
references explicitly by calling `destroy()` on your
OptionParser once you are done with it. This is particularly useful in
long-running applications where large object graphs are reachable from your
OptionParser.