---
id: python-putting-it-all-together-https-docs-python-org-3-library-optp-f59a6996
type: concept
title: Putting it all together[¶](https://docs.python.org/3/library/optparse.html#putting-it-all-together
  "Link to this heading")
description: 'Here’s what `optparse`-based scripts usually look like:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Putting it all together[¶](https://docs.python.org/3/library/optparse.html#putting-it-all-together "Link to this heading")

Here’s what `optparse`-based scripts usually look like:

```
from optparse import OptionParser
...
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    ...
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print("reading %s..." % options.filename)
    ...

if __name__ == "__main__":
    main()
```

## Reference Guide[¶](https://docs.python.org/3/library/optparse.html#reference-guide "Link to this heading")