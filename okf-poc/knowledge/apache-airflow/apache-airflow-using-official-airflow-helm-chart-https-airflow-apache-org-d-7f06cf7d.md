---
id: apache-airflow-using-official-airflow-helm-chart-https-airflow-apache-org-d-7f06cf7d
type: concept
title: '[Using Official Airflow Helm Chart](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id5)'
description: 'More details: [Helm Chart for Apache Airflow](https://airflow.apache.org/docs/helm-chart/stable/index.html
  "(in helm-chart v2.0.0)")'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [Using Official Airflow Helm Chart](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id5)

More details: [Helm Chart for Apache Airflow](https://airflow.apache.org/docs/helm-chart/stable/index.html "(in helm-chart v2.0.0)")

**When this option works best**

- This installation method is useful when you are not only familiar with Container/Docker stack but also when you
  use Kubernetes and want to install and maintain Airflow using the community-managed Kubernetes installation
  mechanism via Helm chart.
- It provides not only a capability of running Airflow components in isolation from other software
  running on the same physical or virtual machines and managing dependencies, but also it provides capabilities of
  easier maintaining, configuring and upgrading Airflow in the way that is standardized and will be maintained
  by the community.
- The Chart uses the Official Airflow Production Docker Images to run Airflow.

**Intended users**

- Users who are familiar with Containers and Docker stack and understand how to build their own container images.
- Users who understand how to install providers and dependencies from PyPI with constraints if they want to extend or customize the image.
- Users who manage their infrastructure using Kubernetes and manage their applications on Kubernetes using Helm Charts.

**What are you expected to handle**

- You are expected to be able to customize or extend Container/Docker images if you want to
  add extra dependencies. You are expected to put together a deployment built of several containers
  (for example using Docker Compose) and to make sure that they are linked together.
- You are responsible for setting up database.
- The Helm Chart manages your database schema, automates startup, recovery and restarts of the
  components of the application and linking them together, so you do not have to worry about that.
- You are responsible to manage your own customizations and extensions for your custom dependencies.
  With the Official Airflow Docker Images, upgrades of Airflow and Airflow Providers which
  are part of the reference image are handled by the community - you need to make sure to pick up
  those changes when released by upgrading the base image. However, you are responsible for creating a
  pipeline of building your own custom images with your own added dependencies and Providers and need to
  repeat the customization step and building your own image when new version of Airflow image is released.
- You need to setup monitoring of your system allowing you to observe resources and react to problems.
- You are expected to configure and manage appropriate resources for the installation (memory, CPU, etc) based
  on the monitoring of your installation and feedback loop.

**What Apache Airflow Community provides for that method**

- You have instructions: [Building the image](https://airflow.apache.org/docs/docker-stack/build.html "(in docker-stack vstable)") on how to build and customize your image.
- You have [Helm Chart for Apache Airflow](https://airflow.apache.org/docs/helm-chart/stable/index.html "(in helm-chart v2.0.0)") - full documentation on how to configure and install the Helm Chart.
- The Helm Chart is managed by the same people who build Airflow, and they are committed to keep
  it updated whenever new features and capabilities of Airflow are released.

**Where to ask for help**

- For quick questions with the Official Docker Image there is the `#production-docker-image` channel in Airflow Slack.
- For quick questions with the official Helm Chart there is the `#helm-chart-official` channel in Slack.
- The `#user-troubleshooting` channel on Airflow Slack for quick general
  troubleshooting questions. The [GitHub discussions](https://github.com/apache/airflow/discussions)
  if you look for longer discussion and have more information to share.
- The `#user-best-practices` channel on Slack can be used to ask for and share best
  practices on u