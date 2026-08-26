---
id: python-description-https-docs-python-org-3-library-argparse-html-de-49b35a18
type: concept
title: description[¶](https://docs.python.org/3/library/argparse.html#description
  "Link to this heading")
description: Most calls to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") constructor will use the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### description[¶](https://docs.python.org/3/library/argparse.html#description "Link to this heading")

Most calls to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor will use the
`description=` keyword argument. This argument gives a brief description of
what the program does and how it works. In help messages, the description is
displayed between the command-line usage string and the help messages for the
various arguments.

By default, the description will be line-wrapped so that it fits within the
given space. To change this behavior, see the [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class) argument.