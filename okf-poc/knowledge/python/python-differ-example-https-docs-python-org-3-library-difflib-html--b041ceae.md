---
id: python-differ-example-https-docs-python-org-3-library-difflib-html--b041ceae
type: concept
title: Differ example[¶](https://docs.python.org/3/library/difflib.html#differ-example
  "Link to this heading")
description: This example compares two texts. First we set up the texts, sequences
  of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Differ example[¶](https://docs.python.org/3/library/difflib.html#differ-example "Link to this heading")

This example compares two texts. First we set up the texts, sequences of
individual single-line strings ending with newlines (such sequences can also be
obtained from the [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") method of file-like objects):

```
>>> text1 = '''  1. Beautiful is better than ugly.
...   2. Explicit is better than implicit.
...   3. Simple is better than complex.
...   4. Complex is better than complicated.
... '''.splitlines(keepends=True)
>>> len(text1)
4
>>> text1[0][-1]
'\n'
>>> text2 = '''  1. Beautiful is better than ugly.
...   3.   Simple is better than complex.
...   4. Complicated is better than complex.
...   5. Flat is better than nested.
... '''.splitlines(keepends=True)
```

Next we instantiate a Differ object:

```
>>> d = Differ()
```

Note that when instantiating a [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") object we may pass functions to
filter out line and character “junk.” See the [`Differ()`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") constructor for
details.

Finally, we compare the two:

```
>>> result = list(d.compare(text1, text2))
```

`result` is a list of strings, so let’s pretty-print it:

```
>>> from pprint import pprint
>>> pprint(result)
['    1. Beautiful is better than ugly.\n',
 '-   2. Explicit is better than implicit.\n',
 '-   3. Simple is better than complex.\n',
 '+   3.   Simple is better than complex.\n',
 '?     ++\n',
 '-   4. Complex is better than complicated.\n',
 '?            ^                     ---- ^\n',
 '+   4. Complicated is better than complex.\n',
 '?           ++++ ^                      ^\n',
 '+   5. Flat is better than nested.\n']
```

As a single multi-line string it looks like this:

```
>>> import sys
>>> sys.stdout.writelines(result)
    1. Beautiful is better than ugly.
-   2. Explicit is better than implicit.
-   3. Simple is better than complex.
+   3.   Simple is better than complex.
?     ++
-   4. Complex is better than complicated.
?            ^                     ---- ^
+   4. Complicated is better than complex.
?           ++++ ^                      ^
+   5. Flat is better than nested.
```