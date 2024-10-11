# Extracted from https://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-arguments
import script1

for i in range(whatever):
    script1.some_function(i)

import contextlib
@contextlib.contextmanager
def redirect_argv(num):
    sys._argv = sys.argv[:]
    sys.argv=[str(num)]
    yield
    sys.argv = sys._argv

with redirect_argv(1):
    print(sys.argv)

