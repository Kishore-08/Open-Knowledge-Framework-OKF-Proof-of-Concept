---
id: python-import-resolution-and-custom-importers-https-docs-python-org-fca5b00e
type: concept
title: Import resolution and custom importers[¶](https://docs.python.org/3/library/logging.config.html#import-resolution-and-custom-importers
  "Link to this heading")
description: Import resolution, by default, uses the builtin [`__import__()`](https://docs.python.org/3/library/functions.html#import__
  "__import__") function
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Import resolution and custom importers[¶](https://docs.python.org/3/library/logging.config.html#import-resolution-and-custom-importers "Link to this heading")

Import resolution, by default, uses the builtin [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") function
to do its importing. You may want to replace this with your own importing
mechanism: if so, you can replace the `importer` attribute of the
`DictConfigurator` or its superclass, the
`BaseConfigurator` class. However, you need to be
careful because of the way functions are accessed from classes via
descriptors. If you are using a Python callable to do your imports, and you
want to define it at class level rather than instance level, you need to wrap
it with [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod"). For example:

```
from importlib import import_module
from logging.config import BaseConfigurator

BaseConfigurator.importer = staticmethod(import_module)
```

You don’t need to wrap with [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") if you’re setting the import
callable on a configurator *instance*.