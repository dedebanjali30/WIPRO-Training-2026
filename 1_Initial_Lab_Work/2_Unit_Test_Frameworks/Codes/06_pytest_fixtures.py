import pytest


@pytest.fixture
def numbers():
    return 10, 5


def test_addition(numbers):
    a, b = numbers
    assert a + b == 15


def test_subtraction(numbers):
    a, b = numbers
    assert a - b == 5