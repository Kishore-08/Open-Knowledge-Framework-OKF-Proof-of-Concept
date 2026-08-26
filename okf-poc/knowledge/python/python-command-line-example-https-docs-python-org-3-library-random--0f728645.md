---
id: python-command-line-example-https-docs-python-org-3-library-random--0f728645
type: concept
title: Command-line example[¶](https://docs.python.org/3/library/random.html#command-line-example
  "Link to this heading")
description: 'Here are some examples of the `random` command-line interface:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-line example[¶](https://docs.python.org/3/library/random.html#command-line-example "Link to this heading")

Here are some examples of the `random` command-line interface:

```
$ # Choose one at random
$ python -m random egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
Lobster Thermidor aux crevettes with a Mornay sauce

$ # Random integer
$ python -m random 6
6

$ # Random floating-point number
$ python -m random 1.8
1.7080016272295635

$ # With explicit arguments
$ python  -m random --choice egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
egg

$ python -m random --integer 6
3

$ python -m random --float 1.8
1.5666339105010318

$ python -m random --integer 6
5

$ python -m random --float 6
3.1942323316565915
```