---
id: apache-airflow-does-airflow-support-extended-ascii-or-unicode-characters-1ae4eb88
type: concept
title: Does Airflow support extended ASCII or unicode characters?
description: If you intend to use extended ASCII or Unicode characters in Airflow,
  you have to provide a proper connection string to
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Does Airflow support extended ASCII or unicode characters?

If you intend to use extended ASCII or Unicode characters in Airflow, you have to provide a proper connection string to
the MySQL database since they define charset explicitly.

```
sql_alchemy_conn = mysql://airflow@localhost:3306/airflow?charset=utf8
```

You will experience `UnicodeDecodeError` thrown by `WTForms` templating and other Airflow modules like below.

```
'ascii' codec can't decode byte 0xae in position 506: ordinal not in range(128)
```