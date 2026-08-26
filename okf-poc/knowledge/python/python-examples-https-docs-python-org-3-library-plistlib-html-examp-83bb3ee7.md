---
id: python-examples-https-docs-python-org-3-library-plistlib-html-examp-83bb3ee7
type: concept
title: Examples[¶](https://docs.python.org/3/library/plistlib.html#examples "Link
  to this heading")
description: 'Generating a plist:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/plistlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples[¶](https://docs.python.org/3/library/plistlib.html#examples "Link to this heading")

Generating a plist:

```
import datetime as dt
import plistlib

pl = dict(
    aString = "Doodah",
    aList = ["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat = 0.1,
    anInt = 728,
    aDict = dict(
        anotherString = "<hello & hi there!>",
        aThirdString = "M\xe4ssig, Ma\xdf",
        aTrueValue = True,
        aFalseValue = False,
    ),
    someData = b"<binary gunk>",
    someMoreData = b"<lots of binary gunk>" * 10,
    aDate = dt.datetime.now()
)
print(plistlib.dumps(pl).decode())
```

Parsing a plist:

```
import plistlib

plist = b"""<plist version="1.0">
<dict>
    <key>foo</key>
    <string>bar</string>
</dict>
</plist>"""
pl = plistlib.loads(plist)
print(pl["foo"])
```