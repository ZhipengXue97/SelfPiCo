# Extracted from https://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python
class Exampleclass(object):
  def __init__(self, **kwargs):
    for k in kwargs.keys():
       if k in [acceptable_keys_list]:
          self.__setattr__(k, kwargs[k])

