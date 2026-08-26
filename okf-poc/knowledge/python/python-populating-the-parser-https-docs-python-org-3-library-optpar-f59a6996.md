---
id: python-populating-the-parser-https-docs-python-org-3-library-optpar-f59a6996
type: concept
title: Populating the parser[¶](https://docs.python.org/3/library/optparse.html#populating-the-parser
  "Link to this heading")
description: There are several ways to populate the parser with options. The preferred
  way
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Populating the parser[¶](https://docs.python.org/3/library/optparse.html#populating-the-parser "Link to this heading")

There are several ways to populate the parser with options. The preferred way
is by using [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option"), as shown in section
[Tutorial](https://docs.python.org/3/library/optparse.html#optparse-tutorial). `add_option()` can be called in one of two ways:

- pass it an Option instance (as returned by `make_option()`)
- pass it any combination of positional and keyword arguments that are
  acceptable to `make_option()` (i.e., to the Option constructor), and it
  will create the Option instance for you

The other alternative is to pass a list of pre-constructed Option instances to
the OptionParser constructor, as in:

```
option_list = [
    make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
    make_option("-q", "--quiet",
                action="store_false", dest="verbose"),
    ]
parser = OptionParser(option_list=option_list)
```

(`make_option()` is a factory function for creating Option instances;
currently it is an alias for the Option constructor. A future version of
`optparse` may split Option into several classes, and `make_option()`
will pick the right class to instantiate. Do not instantiate Option directly.)