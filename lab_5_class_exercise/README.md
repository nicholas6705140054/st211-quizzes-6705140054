# Lab 5 Class Exercise - Parameterized and Data-Driven Testing

# Min Htet Aung - 6705140054

This lab is about running one test function against many inputs instead of copy-pasting
near-identical tests (DRY testing: Don't Repeat Yourself). It covers three ways to do it:
inline `@pytest.mark.parametrize`, parametrized fixtures, and loading cases from data files.

## What is in this folder

| File | What it shows |
| --- | --- |
| `mathutils.py` | `is_even` and `factorial` - the first code under test |
| `test_param.py` | One parameter, plain list of values (2 functions -> 10 tests) |
| `test_factorial.py` | Input/expected pairs as tuples |
| `test_multi.py` | Two stacked decorators -> every combination (3 x 2 = 6 tests) |
| `discount.py` | `apply_discount(price, percent)` |
| `test_discount.py` | Five hand-picked discount scenarios |
| `test_discount_errors.py` | Parameterizing the error cases with `pytest.raises` |
| `test_default_ids.py` | Dictionary parameters get cryptic IDs: `[user0]`, `[user1]` |
| `test_custom_ids.py` | `ids=` gives readable IDs: `[alice-adult]`, `[bob-adult]` |
| `test_param_ids.py` | `pytest.param(..., id="free")` for per-case names |
| `test_param_marks.py` | `pytest.param(..., marks=xfail)` on one known-bad case |
| `test_param_fixture.py` | A fixture with `params=` - three database types |
| `test_browsers.py` | Two tests x three browsers, each with setup/teardown |
| `test_cases.json`, `test_data_driven.py` | Uppercase test cases loaded from JSON |
| `logins.csv`, `validate.py`, `test_csv_driven.py` | Login test cases loaded from CSV |

## Step 1 - Basic parameterization

`@pytest.mark.parametrize("n,expected", [(0, 1), (1, 1), ...])` works like a table: the
string is the column names and each tuple is a row. Unlike a `for` loop, every row is a
separate test, so one failing input does not stop the others from running.

## Step 2 - Multiple parameters

Stacking two decorators produces the **cross-product**:

```
test_combinations[10-1]  test_combinations[10-2]  test_combinations[10-3]
test_combinations[20-1]  test_combinations[20-2]  test_combinations[20-3]
```

Stacking is right when every pair is meaningful (every browser x every screen size). For
hand-picked scenarios like the discount cases, one decorator with tuples is right -
stacking 5 prices with 5 expected values would make 25 mostly wrong tests.

## Step 3 - IDs and readability

When a test fails in CI the ID is what you see first. `FAILED test_discount[free]` says
which scenario broke immediately; `[user1]` makes you go and look it up.

`test_param_marks.py` marks one case with `xfail`, with a `reason`, to document a known bug
without breaking the suite:

```
test_square[two_squared]    PASSED
test_square[three_squared]  PASSED
test_square[known_bug]      XFAIL (5**2 is 25, not 20 - bug not fixed yet)
```

## Step 4 - Parametrized fixtures

`@pytest.fixture(params=[...])` makes **every test that uses the fixture** run once per
value. In `test_browsers.py`, 2 tests x 3 browsers = 6 runs, each with its own setup and
teardown because the fixture uses `yield`. Adding a fourth browser to the list would cover
the whole suite without touching any test.

| | `@pytest.mark.parametrize` | `fixture(params=...)` |
| --- | --- | --- |
| Affects | One test function | All tests using the fixture |
| Good for | Input/output variations | Environment variations |
| Setup/teardown | No | Yes, via `yield` |

## Step 5 - Data-driven testing

The cases live in `test_cases.json` and `logins.csv`; the test code only loads and runs
them. Someone who does not write Python can add a row to the CSV and the suite covers it
on the next run. The loaders run at **collection** time, because pytest needs the list of
cases before it can create the tests.

The data file path is built from the test file's own location (`Path(__file__).parent`),
so the tests still find their data when pytest is started from another folder.

## How to run

```bash
cd lab_5_class_exercise
python -m pytest -v
python -m pytest -v -s      # show the print / setup / teardown output
```

Result: **57 passed, 1 xfailed**. The xfail is the deliberate `known_bug` case.

## Review questions

1. **Stacking 3 values and 4 values gives how many tests?** 3 x 4 = 12.
2. **Why add custom IDs?** So a failure message names the scenario (`[free]`) instead of
   an index (`[case2]`).
3. **`parametrize` on a test vs `params=` on a fixture?** `parametrize` affects only the
   one function it decorates; a parametrized fixture expands every test that uses it.
4. **What does data-driven testing give a non-programmer on the QA team?** They can add
   test cases by editing a CSV or JSON file, without writing any Python.
