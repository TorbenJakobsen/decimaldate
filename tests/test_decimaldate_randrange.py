import pytest

from decimaldate import DecimalDate, DecimalDateRange


def test_randrange_ident_raises_value_error() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2014_02_14)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd, dd)


def test_randrange_step_0_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd1, dd2, 0)
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd2, dd1, 0)


def test_randrange_pos_dir_pos_step_is_ok() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    _ = DecimalDate.randrange(dd1, dd2, 1)


def test_randrange_pos_dir_neg_step_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd1, dd2, -1)


def test_randrange_neg_dir_pos_step_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd2, dd1, 1)


def test_randrange_neg_dir_neg_step_is_ok() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    _ = DecimalDate.randrange(dd2, dd1, -1)
