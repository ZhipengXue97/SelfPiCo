# Extracted from https://stackoverflow.com/questions/37835179/how-can-i-specify-the-function-type-in-my-type-hints
def f(my_function: type(abs)) -> int:
    return my_function(100)

