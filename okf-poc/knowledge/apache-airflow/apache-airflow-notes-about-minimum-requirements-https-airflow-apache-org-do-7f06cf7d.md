---
id: apache-airflow-notes-about-minimum-requirements-https-airflow-apache-org-do-7f06cf7d
type: concept
title: '[Notes about minimum requirements](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id8)'
description: There are often questions about minimum requirements for Airflow for
  production systems, but it is
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [Notes about minimum requirements](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id8)

There are often questions about minimum requirements for Airflow for production systems, but it is
not possible to give a simple answer to that question.

The requirements that Airflow might need depend on many factors, including (but not limited to):
:   - The deployment your Airflow is installed with (see above ways of installing Airflow)
    - The requirements of the deployment environment (for example Kubernetes, Docker, Helm, etc.) that
      are completely independent from Airflow (for example DNS resources, sharing the nodes/resources)
      with more (or less) pods and containers that are needed that might depend on particular choice of
      the technology/cloud/integration of monitoring etc.
    - Technical details of database, hardware, network, etc. that your deployment is running on
    - The complexity of the code you add to your Dags, configuration, plugins, settings etc. (note, that
      Airflow runs the code that Dag author and Deployment Manager provide)
    - The number and choice of providers you install and use (Airflow has more than 80 providers) that can
      be installed by choice of the Deployment Manager and using them might require more resources.
    - The choice of parameters that you use when tuning Airflow. Airflow has many configuration parameters
      that can fine-tuned to your needs
    - The number of DagRuns and tasks instances you run with parallel instances of each in consideration
    - How complex are the tasks you run

The above “Dag” characteristics will change over time and even will change depending on the time of the day
or week, so you have to be prepared to continuously monitor the system and adjust the parameters to make
it works smoothly.

While we can provide some specific minimum requirements for some development “quick start” - such as
in case of our [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker) quick-start guide, it is not possible to provide any minimum
requirements for production systems.

The best way to think of resource allocation for Airflow instance is to think of it in terms of process
control theory - where there are two types of systems:

1. Fully predictable, with few knobs and variables, where you can reliably set the values for the
   knobs and have an easy way to determine the behaviour of the system
2. Complex systems with multiple variables, that are hard to predict and where you need to monitor
   the system and adjust the knobs continuously to make sure the system is running smoothly.

Airflow (and generally any modern systems running usually on cloud services, with multiple layers responsible
for resources as well multiple parameters to control their behaviour) is a complex system and it fall
much more in the second category. If you decide to run Airflow in production on your own, you should be
prepared for the monitor/observe/adjust feedback loop to make sure the system is running smoothly.

Having a good monitoring system that will allow you to monitor the system and adjust the parameters
is a must to put that in practice.

There are a few guidelines that you can use for optimizing your resource usage as well. The
[Fine-tuning your Scheduler performance](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#fine-tuning-scheduler) is a good starting point to fine-tune your scheduler, you can also follow
the [Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#best-practice) guide to make sure you are using Airflow in the most efficient way.

Also, one of the important things that Managed Services for Airflow provide is that they make a lot
of opinionated choices and fine-tune the system for you, so you don’t have to worry about it too much.
With such manage