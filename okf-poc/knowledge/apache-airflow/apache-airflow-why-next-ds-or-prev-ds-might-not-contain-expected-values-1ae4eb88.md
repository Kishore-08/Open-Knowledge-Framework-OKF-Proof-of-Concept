---
id: apache-airflow-why-next-ds-or-prev-ds-might-not-contain-expected-values-1ae4eb88
type: concept
title: Why `next_ds` or `prev_ds` might not contain expected values?
description: '- When scheduling Dag, the `next_ds` `next_ds_nodash` `prev_ds` `prev_ds_nodash`
  are calculated using'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Why `next_ds` or `prev_ds` might not contain expected values?

- When scheduling Dag, the `next_ds` `next_ds_nodash` `prev_ds` `prev_ds_nodash` are calculated using
  `logical_date` and the Dag’s schedule (if applicable). If you set `schedule` as `None` or `@once`,
  the `next_ds`, `next_ds_nodash`, `prev_ds`, `prev_ds_nodash` values will be set to `None`.
- When manually triggering Dag, the schedule will be ignored, and `prev_ds == next_ds == ds`.

## Task execution interactions