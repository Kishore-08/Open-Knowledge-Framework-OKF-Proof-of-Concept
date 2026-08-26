---
id: python-transaction-control-https-docs-python-org-3-library-sqlite3--d14c7d1a
type: concept
title: Transaction control[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control
  "Link to this heading")
description: '`sqlite3` offers multiple methods of controlling whether,'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Transaction control[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control "Link to this heading")

`sqlite3` offers multiple methods of controlling whether,
when and how database transactions are opened and closed.
[Transaction control via the autocommit attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-autocommit) is recommended,
while [Transaction control via the isolation\_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level)
retains the pre-Python 3.12 behaviour.

#### Transaction control via the `autocommit` attribute[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-autocommit-attribute "Link to this heading")

The recommended way of controlling transaction behaviour is through
the [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute,
which should preferably be set using the *autocommit* parameter
of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect").

It is suggested to set *autocommit* to `False`,
which implies [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction control.
This means:

- `sqlite3` ensures that a transaction is always open,
  so [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"), [`Connection.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit"), and [`Connection.rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback")
  will implicitly open a new transaction
  (immediately after closing the pending one, for the latter two).
  `sqlite3` uses `BEGIN DEFERRED` statements when opening transactions.
- Transactions should be committed explicitly using `commit()`.
- Transactions should be rolled back explicitly using `rollback()`.
- An implicit rollback is performed if the database is
  [`close()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close")-ed with pending changes.

Set *autocommit* to `True` to enable SQLite’s [autocommit mode](https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions).
In this mode, [`Connection.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") and [`Connection.rollback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.rollback "sqlite3.Connection.rollback")
have no effect.
Note that SQLite’s autocommit mode is distinct from
the [**PEP 249**](https://peps.python.org/pep-0249/)-compliant [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") attribute;
use [`Connection.in_transaction`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.in_transaction "sqlite3.Connection.in_transaction") to query
the low-level SQLite autocommit mode.

Set *autocommit* to [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL")
to leave transaction control behaviour to the
[`Connection.isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") attribute.
See [Transaction control via the isolation\_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information.

#### Transaction control via the `isolation_level` attribute[¶](https://docs.python.org/3/library/sqlite3.html#transaction-control-via-the-isolation-level-attribute "Link to this heading")

Note

The recommended way of controlling transactions is via the
[`autocommit`](https://docs.python.org/3/library/sqlite3.