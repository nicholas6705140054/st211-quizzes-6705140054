# Lab 2 Class Exercise - Writing Effective Test Cases

# Min Htet Aung - 6705140054

I started with a simple banking exercise using `bank.py` and testing it with `pytest`. This helped me understand classes, methods, and validation in Python. I practiced creating a `BankAccount` with `deposit()` and `withdraw()`, and I learned how to handle invalid inputs using `ValueError`.

After that, I moved on to a grade calculation exercise in `grades.py`. This introduced conditional logic and score boundaries, where marks are converted into letter grades such as A, B, C, and F.

The rest of the lab was about what makes a test valuable instead of wasteful: one
behaviour per test, independence, descriptive names, and checking bad input as well as
good input.

## What is in this folder

| File | What it shows |
| --- | --- |
| `bank.py` | `BankAccount` - the code under test |
| `test_bank.py` | One clear Arrange-Act-Assert test |
| `test_bad_example.py` | What to avoid: three actions in one test |
| `test_dependent.py` | What to avoid: two tests sharing one account |
| `test_independent.py` | The fix: every test creates its own fresh account |
| `grades.py`, `test_grades.py` | Boundary value testing on letter grades |
| `test_named.py` | Test names that read like a specification |
| `validators.py` | `validate_email` and `validate_age` |
| `test_positive.py` | Positive tests - valid input is accepted |
| `test_negative.py` | Negative tests - invalid input is rejected |

## Step 1 - AAA in depth

Each test should Arrange the data, Act once, and Assert one outcome.
`test_everything_at_once` deposits, withdraws and deposits again before checking the
balance. It passes, but if it ever failed there would be no way to tell which of the three
actions broke.

## Step 2 - Test independence

`test_dependent.py` uses one `shared_account` for both tests. Run together they pass, but
running the second test on its own fails:

```bash
pytest test_dependent.py::test_b_withdraw -v
# E   assert 70 == 120
```

`test_b_withdraw` expected 120 only because `test_a_deposit` had already added 50.
`test_independent.py` fixes this by creating a fresh `BankAccount(100)` inside each test, so
the tests pass alone and in any order.

## Step 3 - Boundary values

Bugs hide at the edges, e.g. writing `>` instead of `>=`. A score of 85 would never catch
that, but 80 would. For `letter_grade` the values worth testing are 0 and 100 (min/max),
-1 (just below min), and each threshold plus the value just below it (80/79, 60/59).

## Step 4 - Descriptive names

`test_named.py` follows `test_[what]_[condition]_[expected]`. Reading only the `-v` output
already explains the rules of the account:

```
test_deposit_positive_amount_increases_balance PASSED
test_deposit_negative_amount_raises_value_error PASSED
test_withdraw_more_than_balance_raises_value_error PASSED
test_withdraw_exact_balance_leaves_zero PASSED
```

## Step 5 - Positive and negative testing

- **Positive** - does valid input work? A real email and the boundary ages 0 and 150 are
  accepted.
- **Negative** - is invalid input rejected? An email with no `@` or no domain raises
  `ValueError`; a negative age raises `ValueError`; a string age raises `TypeError`.

Code that accepts good input but crashes on bad input is not ready for real users, so both
kinds of test matter.

## How to run

```bash
cd lab_2_class_exercise
python -m pytest -v
pytest test_named.py -v --no-header
pytest test_positive.py test_negative.py -v
```

Result: **23 passed**.

## Review questions

1. **Why must tests be independent?** So a test's result depends only on the code it
   checks, not on which other tests ran first. Otherwise running one test alone, or in a
   different order, gives false failures.
2. **Scores 0-100 - which boundary values?** -1, 0, 100, 101, plus every threshold and the
   value just below it (59/60, 69/70, 79/80).
3. **Positive vs negative testing?** Positive tests confirm valid input is handled
   correctly; negative tests confirm invalid input is rejected with the right error.

## What I learned

- Python classes and functions
- writing and running tests
- edge cases and invalid inputs
- using test-driven practice to catch errors early
- one action per test makes failures easy to pinpoint
- shared state between tests creates fragile, order-dependent results
