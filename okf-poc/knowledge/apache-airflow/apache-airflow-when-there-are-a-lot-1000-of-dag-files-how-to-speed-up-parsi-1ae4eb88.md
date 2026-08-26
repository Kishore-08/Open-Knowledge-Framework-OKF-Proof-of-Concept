---
id: apache-airflow-when-there-are-a-lot-1000-of-dag-files-how-to-speed-up-parsi-1ae4eb88
type: concept
title: When there are a lot (>1000) of Dag files, how to speed up parsing of new files?
description: Change the [file\_parsing\_sort\_mode](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-file-parsing-sort-mode)
  to `modified_time`, raise
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### When there are a lot (>1000) of Dag files, how to speed up parsing of new files?

Change the [file\_parsing\_sort\_mode](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-file-parsing-sort-mode) to `modified_time`, raise
the [min\_file\_process\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-min-file-process-interval) to `600` (10 minutes), `6000` (100 minutes)
or a higher value.

The Dag parser will skip the `min_file_process_interval` check if a file is recently modified.

This might not work for case where the Dag is imported/created from a separate file. Example:
`dag_file.py` that imports `dag_loader.py` where the actual logic of the Dag file is as shown below.
In this case if `dag_loader.py` is updated but `dag_file.py` is not updated, the changes won’t be reflected
until `min_file_process_interval` is reached since Dag Parser will look for modified time for `dag_file.py` file.

dag\_file.py

```
 from dag_loader import create_dag

 globals()[dag.dag_id] = create_dag(dag_id, schedule, dag_number, default_args)
```

dag\_loader.py

```
 from airflow.sdk import DAG
 from airflow.sdk import task

 import pendulum


 def create_dag(dag_id, schedule, dag_number, default_args):
     dag = DAG(
         dag_id,
         schedule=schedule,
         default_args=default_args,
         pendulum.datetime(2021, 9, 13, tz="UTC"),
     )

     with dag:

         @task()
         def hello_world():
             print("Hello World")
             print(f"This is Dag: {dag_number}")

         hello_world()

     return dag
```