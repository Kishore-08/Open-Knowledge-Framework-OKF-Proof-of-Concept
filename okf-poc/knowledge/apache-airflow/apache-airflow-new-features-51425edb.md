---
id: apache-airflow-new-features-51425edb
type: concept
title: New Features
description: '- `TaskRunner`: notify of component start and finish (#27855)'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### New Features

- `TaskRunner`: notify of component start and finish (#27855)
- Add DagRun state change to the Listener plugin system(#27113)
- Metric for raw task return codes (#27155)
- Add logic for XComArg to pull specific map indexes (#27771)
- Clear TaskGroup (#26658, #28003)
- Add critical section query duration metric (#27700)
- Add: #23880 :: Audit log for `AirflowModelViews(Variables/Connection)` (#24079, #27994, #27923)
- Add postgres 15 support (#27444)
- Expand tasks in mapped group at run time (#27491)
- reset commits, clean submodules (#27560)
- scheduler\_job, add metric for scheduler loop timer (#27605)
- Allow datasets to be used in taskflow (#27540)
- Add expanded\_ti\_count to ti context (#27680)
- Add user comment to task instance and dag run (#26457, #27849, #27867)
- Enable copying DagRun JSON to clipboard (#27639)
- Implement extra controls for SLAs (#27557)
- add dag parsed time in DAG view (#27573)
- Add max\_wait for exponential\_backoff in BaseSensor (#27597)
- Expand tasks in mapped group at parse time (#27158)
- Add disable retry flag on backfill (#23829)
- Adding sensor decorator (#22562)
- Api endpoint update ti (#26165)
- Filtering datasets by recent update events (#26942)
- Support `Is /not` Null filter for value is None on `webui` (#26584)
- Add search to datasets list (#26893)
- Split out and handle ‘params’ in mapped operator (#26100)
- Add authoring API for TaskGroup mapping (#26844)
- Add `one_done` trigger rule (#26146)
- Create a more efficient airflow dag test command that also has better local logging (#26400)
- Support add/remove permissions to roles commands (#26338)
- Auto tail file logs in Web UI (#26169)
- Add triggerer info to task instance in API (#26249)
- Flag to deserialize value on custom XCom backend (#26343)