---
id: python-exceptions-https-docs-python-org-3-library-ctypes-html-excep-07786b1c
type: concept
title: Exceptions[¶](https://docs.python.org/3/library/ctypes.html#exceptions "Link
  to this heading")
description: '*exception* ctypes.ArgumentError[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ArgumentError
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Exceptions[¶](https://docs.python.org/3/library/ctypes.html#exceptions "Link to this heading")

*exception* ctypes.ArgumentError[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ArgumentError "Link to this definition")
:   This exception is raised when a foreign function call cannot convert one of the
    passed arguments.

*exception* ctypes.COMError(*hresult*, *text*, *details*)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "Link to this definition")
:   This exception is raised when a COM method call failed.

    hresult[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.hresult "Link to this definition")
    :   The integer value representing the error code.

    text[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.text "Link to this definition")
    :   The error message.

    details[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.details "Link to this definition")
    :   The 5-tuple `(descr, source, helpfile, helpcontext, progid)`.

        *descr* is the textual description. *source* is the language-dependent
        `ProgID` for the class or application that raised the error. *helpfile*
        is the path of the help file. *helpcontext* is the help context
        identifier. *progid* is the `ProgID` of the interface that defined the
        error.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Windows

    Added in version 3.14.