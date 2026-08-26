---
id: apache-airflow-what-does-templatenotfound-mean-1ae4eb88
type: concept
title: What does `TemplateNotFound` mean?
description: '`TemplateNotFound` errors are usually due to misalignment with user
  expectations when passing path to operator'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### What does `TemplateNotFound` mean?

`TemplateNotFound` errors are usually due to misalignment with user expectations when passing path to operator
that trigger Jinja templating. A common occurrence is with `BashOperator`.

Another commonly missed fact is that the files are resolved relative to where the pipeline file lives. You can add
other directories to the `template_searchpath` of the Dag object to allow for other non-relative location.