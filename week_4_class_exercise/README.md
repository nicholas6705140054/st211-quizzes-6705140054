# Week 4 Class Exercise - Assertion Types and Test Classes

# Min Htet Aung - 6705140054

This week covered the first two steps of the Assertions and Test Organization lab:
choosing the right kind of assertion for the kind of data being checked, and grouping
related tests together inside a class.

## What is in this folder

| File | What it shows |
| --- | --- |
| `test_assertions.py` | Equality, inequality, comparison, membership, boolean and `None` assertions |
| `test_collections.py` | Asserting on lists, dictionaries and sets |
| `test_floats.py` | Comparing floating-point numbers with `pytest.approx` |
| `shopping.py` | A small `ShoppingCart` class used as the code under test |
| `test_shopping.py` | `TestShoppingCart`, a class that groups the four cart tests |

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

## How to run

```bash
cd week_4_class_exercise
pytest -v
```

Result: **16 passed**.

## What I learned

- Different data types deserve different assertions
- Floating-point comparisons need `pytest.approx`, never `==`
- Test classes group related tests so they can be selected and run as one unit
- Pytest discovers tests by naming convention, so the names are part of the code
