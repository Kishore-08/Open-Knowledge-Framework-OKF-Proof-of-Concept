---
id: python-cross-platform-https-docs-python-org-3-library-platform-html-8418a7a3
type: concept
title: Cross platform[¶](https://docs.python.org/3/library/platform.html#cross-platform
  "Link to this heading")
description: platform.architecture(*executable=sys.executable*, *bits=''*, *linkage=''*)[¶](https://docs.python.org/3/library/platform.html#platform.architecture
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Cross platform[¶](https://docs.python.org/3/library/platform.html#cross-platform "Link to this heading")

platform.architecture(*executable=sys.executable*, *bits=''*, *linkage=''*)[¶](https://docs.python.org/3/library/platform.html#platform.architecture "Link to this definition")
:   Queries the given executable (defaults to the Python interpreter binary) for
    various architecture information.

    Returns a tuple `(bits, linkage)` which contain information about the bit
    architecture and the linkage format used for the executable. Both values are
    returned as strings.

    Values that cannot be determined are returned as given by the parameter presets.
    If bits is given as `''`, the `sizeof(pointer)` (or
    `sizeof(long)` on Python version < 1.5.2) is used as indicator for the
    supported pointer size.

    The function relies on the system’s `file` command to do the actual work.
    This is available on most if not all Unix platforms and some non-Unix platforms
    and then only if the executable points to the Python interpreter. Reasonable
    defaults are used when the above needs are not met.

    Note

    On macOS (and perhaps other platforms), executable files may be
    universal files containing multiple architectures.

    To get at the “64-bitness” of the current interpreter, it is more
    reliable to query the [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize") attribute:

    ```
    is_64bits = sys.maxsize > 2**32
    ```

platform.machine()[¶](https://docs.python.org/3/library/platform.html#platform.machine "Link to this definition")
:   Returns the machine type, e.g. `'AMD64'`. An empty string is returned if the
    value cannot be determined.

    The output is platform-dependent and may differ in casing and naming conventions.

platform.node()[¶](https://docs.python.org/3/library/platform.html#platform.node "Link to this definition")
:   Returns the computer’s network name (may not be fully qualified!). An empty
    string is returned if the value cannot be determined.

platform.platform(*aliased=False*, *terse=False*)[¶](https://docs.python.org/3/library/platform.html#platform.platform "Link to this definition")
:   Returns a single string identifying the underlying platform with as much useful
    information as possible.

    The output is intended to be *human readable* rather than machine parseable. It
    may look different on different platforms and this is intended.

    If *aliased* is true, the function will use aliases for various platforms that
    report system names which differ from their common names, for example SunOS will
    be reported as Solaris. The [`system_alias()`](https://docs.python.org/3/library/platform.html#platform.system_alias "platform.system_alias") function is used to implement
    this.

    Setting *terse* to true causes the function to return only the absolute minimum
    information needed to identify the platform.

    Changed in version 3.8: On macOS, the function now uses [`mac_ver()`](https://docs.python.org/3/library/platform.html#platform.mac_ver "platform.mac_ver"), if it returns a
    non-empty release string, to get the macOS version rather than the darwin
    version.

platform.processor()[¶](https://docs.python.org/3/library/platform.html#platform.processor "Link to this definition")
:   Returns the (real) processor name, e.g. `'amdk6'`.

    An empty string is returned if the value cannot be determined. Note that many
    platforms do not provide this information or simply return the same value as for
    [`machine()`](https://docs.python.org/3/library/platform.html#platform.machine "platform.machine"). NetBSD does this.

platform.python\_build()[¶](https://docs.python.org/3/library/platform.html#platform.python_build "Link to this definition")
:   Returns a tuple `(buildno, builddate)` stating the Python build number and
    date as strings.

platform.python\_compiler()[¶](https://docs.python.org/3/libra