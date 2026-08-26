---
id: python-counter-https-docs-python-org-3-library-collections-html-col-4b36d233
type: concept
title: '[`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter
  "collections.Counter") objects[¶](https://docs.python.org/3/library/collections.html#counter-objects
  "Link to this heading")'
description: A counter tool is provided to support convenient and rapid tallies.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") objects[¶](https://docs.python.org/3/library/collections.html#counter-objects "Link to this heading")

A counter tool is provided to support convenient and rapid tallies.
For example:

```
>>> # Tally occurrences of words in a list
>>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
...
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
```

*class* collections.Counter(*\*\*kwargs*)[¶](https://docs.python.org/3/library/collections.html#collections.Counter "Link to this definition")

*class* collections.Counter(*iterable*, */*, *\*\*kwargs*)

*class* collections.Counter(*mapping*, */*, *\*\*kwargs*)
:   A `Counter` is a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") subclass for counting [hashable](https://docs.python.org/3/glossary.html#term-hashable) objects.
    It is a collection where elements are stored as dictionary keys
    and their counts are stored as dictionary values. Counts are allowed to be
    any integer value including zero or negative counts. The `Counter`
    class is similar to bags or multisets in other languages.

    Elements are counted from an *iterable* or initialized from another
    *mapping* (or counter):

    ```
    >>> c = Counter()                           # a new, empty counter
    >>> c = Counter('gallahad')                 # a new counter from an iterable
    >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
    >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
    ```

    Counter objects have a dictionary interface except that they return a zero
    count for missing items instead of raising a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError"):

    ```
    >>> c = Counter(['eggs', 'ham'])
    >>> c['bacon']                              # count of a missing element is zero
    0
    ```

    Setting a count to zero does not remove an element from a counter.
    Use `del` to remove it entirely:

    ```
    >>> c['sausage'] = 0                        # counter entry with a zero count
    >>> del c['sausage']                        # del actually removes the entry
    ```

    Added in version 3.1.

    Changed in version 3.7: As a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") subclass, `Counter`
    inherited the capability to remember insertion order. Math operations
    on *Counter* objects also preserve order. Results are ordered
    according to when an element is first encountered in the left operand
    and then by the order encountered in the right operand.

    Counter objects support additional methods beyond those available for all
    dictionaries:

    elements()[¶](https://docs.python.org/3/library/collections.html#collections.Counter.elements "Link to this definition")
    :   Return an iterator over elements repeating each as many times as its
        count. Elements are returned in the order first encountered. If an
        element’s count is less than one, `elements()` will ignore it.

        ```
        >>> c = Counter(a=4, b=2, c=0, d=-2)
        >>> sorted(c.elements())
        ['a', 'a', 'a', 'a', 'b', 'b']
        ```

    most\_common(*n=None*)[¶](https://docs.python.org/3/library/collections.html#collections.Counter.most_common "Link to this definition")
    :   Return a list of the *n* most common elements and their counts from the
        most common to the least. If *n* is omitted or `None`,
        `most_common()` returns *all* elements in the counter.
        Elements wit