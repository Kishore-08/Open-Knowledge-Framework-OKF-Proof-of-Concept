---
id: apache-airflow-using-production-docker-images-https-airflow-apache-org-docs-7f06cf7d
type: concept
title: '[Using Production Docker Images](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id4)'
description: 'More details: [Docker Image for Apache Airflow](https://airflow.apache.org/docs/docker-stack/index.html
  "(in docker-stack vstable)")'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [Using Production Docker Images](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id4)

More details: [Docker Image for Apache Airflow](https://airflow.apache.org/docs/docker-stack/index.html "(in docker-stack vstable)")

**When this option works best**

This installation method is useful when you are familiar with Container/Docker stack. It provides a capability of
running Airflow components in isolation from other software running on the same physical or virtual machines with easy
maintenance of dependencies.

The images are built by Apache Airflow release managers and they use officially released packages from PyPI
and official constraint files - same that are used for installing Airflow from PyPI.

**Intended users**

- Users who are familiar with Containers and Docker stack and understand how to build their own container images.
- Users who understand how to install providers and dependencies from PyPI with constraints if they want to extend or customize the image.
- Users who know how to create deployments using Docker by linking together multiple Docker containers and maintaining such deployments.

**What are you expected to handle**

- You are expected to be able to customize or extend Container/Docker images if you want to
  add extra dependencies. You are expected to put together a deployment built of several containers
  (for example using `docker-compose`) and to make sure that they are linked together.
- You are responsible for setting up the database, creating and managing database schema with `airflow db` commands,
  automated startup and recovery, maintenance, cleanup and upgrades of Airflow and the Airflow Providers.
- You are responsible to manage your own customizations and extensions for your custom dependencies.
  With the Official Airflow Docker Images, upgrades of Airflow and Airflow Providers which
  are part of the reference image are handled by the community - you need to make sure to pick up
  those changes when released by upgrading the base image. However, you are responsible for creating a
  pipeline of building your own custom images with your own added dependencies and Providers and need to
  repeat the customization step and building your own image when new version of Airflow image is released.
- You should choose the right deployment mechanism. There are a number of available options of
  deployments of containers. You can use your own custom mechanism, custom Kubernetes deployments,
  custom Docker Compose, custom Helm charts etc., and you should choose it based on your experience
  and expectations.
- You need to setup monitoring of your system allowing you to observe resources and react to problems.
- You are expected to configure and manage appropriate resources for the installation (memory, CPU, etc) based
  on the monitoring of your installation and feedback loop.

**What Apache Airflow Community provides for that method**

- You have instructions: [Building the image](https://airflow.apache.org/docs/docker-stack/build.html "(in docker-stack vstable)") on how to build and customize your image.
- You have [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) where you can see an example of Quick Start which
  you can use to start Airflow quickly for local testing and development. However, this is just for inspiration.
  Do not expect to use this `docker-compose.yml` file for production installation, you need to get familiar
  with Docker Compose and its capabilities and build your own production-ready deployment with it if
  you choose Docker Compose for your deployment.
- The Docker Image is managed by the same people who build Airflow, and they are committed to keep
  it updated whenever new features and capabilities of Airflow are released.

**Where to ask for help**

- For quick questions with the Official Docker Image there is the `#production-docker-image` channel in Airflow Slack.
- The `#u