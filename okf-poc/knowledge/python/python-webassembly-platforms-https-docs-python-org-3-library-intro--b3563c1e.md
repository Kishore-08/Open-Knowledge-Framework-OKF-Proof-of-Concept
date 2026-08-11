---
id: python-webassembly-platforms-https-docs-python-org-3-library-intro--b3563c1e
type: concept
title: WebAssembly platforms[¶](https://docs.python.org/3/library/intro.html#webassembly-platforms
  "Link to this heading")
description: The [WebAssembly](https://webassembly.org/) platforms `wasm32-emscripten`
  ([Emscripten](https://emscripten.org/)) and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/intro.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### WebAssembly platforms[¶](https://docs.python.org/3/library/intro.html#webassembly-platforms "Link to this heading")

The [WebAssembly](https://webassembly.org/) platforms `wasm32-emscripten` ([Emscripten](https://emscripten.org/)) and
`wasm32-wasi` ([WASI](https://wasi.dev/)) provide a subset of POSIX APIs. WebAssembly runtimes
and browsers are sandboxed and have limited access to the host and external
resources. Any Python standard library module that uses processes, threading,
networking, signals, or other forms of inter-process communication (IPC), is
either not available or may not work as on other Unix-like systems. File I/O,
file system, and Unix permission-related functions are restricted, too.
Emscripten does not permit blocking I/O. Other blocking operations like
[`sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep") block the browser event loop.

The properties and behavior of Python on WebAssembly platforms depend on the
[Emscripten](https://emscripten.org/)-SDK or [WASI](https://wasi.dev/)-SDK version, WASM runtimes (browser, NodeJS,
[wasmtime](https://wasmtime.dev/)), and Python build time flags. WebAssembly, Emscripten, and WASI
are evolving standards; some features like networking may be
supported in the future.

For Python in the browser, users should consider [Pyodide](https://pyodide.org/) or [PyScript](https://pyscript.net/).
PyScript is built on top of Pyodide, which itself is built on top of
CPython and Emscripten. Pyodide provides access to browsers’ JavaScript and
DOM APIs as well as limited networking capabilities with JavaScript’s
`XMLHttpRequest` and `Fetch` APIs.

- Process-related APIs are not available or always fail with an error. That
  includes APIs that spawn new processes ([`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork"),
  [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")), wait for processes ([`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")), send signals
  ([`kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill")), or otherwise interact with processes. The
  [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") is importable but does not work.
- The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module is available, but is limited and behaves
  differently from other platforms. On Emscripten, sockets are always
  non-blocking and require additional JavaScript code and helpers on the
  server to proxy TCP through WebSockets; see [Emscripten Networking](https://emscripten.org/docs/porting/networking.html)
  for more information. WASI snapshot preview 1 only permits sockets from an
  existing file descriptor.
- Some functions are stubs that either don’t do anything and always return
  hardcoded values.
- Functions related to file descriptors, file permissions, file ownership, and
  links are limited and don’t support some operations. For example, WASI does
  not permit symlinks with absolute file names.