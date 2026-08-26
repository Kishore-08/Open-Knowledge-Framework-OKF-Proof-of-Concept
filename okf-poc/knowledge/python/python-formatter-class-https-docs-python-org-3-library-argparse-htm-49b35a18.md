---
id: python-formatter-class-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: formatter\_class[¶](https://docs.python.org/3/library/argparse.html#formatter-class
  "Link to this heading")
description: '[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") objects allow the help formatting to be customized by'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### formatter\_class[¶](https://docs.python.org/3/library/argparse.html#formatter-class "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects allow the help formatting to be customized by
specifying an alternate formatting class. Currently, there are four such
classes:

*class* argparse.RawDescriptionHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "Link to this definition")

*class* argparse.RawTextHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "Link to this definition")

*class* argparse.ArgumentDefaultsHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "Link to this definition")

*class* argparse.MetavarTypeHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.MetavarTypeHelpFormatter "Link to this definition")

[`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter") and [`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter") give
more control over how textual descriptions are displayed.
By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects line-wrap the [description](https://docs.python.org/3/library/argparse.html#description) and
[epilog](https://docs.python.org/3/library/argparse.html#epilog) texts in command-line help messages:

```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
>>> parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines
```

Passing [`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter") as `formatter_class=`
indicates that [description](https://docs.python.org/3/library/argparse.html#description) and [epilog](https://docs.python.org/3/library/argparse.html#epilog) are already correctly formatted and
should not be line-wrapped:

```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
>>> parser.print_help()
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

options:
 -h, --help  show this help message and exit
```

[`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter") maintains whitespace for all sorts of help text,
including argument descriptions. However, multiple newlines are replaced with
one. If you wish to preserve multiple blank lines, add spaces between the
newlines.

[`ArgumentDefaultsHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "argparse.ArgumentDefaultsHelpFormatter") automatically adds information about
default values to each of the argument help messages:

```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=