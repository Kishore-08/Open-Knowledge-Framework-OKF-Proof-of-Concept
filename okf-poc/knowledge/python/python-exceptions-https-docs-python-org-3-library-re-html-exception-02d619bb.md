---
id: python-exceptions-https-docs-python-org-3-library-re-html-exception-02d619bb
type: concept
title: Exceptions[¶](https://docs.python.org/3/library/re.html#exceptions "Link to
  this heading")
description: '*exception* re.PatternError(*msg*, *pattern=None*, *pos=None*)[¶](https://docs.python.org/3/library/re.html#re.PatternError
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Exceptions[¶](https://docs.python.org/3/library/re.html#exceptions "Link to this heading")

*exception* re.PatternError(*msg*, *pattern=None*, *pos=None*)[¶](https://docs.python.org/3/library/re.html#re.PatternError "Link to this definition")
:   Exception raised when a string passed to one of the functions here is not a
    valid regular expression (for example, it might contain unmatched parentheses)
    or when some other error occurs during compilation or matching. It is never an
    error if a string contains no match for a pattern. The `PatternError` instance has
    the following additional attributes:

    msg[¶](https://docs.python.org/3/library/re.html#re.PatternError.msg "Link to this definition")
    :   The unformatted error message.

    pattern[¶](https://docs.python.org/3/library/re.html#re.PatternError.pattern "Link to this definition")
    :   The regular expression pattern.

    pos[¶](https://docs.python.org/3/library/re.html#re.PatternError.pos "Link to this definition")
    :   The index in *pattern* where compilation failed (may be `None`).

    lineno[¶](https://docs.python.org/3/library/re.html#re.PatternError.lineno "Link to this definition")
    :   The line corresponding to *pos* (may be `None`).

    colno[¶](https://docs.python.org/3/library/re.html#re.PatternError.colno "Link to this definition")
    :   The column corresponding to *pos* (may be `None`).

    Changed in version 3.5: Added additional attributes.

    Changed in version 3.13: `PatternError` was originally named `error`; the latter is kept as an alias for
    backward compatibility.