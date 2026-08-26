---
id: apache-airflow-how-to-control-dag-file-parsing-timeout-for-different-dag-fi-1ae4eb88
type: concept
title: How to control Dag file parsing timeout for different Dag files?
description: (only valid for Airflow >= 2.3.0)
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to control Dag file parsing timeout for different Dag files?

(only valid for Airflow >= 2.3.0)

You can add a `get_dagbag_import_timeout` function in your `airflow_local_settings.py` which gets
called right before a Dag file is parsed. You can return different timeout value based on the Dag file.
When the return value is less than or equal to 0, it means no timeout during the Dag parsing.

airflow\_local\_settings.py

```
 def get_dagbag_import_timeout(dag_file_path: str) -> Union[int, float]:
     """
     This setting allows to dynamically control the Dag file parsing timeout.

     It is useful when there are a few Dag files requiring longer parsing times, while others do not.
     You can control them separately instead of having one value for all Dag files.

     If the return value is less than or equal to 0, it means no timeout during the Dag parsing.
     """
     if "slow" in dag_file_path:
         return 90
     if "no-timeout" in dag_file_path:
         return 0
     return conf.getfloat("core", "DAGBAG_IMPORT_TIMEOUT")
```

See [Configuring local settings](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html#set-config-configuring-local-settings) for details on how to
configure local settings.