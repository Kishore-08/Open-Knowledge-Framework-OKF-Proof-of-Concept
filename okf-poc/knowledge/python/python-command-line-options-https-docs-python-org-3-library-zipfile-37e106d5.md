---
id: python-command-line-options-https-docs-python-org-3-library-zipfile-37e106d5
type: concept
title: Command-line options[¶](https://docs.python.org/3/library/zipfile.html#command-line-options
  "Link to this heading")
description: -l <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zipfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Command-line options[¶](https://docs.python.org/3/library/zipfile.html#command-line-options "Link to this heading")

-l <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l "Link to this definition")

--list <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-list "Link to this definition")
:   List files in a zipfile.

-c <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c "Link to this definition")

--create <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-create "Link to this definition")
:   Create zipfile from source files.

-e <zipfile> <output\_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e "Link to this definition")

--extract <zipfile> <output\_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-extract "Link to this definition")
:   Extract zipfile into target directory.

-t <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t "Link to this definition")

--test <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-test "Link to this definition")
:   Test whether the zipfile is valid or not.

--metadata-encoding <encoding>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-metadata-encoding "Link to this definition")
:   Specify encoding of member names for [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l), [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e) and
    [`-t`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t).

    Added in version 3.11.