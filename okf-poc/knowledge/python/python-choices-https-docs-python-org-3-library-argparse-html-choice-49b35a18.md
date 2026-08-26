---
id: python-choices-https-docs-python-org-3-library-argparse-html-choice-49b35a18
type: concept
title: choices[¶](https://docs.python.org/3/library/argparse.html#choices "Link to
  this heading")
description: Some command-line arguments should be selected from a restricted set
  of values.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### choices[¶](https://docs.python.org/3/library/argparse.html#choices "Link to this heading")

Some command-line arguments should be selected from a restricted set of values.
These can be handled by passing a sequence object as the *choices* keyword
argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). When the command line is
parsed, argument values will be checked, and an error message will be displayed
if the argument was not one of the acceptable values:

```
>>> parser = argparse.ArgumentParser(prog='game.py')
>>> parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
>>> parser.parse_args(['rock'])
Namespace(move='rock')
>>> parser.parse_args(['fire'])
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')
```

Any sequence can be passed as the *choices* value, so [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") objects,
[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") objects, and custom sequences are all supported.

Use of [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") is not recommended because it is difficult to
control its appearance in usage, help, and error messages.

Note that *choices* are checked after any [type](https://docs.python.org/3/library/argparse.html#type)
conversions have been performed, so objects in *choices*
should match the [type](https://docs.python.org/3/library/argparse.html#type) specified. This can make *choices*
appear unfamiliar in usage, help, or error messages.

To keep *choices* user-friendly, consider a custom type wrapper that
converts and formats values, or omit [type](https://docs.python.org/3/library/argparse.html#type) and handle conversion in
your application code.

Formatted choices override the default *metavar* which is normally derived
from *dest*. This is usually what you want because the user never sees the
*dest* parameter. If this display isn’t desirable (perhaps because there are
many choices), just specify an explicit [metavar](https://docs.python.org/3/library/argparse.html#metavar).