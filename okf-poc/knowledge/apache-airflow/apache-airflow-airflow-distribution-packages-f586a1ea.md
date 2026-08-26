---
id: apache-airflow-airflow-distribution-packages-f586a1ea
type: concept
title: Airflow distribution packages
description: With Airflow 3, Airflow is now split into several independent and isolated
  distribution packages on top of
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Airflow distribution packages

With Airflow 3, Airflow is now split into several independent and isolated distribution packages on top of
already existing `providers` and the dependencies are isolated and simplified across those distribution
packages.

While the original installation methods via `apache-airflow` distribution package and extras still
work as previously and it installs complete Airflow installation ready to serve as scheduler, webserver, triggerer
and worker, the `apache-airflow` package is now a meta-package that installs all the other distribution
packages, it’s also possible to install only the distribution packages that are needed for a specific
component you want to run Airflow with.

The following distribution packages are available:

|  |  |  |
| --- | --- | --- |
| Distribution package | Purpose | Optional extras |
| apache-airflow-core | This is the core distribution package that contains the Airflow scheduler, webserver, triggerer code. | - Core extras that add optional functionality to Airflow   core system - enhancing its functionality across   multiple providers. - Group `all` extra that installs all optional   functionalities together. |
| apache-airflow-task-sdk | This is the distribution package that is needed to run tasks in the worker | - No optional extras |
| apache-airflow-providers-\* | Those are distribution packages that contain integrations of Airflow with external systems, 3rd-party software and services. Usually they provide operators, hooks, sensors, triggers, but also different types of extensions such as logging handlers, executors, and other functionalities that are tied to particular service or system. | - Each provider distribution packages might have its   own optional extras |
| apache-airflow | This is the meta-distribution-package that installs (mandatory):   - `apache-airflow-core` (always the same version as the   `apache-airflow`) - `apache-airflow-task-sdk` (latest) | - Any of the core extras - Any of the provider packages via extras   This is backwards-compatible with previous installation methods in Airflow 2.  Group extras:   - `all-core` - extra that installs all extras of the   `apache-airflow-core` package - `all` - extra that installs all core extras and   all provider packages (without their optional extras). |

As mentioned above, Airflow has a number of optional “extras” that you can use to add features to your
installation when you are installing Airflow. Those extras are a good way for the users to manage their
installation, but also they are useful for contributors to Airflow when they want to contribute some of
the features - including optional integrations of Airflow - via providers.

Here’s the list of all the extra dependencies of Apache Airflow.