# Extracted from https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
from dataclasses import dataclass

@dataclass(frozen=True)
class _Const:
    SOME_STRING = 'some_string'
    SOME_INT = 5
    
Const = _Const()

# In another file import Const and try
print(Const.SOME_STRING)  # ITS OK!
Const.SOME_INT = 6  # dataclasses.FrozenInstanceError: cannot assign to field 'SOME_INT'

