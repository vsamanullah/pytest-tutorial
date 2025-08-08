def add(num1,num2):
    return num1 + num2

def div(num1,num2):
    if(num2 == 0):
        raise ValueError
    return num1 / num2