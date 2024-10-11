# Extracted from ./data/repos/flask/src/flask/config.py
if obj is None:
    exit(self)
rv = obj.config[self.__name__]
if self.get_converter is not None:
    rv = self.get_converter(rv)
exit(rv)
