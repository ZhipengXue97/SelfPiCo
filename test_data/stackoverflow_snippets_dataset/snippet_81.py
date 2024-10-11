# Extracted from https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python
with elapsed_timer() as elapsed:
    # some lengthy code
    print( "midpoint at %.2f seconds" % elapsed() )  # time so far
    # other lengthy code

print( "all done at %.2f seconds" % elapsed() )

from contextlib import contextmanager
from timeit import default_timer

@contextmanager
def elapsed_timer():
    start = default_timer()
    elapser = lambda: default_timer() - start
    yield lambda: elapser()
    end = default_timer()
    elapser = lambda: end-start

import time

with elapsed_timer() as elapsed:
    time.sleep(1)
    print(elapsed())
    time.sleep(2)
    print(elapsed())
    time.sleep(3)

