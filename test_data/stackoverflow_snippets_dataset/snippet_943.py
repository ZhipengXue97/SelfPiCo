# Extracted from https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
class Person:
    def test(self): # <- With "self" 
        print("Test")

Person.test() # Here

class Person:
    @staticmethod
    def test(self): # <- With "self" 
        print("Test")

obj = Person()
obj.test() # Here

# Or

Person.test() # Here

class Person:
    def test(self): # <- With "self" 
        print("Test")

obj = Person()
obj.test() # Here

class Person:
    @staticmethod
    def test(): # <- "self" removed 
        print("Test")

obj = Person()
obj.test() # Here

# Or

Person.test() # Here

Test

