import csv
from pathlib import Path

import pytest
from validate import is_valid_login

# Resolve the data file next to this test, so it works from any working directory
DATA_FILE = Path(__file__).parent / "logins.csv"


def load_login_cases():
    cases = []
    with open(DATA_FILE) as f:
        for row in csv.DictReader(f):  # reads header row as dict keys
            expected = row["valid"] == "True"  # convert string to bool
            cases.append((row["username"], row["password"], expected))
    return cases


@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected
