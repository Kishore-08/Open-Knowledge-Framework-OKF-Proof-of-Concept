---
id: python-exiting-methods-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: Exiting methods[¶](https://docs.python.org/3/library/argparse.html#exiting-methods
  "Link to this heading")
description: ArgumentParser.exit(*status=0*, *message=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.exit
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Exiting methods[¶](https://docs.python.org/3/library/argparse.html#exiting-methods "Link to this heading")

ArgumentParser.exit(*status=0*, *message=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.exit "Link to this definition")
:   This method terminates the program, exiting with the specified *status*
    and, if given, it prints a *message* to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") before that.
    The user can override this method to handle these steps differently:

    ```
    class ErrorCatchingArgumentParser(argparse.ArgumentParser):
        def exit(self, status=0, message=None):
            if status:
                raise Exception(f'Exiting because of an error: {message}')
            exit(status)
    ```

ArgumentParser.error(*message*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.error "Link to this definition")
:   This method prints a usage message, including the *message*, to
    [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and terminates the program with a status code of 2.