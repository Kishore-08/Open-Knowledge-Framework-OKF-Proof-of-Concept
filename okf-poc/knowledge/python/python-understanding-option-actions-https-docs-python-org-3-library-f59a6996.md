---
id: python-understanding-option-actions-https-docs-python-org-3-library-f59a6996
type: concept
title: Understanding option actions[¶](https://docs.python.org/3/library/optparse.html#understanding-option-actions
  "Link to this heading")
description: Actions tell `optparse` what to do when it encounters an option on the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Understanding option actions[¶](https://docs.python.org/3/library/optparse.html#understanding-option-actions "Link to this heading")

Actions tell `optparse` what to do when it encounters an option on the
command line. There is a fixed set of actions hard-coded into `optparse`;
adding new actions is an advanced topic covered in section
[Extending optparse](https://docs.python.org/3/library/optparse.html#optparse-extending-optparse). Most actions tell `optparse` to store
a value in some variable—for example, take a string from the command line and
store it in an attribute of `options`.

If you don’t specify an option action, `optparse` defaults to `store`.