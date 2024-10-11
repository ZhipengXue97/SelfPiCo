# Extracted from https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
class Foo:
    x = 1
  
    @classmethod
    def increment(cls, y=1):
        cls.x += y

