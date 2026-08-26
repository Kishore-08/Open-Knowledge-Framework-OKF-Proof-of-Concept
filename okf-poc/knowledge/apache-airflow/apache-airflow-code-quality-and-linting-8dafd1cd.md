---
id: apache-airflow-code-quality-and-linting-8dafd1cd
type: concept
title: Code Quality and Linting
description: Maintaining high code quality is essential for the reliability and maintainability
  of your Airflow workflows.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Code Quality and Linting

Maintaining high code quality is essential for the reliability and maintainability of your Airflow workflows.
The following points summarize how this relates to Ruff:

1. This page documents Airflow best practices. Some of those practices are also supported by Ruff `AIR` rules,
   which help detect and enforce Airflow-specific best practices, including deprecated patterns and migration issues.
   The full list is available in
   [Airflow (AIR)](https://docs.astral.sh/ruff/rules/#airflow-air).
2. If you want to suggest a new Airflow best practice and add a matching Ruff `AIR` rule, follow the contributor
   process described in
   [Proposing Airflow Best Practices and Ruff AIR Rules](https://github.com/apache/airflow/blob/main/contributing-docs/24_proposing_best_practices_and_air_rules.rst).