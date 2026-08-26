---
id: apache-airflow-locally-installed-software-extras-f586a1ea
type: concept
title: Locally installed software extras
description: These are extras that add dependencies needed for integration with other
  software packages installed usually as part of the deployment of Airflow.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Locally installed software extras

These are extras that add dependencies needed for integration with other software packages installed usually as part of the deployment of Airflow.
Some of those enable Airflow to use executors to run tasks with them - other than via the built-in LocalExecutor.

| extra | install command | brings | enables executors |
| --- | --- | --- | --- |
| arangodb | `pip install 'apache-airflow[arangodb]'` | ArangoDB operators, sensors and hook |  |
| celery | `pip install 'apache-airflow[celery]'` | Celery dependencies and sensor | CeleryExecutor |
| cncf-kubernetes | `pip install 'apache-airflow[cncf-kubernetes]'` | Kubernetes client libraries, KubernetesPodOperator & friends | KubernetesExecutor |
| docker | `pip install 'apache-airflow[docker]'` | Docker hooks and operators |  |
| edge3 | `pip install 'apache-airflow[edge3]'` | Connect Edge Workers via HTTP to the scheduler | EdgeExecutor |
| elasticsearch | `pip install 'apache-airflow[elasticsearch]'` | Elasticsearch hooks and Log Handler |  |
| exasol | `pip install 'apache-airflow[exasol]'` | Exasol hooks and operators |  |
| fab | `pip install 'apache-airflow[fab]'` | FAB auth manager |  |
| git | `pip install 'apache-airflow[git]'` | Git bundle and hook |  |
| github | `pip install 'apache-airflow[github]'` | GitHub operators and hook |  |
| influxdb | `pip install 'apache-airflow[influxdb]'` | Influxdb operators and hook |  |
| ibm-mq | `pip install 'apache-airflow[ibm-mq]'` | IBM MQ hook and trigger |  |
| jenkins | `pip install 'apache-airflow[jenkins]'` | Jenkins hooks and operators |  |
| mongo | `pip install 'apache-airflow[mongo]'` | Mongo hooks and operators |  |
| microsoft-mssql | `pip install 'apache-airflow[microsoft-mssql]'` | Microsoft SQL Server operators and hook. |  |
| mysql | `pip install 'apache-airflow[mysql]'` | MySQL operators and hook |  |
| neo4j | `pip install 'apache-airflow[neo4j]'` | Neo4j operators and hook |  |
| odbc | `pip install 'apache-airflow[odbc]'` | ODBC data sources including MS SQL Server |  |
| openfaas | `pip install 'apache-airflow[openfaas]'` | OpenFaaS hooks |  |
| oracle | `pip install 'apache-airflow[oracle]'` | Oracle hooks and operators |  |
| postgres | `pip install 'apache-airflow[postgres]'` | PostgreSQL operators and hook |  |
| presto | `pip install 'apache-airflow[presto]'` | All Presto related operators & hooks |  |
| redis | `pip install 'apache-airflow[redis]'` | Redis hooks and sensors |  |
| samba | `pip install 'apache-airflow[samba]'` | Samba hooks and operators |  |
| singularity | `pip install 'apache-airflow[singularity]'` | Singularity container operator |  |
| teradata | `pip install 'apache-airflow[teradata]'` | Teradata hooks and operators |  |
| trino | `pip install 'apache-airflow[trino]'` | All Trino related operators & hooks |  |