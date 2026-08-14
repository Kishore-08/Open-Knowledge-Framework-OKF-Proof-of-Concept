---
id: fastapi-run-your-code-with-your-debugger-https-fastapi-tiangolo-com--222721d9
type: concept
title: Run your code with your debugger[¶](https://fastapi.tiangolo.com/tutorial/debugging/#run-your-code-with-your-debugger
  "Permanent link")
description: Because you are running the Uvicorn server directly from your code, you
  can call your Python program (your FastAPI application) directly from the debugger.
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/debugging/
updated_at: '2026-08-14'
created_at: '2026-08-14'
---

## Run your code with your debugger[¶](https://fastapi.tiangolo.com/tutorial/debugging/#run-your-code-with-your-debugger "Permanent link")

Because you are running the Uvicorn server directly from your code, you can call your Python program (your FastAPI application) directly from the debugger.

---

For example, in Visual Studio Code, you can:

- Go to the "Debug" panel.
- "Add configuration...".
- Select "Python"
- Run the debugger with the option "`Python: Current File (Integrated Terminal)`".

It will then start the server with your **FastAPI** code, stop at your breakpoints, etc.

Here's how it might look:

---

If you use PyCharm, you can:

- Open the "Run" menu.
- Select the option "Debug...".
- Then a context menu shows up.
- Select the file to debug (in this case, `main.py`).

It will then start the server with your **FastAPI** code, stop at your breakpoints, etc.

Here's how it might look: