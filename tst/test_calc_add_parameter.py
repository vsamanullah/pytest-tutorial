import pytest
import csv
from pathlib import Path
import src.calc_add as calculator_add

def read_test_data_from_csv():
    csv_file = Path("testdata/test_add_data.csv")
    reader = {}
    test_data = []
    with csv_file.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_data.append((int(row['num1']), int(row['num2']), int(row['expected'])))
    return test_data


@pytest.mark.parametrize("num1,num2,expected", read_test_data_from_csv() )
def test_calc_add_csv(num1, num2, expected):
    result = calculator_add.cal_add(num1, num2)
    assert result == expected


@pytest.mark.parametrize("num1,num2,expected",
                         [(10, 100, 110), (-10, 100, 90), (1, 100, 101), (-10, -100, -110), (0, -100, -100)])
def test_calc_add(num1, num2, expected):
    result = calculator_add.cal_add(num1, num2)
    assert result == expected
