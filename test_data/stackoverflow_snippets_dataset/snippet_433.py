# Extracted from https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
class MyClass:
    def __init__(self, public_read_variable, private_variable):
        self.public_read_variable_ = public_read_variable
        self.__private_variable = private_variable

my_class = MyClass("public", "private")
print(my_class.public_read_variable_) # OK
my_class.public_read_variable_ = 'another value' # NOT OK, don't do that.

