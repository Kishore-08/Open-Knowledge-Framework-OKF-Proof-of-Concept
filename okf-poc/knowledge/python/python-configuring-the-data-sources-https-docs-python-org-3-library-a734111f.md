---
id: python-configuring-the-data-sources-https-docs-python-org-3-library-a734111f
type: concept
title: Configuring the data sources[¶](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources
  "Link to this heading")
description: When `ZoneInfo(key)` is called, the constructor first searches the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Configuring the data sources[¶](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources "Link to this heading")

When `ZoneInfo(key)` is called, the constructor first searches the
directories specified in [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") for a file matching `key`, and on
failure looks for a match in the tzdata package. This behavior can be
configured in three ways:

1. The default [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") when not otherwise specified can be configured at
   [compile time](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-compile-time-config).
2. [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") can be configured using [an environment variable](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-environment-var).
3. At [runtime](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-runtime-config), the search path can be
   manipulated using the [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") function.

#### Compile-time configuration[¶](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration "Link to this heading")

The default [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") includes several common deployment locations for the
time zone database (except on Windows, where there are no “well-known”
locations for time zone data). On POSIX systems, downstream distributors and
those building Python from source who know where their system
time zone data is deployed may change the default time zone path by specifying
the compile-time option `TZPATH` (or, more likely, the [`configure
flag --with-tzpath`](https://docs.python.org/3/using/configure.html#cmdoption-with-tzpath)), which should be a string delimited by
[`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep").

On all platforms, the configured value is available as the `TZPATH` key in
[`sysconfig.get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var").

#### Environment configuration[¶](https://docs.python.org/3/library/zoneinfo.html#environment-configuration "Link to this heading")

When initializing [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") (either at import time or whenever
[`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") is called with no arguments), the `zoneinfo` module will
use the environment variable `PYTHONTZPATH`, if it exists, to set the search
path.

PYTHONTZPATH[¶](https://docs.python.org/3/library/zoneinfo.html#envvar-PYTHONTZPATH "Link to this definition")
:   This is an [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")-separated string containing the time zone
    search path to use. It must consist of only absolute rather than relative
    paths. Relative components specified in `PYTHONTZPATH` will not be used,
    but otherwise the behavior when a relative path is specified is
    implementation-defined; CPython will raise [`InvalidTZPathWarning`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.InvalidTZPathWarning "zoneinfo.InvalidTZPathWarning"), but
    other implementations are free to silently ignore the erroneous component
    or raise an exception.

To set the system to ignore the system data and use the tzdata package
instead, set `PYTHONTZPATH=""`.

#### Runtime configuration[¶](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration "Link to this heading")

The TZ search path can also be configured at runtime using the
[`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") functi