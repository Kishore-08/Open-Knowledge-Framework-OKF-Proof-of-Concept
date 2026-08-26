---
id: python-sequencematcher-objects-https-docs-python-org-3-library-diff-b041ceae
type: concept
title: SequenceMatcher objects[¶](https://docs.python.org/3/library/difflib.html#sequencematcher-objects
  "Link to this heading")
description: '*class* difflib.SequenceMatcher(*isjunk=None*, *a=''''*, *b=''''*, *autojunk=True*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## SequenceMatcher objects[¶](https://docs.python.org/3/library/difflib.html#sequencematcher-objects "Link to this heading")

*class* difflib.SequenceMatcher(*isjunk=None*, *a=''*, *b=''*, *autojunk=True*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "Link to this definition")
:   Optional argument *isjunk* must be `None` (the default) or a one-argument
    function that takes a sequence element and returns true if and only if the
    element is “junk” and should be ignored. Passing `None` for *isjunk* is
    equivalent to passing `lambda x: False`; in other words, no elements are ignored.
    For example, pass:

    ```
    lambda x: x in " \t"
    ```

    if you’re comparing lines as sequences of characters, and don’t want to synch up
    on blanks or hard tabs.

    The optional arguments *a* and *b* are sequences to be compared; both default to
    empty strings. The elements of both sequences must be [hashable](https://docs.python.org/3/glossary.html#term-hashable).

    The optional argument *autojunk* can be used to disable the automatic junk
    heuristic.

    Changed in version 3.2: Added the *autojunk* parameter.

    SequenceMatcher objects get three data attributes: *bjunk* is the
    set of elements of *b* for which *isjunk* is `True`; *bpopular* is the set of
    non-junk elements considered popular by the heuristic (if it is not
    disabled); *b2j* is a dict mapping the remaining elements of *b* to a list
    of positions where they occur. All three are reset whenever *b* is reset
    with [`set_seqs()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seqs "difflib.SequenceMatcher.set_seqs") or [`set_seq2()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "difflib.SequenceMatcher.set_seq2").

    Added in version 3.2: The *bjunk* and *bpopular* attributes.

    `SequenceMatcher` objects have the following methods:

    set\_seqs(*a*, *b*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seqs "Link to this definition")
    :   Set the two sequences to be compared.

    `SequenceMatcher` computes and caches detailed information about the
    second sequence, so if you want to compare one sequence against many
    sequences, use [`set_seq2()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "difflib.SequenceMatcher.set_seq2") to set the commonly used sequence once and
    call [`set_seq1()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq1 "difflib.SequenceMatcher.set_seq1") repeatedly, once for each of the other sequences.

    set\_seq1(*a*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq1 "Link to this definition")
    :   Set the first sequence to be compared. The second sequence to be compared
        is not changed.

    set\_seq2(*b*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "Link to this definition")
    :   Set the second sequence to be compared. The first sequence to be compared
        is not changed.

    find\_longest\_match(*alo=0*, *ahi=None*, *blo=0*, *bhi=None*)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.find_longest_match "Link to this definition")
    :   Find longest matching block in `a[alo:ahi]` and `b[blo:bhi]`.

        If *isjunk* was omitted or `None`, `find_longest_match()` returns
        `(i, j, k)` such that `a[i:i+k]` is equal to `b[j:j+k]`, where `alo
        <= i <= i+k <= ahi` and `blo <= j <= j+k <= bhi`. For all `(i', j',
        k')` meeting those conditions, the additional conditions `k >= k'`, `i
        <= i'`, and if `i == i'`, `j <= j'` are also met. In other words, of
        all maximal matching blocks, return one that starts earliest in *a*, and
        of all those maximal matching blocks that start earliest in *a*, return
        the one that starts earliest in *b*.

        ```