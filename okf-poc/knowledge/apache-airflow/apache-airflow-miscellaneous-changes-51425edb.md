---
id: apache-airflow-miscellaneous-changes-51425edb
type: concept
title: Miscellaneous Changes
description: Maximum retry task delay is set to be 24h (86400s) by default. You can
  change it globally via `core.max_task_retry_delay`
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Miscellaneous Changes

#### Handle OverflowError on exponential backoff in next\_run\_calculation (#28172)

Maximum retry task delay is set to be 24h (86400s) by default. You can change it globally via `core.max_task_retry_delay`
parameter.

#### Move Hive macros to the provider (#28538)

The Hive Macros (`hive.max_partition`, `hive.closest_ds_partition`) are available only when Hive Provider is
installed. Please install Hive Provider > 5.1.0 when using those macros.

#### Updated app to support configuring the caching hash method for FIPS v2 (#30675)

Various updates for FIPS-compliance when running Airflow in Python 3.9+. This includes a new webserver option, `caching_hash_method`,
for changing the default flask caching method.