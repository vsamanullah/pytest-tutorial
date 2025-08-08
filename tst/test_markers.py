import sys

import src.calculator as calc
import pytest
import csv
from pathlib import Path
'''
Test for both +ve
Test for both -ve
Test for one +ve and -ve
Test with 0
Test with 1
'''

def read_test_data_from_csv():
    csv_file = Path("testdata/test_add_data.csv")
    reader = {}
    test_data = []
    with csv_file.open() as file_hand:
        reader = csv.DictReader(file_hand)
        for row in reader:
            test_data.append((int(row['num1']), int(row['num2']), int(row['expected'])))
    return test_data

#@pytest.mark.parametrize("num1,num2,expected" , [(20,10,30) , (-10 , -20 , -30) , (10 , -5 , 5) , (0 , 5 , 5) , (1 , 5 , 6)])
@pytest.mark.parametrize("num1,num2,expected" , read_test_data_from_csv())
def test_add_parameters_from_csv(num1,num2,expected):
    result = calc.add(num1, num2)
    # print(f"result of test_add is {result}")
    assert result == expected

@pytest.mark.parametrize("num1,num2,expected" , [(20,10,30) , (-10 , -20 , -30) , (10 , -5 , 5) , (0 , 5 , 5) , (1 , 5 , 6)])
def test_add_parameters_inline(num1,num2,expected):
    result = calc.add(num1, num2)
    # print(f"result of test_add is {result}")
    assert result == expected

@pytest.mark.smoke
def test_add_zero():
    result = calc.add(10,0)
    #print(f"result of test_add_zero is {result}")
    assert result==10

@pytest.mark.skip
def test_add_negative():
    result = calc.add(10,-2)
    #print(f"result of test_add_negative is {result}")
    assert result==8

