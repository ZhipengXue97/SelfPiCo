# Extracted from https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
class Abstract1:
    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def aMethod(self):
        raise NotImplementedError("Should have implemented this")

class SomeAbstraction:
    pass  # lots of stuff - but missing something

class Mixin1:
    def something(self):
        pass  # one implementation

class Mixin2:
    def something(self):
        pass  # another

class Concrete1(SomeAbstraction, Mixin1):
    pass

class Concrete2(SomeAbstraction, Mixin2):
    pass

