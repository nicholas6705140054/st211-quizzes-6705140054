# Automated Software Testing (192-211)

**Student:** Min Htet Aung
**Student ID:** 6705140054
**University:** International College, Siam University

This repository holds my class exercises for Automated Software Testing, written in Python
with pytest. Each folder has its own README explaining what the lab covered, how to run
it, and the result.

## Labs

| Lab | Folder | Topic | Result |
| --- | --- | --- | --- |
| Lab 1 | [lab_1_class_exercise](lab_1_class_exercise/) | Testing fundamentals: first tests, reading output, calculator, AAA, exceptions | 12 passed |
| Lab 2 | [class_exercise](class_exercise/) | Effective test cases: AAA, independence, boundaries, naming, positive/negative | 23 passed |
| Lab 3 (steps 1-2) | [week_4_class_exercise](week_4_class_exercise/) | Assertion types and test classes | 16 passed |
| Lab 3 (steps 3-5) | [week_5_class_exercise](week_5_class_exercise/) | Markers, skip, xfail, `pytest.ini` | 6 passed, 1 skipped, 1 xfailed, 1 xpassed |
| Lab 4 | [lab_4_class_exercise](lab_4_class_exercise/) | Fixtures: setup/teardown, scope, `conftest.py`, factories | 24 passed |
| Lab 5 | [lab_5_class_exercise](lab_5_class_exercise/) | Parameterized and data-driven testing | 57 passed, 1 xfailed |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

## Running the tests

Run each lab from inside its own folder. Several labs have their own `bank.py`, so running
everything at once from the repository root would mix them up.

```bash
cd lab_1_class_exercise && python -m pytest -v && cd ..
cd class_exercise && python -m pytest -v && cd ..
cd week_4_class_exercise && python -m pytest -v && cd ..
cd week_5_class_exercise && python -m pytest --ignore=test_strict.py && cd ..
cd lab_4_class_exercise && python -m pytest -v && cd ..
cd lab_5_class_exercise && python -m pytest -v && cd ..
```

Some results are intentional and explained in the lab READMEs:

- **Lab 2** - `pytest test_dependent.py::test_b_withdraw` fails on its own. That file is the
  bad example of tests sharing state.
- **Lab 3** - `test_strict.py` stops with a collection error, proving `--strict-markers`
  catches an undeclared marker. The skip / xfail / xpass results are expected.
- **Lab 5** - the `known_bug` case is marked `xfail` on purpose.
