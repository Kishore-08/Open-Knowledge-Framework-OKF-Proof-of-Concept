---
id: python-argument-abbreviations-prefix-matching-https-docs-python-org-49b35a18
type: concept
title: Argument abbreviations (prefix matching)[¶](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching
  "Link to this heading")
description: The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "argparse.ArgumentParser.parse_args") method [by default](https://docs.python.org/3/library/argp
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Argument abbreviations (prefix matching)[¶](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching "Link to this heading")

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method [by default](https://docs.python.org/3/library/argparse.html#allow-abbrev)
allows long options to be abbreviated to a prefix, if the abbreviation is
unambiguous (the prefix matches a unique option):

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-bacon')
>>> parser.add_argument('-badger')
>>> parser.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
>>> parser.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
>>> parser.parse_args('-ba BA'.split())
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon
```

An error is produced for arguments that could produce more than one options.
This feature can be disabled by setting [allow\_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev) to `False`.