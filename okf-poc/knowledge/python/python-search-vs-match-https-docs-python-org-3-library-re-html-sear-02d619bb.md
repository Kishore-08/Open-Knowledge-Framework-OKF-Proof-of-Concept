---
id: python-search-vs-match-https-docs-python-org-3-library-re-html-sear-02d619bb
type: concept
title: search() vs. match()[¶](https://docs.python.org/3/library/re.html#search-vs-match
  "Link to this heading")
description: 'Python offers different primitive operations based on regular expressions:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### search() vs. match()[¶](https://docs.python.org/3/library/re.html#search-vs-match "Link to this heading")

Python offers different primitive operations based on regular expressions:

- [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match") checks for a match only at the beginning of the string
- [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search") checks for a match anywhere in the string
  (this is what Perl does by default)
- [`re.fullmatch()`](https://docs.python.org/3/library/re.html#re.fullmatch "re.fullmatch") checks for entire string to be a match

For example:

```
>>> re.match("c", "abcdef")    # No match
>>> re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
>>> re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
>>> re.fullmatch("r.*n", "python") # No match
```

Regular expressions beginning with `'^'` can be used with [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") to
restrict the match at the beginning of the string:

```
>>> re.match("c", "abcdef")    # No match
>>> re.search("^c", "abcdef")  # No match
>>> re.search("^a", "abcdef")  # Match
<re.Match object; span=(0, 1), match='a'>
```

Note however that in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode [`match()`](https://docs.python.org/3/library/re.html#re.match "re.match") only matches at the
beginning of the string, whereas using [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") with a regular expression
beginning with `'^'` will match at the beginning of each line.

```
>>> re.match("X", "A\nB\nX", re.MULTILINE)  # No match
>>> re.search("^X", "A\nB\nX", re.MULTILINE)  # Match
<re.Match object; span=(4, 5), match='X'>
```