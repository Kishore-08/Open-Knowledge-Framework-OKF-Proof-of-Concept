---
id: python-netrc-objects-https-docs-python-org-3-library-netrc-html-net-76338711
type: concept
title: netrc Objects[¶](https://docs.python.org/3/library/netrc.html#netrc-objects
  "Link to this heading")
description: 'A [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc
  "netrc.netrc") instance has the following methods:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/netrc.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## netrc Objects[¶](https://docs.python.org/3/library/netrc.html#netrc-objects "Link to this heading")

A [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc") instance has the following methods:

netrc.authenticators(*host*)[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.authenticators "Link to this definition")
:   Return a 3-tuple `(login, account, password)` of authenticators for *host*.
    If the netrc file did not contain an entry for the given host, return the tuple
    associated with the ‘default’ entry. If neither matching host nor default entry
    is available, return `None`.

netrc.\_\_repr\_\_()[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.__repr__ "Link to this definition")
:   Dump the class data as a string in the format of a netrc file. (This discards
    comments and may reorder the entries.)

Instances of [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc") have public instance variables:

netrc.hosts[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.hosts "Link to this definition")
:   Dictionary mapping host names to `(login, account, password)` tuples. The
    ‘default’ entry, if any, is represented as a pseudo-host by that name.

netrc.macros[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.macros "Link to this definition")
:   Dictionary mapping macro names to string lists.