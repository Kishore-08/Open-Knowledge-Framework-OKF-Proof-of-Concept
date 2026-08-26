---
id: apache-airflow-are-top-level-python-code-allowed-1ae4eb88
type: concept
title: Are top level Python code allowed?
description: While it is not recommended to write any code outside of defining Airflow
  constructs, Airflow does support any
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Are top level Python code allowed?

While it is not recommended to write any code outside of defining Airflow constructs, Airflow does support any
arbitrary python code as long as it does not break the Dag file processor or prolong file processing time past the
[dagbag\_import\_timeout](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-dagbag-import-timeout) value.

A common example is the violation of the time limit when building a dynamic Dag which usually requires querying data
from another service like a database. At the same time, the requested service is being swamped with Dag file
processors requests for data to process the file. These unintended interactions may cause the service to deteriorate
and eventually cause Dag file processing to fail.

Refer to [Dag writing best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#best-practice-writing-a-dag) for more information.