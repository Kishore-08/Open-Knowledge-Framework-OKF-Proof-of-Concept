---
id: python-supporting-older-python-versions-https-docs-python-org-3-lib-47076c99
type: concept
title: Supporting older Python versions[¶](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions
  "Link to this heading")
description: Extraction filters were added to Python 3.12, but may be backported to
  older
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Supporting older Python versions[¶](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions "Link to this heading")

Extraction filters were added to Python 3.12, but may be backported to older
versions as security updates.
To check whether the feature is available, use e.g.
`hasattr(tarfile, 'data_filter')` rather than checking the Python version.

The following examples show how to support Python versions with and without
the feature.
Note that setting `extraction_filter` will affect any subsequent operations.

- Fully trusted archive:

  ```
  my_tarfile.extraction_filter = (lambda member, path: member)
  my_tarfile.extractall()
  ```
- Use the `'data'` filter if available, but revert to Python 3.11 behavior
  (`'fully_trusted'`) if this feature is not available:

  ```
  my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                         (lambda member, path: member))
  my_tarfile.extractall()
  ```
- Use the `'data'` filter; *fail* if it is not available:

  ```
  my_tarfile.extractall(filter=tarfile.data_filter)
  ```

  or:

  ```
  my_tarfile.extraction_filter = tarfile.data_filter
  my_tarfile.extractall()
  ```
- Use the `'data'` filter; *warn* if it is not available:

  ```
  if hasattr(tarfile, 'data_filter'):
      my_tarfile.extractall(filter='data')
  else:
      # remove this when no longer needed
      warn_the_user('Extracting may be unsafe; consider updating Python')
      my_tarfile.extractall()
  ```