import csv
from pathlib import Path
def cal_div_with_no_exception(num1, num2):
    result = num1 / num2
    print(f"result from division of {num1} and {num2} is {result}")
    return result


def cal_div_with_exception(num1, num2):
    if num2 == 0:
        raise ValueError
    result = num1 / num2
    print(f"result from division of {num1} and {num2} is {result}")
    return result



if __name__ == "__main__":
    pass




