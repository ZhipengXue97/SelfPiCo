# Extracted from https://stackoverflow.com/questions/2675028/list-attributes-of-an-object
import json

def get_info(obj):

  type_name = type(obj).__name__
  print('Value is of type {}!'.format(type_name))
  prop_names = dir(obj)

  for prop_name in prop_names:
    prop_val = getattr(obj, prop_name)
    prop_val_type_name = type(prop_val).__name__
    print('{} has property "{}" of type "{}"'.format(type_name, prop_name, prop_val_type_name))

    try:
      val_as_str = json.dumps([ prop_val ], indent=2)[1:-1]
      print('  Here\'s the {} value: {}'.format(prop_name, val_as_str))
    except:
      pass

get_info(None)
get_info('hello')

import numpy
get_info(numpy)
# ... etc.

