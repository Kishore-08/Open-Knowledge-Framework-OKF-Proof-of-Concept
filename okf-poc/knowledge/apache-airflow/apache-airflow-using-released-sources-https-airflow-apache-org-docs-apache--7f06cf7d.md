---
id: apache-airflow-using-released-sources-https-airflow-apache-org-docs-apache--7f06cf7d
type: concept
title: '[Using released sources](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id2)'
description: 'More details: [Installing from Sources](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-sources.html)'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [Using released sources](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id2)

More details: [Installing from Sources](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-sources.html)

**When this option works best**

- This option is best if you expect to build all your software from sources.
- Apache Airflow is one of the projects that belong to the [Apache Software Foundation](https://www.apache.org/).
  It is a requirement for all ASF projects that they can be installed using official sources released via [Official Apache Downloads](https://dlcdn.apache.org/).
- This is the best choice if you have a strong need to [verify the integrity and provenance of the software](https://www.apache.org/dyn/closer.cgi#verify)

**Intended users**

- Users who are familiar with installing and building software from sources and are conscious about integrity and provenance
  of the software they use down to the lowest level possible.

**What are you expected to handle**

- You are expected to build and install Airflow and its components on your own.
- You should develop and handle the deployment for all components of Airflow.
- You are responsible for setting up the database, creating and managing database schema with `airflow db` commands,
  automated startup and recovery, maintenance, cleanup and upgrades of Airflow and the Airflow Providers.
- You need to setup monitoring of your system allowing you to observe resources and react to problems.
- You are expected to configure and manage appropriate resources for the installation (memory, CPU, etc) based
  on the monitoring of your installation and feedback loop. See the notes about requirements.

**What Apache Airflow Community provides for that method**

- You have [instructions](https://github.com/apache/airflow/blob/main/INSTALL) on how to build the software but due to various environments
  and tools you might want to use, you might expect that there will be problems which are specific to your deployment and environment
  you will have to diagnose and solve.

**Where to ask for help**

- The `#user-troubleshooting` channel on Slack can be used for quick general troubleshooting questions. The
  [GitHub discussions](https://github.com/apache/airflow/discussions) if you look for longer discussion and have more information to share.
- The `#user-best-practices` channel on Slack can be used to ask for and share best practices on using and deploying Airflow.
- If you can provide description of a reproducible problem with Airflow software, you can open issue at [GitHub issues](https://github.com/apache/airflow/issues)
- If you want to contribute back to Airflow, the `#contributors` Slack channel for building the Airflow itself