---
id: python-command-line-options-https-docs-python-org-3-library-tarfile-47076c99
type: concept
title: Command-line options[¶](https://docs.python.org/3/library/tarfile.html#command-line-options
  "Link to this heading")
description: -l <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Command-line options[¶](https://docs.python.org/3/library/tarfile.html#command-line-options "Link to this heading")

-l <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l "Link to this definition")

--list <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-list "Link to this definition")
:   List files in a tarfile.

-c <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c "Link to this definition")

--create <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-create "Link to this definition")
:   Create tarfile from source files.

-e <tarfile> [<output\_dir>][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e "Link to this definition")

--extract <tarfile> [<output\_dir>][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-extract "Link to this definition")
:   Extract tarfile into the current directory if *output\_dir* is not specified.

-t <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-t "Link to this definition")

--test <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-test "Link to this definition")
:   Test whether the tarfile is valid or not.

-v, --verbose[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-v "Link to this definition")
:   Verbose output.

--filter <filtername>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-filter "Link to this definition")
:   Specifies the *filter* for `--extract`.
    See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details.
    Only string names are accepted (that is, `fully_trusted`, `tar`,
    and `data`).

## Examples[¶](https://docs.python.org/3/library/tarfile.html#examples "Link to this heading")