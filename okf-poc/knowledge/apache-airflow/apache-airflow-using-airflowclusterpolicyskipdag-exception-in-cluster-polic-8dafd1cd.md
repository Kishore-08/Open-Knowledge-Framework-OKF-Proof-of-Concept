---
id: apache-airflow-using-airflowclusterpolicyskipdag-exception-in-cluster-polic-8dafd1cd
type: concept
title: Using AirflowClusterPolicySkipDag exception in cluster policies to skip specific
  Dags
description: Added in version 2.7.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using AirflowClusterPolicySkipDag exception in cluster policies to skip specific Dags

Added in version 2.7.

Airflow Dags can usually be deployed and updated with the specific branch of Git repository via `git-sync`.
But, when you have to run multiple Airflow clusters for some operational reasons, it’s very cumbersome to maintain multiple Git branches.
Especially, you have some difficulties when you need to synchronize two separate branches(like `prod` and `beta`) periodically with proper branching strategy.

- cherry-pick is too cumbersome to maintain Git repository.
- hard-reset is not recommended way for GitOps

So, you can consider connecting multiple Airflow clusters with same Git branch (like `main`), and maintaining those with different environment variables and different connection configurations with same `connection_id`.
you can also raise [`AirflowClusterPolicySkipDag`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/exceptions/index.html#airflow.exceptions.AirflowClusterPolicySkipDag "airflow.exceptions.AirflowClusterPolicySkipDag") exception on the cluster policy, to load specific Dags to `DagBag` on the specific Airflow deployment only, if needed.

```
def dag_policy(dag: DAG):
    """Skipping the Dag with `only_for_beta` tag."""

    if "only_for_beta" in dag.tags:
        raise AirflowClusterPolicySkipDag(
            f"Dag {dag.dag_id} is not loaded on the production cluster, due to `only_for_beta` tag."
        )
```

The example above, shows the `dag_policy` code snippet to skip the Dag depending on the tags it has.