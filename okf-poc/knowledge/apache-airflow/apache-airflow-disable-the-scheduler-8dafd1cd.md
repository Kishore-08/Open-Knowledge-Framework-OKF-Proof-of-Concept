---
id: apache-airflow-disable-the-scheduler-8dafd1cd
type: concept
title: Disable the scheduler
description: You might consider disabling the Airflow cluster while you perform such
  maintenance.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Disable the scheduler

You might consider disabling the Airflow cluster while you perform such maintenance.

One way to do so would be to set the param `[scheduler] > use_job_schedule` to `False` and wait for any running Dags to complete; after this no new Dag runs will be created unless externally triggered.

A *better* way (though it’s a bit more manual) is to use the `dags pause` command. You’ll need to keep track of the Dags that are paused before you begin this operation so that you know which ones to unpause after maintenance is complete. First run `airflow dags list` and store the list of unpaused Dags. Then use this same list to run both `dags pause` for each Dag prior to maintenance, and `dags unpause` after. A benefit of this is you can try un-pausing just one or two Dags (perhaps dedicated [test Dags](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#integration-test-dags)) after the upgrade to make sure things are working before turning everything back on.