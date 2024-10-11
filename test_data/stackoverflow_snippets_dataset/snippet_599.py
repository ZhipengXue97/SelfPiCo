# Extracted from https://stackoverflow.com/questions/6886493/get-all-object-attributes-in-python
class MyObj(object):
  def __init__(self):
    self.name = 'Chuck Norris'
    self.phone = '+6661'

obj = MyObj()
print(obj.__dict__)
print(dir(obj))

# Output:  
# obj.__dict__ --> {'phone': '+6661', 'name': 'Chuck Norris'}
#
# dir(obj)     --> ['__class__', '__delattr__', '__dict__', '__doc__',
#               '__format__', '__getattribute__', '__hash__', 
#               '__init__', '__module__', '__new__', '__reduce__', 
#               '__reduce_ex__', '__repr__', '__setattr__', 
#               '__sizeof__', '__str__', '__subclasshook__', 
#               '__weakref__', 'name', 'phone']

