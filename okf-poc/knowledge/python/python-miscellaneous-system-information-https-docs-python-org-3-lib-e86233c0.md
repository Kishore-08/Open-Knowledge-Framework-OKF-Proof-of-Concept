---
id: python-miscellaneous-system-information-https-docs-python-org-3-lib-e86233c0
type: concept
title: Miscellaneous System Information[¶](https://docs.python.org/3/library/os.html#miscellaneous-system-information
  "Link to this heading")
description: os.confstr(*name*, */*)[¶](https://docs.python.org/3/library/os.html#os.confstr
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Miscellaneous System Information[¶](https://docs.python.org/3/library/os.html#miscellaneous-system-information "Link to this heading")

os.confstr(*name*, */*)[¶](https://docs.python.org/3/library/os.html#os.confstr "Link to this definition")
:   Return string-valued system configuration values. *name* specifies the
    configuration value to retrieve; it may be a string which is the name of a
    defined system value; these names are specified in a number of standards (POSIX,
    Unix 95, Unix 98, and others). Some platforms define additional names as well.
    The names known to the host operating system are given as the keys of the
    `confstr_names` dictionary. For configuration variables not included in that
    mapping, passing an integer for *name* is also accepted.

    If the configuration value specified by *name* isn’t defined, `None` is
    returned.

    If *name* is a string and is not known, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If a
    specific value for *name* is not supported by the host system, even if it is
    included in `confstr_names`, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with
    [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL") for the error number.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.confstr\_names[¶](https://docs.python.org/3/library/os.html#os.confstr_names "Link to this definition")
:   Dictionary mapping names accepted by [`confstr()`](https://docs.python.org/3/library/os.html#os.confstr "os.confstr") to the integer values
    defined for those names by the host operating system. This can be used to
    determine the set of names known to the system.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.cpu\_count()[¶](https://docs.python.org/3/library/os.html#os.cpu_count "Link to this definition")
:   Return the number of logical CPUs in the **system**. Returns `None` if
    undetermined.

    The [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") function can be used to get the number of
    logical CPUs usable by the calling thread of the **current process**.

    Added in version 3.4.

    Changed in version 3.13: If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set,
    `cpu_count()` returns the override value *n*.

os.getloadavg()[¶](https://docs.python.org/3/library/os.html#os.getloadavg "Link to this definition")
:   Return the number of processes in the system run queue averaged over the last
    1, 5, and 15 minutes or raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the load average was
    unobtainable.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.process\_cpu\_count()[¶](https://docs.python.org/3/library/os.html#os.process_cpu_count "Link to this definition")
:   Get the number of logical CPUs usable by the calling thread of the **current
    process**. Returns `None` if undetermined. It can be less than
    [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") depending on the CPU affinity.

    The [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") function can be used to get the number of logical CPUs
    in the **system**.

    If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set,
    `process_cpu_count()` returns the override value *n*.

    See also the [`sched_getaffinity()`](https://docs.python.org/3/library/os.html#os.sched_getaffinity "os.sched_