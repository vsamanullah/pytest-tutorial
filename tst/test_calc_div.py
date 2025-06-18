import pytest
import src.calc_div as calculator_div

def test_calc_div_posetive():
    result = calculator_div.cal_div_with_no_exception(100, 10)
    assert result == 10


def test_calc_div_one_posetive():
    result = calculator_div.cal_div_with_no_exception(100, -10)
    assert result == -10


def test_calc_div_add_one():
    result = calculator_div.cal_div_with_no_exception(10,1)
    assert result == 10


def test_calc_div_negative():
    result = calculator_div.cal_div_with_no_exception(-100, -10)
    assert result == 10


def test_calc_div_zero():
    with pytest.raises(ZeroDivisionError):
        result = calculator_div.cal_div_with_no_exception(100,0)
    assert True


def test_calc_div_zero_exception():
    with pytest.raises(ValueError):
        result = calculator_div.cal_div_with_exception(100,0)
    assert True