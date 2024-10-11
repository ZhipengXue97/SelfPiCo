# Extracted from https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class
method_list = [func for func in dir(Foo) if callable(getattr(Foo, func))]

method_list = [func for func in dir(Foo) if callable(getattr(Foo, func)) and not func.startswith("__")]

