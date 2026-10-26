def test_equality():
    assert 2 + 2 == 4


def test_inequality():
    assert 5 != 3


def test_comparison():
    assert 10 > 5
    assert 3 <= 3


def test_membership():
    assert "a" in "apple"
    assert 2 in [1, 2, 3]
    assert "key" in {"key": "value"}


def test_boolean():
    assert True
    assert not False


def test_none():
    assert None is None
