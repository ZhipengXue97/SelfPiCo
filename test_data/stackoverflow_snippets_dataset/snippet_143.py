# Extracted from https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
hasattr(1, "__len__")
False
hasattr(1.3, "__len__")
False
hasattr("a", "__len__")
True
hasattr([1,2,3], "__len__")
True
hasattr({1,2}, "__len__")
True
hasattr({"a":1}, "__len__")
True
hasattr(("a", 1), "__len__")
True

import types
types.GeneratorType
gen = (i for i in range(10))
isinstance(gen, types.GeneratorType)
True

