# Extracted from https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes
class Test:
   def hello(self, name):
      print ('hello ', name)

obj = Test()
obj.hello('Rahul')

class Test:
       def hello(cls, name):
          print ('hello ', name)


Test.hello('Rahul')

