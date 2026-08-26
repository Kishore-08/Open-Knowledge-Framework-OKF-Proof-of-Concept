---
id: apache-airflow-apache-software-extras-f586a1ea
type: concept
title: Apache Software extras
description: These are extras that add dependencies needed for integration with other
  Apache projects (note that `apache.atlas` and
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Apache Software extras

These are extras that add dependencies needed for integration with other Apache projects (note that `apache.atlas` and
`apache.webhdfs` do not have their own providers - they only install additional libraries that can be used in
custom bash/python providers).

| extra | install command | enables |
| --- | --- | --- |
| apache-atlas | `pip install 'apache-airflow[apache-atlas]'` | Apache Atlas |
| apache-beam | `pip install 'apache-airflow[apache-beam]'` | Apache Beam operators & hooks |
| apache-cassandra | `pip install 'apache-airflow[apache-cassandra]'` | Cassandra related operators & hooks |
| apache-drill | `pip install 'apache-airflow[apache-drill]'` | Drill related operators & hooks |
| apache-druid | `pip install 'apache-airflow[apache-druid]'` | Druid related operators & hooks |
| apache-flink | `pip install 'apache-airflow[apache-flink]'` | Flink related operators & hooks |
| apache-hdfs | `pip install 'apache-airflow[apache-hdfs]'` | HDFS hooks and operators |
| apache-hive | `pip install 'apache-airflow[apache-hive]'` | All Hive related operators |
| apache-iceberg | `pip install 'apache-airflow[apache-iceberg]'` | Apache Iceberg hooks |
| apache-impala | `pip install 'apache-airflow[apache-impala]'` | All Impala related operators & hooks |
| apache-kafka | `pip install 'apache-airflow[apache-kafka]'` | All Kafka related operators & hooks |
| apache-kylin | `pip install 'apache-airflow[apache-kylin]'` | All Kylin related operators & hooks |
| apache-livy | `pip install 'apache-airflow[apache-livy]'` | All Livy related operators, hooks & sensors |
| apache-pig | `pip install 'apache-airflow[apache-pig]'` | All Pig related operators & hooks |
| apache-pinot | `pip install 'apache-airflow[apache-pinot]'` | All Pinot related hooks |
| apache-spark | `pip install 'apache-airflow[apache-spark]'` | All Spark related operators & hooks |
| apache-tinkerpop | `pip install apache-airflow[apache-tinkerpop]` | Apache-tinkerpop hooks and operators |
| apache-webhdfs | `pip install 'apache-airflow[apache-webhdfs]'` | HDFS hooks and operators |