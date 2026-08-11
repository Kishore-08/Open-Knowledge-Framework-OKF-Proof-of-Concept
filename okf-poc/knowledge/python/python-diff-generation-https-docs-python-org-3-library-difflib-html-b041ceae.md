---
id: python-diff-generation-https-docs-python-org-3-library-difflib-html-b041ceae
type: concept
title: Diff generation[¶](https://docs.python.org/3/library/difflib.html#diff-generation
  "Link to this heading")
description: '*class* difflib.Differ[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Diff generation[¶](https://docs.python.org/3/library/difflib.html#diff-generation "Link to this heading")

*class* difflib.Differ[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ "Link to this definition")
:   This is a class for comparing sequences of lines of text, and producing
    human-readable differences or deltas. Differ uses [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher")
    both to compare sequences of lines, and to compare sequences of characters
    within similar (near-matching) lines.

    Each line of a `Differ` delta begins with a two-letter code:

    | Code | Meaning |
    | --- | --- |
    | `'- '` | line unique to sequence 1 |
    | `'+ '` | line unique to sequence 2 |
    | `'  '` | line common to both sequences |
    | `'? '` | line not present in either input sequence |

    Lines beginning with ‘`?`’ attempt to guide the eye to intraline differences,
    and were not present in either input sequence. These lines can be confusing if
    the sequences contain whitespace characters, such as spaces, tabs or line breaks.

    Note that `Differ`-generated deltas make no claim to be **minimal**
    diffs. To the contrary, minimal diffs are often counter-intuitive for humans,
    because they synch up anywhere possible, sometimes at accidental matches
    100 pages apart.
    Restricting synch points to contiguous matches preserves some notion of
    locality, at the occasional cost of producing a longer diff.

    The `Differ` class has this constructor:

    \_\_init\_\_(*linejunk=None*, *charjunk=None*)[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ.__init__ "Link to this definition")
    :   Optional keyword parameters *linejunk* and *charjunk* are for filter functions
        (or `None`):

        *linejunk*: A function that accepts a single string argument, and returns true
        if the string is junk. The default is `None`, meaning that no line is
        considered junk.

        *charjunk*: A function that accepts a single character argument (a string of
        length 1), and returns true if the character is junk. The default is `None`,
        meaning that no character is considered junk.

        These junk-filtering functions speed up matching to find
        differences and do not cause any differing lines or characters to
        be ignored. Read the description of the
        [`find_longest_match()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.find_longest_match "difflib.SequenceMatcher.find_longest_match") method’s *isjunk*
        parameter for an explanation.

    `Differ` objects are used (deltas generated) via a single method:

    compare(*a*, *b*)[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ.compare "Link to this definition")
    :   Compare two sequences of lines, and generate the delta (a sequence of lines).

        Each sequence must contain individual single-line strings ending with
        newlines. Such sequences can be obtained from the
        [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") method of file-like objects. The generated
        delta also consists of newline-terminated strings, ready to be
        printed as-is via the [`writelines()`](https://docs.python.org/3/library/io.html#io.IOBase.writelines "io.IOBase.writelines") method of a
        file-like object.

*class* difflib.HtmlDiff[¶](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff "Link to this definition")
:   This class can be used to create an HTML table (or a complete HTML file
    containing the table) showing a side by side, line by line comparison of text
    with inter-line and intra-line change highlights. The table can be generated in
    either full or contextual difference mode.

    Warning

    The trailing newlines get stripped before the diff, so the result can be
    incomple