from app.services.calculator_service import is_leap_year
import pytest


def test_leap_true():
    assert is_leap_year(2000) is True
    assert is_leap_year(2024) is True


def test_leap_false():
    assert is_leap_year(1900) is False
    assert is_leap_year(2019) is False


def test_invalid_year_raises():
    with pytest.raises(ValueError):
        is_leap_year(0)
    with pytest.raises(ValueError):
        is_leap_year(-100)
