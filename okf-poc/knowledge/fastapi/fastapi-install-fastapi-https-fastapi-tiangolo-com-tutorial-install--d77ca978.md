---
id: fastapi-install-fastapi-https-fastapi-tiangolo-com-tutorial-install--d77ca978
type: concept
title: Install FastAPI[¶](https://fastapi.tiangolo.com/tutorial/#install-fastapi "Permanent
  link")
description: The first step is to set up your project and add FastAPI.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Install FastAPI[¶](https://fastapi.tiangolo.com/tutorial/#install-fastapi "Permanent link")

The first step is to set up your project and add FastAPI.

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/), then create a project and add FastAPI:

```
$ uv init awesome-project --bare
$ cd awesome-project
$ uv add "fastapi[standard]"

---> 100%
```

`uv add` creates the project's virtual environment in `.venv`, adds FastAPI to `pyproject.toml`, and creates `uv.lock` so the same package versions can be installed later.

What these commands do

- `uv init`: create a new Python project.
- `awesome-project`: create the project in a new directory with this name.
- `--bare`: create only the minimal `pyproject.toml` file, without generating a sample `main.py`, `README.md`, or other files. You will create the application files yourself in the next steps of this tutorial.

Then `cd awesome-project` enters the new project directory before adding FastAPI.

`uv` will use a compatible Python version already installed on your system, or download one if needed.

When you run `uv add`, it selects compatible versions of FastAPI and all the packages FastAPI depends on. It records the exact versions in `uv.lock`, making it possible to install the same package versions later on another computer or when deploying the application.

Creating or updating this file is called [**locking** the project dependencies](https://docs.astral.sh/uv/concepts/projects/sync/). `uv` does this automatically when you add a package.


FastAPI installation options

When you install with `uv add "fastapi[standard]"` it comes with some default optional standard dependencies, including `fastapi-cloud-cli`, which allows you to deploy to [FastAPI Cloud](https://fastapicloud.com).

If you don't want to have those optional dependencies, you can instead install `uv add fastapi`.

If you want to install the standard dependencies but without the `fastapi-cloud-cli`, you can install with `uv add "fastapi[standard-no-fastapi-cloud-cli]"`.


Using `pip` instead

If you prefer to manage a virtual environment and packages manually, create and activate a virtual environment and then install FastAPI with `pip install "fastapi[standard]"`.

Read the [Virtual Environments guide](https://tiangolo.com/guides/virtual-environments/) for the detailed steps.