import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 15),
        (20, 10, 30),
        (5, 5, 10),
        (100, 50, 150)
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected