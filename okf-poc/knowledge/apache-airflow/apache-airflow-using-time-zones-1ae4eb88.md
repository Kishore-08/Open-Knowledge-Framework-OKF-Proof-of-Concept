---
id: apache-airflow-using-time-zones-1ae4eb88
type: concept
title: Using time zones
description: Creating a time zone aware datetime (e.g. Dag’s `start_date`) is quite
  simple. Just make sure to supply
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using time zones

Creating a time zone aware datetime (e.g. Dag’s `start_date`) is quite simple. Just make sure to supply
a time zone aware dates using `pendulum`. Don’t try to use standard library
[timezone](https://docs.python.org/3/library/datetime.html#timezone-objects) as they are known to
have limitations and we deliberately disallow using them in Dags.