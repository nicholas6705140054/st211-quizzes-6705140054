# Lab 3 Class Exercise - Assertions and Test Organization

# Min Htet Aung - 6705140054

This lab was done over two classes (weeks 4 and 5). Week 4 covered Steps 1-2: choosing
the right kind of assertion for the kind of data being checked, and grouping related tests
together inside a class. Week 5 continued from Step 3 to the end: tagging tests with
markers, skipping tests, marking expected failures, and configuring pytest for the whole
project with `pytest.ini`.

## What is in this folder

| File | What it shows |
| --- | --- |
| `test_assertions.py` | Equality, inequality, comparison, membership, boolean and `None` assertions |
| `test_collections.py` | Asserting on lists, dictionaries and sets |
| `test_floats.py` | Comparing floating-point numbers with `pytest.approx` |
| `shopping.py` | A small `ShoppingCart` class used as the code under test |
| `test_shopping.py` | `TestShoppingCart`, a class that groups the four cart tests |
| `test_markers.py` | Custom `smoke`, `slow` and `regression` markers |
| `test_skips.py` | `skip` and `skipif` |
| `test_xfail.py` | Expected failures, including an `XPASS` |
| `test_conditional.py` | `skipif` based on a condition checked at runtime |
| `test_strict.py` | An undeclared marker, kept on purpose to prove `--strict-markers` works |
| `pytest.ini` | Project-wide configuration |

## Step 1 - Assertion types

I practised writing assertions that match the data instead of forcing everything into
one style. Lists and dictionaries compare directly with `==`, dictionaries ignore key
order, and sets support operations such as `&` for intersection.

The float test was the important one. `0.1 + 0.2` does not give exactly `0.3` in binary
floating point, so a plain `==` comparison fails. `pytest.approx(0.3)` passes because it
allows a tiny tolerance, and `test_float_without_approx_fails` documents the raw
inequality so the reason is visible in the test suite itself.

## Step 2 - Grouping tests in a class

`TestShoppingCart` collects every cart test in one place. The naming rules matter here:
the class name has to start with `Test`, the methods have to start with `test_`, each
method takes `self`, and the class must not define `__init__`, because pytest creates the
instance itself.

Grouping means I can run the whole group or one single method:

```bash
pytest test_shopping.py::TestShoppingCart -v
pytest "test_shopping.py::TestShoppingCart::test_total_sums_prices" -v
```

## Step 3 - Markers

A marker is a tag attached to a test with a decorator such as `@pytest.mark.smoke`.
Markers let one test suite serve several purposes:

- **smoke** - a small set of quick checks on the most critical features. If a smoke test
  fails, the build is too broken to bother testing further.
- **slow** - tests that take noticeable time, usually because they touch a database, call
  an external API, load large files or do heavy computation.
- **regression** - tests that lock in a bug fix so the same bug cannot come back.

Selecting by marker (run from this folder, excluding `test_strict.py`):

```bash
pytest -m smoke --ignore=test_strict.py                  # 2 passed, 23 deselected
pytest -m "not slow" --ignore=test_strict.py             # only the slow test is deselected
pytest -m "smoke or regression" --ignore=test_strict.py  # 3 passed, 22 deselected
```

The deselected count in the output is the proof that the filtering worked.

## Step 4 - Skipping and expected failures

`skip` and `xfail` look similar but mean different things:

- `skip` means **do not run this at all**. The body never executes, so
  `test_future_feature` contains `assert False` and still does not fail.
- `xfail` means **run it, I already know it fails**. The failure is recorded as expected
  instead of breaking the build.

Running the file gives all four outcomes:

```
test_skips.py::test_future_feature       SKIPPED (Feature not implemented yet)
test_skips.py::test_needs_modern_python  PASSED
test_xfail.py::test_known_broken_feature XFAIL (Known bug #123, fix pending)
test_xfail.py::test_actually_works_now   XPASS (Might pass sometimes)
```

`XPASS` is the interesting one. It means a test marked as broken has started passing,
which is the signal that the bug was fixed and the marker should now be removed. That is
why `xfail` is better than deleting a failing test: deleting it loses the record of the
bug, while `xfail` keeps it documented and tells you when it is fixed.

## Step 5 - Configuration with pytest.ini

`pytest.ini` puts the settings in one file so everyone runs the tests the same way:

| Setting | Purpose |
| --- | --- |
| `testpaths` | Where pytest looks for tests |
| `addopts` | Flags applied automatically on every run |
| `markers` | The list of declared marker names |
| `--strict-markers` | Turns an unregistered marker into an error instead of a warning |
| `python_files` / `python_classes` / `python_functions` | The discovery naming rules |

Because `addopts = -v --tb=short --strict-markers`, running plain `pytest` is already
verbose with short tracebacks, without typing any flags.

## The strict-markers demonstration

`test_strict.py` uses `@pytest.mark.nonexistent_marker`, which is not declared in
`pytest.ini`. Running it produces a collection error rather than a silent pass:

```bash
pytest test_strict.py
# ERROR test_strict.py - Failed: 'nonexistent_marker' not found in `markers` configuration option
```

Without `--strict-markers`, a typo like `@pytest.mark.smoek` would be accepted quietly and
that test would never be picked up by `pytest -m smoke`. The test would exist but never
run, which is worse than a test that fails.

## How to run

`test_strict.py` is kept deliberately, so the full suite is run with it excluded:

```bash
cd lab_3_class_exercise
pytest --ignore=test_strict.py
```

Result: **22 passed, 1 skipped, 1 xfailed, 1 xpassed**.

## Review questions

1. **Why use `pytest.approx` for floats?** Floating-point maths is slightly imprecise
   (`0.1 + 0.2` is not exactly `0.3`), so `approx` compares within a tiny tolerance.
2. **Difference between skip and xfail?** `skip` never runs the test; `xfail` runs it and
   expects it to fail, reporting `XPASS` if it unexpectedly passes.
3. **What does `--strict-markers` protect against?** Typos in marker names, which would
   otherwise be accepted silently and leave tests that never get selected.

## What I learned

- Different data types deserve different assertions
- Floating-point comparisons need `pytest.approx`, never `==`
- Test classes group related tests so they can be selected and run as one unit
- Pytest discovers tests by naming convention, so the names are part of the code
- Markers turn one suite into many suites that can be selected on demand
- `skip` never runs a test, `xfail` runs it and expects the failure
- `XPASS` is a signal to go back and remove the marker
- Central configuration removes the guesswork about how tests should be run
- `--strict-markers` catches marker typos, which would otherwise hide tests silently
