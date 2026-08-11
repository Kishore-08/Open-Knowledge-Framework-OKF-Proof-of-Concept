---
id: python-lists-https-docs-python-org-3-library-stdtypes-html-lists-li-5e0bc1d7
type: concept
title: Lists[¶](https://docs.python.org/3/library/stdtypes.html#lists "Link to this
  heading")
description: Lists are mutable sequences, typically used to store collections of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Lists[¶](https://docs.python.org/3/library/stdtypes.html#lists "Link to this heading")

Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).

*class* list(*iterable=()*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#list "Link to this definition")
:   Lists may be constructed in several ways:

    - Using a pair of square brackets to denote the empty list: `[]`
    - Using square brackets, separating items with commas: `[a]`, `[a, b, c]`
    - Using a list comprehension: `[x for x in iterable]`
    - Using the type constructor: `list()` or `list(iterable)`

    The constructor builds a list whose items are the same and in the same
    order as *iterable*’s items. *iterable* may be either a sequence, a
    container that supports iteration, or an iterator object. If *iterable*
    is already a list, a copy is made and returned, similar to `iterable[:]`.
    For example, `list('abc')` returns `['a', 'b', 'c']` and
    `list( (1, 2, 3) )` returns `[1, 2, 3]`.
    If no argument is given, the constructor creates a new empty list, `[]`.

    Many other operations also produce lists, including the [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted")
    built-in.

    Lists are [generic](https://docs.python.org/3/library/typing.html#generics) over the types of their items.

    Lists implement all of the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common) and
    [mutable](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) sequence operations. Lists also provide the
    following additional method:

    sort(*\**, *key=None*, *reverse=False*)[¶](https://docs.python.org/3/library/stdtypes.html#list.sort "Link to this definition")
    :   This method sorts the list in place, using only `<` comparisons
        between items. Exceptions are not suppressed - if any comparison operations
        fail, the entire sort operation will fail (and the list will likely be left
        in a partially modified state).

        `sort()` accepts two arguments that can only be passed by keyword
        ([keyword-only arguments](https://docs.python.org/3/glossary.html#keyword-only-parameter)):

        *key* specifies a function of one argument that is used to extract a
        comparison key from each list element (for example, `key=str.lower`).
        The key corresponding to each item in the list is calculated once and
        then used for the entire sorting process. The default value of `None`
        means that list items are sorted directly without calculating a separate
        key value.

        The [`functools.cmp_to_key()`](https://docs.python.org/3/library/functools.html#functools.cmp_to_key "functools.cmp_to_key") utility is available to convert a 2.x
        style *cmp* function to a *key* function.

        *reverse* is a boolean value. If set to `True`, then the list elements
        are sorted as if each comparison were reversed.

        This method modifies the sequence in place for economy of space when
        sorting a large sequence. To remind users that it operates by side
        effect, it does not return the sorted sequence (use [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted") to
        explicitly request a new sorted list instance).

        The `sort()` method is guaranteed to be stable. A sort is stable if it
        guarantees not to change the relative order of elements that compare equal
        — this is helpful for sorting in multiple passes (for example, sort by
        department, then by salary grade).

        For sorting examples and a brief sorting tutorial, see [Sorting Techniques](https://docs.python.org/3/howto/sorting.html#sortinghowto).

        **CPython implementation detail:** While a list is being sorted, the effect of attempting to mutate, or even
        inspect, the list is undefined. The C im