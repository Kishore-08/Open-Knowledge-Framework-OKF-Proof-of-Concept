---
id: apache-airflow-bug-fixes-51425edb
type: concept
title: Bug Fixes
description: '- Gracefully handle whole config sections being renamed (#28008)'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Bug Fixes

- Gracefully handle whole config sections being renamed (#28008)
- Add allow list for imports during deserialization (#27887)
- Soft delete datasets that are no longer referenced in DAG schedules or task outlets (#27828)
- Redirect to home view when there are no valid tags in the URL (#25715)
- Refresh next run datasets info in dags view (#27839)
- Make MappedTaskGroup depend on its expand inputs (#27876)
- Make DagRun state updates for paused DAGs faster (#27725)
- Don’t explicitly set include\_examples to False on task run command (#27813)
- Fix menu border color (#27789)
- Fix backfill queued task getting reset to scheduled state. (#23720)
- Fix clearing child dag mapped tasks from parent dag (#27501)
- Handle json encoding of `V1Pod` in task callback (#27609)
- Fix ExternalTaskSensor can’t check zipped dag (#27056)
- Avoid re-fetching DAG run in TriggerDagRunOperator (#27635)
- Continue on exception when retrieving metadata (#27665)
- External task sensor fail fix (#27190)
- Add the default None when pop actions (#27537)
- Display parameter values from serialized dag in trigger dag view. (#27482, #27944)
- Move TriggerDagRun conf check to execute (#27035)
- Resolve trigger assignment race condition (#27072)
- Update google\_analytics.html (#27226)
- Fix some bug in web ui dags list page (auto-refresh & jump search null state) (#27141)
- Fixed broken URL for docker-compose.yaml (#26721)
- Fix xcom arg.py .zip bug (#26636)
- Fix 404 `taskInstance` errors and split into two tables (#26575)
- Fix browser warning of improper thread usage (#26551)
- template rendering issue fix (#26390)
- Clear `autoregistered` DAGs if there are any import errors (#26398)
- Fix `from airflow import version` lazy import (#26239)
- allow scroll in triggered dag runs modal (#27965)