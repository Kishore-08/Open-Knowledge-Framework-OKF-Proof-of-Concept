---
id: python-pickle-serialization-https-docs-python-org-3-library-zoneinf-a734111f
type: concept
title: Pickle serialization[¶](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization
  "Link to this heading")
description: Rather than serializing all transition data, `ZoneInfo` objects are
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Pickle serialization[¶](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization "Link to this heading")

Rather than serializing all transition data, `ZoneInfo` objects are
serialized by key, and `ZoneInfo` objects constructed from files (even those
with a value for `key` specified) cannot be pickled.

The behavior of a `ZoneInfo` file depends on how it was constructed:

1. `ZoneInfo(key)`: When constructed with the primary constructor, a
   `ZoneInfo` object is serialized by key, and when deserialized, the
   deserializing process uses the primary and thus it is expected that these
   are the same object as other references to the same time
   zone. For example, if `europe_berlin_pkl` is a string containing a pickle
   constructed from `ZoneInfo("Europe/Berlin")`, one would expect the
   following behavior:

   ```
   >>> a = ZoneInfo("Europe/Berlin")
   >>> b = pickle.loads(europe_berlin_pkl)
   >>> a is b
   True
   ```
2. `ZoneInfo.no_cache(key)`: When constructed from the cache-bypassing
   constructor, the `ZoneInfo` object is also serialized by key, but when
   deserialized, the deserializing process uses the cache bypassing
   constructor. If `europe_berlin_pkl_nc` is a string containing a pickle
   constructed from `ZoneInfo.no_cache("Europe/Berlin")`, one would expect
   the following behavior:

   ```
   >>> a = ZoneInfo("Europe/Berlin")
   >>> b = pickle.loads(europe_berlin_pkl_nc)
   >>> a is b
   False
   ```
3. `ZoneInfo.from_file(file_obj, /, key=None)`: When constructed from a file, the
   `ZoneInfo` object raises an exception on pickling. If an end user wants to
   pickle a `ZoneInfo` constructed from a file, it is recommended that they
   use a wrapper type or a custom serialization function: either serializing by
   key or storing the contents of the file object and serializing that.

This method of serialization requires that the time zone data for the required
key be available on both the serializing and deserializing side, similar to the
way that references to classes and functions are expected to exist in both the
serializing and deserializing environments. It also means that no guarantees
are made about the consistency of results when unpickling a `ZoneInfo`
pickled in an environment with a different version of the time zone data.