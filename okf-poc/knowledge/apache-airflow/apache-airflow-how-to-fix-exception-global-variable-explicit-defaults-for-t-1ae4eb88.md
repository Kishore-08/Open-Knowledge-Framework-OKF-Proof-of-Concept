---
id: apache-airflow-how-to-fix-exception-global-variable-explicit-defaults-for-t-1ae4eb88
type: concept
title: 'How to fix Exception: Global variable `explicit_defaults_for_timestamp` needs
  to be on (1)?'
description: 'This means `explicit_defaults_for_timestamp` is disabled in your mysql
  server and you need to enable it by:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to fix Exception: Global variable `explicit_defaults_for_timestamp` needs to be on (1)?

This means `explicit_defaults_for_timestamp` is disabled in your mysql server and you need to enable it by:

1. Set `explicit_defaults_for_timestamp = 1` under the `mysqld` section in your `my.cnf` file.
2. Restart the Mysql server.

## Connections