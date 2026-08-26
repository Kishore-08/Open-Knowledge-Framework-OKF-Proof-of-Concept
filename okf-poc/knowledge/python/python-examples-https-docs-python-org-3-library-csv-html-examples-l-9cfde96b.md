---
id: python-examples-https-docs-python-org-3-library-csv-html-examples-l-9cfde96b
type: concept
title: Examples[¶](https://docs.python.org/3/library/csv.html#examples "Link to this
  heading")
description: 'The simplest example of reading a CSV file:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/csv.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples[¶](https://docs.python.org/3/library/csv.html#examples "Link to this heading")

The simplest example of reading a CSV file:

```
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Reading a file with an alternate format:

```
import csv
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
```

The corresponding simplest possible writing example is:

```
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```

Since [`open()`](https://docs.python.org/3/library/functions.html#open "open") is used to open a CSV file for reading, the file
will by default be decoded into unicode using the system default
encoding (see [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")). To decode a file
using a different encoding, use the `encoding` argument of open:

```
import csv
with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

The same applies to writing in something other than the system default
encoding: specify the encoding argument when opening the output file.

Registering a new dialect:

```
import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
```

A slightly more advanced use of the reader — catching and reporting errors:

```
import csv, sys
filename = 'some.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit(f'file {filename}, line {reader.line_num}: {e}')
```

And while the module doesn’t directly support parsing strings, it can easily be
done:

```
import csv
for row in csv.reader(['one,two,three']):
    print(row)
```

Footnotes