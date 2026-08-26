---
id: python-raw-string-notation-https-docs-python-org-3-library-re-html--02d619bb
type: concept
title: Raw String Notation[¶](https://docs.python.org/3/library/re.html#raw-string-notation
  "Link to this heading")
description: Raw string notation (`r"text"`) keeps regular expressions sane. Without
  it,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Raw String Notation[¶](https://docs.python.org/3/library/re.html#raw-string-notation "Link to this heading")

Raw string notation (`r"text"`) keeps regular expressions sane. Without it,
every backslash (`'\'`) in a regular expression would have to be prefixed with
another one to escape it. For example, the two following lines of code are
functionally identical:

```
>>> re.match(r"\W(.)\1\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
>>> re.match("\\W(.)\\1\\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
```

When one wants to match a literal backslash, it must be escaped in the regular
expression. With raw string notation, this means `r"\\"`. Without raw string
notation, one must use `"\\\\"`, making the following lines of code
functionally identical:

```
>>> re.match(r"\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
>>> re.match("\\\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
```