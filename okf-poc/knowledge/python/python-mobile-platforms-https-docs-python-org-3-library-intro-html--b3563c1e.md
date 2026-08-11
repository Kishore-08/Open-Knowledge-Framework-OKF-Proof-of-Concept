---
id: python-mobile-platforms-https-docs-python-org-3-library-intro-html--b3563c1e
type: concept
title: Mobile platforms[¶](https://docs.python.org/3/library/intro.html#mobile-platforms
  "Link to this heading")
description: Android and iOS are, in most respects, POSIX operating systems. File
  I/O, socket handling,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/intro.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Mobile platforms[¶](https://docs.python.org/3/library/intro.html#mobile-platforms "Link to this heading")

Android and iOS are, in most respects, POSIX operating systems. File I/O, socket handling,
and threading all behave as they would on any POSIX operating system. However,
there are several major differences:

- Mobile platforms can only use Python in “embedded” mode. There is no Python
  REPL, and no ability to use separate executables such as **python** or
  **pip**. To add Python code to your mobile app, you must use
  the [Python embedding API](https://docs.python.org/3/extending/embedding.html#embedding). For more details, see
  [Using Python on Android](https://docs.python.org/3/using/android.html#using-android) and [Using Python on iOS](https://docs.python.org/3/using/ios.html#using-ios).
- Subprocesses:

  - On Android, creating subprocesses is possible but [officially unsupported](https://issuetracker.google.com/issues/128554619#comment4).
    In particular, Android does not support any part of the System V IPC API,
    so [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") is not available.
  - An iOS app cannot use any form of subprocessing, multiprocessing, or
    inter-process communication. If an iOS app attempts to create a subprocess,
    the process creating the subprocess will either lock up, or crash. An iOS app
    has no visibility of other applications that are running, nor any ability to
    communicate with other running applications, outside of the iOS-specific APIs
    that exist for this purpose.
- Mobile apps have limited access to modify system resources (such as the system
  clock). These resources will often be *readable*, but attempts to modify
  those resources will usually fail.
- Console input and output:

  - On Android, the native `stdout` and `stderr` are not connected to
    anything, so Python installs its own streams which redirect messages to the
    system log. These can be seen under the tags `python.stdout` and
    `python.stderr` respectively.
  - iOS apps have a limited concept of console output. `stdout` and
    `stderr` *exist*, and content written to `stdout` and `stderr` will be
    visible in logs when running in Xcode, but this content *won’t* be recorded
    in the system log. If a user who has installed your app provides their app
    logs as a diagnostic aid, they will not include any detail written to
    `stdout` or `stderr`.
  - Mobile apps have no usable `stdin` at all. While apps can display an on-screen
    keyboard, this is a software feature, not something that is attached to
    `stdin`.

    As a result, Python modules that involve console manipulation (such as
    [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.") and [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")) are not available on mobile platforms.