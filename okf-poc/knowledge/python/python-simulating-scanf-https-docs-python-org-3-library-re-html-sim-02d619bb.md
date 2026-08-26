---
id: python-simulating-scanf-https-docs-python-org-3-library-re-html-sim-02d619bb
type: concept
title: Simulating scanf()[¶](https://docs.python.org/3/library/re.html#simulating-scanf
  "Link to this heading")
description: Python does not currently have an equivalent to `scanf()`. Regular
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Simulating scanf()[¶](https://docs.python.org/3/library/re.html#simulating-scanf "Link to this heading")

Python does not currently have an equivalent to `scanf()`. Regular
expressions are generally more powerful, though also more verbose, than
`scanf()` format strings. The table below offers some more-or-less
equivalent mappings between `scanf()` format tokens and regular
expressions.

| `scanf()` Token | Regular Expression |
| --- | --- |
| `%c` | `.` |
| `%5c` | `.{5}` |
| `%d` | `[-+]?\d+` |
| `%e`, `%E`, `%f`, `%g` | `[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?` |
| `%i` | `[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)` |
| `%o` | `[-+]?[0-7]+` |
| `%s` | `\S+` |
| `%u` | `\d+` |
| `%x`, `%X` | `[-+]?(0[xX])?[\dA-Fa-f]+` |

To extract the filename and numbers from a string like

```
/usr/sbin/sendmail - 0 errors, 4 warnings
```

you would use a `scanf()` format like

```
%s - %d errors, %d warnings
```

The equivalent regular expression would be

```
(\S+) - (\d+) errors, (\d+) warnings
```