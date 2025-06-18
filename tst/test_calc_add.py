import pytest
import src.calc_add as calculator_add


def test_calc_add_posetive():
    result = calculator_add.cal_add(10, 100)
    assert result == 110


def test_calc_add_one_posetive():
    result = calculator_add.cal_add(-10, 100)
    assert result == 90


def test_calc_add_one():
    result = calculator_add.cal_add(1, 100)
    assert result == 101


def test_calc_add_negative():
    result = calculator_add.cal_add(-10, -100)
    assert result == -110


def test_calc_add_zero():
    result = calculator_add.cal_add(0, -100)
    assert result == -100
