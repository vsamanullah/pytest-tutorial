import pytest
import src.calc_div as calculator_div


class TestCalcDivClass:
    def test_calc_div_posetive_no_exp(self):
        result = calculator_div.cal_div_with_no_exception(100, 10)
        assert result == 10

    def test_calc_div_one_posetive_no_exp(self):
        result = calculator_div.cal_div_with_no_exception(100, -10)
        assert result == -10

    def test_calc_div_add_one_no_exp(self):
        result = calculator_div.cal_div_with_no_exception(10, 1)
        assert result == 10

    def test_calc_div_negative_no_exp(self):
        result = calculator_div.cal_div_with_no_exception(-100, -10)
        assert result == 10

    def test_calc_div_zero_no_exp(self):
        with pytest.raises(ZeroDivisionError):
            result = calculator_div.cal_div_with_no_exception(100, 0)
        assert True