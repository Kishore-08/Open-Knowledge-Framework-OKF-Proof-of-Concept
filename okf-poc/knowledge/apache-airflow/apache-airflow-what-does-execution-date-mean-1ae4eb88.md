---
id: apache-airflow-what-does-execution-date-mean-1ae4eb88
type: concept
title: What does `execution_date` mean?
description: '*Execution date* or `execution_date` is a historical name for what is
  called a'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### What does `execution_date` mean?

*Execution date* or `execution_date` is a historical name for what is called a
*logical date*, and also usually the start of the data interval represented by a
Dag run.

Airflow was developed as a solution for ETL needs. In the ETL world, you
typically summarize data. So, if you want to summarize data for `2016-02-19`,
you would do it at `2016-02-20` midnight UTC, which would be right after all
data for `2016-02-19` becomes available. This interval between midnights of
`2016-02-19` and `2016-02-20` is called the *data interval*, and since it
represents data in the date of `2016-02-19`, this date is also called the
run’s *logical date*, or the date that this Dag run is executed for, thus
*execution date*.

For backward compatibility, a datetime value `execution_date` is still
as [Template variables](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#templates-variables) with various formats in Jinja
templated fields, and in Airflow’s Python API. It is also included in the
context dictionary given to an Operator’s execute function.

```
class MyOperator(BaseOperator):
    def execute(self, context):
        logging.info(context["execution_date"])
```

However, you should always use `data_interval_start` or `data_interval_end`
if possible, since those names are semantically more correct and less prone to
misunderstandings.

Note that `ds` (the YYYY-MM-DD form of `data_interval_start`) refers to
*date* **\*string\***, not *date* **\*start\*** as may be confusing to some.

Tip

For more information on `logical date`, see [Data Interval](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html#data-interval) and
[Running Dags](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-dag-run).