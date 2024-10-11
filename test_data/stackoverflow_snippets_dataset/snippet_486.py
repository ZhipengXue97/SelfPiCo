# Extracted from https://stackoverflow.com/questions/5929107/decorators-with-parameters
from numbers import Number

def multiply(num=1):
    def _multiply(func):
        def core(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(num, Number):
                return result * num
            else:
                return result
        return core
    if callable(num):
        return _multiply(num)
    else:
        return _multiply

def sum(num1, num2):
    return num1 + num2

# (4 + 6) x 5 = 50

@multiply(5) # Here
def sum(num1, num2):
    return num1 + num2

result = sum(4, 6)
print(result)

50

# (4 + 6) x 1 = 10

@multiply() # Here
def sum(num1, num2):
    return num1 + num2
    
result = sum(4, 6)
print(result)

# 4 + 6 = 10

@multiply # Here
def sum(num1, num2):
    return num1 + num2
    
result = sum(4, 6)
print(result)

10

