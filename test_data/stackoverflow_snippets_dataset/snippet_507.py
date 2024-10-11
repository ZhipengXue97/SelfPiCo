# Extracted from https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
def get_object_functions(object_):
    functions = [attr_name
                 for attr_name in dir(object_)
                 if str(type(getattr(object_,
                                     attr_name))) in ("<class 'function'>",
                                                      "<class 'method'>")]
    return functions

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'My name is {self.name}')

    @staticmethod
    def say_hi():
        print('hi')

    @classmethod
    def reproduce(cls, name):
        return cls(name, 0)


person = Person('Rafael', 27)
print(get_object_functions(person))


['__init__', 'introduce', 'reproduce', 'say_hi']

