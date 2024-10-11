# Extracted from https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it
class MyClass:
  i = 123456
  def f(self):
    return "hello world"

b = MyClass()
b.c = MyClass()
setattr(b.c, 'test', 123)
b.c.test

