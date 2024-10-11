# Extracted from https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
from importlib import reload  # Python 3.4+
import foo

while True:
    # Do some things.
    if is_changed(foo):
        foo = reload(foo)

