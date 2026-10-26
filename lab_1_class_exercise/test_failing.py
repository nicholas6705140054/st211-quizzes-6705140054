from calculator import add, divide


def test_this_will_fail():
    result = add(2, 2)
    assert result == 5  # WRONG on purpose - 2+2 is 4, not 5
