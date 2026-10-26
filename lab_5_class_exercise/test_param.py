import pytest
from mathutils import is_even


@pytest.mark.parametrize("number", [2, 4, 6, 8, 100])
def test_even_numbers(number):
    assert is_even(number) is True  # every value in the list must pass


@pytest.mark.parametrize("number", [1, 3, 5, 7, 99])
def test_odd_numbers(number):
    assert is_even(number) is False  # odd numbers must return False
