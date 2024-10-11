# Extracted from https://stackoverflow.com/questions/5626193/what-is-monkey-patching
import pandas as pd
def just_foo_cols(self):
    """Get a list of column names containing the string 'foo'

    """
    return [x for x in self.columns if 'foo' in x]

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class
df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
df.just_foo_cols()
del pd.DataFrame.just_foo_cols # you can also remove the new method

import pandas as pd

def just_foo_cols(self):
    """Get a list of column names containing the string 'foo'

    """
    return [x for x in self.columns if 'foo' in x]

pd.DataFrame.just_foo_cols = just_foo_cols # monkey-patch the DataFrame class

df = pd.DataFrame([list(range(4))], columns=["A","foo","foozball","bar"])
df.just_foo_cols()
del pd.DataFrame.just_foo_cols # you can also remove the new method

import datasource

def get_data(self):
    '''monkey patch datasource.Structure with this to simulate error'''
    raise datasource.DataRetrievalError

datasource.Structure.get_data = get_data

def setUp(self):
    # retain a pointer to the actual real method:
    self.real_get_data = datasource.Structure.get_data
    # monkey patch it:
    datasource.Structure.get_data = get_data

def tearDown(self):
    # give the real method back to the Structure object:
    datasource.Structure.get_data = self.real_get_data

