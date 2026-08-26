---
id: python-example-https-docs-python-org-3-library-shelve-html-example--cdcf0600
type: concept
title: Example[¶](https://docs.python.org/3/library/shelve.html#example "Link to this
  heading")
description: To summarize the interface (`key` is a string, `data` is an arbitrary
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shelve.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Example[¶](https://docs.python.org/3/library/shelve.html#example "Link to this heading")

To summarize the interface (`key` is a string, `data` is an arbitrary
object):

```
import shelve

d = shelve.open(filename)  # open -- file may get suffix added by low-level
                           # library

d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
```

See also

Module [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix \"database\" formats.")
:   Generic interface to `dbm`-style databases.

Module [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
:   Object serialization used by `shelve`.