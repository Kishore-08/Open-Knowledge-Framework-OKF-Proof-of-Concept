---
id: apache-airflow-other-extras-f586a1ea
type: concept
title: Other extras
description: These are extras that provide support for integration with external systems
  via some - usually - standard protocols.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Other extras

These are extras that provide support for integration with external systems via some - usually - standard protocols.

The entries with `*` in the `Preinstalled` column indicate that those extras (providers) are always
pre-installed when Airflow is installed.

| extra | install command | enables | Preinstalled |
| --- | --- | --- | --- |
| common-ai | `pip install 'apache-airflow[common-ai]'` | Common AI Operators and Hooks |  |
| common-compat | `pip install 'apache-airflow[common-compat]'` | Compatibility code for old Airflow |  |
| common-io | `pip install 'apache-airflow[common-io]'` | Core IO Operators |  |
| common-messaging | `pip install 'apache-airflow[common-messaging]'` | Core Messaging Operators |  |
| common-sql | `pip install 'apache-airflow[common-sql]'` | Core SQL Operators |  |
| ftp | `pip install 'apache-airflow[ftp]'` | FTP hooks and operators |  |
| grpc | `pip install 'apache-airflow[grpc]'` | Grpc hooks and operators |  |
| http | `pip install 'apache-airflow[http]'` | HTTP hooks, operators and sensors |  |
| imap | `pip install 'apache-airflow[imap]'` | IMAP hooks and sensors |  |
| jdbc | `pip install 'apache-airflow[jdbc]'` | JDBC hooks and operators |  |
| keycloak | `pip install apache-airflow[keycloak]` | Keycloak hooks and operators |  |
|
| microsoft-psrp | `pip install 'apache-airflow[microsoft-psrp]'` | PSRP hooks and operators |  |
| microsoft-winrm | `pip install 'apache-airflow[microsoft-winrm]'` | WinRM hooks and operators |  |
| openlineage | `pip install 'apache-airflow[openlineage]'` | Sending OpenLineage events |  |
| opensearch | `pip install 'apache-airflow[opensearch]'` | Opensearch hooks and operators |  |
| papermill | `pip install 'apache-airflow[papermill]'` | Papermill hooks and operators |  |
| sftp | `pip install 'apache-airflow[sftp]'` | SFTP hooks, operators and sensors |  |
| smtp | `pip install 'apache-airflow[smtp]'` | SMTP hooks and operators |  |
| sqlite | `pip install 'apache-airflow[sqlite]'` | SQLite hooks and operators |  |
| ssh | `pip install 'apache-airflow[ssh]'` | SSH hooks and operators |  |
| informatica | `pip install 'apache-airflow[informatica]'` | Informatica hooks and operators |  |