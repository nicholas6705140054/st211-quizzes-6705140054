import json
from pathlib import Path

import pytest

# Resolve the data file next to this test, so it works from any working directory
DATA_FILE = Path(__file__).parent / "test_cases.json"


def load_cases():
    with open(DATA_FILE) as f:
        data = json.load(f)  # read the whole file
    return [(case["input"], case["expected"]) for case in data]


@pytest.mark.parametrize("text,expected", load_cases())  # loader runs at collection
def test_uppercase(text, expected):
    assert text.upper() == expected
