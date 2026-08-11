---
id: python-junk-definition-functions-https-docs-python-org-3-library-di-b041ceae
type: concept
title: Junk definition functions[¶](https://docs.python.org/3/library/difflib.html#junk-definition-functions
  "Link to this heading")
description: difflib.IS\_LINE\_JUNK(*line*)[¶](https://docs.python.org/3/library/difflib.html#difflib.IS_LINE_JUNK
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/difflib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Junk definition functions[¶](https://docs.python.org/3/library/difflib.html#junk-definition-functions "Link to this heading")

difflib.IS\_LINE\_JUNK(*line*)[¶](https://docs.python.org/3/library/difflib.html#difflib.IS_LINE_JUNK "Link to this definition")
:   Return `True` for ignorable lines. The line *line* is ignorable if *line* is
    blank or contains a single `'#'`, otherwise it is not ignorable. Used as a
    default for parameter *linejunk* in [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff") in older versions.

difflib.IS\_CHARACTER\_JUNK(*ch*)[¶](https://docs.python.org/3/library/difflib.html#difflib.IS_CHARACTER_JUNK "Link to this definition")
:   Return `True` for ignorable characters. The character *ch* is ignorable if *ch*
    is a space or tab, otherwise it is not ignorable. Used as a default for
    parameter *charjunk* in [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff").