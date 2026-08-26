---
id: apache-airflow-staging-environment-8dafd1cd
type: concept
title: Staging environment
description: If possible, keep a staging environment to test the complete Dag run
  before deploying in the production.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Staging environment

If possible, keep a staging environment to test the complete Dag run before deploying in the production.
Make sure your Dag is parameterized to change the variables, e.g., the output path of S3 operation or the database used to read the configuration.
Do not hard code values inside the Dag and then change them manually according to the environment.

You can use environment variables to parameterize the Dag.

```
import os

dest = os.environ.get("MY_DAG_DEST_PATH", "s3://default-target/path/")
```