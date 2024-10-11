# Extracted from https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given-but-i-only-pa
my_object.method("foo")

MyClass.method(my_object, "foo")

class MyNewClass:

    def method(self, arg):
        print(self)
        print(arg)

my_new_object = MyNewClass()
my_new_object.method("foo")
foo

class MyOtherClass:

    @staticmethod
    def method(arg):
        print(arg)

my_other_object = MyOtherClass()
my_other_object.method("foo")
foo

