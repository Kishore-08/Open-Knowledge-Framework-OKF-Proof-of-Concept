---
id: python-the-zoneinfo-class-https-docs-python-org-3-library-zoneinfo--a734111f
type: concept
title: The `ZoneInfo` class[¶](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class
  "Link to this heading")
description: '*class* zoneinfo.ZoneInfo(*key*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## The `ZoneInfo` class[¶](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class "Link to this heading")

*class* zoneinfo.ZoneInfo(*key*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "Link to this definition")
:   A concrete [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass that represents an IANA time
    zone specified by the string `key`. Calls to the primary constructor will
    always return objects that compare identically; put another way, barring
    cache invalidation via [`ZoneInfo.clear_cache()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.clear_cache "zoneinfo.ZoneInfo.clear_cache"), for all values of
    `key`, the following assertion will always be true:

    ```
    a = ZoneInfo(key)
    b = ZoneInfo(key)
    assert a is b
    ```

    `key` must be in the form of a relative, normalized POSIX path, with no
    up-level references. The constructor will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if a
    non-conforming key is passed.

    If no file matching `key` is found, the constructor will raise
    [`ZoneInfoNotFoundError`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "zoneinfo.ZoneInfoNotFoundError").

The `ZoneInfo` class has two alternate constructors:

*classmethod* ZoneInfo.from\_file(*file\_obj*, */*, *key=None*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.from_file "Link to this definition")
:   Constructs a `ZoneInfo` object from a file-like object returning bytes
    (e.g. a file opened in binary mode or an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object).
    Unlike the primary constructor, this always constructs a new object.

    The `key` parameter sets the name of the zone for the purposes of
    [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__").

    Objects created via this constructor cannot be pickled (see [pickling](https://docs.python.org/3/library/zoneinfo.html#pickling)).

    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the data read from *file\_obj* is not a valid
    TZif file.

*classmethod* ZoneInfo.no\_cache(*key*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.no_cache "Link to this definition")
:   An alternate constructor that bypasses the constructor’s cache. It is
    identical to the primary constructor, but returns a new object on each
    call. This is most likely to be useful for testing or demonstration
    purposes, but it can also be used to create a system with a different cache
    invalidation strategy.

    Objects created via this constructor will also bypass the cache of a
    deserializing process when unpickled.

    Caution

    Using this constructor may change the semantics of your datetimes in
    surprising ways, only use it if you know that you need to.

The following class methods are also available:

*classmethod* ZoneInfo.clear\_cache(*\**, *only\_keys=None*)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.clear_cache "Link to this definition")
:   A method for invalidating the cache on the `ZoneInfo` class. If no
    arguments are passed, all caches are invalidated and the next call to
    the primary constructor for each key will return a new instance.

    If an iterable of key names is passed to the `only_keys` parameter, only
    the specified keys will be removed from the cache. Keys passed to
    `only_keys` but not found in the cache are ignored.

    Warning

    Invoking this function may change the semantics of datetimes using
    `ZoneInfo` in surprising ways; this modifies module state
    and thus may have wide-ranging