---
id: apache-airflow-timetables-8dafd1cd
type: concept
title: Timetables
description: Avoid using Airflow Variables/Connections or accessing Airflow database
  at the top level of your timetable code.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Timetables

Avoid using Airflow Variables/Connections or accessing Airflow database at the top level of your timetable code.
Database access should be delayed until the execution time of the Dag. This means that you should not have variables/connections retrieval
as argument to your timetable class initialization or have Variable/connection at the top level of your custom timetable module.

Bad example:

```
from airflow.sdk import Variable
from airflow.timetables.interval import CronDataIntervalTimetable


class CustomTimetable(CronDataIntervalTimetable):
    def __init__(self, *args, something=Variable.get("something"), **kwargs):
        self._something = something
        super().__init__(*args, **kwargs)
```

Good example:

```
from airflow.sdk import Variable
from airflow.timetables.interval import CronDataIntervalTimetable


class CustomTimetable(CronDataIntervalTimetable):
    def __init__(self, *args, something="something", **kwargs):
        self._something = Variable.get(something)
        super().__init__(*args, **kwargs)
```