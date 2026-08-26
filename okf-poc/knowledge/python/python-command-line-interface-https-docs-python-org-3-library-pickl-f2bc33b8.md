---
id: python-command-line-interface-https-docs-python-org-3-library-pickl-f2bc33b8
type: concept
title: Command-line interface[¶](https://docs.python.org/3/library/pickle.html#command-line-interface
  "Link to this heading")
description: The `pickle` module can be invoked as a script from the command line,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command-line interface[¶](https://docs.python.org/3/library/pickle.html#command-line-interface "Link to this heading")

The `pickle` module can be invoked as a script from the command line,
it will display contents of the pickle files. However, when the pickle file
that you want to examine comes from an untrusted source, `-m pickletools`
is a safer option because it does not execute pickle bytecode, see
[pickletools CLI usage](https://docs.python.org/3/library/pickletools.html#pickletools-cli).

```
python -m pickle pickle_file [pickle_file ...]
```

The following option is accepted:

pickle\_file[¶](https://docs.python.org/3/library/pickle.html#cmdoption-pickle-arg-pickle_file "Link to this definition")
:   A pickle file to read, or `-` to indicate reading from standard input.

See also

Module [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.")
:   Pickle interface constructor registration for extension types.

Module [`pickletools`](https://docs.python.org/3/library/pickletools.html#module-pickletools "pickletools: Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.")
:   Tools for working with and analyzing pickled data.

Module [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")
:   Indexed databases of objects; uses `pickle`.

Module [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
:   Shallow and deep object copying.

Module [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
:   High-performance serialization of built-in types.

Footnotes