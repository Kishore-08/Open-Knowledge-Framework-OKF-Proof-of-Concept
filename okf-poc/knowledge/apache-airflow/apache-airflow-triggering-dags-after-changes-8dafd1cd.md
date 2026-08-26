---
id: apache-airflow-triggering-dags-after-changes-8dafd1cd
type: concept
title: Triggering Dags after changes
description: Avoid triggering Dags immediately after changing them or any other accompanying
  files that you change in the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Triggering Dags after changes

Avoid triggering Dags immediately after changing them or any other accompanying files that you change in the
Dag folder.

You should give the system sufficient time to process the changed files. This takes several steps.
First the files have to be distributed to scheduler - usually via distributed filesystem or Git-Sync, then
scheduler has to parse the Python files and store them in the database. Depending on your configuration,
speed of your distributed filesystem, number of files, number of Dags, number of changes in the files,
sizes of the files, number of schedulers, speed of CPUS, this can take from seconds to minutes, in extreme
cases many minutes. You should wait for your Dag to appear in the UI to be able to trigger it.

In case you see long delays between updating it and the time it is ready to be triggered, you can look
at the following configuration parameters and fine tune them according your needs (see details of
each parameter by following the links):

- [scheduler\_idle\_sleep\_time](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-scheduler-scheduler-idle-sleep-time)
- [min\_file\_process\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-min-file-process-interval)
- [refresh\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-refresh-interval)
- [parsing\_processes](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-parsing-processes)
- [file\_parsing\_sort\_mode](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-file-parsing-sort-mode)