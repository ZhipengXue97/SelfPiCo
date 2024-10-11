# Extracted from https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
class Example(object):

    def regular_instance_method(self):
        """A function of an instance has access to every attribute of that 
        instance, including its class (and its attributes.)
        Not accepting at least one argument is a TypeError.
        Not understanding the semantics of that argument is a user error.
        """
        return some_function_f(self)

    @classmethod
    def a_class_method(cls):
        """A function of a class has access to every attribute of the class.
        Not accepting at least one argument is a TypeError.
        Not understanding the semantics of that argument is a user error.
        """
        return some_function_g(cls)

    @staticmethod
    def a_static_method():
        """A static method has no information about instances or classes
        unless explicitly given. It just lives in the class (and thus its 
        instances') namespace.
        """
        return some_function_h()

some_function_h = some_function_g = some_function_f = lambda x=None: x

instance = Example()
instance.regular_instance_method 

instance.regular_instance_method()

instance = Example()
instance.regular_instance_method()

instance.a_class_method()
Example.a_class_method()

print(instance.a_static_method())
None

def function(x, y, z): ...

def function(y, z): ...

def function(z): ...

def an_instance_method(self, arg, kwarg=None):
    cls = type(self)             # Also has the class of instance!
    ...

@classmethod
def a_class_method(cls, arg, kwarg=None):
    ...

@staticmethod
def a_static_method(arg, kwarg=None):
    ...

'abc'.translate(str.maketrans({'a': 'b'}))
'bbc'

dict.fromkeys('abc')
{'a': None, 'c': None, 'b': None}

class MyDict(dict): pass
type(MyDict.fromkeys('abc'))

