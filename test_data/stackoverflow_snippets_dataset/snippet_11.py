# Extracted from https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
class A:
    def foo():  # no self parameter, no decorator
        pass

class B:
    @staticmethod
    def foo():  # no self parameter
        pass

A.foo()
TypeError
A().foo()
TypeError
B.foo()
B().foo()

A.foo()
A().foo()
TypeError
B.foo()
B().foo()

