# Extracted from https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
class MyClass:
    @classmethod
    def make_new(cls) -> __qualname__:
        return cls()

