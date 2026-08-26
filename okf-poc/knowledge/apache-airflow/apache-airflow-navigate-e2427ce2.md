---
id: apache-airflow-navigate-e2427ce2
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/start.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Quick Start

This quick start guide will help you bootstrap an Airflow standalone instance on your local machine.

Note

Successful installation requires a Python 3 environment. Starting with Airflow 3.2.0, Airflow supports Python 3.10, 3.11, 3.12, 3.13, 3.14.

Officially supported installation methods are `pip` or `uv`.

Run `pip install apache-airflow[EXTRAS]==AIRFLOW_VERSION --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-AIRFLOW_VERSION/constraints-PYTHON_VERSION.txt"`, for example `pip install "apache-airflow[celery]==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.10.txt"` to install Airflow in a reproducible way. You can also use - much faster - `uv` - by adding `uv` before the command.

While there have been successes with using other tools like [poetry](https://python-poetry.org/) or
[pip-tools](https://pypi.org/project/pip-tools/), they do not share the same workflow as
`pip` or `uv` - especially when it comes to constraint vs. requirements management.
Installing via `Poetry` or `pip-tools` is not currently supported.

If you wish to install Airflow using those tools you should use the constraint files and convert
them to appropriate format and workflow that your tool requires.

This guide will help you quickly set up Apache Airflow using `uv`, a fast and modern tool for managing Python environments and dependencies. `uv` makes the installation process easy and provides a
smooth setup experience.

If you are on Windows, you have to use WSL2 (Linux environment for Windows).

```
wsl --install
```

1. **Set Airflow Home (optional)**:

   Airflow requires a home directory, and uses `~/airflow` by default, but you can set a different location if you prefer. The `AIRFLOW_HOME` environment variable is used to inform Airflow of the desired location. This step of setting the environment variable should be done before installing Airflow so that the installation process knows where to store the necessary files.

   ```
   export AIRFLOW_HOME=~/airflow
   ```
2. Install Airflow in a virtual environment using `uv` since it is a faster alternative that creates the `venv` automatically for you. It is an efficient alternative to using `pip` and `venv`.

   > Install uv: [uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
   >
   > For creating virtual environment with `uv`, refer to the documentation here:
   > [Creating and Maintaining Local virtual environment with uv](https://github.com/apache/airflow/blob/main/contributing-docs/07_local_virtualenv.rst#creating-and-maintaining-local-virtualenv-with-uv-recommended)

For installation using `pip` and `venv`, carry out the following steps.
On Debian/Ubuntu systems, Python may enforce
externally managed environments (PEP 668), so use a virtual environment
before running `pip install` commands:

```
# For Windows after WSL2 install, restart computer, then in WSL Ubuntu terminal
sudo apt update
sudo apt install python3-pip python3-venv

# Go to Linux home directory (not Windows mount)
cd ~

# Create airflow directory
mkdir -p ~/airflow
cd ~/airflow

# Create virtual environment
python3 -m venv airflow_venv

# Activate
source airflow_venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Airflow with correct Python version constraints
pip install apache-airflow[celery]==3.1.0 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.1.0/constraints-3.12.txt

# Verify installation
airflow version
```

3. Install Airflow using the constraints file, which is determined based on the URL we pass:

   ```
   AIRFLOW_VERSION=3.1.1

   # Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
   # See above for supported versions.
   PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{s