# Lab 1 Class Exercise - Testing Fundamentals and Your First Automated Test

# Min Htet Aung - 6705140054

This lab set up pytest and walked through the basics: writing a test function, reading
the output, testing a real module, and handling failing tests and exceptions.

## What is in this folder

| File | What it shows |
| --- | --- |
| `test_first.py` | Three first tests using plain `assert` |
| `test_output.py` | A test that prints, used to show what the `-s` flag does |
| `calculator.py` | `add`, `subtract`, `multiply`, `divide` - the code under test |
| `test_calculator.py` | Tests for every calculator function, plus one written explicitly as Arrange-Act-Assert |
| `test_failing.py` | A test that was committed failing on purpose, then fixed in the next commit |
| `test_exceptions.py` | `pytest.raises` checking that dividing by zero raises `ValueError` with the right message |

## Step 2 - First tests

pytest finds tests by name: the file must start with `test_` and so must the function.
Inside, a plain `assert` is the check. If the expression is true the test passes.

## Step 3 - Reading the output

| Command | What it does |
| --- | --- |
| `pytest` | Runs everything, one dot per passing test |
| `pytest -v` | Verbose - one line per test with PASSED / FAILED |
| `pytest -s` | Shows `print` output, which pytest hides by default |
| `pytest --tb=no -q` | Just the summary line |
| `pytest test_first.py::test_addition` | Runs one single test |

Result symbols: `.` passed, `F` failed, `E` error, `s` skipped, `x` expected failure.

## Step 4 - Testing a real function and the AAA pattern

`test_add_aaa_pattern` splits the test into three parts:

- **Arrange** - set up the inputs (`first_number = 100`, `second_number = 250`)
- **Act** - call the function once (`add(...)`)
- **Assert** - check the result (`== 350`)

## Step 5 - Failing tests and exceptions

`test_failing.py` first expected `add(2, 2) == 5`. pytest reported:

```
>       assert result == 5
E       assert 4 == 5
```

The `E` line shows the actual value (4) next to the expected one (5), so the mistake is
obvious. The expectation was corrected to 4 in the following commit.

`test_exceptions.py` shows that raising an error can be the *correct* behaviour.
`pytest.raises(ValueError, match="Cannot divide by zero")` passes only if that exact
error is raised.

## How to run

```bash
cd lab_1_class_exercise
python -m pytest -v
```

Result: **12 passed**.

## Review questions

1. **What naming rule must a test function follow?** Its name must start with `test_`,
   inside a file whose name starts with `test_`.
2. **What does AAA stand for?** Arrange, Act, Assert.
3. **How do you test that a function raises an exception?** Wrap the call in
   `with pytest.raises(ErrorType):` - optionally with `match=` to check the message.
