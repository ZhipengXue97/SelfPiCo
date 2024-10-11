from .Logging import logger
from .Hyperparams import Hyperparams as params
from torch import Tensor
from numpy import ndarray, array
from pandas import DataFrame

def abstract_value(value):
    t = type(value)
    # common primitive values
    if value is None:
        abstract_value = "None"
    elif t is bool:
        abstract_value = "Boolean"
    # strings
    elif t is str:
        abstract_value = "String"
    # built-in numeric types
    elif t is int:
        abstract_value = "Integer"
    elif t is float:
        abstract_value = "Float"
    # built-in sequence types
    elif t is list:
        abstract_value = "List"
    elif t is tuple:
        abstract_value = "Tuple"
    # built-in set and dict types
    elif t is set:
        abstract_value = "Set"
    elif t is dict:
        abstract_value = "Dictionary"
    # Third-party types
    elif t is Tensor:
        abstract_value = "Tensor"
    elif t is ndarray:
        abstract_value = "Array"
    elif t is DataFrame:
        abstract_value = "DataFrame"
    # functions and methods
    elif callable(value):
        if hasattr(value, "__enter__") and hasattr(value, "__exit__"):
            abstract_value = "resource"
        else:
            abstract_value = "Callable"
    # all other types
    else:
        abstract_value = "Object"

    return abstract_value


class DummyResource(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        return True
    
    def read(self):
        return "a"
    
    def readlines(self):
        return ['a']

    def write(self):
        pass


class DummyObject():
    def __init__(self, *a, **b):
        pass
    def __call__(self, *args, **kwargs):
        pass
    def __iter__(self):
        yield from [1]
    def __next__(self):
        return 1
    def __len__(self):
        return len([1])
    def __contains__(self, item):
        return True



def restore_value(abstract_value):
    # common primitive values
    if abstract_value == "None":
        return None
    elif abstract_value == "Boolean":
        return True
    # strings
    elif abstract_value == "String":
        return "a"
    # built-in numeric types
    elif abstract_value == "Integer":
        return 1
    elif abstract_value == "Float":
        return 1.0
    # built-in sequence types
    elif abstract_value == "List":
        return [DummyObject()]
    elif abstract_value == "Tuple":
        return (DummyObject(),)
    # built-in set and dict types
    elif abstract_value == "Set":
        return {DummyObject()}
    elif abstract_value == "Dictionary":
        return {"a": DummyObject()}
    # Third-party types
    elif abstract_value == "Tensor":
        return Tensor([[1.0]])
    elif abstract_value == "Array":
        return array([1])
    elif abstract_value == "DataFrame":
        return DataFrame({"a": [1]})
    # functions and methods
    elif abstract_value == "Resource":
        return DummyResource()
    elif abstract_value == "Callable":
        return DummyObject
    elif abstract_value == "Object":
        return DummyObject()
    # all other types
    else:
        logger.info("Unknown abstract value: %s", abstract_value)
        return DummyObject()

