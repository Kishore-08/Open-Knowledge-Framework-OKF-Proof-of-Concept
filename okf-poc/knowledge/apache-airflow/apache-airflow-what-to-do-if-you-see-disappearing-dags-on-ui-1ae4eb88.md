---
id: apache-airflow-what-to-do-if-you-see-disappearing-dags-on-ui-1ae4eb88
type: concept
title: What to do if you see disappearing Dags on UI?
description: 'There are several reasons why Dags might disappear from the UI. Common
  causes include:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### What to do if you see disappearing Dags on UI?

There are several reasons why Dags might disappear from the UI. Common causes include:

- **Total parsing of all Dags is too long** - If parsing takes longer than [dagbag\_import\_timeout](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-dagbag-import-timeout),
  files may not be processed completely. This often occurs when Dags don’t follow
  [Dag writing best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#best-practice-writing-a-dag) like:

  - Excessive top-level code execution
  - External system calls during parsing
  - Complex dynamic Dag generation
- **Inconsistent dynamic Dag generation** - Dags created through
  [dynamic generation](https://airflow.apache.org/docs/apache-airflow/stable/howto/dynamic-dag-generation.html) must produce stable Dag IDs across parses.
  Verify consistency by running `python your_dag_file.py` repeatedly.
- **File processing configuration issues** - A certain combination of parameters may lead to scenarios which certain Dags are less likely to be processed at each loop. Check these parameters:

  - [file\_parsing\_sort\_mode](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-file-parsing-sort-mode) - Ensure sorting method matches your sync strategy
  - [parsing\_processes](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-parsing-processes) - Number of parallel parsers
  - [parsing\_cleanup\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-scheduler-parsing-cleanup-interval) - Controls stale Dag cleanup frequency
- **File synchronization problems** - Common with git-sync setups:

  - Symbolic link swapping delays
  - Permission changes during sync
  - `mtime` preservation issues
- **Time synchronization issues** - Ensure all nodes (database, schedulers, workers) use NTP with <1s clock drift.