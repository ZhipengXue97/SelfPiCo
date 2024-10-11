# Extracted from https://stackoverflow.com/questions/890128/how-are-lambdas-useful
import imported.module

def func():
    return lambda: imported.module.method("foo", "bar")

import imported.module

def func():
    def cb():
        return imported.module.method("foo", "bar")
    return cb

