---
id: apache-airflow-exception-matching-dda6bf43
type: concept
title: Exception matching
description: Exception types can be specified as Python classes or dotted import path
  strings
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Exception matching

Exception types can be specified as Python classes or dotted import path strings
(e.g. `"requests.exceptions.HTTPError"`). String paths are validated at DAG parse
time – a path without a dot raises `ValueError` immediately, and unresolvable paths
produce a warning.

By default, rules use `isinstance` matching, so a rule for `OSError` also matches
`ConnectionError` (a subclass). Set `match_subclasses=False` for exact type matching:

```
RetryRule(exception=OSError, match_subclasses=False)  # only OSError, not subclasses
```