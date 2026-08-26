---
id: python-graphlib-functionality-to-operate-with-graph-like-structures-2d2db348
type: concept
title: '`graphlib` — Functionality to operate with graph-like structures[¶](https://docs'
description: '**Source code:** [Lib/graphlib.py](https://github.com/python/cpython/tree/3.14/Lib/graphlib.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/graphlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `graphlib` — Functionality to operate with graph-like structures[¶](https://docs.python.org/3/library/graphlib.html#module-graphlib "Link to this heading")

**Source code:** [Lib/graphlib.py](https://github.com/python/cpython/tree/3.14/Lib/graphlib.py)

---

*class* graphlib.TopologicalSorter(*graph=None*)[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter "Link to this definition")
:   Provides functionality to topologically sort a graph of [hashable](https://docs.python.org/3/glossary.html#term-hashable) nodes.

    A topological order is a linear ordering of the vertices in a graph such that
    for every directed edge u -> v from vertex u to vertex v, vertex u comes
    before vertex v in the ordering. For instance, the vertices of the graph may
    represent tasks to be performed, and the edges may represent constraints that
    one task must be performed before another; in this example, a topological
    ordering is just a valid sequence for the tasks. A complete topological
    ordering is possible if and only if the graph has no directed cycles, that
    is, if it is a directed acyclic graph.

    If the optional *graph* argument is provided it must be a dictionary
    representing a directed acyclic graph where the keys are nodes and the values
    are iterables of all predecessors of that node in the graph (the nodes that
    have edges that point to the value in the key). Additional nodes can be added
    to the graph using the [`add()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.add "graphlib.TopologicalSorter.add") method.

    In the general case, the steps required to perform the sorting of a given
    graph are as follows:

    - Create an instance of the `TopologicalSorter` with an optional
      initial graph.
    - Add additional nodes to the graph.
    - Call [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare") on the graph.
    - While [`is_active()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.is_active "graphlib.TopologicalSorter.is_active") is `True`, iterate over
      the nodes returned by [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready") and
      process them. Call [`done()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "graphlib.TopologicalSorter.done") on each node as it
      finishes processing.

    In case just an immediate sorting of the nodes in the graph is required and
    no parallelism is involved, the convenience method
    [`TopologicalSorter.static_order()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.static_order "graphlib.TopologicalSorter.static_order") can be used directly:

    ```
    >>> graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    >>> ts = TopologicalSorter(graph)
    >>> tuple(ts.static_order())
    ('A', 'C', 'B', 'D')
    ```

    The class is designed to easily support parallel processing of the nodes as
    they become ready. For instance:

    ```
    topological_sorter = TopologicalSorter()

    # Add nodes to 'topological_sorter'...

    topological_sorter.prepare()
    while topological_sorter.is_active():
        for node in topological_sorter.get_ready():
            # Worker threads or processes take nodes to work on off the
            # 'task_queue' queue.
            task_queue.put(node)

        # When the work for a node is done, workers put the node in
        # 'finalized_tasks_queue' so we can get more nodes to work on.
        # The definition of 'is_active()' guarantees that, at this point, at
        # least one node has been placed on 'task_queue' that hasn't yet
        # been passed to 'done()', so this blocking 'get()' must (eventually)
        # succeed.  After calling 'done()', we loop back to call 'get_ready()'