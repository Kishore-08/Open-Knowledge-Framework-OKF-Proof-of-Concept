---
id: apache-airflow-improvement-changes-51425edb
type: concept
title: Improvement Changes
description: The configurations view now only displays the running configuration.
  Previously, the default configuration
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Improvement Changes

#### Display only the running configuration in configurations view (#28892)

The configurations view now only displays the running configuration. Previously, the default configuration
was displayed at the top but it was not obvious whether this default configuration was overridden or not.
Subsequently, the non-documented endpoint `/configuration?raw=true` is deprecated and will be removed in
Airflow 3.0. The HTTP response now returns an additional `Deprecation` header. The `/config` endpoint on
the REST API is the standard way to fetch Airflow configuration programmatically.

#### Explicit skipped states list for ExternalTaskSensor (#29933)

ExternalTaskSensor now has an explicit `skipped_states` list