import pytest

from decimaldate import DecimalDateRange


@pytest.mark.parametrize(
    "arg,div,expected",
    [
        pytest.param(7, 1, 7),
        pytest.param(7, 2, 6),
        pytest.param(7, 3, 6),
        pytest.param(7, 4, 4),
        pytest.param(7, 5, 5),
        pytest.param(7, 6, 6),
        pytest.param(7, 7, 7),
        pytest.param(7, 8, 0),
    ],
)
def test_highest_multiple_of(arg, div, expected) -> None:
    assert DecimalDateRange._DecimalDateRange__highest_multiple_of(arg, div) == expected
