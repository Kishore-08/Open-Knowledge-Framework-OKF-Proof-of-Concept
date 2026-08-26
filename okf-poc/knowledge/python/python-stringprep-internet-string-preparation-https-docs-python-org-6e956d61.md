---
id: python-stringprep-internet-string-preparation-https-docs-python-org-6e956d61
type: concept
title: '`stringprep` — Internet String Preparation[¶](https://docs.python.org/3/library/'
description: '**Source code:** [Lib/stringprep.py](https://github.com/python/cpython/tree/3.14/Lib/stringprep.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stringprep.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `stringprep` — Internet String Preparation[¶](https://docs.python.org/3/library/stringprep.html#module-stringprep "Link to this heading")

**Source code:** [Lib/stringprep.py](https://github.com/python/cpython/tree/3.14/Lib/stringprep.py)

---

When identifying things (such as host names) in the internet, it is often
necessary to compare such identifications for “equality”. Exactly how this
comparison is executed may depend on the application domain, e.g. whether it
should be case-insensitive or not. It may be also necessary to restrict the
possible identifications, to allow only identifications consisting of
“printable” characters.

[**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html) defines a procedure for “preparing” Unicode strings in internet
protocols. Before passing strings onto the wire, they are processed with the
preparation procedure, after which they have a certain normalized form. The RFC
defines a set of tables, which can be combined into profiles. Each profile must
define which tables it uses, and what other optional parts of the `stringprep`
procedure are part of the profile. One example of a `stringprep` profile is
`nameprep`, which is used for internationalized domain names.

The module `stringprep` only exposes the tables from [**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html). As these
tables would be very large to represent as dictionaries or lists, the
module uses the Unicode character database internally. The module source code
itself was generated using the `mkstringprep.py` utility.

As a result, these tables are exposed as functions, not as data structures.
There are two kinds of tables in the RFC: sets and mappings. For a set,
`stringprep` provides the “characteristic function”, i.e. a function that
returns `True` if the parameter is part of the set. For mappings, it provides the
mapping function: given the key, it returns the associated value. Below is a
list of all functions available in the module.

stringprep.in\_table\_a1(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_a1 "Link to this definition")
:   Determine whether *code* is in tableA.1 (Unassigned code points in Unicode 3.2).

stringprep.in\_table\_b1(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_b1 "Link to this definition")
:   Determine whether *code* is in tableB.1 (Commonly mapped to nothing).

stringprep.map\_table\_b2(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b2 "Link to this definition")
:   Return the mapped value for *code* according to tableB.2 (Mapping for
    case-folding used with NFKC).

stringprep.map\_table\_b3(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b3 "Link to this definition")
:   Return the mapped value for *code* according to tableB.3 (Mapping for
    case-folding used with no normalization).

stringprep.in\_table\_c11(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11 "Link to this definition")
:   Determine whether *code* is in tableC.1.1 (ASCII space characters).

stringprep.in\_table\_c12(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c12 "Link to this definition")
:   Determine whether *code* is in tableC.1.2 (Non-ASCII space characters).

stringprep.in\_table\_c11\_c12(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11_c12 "Link to this definition")
:   Determine whether *code* is in tableC.1 (Space characters, union of C.1.1 and
    C.1.2).

stringprep.in\_table\_c21(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c21 "Link to this definition")
:   Determine whether *code* is in tableC.2.1 (ASCII control characters).

stringprep.in\_table\_c22(*code*)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c22 "Link to this definition")
:   Determine whether *code* is in tableC.2.2