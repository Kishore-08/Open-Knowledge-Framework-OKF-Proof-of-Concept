---
id: python-epilog-https-docs-python-org-3-library-argparse-html-epilog--49b35a18
type: concept
title: epilog[¶](https://docs.python.org/3/library/argparse.html#epilog "Link to this
  heading")
description: Some programs like to display additional description of the program after
  the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### epilog[¶](https://docs.python.org/3/library/argparse.html#epilog "Link to this heading")

Some programs like to display additional description of the program after the
description of the arguments. Such text can be specified using the `epilog=`
argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):

```
>>> parser = argparse.ArgumentParser(
...     description='A foo that bars',
...     epilog="And that's how you'd foo a bar")
>>> parser.print_help()
usage: argparse.py [-h]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar
```

As with the [description](https://docs.python.org/3/library/argparse.html#description) argument, the `epilog=` text is by default
line-wrapped, but this behavior can be adjusted with the [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class)
argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser").