# Lab 4 Class Exercise - Fixtures and Test Data Management

# Min Htet Aung - 6705140054

Earlier labs repeated the same setup (`BankAccount(100)`) inside every test. This lab
replaced that repetition with fixtures: functions that prepare what a test needs and
hand it over automatically.

## What is in this folder

| File | What it shows |
| --- | --- |
| `bank.py` | The `BankAccount` used in this lab |
| `test_before.py` | The problem: setup copied into every test |
| `test_after.py` | The fix: one `account` fixture, requested by name |
| `test_teardown.py` | `yield` fixture that creates a file, then deletes it after each test |
| `test_db_style.py` | `yield` fixture that connects a fake database, then disconnects |
| `test_scope.py` | `function` scope vs `module` scope |
| `test_session.py` | `session` scope - setup runs once for the whole run |
| `conftest.py` | Fixtures shared by every test file in this folder |
| `test_shared_a.py`, `test_shared_b.py` | Use the `conftest.py` fixtures without importing them |
| `test_factory.py` | Factory fixture - `make_account(balance)` builds custom accounts |
| `test_factory_advanced.py` | Factory with a default role and cleanup tracking |

## Step 1 - First fixture

A test lists the fixture name as a parameter, and pytest runs the fixture and passes the
result in. Each test gets a **fresh** account, so the tests stay independent.

## Step 2 - Setup and teardown

Code before `yield` is setup, code after it is teardown. With `-s` the order is visible:

```
test_teardown.py::test_file_exists
[setup] file created
[teardown] file removed
```

Teardown runs even when a test fails, so `test_data.txt` never gets left behind.

## Step 3 - Scope

| Scope | Runs once per |
| --- | --- |
| `function` (default) | test |
| `class` | test class |
| `module` | file |
| `session` | whole test run |

In `test_scope.py` the function fixture printed 3 times (once per test) and the module
fixture printed only once. Wider scope is faster but means tests share the object, so it
suits read-only things like config, not something a test changes.

## Step 4 - conftest.py

Fixtures in `conftest.py` are found automatically by every test file in the same folder,
with no import. `test_shared_a.py` and `test_shared_b.py` both use `funded_account`, and
each still gets its own fresh `BankAccount(1000)`.

## Step 5 - Factory fixtures

A normal fixture returns an object; a factory fixture returns a **function** that builds
objects. That lets one test ask for `make_account(100)` and another for
`make_account(5000)`, or create several in one test. `make_user` also tracks every user it
made and reports them in its teardown.

## How to run

```bash
cd lab_4_class_exercise
python -m pytest -v
python -m pytest -v -s      # show setup / teardown / scope prints
```

Result: **24 passed**.

## Review questions

1. **Before vs after `yield`?** Before: setup (create, connect). After: teardown (delete,
   disconnect). The yielded value is what the test receives.
2. **When use `scope="session"`?** For expensive setup that tests only read - e.g. loading
   config or opening one connection for the whole run.
3. **Why does a factory return a function?** So each test can decide the details
   (balance, name, role) and create as many objects as it needs.
