---
id: python-exceptions-https-docs-python-org-3-library-graphlib-html-exc-2d2db348
type: concept
title: Exceptions[¶](https://docs.python.org/3/library/graphlib.html#exceptions "Link
  to this heading")
description: 'The `graphlib` module defines the following exception classes:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/graphlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Exceptions[¶](https://docs.python.org/3/library/graphlib.html#exceptions "Link to this heading")

The `graphlib` module defines the following exception classes:

*exception* graphlib.CycleError[¶](https://docs.python.org/3/library/graphlib.html#graphlib.CycleError "Link to this definition")
:   Subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") raised by [`TopologicalSorter.prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare") if cycles exist
    in the working graph. If multiple cycles exist, only one undefined choice among them will
    be reported and included in the exception.

    The detected cycle can be accessed via the second element in the [`args`](https://docs.python.org/3/library/exceptions.html#BaseException.args "BaseException.args")
    attribute of the exception instance and consists in a list of nodes, such that each node is,
    in the graph, an immediate predecessor of the next node in the list. In the reported list,
    the first and the last node will be the same, to make it clear that it is cyclic.