# Extracted from https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
#!/usr/bin/env python3
import os, pkgutil, importlib, inspect

class ArgBaseClass():
    # Assign all keyword arguments as properties on self, and keep the kwargs for later.
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        for (k, v) in kwargs.items():
            setattr(self, k, v)
        ms = inspect.getmembers(self, predicate=inspect.ismethod)
        self.methods = dict([(n, m) for (n, m) in ms if not n.startswith('_')])

    # Add the names of the methods to a parser object.
    def _parse_arguments(self, parser):
        parser.add_argument('method', choices=list(self.methods))
        return parser

    # Instantiate one of each of the subclasses of this class.
    def load_subclasses(self):
        module_dir = os.path.dirname(__file__)
        module_name = os.path.basename(os.path.normpath(module_dir))
        parent_class = self.__class__
        modules = {}
        # Load all the modules it the package:
        for (module_loader, name, ispkg) in pkgutil.iter_modules([module_dir]):
            modules[name] = importlib.import_module('.' + name, module_name)

        # Instantiate one of each class, passing the keyword arguments.
        ret = {}
        for cls in parent_class.__subclasses__():
            path = cls.__module__.split('.')
            ret[path[-1]] = cls(**self._kwargs)
        return ret

